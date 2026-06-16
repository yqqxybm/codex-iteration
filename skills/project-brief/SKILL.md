---
name: project-brief
description: >
  Downstream software-project task-brief stage selected by project-lifecycle
  for fuzzy project, feature, or code requests that need scope, users,
  constraints, success criteria, non-goals, and deliverable shape before the
  lifecycle chain continues. Project adapter for the co-star cognitive core.
  Does not implement, commit, deploy, or replace project-lifecycle.
---

# Project Brief

This is the software-project adapter for the `co-star` cognitive core. Preserve
CO-STAR's task-structuring discipline; add only project reality: scope,
constraints, verification, lifecycle chain, and non-goals. It does not implement.

## Lifecycle Position

Use this skill when `project-lifecycle` determines that a software idea,
feature, refactor, automation, or code task is too vague for a correct lifecycle
chain.

Use it as the default downstream brief stop for root-state changes when the user
has not already supplied a frozen charter: new project creation, project initialization,
PRD, requirements document, MVP boundary, root architecture/design document,
version target, or broad "做一个版本" request. The output must be a charter
packet, not an implementation plan.

Do not use it for everyday writing or prompt shaping; use `co-star`. Do not use
it for deep architecture or debugging decisions; return to `project-lifecycle`
so it can route to `project-analysis`. Do not use it after the implementation
target is already clear; return the resolved boundary to `project-lifecycle`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume the current request or Context
Packet before shaping the brief. Preserve
`intent`, `constraints`, `owned_scope`, `verification_required`,
`standard_compliance_ledger`, and `do_not_do` when they are available. When
provided, also preserve `project_goal`, `goal_runtime`, `goal_synthesis` /
`control_system_goal`, `goal_preflight` / `optimality_law`,
`perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`subagent_dispatch_policy`, `agent_owner`, `write_policy`, and
`protocol_evidence`.

Return a Handoff Record with the resolved brief, selected next skill, material
assumptions, blocking questions if any, success criterion,
`standard_compliance_delta`, `domain_resource_evidence` when `software-contract`
was loaded, open risks, why the chosen chain fits, and any item status needed by
an active `plan_state_sink`. Do not implement, commit, deploy, sync, or rewrite
the target.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Return the brief as a receipt
or Handoff Record to `project-lifecycle`.

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

For root-state changes, normalize the result as:

```yaml
frozen_charter:
  intent: <user-visible product goal>
  target_user: <primary user/operator>
  core_workflow: <main scenario>
  non_goals: <explicit exclusions>
  success_criterion: <observable completion criterion>
  constraints: <hard limits>
  project_shape: <documentation/profile shape if assets are involved>
  doc_profile: <standard docs profile or not_applicable>
  docs_ia: <authorized root docs and docs/ subdirectories, or not_applicable>
```

Do not let a broad idea become an implementation, doc, or scaffold request until
these fields are explicit enough to prevent project-direction drift.
If docs or assets are involved and `doc_profile` / `docs_ia` cannot be resolved
from the brief and software contract, return a profiling agenda item to
`project-lifecycle` before any docs are created.

When the Standard Development Contract is active, update only the brief-level
ledger entries: MVP boundary, target user, core scenarios, non-goals, success
criteria, Metrics/NFR applicability, and which downstream skill owns each
remaining standard item. Do not mark an implementation/doc/release item
`satisfied` from the brief alone.
When standard details affect ownership or status, load `software-contract` and
read `~/.codex/skills/software-contract/references/standard-development-contract.md`.
If the required reference is unavailable, stop and report the missing resource.

Then choose the chain result:

- **Next skill recommendation for `project-lifecycle`**:
  `project-bootstrap`, `project-iteration`, `project-analysis`,
  `project-frontend`, `project-refine`, `project-release`, `project-docs`,
  `project-sync`, or `project-retrospective`.

## Execution Rules

- Infer obvious fields from local context and state them briefly.
- Ask only when a missing field would select the wrong lifecycle chain, change
  root project direction, expand the version boundary, or risk data loss.
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
standard_compliance_delta: <brief-level guide entries satisfied, missing, deferred, blocked, or not_applicable>
```

## Final Response

Report:
- resolved brief,
- assumption that matters,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- next skill or why no project action should start.
