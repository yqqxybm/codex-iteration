# Subagent Execution

Use this reference whenever project-lifecycle finds independent work surfaces,
delegates a bounded task, selects a subagent model, or evaluates whether
delegated state must survive interruption. Loading this reference does not
activate CAO. This is the single authority for project subagent control policy
and accounting. Codex multi-agent V2 is the only runtime backend.

## Table Of Contents

- Control Boundary
- Task Graph And Dispatch Proof
- Model Routing
- V2 Native Dispatch
- Durable State With CAO
- Receipt Contract
- Join And Thread Accounting
- Pressure Scenarios

## Control Boundary

The system has three layers:

1. Codex multi-agent V2 owns spawn, model and reasoning overrides, canonical
   `task_name`, follow-up, messaging, wait, interruption, status listing, and
   terminal-thread lifecycle.
2. Project-lifecycle owns task decomposition, dependency and conflict proof,
   model-class judgment, assignment boundaries, receipt acceptance,
   integration, verification, and convergence.
3. CAO owns durable machine-checkable task state only after the CAO activation
   test proves that a required same-parent interruption/resume would make
   ownership, locks, attempt identity/history, receipt acceptance, or
   convergence unsafe without machine persistence. V2 thread persistence alone
   does not justify CAO.

Do not mirror native thread events in skills or CAO. Do not make CAO a second
controller. Do not send the full parent goal, graph, loop counters, or unrelated
context to a child when one bounded assignment is sufficient. Always use
`fork_turns: "none"` and carry the complete bounded assignment in the initial
message.

V2 is required. If it is disabled, unavailable, or blocked by policy, record the
node as blocked and stop delegation; do not substitute another subagent backend.
In config, enable `multi_agent_v2`, disable `multi_agent`, and set
`agents.enabled = true`: the feature flags select V2 while the agents switch
exposes its tools. Use the current Fast tier's native
`service_tier = "priority"` id. This system optimizes elapsed time rather than
preserving a slower service-tier path.

Parallel execution is opt-out. For every agenda with multiple independent
surfaces, identify dependency and write-conflict edges, then dispatch the
obvious safe wave that shortens the critical path. Use available capacity when
it saves more work than scheduling it costs; do not turn decomposition into an
optimization problem. Sequential execution is valid only with a concrete
dependency, conflict, runtime, policy, ROI, integration, or verification
blocker.

## Task Graph And Dispatch Proof

Represent work as nodes with dependency edges and conflict edges. A parallel
wave may contain only an antichain with no dependency or conflict edge between
selected nodes. Treat the same file, lockfile, schema, route, shared component,
migration, generated artifact, global configuration, deployment target, and
release state as conflict keys unless evidence proves isolation.

Before dispatch, record:

~~~yaml
subagent_execution:
  runtime_capability:
    backend: multi_agent_v2
    state: <enabled | unavailable | blocked_by_policy>
    controls: <spawn_agent, followup_task, send_message, wait_agent,
      interrupt_agent, list_agents>
    agent_types: <default, explorer, worker, reviewer>
    concurrency_limit: <number>
    evidence: <feature/config/tool metadata or runtime output>
  task_graph:
    nodes: <agenda ids>
    dependency_edges: <blocking edges>
    conflict_edges: <unsafe concurrent edges>
    selected_antichain: <ids or none>
    critical_path: <ids>
  mode: <sequential | subagent_wave | controller_team | workflow_batch>
  model_route: <per-node route records>
  merge:
    write_policy: <read_only | same_worktree_disjoint | single_writer>
    integration_owner: main lifecycle thread
    join_barrier: required
  roi: <why the wave shortens the critical path, or why delegation would cost more>
  parallel_blocker: <none or concrete blocker>
~~~

Use these modes:

- `sequential`: no profitable safe antichain;
- `subagent_wave`: one bounded antichain;
- `controller_team`: multiple controller-owned waves over an evolving agenda;
- `workflow_batch`: phased parallel execution over many similar or
  cross-checked items.

Use configured V2 concurrency capacity for profitable nodes from the selected
antichain without forcing unsafe or unprofitable slot filling. Target practical
utilization of expensive child slots; do not claim absolute yield or guaranteed
fill. Do not impose a smaller fixed reader or writer quota. Writer nodes still
require disjoint canonical scopes and conflict keys.
Commit, push, deploy, release mutation, remote sync mutation, parent-goal
completion, and final project completion remain main-thread actions.

