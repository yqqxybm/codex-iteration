# Goal And Subagent Orchestration

Use this reference when `project-lifecycle` enters goal-backed project concierge
mode or needs bounded subagent delegation.

## Table Of Contents

- Goal Contract
- Control-System Goal Synthesis
- Goal State Machine
- Cyclic Project Goal Loop
- Loop Control Matrix
- Incomplete Closeout Targets
- Agenda Extensions
- Parallel Execution Mode
- Subagent Dispatch
- Runtime Handle Reclamation
- Receipt And Convergence

## Goal Contract

Convert incomplete user targets such as "完成 v0.1" into a verifiable goal:

```yaml
project_goal:
  objective: <single project outcome>
  product_boundary: <what the project is and is not>
  non_goals: <explicit exclusions and phase limits>
  required_surfaces: <product, docs, code, security, tests, deploy, handoff, review>
  success_criterion: <observable finished state>
  verification_loop: <commands, deployment health, review clean passes>
  evidence_boundary: <what evidence can and cannot prove>
  stop_condition: <done, blocked, unsafe, user decision needed>
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

```yaml
goal_synthesis:
  user_objective: <text after 目标! or 目标！>
  target_layer: <local_change | feature_workflow | version_phase | release_operation |
    whole_project | project_system | codex_self_iteration>
  goal_preflight:
    material_model:
      direct_intent: <what the user explicitly wants>
      hidden_intent: <likely reason, frustration, or success need behind it>
      target_world: <repo/product/skill/config/runtime system being changed>
      controlling_tension: <core contradiction or tradeoff that governs success>
      candidate_paths: <2-3 plausible ways to satisfy the objective>
    calibration:
      default_judgment: <best current interpretation before asking>
      key_assumptions: <facts or values the judgment depends on>
      reversal_conditions: <conditions that would change target layer, scope, or stop>
      question_governance: <self-answer | evidence-needed | assumption | blocking-user-question>
    optimality_law:
      what_best_means: <task-specific definition of best>
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
  control_system_goal:
    objective: <single observable outcome written by Codex>
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
      ask_user_when: <user-private reversal variable, missing controlling plan,
        unsafe/destructive boundary>
      block_when: <missing secret, inaccessible deploy/remote, conflicting
        active goal, unsafe operation>
    stop_condition: <controller-written completion boundary>
  subagent_dispatch_policy:
    runtime_permission: <auto_parallel_safe | blocked_by_runtime_or_tool_policy | unsafe_or_not_worth_it>
    decision_basis: <global user preference, agenda evidence, runtime/tool availability, or blocker>
    eligible_parallel_groups: <agenda group ids or none>
    fallback_when_blocked: <main_thread_sequential | main_thread_local_parallel_planning>
  runtime_capability_probe:
    subagent_spawn_mechanism: <callable | unavailable | blocked_by_policy>
    subagent_close_mechanism: <callable | runtime_auto_closes | unavailable | blocked_by_policy>
    custom_project_agents: <available | unavailable | unknown>
    worktree_isolation: <available | unavailable | unknown>
    thread_or_background_sessions: <available | unavailable | not_requested>
    max_parallel_agents: <number | unknown>
    evidence: <tool discovery, runtime output, or explicit policy>
  subagent_runtime_registry:
    - agent_runtime_id: <spawned agent id or not_applicable>
      agenda_item: <id>
      wave: <wave id>
      receipt_state: <pending | received | consumed | rejected | missing>
      close_required: <true | false>
      close_state: <open | closed | not_found | close_failed | not_applicable>
      close_evidence: <tool result or reason>
  parallel_execution_mode:
    mode: <sequential | subagent_wave | controller_team | workflow_batch>
    reason: <why this is the smallest correct coordination structure>
    parallel_roi:
      expected_saved_work: <material | marginal | none>
      coordination_cost: <low | medium | high>
      decision: <parallelize | sequentialize>
    task_graph:
      nodes: <agenda item ids>
      dependency_edges: <blocking dependencies>
      conflict_edges: <same file/schema/route/config/deploy/generated surface conflicts>
      antichains: <parallel-safe groups>
      critical_path: <ids that determine minimum elapsed work>
    merge_strategy:
      isolation: <read_only | same_worktree_disjoint | isolated_worktree_if_supported | main_applies_patch>
      join_barrier: required
      integration_owner: main lifecycle thread
      conflict_resolution: <reject | serialize | main_applies_patch>
    coordination:
      lead: main lifecycle thread
      task_board: <trace/formal plan/in-conversation agenda>
      mailbox: <subagent receipts and main-thread join notes>
      runtime_registry: <subagent_runtime_registry and runtime_resource_ledger>
      claim_policy: <lead_assigns | self_claim_not_supported | sequential>
    quality_gates:
      before_start: <scope, owner, done_when, verification, conflict key, runtime handle registry>
      before_complete: <receipt, evidence, join gate, verification/review, runtime handle closure>
      reset_on: <material issue, failed verification, conflict, or stale assumption>
  loop_control_matrix:
    active_loops: <tool_goal | agenda | subagent_wave | subagent_runtime_loop | review_clean_pass | optimize_framework_cycle>
    reset_edges: <which event resets which counters or states>
    stop_precedence: <which stop condition must be satisfied before completion>
    non_equivalence: <loops/counters that must not be counted as each other>
