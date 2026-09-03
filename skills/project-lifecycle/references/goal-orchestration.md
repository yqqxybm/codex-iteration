# Goal Orchestration

Use this reference when `project-lifecycle` enters goal-backed project concierge
mode, synthesizes a tool goal, or controls a cyclic project objective.

## Table Of Contents

- Goal Contract
- Goal Synthesis After Judgment
- Goal State Machine
- Cyclic Project Goal Loop
- Loop Control Matrix
- Incomplete Closeout Targets
- Subagent Execution Contract

## Goal Contract

Turn a user target such as "完成 v0.1" into a goal for the next accepted
commitment. When the product boundary is unresolved, that commitment may be a
bounded inquiry: the goal controls the inquiry work and adoption gate, never its
conclusion. Do not make an inquiry commitment look like an already accepted
product boundary:

```yaml
project_goal:
  objective: <single project outcome>
  product_boundary: <accepted boundary, or the concrete question preventing one>
  non_goals: <explicit exclusions and phase limits known so far>
  required_surfaces: <only surfaces made necessary by the current commitment>
  success_criterion: <observable finish condition appropriate to that commitment>
  evidence_boundary: <what reality can and cannot establish before the next commitment>
```

When the Codex goal tool is available and the request is goal-backed, create or
maintain a goal from this structure. If the environment cannot activate a goal,
keep the same structure in the active agenda and trace; do not downgrade to a
one-turn checklist.

The text passed to `create_goal.objective` or used to maintain an existing tool
goal is not a short title. It is a compact control prompt. If
`control_system_goal.loop_policy.mode` is `bounded_goal_loop` or
`explicit_repeated_review`, the tool goal prompt must explicitly include the loop
contract:

```yaml
tool_goal_prompt:
  outcome: <single observable target>
  loop_mode: <bounded_goal_loop | explicit_repeated_review>
  continue_while:
    - <pending agenda item, failed verification, material in-scope work,
      missing commit/push/deploy/sync evidence, incomplete explicitly requested
      review rounds, or unresolved material-work source>
  revisit_on:
    - <material in-scope work>
    - <verification failure>
    - <material state change during explicitly requested review rounds>
  stop_only_when:
    - <all agenda items done or user-approved skipped>
    - <required verification evidence exists>
    - <delivery states such as commit/push/deploy/sync are satisfied or
      explicitly not_applicable with evidence>
    - <explicitly requested review rounds, if any, are satisfied after the last
      material change>
    - <material-work source has no unresolved accepted work>
  never_complete_from:
    - <single downstream handoff, commit, push, deploy, verification command,
      or review statement alone>
```

For looped goals, do not call `create_goal` with only the user's outcome or a
one-sentence summary. If the goal prompt lacks `continue_while`, `revisit_on`, and
`stop_only_when`, the prompt has failed the elegance gate even if the sidecar
`cyclic_goal_loop` field is correct.

Do not create a goal for an explicitly single-point, local, or diff-only
request unless the user used `目标!` / `目标！`. If a request asks to finish a version,
close out a phase, run until no known residual issue remains, or pass repeated
whole-project review gates, treat that language as goal-backed even when the
user gives only a rough target. The recommended explicit trigger is `目标!` or
`目标！` at the start of a project request; when present, always synthesize a
goal from the rest of the message. A local explicit trigger may produce a
lightweight single-pass goal, but it is still controlled by this reference.

## Goal Synthesis After Judgment

For `目标!` / `目标！`, the user should not have to write the loop, hardness,
or stop condition. Lifecycle first obtains the judgment needed for the next
commitment from the appropriate inquiry owner and resolves any necessary
dialogue. Goal orchestration begins only after that commitment is accepted. The
goal preserves the accepted purpose and completion boundary; the agenda is its
mutable execution state.

Before writing `goal_synthesis` or the final `tool_goal_prompt`, consume an
`accepted_project_judgment`. Select skills, contracts, verification, delivery,
and execution structure only where that judgment establishes their necessity.
An unresolved premise may justify a bounded inquiry commitment, but must not be
silently filled with downstream requirements, task nodes, quality defaults, or
delivery obligations.

