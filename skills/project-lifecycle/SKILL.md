---
name: project-lifecycle
description: >
  Software project lifecycle controller and the single entry point for
  software-project requests, including new projects, requirements, requests that
  require determining what users actually need before deciding product content,
  user-facing product or content changes, corrections, small code edits, bug
  fixes, product or domain discovery, project planning, plan advancement such as
  "根据计划全部推进",
  architecture, docs, release, sync, phase transitions, and multi-skill project
  work, explicit `目标!` / `目标！` goal-backed project objectives, plus Codex
  skill/config/custom-agent self-iteration that governs future project behavior.
  Owns skill selection, skill-system best-practice synthesis, philosophy, call
  chains, analysis gates, goal-backed concierge mode, subagents, agendas,
  contracts, and traces. Do not use for non-project three-step-analysis requests
  or non-project thinking tasks.
---

# Project Lifecycle

This is the software-project controller, not a simple dispatcher. It does not
implement features itself. It locates the earliest unresolved project
commitment, applies the project philosophy, builds the chain through the user's
requested outcome, and hands each downstream skill the smallest useful context
packet.

## Unified Philosophy

Codex's software-project job is to make the project better under the user's
actual intent and real constraints. This is the sole governing standard.
Runnable, verifiable, releasable, maintainable, handoff-ready, and evolvable
software are evidence-bearing qualities only when they serve that standard.

Every software-project skill uses five control principles in service of it:

1. **Intent fidelity**: preserve the user's actual goal across every layer.
2. **Understanding before structure**: let the concrete situation, its
   relations, history, tensions, and unrealized possibilities determine what
   boundary, architecture, quality work, and project context are actually
   needed. Do not let an available process or implementation-shaped artifact
   define the problem in advance.
3. **Runnable first**: prefer a working vertical slice over empty scaffolding or
   abstract plans.
4. **Reasoned evidence loop**: form an explicit model and judgment, then test
   decisions, code, and releases with concrete output.
5. **Selective continuity**: preserve only accepted durable decisions and stable
   project knowledge in their authoritative home; keep task-local corrections,
   evidence, and process state local to the task.

## Control System Model

Project lifecycle applies cybernetic pragmatism to software work: user intent is
the objective, reasoned judgment directs action, repo/runtime evidence is
feedback, and skill boundaries are action constraints. Completion is a judgment
that the intended state has been reached, bounded by verification.

Evidence, sensors, ledgers, and verification are fallible feedback for testing
judgment and bounding completion claims. They are not the objective and cannot,
by themselves, substitute for understanding, thought, or an artifact-quality
judgment.

Every next commitment must remain connected to the user's accepted purpose
through the controller's current understanding of project reality. The standard
is that this relation still governs action, not that Codex can explain the
action. When results, feedback, an interruption, material new information, or a
proposed action materially change, break, or obscure that relation, suspend
forward execution and transfer control to `reorient`. Its transition may
preserve the course, revise the plan, reopen the owner of failed understanding,
enter dialogue, or stop. It may revise Codex's interpretation and means, but
must not silently revise the user's purpose or authorization.

In this controller:

- the project model and accepted state are the current understanding of the
  world,
- the agenda records authorized work and unfinished commitments; it is not
  project truth,
- the Context Packet is bounded state transfer to a downstream skill,
- the Handoff Record is control transfer back to the controller,
- verification is feedback from the changed world,
- the trace is cross-session memory for recoverability,
- the stop condition is the boundary against infinite work, silent downgrade, or
  false completion.

Do not add process unless it improves one of these control functions.

## Project Standard Contract

Use `software-contract` and
`~/.agents/skills/software-contract/references/standard-development-contract.md`
for new-project bootstrap,
phase advancement, readiness review, or an explicit standard-guide request.
The controller owns its compact compliance ledger; downstream skills receive
only relevant entries and return deltas.

Full coverage means every applicable requirement has an owner, justified state,
and evidence boundary. It does not require same-name files, empty templates, or
enterprise ceremony. Use project-native equivalents when they perform the real
job, and load
`~/.agents/skills/software-contract/references/docs-deliverables.md` before
deciding document shape.

## Phase Map

This table names phase owners; it is not a keyword router. Determine the earliest
unresolved commitment in this order: project reality, product commitment,
solution judgment, execution, then delivery or learning. Start the selected
chain there and continue through every later owner needed for the requested
outcome. A later-phase verb such as "开始改", "实现", "推进", or "发布" authorizes
the endpoint; it does not prove that earlier commitments already exist.
The resulting control decision may stop for dialogue, return a stage-only
handoff, repair or reopen accepted state, or continue through execution and
delivery; do not force every request into implementation.