Refresh the graph and wave whenever user feedback, a receipt, verification
failure, review finding, or accepted `new_work` changes nodes or edges. Do not
continue a serial plan by inertia when a new safe antichain appears.

## Model Routing

Keep the root lifecycle controller on the native proactive V2 effort
(`ultra` in the current model catalog). Route child capacity independently;
controller effort is not a reason to send every child to Sol.

The global fast path is `gpt-5.6-terra` with `medium` reasoning. Override it per
node when task shape requires more capacity:

- Terra `low` or `medium`: bounded exploration, broad read-heavy scans,
  deterministic verification, summarization, and mechanical low-coupling work.
- Terra `high`: bounded work that needs careful tracing but not frontier
  judgment.
- Sol `high`, `xhigh`, or stronger: ambiguous or coupled implementation,
  architecture or control-law judgment, security/data/release-sensitive work,
  deep or exhaustive review, disputed evidence, and final synthesis.
- `inherit`: only when the parent model and effort already match the selected
  class.

Record the exact native `agent_type`, logical role, model, reasoning effort,
reason, and availability per node. Select the smallest sufficient controlled
execution posture:

- `explorer`: specific, bounded, read-only codebase questions;
- `worker`: bounded implementation or production work with explicit ownership;
- `reviewer`: independent focused, deep, or exhaustive review.

The installed `explorer`, `worker`, and `reviewer` custom-agent layers under
`~/.codex/agents/` disable CAO and nested multi-agent tools inside child
threads.
Prove the selected posture is discoverable before dispatch and repair its
definition instead of silently substituting `default`. CAO-backed work uses
only these controlled postures.

Native `agent_type` does not replace `agent_owner` or `role_and_lens`: the former
sets the reusable runtime posture, while the latter two carry the
project-specific responsibility and lens. Model and effort resolve
independently. A value pinned in the selected custom-agent file wins; otherwise
the precedence is explicit spawn override, the corresponding `[agents]`
default, then the parent value. The controlled agent files deliberately leave
model and effort unpinned so lifecycle routing remains dynamic.

Never silently replace a Sol-class assignment with Terra. If the selected route
is unavailable, keep the node pending and replan or ask. Using Sol for a
Terra-class node is allowed only when availability or consolidation makes it
the faster total path.

## V2 Native Dispatch

Select the logical role, model route, assignment boundary, and verification
contract before spawning. When CAO is active, obtain `execution_owner_id`,
immutable `assignment_id`, and the complete spawn-ready assignment, including
universal hard boundaries, from its atomic `dispatch`; otherwise lifecycle
creates those identities and the same complete contract. Never reuse either
identity in the parent objective's attempt history. Include the complete
assignment in the initial spawn. Neither identifier is a native V2 thread id.
Never create an empty child or use a pre-assignment handshake.

Use the native V2 spawn arguments directly:

~~~yaml
v2_spawn:
  task_name: <unique lowercase/digit/underscore runtime label>
  agent_type: <default | explorer | worker | reviewer>
  fork_turns: "none"
  model: <omit for configured Terra default, or explicit route override>
  reasoning_effort: <omit for configured medium default, or explicit override>
  message: <complete subagent_assignment below>
~~~

`fork_turns: "none"` is the only protocol path. Put every irreducible input in
the bounded initial assignment so context transfer stays explicit, minimal, and
compatible with per-task model and effort routing. Do not use a positive integer
or `fork_turns: "all"`.
`task_name` is the V2 runtime handle; it is not the agenda id,
`execution_owner_id`, or `assignment_id`.
Dispatch exists only when `spawn_agent` returns the canonical `task_name`.
Narration, an intended task label, `wait_agent`, or an empty `list_agents`
result is not spawn evidence; mark the node blocked instead of simulating a
child or its result.

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
    value_ordering: <rule that resolves local tradeoffs>
    stop_condition: <parent condition the child must not overclaim>
  task:
    id: <agenda id>
    agent_owner: <logical project role>
    role_and_lens: <stable role plus assignment-specific emphasis; when a
      project-optimality packet is active, include the complete typed
      project_optimality_projection>
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
    schema: <embed the exact Receipt Contract>
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

Every field is required; `forbidden_scope` and `conflict_keys` may be empty.
`current_task_status` records the status carried by the assignment; a
spawn-ready CAO dispatch assignment carries `active`.
Native lifecycle dispatch and CAO dispatch use this same complete assignment;
CAO supplies it atomically when durable state is active.
When a `project_optimality_packet` is active, carry the assigned concern/probe
subset without extending this schema: put the complete
`project_optimality_projection` in `role_and_lens`, including packet/base
revision, claim boundary, concern basis/applicability, probe state/evidence ids,
referenced evidence, and affecting human decisions. Put executable evidence
surfaces and `observed_against` identity in `verification`; put local decision
impact in `done_when`. Add every assigned probe id as a packet-scoped
`conflict_key`, including read-only evidence assignments.

