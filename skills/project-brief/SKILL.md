---
name: project-brief
description: >
  Software-project task-brief skill. Use for fuzzy project, feature, or code
  requests that need scope, users, constraints, success criteria, non-goals, and
  deliverable shape before lifecycle execution. Project adapter for the co-star
  cognitive core. Does not implement, commit, deploy, or replace
  project-lifecycle.
---

# Project Brief

This is the software-project adapter for the `co-star` cognitive core. Preserve
CO-STAR's task-structuring discipline; add only project reality: scope,
constraints, verification, lifecycle chain, and non-goals. It does not implement.

## Lifecycle Position

Use this skill when the user describes a software idea, feature, refactor,
automation, or code task too vaguely for a correct lifecycle chain.

Do not use it for everyday writing or prompt shaping; use `co-star`. Do not use
it for deep architecture or debugging decisions; use `project-analysis`. Do not
use it after the implementation target is already clear; go directly to the
relevant project skill.

## Call Chain Contract

When invoked by `project-lifecycle` or used before lifecycle selection, consume
the current request or Context Packet before shaping the brief. Preserve
`intent`, `constraints`, `owned_scope`, `verification_required`, and `do_not_do`
when they are available.

Return a Handoff Record with the resolved brief, selected next skill, material
assumptions, blocking questions if any, success criterion, open risks, and why
the chosen chain fits. Do not implement, commit, deploy, sync, or rewrite the
target.

## Adapter Fields

Translate CO-STAR into project execution terms. Capture only fields that change
the lifecycle chain:

- **C / Project context**: repo, module, platform, runtime, or service boundary.
- **O / Intent and success criterion**: user-visible outcome and observable
  finish condition.
- **S+T / Constraints and conventions**: hard limits, exclusions, existing
  style, security/data rules, and accepted implementation taste.
- **A / Audience/user**: who benefits from or operates it.
- **R / Deliverable shape**: code change, vertical slice, architecture decision,
  release, sync, docs, or retrospective.

Then choose the chain result:

- **Next skill**: `project-lifecycle`, `project-bootstrap`,
  `project-iteration`, `project-analysis`, `project-frontend`,
  `project-refine`, `project-release`, `project-docs`, `project-sync`, or
  `project-retrospective`.

## Execution Rules

- Infer obvious fields from local context and state them briefly.
- Ask only when a missing field would select the wrong lifecycle chain or risk
  data loss.
- When a blocking fork exists and `request_user_input` is available, use it with
  1-3 concise questions and recommended options first. If the tool is unavailable,
  ask concise text questions and stop until answered.
- Do not show a full card unless the user asks for a brief, spec, prompt, or
  handoff format.
- If the brief is enough to proceed, hand off to the next skill immediately.

## Output Shape

When a brief must be shown, use:

```yaml
intent: <user-visible outcome>
project_context: <repo/module/platform>
owned_scope: <files/modules/phase>
constraints: <hard limits and exclusions>
success_criterion: <observable finish condition>
deliverable_shape: <code/docs/release/sync/decision/etc.>
next_skill: <project skill>
```

## Final Response

Report:
- resolved brief,
- assumption that matters,
- next skill or why no project action should start.
