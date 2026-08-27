---
name: project-analysis
description: >
  Downstream software-project analysis stage selected by project-lifecycle, and
  the adapter for 项目三步分析 / 代码三步分析 inside project work. Use after the
  project lifecycle controller chooses analysis for architecture, stack choices,
  debugging and bug root-cause strategy, codebase risk, performance/security
  tradeoffs, PRD/requirements/MVP/version boundary decisions, implementation
  path selection, adoption of project-discovery findings,
  regression/systemic-risk checks, or any material
  software-project change before implementation. The lifecycle controller may
  skip it for an explicit analysis waiver or a fully proved `very_small` change.
  A local mutation boundary alone only scopes the analysis. Does not edit code;
  returns a Handoff Record to project-lifecycle.
---

# Project Analysis

This is the software-project adapter for the `three-step-analysis` cognitive
core. Preserve the current three-step-analysis philosophy:

1. build a project-world model from the user's goal, project relations, and
   repo/product/runtime reality,
2. bring its current judgment into dialogue when the user's perspective is
   non-substitutable and material,
3. commit to a verifiable project decision and downstream execution boundary.

Add only project reality: repo context, verification paths, lifecycle handoff,
and implementation boundaries.

## Lifecycle Position

This is not the project entry point. `project-lifecycle` is the single entry
point for software-project requests and selects this skill as the downstream
analysis stage. A request that names `project-analysis` or project/code
three-step analysis still enters `project-lifecycle`; the controller either
selects this adapter or returns to an earlier unresolved owner.

When selected by `project-lifecycle`, use this skill by default before project
implementation. A small code request can still be a local expression of a
broader system issue, so do not skip this skill merely because the requested
diff looks small.

When the user explicitly asks for project/code "三步分析", "三步认真分析",
"three-step-analysis", or "project-analysis", this adapter is a visible
non-skippable gate, not hidden preparation. Return a staged result that exposes:
Stage 1 project-world model, Stage 2 dialogue governance, and Stage 3 verifiable
project decision. Do not let `project-lifecycle` continue to implementation,
sync, commit, or final completion until the three visible stages are complete or
Stage 2 is blocked awaiting the user's answer.

When the user asks to change, fix, implement, update, optimize, configure,
sync, or rewrite project/code artifacts, this adapter is also the default
visible gate for any `material_change` unless the lifecycle records the user's
explicit analysis waiver, even if the user did not say "三步分析". A project/code
change is `very_small` only when it is one local reversible semantic change with
no behavior, API, schema, security, data, deploy, durable test-contract,
generated-artifact, docs information-architecture, control-law, independent
cross-file, or cross-module impact, no unclear scope, and no meaningful
user-visible risk beyond what one targeted local check can conclusively resolve.
An incidental snapshot or text assertion that only mirrors a mutable literal is
mechanically coupled cleanup within the same semantic change, not test-contract
impact. A bounded reversible
uncertainty may remain `very_small` when that check can close it without
expanding the mutation boundary. If a failed check exposes neither semantic risk
nor broader mutation, correct only the originally authorized semantic change and
check again. If it exposes either, reclassify as `material_change` before any
further edit. If any material condition is false or remains uncertain after
inspecting the affected surface, classify it as `material_change` and expose
Stage 1, Stage 2, and Stage 3 before returning implementation boundaries.

Use it for project or code decisions that need thinking before action:
architecture, debugging direction, stack selection, API design, migration risk,
security tradeoffs, performance strategy, phase planning, PRD/root requirements,
version/MVP scope, implementation strategy, regression diagnosis, and any bug or
feature where the visible request may be a local expression of a broader system
issue.

The lifecycle controller may skip this stage when the user explicitly waives
project analysis, or when every `very_small` condition above is proved. Scope
limits such as "只改这一处", "不要扩展范围", or "diff-only" remain analysis
constraints, not waivers, unless the user also says to skip project/systemic
analysis. Record which disposition applies; uncertainty is material and must not
use the light path only when semantic impact or user-visible risk remains
unresolved after inspecting the affected surface.

It does not edit code. Return the decision to `project-lifecycle`; implementation
belongs to downstream executor stages such as `project-iteration` or
`project-bootstrap`.

Do not use it for:
- ordinary non-project deep thinking; use `three-step-analysis`,
- unresolved user, market, competitor, product, or domain reality that will
  decide what to build; return to `project-lifecycle` for `project-discovery`,