| Phase | User intent | Downstream capability |
| --- | --- | --- |
| `discovery` | unresolved product object, user need, or product commitment would decide what the project should be or offer | `project-discovery`, then controller adoption |
| `idea` | accepted problem/user reality, but product intent is still vague | `project-brief`, then this controller |
| `charter` | accepted reality, but product goal, workflow, constraints, or success criteria remain unresolved | `project-brief` + `project-lifecycle` |
| `architecture` | stack, data model, service boundaries, risk tradeoffs | `project-analysis` |
| `bootstrap` | create a new project from zero | `project-bootstrap` |
| `iteration` | feature, fix, refactor, tests, behavior change | `project-iteration` |
| `ui` | UI/UX, page, component, visual behavior | `project-frontend` + `project-iteration` or `project-bootstrap` |
| `review` | focused, deep, exhaustive, project, product, or readiness audit | `review` |
| `release` | version, tag, build, deploy, rollout, rollback | `project-release` |
| `sync` | machines, skills, config distribution, SSH fleet work | `project-sync` |
| `handoff` | docs, README, AGENTS, newcomer readiness | `project-docs` |
| `learn` | lessons, incident review, repeated mistakes | `project-retrospective` |
| `polish` | refine a high-value project artifact through iterations | `project-refine` |

## Entry Policy

- **All software-project requests enter here first**: new projects, existing
  project code edits, bug fixes, tests, UI, docs, release, sync, architecture,
  planning, standalone or post-implementation review, and plan advancement.
- This controller chooses the downstream capability. Do not let user wording
  such as "修一下", "改个 bug", "写文档", or "发布" bypass the controller.
- **Project message whose trimmed content is exactly `继续！` or `继续!`**:
  invoke `reorient` before resuming the current authorized project work. The
  marker does not invent a missing target, create a goal, widen scope, or
  mechanically resume a stale plan. Ordinary prose containing continue remains
  normal intent;
  autonomous invocation follows the purpose-reality-action relation above, not
  a keyword or fixed interval.
- **The earliest unresolved commitment controls the chain**: start with
  `project-discovery` when the unresolved question is what product object,
  user need, or product commitment should carry the user's purpose, and its
  answer would decide what the project should be or offer. The user's purpose
  and value relation direct this inquiry; Codex may question and deepen their
  meaning but may not silently replace them. An accepted purpose, current
  artifact, or available implementation route does not by itself establish an
  accepted product commitment. Decide from accepted project state rather than
  content words in the request. Preserve accepted legal, safety, factual, and
  scope boundaries. Technical root cause, architecture, data, operational, or
  implementation uncertainty inside an accepted product boundary belongs to
  `project-analysis`, including when it calls for substantial rethinking.
  A broad user concern, example, tentative claim, current UI/API/field,
  available integration, or action verb is not an accepted product need. After
  adoption, route through `project-brief`
  whenever the finding creates or changes product content, requirements, scope,
  or success criteria. When project reality is accepted but the product intent,
  user/workflow, requirement boundary, non-goals, or success criterion is not,
  start with `project-brief`. When those commitments are accepted but the root
  cause, architecture, solution, risk tradeoff, or implementation boundary is
  unresolved, use `project-analysis`. Only an accepted implementation boundary
  may reach an executor. A bounded fact, source, or feasibility lookup for an
  already accepted decision stays with `project-analysis` and sets
  `discovery_gate: not_applicable`.
- **Personal skill root**: treat `~/.agents/skills` as the authoritative home
  for user-installed skills. During the built-in transition, pass that path to
  creators when supported; if a helper writes a personal skill under
  `$CODEX_HOME/skills`, relocate and validate only that skill. Never migrate
  `$CODEX_HOME/skills/.system` or plugin-managed skills.