The child receipt `evidence` must account for every assigned probe. Because the
CAO receipt schema accepts evidence strings, encode each packet-backed probe
record as one compact JSON string with `probe_id`, `previous_state`,
`next_state`, `evidence_id`, protected `source_ref`, concise redacted
`observation`, and `observed_against`; for pending/blocking results, encode the
state and exact blocker instead of inventing evidence. The parent supplies
`introduced_by` while normalizing the receipt into a base-revision
`project_optimality_delta` and applies the contract's stale/conflict rules before
merge. Bounded children cannot change global concern applicability. Material
follow-up goes in `new_work`.
Do not spawn while the target, scope, write policy, done condition, or
verification boundary remains unresolved.
Use `not_required_read_only` only for a non-mutating node with an explicit
read-only contract. A material review that consumes a project-analysis or
goal-preflight model remains `project_analysis_consumed`.

Canonicalize filesystem identity before conflict proof or dispatch. Resolve
`scope_root` to one absolute real path; reject absolute task paths, NUL, `..`,
and any resolved path outside that root. Normalize symlink aliases to the same
root-relative identity. `.` means the whole root, a trailing slash means a
directory and descendants, and a bare path means one exact file. When the user
names an absolute target, place its common absolute base in `scope_root` and
keep `owned_scope` and `forbidden_scope` relative to that base.

Subagents inherit the parent turn's live permission policy. `write_policy` is an
assignment boundary, not OS enforcement. When correctness requires enforced
read-only isolation, run the parent turn read-only; otherwise disclose that the
boundary is instructional.

After spawn, keep only the compact controller state needed to join the wave:

~~~yaml
v2_wave_state:
  - assignment_id: <attempt id>
    execution_owner_id: <logical execution-slot id>
    task_id: <agenda id>
    task_name: <canonical V2 runtime handle returned by spawn_agent>
    agent_type: <native V2 execution posture>
    logical_role: <agent_owner plus role_and_lens>
    model_route: <model and effort>
    thread_state: <latest state returned by list_agents>
    receipt_state: <pending | received | consumed | rejected>
~~~

Native V2 remains the thread source of truth. Do not duplicate its event history
or build a transport registry. Continue non-overlapping parent work while
children run, use completion notifications, and wait only at a critical-path or
join barrier. Steer a live child for bounded corrections instead of spawning
duplicate work. For a later compatible assignment in the same parent turn,
use `followup_task` on an idle completed agent with the complete new assignment
when its retained context saves setup. Otherwise use a fresh spawn; V2 may
automatically unload an eligible resident when it needs the slot.

## Durable State With CAO

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
id, or a user-visible tool argument to pretend task identity. Children never run
CAO mutations or joins.
Keep the MCP allowlist read-only until the installed runtime consumes trusted
request-local identity and proves both same-task continuity and different-task
takeover rejection, including concurrent-request isolation.
Here, every `dispatch`, `receipt`, `replan`, `release`, `reopen`, `complete`,
reconciliation, and semantic `join` means that wrapper path.

Ordinary in-turn parallel work uses V2 alone.
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
   transition first evaluates the deterministic
   stable-order greedy route over the complete ready sequence and returns it
   when it fills available capacity. On underfill, it constructs complete
   whole-ready conflict adjacency, compares a bounded deterministic greedy
   portfolio, and runs one step-bounded greedy-color search with the best route
   as its incumbent. The search keeps a better partial wave when the target is
   unreachable or the shared budget expires. It chooses greatest evaluated
   cardinality, then greater deterministic residual-wave cardinality, then the
   lexicographically smaller sorted original-ready index tuple. Capacity,
   dependencies, active locks, and write conflicts remain hard
   constraints. A result below available capacity is inclusion-maximal, and
   unique logical pair evaluation is bounded by `n(n-1)/2`. The deterministic
   heuristic does not promise an exact/global maximum, globally minimal wave
   count, a fixed approximation ratio, or guaranteed fill. The same transition
   creates all attempt identities, marks selected nodes active, and persists
   every exact spawn-ready
   payload as `subagent_assignment` with its canonical digest in
   `subagent_assignment_fingerprint`. It returns those complete durable
   assignments. There is no separate `ready`, `claim`, or `prompt` step.
