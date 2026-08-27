# Plan-Driven Iteration

Read this reference only when the Context Packet contains an agenda, plan,
checklist, issue list, or an instruction to advance planned
work. It supplies execution state mechanics; `project-lifecycle` still owns the
agenda, task graph, scope changes, and dispatch.

## Iteration Items

Own only implementation items assigned to `project-iteration`. Return
architecture, release, broad docs cleanup, sync, new-project work, and any
version/root-state change to `project-lifecycle`.

```yaml
iteration_items:
  - id: <stable short id>
    source_plan_item: <upstream agenda id, source line, or none>
    change: <specific code/docs/test outcome>
    files_or_area: <owned scope>
    done_when: <observable condition>
    verification: <targeted command and expected result>
    review_gates: <spec compliance, code quality, or both>
    status: <pending | active | done | blocked | skipped>
```

The iteration remains open while any owned item is pending, active, or
unverified. For each item:

1. Implement one pending item within its accepted boundary.
2. Update directly affected docs or tests only when they authoritatively
   describe or enforce the changed durable contract, or when removing an
   assertion that falsely freezes mutable implementation state.
3. Run the item's targeted verification, or record the exact blocker.
4. If a `not_required_very_small` check reveals semantic risk or a broader
   mutation, stop and return `material_change` for visible analysis. A local
   failure may be fixed and rerun only inside the original semantic boundary.
5. Add newly discovered work locally only when it belongs to the same serial
   item or the Context Packet already authorizes sequential handling. Return an
   independent read or disjoint write surface as `material_in_scope_new_work`
   with `subagent_execution_delta: replan_required`.
6. Return version/root-state input to `project-lifecycle` for State Boundary
   Enforcement; do not classify it locally as a `change_request`. Preserve
   `source_plan_item` when splitting work and report its resulting state.

Do not stop at the first passing test, commit, or subtask while owned work
remains. Stop only for a real blocker, an unsafe operation, an unfixable local
verification failure, an explicit user limit, or completion of every owned
item. Update the lifecycle trace before a forced interruption of a long or
resumable list.

Version management follows completion of the current iteration unless focused
commit boundaries require multiple commits. Continue the item loop after each
such commit.