```

Default synthesis rules:

- Run `goal_preflight` before writing the final `control_system_goal`, creating
  a tool goal, building the agenda, or asking the user. This is a compact
  three-step-analysis adapter, not a visible essay: material model -> calibration
  -> commitment. It exists so the goal prompt knows what problem-world it is
  controlling before it chooses fields, lenses, loops, or subagents.
- `optimality_law` is mandatory for review, optimization, project-system,
  Codex self-iteration, product readiness, version closeout, or any goal where
  "best", "done", or "no known issue" could otherwise expand without limit.
  It must define the value ordering that resolves conflicts between user value,
  engineering quality, product maturity, architecture, delivery, elegance, and
  verification.
- If `goal_preflight` finds a `blocking-user-question`, ask before creating or
  maintaining the tool goal. If all material questions are self-answerable,
  evidence-needed, or safe assumptions, proceed and carry them as explicit risk
  or evidence work.
- Infer the target layer first. If adjacent layers are plausible, choose the
  higher layer unless the user explicitly narrows the boundary.
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
- `push: required` when a remote exists and the goal is version closeout,
  release readiness, deployment, handoff, shared workspace completion, or the
  user asks for a delivered state; otherwise mark `not_applicable` with evidence.
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
- Ask only when a user-private reversal variable, missing controlling plan,
  unsafe/destructive boundary, or conflicting active goal prevents a correct
  synthesized goal. Never ask the user to choose loop hardness, review depth,
  scope, clean-pass count, commit/push/deploy applicability, or stop condition
  when local evidence can determine it.
- If later evidence proves the target layer or stop condition was wrong, record
  `control_reclassification`, regenerate the agenda, reset affected clean-pass
  counters, and continue from the new control law instead of patching the old
  loop silently.
- Build a `loop_control_matrix` whenever more than one loop is active: tool goal,
  agenda advancement, subagent waves, review clean passes, optimize framework
  cycles, release/deploy health, or sync verification. Do not let one loop's
  clean result stand in for another loop's stop condition.
- Automatic parallelization is the default in goal-backed project work. The
  user's standing preference is: when work can be safely parallelized, parallelize
  automatically. Set `subagent_dispatch_policy.runtime_permission` to
  `auto_parallel_safe` when the agenda has disjoint, executable items, the
  runtime exposes a safe subagent mechanism, and current tool policy permits
  spawning for this request. The user does not need to say "并行", "子agent", or
  "分派" only when the active tool policy already authorizes automatic
  delegation.
- If active tool metadata says subagents may be spawned only after an explicit
  user request for subagents, delegation, or parallel agent work, and the current
  user message does not contain that authorization, set
  `runtime_permission: blocked_by_runtime_or_tool_policy`, preserve the task
  graph, and execute sequentially.
- Explicit words such as "并行", "子agent", "分派", "multi-agent", or delegation
  are acceleration signals, not required authorization. They should increase the
  effort spent finding a safe parallel split, but they do not override the safety
  gates below.
- Before setting `runtime_permission` to `blocked_by_runtime_or_tool_policy`,
  attempt runtime tool discovery when a tool-discovery capability is available
  (for example, search for subagent or multi-agent tools). If discovery makes a
  safe subagent mechanism callable, reclassify to `auto_parallel_safe`.
- Record `runtime_capability_probe` before choosing a non-sequential mode. Do
  not infer background sessions, peer-to-peer agent messaging, nested agents, or
  isolated worktrees from the existence of a subagent spawn tool. Also record
  whether spawned agents require an explicit close call, such as `close_agent`,
  before dispatch. If a capability is unknown, treat it as unavailable for write
  isolation and choose `same_worktree_disjoint`, `main_applies_patch`, or
  `sequential`.
- Set `runtime_permission` to `blocked_by_runtime_or_tool_policy` when the current
  Codex runtime has no callable subagent tool or the tool policy forbids spawning.
  Also set it to blocked when spawned agents persist after completion but no
  close mechanism or runtime auto-close guarantee exists.
  Set it to `unsafe_or_not_worth_it` when scopes overlap, the task is too small to
  justify dispatch, ordering matters, or the split would reduce correctness. In
  either case, preserve `eligible_parallel_groups` when useful and disclose the
  fallback instead of asking for permission to do ordinary safe parallelism.
- Apply the ROI gate before dispatch. Parallelize only when expected saved work
  is material after spawn, context packaging, join, merge, and verification cost.
  If the ROI is marginal, keep the task graph but execute sequentially.
- Choose `parallel_execution_mode` before spawning agents. The mode is a control
  topology, not a style preference:
  - `sequential`: use when dependency or conflict edges leave no material
    parallel antichain, or when coordination overhead would exceed the saved
    work.
  - `subagent_wave`: use for one bounded wave of independent read-only,
    verification, review, docs, or disjoint single-writer items whose results
    only need main-thread synthesis.
  - `controller_team`: use for multi-wave project work where the main lifecycle
    thread emulates a team lead over a shared task board: discovery creates new
    tasks, workers finish and return receipts, reviewers/verifiers gate
    completion, and the controller assigns the next unblocked items. In Codex
    this is lead-mediated orchestration unless runtime evidence proves otherwise:
    child agents do not message each other, spawn descendants, own the goal, or
    merge autonomously.
  - `workflow_batch`: use for codebase-wide audits, large migrations,
    cross-checked research, or repeated review/optimization where the plan is
    better represented as phases over many similar tasks. This is a Codex
    workflow plan executed by controlled waves; it is not a background workflow
    engine unless runtime evidence exposes one. The controller writes a phase
    plan first, runs waves of agents per phase, cross-checks results, and then
    reports a synthesized result.
- The mode is optimal when it is the least coordinated mode that preserves the
  required isolation, evidence, and convergence behavior. Do not choose a more
  complex mode merely because more agents are available.

### Perspective Model Synthesis

For review, optimization, deep review-optimize, product readiness, project
system, or Codex self-iteration goals, synthesize `perspective_model` before
writing the final goal or agenda. The user's examples are seed patterns, not the
complete checklist. Codex must generate the smallest role/lens set that can
materially change the judgment.

Use these seed families only when they are relevant to the target:

- explicit user intent and the user's stated frustration,
- core user/customer/operator who must succeed with the product,
- professional engineer maintaining the implementation,
- product manager judging user value, positioning, scope, and adoption,
- architect judging structure, boundaries, long-term change cost, and failure
  propagation,
- security/data/release/operator lens when permissions, secrets, deployment, or
  production risk are in scope,
- competitor-switching or same-category user lens when product quality,
  differentiation, or "would users switch to us" matters,
- future Codex/session/user of the skill when the target governs future agent
  behavior.

Each lens must define a question, evidence surface, and materiality standard.
Do not list roles mechanically. Exclude lenses that cannot change the outcome,
would only add personal taste, or duplicate another lens. For review goals, a
lens can produce findings only from evidence. For optimization goals, a lens can
produce changes only when it improves the optimality standard without unjustified
complexity or re-optimization drift.

Carry `perspective_model` into `goal_synthesis`, the agenda, downstream Context
Packets, review/optimize prompts, and subagent assignments when those actors are
expected to review, optimize, or verify the same claim. If a downstream skill
does not need the full model, pass only the relevant lens summaries.

### Goal Prompt Elegance Gate

Before activating the tool goal or handing work downstream, audit the generated
goal prompt. A goal prompt is elegant only when it is the smallest control law
that still preserves correct behavior:

- each field changes action, evidence, boundary, handoff, or stop condition,
- the `optimality_law` resolves conflicts between lenses instead of letting all
  lenses accumulate equal weight,
- `perspective_model` has no decorative, duplicate, or unverifiable lens,
- the agenda items are executable and do not repeat the same control rule,
- the stop condition is falsifiable from named evidence,
- the prompt states non-goals and forbidden mutations clearly enough to prevent
  silent expansion,
- the user is not asked to provide loop hardness, review depth, clean-pass
  count, role list, stop condition, or prompt wording that Codex can infer.

If the gate fails, simplify or rebuild the goal prompt before creating the tool
goal. Do not treat a longer, more philosophical, or more comprehensive prompt as
better unless it changes one of the control functions above.

Also treat these control-law changes as goal-backed by default: optimizing
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
- Subagents must not inherit, activate, resume, edit, clear, or complete the
  parent goal.
- Subagents must not spawn further subagents. Keep `agents.max_depth = 1`.
- The main thread is the only merge owner and the only actor allowed to mark the
  agenda or goal complete.
- The main thread owns subagent runtime handles. Subagents return receipts; they
  do not close themselves, mutate the runtime registry, or decide whether their
  execution state can remain open.

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
  objective_hash: <stable short hash or slug of objective + boundary>
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
  unless a user-private reversal variable makes the synthesized goal unsafe.
- "`目标！ <project objective>` with multiple independent work surfaces": infer
  `subagent_dispatch_policy.runtime_permission: auto_parallel_safe` when the
  runtime supports subagents, current tool policy permits spawning for this
  request, and the agenda contains disjoint read-only, verification, review,
  docs, or single-writer items. Dispatch automatically within the concurrency
  budget only when that policy gate passes; otherwise preserve the graph and
  execute sequentially with the policy boundary recorded.
- "`目标！ <project objective>` but no subagent tool/runtime support": set
  `runtime_permission: blocked_by_runtime_or_tool_policy`, keep the parallel split
  in the agenda when useful, execute sequentially or with main-thread local
  planning, and disclose the fallback.
- "完成 v0.1 收口 / 直到无遗留问题": create or maintain a tool goal when
  available, build a discovery-first agenda, create/update trace, and continue
  until the strict completion rule is met.
- "优化 project-lifecycle / goal 体系 / 项目 skill 体系 / 自我迭代规则":
  create or maintain a tool goal before editing unless the user explicitly says
  no goal or wording-only. Generate a `perspective_model` that covers at least
  the current user/operator, future Codex session, downstream skill executor,
  reviewer/optimizer, and maintainer lenses unless evidence shows one is
  irrelevant.
- "优化 Codex 配置 / AGENTS / skills / custom agents": treat as the same
  future-behavior control-law change; use a tool goal unless explicitly
  wording-only, no-goal, or one local line.
- "只修这个 diff / 单点改动 / 不做整体推进": do not create a goal; run the
  normal lifecycle chain with the explicit narrow boundary.
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
- all lifecycle-spawned subagent runtime handles are `closed`, `not_found`, or
  explicitly `not_applicable` with evidence.

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
    subagent_runtime_loop: <active | none>
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
    subagent_close_failure:
      resets: <wave join and parent completion eligibility>
  stop_precedence:
    - all required agenda items done or user-approved skipped
    - all subagent receipts joined, rejected, or converted into visible agenda state
    - all lifecycle-spawned subagent runtime handles closed, not_found, or explicitly not_applicable with evidence
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
    - a consumed subagent receipt is not execution-handle closure
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
discovery-first agenda and use `project-explorer` where useful to resolve:

- project root and controlling repository,
- plan/backlog source of truth: trace, issues, roadmap, TODO, release checklist,
  handoff doc, or explicit user message,
- deploy target, run/deploy command, and health signal,
- review scope and clean-pass requirement,
- residual-issue source of truth.

Ask the user only if these cannot be found from local project evidence or if
multiple credible sources would produce different goals.

For "全局审查" without a narrower scope, default to repository-relevant product
readiness: user goal, root charter/version boundary, code/runtime, tests/build,
security boundary, docs/handoff, release/deploy health, standard ledger, and
known backlog/trace/TODO items. Record this inferred scope in the agenda.

"No known residual issue" requires evidence from the selected source of truth.
If no source exists, create one in the trace for this run and record that the
claim is limited to inspected evidence, not unknowable external backlog.

## Agenda Extensions

Add these fields to agenda items when concierge mode or subagents are used:

```yaml
agenda:
  - id: <stable short id>
    objective: <user-visible outcome>
    owner_skill: <project skill or main>
    agent_owner: <main | project-explorer | project-worker | project-reviewer | project-verifier>
    agent_runtime_id: <spawned runtime id when delegated, or none>
    prerequisites: <ids or none>
    owned_scope: <files, modules, artifact, read-only area, or project surface>
    write_policy: <read_only | same_worktree_disjoint | single_writer | isolated_worktree_if_supported | main_applies_patch>
    parallel_group: <none or group id>
    conflict_key: <file, schema, route, shared component, lockfile, config, deploy target, generated artifact, or none>
    dynamic_mission_profile:
      base_agent: <project-explorer | project-worker | project-reviewer | project-verifier>
      specialization: <bounded role for this item, or none>
      derivation_sources: <task_graph_node, perspective_model, owned_scope, verification_required, risk model>
      execution_lens: <what this agent must pay special attention to>
      evidence_surface: <files, workflows, commands, docs, runtime proof>
      materiality_standard: <what counts as a material issue, completion, or opportunity>
      likely_failure_modes: <things this assignment is likely to miss>
      expires_after: this_assignment
    merge_owner: <main lifecycle thread | specific owning skill>
    done_when: <observable completion criterion>
    verification: <command, artifact, or evidence matched to the change type>
    status: <pending | active | done | blocked | skipped>
    result: <artifact, commit, decision, or none>
