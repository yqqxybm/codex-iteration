# Controller Protocol

Use this reference when `project-lifecycle` builds a multi-skill chain, advances
a plan or version, prepares Context Packets, consumes Handoff Records, writes a
trace, or finalizes a lifecycle task.

## Table Of Contents

- Call Chain Plan
- Protocol Evidence Gate
- Executable Plan Quality
- Plan Advancement Loop
- Context Packet
- Handoff Record
- Trace Placement
- Pressure Scenarios
- Final Response

## Protocol Evidence Gate

Referenced protocols are binding. When `project-lifecycle/SKILL.md` requires
this reference, the controller must prove that the reference changed execution
state instead of treating it as background reading.

Maintain compact evidence:

```yaml
protocol_evidence:
  loaded_references:
    - references/controller-protocol.md
    - <other required references, or none>
  active_protocols: <call_chain | plan_advancement | context_packet | handoff | trace | final_response>
  required_schemas: <call_chain_plan | agenda | context_packet | handoff_record | final_response>
  gates_applied: <analysis_gate | executable_plan_quality | stop_condition | verification_scope | none>
  stop_condition_checked: <true | false, with reason>
```

Do not claim a governed action progressed or completed unless
`protocol_evidence` shows the required reference, schemas, gates, and stop
condition were applied. If the evidence is missing, reopen the controller step
instead of allowing a downstream skill, commit, review, or verification command
to stand in for lifecycle completion.

## Call Chain Plan

Before downstream work starts, produce a compact plan:

```yaml
phase: <current lifecycle phase>
goal: <user-visible objective>
selected_chain:
  - skill: <skill-name>
    purpose: <why this skill is needed>
analysis_gate: <project-analysis required | explicitly_skipped_by_user>
success_criterion: <observable finish condition for the whole request>
standard_compliance_ledger: <required when a project is created, phase-advanced, or standard-audited>
codegraph_init_required: <true for new software project bootstrap unless explicitly not a code project>
goal_synthesis: <required for explicit 目标! / 目标！ or goal-backed concierge>
goal_preflight/optimality_law: <required before creating or maintaining a
  goal-backed tool goal>
tool_goal_prompt: <required before create_goal/maintain_goal; for looped goals,
  must include continue_while, reset_on, stop_only_when, and never_complete_from>
perspective_model: <required when review, optimization, product readiness,
  project-system, or Codex self-iteration judgment is part of the goal>
subagent_dispatch_policy: <auto_parallel_safe | blocked_by_runtime_or_tool_policy | unsafe_or_not_worth_it>
runtime_capability_probe: <subagent/custom-agent/worktree/background/concurrency evidence>
parallel_execution_mode: <sequential | subagent_wave | controller_team | workflow_batch,
  with task_graph, conflict edges, selected antichains, runtime capability,
  parallel ROI, merge strategy, join barrier, and optimality argument>
dynamic_mission_profile: <required for each subagent assignment; derived from task node, lenses, scope, verification, and risk>
loop_control_matrix: <required when goal, agenda, subagent, review, optimize, release, or sync loops interact>
review_clean_pass_loop: <review clean-pass counter and reset source when review depth requires clean passes>
optimize_framework_cycle_loop: <framework exhaustion cycle counter and reset source when deep optimization is active>
plan_state_sink: <trace_only | formal_plan_file | trace_and_formal_plan, with paths>
cyclic_goal_loop: <required for goal-backed advancement, version closeout, or release readiness>
stop_condition: <when not to continue the chain>
protocol_evidence: <loaded references, active protocols, gates, and stop-condition check>
```

Every selected skill must change the outcome. Do not include decorative steps.

## Executable Plan Quality

When this controller creates, normalizes, or advances a plan, the plan must be
executable rather than merely descriptive. Each required work item must name:

- the user-visible outcome,
- the owner skill,
- the owned files, modules, artifact, or project area when knowable,
- the exact verification command, artifact, or evidence expected,
- the verification scope matched to the change type,
- the observable `done_when` condition.

