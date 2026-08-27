# Goal Orchestration

Use this reference when `project-lifecycle` enters goal-backed project concierge
mode, synthesizes a tool goal, or controls a cyclic project objective.

## Table Of Contents

- Goal Contract
- Control-System Goal Synthesis
- Goal State Machine
- Cyclic Project Goal Loop
- Loop Control Matrix
- Incomplete Closeout Targets
- Subagent Execution Contract

## Goal Contract

Convert incomplete user targets such as "完成 v0.1" into a verifiable goal:

```yaml
project_goal:
  objective: <single project outcome>
  product_boundary: <what the project is and is not>
  non_goals: <explicit exclusions and phase limits>
  required_surfaces: <product, docs, code, security, tests, deploy, handoff, review>
  success_criterion: <observable finished state>
  evidence_boundary: <what evidence can and cannot prove>
```

When the Codex goal tool is available and the request is goal-backed, create or
maintain a goal from this structure. If the environment cannot activate a goal,
keep the same structure in the active agenda and trace; do not downgrade to a
one-turn checklist.

The text passed to `create_goal.objective` or used to maintain an existing tool
goal is not a short title. It is a compact control prompt. If
`control_system_goal.loop_policy.mode` is `bounded_goal_loop` or
`cyclic_until_clean`, the tool goal prompt must explicitly include the loop
contract:

```yaml
tool_goal_prompt:
  outcome: <single observable target>
  loop_mode: <bounded_goal_loop | cyclic_until_clean>
  continue_while:
    - <pending agenda item, failed verification, material in-scope issue,
      missing commit/push/deploy/sync evidence, insufficient clean passes,
      or unresolved residual issue source>
  reset_on:
    - <material in-scope issue>
    - <verification failure>
    - <code/docs/config/release/evidence change after a clean pass>
  stop_only_when:
    - <all agenda items done or user-approved skipped>
    - <required verification evidence exists>
    - <delivery states such as commit/push/deploy/sync are satisfied or
      explicitly not_applicable with evidence>
    - <required review depth and clean-pass count are satisfied after the last
      material change>
    - <known residual issue source has no unresolved material issue>
  never_complete_from:
    - <single downstream handoff, commit, push, deploy, verification command,
      or one clean review pass alone>
```

For looped goals, do not call `create_goal` with only the user's outcome or a
one-sentence summary. If the goal prompt lacks `continue_while`, `reset_on`, and
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

## Control-System Goal Synthesis

For `目标!` / `目标！`, the user should not have to write the loop, hardness,
or stop condition. The controller must synthesize a control-system goal before
asking, planning, or executing. The goal is the control law; the agenda is the
mutable execution state.

Before writing `goal_synthesis` or the final `tool_goal_prompt`, consume the
controller's `skill_system_best_practice_packet` when present, or synthesize it
from the current skill metadata and selected/ambiguous `SKILL.md` files. This
packet is not a replacement for `tool_goal_prompt`; it is the skill-system
practice layer that determines which existing skills, adapters, contracts,
framework loops, verification gates, delivery gates, and stop conditions should
shape the goal prompt.

