# Controller Protocol

Use this reference when `project-lifecycle` builds a multi-skill chain, advances
a plan or version, prepares Context Packets, consumes Handoff Records, writes a
trace, or finalizes a lifecycle task.

## Table Of Contents

- Call Chain Plan
- Protocol Evidence Gate
- Executable Plan Quality
- Plan Advancement Loop
- Runtime Resource Ledger
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
  active_protocols: <call_chain | plan_advancement | goal_orchestration |
    subagent_execution | context_packet | handoff | trace | final_response>
  required_schemas: <only the authoritative schemas loaded for this request>
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
phase: <earliest unresolved lifecycle phase and accepted upstream commitments>
goal: <user-visible objective>
selected_chain:
  - skill: <skill-name>
    purpose: <which unresolved commitment or requested outcome this skill owns>
analysis_gate: <project-analysis required | explicitly_skipped_by_user |
  not_required_read_only | not_required_very_small>
discovery_gate: <required | ready_for_adoption | adopted | rejected |
  model_reset (discovery-owned only) | blocked | insufficient | not_applicable>
success_criterion: <observable finish condition for the whole request>
skill_system_best_practice_packet: <required for fuzzy or under-specified project intents; input to goal prompt synthesis when goal-backed>
standard_compliance_ledger: <required when a project is created, phase-advanced, or standard-audited>
codegraph_init_required: <true for new software project bootstrap unless explicitly not a code project>
goal_synthesis: <required for explicit 目标! / 目标！ or goal-backed concierge>
goal_preflight/optimality_law: <required before creating or maintaining a
  goal-backed tool goal; must include candidate calibration questions and
  ask-or-not-ask handling>
tool_goal_prompt: <required before create_goal/goal reconciliation; for looped goals,
  must include continue_while, reset_on, stop_only_when, and never_complete_from>
perspective_model: <required when review, optimization, product readiness,
  project-system, or Codex self-iteration judgment is part of the goal>
project_optimality_packet: <authoritative revisioned project-quality evidence
  when its state must survive broad/unqualified review or optimization,
  cross-phase or resumable work, multi-agent work, or concurrent mutation>
subagent_execution: <required for independent work or delegation; authoritative
  dispatch proof, assignment, receipt-join, and thread-accounting state from
  references/subagent-execution.md>
runtime_resource_ledger: <required when lifecycle creates a non-subagent server, browser, terminal, ssh, tunnel, automation, or other long-lived runtime handle>
loop_control_matrix: <required when goal, agenda, subagent, review, optimize, release, or sync loops interact>
review_clean_pass_loop: <review clean-pass counter and reset source when review depth requires clean passes>
optimize_framework_cycle_loop: <framework exhaustion cycle counter and reset source when deep optimization is active>
plan_state_sink: <trace_only | formal_plan_file | trace_and_formal_plan, with paths>
cyclic_goal_loop: <required for goal-backed advancement, version closeout, or release readiness>
stop_condition: <when not to continue the chain>
protocol_evidence: <loaded references, active protocols, gates, and stop-condition check>
```

The selected chain begins at the earliest unresolved commitment and reaches the
user's requested outcome. Omit an earlier phase only when its state is already
accepted or genuinely not applicable; do not infer readiness from the user's
action verb or the existence of implementation-shaped artifacts. Every selected
skill must change the outcome, so accepted phases are not replayed decoratively.
`project-analysis required` is only a pre-execution plan state; before any
executor Context Packet or task node, it must become
`project_analysis_consumed` or stop at the analysis gate.

### Skill-System Best-Practice Packet Gate

Before writing `tool_goal_prompt` for a goal-backed request, or before handing off
any fuzzy project request, synthesize `skill_system_best_practice_packet` from the
current skill system. This packet is not the final `tool_goal_prompt`; it is the
skill-utilization layer that teaches the controller which existing skills,
adapters, resources, contracts, and verification gates should shape the final
prompt and Context Packet.

The packet must consider the available skill metadata, then read the `SKILL.md`
for selected owner skills and any ambiguous competing skill. Do not read every
unrelated skill body for ordinary requests, but do consider all materially
relevant skill families before selecting the chain. For Codex skill-system
optimization, review, or self-iteration, broaden the survey to all affected
skills and cross-skill references.

```yaml
skill_system_best_practice_packet:
  user_surface_request: <raw user wording>
  inferred_target: <task class>
  skill_survey: <metadata considered; selected and rejected skills with reasons>
  codex_written_task_prompt: <task-specific execution prompt fragment>
  skill_system_utilization: <skills, adapters, resources, and contracts used or skipped>
  quality_defaults: <applicable quality and loop defaults>
  required_contracts: <resource, review, delivery, and verification contracts>
  downstream_chain: <selected owner chain>
  verification_defaults: <commands, artifacts, or evidence>
  relationship_to_tool_goal_prompt: <input_only | not_applicable>
  user_not_required_to_supply: <control details inferred by Codex>
  blocking_question_boundary: <non-substitutable user perspective with material
    effect on understanding or commitment, or none>