```yaml
goal_synthesis:
  user_objective: <text after 目标! or 目标！>
  accepted_project_judgment:
    object_and_purpose: <what is being understood or changed and why it matters>
    concrete_relations: <reality, history, actors, constraints, and consequences that govern it>
    governing_tension: <relation that most affects the commitment>
    practical_commitment: <accepted action or bounded inquiry>
    preservation_boundary: <what remains valid and must not be lost>
    material_uncertainty: <what could alter the commitment or action>
    reversal_conditions: <what would reopen inquiry>
    dialogue_state: <resolved user contribution, or why none was needed>
    optimality_law:
      what_best_means: <how this commitment makes the software project better>
      value_relation: <how material values jointly serve the purpose; when a
        real conflict occurs, the conditional priority and reason>
      elegance_constraint: <smallest execution structure that preserves behavior>
      non_goal_boundary: <what must not be pulled into this goal>
      falsification_test: <evidence that would prove the commitment wrong>
  project_goal: <normalized Goal Contract above; the single semantic target>
  skill_system_best_practice_packet: <judgment-led selected/deferred capabilities; not a prefilled execution recipe>
  target_layer: <local_change | feature_workflow | version_phase | release_operation |
    whole_project | project_system | codex_self_iteration>
  control_system_goal: # Include only controls made meaningful by the next commitment.
    state_model:
      current_state_sources: <repo, docs, tests, deploy, trace, backlog, conversation>
      desired_state: <observable finished state>
      unknown_state: <facts to inspect, assume with risk, or ask about>
      reversal_conditions: <conditions that would change target_layer, scope, or stop condition>
    sensors: # Select only feedback that can correct the next action.
      repo_evidence: <git status, diff, tests, lint, typecheck, build, codegraph>
      product_evidence: <browser, API, workflow, UI, data, artifact output>
      operation_evidence: <deploy health, logs, remote sync, rollback path>
      review_judgment: <core judgment and material limits when review is required>
      knowledge_evidence: <docs, handoff, standard ledger, trace, agenda>
    actuators: # Include only when a mutation boundary is accepted.
      primary_skill_chain: <owner skills -> review/release/sync as needed;
        include inquiry only for a bounded inquiry commitment or reopened judgment>
      allowed_mutations: <code, docs, tests, config, deploy, sync, commits>
      forbidden_mutations: <explicit exclusions, unsafe/destructive areas, out-of-scope layers>
    loop_policy: # Include only when execution or an explicit review sequence exists.
      mode: <single_pass | bounded_goal_loop | explicit_repeated_review>
      revisit_on: <material_in_scope_work | verification_failure | material state change>
      explicit_review_rounds: <user-requested count | not_applicable>
    hardness_policy: # Include only when verification or review is in scope.
      verification: <targeted | full_project | release_health>
      review_depth: <focused | deep | exhaustive>
      review_scope: <diff | affected_workflow | project_global | release_readiness>
    delivery_policy: # Include only when delivery is in scope.
      commit: <required | not_applicable>
      push: <required | not_applicable | blocked>
      deploy_health: <required | not_applicable | blocked>
      sync: <required | not_applicable | blocked>
    escalation_policy:
      ask_user_when: <non-substitutable user perspective with material effect on
        understanding or commitment, missing controlling plan, or unsafe/destructive boundary>
      block_when: <missing secret, inaccessible deploy/remote, conflicting
        active goal, unsafe operation>
    stop_condition: <controller-written completion boundary>
  subagent_execution: # Include only when accepted work has independent executable surfaces.
    protocol: references/subagent-execution.md
    applicability: <required when the goal has independent work surfaces or delegates work>
    state: <task graph, parallel mode, model route, receipt/join state, hard-state status, or not_applicable>
  loop_control_matrix: # Include only when more than one active execution loop exists.
    active_loops: <tool_goal | agenda | subagent_wave | release_or_sync |
      user_explicit_review_rounds>
    reset_edges: <which event resets which counters or states>
    stop_precedence: <which stop condition must be satisfied before completion>
    non_equivalence: <loops/counters that must not be counted as each other>
```

`accepted_project_judgment` is the inquiry handoff that makes goal synthesis
possible, not a field for goal machinery to invent or revise. `project_goal`
preserves its accepted purpose and value relation; the agenda and trace preserve
execution and continuity. If reality challenges that judgment, suspend the
affected control state and return to its inquiry owner before rebuilding the
goal or applying `model_reset`.

Default synthesis rules:

- Before `accepted_project_judgment` exists, lifecycle invokes the earliest
  unresolved inquiry owner and resolves its dialogue before writing the final
  `control_system_goal`, creating a tool goal, or building the execution agenda.
  Inquiry inherits the three-step cognitive core:
  concrete inquiry and provisional synthesis -> dialogue -> plan. Ordinarily
  this work is expressed only as far as goal formation needs. When the user
  explicitly requested three-step analysis, enact the complete visible core
  under its exact original headings. `阶段 2：反向询问` asks and stops before
  goal activation; `阶段 3：计划制定` exists only after the user's answer. The
  goal must grow from the understanding, not from a preselected control structure.
- The judgment is incomplete until it expands the material relations,
  feedback, and time that can change the goal, identifies the governing standard,
  and tests the leading model against the strongest opposing view,
  counterexample, boundary, or failure mode. Revise the model before calibration;
  compactness may compress this dialectical test, not omit it.
- When an unresolved product object, user need, or product commitment would
  decide what the project should be or offer, select `project-discovery`. Make
  this judgment from the concrete situation and accepted state, not from content
  keywords or the current feature surface. Technical uncertainty within an
  accepted product boundary remains with `project-analysis`. The initial agenda must
  contain exactly the discovery work and its lifecycle-owned adoption gate; do
  not pre-create downstream nodes even as pending placeholders. Materialize brief,
  requirements, implementation, and their task graph only after the relevant
  judgment and adoption make them meaningful.
  Parallelize independent research surfaces when useful, but do not run
  implementation concurrently with an unresolved discovery gate.
- `accepted_project_judgment` must resolve dialogue before the goal is
  activated: the current interpretation, target layer, mutation boundary,
  strongest candidate question, and either the question or one concrete reason
  an internal invocation can continue. When the user explicitly requested
  three-step analysis, the core owns Stage 2 and defaults to dialogue; an
  internal synthesis cannot replace the user's participation.
- Strong calibration is mandatory for `目标!` / `目标！`: generate at least one
  candidate calibration question before activating the goal. For root direction,
  new project, PRD, architecture, MVP/version, release, product positioning,
  project-system, goal-system, subagent-orchestration, Codex skill/config, or
  Codex self-iteration goals, default missing target boundary, success
  criterion, non-goal, risk acceptance, delivery expectation, or external-state
  dependency to `ask_user` when the user's perspective is non-substitutable and
  materially affects the goal understanding or commitment. Materiality includes
  correction, deepening, reframing, or co-determination, not only reversal. If no
  question is asked, show the current judgment and one natural, specific reason
  dialogue is not needed; do not use a ledger or classification table as proof.
- `optimality_law` is mandatory for review, optimization, project-system,
  Codex self-iteration, product readiness, version closeout, or any goal where
  "best", "done", or "no known issue" could otherwise expand without limit.
  It must relate the user purpose, material qualities, binding constraints, and
  preservation commitments. It names a conditional priority only where a real
  conflict requires one; it does not force every value into a fixed score or
  total ranking.
- If inquiry finds that necessary user input would materially change
  the project understanding or commitment, ask before creating or maintaining
  the tool goal. Otherwise proceed only after exposing the current judgment and
  the concise reason dialogue is not needed; carry unresolved factual work as
  risk or evidence work.
- For Codex skills, AGENTS/global instructions, lifecycle rules, goal prompts,
  subagent orchestration, custom agents, sync rules, or any future-behavior
  object, treat competing interpretations of the edit boundary as blocking
  when they would lead to different mutations. Do not silently choose between
  behavior-only, light-rule, and full-protocol/schema changes.
- Infer the target layer from the user's explicit outcome and accepted boundary.
  Choose the smallest layer that fully satisfies that outcome. If an adjacent
  layer would materially change mutation, review, acceptance, or completion
  boundaries, ask instead of silently promoting the goal. Apparent completeness
  alone is not evidence that the higher layer is intended.
- `local_change`: use `single_pass` and targeted verification. Add an
  independent review only when the risk or requested claim needs it. Do not add
  deploy/push unless the user or accepted delivery boundary requires them.
- `feature_workflow`: use `bounded_goal_loop` and affected-workflow or
  full-project verification according to shared consequences. Review the changed
  whole when implementation can alter a governing product or technical judgment.
- `version_phase`, `whole_project`, or closeout work uses
  `bounded_goal_loop`, full-project verification, and review scope/depth
  proportionate to the completion claim; repeated rounds are not automatic.
- `release_operation`: use `bounded_goal_loop`, release-readiness judgment,
  release-health verification, and rollback/deploy evidence. Use exhaustive
  review only when explicitly requested or when the accepted high-risk claim
  genuinely requires traversing every material direction.
