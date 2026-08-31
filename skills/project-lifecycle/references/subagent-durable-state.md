# CAO Durable Subagent State

Load this reference only after the CAO activation test succeeds. It defines the
strict durable contract for CAO-backed assignments. When CAO is not active,
use the lightweight native V2 protocol in `subagent-execution.md`; do not
apply this strict schema merely because work is long, multi-wave, or
cross-turn.

This reference owns durable machine-checkable task state, not native V2 thread
mechanics. Shared parallelism, model routing, native dispatch, follow-up, and
resident-thread accounting are defined by `subagent-execution.md` and are not
duplicated here.

## Activation And Authority

Run the CAO activation test before activating it: ask whether an actual or
required interruption/resume in this same parent task would make ownership,
locks, attempt identity/history, receipt acceptance, or convergence unsafe
without machine persistence. Activate CAO only on a concrete yes. Long,
cyclic, multi-wave, cross-turn, read-only, or V2-persistence work is never
sufficient by itself: use V2 when the controller can safely reread and
recompute the needed state.

The current Codex host supplies request-local thread identity in MCP call
metadata while leaving the MCP process environment without a per-task
`CODEX_THREAD_ID`. Host metadata availability is not authority by itself: the
installed CAO MCP runtime does not yet bind and validate that request-local
identity for controller mutations.

Therefore the main lifecycle task runs every CAO mutation and semantic join
through the current-task CLI wrapper `~/.codex/bin/cao`. MCP may only validate,
report conflicts, or report status; never use inherited environment, a static
id, or a user-visible tool argument to pretend task identity. Children never
run CAO mutations or joins. Keep the MCP allowlist read-only until the installed
runtime consumes trusted request-local identity and proves both same-task
continuity and different-task takeover rejection, including concurrent-request
isolation.

Here, every `dispatch`, `receipt`, `replan`, `release`, `reopen`, `complete`,
reconciliation, and semantic `join` means that wrapper path. CAO stores
execution state, not native V2 task navigation, wait, messaging, interruption,
or terminal-thread events.

Hard state is blocked only when this activation test concretely requires CAO
and the current-task CLI wrapper is unavailable or invalid. Do not silently
downgrade to conversational state in that case.

## Strict Assignment Contract

For CAO-enabled work, every native child receives this complete durable
`subagent_assignment`. All fields are required; `forbidden_scope` and
`conflict_keys` may be empty. `current_task_status` records the status carried
by the assignment; a spawn-ready CAO dispatch assignment carries `active`.
`assignment_id` is a unique immutable attempt id, and `execution_owner_id` is
a stable logical execution-slot id; neither is a native V2 thread id. Never
reuse either identity in the parent objective's attempt history.

~~~yaml
subagent_assignment:
  wave_id: <unique dispatch wave id>
  assignment_id: <unique attempt id>
  execution_owner_id: <stable logical execution-slot id>
  current_task_status: <current task status at assignment time>
  parent_target:
    objective: <outcome served by this task>
    boundary: <relevant goal and non-goal boundary>
    scope_root: <absolute canonical base for every relative task scope>
    value_relation: <how local values jointly serve the assignment and how a real tradeoff is resolved>
    stop_condition: <parent condition the child must not overclaim>
  task:
    id: <agenda id>
    agent_owner: <logical project role>
    role_and_lens: <stable role plus assignment-specific emphasis>
    analysis_gate: <project_analysis_consumed | explicitly_skipped_by_user |
      not_required_read_only | not_required_very_small>
    analysis_gate_evidence: <Stage 3 boundary, exact waiver, concise read-only
      proof, or concise very_small proof>
    owned_scope: <relative scopes>
    forbidden_scope: <relative denied scopes; empty when none>
    write_policy: <read_only | same_worktree_disjoint | single_writer>
    conflict_keys: <opaque shared-resource keys; empty when none>
    done_when: <observable local completion condition>
    verification: <commands, artifacts, or evidence>
  output_requirement:
    format: subagent_receipt
    evidence:
      role_and_lens: <task role_and_lens echoed as the evidence lens>
      done_when: <task done_when echoed as the acceptance boundary>
      verification: <task verification echoed as required proof>
    schema: <embed the exact Receipt Contract below>
  hard_boundaries:
    - do not mutate or complete the parent goal
    - do not spawn subagents
    - do not message, steer, follow up, interrupt, or retask peer agents
    - do not commit, push, publish, release, deploy, sync, or claim project completion
    - do not write outside owned_scope or inside forbidden_scope
    - preserve user and peer changes
    - return peer coordination, graph changes, and material follow-up to the parent
      in task_graph_delta and new_work
~~~

Do not dispatch while target, scope, write policy, done condition, or
verification boundary remains unresolved. Use `not_required_read_only` only for
a non-mutating node with an explicit read-only contract. A material review that
consumes a project-analysis or goal-preflight model remains
`project_analysis_consumed`.