```

## Parallel Execution Mode

Build the task graph before choosing agent count. The graph has two independent
constraints:

- `dependency_edges`: work that cannot start until another node's evidence is
  complete.
- `conflict_edges`: work that may be logically independent but cannot safely run
  as concurrent writers because it touches the same file, lockfile, schema,
  route, shared component, migration, global config, deployment target, generated
  artifact, or release state.

Parallelism is allowed only inside an antichain with no dependency or conflict
edge between the selected nodes. The critical path determines the lower bound on
elapsed work; spawning agents outside antichains cannot improve that bound and
only adds merge risk.

The task graph is scheduling structure, not execution semantics. Before a
subagent receives a node, derive a `dynamic_mission_profile` for that node. The
mission profile explains how the selected static agent shell should think for
this assignment; it does not create a new permanent agent type.

Run four gates in order:

1. **Capability gate**: prove the current Codex runtime exposes a callable
   subagent mechanism and record whether custom project agents, worktree
   isolation, background/thread sessions, and concurrency limits are actually
   available.
2. **Graph gate**: select only dependency-free and conflict-free antichains.
3. **Isolation/merge gate**: choose `read_only`, `same_worktree_disjoint`,
   `single_writer`, `main_applies_patch`, or
   `isolated_worktree_if_supported` from evidence. Do not claim isolated
   worktree safety when the runtime does not expose it.
4. **ROI gate**: spawn only when the saved critical-path work is larger than
   spawn/context/join/merge/verification cost.

Use this selection proof:

```yaml
parallel_execution_mode:
  runtime_capability_probe:
    subagent_spawn_mechanism: <callable | unavailable | blocked_by_policy>
    custom_project_agents: <available | unavailable | unknown>
    worktree_isolation: <available | unavailable | unknown>
    thread_or_background_sessions: <available | unavailable | not_requested>
    max_parallel_agents: <number | unknown>
    subagent_close_mechanism: <callable | runtime_auto_closes | unavailable | blocked_by_policy>
    evidence: <tool discovery, runtime output, or explicit policy>
  candidate_modes:
    sequential:
      valid_when: <no material antichain or high coordination risk>
      cost: <lowest coordination overhead>
    subagent_wave:
      valid_when: <one antichain, bounded scopes, main-thread synthesis enough>
      cost: <spawn/join overhead>
    controller_team:
      valid_when: <multiple waves, evolving task board, lead-mediated coordination>
      cost: <task-board and join overhead>
    workflow_batch:
      valid_when: <many similar tasks, phased execution, cross-checking needed>
      cost: <phase-plan and cross-check overhead>
  selected: <mode>
  parallel_roi:
    expected_saved_work: <material | marginal | none>
    coordination_cost: <low | medium | high>
    decision: <parallelize | sequentialize>
  merge_strategy:
    isolation: <read_only | same_worktree_disjoint | isolated_worktree_if_supported | main_applies_patch>
    join_barrier: required
    integration_owner: main lifecycle thread
    conflict_resolution: <reject | serialize | main_applies_patch>
  optimality_argument:
    feasibility: <why runtime tools, scopes, and evidence can support it>
    dominance: <why simpler valid modes are insufficient or why more complex
      modes add no material value>
    safety: <how dependency/conflict edges prevent unsafe parallel writes>
    convergence: <how receipts, runtime handle closure, verification, review,
      and clean-pass counters return control to the main lifecycle thread>