```

This is controller-owned context, not user homework. In goal-backed work it is
input to, never a replacement for, the final `tool_goal_prompt`.

The gate fails if:

- the user is asked to write the best-practice prompt, name routine skills, choose
  ordinary review/optimization hardness, or provide stop conditions that Codex can
  infer from the skill system and project evidence,
- a goal-backed `tool_goal_prompt` ignores the packet's selected skills,
  contracts, verification defaults, or stop-condition implications,
- the packet is passed to `create_goal` as if it were the final
  `tool_goal_prompt`.

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
If missing detail changes the work, resolve it from local context when Codex can
do so responsibly. Ask and block only when the user's perspective is
non-substitutable and materially affects the understanding or commitment;
otherwise record any real external blocker in the agenda.

Verification scope is part of the plan, not an executor afterthought. Choose the
smallest appropriate evidence that can genuinely challenge the item's reasoning
and `done_when` claim; do not manufacture checks, ledgers, or artifacts merely
to make status observable or closable. Do not default docs-only or text-only
work to broad runtime verification such as
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
    on_user_interruption: <flush active execution state, then apply State Boundary Enforcement>
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
subagent_execution: <required state summary from
  references/subagent-execution.md, or not_applicable with evidence>
```

Loop invariant: the plan is not complete while any required item is `pending`,
`active`, unverified, or while concierge `cyclic_goal_loop` has material
in-scope issues, unmet commit/push/deploy/health requirements, or insufficient
clean passes, while non-subagent runtime resources remain open without a visible
keep-open policy, or while the subagent receipt-join/thread-accounting gate is unsatisfied.

Before invoking downstream skills, run the Executable Plan Quality gate over the
agenda and the task graph. Do not start a vague item and hope the downstream
skill discovers the missing scope. Do not parallelize until dependency edges,
conflict edges, selected antichain, owner, `done_when`, verification evidence,
and the complete dispatch proof required by
`references/subagent-execution.md` are known.
For any agenda with multiple independent surfaces, sequential mode is valid only
when `parallel_blocker` names why parallel execution is impossible or materially
unsafe. Missing parallel proof is not a reason to run sequentially; it is a
controller bug to fix before execution.

Loop until the agenda reaches a real stop condition:

1. Select the highest-priority `pending` item whose prerequisites are all
   `done`. A skipped prerequisite is not met: before a successor can run, the
   parent must replan and remove or replace the edge, visibly block the
   successor, or skip it with a user-approved reason.
2. Mark selected items `active` and persist the state to `plan_state_sink`
   before invoking a downstream skill or subagent.
3. In concierge mode, or any multi-item agenda with independent work surfaces,
   select the next execution set from `subagent_execution.mode`: one item for
   `sequential`, the current antichain for `subagent_wave`, a controller-selected
   wave for `controller_team`, or the current phase wave for `workflow_batch`.
   Apply `references/subagent-execution.md`. If ROI or isolation evidence does
   not support the selected parallel mode, reclassify to the nearest valid mode
   and record the exact blocker. If V2 is unavailable or blocked, keep delegated
   nodes blocked as required by that reference; do not reclassify them into a
   sequential substitute.
   When the subagent execution record marks CAO durable state active, run the
   required `cao` command before the corresponding lifecycle transition; do
   not satisfy the hard-state gate with in-conversation YAML alone.