- accepted project reality with an unresolved product commitment; return to
  `project-lifecycle` for `project-brief`,
- direct implementation in an existing repo; return implementation boundaries
  to `project-lifecycle` so it can select `project-iteration`,
- new project scaffolding; return bootstrap boundaries to `project-lifecycle`
  so it can select `project-bootstrap`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before analysis.
Preserve the controller-accepted intent and boundaries, owned analysis scope,
active goal/plan state, and only the quality, verification, or subagent
projection relevant to this decision. Do not instantiate or echo absent packet
fields.

When the packet includes a `discovery_handoff`, treat every finding and
adoption candidate as `evidence_only`. Test it independently and return an
adoption recommendation; only `project-lifecycle` can record the resulting
project decision.

Before analyzing an implementation path, require a controller-accepted project
commitment. An accepted purpose does not close discovery when the object or the
relation through which the project should realize that purpose remains unsettled
enough to change the direction. Return that condition to `project-lifecycle` as
an upstream judgment rather than inferring it from content words or the current
artifact.
If project reality is accepted but the requirement, scope, non-goal, or success
boundary is missing, return `project-brief`. Do not use technical feasibility,
current artifacts, or the user's action verb to manufacture either upstream
state.

That return is an upstream-routing Handoff, not a completed solution judgment:
do not emit `analysis_gate: project_analysis_consumed`. Only a Stage 3 decision
that establishes the implementation or analysis boundary may consume the gate.
When the incoming packet carries `three_step_visibility: explicit`, preserve it
in this Handoff so the controller can require the earlier owner to expose the
same compact visible Stage 1/2/3 gate.

After Stage 3 completes, return an ordinary Handoff Record: the conclusions that
change the project judgment, plan, or action; unresolved questions; and the
verification boundary. Include the next recommended skill only when the
conclusion directs a subsequent action. Preserve the visible Stage 3 decision and
implementation boundary without turning the handoff into a parallel tracking
protocol. Use `.codex/traces/` only for long or resumable chains.

If invoked as a subagent, preserve the assigned `assignment_id`,
`execution_owner_id`, `agent_owner`, and `write_policy`; do not edit the parent
goal, spawn subagents, commit, push, deploy, sync remote state, broaden scope, or
claim project completion. Return the exact assignment-required
`subagent_receipt`; a Handoff Record may accompany but never replace it.

## Project Analysis Rules

### 1. Stage 1 Maps To Project Reality

Use `three-step-analysis` Stage 1, but ground the material-spread and brainstorm
in project facts:
- user-visible symptom or requested behavior,
- possible local expression vs broader system pattern,
- current repo/module/service boundary,
- user-visible goal,
- explicit user boundaries and exclusions, plus any user correction as feedback
  on whether the current artifact, commitment, or project model remains valid,
- existing architecture and local conventions,
- hard constraints, data or security risk, deployment/runtime context,
- traceability of current docs/tests/implementation to the user request,
  trusted facts, approved product boundary, or specified artifact,
- for UI/frontend work, whether the visible request reflects a broader
  Simple-Coherent-Elegant failure: unjustified complexity, competing visual
  theses, disproportionate expressive moves, missing state pressure, or sibling
  surfaces sharing the same pattern,
- commands that would verify the decision.

The following Stage 1 cognitive minimum is non-skippable. Project evidence and
verification are inputs and tests for this judgment; they cannot independently
prove that analysis is complete:
- understand the object's nature before selecting the relevant factual,
  normative, interpretive, aesthetic, or strategic reasons;
- expand the material through relevant roles, relationships, feedback loops, and
  time, distinguishing inspected facts from inferences;
- name the governing structure and the standard by which the decision will be
  judged, then identify the dominant variable instead of weighing every project
  dimension equally;
- explore enough genuine alternatives to test the leading judgment, with their
  applicability, benefit, cost, and preservation boundaries; when no material
  alternative exists, use the strongest opposing view, counterexample, boundary,
  or failure mode instead of manufacturing extra paths;
- revise the judgment when that test exposes a flaw, and connect the material,
  governing structure, and dominant variables through reasons appropriate to the
  object, including what evidence or user experience would force correction.

