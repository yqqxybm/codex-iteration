#!/usr/bin/env python3
"""Stateless native task preparation and receipt checks; not an OS sandbox."""

import argparse
import json
import os
from pathlib import Path, PureWindowsPath
import re
import sys
import unicodedata
import uuid


ROLES = {"explorer", "worker", "reviewer"}
EFFORTS = {"none", "minimal", "low", "medium", "high", "xhigh", "max", "ultra"}
WRITE_POLICIES = {"read_only", "same_worktree_disjoint", "single_writer"}
WRITE_GATES = {"project_analysis_consumed", "explicitly_skipped_by_user", "not_required_very_small"}
STATUSES = {"done", "blocked", "failed", "out_of_scope"}
TEXT_FIELDS = (
    "task_id", "task_name", "agent_owner", "agent_type", "model", "reasoning_effort",
    "route_reason", "write_policy", "analysis_gate", "analysis_gate_basis", "task",
    "done_when", "verification",
)
REQUEST_FIELDS = set(TEXT_FIELDS) | {"scope_root", "owned_scope", "forbidden_scope"}
IDENTITY_FIELDS = {"assignment_id", "execution_owner_id"}
RECEIPT_FIELDS = {"assignment_id", "status", "changed_files", "result", "verification", "new_work"}
PLACEHOLDERS = {"todo", "tbd", "pending", "n/a", "none", "null", "...", "-", "{}", "[]"}