4. Build a Context Packet for each selected item and invoke the owning skill or
   bounded project subagent through V2. Keep only the compact V2 wave state
   required by `references/subagent-execution.md`; register non-subagent
   long-lived handles in `runtime_resource_ledger`.
5. Record Handoff Records, subagent receipts, and runtime-resource deltas, then
   update the agenda and persist the result to `plan_state_sink`.
6. Mark the item `done` only when its `done_when` and verification evidence are
   satisfied and the source plan requirement is preserved.
7. If the handoff creates new required work, add it to the agenda instead of
   leaving it implicit. When CAO is active, add concrete follow-up nodes after
   the source receipt and bind them during completion or same-contract reopen.
   If the source node's own scope, dependencies, conflicts, owner, lens, done
   condition, or verification changes, persist the complete replacement with
   atomic `cao replan` before redispatch.
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
- lifecycle-created runtime resources cannot be closed, proven auto-closed, or
  explicitly kept open with a user-visible reason,
- the subagent receipt-join or thread-accounting gate remains unsatisfied,
- the environment forces interruption; in that case write or update the trace,
  name the next agenda item, and do not claim the plan is complete.

If the user sends new input while a version or goal agenda is active, flush only
the current execution facts needed for recovery and apply State Boundary
Enforcement before deciding how the agenda changes. A new requirement, priority
shift, or correction classified as a user-confirmed change to an already accepted
goal, scope, or priority uses interruption reconciliation before new execution:

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

Preserve only agenda items whose accepted basis remains valid after State
Boundary Enforcement, then apply its resulting bounded repair, existing
`change_request`, or `model_reset` and replan consequence. This protocol does not
classify corrections or create a correction record.

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

## Runtime Resource Ledger

When lifecycle work creates a non-subagent runtime handle that can outlive the
immediate tool call, track it explicitly. This covers reusable browser or app
sessions, dev servers, background terminal commands, SSH tunnels, remote batch
sessions, automations, and any other non-subagent handle that can consume quota,
ports, state, or attention after the semantic work appears done. V2 subagent
threads are governed only by `references/subagent-execution.md`.

Use the ledger only for resources created or taken over by the lifecycle task;
do not inventory unrelated user processes.

```yaml
runtime_resource_ledger:
  - id: <tool/session/process id, port, host, or handle>
    type: <dev_server | browser | terminal_session | ssh_tunnel | remote_batch | automation | other>
    owner: <main lifecycle thread | downstream skill>
    purpose: <why it was created>
    agenda_item: <id or none>
    state: <active | completed | failed | abandoned | kept_open | closed | not_found | not_applicable>
    close_policy: <close_after_receipt | close_after_verification | keep_open_for_user | runtime_auto_closes | none>
    close_evidence: <command/tool result, URL disclosed to user, or reason>
```

Completion rules:

- A lifecycle task may not claim complete while any runtime resource remains
  active, completed-but-unclosed, failed-without-decision, or unaccounted.
- `kept_open` is valid only when the user benefits from it, such as a dev server
  URL to try, and the final response names the handle and reason.
- `not_applicable` is valid only when no persistent handle was created or the
  runtime proves auto-cleanup.
- Do not record credentials, tokens, secret values, or private session contents
  in the ledger.

## Context Packet

Before using a downstream skill, carry forward only the context it needs:
Evaluate the Project Optimality State Contract activation conditions before
dispatch. When project-quality evidence must survive broad/unqualified review or
optimization, cross-phase or resumable work, multi-agent work, or concurrent
mutation, `project-lifecycle` initializes the packet before dispatch and supplies
the full packet, a resolvable reference, or a typed bounded projection. A
downstream skill must return to lifecycle if required persistent state is
missing; it must not silently substitute ephemeral probes. When none of those
conditions applies, keep bounded probes ephemeral.

A Context Packet is a typed bounded projection, not a form to fill. Include only
active fields the recipient can use or invalidate. An absent field is inactive,
not a request for a placeholder. Downstream skills preserve the supplied
authority and return only relevant deltas; they do not reconstruct, echo, or
instantiate the rest of this vocabulary.