- `project_system` or `codex_self_iteration`: use `bounded_goal_loop`,
  realistic behavior checks, and remote sync verification when cross-machine
  behavior is intended. Review only where independent judgment can change the
  result.
- Use `hardness_policy.review_depth: exhaustive` when the objective explicitly
  asks for exhaustive/全面/穷尽/逐词逐句 review, or when production release,
  security, data integrity, migration, payment, credential, or destructive
  operations are materially in scope.
- Use `hardness_policy.review_scope: affected_workflow` for an explicitly
  bounded feature or fix that does not claim version, release, closeout,
  whole-project, or no-residual completeness.
- `commit: required` whenever the project is Git-managed and the goal produces
  deliverable source/docs/config changes.
- `push: required` only when the user explicitly asks for remote delivery or an
  authoritative release/deployment/shared-workspace contract makes a remote
  update part of the approved target. A remote existing, version closeout, or
  handoff wording alone does not authorize mutation; otherwise mark
  `not_applicable` with evidence.
- `deploy_health: required` when the objective is a website/app/service,
  release/readiness/上线/部署 target, or project evidence exposes a deploy/run
  health path. If no deploy target exists, mark `not_applicable` with evidence
  instead of weakening the stop condition silently.
- `sync: required` when the target changes Codex skills/config/agents intended
  to govern another Mac or remote environment; otherwise mark `not_applicable`
  with evidence.
- Verification defaults to the strongest relevant evidence for the target layer:
  targeted for local changes, full project for version/global goals, and release
  health for deploy/release goals.
- If later evidence proves the target layer or stop condition was wrong, suspend
  the affected execution state and return to inquiry. After a renewed judgment,
  record `control_reclassification`, regenerate the affected agenda, and revisit
  dependent verification or explicit review rounds instead of patching the old
  loop silently.
- Build a `loop_control_matrix` whenever more than one execution loop is active:
  tool goal, agenda advancement, subagent waves, release/deploy health, sync
  verification, or user-explicit repeated review. Do not let one loop's result
  stand in for another loop's stop condition.
- When the goal has independent work surfaces, delegated work, or durable
  execution state, load `references/subagent-execution.md`. That reference alone
  owns task-graph scheduling, model routing, V2 dispatch policy, CAO escalation,
  assignment, receipt acceptance, join judgment, and thread accounting.
  Native Codex V2 alone performs agent and thread mechanics.
  Carry only the accepted state summary in the goal contract; do not restate its
  schemas here.

### Accepted Project Judgment

Before goal orchestration writes an agenda, the applicable inquiry owner must
return a compact `accepted_project_judgment`. For broad review, optimization,
product readiness, project-system, or Codex self-iteration work, begin with the
object, user purpose, concrete relationships, history, constraints, and
governing tension. Use
`~/.agents/skills/software-contract/references/coding-quality-contract.md` when
software quality is material.

Follow every project relation that could overturn the whole judgment, including
project-specific relations not named by a generic contract. This is not a
perspective matrix: do not create one item per role, dimension, or evidence
surface, and do not require explicit dismissal of everything else. Evidence is
selected where it can correct the object model, practical judgment, action, or
claim strength.

Carry the judgment in the Context Packet and ordinary Handoff only while another
owner needs it. The goal carries only the accepted purpose, value relation, and
reversal conditions needed to direct execution; the agenda and trace preserve
continuity, not a second source of judgment.

### Goal Prompt Elegance Gate

Before activating the tool goal or handing work downstream, audit the generated
goal prompt. A goal prompt is elegant only when it is the smallest
self-contained execution contract that still preserves correct behavior:

- each field changes action, evidence, boundary, handoff, or stop condition,
- the `optimality_law` keeps jointly served values visible and resolves only
  genuine conflicts instead of forcing every lens into equal weight or a total
  ranking,
- the goal, agenda, and trace preserve only accepted direction, work, and
  continuity; review or optimization records do not become a second truth source,
- the agenda items are executable and do not repeat the same control rule,
- the stop condition is falsifiable from named evidence,
- the prompt states non-goals and forbidden mutations clearly enough to prevent
  silent expansion,
- the user is not asked to provide loop mechanics, review depth, role list, stop
  condition, or prompt wording that Codex can infer.

If the gate fails, simplify or rebuild the goal prompt before creating the tool
goal. Do not treat a longer, more philosophical, or more comprehensive prompt as
better unless it changes one of the control functions above.