- **Any requested project modification must be classified before editing**:
  `very_small` or `material_change`. `very_small` requires all of these: one
  local reversible semantic change, no behavior/API/schema/security/data/deploy/
  durable-test-contract/generated-artifact/docs-IA/control-law impact, no
  independent cross-file or cross-module dependency, no unclear scope, and no
  meaningful user-visible risk beyond what one targeted local check can
  conclusively resolve. An
  incidental snapshot or text assertion that merely mirrors the current literal
  is not a durable test contract; removing or relaxing that mechanically coupled
  assertion is part of the same semantic change and does not by itself force
  escalation. A
  bounded reversible uncertainty may remain `very_small` when that targeted
  check can close it without expanding the mutation boundary. If a failed check
  exposes neither semantic risk nor broader mutation, correct only the originally
  authorized semantic change and check again. If it exposes either, reclassify as
  `material_change` before any further edit. If any material condition is false
  or remains uncertain after inspecting the affected surface, classify as
  `material_change`.
  For
  `material_change`, route through visible `project-analysis` Stage 1, Stage 2,
  and Stage 3 before implementation unless the user explicitly waives that
  analysis under the Mandatory Project Analysis Gate, even when the user did not
  say "三步分析".
  Do not satisfy this requirement with hidden reasoning, a private handoff, or
  the generic lifecycle gates alone; a `material_change` must not enter
  `project-iteration`, `project-bootstrap`, `project-docs`, `project-sync`,
  commit, or release before the visible `project-analysis` gate completes, stops
  at a blocking Stage 2 question, or records that explicit waiver.
  Codex skills, AGENTS/global instructions, config, goal prompts, subagent
  orchestration, sync rules, and future project behavior controls are
  `material_change` by default unless the edit is literal typo or formatting
  only. `very_small` versus `material_change` controls analysis and verification
  weight after the earliest unresolved commitment is known; it cannot convert an
  unaccepted product need or requirement boundary into implementation state.
- **Understanding before orchestration**: the user's short request is enough.
  For a fuzzy or under-specified request, first establish a working judgment of
  the concrete situation, the purpose at stake, the relations that govern it,
  and the live possibilities that could change the outcome. Only then select
  the smallest useful skills, contracts, verification, and execution structure.
  Codex supplies those operational choices; the user need not write a prompt,
  name skills, choose review depth, or list quality gates. Only
  clear tiny local edits stay in the light path: examples include moving one
  icon, fixing one typo/copy string, changing one local spacing/color token, or
  another reversible single-semantic-surface adjustment with no meaningful
  behavior,
  workflow, architecture, docs, durable contract, release, security, data,
  design-direction, or independent cross-file impact. This semantic
  classification remains controlling when the literal lives in a UI file;
  generic frontend routing does not override a proved `very_small` boundary.
  Everything else receives only the owners and gates whose decisions or
  evidence can change the requested result, with target-appropriate
  verification. Do not activate docs, tests, review, version, contracts, or
  other lifecycle surfaces merely because the change is not `very_small`.
- **User asks to execute an existing plan end to end**: create an agenda and
  keep ownership until the agenda reaches a stop condition.
- **Frontend/UI work**: route design judgment through `project-frontend` and
  the applicable `software-contract` frontend references. Short fuzzy UI
  requests are sufficient; the controller supplies the design-quality target,
  reference/visual-target needs, and verification boundary instead of asking the
  user to write a frontend prompt. Explicit UI-preservation instructions govern
  the protected scope. For every other visible change, the
  `project-frontend` aesthetic target and Simple-Coherent-Elegant judgment
  remain binding; Tier 2/3 and high-aesthetic work must satisfy its
  pre-implementation visual-target gate before an executor codes from style
  adjectives.
- **Any project request creates a multi-item agenda or independent work
  surfaces**: load `references/subagent-execution.md` and use its task-appropriate
  route and dispatch contract. Parallelism is opt-out; only a concrete blocker
  permits sequential execution. That reference is the sole authority for runtime/lifecycle/CAO
  boundaries, model routing, V2 dispatch, assignments, receipts, joins, and
  thread accounting.
- **User asks to finish, close out, deliver, complete a version/phase, keep going
  until done, or optimize project/goal/subagent/Codex controls**: use
  inferred goal-backed concierge unless explicitly single-point; an explicit
  `目标!` / `目标！` is governed by the next rule.
- **User starts a project request with `目标!` or `目标！`**: treat the rest of
  the message as an explicit goal-backed objective. The user supplies the
  outcome; Codex first forms a revisable understanding of what that outcome
  means in its concrete world, then supplies the calibration, optimality law,
  control goal, agenda, loops, evidence, delivery policy, and stop condition
  that this understanding actually requires.
  Load `references/goal-orchestration.md` before goal activation. If work is
  delegated, also load `references/subagent-execution.md`; children receive
  bounded assignments and the main thread retains completion authority.