Reject placeholder planning. Items such as `TBD`, `TODO`, "handle edge cases",
"write tests", "similar to previous", or vague "improve/refactor" work are not
ready for execution unless they are expanded into concrete scope and evidence.
If missing detail changes the work, ask or block. If it can be inferred safely
from local context, state the assumption and encode it in the agenda.

Verification scope is part of the plan, not an executor afterthought. Do not
default docs-only or text-only work to broad runtime verification such as
`make verify`. Use docs evidence by default: final diff inspection,
`git diff --check`, touched reference/link/path/command checks, configured
Markdown/docs checks when present, and relative-time grep for durable docs.
Escalate to targeted runtime commands only when the docs changed runnable
commands, API/config/deploy/test instructions, or when the user explicitly
requested full project verification. Escalate to full project verification only
for code/runtime/build/release/security/compliance scope that justifies it.

For UI plans, propagate product-state risk instead of leaving it inside one page.
If a failure pattern appears in a list, table, log, alert, audit, access, card,
filter, action, or async state on one surface, identify sibling pages/components
using the same pattern. Add in-scope checks or fixes as agenda items unless the
user explicitly excluded them; otherwise record them as out-of-scope residual
risk.

## Plan Advancement Loop

When the user asks to "按计划推进", "根据计划全部推进", "继续推进到完成",
"做一个版本", "实现一个版本", "完成一个阶段", "MVP", "v0.x", or otherwise
execute an existing plan or version objective, enter plan advancement mode.

For "按计划推进", "根据计划全部推进", "继续推进到完成", "按已有重构方案",
or equivalent existing-plan requests, do not invent, shrink, or substitute the
plan. For version-state requests without an existing plan, build the controlling
agenda from the frozen charter plus the user's explicit version objective.

Before normalizing the agenda, search for plan sources in order:

1. explicit plan in the current user message,
2. active project trace agenda under `.codex/traces/`,
3. project docs, TODO/checklist files, issue files, roadmap files, refactor
   plans, migration plans, architecture notes, and Handoff Records named by the
   user,
4. visible conversation context.

When the user mentions a plan, refactor, migration, roadmap, checklist, or
phase, use targeted search terms such as `重构`, `refactor`, `plan`, `roadmap`,
`todo`, `checklist`, `migration`, `phase`, `handoff`, and `agenda`.

Maintain an internal source ledger:

```yaml
plan_sources:
  - source: <path, trace, document, issue, or conversation>
    evidence: <matched title, checklist, section, or agenda>
    selected: <yes | no>
    reason: <why this is or is not the controlling plan>
```

If no credible plan source is found for an existing-plan request, stop and ask
for the plan location. Do not proceed with a guessed or reduced agenda. If
multiple plausible plans would produce different work, ask which one controls.

If resuming from a trace, reconcile the agenda against current repo state before
continuing.

Choose the plan state sink before normalizing the agenda:

```yaml
plan_state_sink:
  mode: <trace_only | formal_plan_file | trace_and_formal_plan>
  trace_path: <.codex/traces/... or none>
  formal_plan_file: <project plan file path or none>
  reason: <why this sink is sufficient>
  update_policy:
    before_first_item: <required | not_applicable>
    before_each_item: <mark active and persist>
    after_each_item: <record result, verification, and next item>
    on_user_interruption: <flush active state and record change_request>
```

Use `trace_and_formal_plan` when the user says "项目计划文件", "版本计划",
"roadmap", "plan file", "任务列表", or names an authoritative plan/checklist
file. Use `formal_plan_file` when an existing project plan is the selected
source of truth and the chain is short enough that a trace would add no
recoverability value. Otherwise use `trace_only` for operational state.

If a formal plan file is required but no suitable file exists, add a
`project-docs` agenda item to create the smallest project-native plan state
file before implementation. Do not create a plan file merely to prove work was
done; create or update it only when it is the selected state sink or a durable
project planning artifact.