Canonicalize filesystem identity before conflict proof or dispatch. Resolve
`scope_root` to one absolute real path; reject absolute task paths, NUL, `..`,
and any resolved path outside that root. Normalize symlink aliases to the same
root-relative identity. `.` means the whole root, a trailing slash means a
directory and descendants, and a bare path means one exact file. When the user
names an absolute target, place its common absolute base in `scope_root` and
keep `owned_scope` and `forbidden_scope` relative to that base.

Subagents inherit the parent turn's live permission policy. `write_policy` is
an assignment boundary, not OS enforcement. When correctness requires enforced
read-only isolation, run the parent turn read-only; otherwise disclose that the
boundary is instructional.

## Atomic Dispatch And Durable Recovery

Event-history validation reuses incremental created-id/task-status projections
and receipt/add-task indexes instead of copying growing event prefixes.
Nonempty dispatch builds one historical identity set and updates it in place
for the wave. Material `replan` retains full-graph validation. Treat projection
reuse and growth as the complexity evidence, not a helper invocation count by
itself.

The durable sequence is:

1. Initialize the parent contract and add only graph nodes whose route,
   dependencies, conflicts, scope, and evidence contract are stable.
2. Run `~/.codex/bin/cao validate`, then call
   `~/.codex/bin/cao dispatch --capacity <configured V2 capacity>`. One locked
   transition first evaluates the deterministic stable-order greedy route over
   the complete ready sequence and returns it when it fills available capacity.
   On underfill, it constructs complete whole-ready conflict adjacency,
   compares a bounded deterministic greedy portfolio, and runs one step-bounded
   greedy-color search with the best route as its incumbent. The search keeps a
   better partial wave when the target is unreachable or the shared budget
   expires. It chooses greatest evaluated cardinality, then greater
   deterministic residual-wave cardinality, then the lexicographically smaller
   sorted original-ready index tuple. Capacity, dependencies, active locks, and
   write conflicts remain hard constraints. A result below available capacity is
   inclusion-maximal, and unique logical pair evaluation is bounded by
   `n(n-1)/2`. The deterministic heuristic does not promise an exact/global
   maximum, globally minimal wave count, a fixed approximation ratio, or
   guaranteed fill. The same transition creates all attempt identities, marks
   selected nodes active, and persists every exact spawn-ready payload as
   `subagent_assignment` with its canonical digest in
   `subagent_assignment_fingerprint`. It returns those complete durable
   assignments. There is no separate `ready`, `claim`, or `prompt` step.
3. Verify each returned assignment includes the authoritative hard boundaries.
   Spawn through native V2 with the selected explicit role, model, effort, and
   `fork_turns: "none"`; use the exact durable assignment as the message without
   rewriting it or passing it through the ordinary native compiler.
4. Ingest each returned receipt with `~/.codex/bin/cao receipt`.
5. Inspect and integrate the result. If receipt ingestion rejects a result and
   the contract must change, call `~/.codex/bin/cao replan` directly against
   the still-active assignment. If the rejected result needs only a
   same-contract retry, release that assignment and dispatch again. Use
   `~/.codex/bin/cao reopen` only after an ingested receipt and only for an
   unchanged-contract retry. Use receipt-bearing `~/.codex/bin/cao replan` when
   scope, dependency, conflict, owner, lens, done condition, or verification
   changes; supply the complete replacement contract so receipt archival and
   replacement are one atomic transition. Reject material follow-up with
   evidence, bind integrated same-contract follow-up to concrete tasks added
   after the receipt, or let integrated `replan` bind it to the replacement
   fingerprint.
6. Run parent verification/review, then call `~/.codex/bin/cao complete` with
   the same assignment id, a passed verification outcome, material evidence,
   and concrete post-receipt task ids for any integrated follow-up.
7. Run `~/.codex/bin/cao join`; unresolved tasks, locks, receipts, or evidence
   become the next lifecycle agenda state.

If a mutating CAO command exits with code `3`, do not repeat it. Run the
reported `reconcile_argv` arrays through the current-task CLI wrapper exactly
as argv, without shell evaluation, then continue from the observed committed
state. The recovery status command uses `--include-assignments` so a committed
dispatch with a lost response retains its complete spawn payloads. For each
active lock, recovery uses `assignment_id` to locate exactly one historical
dispatch event assignment, validates the event envelope against the lock and
the payload fingerprint and task history, and returns a deep copy of the exact
persisted `subagent_assignment`. It must not call the current assignment builder
or reconstruct policy. Non-identity policy content in `hard_boundaries` and the
embedded receipt schema comes from the structurally valid,
fingerprint-consistent historical payload rather than current constants, so one
assignment identity cannot drift to later policy. Treat the digest as an
internal consistency check inside CAO's local-state trust boundary, not an
authenticity signature.