```yaml
goal_synthesis:
  user_objective: <text after 目标! or 目标！>
  project_goal: <normalized Goal Contract above; the single semantic target>
  skill_system_best_practice_packet: <skill survey and selected practice layer used as input, or why not applicable>
  target_layer: <local_change | feature_workflow | version_phase | release_operation |
    whole_project | project_system | codex_self_iteration>
  goal_preflight:
    material_model:
      direct_intent: <what the user explicitly wants>
      underlying_concern: <tentative interpretation of what matters beneath the
        request; subordinate to direct_intent>
      target_world: <repo/product/skill/config/runtime system being changed>
      controlling_tension: <governing structure, value conflict, action tension, or tradeoff that governs success>
      candidate_paths: <genuine alternatives needed to test the objective; omit
        when the strongest counterview or failure mode is the better test>
    calibration:
      default_judgment: <best current interpretation before asking>
      key_assumptions: <facts or values the judgment depends on>
      reversal_conditions: <conditions that would change target layer, scope, or stop>
      dialogue_judgment: <strongest candidate question; whether the user's
        perspective is non-substitutable and material to understanding or
        commitment; ask_user or one concise no-dialogue reason>
    optimality_law:
      what_best_means: <how this goal makes the software project better>
      primary_ordering: <which value wins when lenses conflict>
      elegance_constraint: <smallest control structure that preserves behavior>
      non_goal_boundary: <what must not be pulled into this goal>
      falsification_test: <evidence that would prove this goal prompt wrong>
  perspective_model:
    artifact_type: <code | product | skill | config | docs | release | workflow | mixed>
    synthesized_lenses:
      - role: <material viewpoint generated from the objective and evidence>
        why_material: <why this role can change review, optimization, or stop condition>
        core_question: <what this role would ask to judge success>
        evidence_surface: <files, workflows, docs, commands, user behavior, or runtime proof>
        defect_or_opportunity_standard: <what counts as a material issue or improvement>
    excluded_lenses: <irrelevant lenses and why they were excluded>
  project_optimality_packet:
    <lifecycle-owned authoritative project-quality evidence packet or resolvable
    revision-pinned project_optimality_ref; required when project-quality
    evidence must survive broad/unqualified review or optimization, cross-phase
    or resumable work, multi-agent work, or concurrent mutation; bounded
    recipients receive project_optimality_projection>
  control_system_goal:
    state_model:
      current_state_sources: <repo, docs, tests, deploy, trace, backlog, conversation>
      desired_state: <observable finished state>
      unknown_state: <facts to inspect, assume with risk, or ask about>
      reversal_conditions: <conditions that would change target_layer, scope, or stop condition>
    sensors:
      repo_evidence: <git status, diff, tests, lint, typecheck, build, codegraph>
      product_evidence: <browser, API, workflow, UI, data, artifact output>
      operation_evidence: <deploy health, logs, remote sync, rollback path>
      review_evidence: <focused, deep, or exhaustive pass logs and clean-pass count>
      knowledge_evidence: <docs, handoff, standard ledger, trace, agenda>
    actuators:
      primary_skill_chain: <project-analysis -> owner skills -> review/release/sync as needed>
      allowed_mutations: <code, docs, tests, config, deploy, sync, commits>
      forbidden_mutations: <explicit exclusions, unsafe/destructive areas, out-of-scope layers>
    loop_policy:
      mode: <single_pass | bounded_goal_loop | cyclic_until_clean>
      reset_on: <material_in_scope_issue | verification_failure | state_change_after_clean_pass>
      clean_pass_target: <0 | 1 | 2>
    hardness_policy:
      verification: <targeted | full_project | release_health>
      review_depth: <focused | deep | exhaustive>
      review_scope: <diff | affected_workflow | project_global | release_readiness>
    delivery_policy:
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
  subagent_execution:
    protocol: references/subagent-execution.md
    applicability: <required when the goal has independent work surfaces or delegates work>
    state: <task graph, parallel mode, model route, receipt/join state, hard-state status, or not_applicable>
  loop_control_matrix:
    active_loops: <tool_goal | agenda | subagent_wave | review_clean_pass | optimize_framework_cycle>
    reset_edges: <which event resets which counters or states>
    stop_precedence: <which stop condition must be satisfied before completion>
    non_equivalence: <loops/counters that must not be counted as each other>
```

`project_goal`, `goal_preflight`, and `optimality_law` remain the authoritative
user/lifecycle objective and value ordering. When `project_optimality_packet` is
active, its `project_model`, `perspective_model`, and
`control_system_goal.state_model` are revision-pinned evidence projections, not
parallel goal authority. If evidence challenges the objective or value ordering,
the lifecycle reopens preflight and dialogue governance; review and optimize
return evidence/deltas and never silently mutate the goal.
The packet, ledger, and clean-pass count record the coverage and limits of a
judgment; they do not exhaust the subject or turn no observed finding into
quality.

Default synthesis rules:

- Run `goal_preflight` before writing the final `control_system_goal`, creating
  a tool goal, building the agenda, or asking the user. This is a compact
  three-step-analysis adapter: independent project understanding -> dialogue
  judgment -> practical commitment. Ordinarily it is not a visible essay. When
  the lifecycle carries `three_step_visibility: explicit`, it must instead
  expose compact, object-appropriate Stage 1, Stage 2, and Stage 3 before goal
  activation; if Stage 2 blocks, stop there and do not activate the goal or
  emit Stage 3. It exists so the goal prompt knows what problem-world it is
  controlling before it chooses fields, lenses, loops, or subagents.