```

The proof does not need to be long, but it must be explicit for goal-backed
version, release, whole-project, project-system, or Codex self-iteration work.
If no mode is feasible, preserve the graph and execute sequentially with the
reason recorded.

## Subagent Dispatch

Use subagents to reduce context pollution and parallelize bounded work, not to
avoid main-thread judgment. Prefer the custom project agents when available:
`project-explorer`, `project-worker`, `project-reviewer`, and
`project-verifier`.

Spawn subagents automatically when
`subagent_dispatch_policy.runtime_permission` is `auto_parallel_safe`.
Automatic means the controller decided from the agenda, runtime/tool availability,
and safety gates below that parallelism improves delivery without weakening
correctness. When current tool policy permits automatic delegation, do not ask
the user for permission just to parallelize safe bounded work.

Dispatch follows `parallel_execution_mode`:

- `sequential`: do not spawn for speed; use a subagent only for isolated
  read-only context reduction or assigned verification/review.
- `subagent_wave`: spawn the current antichain, wait for receipts, join, then
  close or account for each runtime handle, then continue in the main thread.
- `controller_team`: keep the main lifecycle thread as lead; maintain the task
  board in the trace or formal plan, spawn bounded waves for unblocked items,
  consume receipts, close or account for runtime handles, add new work, and
  repeat until the goal stop condition.
- `workflow_batch`: write the phase plan first, run each phase as one or more
  waves, include cross-check/reviewer phases, then synthesize only claims that
  survived the phase evidence.

No next wave, phase, agenda item, clean-pass increment, or completion claim may
start until the join barrier has consumed every receipt from the current wave
and the runtime registry shows every no-longer-needed spawned handle as
`closed`, `not_found`, or explicitly `not_applicable`.

If `runtime_permission` is `blocked_by_runtime_or_tool_policy`, keep the agenda's
`parallel_group` metadata as planning evidence, then execute in the main thread
or sequentially and disclose the fallback. If it is `unsafe_or_not_worth_it`, do
not spawn; explain the concrete reason in the handoff or final response.

Custom agents may require a new Codex session or reload before the runtime can
select them. If a custom project agent is not selectable in the current runtime,
use a generic subagent only as an execution container when the assignment prompt
carries the same contract, sandbox boundary, and receipt requirements below.
Otherwise keep the work in the main thread and report that custom agents were
not active. Do not call this equivalent unless the control contract is preserved.

Default concurrency budget:

- Dispatch at most three subagents in one wave.
- Use four to six only for read-only exploration or review with disjoint
  surfaces.
- Run writer items sequentially unless owned scopes are provably disjoint.
- Treat lockfiles, generated artifacts, routes, schemas, shared components,
  global config, deployment config, and release state as single-writer surfaces.
- Keep commit, push, deploy, release mutation, remote sync mutation, parent-goal
  completion, and final project completion claims in the main thread. Subagents
  may inspect, verify, prepare patches, or report evidence for those surfaces, but
  the controller must perform or explicitly authorize the final mutating action in
  the main thread.

Parallel dispatch is allowed only when all are true:

- `runtime_capability_probe.subagent_spawn_mechanism` is `callable` and current
  tool policy permits spawning,
- `runtime_capability_probe.subagent_close_mechanism` is `callable` or the
  runtime proves spawned agents auto-close after completion,
- `parallel_roi.decision` is `parallelize`,
- `merge_strategy.join_barrier` is `required` and the main lifecycle thread is
  the integration owner,
- prerequisites are satisfied,
- each item has concrete `owned_scope`, `done_when`, and verification evidence,
- write scopes are disjoint, or all but one item are `read_only`,
- no two writers touch the same file, lockfile, schema, route, shared component,
  migration, global config, deployment target, or generated artifact,
- every child prompt states: do not touch the parent goal, do not spawn
  subagents, do not commit/push/deploy/sync, do not claim project completion, and
  return a receipt.

Do not spawn persistent subagents when no close mechanism or runtime auto-close
evidence exists. Use sequential execution or non-persistent main-thread work
instead.

If scopes overlap, run the items sequentially. When dispatch is otherwise
permitted, one subagent may provide a patch or analysis-only recommendation for
the main thread to apply.

When a subagent is spawned, immediately add its returned id to
`subagent_runtime_registry`. If spawning succeeds but registry update fails, do
not start additional subagents; record the blocker and reconcile before
continuing.

Every subagent assignment prompt must include this contract:

```yaml
subagent_assignment:
  agent_runtime_id: <spawn_agent returned id when known>
  parent_goal_summary: <objective, boundary, stop condition>
  parallel_execution_mode: <selected mode, antichain, conflict keys, and why this item is safe to run now>
  subagent_dispatch_policy: <auto_parallel_safe decision basis and safety gate evidence>
  runtime_capability_summary: <available subagent/custom-agent/worktree/background capabilities and limits>
  merge_strategy: <read_only | same_worktree_disjoint | isolated_worktree_if_supported | main_applies_patch, plus join barrier>
  dynamic_mission_profile:
    base_agent: <project-explorer | project-worker | project-reviewer | project-verifier>
    specialization: <bounded role for this assignment, e.g. frontend-state-pressure-reviewer>
    derived_from: <task_graph_node + perspective_model + owned_scope + verification_required + risk model>
    execution_lens: <what the agent must emphasize>
    evidence_surface: <specific files, workflows, commands, docs, runtime proof>
    materiality_standard: <what counts as material for this assignment>
    likely_failure_modes: <what this assignment is prone to miss>
    expires_after: this_assignment
  optimality_law_summary:
    <value ordering, elegance constraint, and falsification test relevant to this item>
  control_system_goal_summary:
    <target layer, hardness, delivery policy, stop boundary relevant to this item>
  agenda_item: <id and objective>
  owned_scope: <allowed files, modules, docs, commands, or read-only surface>
  forbidden_scope: <files, systems, or actions not allowed>
  write_policy: <read_only | same_worktree_disjoint | single_writer | isolated_worktree_if_supported | main_applies_patch>
  conflict_key: <shared surface this item must not overlap, or none>
  done_when: <observable item completion condition>
  verification_required: <command, artifact, or evidence>
  hard_boundaries:
    - do not create, edit, resume, clear, or complete the parent goal
    - do not spawn subagents
    - do not commit, push, deploy, sync remote state, or claim project completion
    - do not broaden scope silently; return new_work instead
  required_output: subagent_receipt
