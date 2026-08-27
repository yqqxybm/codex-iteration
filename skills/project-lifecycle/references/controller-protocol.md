# Controller Protocol

Use this reference when `project-lifecycle` builds a multi-skill chain, advances
a plan or version, prepares Context Packets, consumes Handoff Records, writes a
trace, or finalizes a lifecycle task.

## Table Of Contents

- Call Chain Plan
- Continuity Principle
- Executable Plan Quality
- Plan Advancement Loop
- Runtime Resource Ledger
- Context Packet
- Handoff Record
- Trace Placement
- Pressure Scenarios
- Final Response

## Continuity Principle

Read the protocol that governs an actual transition and let it change the
decision, boundary, action, or stop condition. Preserve state only when another
stage, agent, or later session needs it to continue correctly. Completion rests
on the resulting project state and the verification appropriate to its claims,
not on a separate record proving that a protocol was read.

## Call Chain Plan

Before downstream work starts, produce a compact plan:

```yaml
phase: <earliest unresolved lifecycle phase and accepted upstream commitments>
goal: <user-visible objective>
selected_chain:
  - skill: <skill-name>
    purpose: <which unresolved commitment or requested outcome this skill owns>
success_criterion: <observable finish condition for the whole request>
active_control_state: <only the analysis/discovery disposition or goal, agenda,
  subagent, runtime, release, sync, or standard state that this chain activates>
stop_condition: <when not to continue the chain>
```

Load and attach a specialized control structure only when its owner is active.
Its authoritative reference defines the detail; the call-chain plan records the
state that can change this chain, not a union of every possible controller field.

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
in-scope issues, unmet commit/push/deploy/health requirements, or unfinished
user-explicit review rounds, while non-subagent runtime resources remain open
without a visible keep-open policy, or while the subagent
receipt-join/thread-accounting gate is unsatisfied.

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
use the goal, agenda, trace, and accepted Handoffs for continuity. Review and
optimization judgments travel as compact context only while they can affect the
next decision or action.

A Context Packet is a bounded projection, not a form to fill. Include only what
the recipient can use or invalidate. Downstream skills preserve the supplied
authority and return only a result or state change that matters to the caller.

An upstream report, analysis, audit, proposal, or retrospective defaults to
`evidence_only`. Its observations, hypotheses, and recommendations may inform
judgment, but they do not become accepted decisions, requirements, agenda items,
acceptance criteria, review coverage, or scope changes until the controller
records an explicit in-scope decision through the applicable existing
transition: adoption, `change_request`, or `model_reset`. This is a semantic
boundary, not a new packet or ledger.

```yaml
intent: <user goal and accepted purpose>
constraints: <hard limits, explicit exclusions, and preserved commitments>
accepted_state: <only decisions the recipient may rely on>
owned_scope: <the decision or action this recipient owns>
current_judgment: <only when it changes this recipient's work>
active_control_state: <only the relevant discovery, analysis, goal, agenda,
  subagent, runtime, release, or sync state; otherwise omit>
verification_boundary: <the claim or consequence this recipient must test>
```

Attach owner-specific detail by reference only when that owner needs it. For
example, a UI owner may need its visual target, a release owner its environment
and rollback path, and a delegated worker its exact assignment. Do not copy the
vocabulary or state of unrelated owners into the packet.

## Handoff Record

After each downstream skill finishes, record a short handoff:

```yaml
skill: <skill-name>
status: <done | blocked | skipped>
judgment_or_result: <what the caller may now conclude or act on>
changed_artifacts: <only actual mutations, or none>
state_delta: <only an adoption, model reset, change request, goal/agenda,
  subagent, runtime, release, or sync change that the controller must apply>
verification: <the decisive check and result, when one was needed>
open_limit: <only a blocker, uncertainty, or risk that changes the next step>
next_recommended_skill: <next owner, when action remains>
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

Carry only judgments that can change the plan, action, or completion boundary.
An unresolved human decision remains in `open_risks` or blocking state for
every affected claim; it cannot disappear through summarization or handoff.

## Trace Placement

Use the lightest trace that preserves recoverability:

1. **Short chain**: keep the trace in the conversation and final response only.
2. **Long, cross-phase, or resumable chain**: create a project-local trace at
   `.codex/traces/<YYYY-MM-DD>-<task-slug>.md`.
3. **Durable project knowledge**: promote only long-lived facts into
   `README.md`, project `AGENTS.md`, or `docs/` through `project-docs`.

Trace files are operational working records, not backups and not formal docs.
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
- A review request selects `review` only when the user's actual intent is an
  independent judgment of an existing object. Resolve scope from the object and
  completion claim; depth follows the requested or risk-appropriate intensity.
  Deep or exhaustive review follows more material relations; a named number of
  passes applies only when the user explicitly makes it part of the result.
- A request for something to become better selects `optimize` only after the
  lifecycle has established that there is a formed object whose better and worse
  realization can be judged. If the request instead challenges what the object
  is or how it should embody the user's purpose, return to discovery or brief
  formation. When the user explicitly requests both review and optimization,
  preserve both responsibilities: let independent review establish the
  diagnosis, let the authorized owner implement the optimization judgment, and
  renew review when the change affects the initiating judgment as defined by
  `optimize/references/deep-optimization.md`. Ordinary modification requests do
  not acquire this compound chain by implication.
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
- A goal-backed review or optimization first synthesizes `goal_preflight` and
  the task-specific `optimality_law`. Carry the formed object, governing
  tension, accepted agenda, and only observations capable of changing the next
  action. Broad work uses the coding-quality contract as directions for inquiry,
  not as a lens matrix or a second state store.
- "只改这个 diff / 单点改动 / 不做整体推进": keep scope focused. Without an
  explicit `目标!` / `目标！`, do not create a goal. With the explicit marker,
  create a lightweight goal without broadening the scope. Record
  `analysis_gate: explicitly_skipped_by_user` only when the user explicitly
  skipped broader analysis, and keep final review labeled focused.
  Preserve that focused boundary in the plan and stop condition.
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
- A request to continue until completion loads
  `references/goal-orchestration.md` and maintains the goal, agenda, delivery,
  and runtime boundaries. A named review-round count becomes an explicit stop
  condition and restarts after material in-scope change; no review or
  optimization cycle is inferred from ordinary completion language.
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

Lead with the concrete result and the judgment that matters to the user's next
decision. Name what changed and the verification that supports the material
claim. When a goal or agenda is active, state its completion and remaining work;
when a resource, subagent, release, sync, or change request remains consequential,
state only the condition the user or next session needs. Internal call chains,
packets, ledgers, matrices, and protocol use remain internal unless the user asks
for them or a failure in them limits the result.
