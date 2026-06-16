---
name: project-analysis
description: >
  Downstream software-project analysis stage selected by project-lifecycle, and
  the adapter for 项目三步分析 / 代码三步分析 inside project work. Use after the
  project lifecycle controller chooses analysis for architecture, stack choices,
  debugging and bug root-cause strategy, codebase risk, performance/security
  tradeoffs, PRD/requirements/MVP/version boundary decisions, implementation
  path selection, regression/systemic-risk checks, or any software-project
  change before implementation unless the user explicitly says no
  full-project/systemic analysis is needed. Does not edit code; returns a
  Handoff Record to project-lifecycle.
---

# Project Analysis

This is the software-project adapter for the `three-step-analysis` cognitive
core. Preserve the current three-step-analysis philosophy:

1. build a project-world model from concrete repo/product/runtime evidence,
2. calibrate the variables most likely to cause a wrong technical decision,
3. commit to a verifiable project decision and downstream execution boundary.

Add only project reality: repo context, verification paths, lifecycle handoff,
and implementation boundaries.

## Lifecycle Position

This is not the project entry point. `project-lifecycle` is the single entry
point for software-project requests and selects this skill as the downstream
analysis stage.

When selected by `project-lifecycle`, use this skill by default before project
implementation. A small code request can still be a local expression of a
broader system issue, so do not skip this skill merely because the requested
diff looks small.

Use it for project or code decisions that need thinking before action:
architecture, debugging direction, stack selection, API design, migration risk,
security tradeoffs, performance strategy, phase planning, PRD/root requirements,
version/MVP scope, implementation strategy, regression diagnosis, and any bug or
feature where the visible request may be a local expression of a broader system
issue.

The lifecycle controller may skip this stage only when the user explicitly says
full-project/systemic analysis is unnecessary, such as "只改这一处", "不要整体分析",
"不要扩展范围", "diff-only", or equivalent.

It does not edit code. Return the decision to `project-lifecycle`; implementation
belongs to downstream executor stages such as `project-iteration` or
`project-bootstrap`.

Do not use it for:
- ordinary non-project deep thinking; use `three-step-analysis`,
- fuzzy task wording; use `project-brief`,
- direct implementation in an existing repo; return implementation boundaries
  to `project-lifecycle` so it can select `project-iteration`,
- new project scaffolding; return bootstrap boundaries to `project-lifecycle`
  so it can select `project-bootstrap`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before analysis.
Preserve `intent`, `constraints`, `owned_scope`, `verification_required`,
`standard_compliance_ledger`, and `do_not_do`. When provided, also preserve
`project_goal`, `goal_runtime`, `goal_synthesis` / `control_system_goal`,
`goal_preflight` / `optimality_law`, `perspective_model`,
`plan_state_sink`, `cyclic_goal_loop`, `loop_control_matrix`,
`review_clean_pass_loop`, `optimize_framework_cycle_loop`,
`subagent_dispatch_policy`, `agent_owner`, `write_policy`, and
`protocol_evidence`.

Return a Handoff Record with decision, alternatives rejected, assumptions,
verification plan, implementation entry point, `standard_compliance_delta`, open
risks, `domain_resource_evidence` when `software-contract` was loaded, and the
next recommended skill. When a lifecycle agenda is active, include item status,
result, and verification evidence needed for `plan_state_sink`
persistence. Use `.codex/traces/` only for long or resumable chains.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Return findings as a receipt
or Handoff Record to `project-lifecycle`.

## Adapter Rules

### 1. Stage 1 Maps To Project Reality

Use `three-step-analysis` Stage 1, but ground the material-spread and brainstorm
in project facts:
- user-visible symptom or requested behavior,
- possible local expression vs broader system pattern,
- current repo/module/service boundary,
- user-visible goal,
- existing architecture and local conventions,
- hard constraints, data or security risk, deployment/runtime context,
- commands that would verify the decision.

Stage 1 must still produce the three-step-analysis 可校准模型, adapted to the
project:
- default technical/product decision if no question is asked,
- ranked alternatives and why the top path currently wins,
- key assumptions about repo facts, user goals, constraints, risk, and
  verification,
- symptom scope: why the request is local, systemic, or not yet known,
- ignorance map: known facts, inferred facts, unknowns, reversal variables,
  evidence-needed variables, user-private variables, and follow-up risks,
- reversal conditions that would change the decision or implementation boundary,
- facts Codex should inspect directly,
- user-private variables that truly require confirmation.

When the Standard Development Contract is active, evaluate analysis-owned guide
entries: tech stack tradeoffs, ADR requirement, architecture boundaries,
data/API contracts, deployment topology, observability/SLO applicability,
performance/security tradeoffs, and NFR applicability. Mark them with evidence
or return them as missing/blocking work; do not let analysis decisions remain
outside the ledger.
When standard details affect the decision or ledger status, load
`software-contract` and read
`~/.codex/skills/software-contract/references/standard-development-contract.md`.
If the required reference is unavailable, stop and report the missing resource.

Do not answer from generic best practice when the repo or project docs can be
inspected. If local context is unavailable, state that limit explicitly.

### 2. Stage 2 Runs Project Question Governance

Use the Stage 2 discipline from `three-step-analysis`: govern the Stage 1
question ledger before asking. Project analysis does not default to asking a
question, but it must account for material project unknowns.

Ask a blocking project question only when the Stage 1 model identifies a
user-private reversal variable that would change the project decision,
implementation boundary, verification standard, risk acceptance, or downstream
skill. If `request_user_input` is available, use it with 1-3 questions and
recommended options. If it is unavailable, ask concise text questions and stop
before the decision.

If the remaining uncertainty can be resolved by repo inspection, docs, commands,
tests, external sources, or engineering judgment, do that instead of asking. If
no user-private reversal variable remains, state `无阻塞校准` with the default
project decision and a compact question ledger summary, then proceed to Stage 3.

Do not ask preference questions that only change wording, style, minor
implementation taste, or make the user choose between under-argued technical
paths. The question must show the current default decision and the condition
that would reverse it.

### 3. Stage 3 Commits To A Project Decision

Use `three-step-analysis` Stage 3, but the final decision must be project-facing:
- recommended path,
- why it fits this project,
- alternatives rejected and why,
- risks and rollback/escape path,
- exact verification evidence expected,
- downstream skill to execute if implementation is requested.

If the user asked only for analysis, return the analysis Handoff Record to
`project-lifecycle` and stop. If the user asked to solve or implement, return
the downstream recommendation to `project-lifecycle`; do not invoke executors
directly from this skill.

### 4. Stage 4 Is Handoff, Not Local Implementation

Do not edit files inside `project-analysis`. When the user wants implementation,
convert the decision into a Context Packet recommendation for
`project-lifecycle`:
- new project -> `project-bootstrap`,
- existing project change -> `project-iteration`,
- release/deploy -> `project-release`,
- docs/handoff -> `project-docs`,
- multi-phase work -> `project-lifecycle`.

## Final Response

Report:
- decision or diagnosis,
- assumptions that matter,
- alternatives rejected,
- verification plan or command,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- next implementation skill, if any.