The controller owns the agenda. Downstream skills own only their assigned item.
First normalize the plan into a living agenda and task graph:

```yaml
agenda:
  - id: <stable short id>
    objective: <user-visible outcome>
    owner_skill: <project skill>
    prerequisites: <ids or none>
    source_plan_item: <source id, line, section, or none>
    owned_scope: <files, modules, artifact, or project area>
    related_surfaces: <sibling pages/components with the same UI pattern, if relevant>
    conflict_key: <file, schema, route, shared component, lockfile, config, deploy target, generated artifact, or none>
    dynamic_mission_profile: <base agent, specialization, execution lens, evidence surface, materiality standard, likely failure modes>
    standard_requirement: <guide requirement covered by this item, if any>
    done_when: <observable completion criterion>
    verification: <command, artifact, or evidence matched to the change type>
    status: <pending | active | done | blocked | skipped>
    result: <artifact, commit, decision, or none>
task_graph:
  dependency_edges: <blocking dependencies>
  conflict_edges: <unsafe concurrent writer or shared-state conflicts>
  antichains: <parallel-safe groups>
  critical_path: <ids that determine minimum elapsed work>
parallel_execution_mode:
  runtime_capability_probe:
    subagent_spawn_mechanism: <callable | unavailable | blocked_by_policy>
    custom_project_agents: <available | unavailable | unknown>
    worktree_isolation: <available | unavailable | unknown>
    thread_or_background_sessions: <available | unavailable | not_requested>
    max_parallel_agents: <number | unknown>
    evidence: <tool discovery, runtime output, or explicit policy>
  selected: <sequential | subagent_wave | controller_team | workflow_batch>
  parallel_roi:
    expected_saved_work: <material | marginal | none>
    coordination_cost: <low | medium | high>
    decision: <parallelize | sequentialize>
  merge_strategy:
    isolation: <read_only | same_worktree_disjoint | isolated_worktree_if_supported | main_applies_patch>
    join_barrier: required
    integration_owner: main lifecycle thread
    conflict_resolution: <reject | serialize | main_applies_patch>
  optimality_argument: <why this is the smallest correct coordination mode>
```

Loop invariant: the plan is not complete while any required item is `pending`,
`active`, unverified, or while concierge `cyclic_goal_loop` has material
in-scope issues, unmet commit/push/deploy/health requirements, or insufficient
clean passes.

Before invoking downstream skills, run the Executable Plan Quality gate over the
agenda and the task graph. Do not start a vague item and hope the downstream
skill discovers the missing scope. Do not parallelize until dependency edges,
conflict edges, selected antichain, owner, `done_when`, verification evidence,
runtime capability, ROI, isolation/merge strategy, dynamic mission profiles, and
join barrier are known.

Loop until the agenda reaches a real stop condition:

1. Select the highest-priority `pending` item whose prerequisites are met.
2. Mark selected items `active` and persist the state to `plan_state_sink`
   before invoking a downstream skill or subagent.
3. In concierge mode, or any multi-item agenda with independent work surfaces,
   select the next execution set from `parallel_execution_mode`: one item for
   `sequential`, the current antichain for `subagent_wave`, a lead-assigned
   wave for `controller_team`, or the current phase wave for `workflow_batch`.
   Apply `references/goal-subagent-orchestration.md`. If runtime capability,
   ROI, or isolation evidence does not support the selected parallel mode,
   downgrade to the nearest valid mode and record the reason as a capability
   boundary, not as an equivalent execution path.
4. Build a Context Packet for each selected item and invoke the owning skill or
   bounded project subagent.
5. Record Handoff Records and subagent receipts, then update the agenda and
   persist the result to `plan_state_sink`.
6. Mark the item `done` only when its `done_when` and verification evidence are
   satisfied and the source plan requirement is preserved.
7. If the handoff creates new required work, add it to the agenda instead of
   leaving it implicit.