Also treat these future-behavior changes as goal-backed by default: optimizing
`project-lifecycle`, the project skill stack, Codex goal rules, subagent
orchestration, custom agents, Codex skills, global instructions, config,
cross-skill call chains, or the user's Codex self-iteration system. These
changes govern future behavior, so they need a real goal, explicit evidence,
sync verification, and a strict completion boundary. Only skip the tool goal
when the user explicitly limits the request to wording, one local line, or
no-goal/no-concierge work.

Goal ownership is exclusive:

- Only the main lifecycle thread owns, creates, updates, completes, or clears
  the project goal.
- The main thread is the only merge owner and the only actor allowed to mark the
  agenda or goal complete.

## Goal State Machine

Treat the goal as the invariant contract, the agenda as the mutable execution
state, the trace as recoverable memory, and receipts/handoffs as evidence. Do
not use these layers interchangeably.

Before activating or maintaining a goal:

1. Use `get_goal` to inspect the current goal state when the tool is available.
2. If no active goal exists and the request is goal-backed, create one from the
  `tool_goal_prompt`: `project_goal`, the minimum accepted purpose/value/reversal
  context needed to guide action, plus the selected `control_system_goal` loop,
  delivery, review, verification, and stop policies. For looped goals, the
  objective text itself must contain the loop contract; do not put the loop only
  in the agenda or trace.
3. If an active goal is the same objective, maintain it and reconcile the agenda
   against current project evidence.
4. If an active goal conflicts with the new request, do not overwrite it. Ask for
   a decision or finish/block the current goal only when the tool's own rules
   allow that state change.
5. If the goal tool is unavailable, set `activation_state: agenda_only` in the
   trace and final response; never claim an active Codex goal exists.

Maintain this runtime record in the trace or handoff whenever concierge mode is
active:

```yaml
goal_runtime:
  activation_state: <active_tool_goal | agenda_only | blocked_by_existing_goal>
  tool_goal_status: <active | complete | blocked | unavailable | none>
  agenda_link: <trace path or in-conversation agenda>
  last_state_change: <created | reconciled | progressed | replanned | blocked | completed>
  next_goal_action: <continue_agenda | ask_user | update_complete | update_blocked | none>
```

Completion and blockage are strict:

- Mark a goal complete only after all required agenda items are done or
  user-approved skipped, required verification supports the completion claim,
  user-explicit review rounds are satisfied when any, and no material in-scope
  `new_work` remains.
- Do not mark a goal complete from a commit, deploy, receipt, or single
  verification command alone.
- Use `update_goal(status="complete")` only at the strict completion boundary.
- Mark a Codex tool goal blocked only when the same blocking condition has
  repeated for at least three consecutive goal turns and no meaningful progress
  is possible without user input or external state change. Otherwise keep the
  agenda active with a visible blocked item or ask for the missing decision.
- Use `update_goal(status="blocked")` only at that strict blocked boundary.
- If material in-scope work appears, reopen or add agenda work, revisit affected
  verification and any explicit review sequence, and keep the goal active.
- When the user deliberately changes an accepted goal, scope, priority, product
  boundary, or success criterion, create a visible `change_request` and
  reconcile the goal contract. When feedback instead reveals that Codex's
  accepted object, premise, actor/task account, judgment standard, explanatory
  relation, or method was wrong, apply `model_reset` first and invalidate its
  causal descendants as defined by `state-transitions.md`; do not preserve that
  state by relabeling the correction as a change request.

Pressure scenarios:

- "`目标! <project objective>` or `目标！ <project objective>`": create or
  maintain a tool goal when available after obtaining
  `accepted_project_judgment` and exposing the next commitment. Show only the
  `control_system_goal`, agenda,
  loop, review, delivery, and verification state that this commitment makes
  meaningful; an inquiry goal may initially contain only discovery and adoption.
  Do not ask the user to provide loop wording, stop
  conditions, review depth, review scope, commit/push/deploy
  requirements, verification hardness, state model, sensors, or actuator chain
  unless the user's perspective on the target boundary, success criterion,
  non-goal, risk acceptance, delivery expectation, or external state is both
  non-substitutable and material to the goal understanding or commitment. If no
  question is asked, show the current judgment and one concise reason dialogue
  is not needed.
  When the objective exposes independent work or needs delegation, load
  `references/subagent-execution.md` and carry only its accepted execution
  state into the goal. That reference owns authorization, graph, model route,
  dispatch failure handling and replanning, receipt acceptance, join judgment,
  and thread accounting; native Codex V2 performs spawn, follow-up, messaging,
  wait, interruption, status listing, and terminal-thread lifecycle.