class HandoffError(ValueError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def _require(condition, code, message):
    if not condition:
        raise HandoffError(code, message)


def _text(value, field, substantive=False):
    _require(isinstance(value, str) and bool(value.strip()), "invalid_field",
             field + " must be a nonempty string")
    _require("\x00" not in value, "invalid_field", field + " must not contain NUL")
    if substantive:
        stripped = value.strip()
        _require(stripped.lower() not in PLACEHOLDERS and not re.fullmatch(r"<[^<>]+>", stripped),
                 "placeholder", field + " must contain actual content, not a placeholder")
    return value


def _enum(value, choices, field):
    _require(isinstance(value, str) and value in choices, "invalid_field",
             field + " must be one of: " + ", ".join(sorted(choices)))


def _disk_spelling(path, directory_names=None):
    """Recover existing component names without folding case-sensitive names."""
    if directory_names is None:
        directory_names = {}
    current = Path(path.anchor)
    for part in path.parts[1:]:
        candidate = current / part
        if candidate.exists():
            names = directory_names.get(current)
            if names is None:
                names = set(os.listdir(current))
                directory_names[current] = names
            if part not in names:
                identity = candidate.lstat()
                matches = [name for name in names
                           if os.path.samestat((current / name).lstat(), identity)]
                _require(len(matches) == 1, "ambiguous_identity",
                         "cannot determine a unique on-disk spelling: " + str(candidate))
                part = matches[0]
        current /= part
    return current


def _case_sensitive(directory):
    while not directory.exists():
        directory = directory.parent
    try:
        # Darwin's public sys/unistd.h defines _PC_CASE_SENSITIVE as 11.
        key = 11 if sys.platform == "darwin" else getattr(os, "pathconf_names", {}).get("PC_CASE_SENSITIVE")
        if key is not None:
            value = os.pathconf(directory, key)
            _require(value in (0, 1), "unknown_case_semantics",
                     "filesystem did not report directory case semantics: " + str(directory))
            return bool(value)
        names = os.listdir(directory)
        for name in names:
            alias = name.swapcase() if name.isascii() else name
            if alias == name:
                continue
            if alias in names:
                return True
            actual = (directory / name).lstat()
            try:
                alternate = (directory / alias).lstat()
            except FileNotFoundError:
                return True
            if os.path.samestat(actual, alternate):
                return False
    except (OSError, ValueError) as error:
        if isinstance(error, HandoffError):
            raise
        raise HandoffError("unknown_case_semantics", "cannot inspect directory case semantics: "
                           + str(directory)) from error
    raise HandoffError("unknown_case_semantics", "cannot determine directory case semantics without "
                       "writing a probe: " + str(directory))


def _same_parts(root, left, right):
    if len(left) != len(right):
        return False
    parent = root
    for first, second in zip(left, right):
        if first != second:
            if first.isascii() and second.isascii() and first.lower() != second.lower():
                return False
            try:
                first_path, second_path = parent / first, parent / second
                first_exists, second_exists = first_path.exists(), second_path.exists()
                if first_exists or second_exists:
                    if not (first_exists and second_exists
                            and _disk_spelling(first_path) == _disk_spelling(second_path)):
                        return False
                else:
                    first_key = unicodedata.normalize("NFD", first).casefold()
                    second_key = unicodedata.normalize("NFD", second).casefold()
                    if first_key != second_key or _case_sensitive(parent):
                        return False
                    _require(first.isascii() and second.isascii(), "ambiguous_identity",
                             "cannot compare missing non-ASCII case aliases using filesystem collation")
            except (OSError, ValueError) as error:
                if isinstance(error, HandoffError):
                    raise
                raise HandoffError("ambiguous_identity", "cannot inspect path identity") from error
        parent /= first
    return True


def _same_scope(root, left, right):
    return (left.endswith("/") == right.endswith("/")
            and _same_parts(root, Path(left).parts, Path(right).parts))


def _root(value):
    _text(value, "scope_root")
    root = Path(value)
    _require(root.is_absolute(), "invalid_path", "scope_root must be absolute")
    try:
        root = _disk_spelling(root.resolve(strict=True))
        _require(root.is_dir(), "invalid_path", "scope_root must be an existing directory")
    except (OSError, RuntimeError, ValueError) as error:
        if isinstance(error, HandoffError):
            raise
        raise HandoffError("invalid_path", "scope_root cannot be resolved: " + str(error)) from error
    return root


def _path(root, value, field, scope=False, directory_names=None):
    _text(value, field)
    path = Path(value)
    _require(not path.is_absolute() and not PureWindowsPath(value).drive and "\\" not in value,
             "invalid_path", field + " must be an unambiguous relative path")
    _require(".." not in path.parts, "invalid_path", field + " must not contain '..'")
    subtree = value.endswith("/") or path == Path(".")
    _require(scope or not subtree, "invalid_path", field + " must name a file, not a directory")
    candidate = root / path
    try:
        resolved = _disk_spelling(candidate.resolve(strict=False), directory_names)
        _require(resolved == root or root in resolved.parents, "path_escape",
                 field + " resolves outside scope_root")
        for parent in candidate.parents:
            if parent == root:
                break
            _require(not parent.exists() or parent.is_dir(), "invalid_path",
                     field + " has a non-directory parent")
        if resolved.exists():
            _require(resolved.is_dir() if subtree else resolved.is_file(), "invalid_path",
                     field + (" subtree must name a directory" if subtree else " must name a regular file"))
        relative = resolved.relative_to(root).as_posix()
    except (OSError, RuntimeError, ValueError) as error:
        if isinstance(error, HandoffError):
            raise
        raise HandoffError("invalid_path", field + " cannot be resolved: " + str(error)) from error
    return relative + ("/" if subtree and relative != "." else "")


def _paths(root, values, field, scope=False, nonempty=False):
    _require(isinstance(values, list) and (not nonempty or bool(values)), "invalid_field",
             field + " must be " + ("a nonempty" if nonempty else "a") + " list of relative paths")
    directory_names = {}
    canonical = [_path(root, value, field, scope=scope, directory_names=directory_names) for value in values]
    seen, candidates = set(), {}
    for path in canonical:
        key = unicodedata.normalize("NFD", path).casefold()
        previous = candidates.setdefault(key, [])
        _require(path not in seen and not any(_same_scope(root, path, other) for other in previous),
                 "duplicate_path", field + " contains duplicate canonical paths")
        seen.add(path)
        previous.append(path)
    return canonical


def _request(request, is_contract=False):
    _require(isinstance(request, dict), "invalid_request", "request must be a JSON object")
    allowed = REQUEST_FIELDS | IDENTITY_FIELDS if is_contract else REQUEST_FIELDS
    _require(request.keys() <= allowed, "unknown_field", "request or contract contains unknown fields")
    result = {field: _text(request.get(field), field) for field in TEXT_FIELDS}
    for field in ("route_reason", "analysis_gate_basis", "task", "done_when", "verification"):
        _text(result[field], field, substantive=True)
    _require(re.fullmatch(r"[a-z0-9_]+", result["task_name"]) is not None, "invalid_field",
             "task_name must contain only lowercase letters, digits and underscores")
    _enum(result["agent_type"], ROLES, "agent_type")
    _enum(result["reasoning_effort"], EFFORTS, "reasoning_effort")
    _enum(result["write_policy"], WRITE_POLICIES, "write_policy")
    read_only = result["write_policy"] == "read_only"
    _require(read_only or result["agent_type"] == "worker", "authority_mismatch",
             "only worker may receive a writing policy; explorer and reviewer require read_only")
    _enum(result["analysis_gate"], WRITE_GATES | {"not_required_read_only"} if read_only else WRITE_GATES,
          "analysis_gate")
    root = _root(request.get("scope_root"))
    result["scope_root"] = str(root)
    result["owned_scope"] = _paths(root, request.get("owned_scope"), "owned_scope",
                                    scope=True, nonempty=True)
    result["forbidden_scope"] = _paths(root, request.get("forbidden_scope", []),
                                        "forbidden_scope", scope=True)
    return result


def prepare(request):
    """Return a fresh contract and explicit, self-contained spawn_agent arguments."""
    contract = _request(request)
    contract["assignment_id"] = str(uuid.uuid4())
    contract["execution_owner_id"] = str(uuid.uuid4())
    template = {
        "assignment_id": contract["assignment_id"], "status": "done",
        "changed_files": [], "result": "<actual result>",
        "verification": "<commands and observed results>", "new_work": [],
    }
    message = "\n".join((
        "Implement or inspect only this assigned task. The contract below is self-contained.",
        "Task, purpose, owner, route, boundaries, analysis basis and verification:",
        json.dumps(contract, ensure_ascii=True, separators=(",", ":")),
        "Scope notation: '.' means the root subtree, a trailing '/' means a subtree, "
        "and a bare path means exactly that file. Forbidden scope overrides owned scope.",
        "Keep the parent goal, CAO and lifecycle state unchanged. Do not spawn subagents "
        "or interfere with peers. Do not commit, push, publish, release, tag, deploy or sync. Stay within owned "
        "scope and write_policy, and preserve others' changes. Return new work to the parent.",
        "Return this receipt with actual content; status is done, blocked, failed or out_of_scope:",
        json.dumps(template, ensure_ascii=True, separators=(",", ":")),
        "The parent must inspect the real diff, results and parallel conflicts. This helper "
        "is not OS isolation, a scheduler or semantic acceptance; do not claim parent completion.",
    ))
    spawn_args = {field: contract[field] for field in
                  ("task_name", "agent_type", "model", "reasoning_effort")}
    spawn_args.update(fork_turns="none", message=message)
    return {"contract": contract, "spawn_args": spawn_args}


def _within(root, path, scope):
    if scope == ".":
        return True
    path_parts, scope_parts = Path(path).parts, Path(scope).parts
    if scope.endswith("/"):
        return (len(path_parts) > len(scope_parts)
                and _same_parts(root, path_parts[:len(scope_parts)], scope_parts))
    return _same_parts(root, path_parts, scope_parts)


def check(contract, receipt):
    """Check declarations only; the parent retains authority over actual acceptance."""
    validated = _request(contract, is_contract=True)
    for field in ("assignment_id", "execution_owner_id"):
        validated[field] = _text(contract.get(field), "contract." + field)
    # A prepared scope is already canonical. Retargeting a symlink must not widen it.
    root = Path(validated["scope_root"])
    old_root = Path(contract["scope_root"])
    _require(root.anchor == old_root.anchor and _same_parts(Path(root.anchor), root.parts[1:],
                                                          old_root.parts[1:]), "scope_changed",
             "contract.scope_root is no longer canonical; prepare a fresh assignment")
    for field in ("owned_scope", "forbidden_scope"):
        previous = contract.get(field)
        _require(isinstance(previous, list) and len(validated[field]) == len(previous)
                 and all(_same_scope(root, old, new) for old, new in zip(previous, validated[field])),
                 "scope_changed",
                 "contract." + field + " is no longer canonical; prepare a fresh assignment")
    _require(isinstance(receipt, dict), "invalid_receipt", "receipt must be a JSON object")
    if "subagent_receipt" in receipt:
        _require(receipt.keys() == {"subagent_receipt"}, "invalid_receipt",
                 "receipt wrapper must contain only subagent_receipt")
        receipt = receipt["subagent_receipt"]
    _require(isinstance(receipt, dict) and RECEIPT_FIELDS == receipt.keys(), "invalid_receipt",
             "receipt must contain exactly assignment_id, status, changed_files, result, verification and new_work")
    _require(isinstance(receipt["assignment_id"], str)
             and receipt["assignment_id"] == validated["assignment_id"], "assignment_mismatch",
             "receipt assignment_id does not match this assignment")
    _enum(receipt["status"], STATUSES, "status")
    for field in ("result", "verification"):
        _require(isinstance(receipt[field], str), "invalid_field", field + " must be text")
        if receipt["status"] == "done":
            _text(receipt[field], field, substantive=True)
    _require(isinstance(receipt["new_work"], list), "invalid_field", "new_work must be a list")
    for item in receipt["new_work"]:
        if isinstance(item, str):
            _text(item, "new_work entry")
        else:
            _require(isinstance(item, dict) and bool(item), "invalid_field",
                     "new_work entries must be nonempty strings or nonempty objects")
    changed = _paths(root, receipt["changed_files"], "changed_files")
    _require(validated["write_policy"] != "read_only" or not changed, "read_only_violation",
             "read_only assignments cannot report changed files")
    for path in changed:
        _require(any(_within(root, path, scope) for scope in validated["owned_scope"]), "outside_owned_scope",
                 "changed file is outside owned_scope: " + path)
        _require(not any(_within(root, path, scope) for scope in validated["forbidden_scope"]),
                 "forbidden_scope", "changed file is in forbidden_scope: " + path)
    return {
        "valid": True, "parent_acceptance": False,
        "task_id": validated["task_id"], "agent_owner": validated["agent_owner"],
        "assignment_id": validated["assignment_id"], "execution_owner_id": validated["execution_owner_id"],
        "status": receipt["status"], "changed_files": changed,
        "result": receipt["result"], "verification": receipt["verification"], "new_work": receipt["new_work"],
        "parent_review_required": "Inspect actual diff, results and parallel conflicts; "
        "this receipt check is not semantic acceptance or OS isolation.",
    }


class _Parser(argparse.ArgumentParser):
    def error(self, message):
        raise HandoffError("invalid_arguments", message)


def _json_object(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, "invalid_json", "duplicate JSON key: " + key)
        result[key] = value
    return result


def _invalid_constant(value):
    raise HandoffError("invalid_json", "non-finite JSON number: " + value)


def _load(value):
    try:
        return json.loads(value, object_pairs_hook=_json_object, parse_constant=_invalid_constant)
    except (ValueError, RecursionError) as error:
        if isinstance(error, HandoffError):
            raise
        raise HandoffError("invalid_json", "invalid JSON: " + str(error)) from error


def main(argv=None):
    try:
        parser = _Parser(add_help=False)
        commands = parser.add_subparsers(dest="command", required=True)
        prepare_parser = commands.add_parser("prepare", add_help=False)
        prepare_parser.add_argument("--request-json", required=True)
        check_parser = commands.add_parser("check", add_help=False)
        check_parser.add_argument("--contract-json", required=True)
        check_parser.add_argument("--receipt-json", required=True)
        args = parser.parse_args(argv)
        if args.command == "prepare":
            result = prepare(_load(args.request_json))
        else:
            result = check(_load(args.contract_json), _load(args.receipt_json))
    except HandoffError as error:
        print(json.dumps({"ok": False, "error": {"code": error.code, "message": str(error)}},
                         ensure_ascii=True))
        return 2
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