8. If a handoff recommends another skill, convert that recommendation into an
   agenda item or explicitly reject it as outside scope.
9. Continue to the next eligible `pending` item without returning a final answer.

Do not stop merely because one downstream skill, commit, or verification step
finished. Stop only when:

- all agenda items are `done` or explicitly `skipped` with a user-approved
  reason,
- a blocker requires user input, secret access, destructive approval, or an
  unsafe operation,
- verification fails after reasonable local fixes and further work would hide
  the failure,
- the environment forces interruption; in that case write or update the trace,
  name the next agenda item, and do not claim the plan is complete.

If the user sends a new requirement, correction, interruption, or priority shift
while a version/goal agenda is active, run interruption reconciliation before
new execution:

```yaml
interruption_reconciliation:
  active_item_status: <done | active | blocked | stale>
  flushed_evidence: <latest files, commands, receipts, or none>
  incoming_change_request:
    source: <user message>
    requested_change: <what changed>
    impact: <agenda item, root direction, docs/assets, tests, release, or none>
    decision: <add_now | replace_item | defer | reject | ask>
    reason: <why this preserves the goal and version boundary>
  preserved_items: <unchanged agenda item ids and statuses>
  state_sink_updated: <trace | formal_plan_file | both | blocked>
```

Never replace the active agenda with the new request. Preserve existing item
statuses, flush the active item state to `plan_state_sink`, then add, replace,
defer, reject, or ask about the new requirement through `change_request`.

For plan advancement with more than two items, create or update a trace from the
start before the first item begins, then update it after each item. The trace
must include the source ledger, agenda table, last completed item, current
blocker if any, and next item. It is a recoverability ledger and completion
proof, not a backup.

An agenda item can be `done` only when:

- its source plan requirement is satisfied,
- its `done_when` condition is met,
- its verification evidence is recorded,
- any newly discovered in-scope required work has been added or completed.

If verification cannot run, mark the item `blocked` unless the user explicitly
accepts an unverified completion status.

## Context Packet

Before using a downstream skill, carry forward only the context it needs:

```yaml
intent: <user goal>
constraints: <hard limits and preferences>
decisions_so_far: <accepted decisions>
owned_scope: <files, modules, project area, or phase responsibility>
project_goal/goal_runtime/cyclic_goal_loop/subagent_dispatch_policy/agent_owner/write_policy:
  <when concierge mode is active>
parallel_execution_mode/task_graph:
  <selected mode, dependencies, conflict edges, active antichain or phase, and
  why the assigned item is safe to run now>
runtime_capability_probe/parallel_roi/merge_strategy:
  <capabilities, ROI decision, write isolation, integration owner, and join barrier
  when subagents or parallel execution are considered>
dynamic_mission_profile:
  <base agent, specialization, execution lens, evidence surface, materiality
  standard, likely failure modes, and why this profile is derived from the task node>
loop_control_matrix:
  <active loops, reset edges, stop precedence, and non-equivalent counters when
  multiple loops interact>
review_clean_pass_loop/optimize_framework_cycle_loop:
  <active counter, clean target, reset source, and why one loop cannot count as the other>
plan_state_sink:
  <trace/formal plan state sink, active item, and update policy when agenda is active>
goal_synthesis/control_system_goal:
  <target layer, state model, sensors, actuators, hardness, delivery,
  escalation, and stop condition when 目标! / 目标！ is active>
goal_preflight/optimality_law:
  <material model, calibration, task-specific value ordering, elegance
  constraint, non-goal boundary, and falsification test>
perspective_model:
  <material role/lens summaries to preserve for review, optimization, product
  readiness, project-system, or Codex self-iteration work>
doc_profile: <when docs/assets are involved>
docs_ia: <authorized root docs and docs/ subdirectories when standalone docs are involved>
verification_required: <actual command or evidence expected>
verification_scope: <docs-only | focused-code | ui | config/build | release | security | full-project>
standard_compliance_ledger: <relevant guide entries and required status updates>
ui_contract: <when downstream work is UI, core workflow and relevant operating conditions>
codegraph_init_required: <true for new software project bootstrap unless explicitly not a code project>
related_surfaces: <same-pattern pages/components to inspect or explicitly exclude>
do_not_do: <explicit exclusions, quality-reduction bans, or boundaries>
protocol_evidence: <required controller protocols and gates the downstream skill must preserve>
```

