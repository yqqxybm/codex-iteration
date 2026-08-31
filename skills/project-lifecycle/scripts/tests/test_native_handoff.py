import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "native_handoff.py"
SPEC = importlib.util.spec_from_file_location("native_handoff", SCRIPT)
handoff = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(handoff)


class NativeHandoffTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "src").mkdir()
        (self.root / "src" / "existing.py").write_text("pass\n")
        self.request = {
            "task_id": "implementation",
            "task_name": "bounded_change",
            "agent_owner": "implementation_owner",
            "agent_type": "worker",
            "model": "explicit-model",
            "reasoning_effort": "high",
            "route_reason": "A bounded implementation with path checks.",
            "scope_root": str(self.root),
            "owned_scope": ["src/"],
            "write_policy": "same_worktree_disjoint",
            "analysis_gate": "project_analysis_consumed",
            "analysis_gate_basis": "Implement a stateless helper; preserve parent authority.",
            "task": "Implement the assigned helper for native task handoff.",
            "done_when": "The requested tests pass.",
            "verification": "Run the focused unittest suite.",
        }

    def prepared(self, **updates):
        request = dict(self.request, **updates)
        return handoff.prepare(request)

    def receipt(self, contract, **updates):
        return dict({
            "assignment_id": contract["assignment_id"],
            "status": "done",
            "changed_files": ["src/new.py"],
            "result": "Implemented the stateless helper.",
            "verification": "Ran unittest: 12 tests passed.",
            "new_work": [],
        }, **updates)

    def rejected(self, contract, **updates):
        with self.assertRaises(handoff.HandoffError):
            handoff.check(contract, self.receipt(contract, **updates))

    def test_prepare_identity_and_self_contained_spawn_args(self):
        first, second = self.prepared(), self.prepared()
        contract, args = first["contract"], first["spawn_args"]
        self.assertNotEqual(contract["assignment_id"], second["contract"]["assignment_id"])
        self.assertNotEqual(contract["execution_owner_id"], second["contract"]["execution_owner_id"])
        self.assertEqual(contract["forbidden_scope"], [])
        for field in ("task_name", "agent_type", "model", "reasoning_effort"):
            self.assertEqual(args[field], self.request[field])
        self.assertEqual(args["fork_turns"], "none")
        for field in ("assignment_id", "execution_owner_id", "agent_owner", "task_id",
                      "scope_root", "task", "done_when", "verification", "analysis_gate_basis"):
            self.assertIn(contract[field], args["message"])
        self.assertEqual(set(args), {"task_name", "agent_type", "model", "reasoning_effort",
                                     "fork_turns", "message"})

    def test_missing_explicit_model_or_effort(self):
        for field in ("model", "reasoning_effort"):
            for value in (None, "", "  "):
                with self.subTest(field=field, value=value), self.assertRaises(handoff.HandoffError):
                    self.prepared(**{field: value})
            request = dict(self.request)
            del request[field]
            with self.assertRaises(handoff.HandoffError):
                handoff.prepare(request)

    def test_invalid_request_types_and_values(self):
        for field, value in (("agent_type", "manager"), ("agent_type", []),
                             ("reasoning_effort", "automatic"), ("model", True),
                             ("owned_scope", []), ("owned_scope", "src/"),
                             ("forbidden_scope", None), ("task", {}),
                             ("analysis_gate_basis", "TODO"),
                             ("write_policy", "shared"), ("task_name", "bad-name")):
            with self.subTest(field=field, value=value), self.assertRaises(handoff.HandoffError):
                self.prepared(**{field: value})
        for request in (None, [], "request"):
            with self.assertRaises(handoff.HandoffError):
                handoff.prepare(request)

    def test_analysis_gate_and_role_compatibility(self):
        for role in ("explorer", "reviewer"):
            with self.assertRaises(handoff.HandoffError):
                self.prepared(agent_type=role)
            self.prepared(agent_type=role, write_policy="read_only", analysis_gate="not_required_read_only")
        with self.assertRaises(handoff.HandoffError):
            self.prepared(analysis_gate="not_required_read_only")
        for gate in ("project_analysis_consumed", "explicitly_skipped_by_user",
                     "not_required_very_small"):
            self.prepared(write_policy="single_writer", analysis_gate=gate)

    def test_read_only_can_preserve_prior_analysis_gate(self):
        for role in ("explorer", "reviewer", "worker"):
            for gate in ("not_required_read_only", "project_analysis_consumed",
                         "explicitly_skipped_by_user", "not_required_very_small"):
                with self.subTest(role=role, gate=gate):
                    contract = self.prepared(agent_type=role, write_policy="read_only",
                                             analysis_gate=gate)["contract"]
                    self.assertEqual(contract["analysis_gate"], gate)
                    self.assertTrue(handoff.check(contract, self.receipt(
                        contract, changed_files=[]))["valid"])
                    self.rejected(contract)

    def test_unknown_request_and_contract_fields_are_rejected(self):
        for field, value in (("forbidden_scopes", ["src/private/"]),
                             ("assignment_id", "injected-assignment"),
                             ("execution_owner_id", "injected-owner"), ("unexpected", True)):
            with self.subTest(field=field), self.assertRaises(handoff.HandoffError):
                self.prepared(**{field: value})
        contract = self.prepared()["contract"]
        for field, value in (("forbidden_scopes", ["src/private/"]), ("unexpected", True)):
            invalid = dict(contract, **{field: value})
            with self.subTest(field=field), self.assertRaises(handoff.HandoffError):
                handoff.check(invalid, self.receipt(contract))

    def test_scope_root_requires_existing_absolute_directory(self):
        for root in ("relative", str(self.root / "missing"), str(self.root / "src/existing.py")):
            with self.subTest(root=root), self.assertRaises(handoff.HandoffError):
                self.prepared(scope_root=root)

    def test_valid_receipt_is_linked_without_parent_acceptance(self):
        contract = self.prepared()["contract"]
        checked = handoff.check(contract, self.receipt(contract))
        self.assertEqual(checked["task_id"], contract["task_id"])
        self.assertEqual(checked["agent_owner"], contract["agent_owner"])
        self.assertEqual(checked["execution_owner_id"], contract["execution_owner_id"])
        self.assertTrue(checked["valid"])
        self.assertFalse(checked["parent_acceptance"])
        self.assertEqual(checked["changed_files"], ["src/new.py"])

    def test_wrapped_receipt(self):
        contract = self.prepared()["contract"]
        self.assertTrue(handoff.check(contract, {"subagent_receipt": self.receipt(contract)})["valid"])

    def test_receipt_and_wrapper_require_exact_fields(self):
        contract = self.prepared()["contract"]
        for field, value in (("execution_owner_id", "wrong-owner"), ("status_typo", "failed"),
                             ("changed_file", ["outside.py"]), ("unexpected", True)):
            invalid = self.receipt(contract, **{field: value})
            for receipt in (invalid, {"subagent_receipt": invalid}):
                with self.subTest(field=field), self.assertRaises(handoff.HandoffError):
                    handoff.check(contract, receipt)
        for field, value in (("assignment_id", "wrong-assignment"), ("status", "failed"),
                             ("unexpected", True)):
            wrapper = {"subagent_receipt": self.receipt(contract), field: value}
            with self.subTest(field=field), self.assertRaises(handoff.HandoffError):
                handoff.check(contract, wrapper)

    def test_new_work_entries_require_nonempty_text_or_object(self):
        contract = self.prepared()["contract"]
        for item in (None, 0, 1, 1.5, True, False, [], ["nested"], {}, "", "  "):
            with self.subTest(item=item):
                self.rejected(contract, new_work=[item])
        new_work = ["Review another scope with the parent.", {"task": "Review related docs."}]
        checked = handoff.check(contract, self.receipt(contract, new_work=new_work))
        self.assertEqual(checked["new_work"], new_work)

    def test_wrong_id_and_status(self):
        contract = self.prepared()["contract"]
        for assignment_id in ("another-assignment", "", None, []):
            self.rejected(contract, assignment_id=assignment_id)
        for status in ("complete", "", None, [], True):
            self.rejected(contract, status=status)
        for status in ("done", "blocked", "failed", "out_of_scope"):
            self.assertTrue(handoff.check(contract, self.receipt(contract, status=status))["valid"])

    def test_missing_empty_or_wrong_receipt_fields(self):
        contract = self.prepared()["contract"]
        for field in self.receipt(contract):
            receipt = self.receipt(contract)
            del receipt[field]
            with self.subTest(missing=field), self.assertRaises(handoff.HandoffError):
                handoff.check(contract, receipt)
        for field, value in (("changed_files", "src/new.py"), ("changed_files", [None]),
                             ("result", {}), ("verification", []), ("new_work", {}),
                             ("result", ""), ("verification", "  "),
                             ("result", "TODO"), ("verification", "<verification>")):
            self.rejected(contract, **{field: value})
        for receipt in ({}, [], {"subagent_receipt": {}}, {"subagent_receipt": []}):
            with self.assertRaises(handoff.HandoffError):
                handoff.check(contract, receipt)

    def test_non_done_may_have_no_completed_result_or_verification(self):
        contract = self.prepared()["contract"]
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, status="blocked", changed_files=[], result="", verification=""))["valid"])

    def test_read_only_rejects_any_reported_write(self):
        contract = self.prepared(agent_type="reviewer", write_policy="read_only",
                                 analysis_gate="not_required_read_only")["contract"]
        self.rejected(contract)
        self.assertTrue(handoff.check(contract, self.receipt(contract, changed_files=[]))["valid"])

    def test_bad_paths_rejected_in_receipt_and_scope(self):
        contract = self.prepared()["contract"]
        for path in ("/tmp/file.py", "../file.py", "src/../file.py", "src/../../file.py",
                     "src/\x00file", "", "  ", "C:\\tmp\\file.py", "C:/tmp/file.py"):
            with self.subTest(path=path):
                self.rejected(contract, changed_files=[path])
                with self.assertRaises(handoff.HandoffError):
                    self.prepared(owned_scope=[path])

    def test_directory_receipts_rejected(self):
        contract = self.prepared(owned_scope=["."])["contract"]
        for path in (".", "src", "src/", "src/new/"):
            self.rejected(contract, changed_files=[path])
        with self.assertRaises(handoff.HandoffError):
            self.prepared(owned_scope=["src"])
        with self.assertRaises(handoff.HandoffError):
            self.prepared(owned_scope=["src/existing.py/"])

    def test_non_directory_parent_is_rejected(self):
        contract = self.prepared()["contract"]
        self.rejected(contract, changed_files=["src/existing.py/child.py"])
        with self.assertRaises(handoff.HandoffError):
            self.prepared(owned_scope=["src/existing.py/child.py"])

    def test_nonexistent_paths_and_exact_file_scope(self):
        contract = self.prepared(owned_scope=["future/new.py"])["contract"]
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, changed_files=["future/new.py"]))["valid"])
        self.rejected(contract, changed_files=["future/new.py/child"])
        self.rejected(contract, changed_files=["future/new.py.bak"])
        subtree = self.prepared(owned_scope=["future/"])["contract"]
        self.assertTrue(handoff.check(subtree, self.receipt(
            subtree, changed_files=["future/deep/new.py"]))["valid"])

    def test_owned_and_forbidden_boundaries(self):
        contract = self.prepared(forbidden_scope=["src/private/", "src/secret.py"])["contract"]
        for path in ("outside.py", "src-other/new.py", "src/private/new.py", "src/secret.py"):
            self.rejected(contract, changed_files=[path])
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, changed_files=["src/secret.py.bak"]))["valid"])
        contract = self.prepared(forbidden_scope=["."])["contract"]
        self.rejected(contract)

    def test_canonical_paths_and_duplicate_identity(self):
        contract = self.prepared(owned_scope=["./src//"])["contract"]
        self.assertEqual(contract["owned_scope"], ["src/"])
        checked = handoff.check(contract, self.receipt(contract, changed_files=["./src//new.py"]))
        self.assertEqual(checked["changed_files"], ["src/new.py"])
        self.rejected(contract, changed_files=["src/new.py", "./src/new.py"])

    def test_600_distinct_names_do_not_require_pairwise_identity_checks(self):
        names = ["src/file_{:04d}.py".format(index) for index in range(600)]
        with mock.patch.object(handoff, "_path", side_effect=lambda root, value, field, **kwargs: value), \
                mock.patch.object(handoff, "_same_scope", return_value=False) as comparisons:
            self.assertEqual(handoff._paths(self.root, names, "changed_files"), names)
            self.assertLessEqual(comparisons.call_count, len(names),
                                 "Distinct names must not incur all-pairs identity comparisons.")

    def test_600_existing_files_reuse_directory_reads_within_one_call(self):
        names = ["src/file_{:04d}.py".format(index) for index in range(600)]
        for name in names:
            (self.root / name).write_text("pass\n")
        with mock.patch.object(handoff.os, "listdir", wraps=os.listdir) as reads, \
                mock.patch.object(handoff, "_same_scope", wraps=handoff._same_scope) as comparisons:
            self.assertEqual(handoff._paths(self.root, names, "changed_files"), names)
            self.assertLessEqual(comparisons.call_count, len(names))
            self.assertLessEqual(reads.call_count, len(self.root.parts) + 2,
                                 "Common directories must not be rescanned for each file.")

    def test_unrelated_ascii_names_need_no_disk_identity_comparison(self):
        (self.root / "src/protected.txt").write_text("protected\n")
        with mock.patch.object(handoff, "_disk_spelling", wraps=handoff._disk_spelling) as disk_lookups:
            self.assertFalse(handoff._same_parts(self.root, ("src", "existing.py"),
                                                  ("src", "protected.txt")))
            self.assertEqual(disk_lookups.call_count, 0)

    def require_case_insensitive(self):
        if not (self.root / "SRC/EXISTING.PY").exists():
            self.skipTest("This test requires a case-insensitive filesystem.")

    def test_case_alias_cannot_bypass_exact_forbidden_scope(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["."], forbidden_scope=["src/existing.py"])["contract"]
        self.rejected(contract, changed_files=["SRC/EXISTING.PY"])

    def test_case_alias_cannot_bypass_forbidden_subtree(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["."], forbidden_scope=["src/"])["contract"]
        self.rejected(contract, changed_files=["SRC/EXISTING.PY"])
        self.rejected(contract, changed_files=["SRC/MISSING.PY"])

    def test_existing_case_alias_uses_actual_disk_spelling(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["SRC/EXISTING.PY"])["contract"]
        self.assertEqual(contract["owned_scope"], ["src/existing.py"])
        checked = handoff.check(contract, self.receipt(contract, changed_files=["SRC/EXISTING.PY"]))
        self.assertEqual(checked["changed_files"], ["src/existing.py"])

    def test_case_alias_lookup_handles_unrelated_dangling_symlink(self):
        self.require_case_insensitive()
        (self.root / "src/dangling").symlink_to("missing-target")
        contract = self.prepared(owned_scope=["SRC/EXISTING.PY"])["contract"]
        self.assertEqual(contract["owned_scope"], ["src/existing.py"])

    def test_case_alias_duplicate_existing_and_absent_files(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["."])["contract"]
        self.rejected(contract, changed_files=["src/existing.py", "SRC/EXISTING.PY"])
        self.rejected(contract, changed_files=["src/missing.py", "SRC/MISSING.PY"])
        for scopes in (["src/existing.py", "SRC/EXISTING.PY"], ["future.py", "FUTURE.PY"]):
            with self.subTest(scopes=scopes), self.assertRaises(handoff.HandoffError):
                self.prepared(owned_scope=scopes)

    def test_absent_and_deleted_case_aliases_obey_boundaries(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["."], forbidden_scope=["src/existing.py", "future/deep/"])["contract"]
        (self.root / "src/existing.py").unlink()
        self.rejected(contract, changed_files=["SRC/EXISTING.PY"])
        self.rejected(contract, changed_files=["FUTURE/DEEP/new.py"])
        owned = self.prepared(owned_scope=["src/existing.py"])["contract"]
        self.assertTrue(handoff.check(owned, self.receipt(
            owned, changed_files=["SRC/EXISTING.PY"]))["valid"])

    def test_creation_and_deletion_do_not_destabilize_case_contract(self):
        self.require_case_insensitive()
        contract = self.prepared(owned_scope=["src/new.py"])["contract"]
        (self.root / "src/NEW.PY").write_text("pass\n")
        checked = handoff.check(contract, self.receipt(contract, changed_files=["src/new.py"]))
        self.assertEqual(checked["changed_files"], ["src/NEW.PY"])
        (self.root / "src/NEW.PY").unlink()
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, changed_files=["SRC/NEW.PY"]))["valid"])

    def test_case_sensitive_distinct_files_keep_separate_meanings(self):
        if (self.root / "SRC/EXISTING.PY").exists():
            self.skipTest("This volume is case-insensitive; distinct case-sensitive files cannot be tested here.")
        (self.root / "src/EXISTING.PY").write_text("different\n")
        contract = self.prepared(owned_scope=["src/"], forbidden_scope=["src/existing.py"])["contract"]
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, changed_files=["src/EXISTING.PY"]))["valid"])
        owned = self.prepared(owned_scope=["src/existing.py"])["contract"]
        self.rejected(owned, changed_files=["src/EXISTING.PY"])
        both = self.prepared(owned_scope=["src/existing.py", "src/EXISTING.PY"])["contract"]
        self.assertTrue(handoff.check(both, self.receipt(
            both, changed_files=["src/existing.py", "src/EXISTING.PY"]))["valid"])

    @unittest.skipUnless(sys.platform == "darwin", "Darwin pathconf-specific failure handling")
    def test_case_probe_error_or_unknown_result_does_not_assume_semantics(self):
        contract = self.prepared(owned_scope=["src/missing.py"])["contract"]
        for options in ({"side_effect": OSError("probe failed")}, {"return_value": -1}):
            with self.subTest(options=options), mock.patch.object(handoff.os, "pathconf", **options):
                with self.assertRaises(handoff.HandoffError) as caught:
                    handoff.check(contract, self.receipt(contract, changed_files=["src/MISSING.PY"]))
                self.assertEqual(caught.exception.code, "unknown_case_semantics")

    def test_simulated_case_sensitive_missing_paths_remain_distinct(self):
        contract = self.prepared(owned_scope=["src/missing.py"])["contract"]
        with mock.patch.object(handoff, "_case_sensitive", return_value=True):
            self.rejected(contract, changed_files=["src/MISSING.PY"])
            separate = self.prepared(owned_scope=["src/missing.py", "src/MISSING.PY"])["contract"]
            self.assertTrue(handoff.check(separate, self.receipt(
                separate, changed_files=["src/missing.py", "src/MISSING.PY"]))["valid"])

    def test_unknown_missing_unicode_case_collation_is_rejected(self):
        contract = self.prepared(owned_scope=["src/\u00e4.py"])["contract"]
        with mock.patch.object(handoff, "_case_sensitive", return_value=False):
            with self.assertRaises(handoff.HandoffError) as caught:
                handoff.check(contract, self.receipt(contract, changed_files=["src/\u00c4.py"]))
            self.assertEqual(caught.exception.code, "ambiguous_identity")

    def test_chinese_filenames_remain_distinct_from_unrelated_forbidden_file(self):
        (self.root / "src/\u6d4b\u8bd5.py").write_text("pass\n")
        for protected_exists in (False, True):
            if protected_exists:
                (self.root / "src/protected.txt").write_text("protected\n")
            contract = self.prepared(owned_scope=["src/"], forbidden_scope=["src/protected.txt"])["contract"]
            for filename in ("src/\u6d4b\u8bd5.py", "src/\u65b0\u6587\u4ef6.py"):
                with self.subTest(protected_exists=protected_exists, filename=filename):
                    self.assertTrue(handoff.check(contract, self.receipt(
                        contract, changed_files=[filename]))["valid"])

    def test_distinct_existing_unicode_files_are_not_casefolded_together(self):
        first, second = self.root / "src/ma\u00df.py", self.root / "src/mass.py"
        first.write_text("first\n")
        if second.exists():
            self.skipTest("This filesystem aliases these Unicode names.")
        second.write_text("second\n")
        contract = self.prepared(owned_scope=["src/"], forbidden_scope=["src/ma\u00df.py"])["contract"]
        self.assertTrue(handoff.check(contract, self.receipt(
            contract, changed_files=["src/mass.py"]))["valid"])

    def test_symlink_escape_including_nonexistent_destination(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.root / "src/escape").symlink_to(outside, target_is_directory=True)
            (self.root / "src/dangling").symlink_to(Path(outside) / "missing")
            contract = self.prepared()["contract"]
            for path in ("src/escape/new.py", "src/dangling"):
                self.rejected(contract, changed_files=[path])
                with self.assertRaises(handoff.HandoffError):
                    self.prepared(owned_scope=[path])

    def test_internal_symlinks_are_canonical_for_ownership_and_forbidden(self):
        (self.root / "alias").symlink_to(self.root / "src", target_is_directory=True)
        contract = self.prepared(owned_scope=["alias/"], forbidden_scope=["alias/secret.py"])["contract"]
        self.assertEqual(contract["owned_scope"], ["src/"])
        self.assertEqual(contract["forbidden_scope"], ["src/secret.py"])
        checked = handoff.check(contract, self.receipt(contract, changed_files=["alias/new.py"]))
        self.assertEqual(checked["changed_files"], ["src/new.py"])
        self.rejected(contract, changed_files=["alias/secret.py"])
        self.rejected(contract, changed_files=["alias"])
        self.rejected(contract, changed_files=["alias/new.py", "src/new.py"])

    def test_symlink_retarget_cannot_expand_prepared_scope(self):
        (self.root / "elsewhere").mkdir()
        (self.root / "alias").symlink_to(self.root / "src", target_is_directory=True)
        contract = self.prepared(owned_scope=["alias/"])["contract"]
        (self.root / "alias").unlink()
        (self.root / "alias").symlink_to(self.root / "elsewhere", target_is_directory=True)
        self.rejected(contract, changed_files=["alias/new.py"])

    def test_symlink_loop_returns_validation_error(self):
        (self.root / "src/loop").symlink_to("loop")
        contract = self.prepared()["contract"]
        self.rejected(contract, changed_files=["src/loop/file.py"])

    def test_check_revalidates_contract(self):
        contract = self.prepared()["contract"]
        for field, value in (("execution_owner_id", ""), ("owned_scope", []),
                             ("write_policy", "read_only")):
            invalid = copy.deepcopy(contract)
            invalid[field] = value
            with self.assertRaises(handoff.HandoffError):
                handoff.check(invalid, self.receipt(contract))

    def test_helpers_do_not_mutate_inputs_or_write_scope_files(self):
        original = copy.deepcopy(self.request)
        before = sorted(path.relative_to(self.root).as_posix() for path in self.root.rglob("*"))
        contract = handoff.prepare(self.request)["contract"]
        receipt = self.receipt(contract)
        saved_contract, saved_receipt = copy.deepcopy(contract), copy.deepcopy(receipt)
        handoff.check(contract, receipt)
        after = sorted(path.relative_to(self.root).as_posix() for path in self.root.rglob("*"))
        self.assertEqual(self.request, original)
        self.assertEqual(contract, saved_contract)
        self.assertEqual(receipt, saved_receipt)
        self.assertEqual(before, after)

    def test_replaced_canonical_scope_is_rejected(self):
        contract = self.prepared()["contract"]
        (self.root / "src").rename(self.root / "moved")
        (self.root / "src").symlink_to(self.root / "moved", target_is_directory=True)
        self.rejected(contract, changed_files=["src/new.py"])

    def run_cli(self, *args):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), *args],
                                text=True, capture_output=True,
                                env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        self.assertEqual(result.stderr, "")
        return result.returncode, json.loads(result.stdout)

    def test_cli_roundtrip(self):
        code, prepared = self.run_cli("prepare", "--request-json", json.dumps(self.request))
        self.assertEqual(code, 0)
        contract = prepared["contract"]
        code, checked = self.run_cli("check", "--contract-json", json.dumps(contract),
                                     "--receipt-json", json.dumps(self.receipt(contract)))
        self.assertEqual(code, 0)
        self.assertTrue(checked["valid"])

    def test_cli_invalid_receipt_and_contract(self):
        contract = self.prepared()["contract"]
        code, error = self.run_cli("check", "--contract-json", json.dumps(contract),
                                   "--receipt-json", json.dumps(self.receipt(
                                       contract, assignment_id="wrong-assignment")))
        self.assertEqual(code, 2)
        self.assertEqual(error["error"]["code"], "assignment_mismatch")
        code, error = self.run_cli("check", "--contract-json", "null", "--receipt-json", "{}")
        self.assertEqual(code, 2)
        self.assertEqual(error["error"]["code"], "invalid_request")

    def test_cli_errors_are_only_structured_json(self):
        for args in ((), ("unknown",), ("prepare",),
                     ("prepare", "--request-json", "{"),
                     ("prepare", "--request-json", "[]"),
                     ("prepare", "--request-json", '{"task_id":"x","task_id":"y"}'),
                     ("prepare", "--request-json", '{"task_id":NaN}')):
            code, error = self.run_cli(*args)
            self.assertNotEqual(code, 0)
            self.assertFalse(error["ok"])
            self.assertIn("code", error["error"])
            self.assertIn("message", error["error"])


if __name__ == "__main__":
    unittest.main()