Stage 1 must still produce the three-step-analysis 可校准暂时判断, adapted to
the project:
- default technical/product decision if no question is asked,
- material alternatives and why the top path currently wins, when genuine
  alternatives exist,
- key assumptions about repo facts, user goals, constraints, risk, and
  verification,
- the project relation, value tension, experience, or consequence that supports
  the judgment and would distinguish it from its strongest challenge,
- correction and symptom scope, determined by the model test below,
- material unknowns, evidence needs, dialogue candidates, and follow-up risks,
- reversal conditions that would change the decision or implementation boundary,
- facts Codex should inspect directly,
- user perspectives that cannot be responsibly substituted and would materially
  correct, deepen, reframe, or co-determine the project judgment.

Apply the same model test when a user correction challenges an existing project
conclusion. A bounded source, fact, execution, or artifact error permits local
repair. Only a user-confirmed change to an already accepted goal, scope, or
priority is a `change_request`; correcting Codex's mistaken understanding of the
original goal is not. If the correction instead shows that the project object,
actors, task, judgment standard, explanatory relation, root cause, method, or
decision premise is unsound, recommend `model_reset`, identify only its causal
descendants, and name the decision stage that owns the failed judgment. Do not
preserve the old model by locally changing its output.

For any decision that introduces or changes user-facing product content or
capability, confirm that its product commitment is grounded either in the user's
concrete product decision or in controller-adopted discovery. A general concern,
example, tentative claim, or request to "开始改" is not sufficient. For a
discovery adoption decision, additionally test whether each proposed conclusion
closes the explanatory relation `actor and situation -> task or judgment ->
needed information or capability -> changed outcome`, including applicability
and reversal conditions. Current UI, APIs, fields, docs, tests, available data,
or competitor prevalence can test feasibility or constrain a choice; they cannot
independently prove user or product need.

When the Standard Development Contract is active, evaluate analysis-owned guide
entries: tech stack tradeoffs, ADR requirement, architecture boundaries,
data/API contracts, deployment topology, observability/SLO applicability,
performance/security tradeoffs, and NFR applicability. Mark them with evidence
or return them as missing/blocking work; do not let analysis decisions remain
outside the ledger.
When standard details affect the decision or ledger status, load
`software-contract` and read
`~/.agents/skills/software-contract/references/standard-development-contract.md`.
If the required reference is unavailable, stop and report the missing resource.

Do not answer from generic best practice when the repo or project docs can be
inspected. If local context is unavailable, state that limit explicitly.

### 2. Stage 2 Runs Project Dialogue Governance

Use the mutually exclusive Stage 2 gate from `three-step-analysis`. Form the
current project judgment first, then deliberately derive the strongest questions
that could correct, deepen, reframe, or co-determine it. Select either
`需要对话并停止` or `无需阻塞`; do not mechanically ask, but do not silently
consume the user's perspective either.

Ask and block only when the user's perspective is both non-substitutable and
material to the project understanding or commitment. Materiality includes a
substantive change in the problem model, product or implementation boundary,
success standard, value relation or concrete tradeoff, risk acceptance,
verification meaning, or
downstream chain; it is not limited to reversing the selected path. Resolve
facts, repo state, external sources, and professional engineering judgments
independently. If `request_user_input` is available and the question fits
mutually exclusive options, use it with 1-3 concise questions and a recommended
answer; otherwise ask concise text questions and stop before the decision.

Once the dual threshold is met, the question is a hard stop, not a label. Do
not convert it to a checklist, user homework, assumption, or follow-up risk in
the same response. Do not return Stage 3, a recommendation, project decision,
Handoff Record, or implementation boundary until the user answers. "Analysis
only" prevents edits; it does not downgrade blocking dialogue.

Root-direction, goal-backed, version, PRD, architecture, project initialization,
MVP, release, and product-positioning analyses have higher dialogue sensitivity.
For these requests, missing target user, product boundary, non-goals, success
criterion, risk acceptance, delivery expectation, or external-state dependency
normally meets the dual threshold unless Stage 1 shows that context or project
facts already answer it without substituting for the user's purpose.