- "`目标！先调研真实用户需要什么，再实现`": create an inquiry goal whose first
  agenda is `project-discovery -> lifecycle adoption`. Treat
  examples, current UI, available APIs, and existing fields as hypotheses. Add
  the downstream brief, plan, and executor graph only after the adoption gate.
- "完成 v0.1 收口 / 直到无遗留问题": create or maintain a tool goal when
  available, build a project-state-first agenda, create/update trace, and continue
  until the strict completion rule is met. Ask first when the phase boundary,
  deploy target, material-work source of truth, acceptance bar, or release/push
  expectation cannot be inferred from project evidence without changing the
  goal.
- "优化 project-lifecycle / goal 体系 / 项目 skill 体系 / 自我迭代规则":
  create or maintain a tool goal before editing unless the user explicitly says
  no goal or wording-only. First obtain `accepted_project_judgment` from the
  actual object, governing tension, realistic behavior, and the user's purpose.
  Ask first when the requested change could reasonably mean
  behavior-only, light-rule, or full-protocol/schema mutation.
- "优化 Codex 配置 / AGENTS / skills / custom agents": treat as the same
  future-behavior change; use a tool goal unless explicitly
  wording-only, no-goal, or one local line. Ask first when the edit boundary or
  persistence/sync target would change the resulting behavior.
- "只修这个 diff / 单点改动 / 不做整体推进": without an explicit
  `目标!` / `目标！`, do not create a goal; with the marker, use a lightweight
  goal. In both cases preserve the explicit narrow boundary.
- "继续推进到两轮全局审查无新增问题": keep the goal active until the agenda,
  verification, delivery obligations, and the two explicitly requested review
  rounds after the last material change are all satisfied.
- "已有不同 active goal": do not overwrite or silently switch; ask for the
  controlling goal or stop at the current goal boundary.
- "goal tool unavailable": use `activation_state: agenda_only`, preserve the
  same agenda/trace discipline, and disclose that no active Codex tool goal was
  created.

## Cyclic Project Goal Loop

Use a cyclic goal loop for project advancement, version closeout, release
readiness, or any goal whose correctness depends on finishing newly discovered
in-scope work before stopping. Repeated review belongs in this loop only when the
user explicitly requests a number of rounds or the goal names an equivalent
concrete condition.

Maintain this state in the trace or Handoff Record:

```yaml
cyclic_goal_loop:
  phase_boundary: <v0.1, v1.0, current milestone, release, or project objective>
  work_source: <agenda | trace | TODO/backlog | review result | release checks>
  explicit_review_rounds: <user-requested count | not_applicable>
  completed_review_rounds: <0..requested count | not_applicable>
  revisit_on: <material_in_scope_work | verification failure | material state change>
  latest_code_state: <uncommitted | committed | pushed | not_applicable | blocked>
  deploy_health: <pass | fail | not_applicable | blocked>
  open_material_work: <none | accepted agenda work, findings, failures, gaps, or unknown>
  stop_state: <continue | blocked | complete>
```

The loop order is:

1. Discover the controlling agenda and material-work source.
2. Implement or delegate the next material item.
3. Verify the changed surface.
4. Commit, push, release, or deploy only when they are part of the goal boundary.
5. Run review only when the goal or a material risk requires independent
   judgment; use the requested depth.
6. If material in-scope work appears, add or reopen agenda work and continue
   from step 2. Restart an explicit review-round sequence after the changed
   object is ready.
7. If no unresolved material work appears, satisfy any explicitly requested
   review rounds, then evaluate the whole stop condition.

Material in-scope work is an accepted finding, failed command, unresolved
requirement, missing evidence that limits a required claim, or handoff gap
that affects the declared phase boundary, required surface, acceptance
criterion, security/data boundary, deploy health, standard compliance, handoff
readiness, practical judgment, or stop claim.

Do not reopen work for explicitly out-of-scope ideas, unaccepted possibilities,
future-version improvements, optional polish, duplicate agenda items,
user-deferred items, or risks whose non-blocking status is already understood.

The goal may stop as complete only when all are true:

- all required agenda items are `done` or user-approved `skipped`,
- current code/docs/config state is verified,
- latest code is committed when the project uses Git and the goal includes a
  deliverable code state,
- latest code is pushed when the user goal, deploy target, or release boundary
  requires remote synchronization,
- deploy/health is `pass` when deployment is in scope, or `not_applicable` with
  evidence when no deploy target exists,
- explicitly requested review rounds, if any, are satisfied after the last
  material change,
- the selected work source contains no unresolved accepted work inside the phase
  boundary,
- the authoritative subagent receipt-join and thread-accounting gate in
  `references/subagent-execution.md` passes when delegation occurred.

If code, docs, config, or release state changes during an explicit review-round
sequence, restart that sequence after the changed object is ready. If remote
push or deploy evidence is unavailable, record the blocker and keep the goal
active unless the user changes the boundary.

## Loop Control Matrix

Use this matrix when goal-backed work combines agenda advancement, subagent
waves, release/deploy checks, sync verification, or user-explicit repeated
review. It coordinates real execution state; it does not define the quality of
review or optimization.

```yaml
loop_control_matrix:
  active_loops:
    tool_goal: <active | agenda_only | none>
    agenda_loop: <active | none>
    subagent_wave_loop: <active | none>
    explicit_review_rounds: <requested count and current count | none>
    release_or_sync_loop: <active | none>
  reset_edges:
    material_in_scope_work:
      revisits: <agenda item, affected verification, explicit review sequence, or release/sync state>
    verification_failure:
      revisits: <agenda item, affected verification, or release/sync state>
    material_change_during_explicit_review:
      revisits: <the requested review sequence after the object is ready>
    subagent_scope_or_merge_conflict:
      revisits: <wave join and affected agenda item>
    subagent_thread_failure:
      revisits: <wave join and affected agenda item>
  stop_precedence:
    - all required agenda items done or user-approved skipped
    - all subagent receipts joined, rejected, or converted into visible agenda state
    - authoritative subagent receipt-join and thread-accounting gate satisfied when delegation occurred
    - required verification/release/sync evidence satisfied or explicitly blocked/not_applicable
    - user-explicit review rounds satisfied after the last material change, when any
    - tool goal marked complete only after the above parent stop condition is true
  non_equivalence:
    - a subagent receipt is not agenda completion
    - a passing command is not an independent review judgment
    - a commit/push/deploy is not goal completion
    - a completed V2 thread is not an accepted receipt
    - a goal completion claim is invalid while unjoined receipts or pending agenda items remain
```

If one loop materially changes another loop's object, revisit only the affected
judgment, verification, or explicit round sequence. Do not restart unrelated
work for out-of-scope ideas, duplicate findings already represented in the
agenda, or rejected non-material drift.

The controller must record which material event caused replanning. Do not retain
process history that cannot change recovery, action, or completion.

## Incomplete Closeout Targets

When the user gives an incomplete long-horizon target such as "完成 v0.1",
"做完 1.0", or "收口", do not ask the user to draft a complete goal. Create a
project-state-first agenda and delegate bounded read-heavy inspection where useful
to resolve:

- project root and controlling repository,
- plan/backlog source of truth: trace, issues, roadmap, TODO, release checklist,
  handoff doc, or explicit user message,
- deploy target, run/deploy command, and health signal,
- review scope and any user-explicit round requirement,
- residual-issue source of truth.

Ask the user only when project evidence cannot resolve the uncertainty and the
user's perspective is non-substitutable and material to the goal understanding
or commitment. Multiple credible sources that would produce different goals are
a common case, not an automatic substitute for that judgment.

For "全局审查" without a narrower scope, default to repository-relevant product
readiness: user goal, root charter/version boundary, code/runtime, tests/build,
security boundary, docs/handoff, release/deploy health, standard ledger, and
known backlog/trace/TODO items. Record this inferred scope in the agenda.

"No known residual issue" requires evidence from the selected source of truth.
If no source exists, create one in the trace for this run and record that the
claim is limited to inspected evidence, not unknowable external backlog.

## Subagent Execution Contract

Load `references/subagent-execution.md` whenever a goal delegates work, has
parallel-safe nodes, or needs state to survive interruption. Preserve the goal's
  objective, boundary, value relation, and stop condition when constructing the
subagent parent target. Goal agenda items carry only the execution node id and
accepted status/result summary; do not copy model-route, assignment, V2 wave,
CAO, or receipt schemas back into this goal reference.