## Handoff Record

After each downstream skill finishes, record a short handoff:

```yaml
skill: <skill-name>
status: <done | blocked | skipped>
changed_artifacts: <files, commands, docs, commits, or none>
decisions: <new decisions made>
verification: <command and key result>
verification_scope: <docs-only | focused-code | ui | config/build | release | security | full-project>
subagent_dispatch_policy/subagent_receipts/goal_runtime/goal_status:
  <dispatch policy, receipts consumed, and goal state, or none>
parallel_execution_mode/task_graph_delta:
  <selected mode, wave/phase joined, new dependencies/conflicts/blocked/unblocked
  items, suggested reclassification, or none>
runtime_capability_probe/parallel_roi/merge_strategy_delta:
  <capability evidence, ROI changes, merge conflicts, serialized items, or none>
dynamic_mission_profile_delta:
  <profile sufficient, missing lens/surface, recommended profile change, or none>
loop_control_matrix_delta:
  <counter resets, clean-pass increments, stop-condition changes, or none>
review_clean_pass_loop/optimize_framework_cycle_loop_delta:
  <increment, reset, satisfied, blocked, or not_applicable with reason>
cyclic_goal_delta: <material issues, clean-pass reset/increment, commit/push/deploy/health state, or none>
frontend_evidence_packet: <when UI work occurred, verified and unverified conditions>
standard_compliance_delta: <guide entries satisfied, missing, deferred, blocked, or not_applicable>
codegraph_status: <initialized/indexed/status output or blocked reason, when bootstrap occurred>
domain_resource_evidence: <software-contract references loaded or missing, when used>
open_risks: <remaining blockers or risks>
next_recommended_skill: <next skill or none>
agenda_update: <done, blocked, added, or remaining items>
plan_state_sink_delta: <trace/formal plan paths updated, active item flushed, or blocked>
protocol_evidence_delta: <protocol gates satisfied, reset, blocked, or missing>
```

If the handoff changes the original plan, update the call chain before
continuing.

## Trace Placement

Use the lightest trace that preserves recoverability:

1. **Short chain**: keep the trace in the conversation and final response only.
2. **Long, cross-phase, or resumable chain**: create a project-local trace at
   `.codex/traces/<YYYY-MM-DD>-<task-slug>.md`.
3. **Durable project knowledge**: promote only long-lived facts into
   `README.md`, project `AGENTS.md`, or `docs/` through `project-docs`.

Trace files are operational working records, not backups and not formal docs.
Do not commit `.codex/traces/` by default. Commit them only if the user asks for
trace history to be part of the repository. If `.codex/traces/` reveals a durable
decision, command, environment variable, API, deployment detail, or lesson,
promote that fact to formal docs and keep the trace minimal.

## Pressure Scenarios

- "`目标! <outcome>` or `目标！ <outcome>`": load this reference and
  `references/goal-subagent-orchestration.md`, synthesize
  `goal_preflight`, `goal_synthesis.control_system_goal`, `tool_goal_prompt`,
  `parallel_execution_mode`, and the goal prompt elegance gate before creating a tool goal, asking, or
  executing. The prompt passed to the goal tool must contain the loop contract
  whenever the selected loop mode is not `single_pass`. Let the
  controller choose target layer, loop hardness, review scope/depth,
  verification, commit/push/deploy/sync applicability, escalation boundary,
  non-goal boundary, and stop condition.
