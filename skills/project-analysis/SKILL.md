---
name: project-analysis
description: >
  Software-project analysis adapter for the three-step-analysis cognitive core,
  also the 项目三步分析 / 代码三步分析 entry. Use for architecture, stack choices,
  debugging strategy, codebase risk, performance/security tradeoffs, project
  planning analysis, or complex technical decisions before implementation. Does
  not edit code; hand off to project-iteration or project-bootstrap.
---

# Project Analysis

This is the software-project adapter for the `three-step-analysis` cognitive
core. Preserve the original stages and philosophy; add only project reality:
repo context, verification paths, lifecycle handoff, and implementation
boundaries.

## Lifecycle Position

Use this skill for project or code decisions that need thinking before action:
architecture, debugging direction, stack selection, API design, migration risk,
security tradeoffs, performance strategy, or phase planning.

It does not edit code. Implementation belongs to `project-iteration` or
`project-bootstrap`.

Do not use it for:
- ordinary non-project deep thinking; use `three-step-analysis`,
- fuzzy task wording; use `project-brief`,
- direct implementation in an existing repo; use `project-iteration`,
- new project scaffolding; use `project-bootstrap`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before analysis.
Preserve `intent`, `constraints`, `owned_scope`, `verification_required`, and
`do_not_do`.

Return a Handoff Record with decision, alternatives rejected, assumptions,
verification plan, implementation entry point, open risks, and the next
recommended skill. Use `.codex/traces/` only for long or resumable chains.

## Adapter Rules

### 1. Stage 1 Maps To Project Reality

Use `three-step-analysis` Stage 1, but ground the brainstorm in project facts:
- current repo/module/service boundary,
- user-visible goal,
- existing architecture and local conventions,
- hard constraints, data or security risk, deployment/runtime context,
- commands that would verify the decision.

Do not answer from generic best practice when the repo or project docs can be
inspected. If local context is unavailable, state that limit explicitly.

### 2. Stage 2 Uses A Blocking Calibration Gate

Use the Stage 2 question discipline from `three-step-analysis`. Project
analysis defaults to one blocking calibration gate before the decision: confirm
the project goal, priority, constraint, verification standard, action boundary,
or recommended path that would most change the project decision.

If `request_user_input` is available, use it with 1-3 questions and recommended
options first. If `request_user_input` is unavailable, ask concise text
questions and stop before the decision. Do not continue to implementation
planning on an uncalibrated project fork.

Only two cases may bypass this gate:

- skill-internal invocation by another owner skill, such as review, optimize,
  self-refine, or framework-pass validation,
- fact verification where repo evidence or external sources determine the
  answer without user preference.

Do not ask preference questions that only change wording, style, or minor
implementation taste.

### 3. Stage 3 Commits To A Project Decision

Use `three-step-analysis` Stage 3, but the final decision must be project-facing:
- recommended path,
- why it fits this project,
- alternatives rejected and why,
- risks and rollback/escape path,
- exact verification evidence expected,
- downstream skill to execute if implementation is requested.

If the user asked only for analysis, stop here. If the user asked to solve or
implement, hand off to `project-lifecycle`, `project-bootstrap`, or
`project-iteration` as appropriate.

### 4. Stage 4 Is Handoff, Not Local Implementation

Do not edit files inside `project-analysis`. When the user wants implementation,
convert the decision into a Context Packet and hand off:
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
- next implementation skill, if any.