3. Verify each returned assignment includes the authoritative hard boundaries
   and spawn the whole wave directly through native V2. Do not rewrite or append
   ad hoc policy to the durable payload.
4. Ingest each returned receipt with `~/.codex/bin/cao receipt`.
5. Inspect and integrate the result. If receipt ingestion rejects a result and
   the contract must change, call `~/.codex/bin/cao replan` directly against the
   still-active assignment. If the rejected result needs only a same-contract
   retry, release that assignment and dispatch again. Use
   `~/.codex/bin/cao reopen` only after an ingested receipt and only for an
   unchanged-contract retry. Use receipt-bearing `~/.codex/bin/cao replan` when
   scope, dependency, conflict, owner, lens, done condition, or verification
   changes; supply the complete replacement contract so receipt
   archival and replacement are one atomic transition. Reject material
   follow-up with evidence, bind integrated same-contract follow-up to concrete
   tasks added after the receipt, or let integrated `replan` bind it to the
   replacement fingerprint.
6. Run parent verification/review, then call `~/.codex/bin/cao complete` with
   the same assignment id, a passed verification outcome, material evidence,
   and concrete post-receipt task ids for any integrated follow-up.
7. Run `~/.codex/bin/cao join`; unresolved tasks, locks, receipts, or evidence
   become the next lifecycle agenda state.

If a mutating CAO command exits with code `3`, do not repeat it. Run the
reported `reconcile_argv` arrays through the current-task CLI wrapper exactly
as argv, without shell evaluation, then
continue from the observed committed state. The recovery status command uses
`--include-assignments` so a committed dispatch with a lost response retains its
complete spawn payloads. For each active lock, recovery uses `assignment_id` to
locate exactly one historical dispatch event assignment, validates the event
envelope against the lock and the payload fingerprint and task history, and
returns a deep copy of the exact persisted `subagent_assignment`. It must not
call the current assignment builder or reconstruct policy. Non-identity policy
content in `hard_boundaries` and the embedded receipt schema comes from the
structurally valid, fingerprint-consistent historical payload rather than
current constants, so one assignment identity cannot drift to later policy.
Treat the digest as an internal consistency check inside CAO's local-state trust
boundary, not an authenticity signature.

CAO stores execution state, not native V2 thread mechanics. It must not persist
task navigation, wait, messaging, interruption, or terminal-thread events.

On resume in the same parent task, inspect V2 child threads and run
`~/.codex/bin/cao validate`, `~/.codex/bin/cao status --include-assignments`,
and `~/.codex/bin/cao join` before new
dispatch. Match durable work through
`execution_owner_id` plus `assignment_id`. If a thread is still active, wait or
steer it. If it completed, ingest its receipt. If it failed or disappeared
without a receipt, interrupt obsolete native work when needed, confirm its
latest state, then release the active durable assignment before dispatching
replacement work. Reserve `reopen` for attempts whose receipt was already
ingested. A different controller thread id is a hard-state blocker, not a
takeover signal. Never blind-resend or spawn a duplicate attempt.

Hard state is blocked only when the activation test concretely requires CAO and
the current-task CLI wrapper is unavailable or invalid. Do not silently
downgrade to conversational state in that case.

## Receipt Contract

Every child returns:

~~~yaml
subagent_receipt:
  assignment_id: <assignment id echoed exactly>
  execution_owner_id: <execution owner echoed exactly>
  agent: <logical project role>
  agenda_item: <task id>
  assigned_scope: <list>
  changed_files: <list; empty for read-only work>
  evidence: <non-empty material string list when done; packet-backed probe
    records use the compact JSON string contract above>
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
returned changes or findings, incorporate accepted graph deltas and `new_work`, run parent
verification/review, and mark the node done only when `done_when` is evidenced.
When CAO is active, persist a passed parent-verification outcome with evidence.
For every material follow-up, bind integration to concrete post-receipt task
ids or an atomic replan fingerprint, or record a rejected outcome with
evidence, before `cao complete`; `cao join` must reject any gap.

## Join And Thread Accounting

Before starting a dependent wave or accepting parent completion:

1. Every dispatched assignment has a receipt that is consumed, rejected, or
   converted into visible agenda state.
2. No failed or missing child result is treated as success.
3. Required parent inspection, verification, integration, and review are
   complete.