- "`目标! <large audit/migration/version closeout>`": build a task graph before
  implementation. Use `subagent_wave` for one independent antichain,
  `controller_team` for multi-wave project work with evolving agenda, and
  `workflow_batch` for many similar items or cross-checked research/review.
  Use `sequential` when conflict edges, dependencies, missing runtime capability,
  weak ROI, or merge risk dominate. Do not imply peer-to-peer agent coordination,
  nested agents, background sessions, or isolated worktrees unless current
  runtime evidence proves those capabilities. For every delegated node, derive a
  `dynamic_mission_profile`; do not assume the task graph alone tells the agent
  how to execute the node.
- "`目标! 推进小版本，把优化点落到项目计划文件`": use `plan_state_sink:
  trace_and_formal_plan`, create or update the smallest authoritative project
  plan file through `project-docs` if none exists, mark items active before
  execution, write result/verification after each item, and record
  `change_request` for every mid-run user addition.
- "`目标! 审查/优化/深度审查优化 <target>`": synthesize a
  `goal_preflight`, task-specific `optimality_law`, and `perspective_model`
  before the agenda. Generate material lenses from the target and evidence
  rather than copying a fixed persona list. Carry those lenses into review,
  optimize, and subagent prompts so the work covers user value, product quality,
  engineering quality, architecture, operation/security, competitive adoption,
  and future-agent behavior only where each lens can change the finding,
  optimization, or stop condition.
- "只改这个 diff / 单点改动 / 不做整体推进": keep scope focused, do not create
  a goal, record `analysis_gate: explicitly_skipped_by_user` only when the user
  explicitly skipped broader analysis, and keep final review labeled focused.
  `protocol_evidence` must show the focused boundary and stop condition.
- "做一个版本 / MVP / v0.x": treat as version-state work, create or consume a
  frozen charter, build an agenda with source/result/verification evidence, and
  do not downgrade to one local iteration. If the user asks to finish or close
  out the version, also load `references/goal-subagent-orchestration.md`.
- "继续推进直到完成 / 两轮全局审查无新增问题 / 没有遗留问题": load both this
  reference and `references/goal-subagent-orchestration.md`, maintain
  `cyclic_goal_loop` and `loop_control_matrix`, reset clean passes on material
  in-scope issues, and stop only at the combined
  agenda/verification/review/optimization/known-issue boundary.
- "改完再深度 review / 全面审查不要只看改动": implement through the selected
  executor, then use the `review` skill at the requested depth. A focused
  closeout gate cannot be reported as deep or exhaustive review.
- "核验/检查文档": default to findings or targeted docs evidence. Do not create
  new docs or run broad runtime verification unless the user asked to modify
  docs, the authoritative doc is missing and required, or the changed text
  affects runnable commands, API/config/deploy/test instructions.

## Final Response

A project-lifecycle task is complete only when the selected downstream skills
have finished their own verification gates and, in plan advancement mode, every
required agenda item is `done` or explicitly user-approved as `skipped`.

The final response names:

- phase handled,
- call chain used,
- agenda completion status, if plan advancement mode was used,
- project goal runtime/status and subagent receipt summary, when concierge mode
  was used,
- subagent dispatch policy and fallback reason when automatic parallelism was
  evaluated,
- parallel execution mode, runtime capability evidence, ROI decision, task graph
  summary, selected antichains/phases, merge strategy, join result, and why the
  chosen mode was the smallest correct coordination structure,
- dynamic mission profiles used for subagents, and any rejected promotion into a
  new static agent type,
- cyclic goal loop state and stop-condition evidence, when goal-backed
  advancement was used,
- loop control matrix state when multiple loops interacted,
- change requests accepted, deferred, rejected, or still blocking during
  version-state work,
- concrete artifact or decision produced,
- verification evidence, including verification scope when narrower or broader
  than normal,
- standard compliance status and remaining gaps, when the contract was active,
- CodeGraph initialization/index status, when project bootstrap occurred,
- `domain_resource_evidence`, when `software-contract` was loaded,
- `protocol_evidence`, when controller references governed the work,
- trace location, if a trace file was created,
- remaining lifecycle gap, if any.