- The `material_model` is incomplete until it expands the material relations,
  feedback, and time that can change the goal, identifies the governing standard,
  and tests the leading model against the strongest opposing view,
  counterexample, boundary, or failure mode. Revise the model before calibration;
  compactness may compress this dialectical test, not omit it.
- When research must decide users, product content, requirements, priorities,
  positioning, or scope, select `project-discovery`. The initial agenda must
  contain exactly the discovery work and its lifecycle-owned adoption gate; do
  not pre-create downstream nodes even as pending placeholders. Materialize brief,
  requirements, implementation, and their task graph only after adoption.
  Parallelize independent research surfaces when useful, but do not run
  implementation concurrently with an unresolved discovery gate.
- `goal_preflight` must still expose a visible dialogue judgment before the goal
  is activated: the current goal interpretation, target layer, mutation boundary,
  strongest candidate question, and either the blocking question or one concise
  reason the user's perspective is not needed before commitment. When
  `three_step_visibility: explicit` applies, this is the visible Stage 2 within
  the full compact Stage 1/2/3 gate. Do not treat an internal preflight as
  sufficient when the user needs a chance to correct or deepen the goal judgment.
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
  It must define the value ordering that resolves conflicts between user value,
  engineering quality, product maturity, architecture, delivery, elegance, and
  verification.
- If `goal_preflight` finds that the user's perspective meets both dialogue
  thresholds, ask before creating or maintaining the tool goal. Otherwise
  proceed only after exposing the current judgment and the concise reason
  dialogue is not needed; carry unresolved factual work as risk or evidence work.
- For Codex skills, AGENTS/global instructions, lifecycle rules, goal prompts,
  subagent orchestration, custom agents, sync rules, or any future-behavior
  control law, treat competing interpretations of the edit boundary as blocking
  when they would lead to different mutations. Do not silently choose between
  behavior-only, light-rule, and full-protocol/schema changes.
- Infer the target layer from the user's explicit outcome and accepted boundary.
  Choose the smallest layer that fully satisfies that outcome. If an adjacent
  layer would materially change mutation, review, acceptance, or completion
  boundaries, ask instead of silently promoting the goal. Apparent completeness
  alone is not evidence that the higher layer is intended.
- `local_change`: use `single_pass`, targeted verification, focused review, and
  `clean_pass_target: 0` or `1` depending on risk. Do not add deploy/push unless
  evidence or the user requires a delivered state.
- `feature_workflow`: use `bounded_goal_loop`, affected-workflow review, targeted
  or full-project verification based on shared surfaces, and `clean_pass_target:
  1`; use `2` when the workflow is cross-module, user-visible, or regression
  prone.
- `version_phase`, `whole_project`, or "finish/close out/no residual issues":
  use `cyclic_until_clean`, project-global deep review, full-project
  verification, and `clean_pass_target: 2`.
- `release_operation`: use `cyclic_until_clean`, release-readiness review,
  release-health verification, rollback/deploy evidence, and `clean_pass_target:
  2`; escalate review to exhaustive for production, data, security, payment,
  credential, migration, or destructive risk.
- `project_system` or `codex_self_iteration`: use `cyclic_until_clean`,
  protocol/skill/config evidence, remote sync verification when cross-machine
  behavior is intended, and `clean_pass_target: 2`.
- Use `hardness_policy.review_depth: exhaustive` when the objective explicitly
  asks for exhaustive/全面/穷尽/逐词逐句 review, or when production release,
  security, data integrity, migration, payment, credential, or destructive
  operations are materially in scope.
- Use `hardness_policy.review_scope: affected_workflow` and
  `clean_pass_target: 1` only when the objective is explicitly a single bounded
  feature/fix and does not claim version, release, closeout, whole-project, or
  no-residual completeness.
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
- If later evidence proves the target layer or stop condition was wrong, record
  `control_reclassification`, regenerate the agenda, reset affected clean-pass
  counters, and continue from the new control law instead of patching the old
  loop silently.
- Build a `loop_control_matrix` whenever more than one loop is active: tool goal,
  agenda advancement, subagent waves, review clean passes, optimize framework
  cycles, release/deploy health, or sync verification. Do not let one loop's
  clean result stand in for another loop's stop condition.
- When the goal has independent work surfaces, delegated work, or durable
  execution state, load `references/subagent-execution.md`. That reference alone
  owns task-graph scheduling, model routing, V2 dispatch policy, CAO escalation,
  assignment, receipt acceptance, join judgment, and thread accounting.
  Native Codex V2 alone performs agent and thread mechanics.
  Carry only the accepted state summary in the goal contract; do not restate its
  schemas here.