```

Use static custom agents as stable shells and dynamic mission profiles as
assignment-specific semantics. A dynamic mission profile may be promoted into a
new static custom agent only when all are true:

- the same profile recurs across projects,
- it needs a distinct sandbox, hard boundary, or trigger,
- its output contract materially differs from the existing receipt contract,
- the runtime can reliably select the new agent after reload,
- and the added static type reduces controller complexity rather than increasing
  agent sprawl.

Otherwise keep it as a dynamic mission profile attached to the assignment.

## Runtime Handle Reclamation

Subagent runtime handles are execution resources, not project evidence. A
receipt can close the semantic loop only after the main thread consumes it; it
does not release the runtime handle. Treat handle reclamation as part of the
join gate, not as a separate optional cleanup task.

Maintain this registry whenever the lifecycle thread spawns a subagent:

```yaml
subagent_runtime_registry:
  - agent_runtime_id: <spawn_agent returned id>
    agent_type: <project-explorer | project-worker | project-reviewer | project-verifier | default>
    agenda_item: <id>
    wave: <wave or phase id>
    spawned_at: <turn or trace marker>
    receipt_state: <pending | received | consumed | rejected | missing>
    still_needed: <true | false>
    close_required: <true | false>
    close_state: <open | closed | not_found | close_failed | not_applicable>
    close_evidence: <close_agent result, runtime auto-close evidence, or reason>