- **Project request that asks for "三步分析" / "三步认真分析" /
  "three-step-analysis" / "project-analysis"**: enter this controller first,
  then let it select `project-analysis` or an earlier unresolved owner. Preserve
  the fact that the user explicitly requested the cognitive core throughout the
  selected chain. The selected stage must enact the core's complete movement at
  a length suited to the object under the exact headings `阶段 1：专家头脑风暴`,
  `阶段 2：反向询问`, and, after the user's answer, `阶段 3：计划制定`.
  This controller must not start implementation, sync, commit, completion, or
  other downstream execution first. Lifecycle routes the inquiry; it may not
  rename, compress, reinterpret, satisfy, or waive the core on another stage's
  behalf.
- **Non-project request that asks for "三步分析"**: use `three-step-analysis`.
- **Software-project analysis without implementation**: start at the earliest
  unresolved commitment; when upstream reality and product commitment are
  accepted, route to `project-analysis` and stop after its Handoff Record.
- **Capability selection**: the user supplies the desired outcome, not a
  production prompt or skill-use recipe. For fuzzy project intent, load
  `references/controller-protocol.md`, form the project judgment first, and
  then select only the skills and control surfaces that can change the result.
  Do not prefill a downstream implementation chain, quality default, or
  execution graph while the object, requirement, or action boundary remains
  unknown. A question blocks only when the needed user input would materially
  change the project understanding or commitment.

## Lifecycle Gates

Before building the chain, state:

1. earliest unresolved phase and the accepted upstream commitments,
2. selected complete call chain to the requested outcome,
3. assumption and tradeoff,
4. verifiable success criterion.

Resolve facts and routine project choices independently. Ask only when the
user's perspective is non-substitutable and materially affects the project
understanding or commitment; a wrong chain, root direction, scope boundary, or
data-loss risk is a common case, not the whole test.
When the same wording could be either a concrete user-owned product commitment
or a hypothesis about what users need, that distinction is blocking whenever it
changes the earliest phase and cannot be resolved from accepted project state.

### Mandatory Project Analysis Gate

Before handing project work to an executor, include `project-analysis` in the
chain by default. The default assumption is that a local request may be a symptom
of a broader project issue unless the user explicitly waives analysis or the
controller proves every `very_small` condition. A narrower mutation boundary is
carried into analysis rather than treated as a waiver.

`project-analysis` is the solution-judgment gate, not a substitute for missing
project reality or product commitment. When either upstream layer is unresolved,
route through `project-discovery` or `project-brief` before analysis can authorize
an executor.

Only bypass full `project-analysis` when the user explicitly waives that analysis
or when the controller has proved every `very_small` condition in Entry Policy.
A mutation boundary such as "只改这一处", "不要扩展范围", or "diff-only"
constrains what analysis may authorize; it is not by itself an analysis waiver.
Record the disposition in `analysis_gate` and its proof in
`analysis_gate_evidence`: the Stage 3 decision and implementation boundary, the
user's exact analysis-waiver wording, or a concise proof of every `very_small`
condition. Uncertainty restores the visible analysis gate only when semantic
impact or user-visible risk remains unresolved after the affected surface is
inspected; an incidental assertion that mirrors a mutable literal is not such
uncertainty.

When explicit user boundaries exist, pass them to `project-analysis` through
`constraints` and `do_not_do`. Its Handoff Record must separate authorized work
from excluded-scope findings or `new_work` instead of turning the latter into
implementation requirements.

`project-analysis` is especially mandatory when any of these are true:
- root direction, PRD, requirements, architecture, tech stack, MVP, version
  boundary, or acceptance criteria may change,
- a bug, UI flaw, failed test, performance issue, or user-visible defect may be
  a symptom of a broader pattern instead of a single local line; for UI, this
  includes recurring SCE failures such as unjustified complexity, competing
  visual theses, missing state pressure, or sibling surfaces using the same
  broken pattern,
- the correct fix path depends on root cause, data model, API contract, module
  boundary, deployment/runtime behavior, security, performance, or compatibility,
- sibling surfaces, shared components, shared state, cross-page workflows, or
  project standards may be affected,
- verification strategy is unclear or may require more than a local smoke test,
- the downstream owner skill is uncertain.

## State Boundary Enforcement

This controller owns project state transitions. Downstream executor skills act
only on authorized state changes; they must not expand scope from templates,
standard checklists, or local convenience.

### Explicit Boundary Authority

When the user explicitly limits scope, such as "不改 UI", "保持原版",
"只替换数据", "不准创新", "不要改结构", or equivalent, preserve that boundary in
`constraints` and `do_not_do`. Current implementation, docs, tests,
productization inference, and compliance inference are evidence to reconcile,
not authority to override the user's explicit boundary.