### Perspective Model Synthesis

For review, optimization, deep review-optimize, product readiness, project
system, or Codex self-iteration goals, synthesize `perspective_model` before
writing the final goal or agenda. The user's examples are seed patterns, not the
complete set.

When `目标!` / `目标！` asks for broad or otherwise unqualified review,
optimization, or review-optimization, load `software-contract` and read
`~/.agents/skills/software-contract/references/coding-quality-contract.md` and
`~/.agents/skills/software-contract/references/project-optimality-state-contract.md`.
Build the lifecycle-owned authoritative project-quality evidence
`project_optimality_packet` in this order:
`project_model` -> dynamic concerns -> atomic probes -> current evidence and
derived claim state.
Generate probes from the contract's open responsibility positions and add any
project-specific authority or affected party required by reality. The named
positions and concerns are discovery sources, not a gold-standard list or equal
weighting system.

Derive `perspective_model` only as a compact human-readable projection of the
packet. Each lens must retain its probe questions, evidence surfaces, and
decision impact; it cannot replace concerns, probes, or evidence.
Complete discovery coverage guarantees breadth, not artificial findings. Every
probe serves the single `optimality_law`. For review goals, evidence becomes a
finding when it changes completion, decision, risk acceptance, or the stop
condition. For optimization goals, select a change only when expected project
benefit exceeds added complexity, cost, scope, risk, and re-optimization drift.

When the user explicitly limits the target, perspective, or review boundary,
derive the material subset that can change that scoped result. Do not use an
explicitly narrow request as permission to omit a lens that remains material
inside the stated boundary.

The lifecycle controller owns the full `project_optimality_packet`. Carry it or
a resolvable, revision-pinned `project_optimality_ref` in `goal_synthesis` and
the agenda. Give review or broad
optimization the full packet; give bounded executors and subagents the complete
typed `project_optimality_projection` defined by the state contract. Declared
delta producers return `project_optimality_delta`; other owners return normal
Handoff evidence and subagents return receipts, which the controller normalizes
before merge, replanning, or counting a clean pass. Carry `perspective_model`
with the same actors only as the packet's compact readable projection.

### Goal Prompt Elegance Gate

Before activating the tool goal or handing work downstream, audit the generated
goal prompt. A goal prompt is elegant only when it is the smallest control law
that still preserves correct behavior:

- each field changes action, evidence, boundary, handoff, or stop condition,
- the `optimality_law` resolves conflicts between lenses instead of letting all
  lenses accumulate equal weight,
- `project_optimality_packet` is the single project-quality state source;
  `perspective_model` stays a compact projection rather than a parallel taxonomy,
- the agenda items are executable and do not repeat the same control rule,
- the stop condition is falsifiable from named evidence,
- the prompt states non-goals and forbidden mutations clearly enough to prevent
  silent expansion,
- the user is not asked to provide loop hardness, review depth, clean-pass
  count, role list, stop condition, or prompt wording that Codex can infer.

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
   `tool_goal_prompt`: `project_goal` plus the selected `control_system_goal`
   loop policy, delivery policy, review policy, verification policy, and stop
   condition. For looped goals, the objective text itself must contain the loop
   contract; do not put the loop only in the agenda or trace.
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
  last_state_change: <created | reconciled | progressed | reset_clean_pass | blocked | completed>
  next_goal_action: <continue_agenda | ask_user | update_complete | update_blocked | none>