On resume in the same parent task, inspect V2 child threads and run
`~/.codex/bin/cao validate`,
`~/.codex/bin/cao status --include-assignments`, and
`~/.codex/bin/cao join` before new dispatch. Match durable work through
`execution_owner_id` plus `assignment_id`. If a thread is still active, wait or
steer it. If it completed, ingest its receipt. If it failed or disappeared
without a receipt, interrupt obsolete native work when needed, confirm its
latest state, then release the active durable assignment before dispatching
replacement work. Reserve `reopen` for attempts whose receipt was already
ingested. A different controller thread id is a hard-state blocker, not a
takeover signal. Never blind-resend or spawn a duplicate attempt.

## Receipt And Semantic Join

Every CAO-backed child returns this receipt schema, embedded exactly in its
assignment's `output_requirement.schema`:

~~~yaml
subagent_receipt:
  assignment_id: <assignment id echoed exactly>
  execution_owner_id: <execution owner echoed exactly>
  agent: <logical project role>
  agenda_item: <task id>
  assigned_scope: <list>
  changed_files: <list; empty for read-only work>
  evidence: <list of material observations or verification outcomes; done requires a non-sentinel item>
  task_graph_delta:
    new_dependency_edges: <list; empty when none>
    new_conflict_edges: <list; empty when none>
    blocked_items: <list; empty when none>
    unblocked_items: <list; empty when none>
    suggested_reclassification: <non-empty string; use none when unchanged>
  status: <done | blocked | failed | out_of_scope>
  new_work: <list; empty when none>
  stop_reason: <meaningful reason why the child stopped>
~~~

The parent rejects receipts with the wrong task id, logical role, execution
owner, or assignment id, missing required evidence, scope violations, or
write-policy conflicts. A receipt never proves completion by itself. Inspect
returned changes or findings, incorporate accepted graph deltas and `new_work`,
run parent verification as appropriate, and mark the node done only when
`done_when` is met. The parent carries the receipt into the lifecycle Handoff,
agenda, and trace only as needed for the next judgment or action. When CAO is
active, persist a passed parent-verification outcome with evidence.

Runtime semantics are strict: `assigned_scope` is a non-empty ordered list of
canonical `scope_root`-relative scopes; `changed_files` is a canonical
scope-root-relative list after symlink resolution; every task-graph delta key
is present; `stop_reason` is material and `none` is invalid; and extra receipt
fields are rejected. Empty `changed_files` is valid for read-only work.

For every material follow-up, bind integration to concrete post-receipt task
ids or an atomic replan fingerprint, or record a rejected outcome with evidence,
before `cao complete`; `cao join` must reject any gap.

Before a dependent durable wave or parent completion, semantic join requires:

1. Every dispatched assignment has a receipt that is consumed, rejected, or
   converted into visible agenda state.
2. No failed or missing child result is treated as success.
3. Required parent inspection, verification, integration, and review are
   complete.
4. `~/.codex/bin/cao join` passes.

Thread state is capacity evidence, not semantic completion proof. A missing
thread without an accepted receipt keeps its task pending. Report the semantic
join result and remaining running child count; do not emit a per-event transport
ledger.

## Durable Pressure Scenarios

- Cyclic multi-wave work spanning an interruption in the same parent task:
  apply the activation test; use CAO only when the controller cannot safely
  reread and recompute state.
- Resume needs an ownership lock and immutable attempt identity that cannot be
  reconstructed safely: activate CAO and use `~/.codex/bin/cao`; do not trust
  local stdio MCP `env_vars` or a supplied thread-id argument.
- Activation test requires CAO but `~/.codex/bin/cao` is unavailable or invalid:
  mark hard state blocked; do not downgrade to V2-only state.
- Receipt rejected before ingestion with a changed contract: atomically
  `replan` the exact active assignment, then dispatch the replacement.
- Receipt rejected before ingestion with an unchanged contract: release the
  exact active assignment, then dispatch a fresh attempt.
- Ingested failed or parent-rejected durable receipt with the same contract:
  resolve material follow-up during `reopen`, then dispatch again.
- Ingested receipt that changes any task-contract field: use atomic `replan`,
  then dispatch the replacement contract; never reopen and mutate later.
- A different controller thread id appears on resume: hard-block rather than
  treating it as a takeover signal.
- A mutating command reports exit `3`: run its exact `reconcile_argv` arrays
  through the wrapper, observe the committed state, and do not blindly retry.
- Scheduler pressure: prove deterministic output, safety under
  capacity/dependency/active-lock/write-conflict constraints, greatest evaluated
  cardinality, residual-wave scoring before the lexicographic
  sorted-original-index tie-break, inclusion-maximal below-capacity results,
  and at most `n(n-1)/2` unique logical pair evaluations. Do not claim an
  exact/global maximum, globally minimal wave count, fixed approximation ratio,
  or never-underfill behavior.