4. `list_agents` shows no running child that lacks an active agenda item. Use
   `interrupt_agent` for obsolete running work. Treat completed threads as
   bounded reusable residents. Use `followup_task` with a fresh complete
   assignment when a compatible resident's retained context saves setup;
   otherwise a fresh spawn is valid. When a new slot is required, V2
   automatically unloads the least-recently-used eligible resident whose status
   is `Completed`, `Errored`, or `Interrupted`. A resident is eligible only
   when it has no active turn and no pending mailbox. If fresh spawn returns
   `AgentLimitReached`, this reservation attempt did not successfully unload a
   resident: none may be eligible, or an eligible unload may have failed. Do not
   spin or blind-retry. Inspect resident/runtime state, continue
   capability-compatible root work, wait for a state change, or keep the node
   visibly blocked.
5. `~/.codex/bin/cao join` passes when durable state was active.

Thread state is capacity evidence, not semantic completion proof. A missing
thread without an accepted receipt keeps its task pending. Report the semantic
join result and remaining running child count; do not emit a per-event
transport ledger.

## Pressure Scenarios

- Bounded read-heavy scan: one or more `explorer` agents on Terra, dispatched
  in a profitable safe V2 wave up to available capacity; no CAO.
- Mechanical disjoint writer nodes: `worker` agents on Terra in one V2 wave,
  with canonical disjoint scopes and one parent integration barrier.
- Ambiguous cross-module or security change: a Sol `worker`, serialized when
  conflict proof requires it; CAO only when durable state is needed.
- Deep or exhaustive final review: a Sol `reviewer` with the review skill's
  required clean-pass loop.
- Cyclic multi-wave objective spanning an interruption in the same parent task:
  first run the activation test; use V2 alone when the controller can reread
  and recompute safely, otherwise use CAO task state and a parent-owned CLI
  join.
- Long read-only cross-turn investigation: V2 alone when its findings and
  ownership can be reread and recomputed; duration and persistence do not
  activate CAO.
- Resume needs an ownership lock and immutable attempt identity that cannot be
  reconstructed safely: activate CAO, and have the main lifecycle task use
  `~/.codex/bin/cao`; do not trust local stdio MCP `env_vars` or a supplied
  thread-id argument.
- Activation test requires CAO but `~/.codex/bin/cao` is unavailable or invalid:
  mark hard state blocked; do not downgrade to V2-only state.
- Parent discovers a new safe antichain during execution: refresh the graph and
  dispatch immediately instead of preserving the old serial order.
- Compatible second-wave work in the same parent turn: use `followup_task` on a
  completed agent with a fresh complete assignment and assignment id when its
  retained context saves setup; otherwise use a fresh spawn. Do not carry the
  previous task boundary forward implicitly.
- Resident capacity pressure: a fresh spawn may automatically unload the
  least-recently-used eligible `Completed`, `Errored`, or `Interrupted`
  resident. If it returns `AgentLimitReached`, this reservation attempt did not
  successfully unload one: none may be eligible, or an eligible unload may
  have failed. Do not spin or blind-retry. Inspect resident/runtime state,
  continue capability-compatible root work, wait for a state change, or leave
  the node visibly blocked.
- Scheduler pressure validation: hide compatible tasks in ready-sequence
  suffixes and use layouts that distinguish the stable-order fast path, bounded
  greedy portfolio, partial-wave improvement, residual-wave scoring, and clean
  budget exhaustion.
  Prove deterministic output, safety under capacity/dependency/active-lock/
  write-conflict constraints, greatest evaluated cardinality, residual-wave
  scoring before the lexicographic sorted-original-index tie-break,
  inclusion-maximal below-capacity results, and at most `n(n-1)/2` unique
  logical pair evaluations. Do not claim an exact/global maximum, globally
  minimal wave count, fixed approximation ratio, or never-underfill behavior.
- Receipt rejected before ingestion with a changed contract: atomically
  `replan` the exact active assignment, then dispatch the replacement.
- Receipt rejected before ingestion with an unchanged contract: release the
  exact active assignment, then dispatch a fresh attempt.
- Ingested failed or parent-rejected durable receipt with the same contract:
  resolve material follow-up during `reopen`, then dispatch again.
- Ingested receipt that changes any task-contract field: use atomic `replan`,
  then dispatch the replacement contract; never reopen and mutate later.
- Sol route unavailable: keep the node pending; do not claim Terra equivalence.
- V2 unavailable: block delegation and report the runtime requirement.
- User explicitly disables parallelism: preserve the graph, record
  `user_explicit_no_parallel`, and execute serially.