```

Completion and blockage are strict:

- Mark a goal complete only after all required agenda items are done or
  user-approved skipped, required verification evidence exists, required review
  clean passes are satisfied, and no material in-scope `new_work` remains.
- Do not mark a goal complete from a commit, deploy, receipt, or single
  verification command alone.
- Use `update_goal(status="complete")` only at the strict completion boundary.
- Mark a Codex tool goal blocked only when the same blocking condition has
  repeated for at least three consecutive goal turns and no meaningful progress
  is possible without user input or external state change. Otherwise keep the
  agenda active with a visible blocked item or ask for the missing decision.
- Use `update_goal(status="blocked")` only at that strict blocked boundary.
- If a material in-scope issue appears after a clean pass, reset the relevant
  clean-pass counter, reopen or add agenda work, and keep the goal active.
- If the product boundary or success criterion changes, create a visible
  `change_request` and reconcile the goal contract before continuing.

Pressure scenarios:

- "`目标! <project objective>` or `目标！ <project objective>`": create or
  maintain a tool goal when available, infer the full control-system
  `goal_synthesis` from the objective, show `target_layer`,
  `control_system_goal`, `goal_runtime`, synthesized `cyclic_goal_loop`,
  `protocol_evidence`, review/delivery/verification policies, and the initial
  agenda before advancing. Do not ask the user to provide loop wording, stop
  conditions, clean-pass count, review depth, review scope, commit/push/deploy
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
- "`目标！先调研真实用户需要什么，再实现`": create the goal and its loop,
  but make the first agenda `project-discovery -> lifecycle adoption`. Treat
  examples, current UI, available APIs, and existing fields as hypotheses. Add
  the downstream brief, plan, and executor graph only after the adoption gate.
- "完成 v0.1 收口 / 直到无遗留问题": create or maintain a tool goal when
  available, build a project-state-first agenda, create/update trace, and continue
  until the strict completion rule is met. Ask first when the phase boundary,
  deploy target, known-issue source of truth, acceptance bar, or release/push
  expectation cannot be inferred from project evidence without changing the
  goal.
- "优化 project-lifecycle / goal 体系 / 项目 skill 体系 / 自我迭代规则":
  create or maintain a tool goal before editing unless the user explicitly says
  no goal or wording-only. For a broad objective, build the contract
  `project_optimality_packet` and its compact `perspective_model`; adapt its
  probe sources to the control system and add control-law domain authority. Ask
  first when the requested
  change could reasonably mean
  behavior-only, light-rule, or full-protocol/schema mutation.
- "优化 Codex 配置 / AGENTS / skills / custom agents": treat as the same
  future-behavior control-law change; use a tool goal unless explicitly
  wording-only, no-goal, or one local line. Ask first when the edit boundary or
  persistence/sync target would change the resulting control law.
- "只修这个 diff / 单点改动 / 不做整体推进": without an explicit
  `目标!` / `目标！`, do not create a goal; with the marker, use a lightweight
  goal. In both cases preserve the explicit narrow boundary.
- "继续推进到两轮全局审查无新增问题": keep the goal active until the agenda,
  verification loop, and required clean-pass counter are all satisfied.
- "已有不同 active goal": do not overwrite or silently switch; ask for the
  controlling goal or stop at the current goal boundary.
- "goal tool unavailable": use `activation_state: agenda_only`, preserve the
  same agenda/trace discipline, and disclose that no active Codex tool goal was
  created.

## Cyclic Project Goal Loop

Use a cyclic goal loop for project advancement, version closeout, release
readiness, "继续推进直到完成", "完成 v0.1/v1.0", "没有已知遗留问题",
"两轮全局审查无新增问题", or any goal whose correctness depends on fixing
newly discovered in-scope issues before stopping.

Maintain this state in the trace or Handoff Record:

```yaml
cyclic_goal_loop:
  phase_boundary: <v0.1, v1.0, current milestone, release, or project objective>
  issue_source: <agenda | trace | TODO/backlog | review findings | release checks>
  clean_pass_target: 2
  clean_pass_count: <0..target>
  reset_on: material_in_scope_issue
  latest_code_state: <uncommitted | committed | pushed | not_applicable | blocked>
  deploy_health: <pass | fail | not_applicable | blocked>
  known_residual_issues: <none | list | unknown>
  stop_state: <continue | blocked | complete>