High-risk future-behavior controls inherit the light-native three-step rule.
For Codex skills, AGENTS/global instructions, config, goal prompts, lifecycle
rules, subagent orchestration, automatic writing, automatic commit, automatic
push, deploy, sync, destructive operations, production/data/security boundaries,
or other persistent project behavior, generic words such as "automatic",
"default", "push", or "full automation" are not a complete risk policy. If
Stage 3 would recommend making such behavior a long-term default and the user
has not stated the concrete authorization boundary, that authorization is both
non-substitutable and material: Stage 2 must ask before returning a project
decision.
This applies even when the current request says "analysis only"; analysis-only
prevents editing, but it does not remove the need to calibrate a recommended
future default.

If current docs, tests, fixtures, scripts, CI, or implementation conflict with
an explicit user boundary, first treat them as suspect evidence. Ask only when
traceability still leaves a user-dependent project meaning or edit boundary.

If the remaining uncertainty can be resolved by repo inspection, docs, commands,
tests, external sources, or engineering judgment, do that instead of asking. If
no candidate question meets both thresholds, state `无需阻塞` with the current
project judgment and one concise, specific reason dialogue is not needed, then
proceed to Stage 3. Do not use a ledger or classification table as a substitute
for this judgment.

Do not ask preference questions that only change wording, style, minor
implementation taste, or make the user choose between under-argued technical
paths. The question must show the current judgment and how the user's answer
would materially participate in the project understanding or commitment.

Stage 2 is a visible gate in project analysis. Do not return a project decision
or implementation boundary until the Handoff Record or response exposes either
the blocking project question or the current judgment plus the concise reason
dialogue is not needed. For explicit project/code three-step-analysis, this
visible gate is mandatory even when analysis is followed by implementation in
the same turn.

For project-system control changes, including Codex skills, AGENTS/global
instructions, goal prompts, lifecycle rules, subagent orchestration, and future
project behavior, competing interpretations of the edit boundary meet the dual
threshold when they would lead to materially different mutations. Ask before
editing or recommending edits; do not silently choose between behavior-only,
light-rule, and full-protocol/schema changes.

### 3. Stage 3 Commits To A Project Decision

Use `three-step-analysis` Stage 3, but the final decision must be project-facing:
- recommended path,
- why it fits this project,
- how it responds to the Stage 1 governing structure and, for a user correction,
  the Stage 1 classification, affected boundary, and resulting recommendation,
- material alternatives rejected and why, when any exist,
- risks and rollback/escape path,
- exact verification evidence expected,
- downstream skill to execute if implementation is requested.

For a discovery adoption decision, also return:

```yaml
adoption_recommendation:
  decision: <adopt | adopt_partial | reject | ask | model_reset>
  accepted_conclusions: <exact conclusions and boundary, or none>
  rejected_or_unresolved: <what remains evidence_only and why>
  rationale_and_reversal: <causal reason and what would change it>
  causal_descendants_to_invalidate: <only when model_reset, otherwise none>
```

This is a recommendation to `project-lifecycle`, not authority to update the
charter, requirements, agenda, docs, tests, or implementation directly.

For UI/frontend decisions, Stage 3 must state the simplest coherent elegant path:
what complexity should be removed or refused, what design thesis should unify
the surface, what expressive move is worth keeping, and which browser/state
evidence should prove it.

For boundary-sensitive changes, name the authorized mutation boundary. Separate
suspect docs, tests, fixtures, scripts, CI assertions, or implementation guards
that may be cleaned inside that boundary from excluded-scope findings that must
be returned as `new_work` or left untouched.

The Stage 3 result must be a verifiable project decision or execution plan. Do
not substitute continued questioning, risk listing, or explanatory framing for
the plan unless Stage 2 is blocked and awaiting a user answer.

If the user asked only for analysis, return the analysis Handoff Record to
`project-lifecycle` and stop. If the user asked to solve or implement, return
the downstream recommendation to `project-lifecycle`; do not invoke executors
directly from this skill.

### 4. Stage 4 Is Handoff, Not Local Implementation

Do not edit files inside `project-analysis`. When the user wants implementation,
convert the decision into a Context Packet recommendation for
`project-lifecycle`:
- unresolved project reality -> `project-discovery`,
- unresolved product commitment -> `project-brief`,
- new project -> `project-bootstrap`,
- existing project change -> `project-iteration`,
- release/deploy -> `project-release`,
- docs/handoff -> `project-docs`,
- multi-phase work -> `project-lifecycle`.

## Final Response

Report:
- decision or diagnosis,
- assumptions that matter,
- material alternatives rejected, when any exist,
- verification plan or command,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- next implementation skill, if any.
