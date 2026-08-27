---
name: project-brief
description: >
  Downstream software-project product-commitment and task-brief stage selected by
  project-lifecycle when accepted project reality or adopted discovery must
  become a clear intent, user/workflow, requirement boundary, scope, constraints,
  success criteria, non-goals, and deliverable shape before analysis or
  implementation. Project adapter for the co-star cognitive core. Does not
  research, implement, commit, deploy, or replace project-lifecycle.
---

# Project Brief

This is the software-project adapter for the `co-star` cognitive core. Preserve
CO-STAR's task-structuring discipline; add only project reality: scope,
constraints, verification, lifecycle chain, and non-goals. It does not implement.

## Lifecycle Position

Use this skill when `project-lifecycle` determines that project reality is
accepted but a software idea, feature, refactor, automation, or code task lacks
the product commitment needed for the later chain. Also use it after discovery
when adopted findings create or change product content, requirements, scope, or
success criteria.

After project reality is accepted, use it as the default downstream brief stop
for root-state changes when the user has not already supplied a frozen charter:
new project creation, project initialization, PRD, requirements document, MVP
boundary, root architecture/design document, version target, or broad
"做一个版本" request. The output must be a charter packet, not an implementation
plan.

Do not use it to discover what users actually need. When unresolved actors,
situations, tasks, needed information or capability, or value relations would
decide the product commitment, return to `project-lifecycle` for
`project-discovery`. Do not use it for everyday writing or prompt shaping; use
`co-star`. Do not use it for deep architecture or debugging decisions; return to
`project-lifecycle` so it can route to `project-analysis`. Do not use it after the
implementation target is already clear; return the resolved boundary to
`project-lifecycle`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume the current request or Context
Packet before shaping the brief. Preserve the accepted intent and boundaries,
owned clarification scope, active goal/plan state, and only the standard,
verification, or subagent projection relevant to the charter. Do not
instantiate or echo absent packet fields.

Consume only controller-adopted discovery conclusions as product-commitment or
charter inputs. A raw research report, `discovery_handoff`, existing
UI/API/schema, available data, competitor pattern, or user example remains
context or hypothesis. If unresolved user, market, product, or domain reality
would decide the user/workflow, requirement boundary, scope, or success
criterion, return to `project-lifecycle` with `project-discovery` as the next
recommendation instead of freezing the hypothesis.

Return a Handoff Record with the resolved brief, selected next skill, material
assumptions, blocking questions if any, success criterion,
`standard_compliance_delta` when its ledger is active,
`domain_resource_evidence` when `software-contract` was loaded, open risks, why
the chosen chain fits, and any item status needed by
an active `plan_state_sink`. Do not implement, commit, deploy, sync, or rewrite
the target.

If invoked as a subagent, preserve the assigned `assignment_id`,
`execution_owner_id`, `agent_owner`, and `write_policy`; do not edit the parent
goal, spawn subagents, commit, push, deploy, sync remote state, broaden scope, or
claim project completion. Return the exact assignment-required
`subagent_receipt`; a Handoff Record may accompany but never replace it.

## Project Framing

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

For under-specified product-commitment requests, also normalize the user's short
outcome into the controller-owned `skill_system_best_practice_packet`. The user
does not need to write the best-practice prompt or name the right skill chain.
Infer the strongest safe practice layer from the project context, Standard
Development Contract, UI contracts, review/optimization rules, local
conventions, available skill metadata, and lifecycle phase. Ask and wait only
when the user's perspective is non-substitutable and materially affects the
target product, platform, risk boundary, review/optimization depth, root
direction, or the understanding from which those choices follow.

For root-state changes, normalize the result as:

```yaml
frozen_charter:
  intent: <user-visible product goal>
  target_user: <primary user/operator>
  core_workflow: <main scenario>
  requirement_boundary: <in-scope product content/capability and its acceptance boundary>
  non_goals: <explicit exclusions>
  success_criterion: <observable completion criterion>
  constraints: <hard limits>
  project_shape: <application, repository, or deliverable shape>
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
read `~/.agents/skills/software-contract/references/standard-development-contract.md`.
If the required reference is unavailable, stop and report the missing resource.

Then choose the chain result:

- **Next skill recommendation for `project-lifecycle`**:
  `project-discovery`, `project-bootstrap`, `project-iteration`,
  `project-analysis`,
  `project-frontend`, `project-refine`, `project-release`, `project-docs`,
  `project-sync`, or `project-retrospective`.

## Execution Rules

- Infer fields only from controller-accepted state or directly inspectable
  project facts. Do not turn a broad user concern, example, tentative claim,
  current UI/API/field, or available data into a user, task, information need, or
  product requirement; return to discovery when that relation would decide the
  brief.
- Apply the dialogue threshold above to missing fields: ask and stop only when
  the user's perspective is non-substitutable and materially affects the brief
  or downstream commitment. A wrong lifecycle chain, root direction, version
  boundary, or data-loss risk is a common case, not the whole test.
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
target_user_and_workflow: <accepted actor, situation, and task or not_applicable>
requirement_boundary: <in-scope product content/capability and its acceptance boundary>
non_goals: <explicitly excluded outcomes or not_applicable>
project_context: <repo/module/platform>
owned_scope: <files/modules/phase>
constraints: <hard limits and exclusions>
success_criterion: <observable finish condition>
deliverable_shape: <code/docs/release/sync/decision/etc.>
next_skill: <project skill>
```

Add `skill_system_best_practice_packet` only for a fuzzy request and
`standard_compliance_delta` only when its ledger is active; do not print empty
optional fields.

## Final Response

Report:
- resolved brief,
- assumption that matters,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- next skill or why no project action should start.