```

Rules:

- Register the handle immediately after `spawn_agent` returns.
- If `wait_agent` times out and the result is still on the critical path, keep
  the agenda item `active`; do not close it merely to make the board clean.
- If a timed-out or failed agent is abandoned, close the handle before
  reassigning the item or starting another wave.
- After a receipt is consumed, rejected, or converted into agenda state, call
  `close_agent` when the runtime exposes it. Record `closed`, `not_found`, or
  `close_failed` from the tool result.
- `not_found` is acceptable only as close evidence for a handle that the runtime
  no longer exposes. It is not evidence that the receipt was consumed.
- `not_applicable` is acceptable only when the capability probe proves the
  runtime auto-closes completed agents or no persistent handle was created.
- `close_failed` blocks parent completion and the next subagent wave unless the
  user explicitly accepts the open handle as residual operational risk.

The main lifecycle thread must not report "all subagents joined" as equivalent
to "all subagent execution state reclaimed." Report both separately.

## Receipt And Convergence

Every subagent must return a receipt:

```yaml
subagent_receipt:
  agent_runtime_id: <id supplied by main thread, or unknown>
  agent: <project-explorer | project-worker | project-reviewer | project-verifier>
  agenda_item: <id>
  assigned_scope: <scope received>
  changed_files: <paths or none>
  evidence: <commands, findings, file refs, or none>
  mission_profile_delta:
    profile_sufficient: <yes | no>
    missing_lens_or_surface: <none | what was missing>
    recommended_profile_change: <none | adjustment for main thread>
  task_graph_delta:
    new_dependency_edges: <edges or none>
    new_conflict_edges: <edges or none>
    blocked_items: <ids or none>
    unblocked_items: <ids or none>
    suggested_reclassification: <agenda/mode/scope changes or none>
  status: <done | blocked | failed | out_of_scope>
  new_work: <required agenda items or none>
  stop_reason: <why the subagent stopped>