When persistent project-optimality context is active, load both
`~/.agents/skills/software-contract/references/coding-quality-contract.md` and
`~/.agents/skills/software-contract/references/project-optimality-state-contract.md`
and record them in `protocol_evidence`.

An upstream report, analysis, audit, proposal, or retrospective defaults to
`evidence_only`. Its observations, hypotheses, and recommendations may inform
judgment, but they do not become accepted decisions, requirements, agenda items,
acceptance criteria, review coverage, or scope changes until the controller
records an explicit in-scope decision through the applicable existing
transition: adoption, `change_request`, or `model_reset`. This is a semantic
boundary, not a new packet or ledger.

```yaml
intent: <user goal>
constraints: <hard limits and preferences>
decisions_so_far: <controller-accepted decisions; upstream proposals remain evidence_only>
discovery_gate: <status and adoption boundary when project-discovery is active>
discovery_handoff: <evidence-only discovery result or resolvable reference,
  supplied only to an adoption decision owner>
analysis_gate: <project_analysis_consumed | explicitly_skipped_by_user |
  not_required_read_only | not_required_very_small>
analysis_gate_evidence: <Stage 3 decision and implementation boundary, exact
  analysis-waiver wording, concise read-only proof, or concise proof of every
  very_small condition>
owned_scope: <files, modules, project area, or phase responsibility>
skill_system_best_practice_packet:
  <controller-written normalized prompt for fuzzy requests: raw user wording,
  inferred target, skill survey, codex-written task-prompt fragment, quality
  defaults, required contracts, selected skill-system utilization, downstream chain,
  verification defaults, relationship to tool_goal_prompt, what the user is not
  required to supply, and blocking-question boundary>
project_goal/goal_runtime/cyclic_goal_loop:
  <when concierge mode is active>
runtime_resource_ledger:
  <created long-lived runtime handles, close policy, and close evidence>
subagent_execution:
  <only the bounded assignment for a child, or the compact parent execution
  summary required by references/subagent-execution.md; never the full parent
  graph, V2 wave, CAO, or loop state when the recipient does not need it>
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
  <compact projection of project_optimality_packet, or material non-software
  role/lens summaries>
project_optimality_packet:
  <authoritative project-quality evidence packet or resolvable revision-pinned
  project_optimality_ref for broad review/optimization, never a replacement for
  project_goal or optimality_law;
  bounded recipients receive a typed project_optimality_projection>
doc_profile: <when docs/assets are involved>
docs_ia: <authorized root docs and docs/ subdirectories when standalone docs are involved>
verification_required: <actual command or evidence expected>
verification_scope: <docs-only | focused-code | ui | config/build | release | security | full-project>
standard_compliance_ledger: <relevant guide entries and required status updates>
ui_contract: <when downstream work is UI, core workflow and relevant operating conditions>
aesthetic_target_level: <AQ1 local-integrity | AQ2 production-grade | AQ3 benchmark-grade, plus inherited floor and evidence basis>
visual_target_gate: <required | not_applicable, with reason>
aesthetic_generation_packet: <concrete beauty mechanism and implementation translation when Tier 2/3/high-aesthetic UI is in scope>
visual_target: <concrete visual target or required downstream output when Tier 2/3/high-aesthetic UI is in scope>
frontend_skill_experiment: <rule hypothesis, experiment path, pass threshold, and failure-to-skill feedback rule when a frontend skill/prompt is being validated by an experimental page>
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
decisions: <controller-accepted decisions only; otherwise proposals/evidence>
state_transition_delta: <discovery handoff or adoption, change_request,
  model_reset with owning stage and causal descendants, or not_applicable>
verification: <command and key result>
verification_scope: <docs-only | focused-code | ui | config/build | release | security | full-project>
goal_runtime/goal_status: <goal state, or none>
runtime_resource_delta:
  <created, kept_open, closed, not_found, close_failed, or not_applicable handles>
subagent_execution_delta:
  <accepted receipt/graph changes, mode or model-route changes, join and
  thread-accounting state, CAO evidence when active, or none; use the authoritative
  schema from references/subagent-execution.md>
loop_control_matrix_delta:
  <counter resets, clean-pass increments, stop-condition changes, or none>
review_clean_pass_loop/optimize_framework_cycle_loop_delta:
  <increment, reset, satisfied, blocked, or not_applicable with reason>
goal_review_delta:
  <review depth, material new work, clean-pass delta, inspected stop surfaces,
  and residual issues, or not_applicable>
project_optimality_delta:
  <typed base-revision delta for model, concerns, probes, append-only evidence,
  invalidation, and human decisions, or none>
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

If the handoff proposes a change to the original plan, the controller must first
apply State Boundary Enforcement and accept it through the applicable adoption,
`change_request`, or `model_reset` transition, then update the call chain before
continuing.

An accepted `model_reset` invalidates its named causal descendants before
replanning, reopens the stage that owns the failed judgment, and prevents those
tests, docs, or current implementation from being used to re-establish the old
decision. When the reset is discovery-owned, also apply the authoritative
discovery-to-adoption transition from `references/state-transitions.md`; an
adoption recommendation from `project-analysis` still requires controller
acceptance.

Validate and merge every `project_optimality_delta` against the
controller-owned packet before replanning, optimization, review, or a clean-pass
increment. Apply the revision, idempotency, stale-merge, evidence-invalidation,
and derived-completion rules from the Project Optimality State Contract.
A pending human decision must remain in the packet and `open_risks` or blocking
state for every affected claim; it cannot disappear through summarization or
handoff.

## Trace Placement

Use the lightest trace that preserves recoverability:

1. **Short chain**: keep the trace in the conversation and final response only.
2. **Long, cross-phase, or resumable chain**: create a project-local trace at
   `.codex/traces/<YYYY-MM-DD>-<task-slug>.md`.
3. **Durable project knowledge**: promote only long-lived facts into
   `README.md`, project `AGENTS.md`, or `docs/` through `project-docs`.

Trace files are operational working records, not backups and not formal docs.
For a long chain with `project_optimality_packet`, the trace stores the
authoritative packet snapshot and merged deltas. Any
`project_optimality_ref` must name that trace section, exact revision, content
hash, and assigned probe ids. Do not persist a second perspective or review
ledger.
Do not commit `.codex/traces/` by default. Commit them only if the user asks for
trace history to be part of the repository. If `.codex/traces/` reveals a stable
project fact or controller-accepted durable decision, route it to `project-docs`
and keep the trace minimal. Task-local boundaries, review verdicts, evidence
gaps, process proof, and one-off lessons remain operational trace unless they
pass the durable-promotion rule; never turn them into formal documentation
merely because they were recorded.

## Pressure Scenarios

- "`目标! <outcome>` or `目标！ <outcome>`": load
  `references/goal-orchestration.md`; when independent surfaces exist, also load
  `references/subagent-execution.md`. Apply both authoritative gates before goal
  activation or delegation.
- "改一下这个弹窗 / 优化一下前端 / 仿照已有网站写一个后台管理页 / 做一个前端 /
  写个页面 / 做个组件 / 做个 dashboard/admin": synthesize
  `skill_system_best_practice_packet` before execution. The packet chooses UI tier,
  AQ target, design contracts, reference-sourcing/default prototype policy,
  local-style extraction for small components, browser/visual/state
  verification, and the owner chain. A vague visible component modification
  defaults to AQ2 and a holistic rendered aesthetic verdict; task/interaction
  success alone is not completion. AQ1 is reserved for an explicit mechanical
  preservation instruction. For full pages, dashboards, admin/workbench
  surfaces, redesigns, or source-inspired UI, default to `project-frontend`
  extreme-quality behavior:
  theme/prototype reference, visual target before implementation, and the
  smallest sufficient rendered aesthetic judgment; use `batch_audit` when the
  reference space is broad or source quality matters. The user must not need to
  provide a polished prompt, reference list, screenshot plan, source-level
  wording, or UI checklist.
- "目标! 循环优化前端 skill，并用实验网页验证": treat the experiment as a
  skill-validation fixture, not merely a deliverable page. Context Packet must
  carry `frontend_skill_experiment` with the rule hypothesis, path, visual
  target, and pass threshold. If rendered screenshot QA says the result is
  correct but not beautiful enough, generic, or weaker than the target, reset
  the loop and classify the cause. Patch skills/resources first for
  `control_law_gap`; regenerate the experiment from updated rules after any
  skill patch. Only an `application_gap` or `implementation_gap` may be fixed by
  rewriting the page without changing the skill.
- "初始化一个项目 / 做一个 app / 搭一个工具": synthesize
  `skill_system_best_practice_packet` plus `frozen_charter` when needed. Start at
  the earliest unresolved commitment: use discovery and adoption when user or
  product reality must decide the product, otherwise begin with `project-brief`;
  then use visible `project-analysis` and `project-bootstrap`. Let Codex select
  production bootstrap defaults, standard ledger, docs profile, runnable vertical
  slice, CodeGraph, and verification evidence.
- "移动一个图标 / 改一个错字 / 调一个局部间距或颜色": when the edit is clearly
  a reversible single-semantic-surface adjustment with no behavior, workflow,
  architecture, docs, durable-test-contract, release, security, data,
  design-direction, or independent cross-file/cross-module impact, keep a light
  focused packet: preserve local conventions, inspect the directly affected
  surface, run focused verification, and do not escalate to full project or
  high-aesthetic workflow. Removing or relaxing an incidental assertion that
  merely mirrors a mutable literal remains part of that same light change.
- "在现有项目里加一个弹窗/表格/组件/小功能": do not assume this is light. Unless
  the user wording and local evidence prove it is the tiny-edit case above,
  locate the earliest unresolved commitment first. A concrete accepted product
  boundary may proceed to `project-analysis`; a claim about what users need whose
  actor/task/value relation is unresolved starts with `project-discovery`, while
  accepted reality with an unclear requirement boundary starts with
  `project-brief`. Then synthesize the smallest sufficient owner implementation,
  directly affected docs/tests, local-style or UI contracts when UI is involved,
  focused/deep review according to wording, version management, and
  verification/stop conditions.
- "改一下 / 修一下 / 加个功能 / 重构一下": synthesize a modification packet that
  starts at the earliest unresolved commitment rather than the last action verb.
  When upstream reality and product commitment are accepted, select the smallest
  sufficient implementation chain: `project-analysis`, then `project-iteration`, plus
  `project-frontend`, `project-docs`, `project-commit`, or `review` only when the
  target and evidence require them as separate skills. Even without separate
  docs/review/commit skills, `project-iteration` still owns directly affected
  docs/tests, focused closeout review, verification, and version management.
  The packet must define implementation boundary, directly affected docs/tests,
  coding-quality contract applicability, verification scope, and focused vs deep
  review semantics.
- "审查一下 / 深度审查 / 全面 review": synthesize a review packet that selects the
  `review` skill. An unqualified software-project, repository, or product review
  defaults to project-global `deep` scope and every reality domain in the Project
  Optimality And Quality Contract. Explicit "全面", "完全", "穷尽",
  "逐词逐句", or `exhaustive` wording selects `exhaustive` depth. An explicitly
  bounded diff, file, issue, or workflow uses a focused completion-claim scope,
  while depth remains governed by wording and risk. Carry the single
  project-improvement `optimality_law`. For project-global, already
  packet-backed, cross-phase, resumable, multi-agent, or concurrently mutating
  review, carry the authoritative project-quality evidence
  `project_optimality_packet` and its compact `perspective_model`; for a focused
  single-owner review without a packet, carry only ephemeral scoped probes.
  Always carry the applicable clean-pass requirements, inspected surfaces, and
  not-inspected boundaries.
  Do not ask the user to name the review surfaces when the project evidence can
  derive them.
- "优化一下 / 深度优化 / 深度审查优化": synthesize an optimization packet that selects
  `optimize` or the project adapter owner, preserves the review-optimize loop when
  requested, carries the authoritative project-quality evidence
  `project_optimality_packet` for broad
  software-project optimization, carries framework-exhaustion requirements, and
  prevents novelty or bloat from replacing the user's target.
- "`目标! <large audit/migration/version closeout>`": build a task graph before
  implementation and load `references/subagent-execution.md`. Use
  `subagent_wave` for one independent antichain,
  `controller_team` for multi-wave project work with evolving agenda, and
  `workflow_batch` for many similar items or cross-checked research/review.
  Use `sequential` when conflict edges, dependencies, weak ROI, or merge risk
  dominate, but record the exact `parallel_blocker`. Missing V2 runtime
  capability blocks delegated nodes; it does not authorize sequential
  substitution.
  Do not imply peer-to-peer agent coordination,
  nested agents, background sessions, or isolated worktrees unless current
  runtime evidence proves those capabilities. For every delegated node, derive
  its assignment-specific `role_and_lens`; do not assume the task graph alone
  tells the agent how to execute the node. Consume every receipt and satisfy the
  V2 thread-accounting gate before the next wave or completion claim.
- "`目标! 推进小版本，把优化点落到项目计划文件`": use `plan_state_sink:
  trace_and_formal_plan`, create or update the smallest authoritative project
  plan file through `project-docs` if none exists, mark items active before
  execution, write result/verification after each item, and record
  `change_request` for every mid-run user addition.
- "`目标! 审查/优化/深度审查优化 <target>`": synthesize a
  `goal_preflight`, task-specific `optimality_law`, and compact
  `perspective_model` before the agenda. A broad or otherwise unqualified
  objective builds the authoritative project-quality evidence
  `project_optimality_packet` from the complete open discovery model in
  `goal-orchestration.md`. An explicitly bounded objective uses only material
  scoped probes and creates persistent packet state only when cross-phase,
  resumable, multi-agent, or concurrent mutation control requires it. Carry the
  active packet, typed projection, or ephemeral probes into review, optimize,
  and subagent prompts. Preserve breadth in discovery while allowing only
  evidence-backed findings and value-justified changes.
- "只改这个 diff / 单点改动 / 不做整体推进": keep scope focused. Without an
  explicit `目标!` / `目标！`, do not create a goal. With the explicit marker,
  create a lightweight goal without broadening the scope. Record
  `analysis_gate: explicitly_skipped_by_user` only when the user explicitly
  skipped broader analysis, and keep final review labeled focused.
  `protocol_evidence` must show the focused boundary and stop condition.
- "改一个错字 / 单一局部 token": use `not_required_very_small` only after all
  Entry Policy conditions are proved. Bounded uncertainty may remain light only
  when one targeted check conclusively resolves it without broader mutation;
  unresolved semantic/user-visible risk or broader mutation restores
  `project-analysis` before further editing.
- "不要并行 / 不用子 agent / 串行执行": preserve any useful task graph for
  planning, but set `parallel_blocker: user_explicit_no_parallel` and do not
  spawn subagents.
- "做一个版本 / MVP / v0.x": treat as version-state work, create or consume a
  frozen charter, build an agenda with source/result/verification evidence, and
  do not downgrade to one local iteration. If the user asks to finish or close
  out the version, also load `references/goal-orchestration.md`.
- "继续推进直到完成 / 两轮全局审查无新增问题 / 没有遗留问题": load both this
  reference and `references/goal-orchestration.md`, maintain
  `cyclic_goal_loop` and `loop_control_matrix`, reset clean passes on material
  in-scope issues, and stop only at the combined
  agenda/verification/review/optimization/known-issue/runtime-resource boundary.
- "改完再深度 review": when an edit target exists, implement through the
  selected executor, then use `review` at deep depth. A focused closeout gate
  cannot be reported as deep review. If no edit target exists in the request or
  active context, ask what to change before any mutation.
- "全面审查不要只看改动": route directly to review-only exhaustive inspection
  unless the user also requested edits or this phrase follows an active edit
  target; only then finish the authorized edits before review.
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
- project goal runtime/status, when concierge mode was used,
- runtime resource ledger summary, including any handles intentionally kept open
  or close failures,
- subagent execution summary when evaluated: chosen mode/model and reason,
  blocker if sequential or unavailable, inspected task surfaces, receipt/join
  result, remaining running V2 child count, and CAO evidence only when hard state was active,
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