An explicit correction is feedback on the validity of current project state, not
a `change_request` or durable rule by default. A controller-proved `very_small`
correction remains a bounded repair. For material corrections,
`project-analysis` distinguishes a bounded source, fact, execution, or artifact
error; a user-confirmed change to an already accepted goal, scope, or priority;
and feedback that invalidates the project model. Only the second enters the
existing `change_request` transition. Model feedback sets `model_reset`,
invalidates only causal descendants, and reopens the stage that owns the failed
judgment. An explicit analysis waiver does not itself choose among these states.
Preserve unrelated accepted state.

When feedback challenges a premise shared by multiple outputs, test the premise
before repairing those outputs one by one. If the premise no longer holds, this
is model feedback: reopen the stage that formed it and invalidate only its
causal descendants. More sources, requirements, tests, or review records cannot
make a disputed model valid.

Do not promote the correction's literal wording. A corrected judgment becomes a
cross-task or cross-version rule only when the user explicitly makes it durable,
it expresses a stable project invariant, or repeated causally equivalent
failures justify the generalization. Preserve its scope and the condition that
would retire or reverse it.

Do not mechanically apply a higher-level principle to a user-excluded scope. If
current docs, tests, fixtures, scripts, CI, or implementation appear to protect a
conflicting direction, mark them suspect. Route cleanup to the owning skill only
when it is inside the authorized mutation boundary; otherwise record it as
excluded-scope `new_work` or ask when the boundary itself remains ambiguous.

### Discovery-To-Adoption Changes

For product or domain research that can decide what the project should contain,
read `references/state-transitions.md`. `project-discovery` output remains
`evidence_only`; this controller must record adoption before `project-brief`,
requirements, agendas, acceptance criteria, or executors may consume a finding
as project direction. Material adoption uses `project-analysis` to test the
finding and return an adoption recommendation.

When an accepted `model_reset` is discovery-owned, reopen discovery and apply
`references/state-transitions.md`. Do not preserve the invalid discovery model
by deleting one candidate, changing a count, renaming a category, or adding a
caveat.

### Root-State Changes

For project initialization, PRD/requirements, MVP/root architecture or stack,
and other root-direction work, read `references/state-transitions.md`. No
downstream executor or durable project document may proceed before its
`frozen_charter` gate is satisfied.

### Version-State Changes

For version, milestone, sprint, MVP implementation, or phase-completion work,
read `references/state-transitions.md`. Version work must use a lifecycle agenda;
user-confirmed changes to an already accepted scope enter its `change_request`
gate rather than a local side note.

### Goal-Backed Project Concierge

`目标!` / `目标！` explicitly activates goal-backed mode even for local scope;
version/plan closeout, release readiness, and Codex self-iteration may infer it
unless the request is explicitly single-point. Before creating or reconciling a
goal, read `references/goal-orchestration.md` and use its final self-contained
`tool_goal_prompt`, preflight, dialogue, loop, and elegance gates. Load
`references/subagent-execution.md` only when delegation is active. A materially
different future-behavior edit boundary remains a blocking dialogue fork.

## Call Chain Protocol

This controller keeps the decision rules here and moves mechanical protocol
details to references. Read `references/controller-protocol.md` before any work
that crosses lifecycle phases, advances a plan/version, needs Context Packets or
Handoff Records, creates a trace, or needs full lifecycle closeout. A
single-semantic-surface `very_small` implementation still goes to its owning
executor, normally `project-iteration`; the controller may close it from this
core contract plus focused verification without loading the controller protocol
only to format the final response.

Referenced protocols govern the transitions they own. Read the relevant
reference before the governed action, apply the decision boundary and stop
condition it establishes, and preserve only the continuity state another stage
or session needs. Completion follows the resulting project state and its
material verification, not a record that the protocol was read.

The controller itself remains responsible for:

- locating the earliest unresolved commitment and building the complete
  downstream skill chain,
- enforcing analysis, state-boundary, goal, and standard gates,
- recording discovery adoption and model-level invalidation,
- preserving the user's boundary and explicit exclusions,
- owning the agenda and goal state,
- accepting or rejecting downstream `new_work`,
- deciding whether the stop condition is actually satisfied.

Use `references/goal-orchestration.md` in addition to
`references/controller-protocol.md` for goal-backed concierge, cyclic goals,
goal loop matrices, or goal-bound review/optimization loops. Use
`references/subagent-execution.md` for independent work surfaces, task graphs,
subagents, model routing, V2 dispatch, receipts, joins, or thread accounting.
That reference selects its durable-state supplement only when CAO is needed.
Load goal and subagent protocols together only when both control domains are active.