```

Do not mark an agenda item `done` from a receipt alone. The main thread must
inspect the receipt, integrate or reject changes, run the required verification
or review gate, and update the agenda. If review or verification finds a
material in-scope issue, add or reopen an agenda item and reset any clean-pass
counter for the affected review loop.

### Join Gate

After a subagent wave, the main thread must join results before selecting the
next item:

1. Validate each receipt has `agent_runtime_id` when supplied, `agent`,
   `agenda_item`, `assigned_scope`, `changed_files`, `evidence`,
   `mission_profile_delta`, `task_graph_delta`, `status`, `new_work`, and
   `stop_reason`. `mission_profile_delta` must state whether the profile was
   sufficient and what lens/surface was missing, with `none` allowed.
   `task_graph_delta` must include `new_dependency_edges`,
   `new_conflict_edges`, `blocked_items`, `unblocked_items`, and
   `suggested_reclassification`, with `none` allowed for every key.
2. Reject or re-run receipts that omit required evidence, exceed scope, or
   conflict with the assigned write policy.
3. Inspect changed files or findings directly; never trust receipt text as
   completion proof.
4. Resolve overlapping edits, stale assumptions, and conflicting findings before
   updating the agenda.
5. Convert material `new_work` and `task_graph_delta` into agenda items,
   dependency edges, conflict edges, or explicitly reject them as
   out of scope with a reason.
6. Run or assign the verification/review gate required by the parent agenda.
7. Mark an item `done` only after its `done_when` condition and evidence match.
8. Reset clean-pass counters whenever a material in-scope issue is found.
9. For every spawned runtime handle in the wave that is no longer needed, call
   `close_agent` when available or record runtime auto-close evidence. Update
   `subagent_runtime_registry.close_state` and `close_evidence`.

The join gate is complete only when every receipt is consumed, rejected, or
converted into visible agenda state, and every no-longer-needed spawned runtime
handle is `closed`, `not_found`, or explicitly `not_applicable` with evidence.
The join gate must not complete while any no-longer-needed spawned runtime
handle remains `open`, `close_failed`, or unaccounted.