```

The loop order is:

1. Discover the controlling agenda and known-issue source.
2. Implement or delegate the next material item.
3. Verify the changed surface.
4. Commit, push, release, or deploy only when they are part of the goal boundary.
5. Run the required focused/deep/exhaustive review gate.
6. If a material in-scope issue appears, add or reopen agenda work, set
   `clean_pass_count: 0`, and continue from step 2.
7. If no material issue appears, increment the clean-pass count and continue
   until `clean_pass_target` is reached.

A clean pass closes only the bounded claim supported by its inspected surfaces
and evidence; by itself, it does not certify artifact quality or replace further
judgment.

A material in-scope issue is any finding, failed command, missing evidence, or
handoff gap that affects the declared phase boundary, required surface,
acceptance criterion, security/data boundary, deploy health, standard
compliance, handoff readiness, or "no known residual issue" claim. Material
issues reset the clean-pass counter even if they are small to fix.

Do not reset the counter for explicitly out-of-scope ideas, future-version
improvements, optional polish, duplicate findings already represented in the
agenda, user-deferred items, or risks whose non-blocking status is recorded with
evidence.

The goal may stop as complete only when all are true:

- all required agenda items are `done` or user-approved `skipped`,
- current code/docs/config state is verified,
- latest code is committed when the project uses Git and the goal includes a
  deliverable code state,
- latest code is pushed when the user goal, deploy target, or release boundary
  requires remote synchronization,
- deploy/health is `pass` when deployment is in scope, or `not_applicable` with
  evidence when no deploy target exists,
- review clean passes satisfy the requested depth and count after the last
  material change,
- the selected known-issue source contains no unresolved material issue inside
  the phase boundary,
- the authoritative subagent receipt-join and thread-accounting gate in
  `references/subagent-execution.md` passes when delegation occurred.

If code, docs, config, release state, or required evidence changes after a clean
review pass, reset `clean_pass_count` to 0. If remote push or deploy evidence is
unavailable, record the blocker and keep the goal active unless the user changes
the boundary.

## Loop Control Matrix

Use this matrix whenever goal-backed work combines agenda advancement, subagent
waves, review clean passes, optimize framework cycles, release/deploy checks, or
sync verification. These loops are related but not interchangeable.

```yaml
loop_control_matrix:
  active_loops:
    tool_goal: <active | agenda_only | none>
    agenda_loop: <active | none>
    subagent_wave_loop: <active | none>
    review_clean_pass_loop: <focused | deep | exhaustive | none>
    optimize_framework_cycle_loop: <active | none>
    release_or_sync_loop: <active | none>
  reset_edges:
    material_in_scope_issue:
      resets: <agenda item, goal clean pass, review clean pass, optimize cycle, or release/sync evidence>
    verification_failure:
      resets: <agenda item, affected clean passes, release/sync evidence>
    artifact_change_after_clean_pass:
      resets: <review clean pass and parent goal clean pass>
    review_finding:
      resets: <goal clean pass and optimize framework cycle when optimization is active>
    optimization_delta:
      resets: <review clean pass, goal clean pass, affected subagent evidence>
    subagent_scope_or_merge_conflict:
      resets: <wave join and affected agenda item>
    subagent_thread_failure:
      resets: <wave join and affected agenda item>
  stop_precedence:
    - all required agenda items done or user-approved skipped
    - all subagent receipts joined, rejected, or converted into visible agenda state
    - authoritative subagent receipt-join and thread-accounting gate satisfied when delegation occurred
    - required verification/release/sync evidence satisfied or explicitly blocked/not_applicable
    - required review clean passes satisfied after the last material artifact change
    - required optimize framework clean cycles satisfied after the last material optimization point
    - tool goal marked complete only after the above parent stop condition is true
  non_equivalence:
    - a subagent receipt is not agenda completion
    - one review clean pass is not two review clean passes
    - review clean passes are not optimize framework clean cycles
    - a passing command is not review coverage
    - a commit/push/deploy is not goal completion
    - a completed V2 thread is not an accepted receipt
    - a goal completion claim is invalid while unjoined receipts or pending agenda items remain
```

If any loop changes the target artifact after another loop was clean, reset the
affected downstream and parent counters. Do not reset unrelated counters for
explicitly out-of-scope ideas, duplicate findings already represented in the
agenda, or rejected non-material drift.

The controller must record which loop caused a reset. A reset without a source
is a false clean-pass audit trail.

## Incomplete Closeout Targets

When the user gives an incomplete long-horizon target such as "完成 v0.1",
"做完 1.0", or "收口", do not ask the user to draft a complete goal. Create a
project-state-first agenda and delegate bounded read-heavy inspection where useful
to resolve:

- project root and controlling repository,
- plan/backlog source of truth: trace, issues, roadmap, TODO, release checklist,
  handoff doc, or explicit user message,
- deploy target, run/deploy command, and health signal,
- review scope and clean-pass requirement,
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
objective, boundary, value ordering, and stop condition when constructing the
subagent parent target. Goal agenda items carry only the execution node id and
accepted status/result summary; do not copy model-route, assignment, V2 wave,
CAO, or receipt schemas back into this goal reference.
