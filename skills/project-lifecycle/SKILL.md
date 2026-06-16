---
name: project-lifecycle
description: >
  Software project lifecycle controller and the single entry point for
  software-project requests, including new projects, small code edits, bug
  fixes, project planning, plan advancement such as "根据计划全部推进",
  architecture, docs, release, sync, phase transitions, and multi-skill project
  work, explicit `目标!` / `目标！` goal-backed project objectives, plus Codex
  skill/config/custom-agent self-iteration that governs future project behavior.
  Owns skill selection, philosophy, call chains, analysis gates, goal-backed
  concierge mode, subagents, agendas, contracts, and traces. Do not use for
  non-project three-step-analysis requests or non-project thinking tasks.
---

# Project Lifecycle

This is the software-project controller, not a simple dispatcher. It does not
implement features itself. It identifies the project phase, applies the project
philosophy, builds the call chain, and hands each downstream skill the smallest
useful context packet.

## Unified Philosophy

Codex's software-project job is to turn user intent into software assets that
are runnable, verifiable, releasable, maintainable, handoff-ready, and able to
evolve.

Every software-project skill must serve five principles:

1. **Intent fidelity**: preserve the user's actual goal across every layer.
2. **Structure first**: establish boundaries, architecture, quality gates, and
   project context before large implementation.
3. **Runnable first**: prefer a working vertical slice over empty scaffolding or
   abstract plans.
4. **Evidence loop**: verify code, releases, and decisions with concrete output.
5. **Knowledge capture**: record decisions, run commands, operations, and lessons
   where future Codex sessions and humans can find them.

## Control System Model

Project lifecycle applies cybernetic pragmatism to software work: user intent is
the objective, repo/runtime evidence is feedback, skill boundaries are action
constraints, and verified project state change is completion.

In this controller:

- the agenda is the current world-state model,
- the Context Packet is bounded state transfer to a downstream skill,
- the Handoff Record is control transfer back to the controller,
- verification is feedback from the changed world,
- the trace is cross-session memory for recoverability,
- the stop condition is the boundary against infinite work, silent downgrade, or
  false completion.

Do not add process unless it improves one of these control functions.

## Project Standard Contract

All software projects are governed by the Standard Development Contract derived
from the user's `标准开发指南`. Full standard enforcement means every guide
requirement must be accounted for; it does not mean every project receives long
same-name documents or enterprise ceremony up front.

In the control model, the standard ledger is the observable project-state for
development maturity: a requirement without evidence is unknown, a missing owner
is uncontrolled, and a claimed completion without verification is false
completion.

Use the `software-contract` resource skill when creating a new project,
advancing a project phase, auditing project readiness, or when the user mentions
the standard guide. Required reference:
`~/.codex/skills/software-contract/references/standard-development-contract.md`.
If it cannot be read, stop and report the missing resource; do not replace it
with memory or a generic checklist.

Maintain a compact `standard_compliance_ledger`:

```yaml
standard_compliance_ledger:
  source: 标准开发指南
  entries:
    - requirement: <guide phase/item>
      owner_skill: <project skill>
      status: <satisfied | not_applicable | blocked | deferred | missing>
      evidence: <file, command, setting, test, or reason>
      next_action: <agenda item, none, or user decision needed>
```

Rules:
- Record `domain_resource_evidence` when the standard contract affects a
  completion claim.
- Full mandatory means every item has a status and evidence boundary.
- Equivalent project paths are allowed, but the mapping must be recorded.
- Optional guide items must still be evaluated; if their condition applies, they
  become required. If not, mark `not_applicable` with a reason.
- Short skeleton docs are acceptable at bootstrap when they give a real entry,
  owner, and verification path. Empty placeholder docs are not `satisfied`.
- Missing standard work becomes agenda, `blocked`, or `deferred`; it is never
  silently ignored.

## Phase Map

Classify the request before acting:

| Phase | User intent | Downstream capability |
| --- | --- | --- |
| `idea` | vague app/product idea, "想做一个..." | `project-brief`, then this controller |
| `charter` | define goals, users, constraints, success criteria | `project-brief` + `project-lifecycle` |
| `architecture` | stack, data model, service boundaries, risk tradeoffs | `project-analysis` |
| `bootstrap` | create a new project from zero | `project-bootstrap` |
| `iteration` | feature, fix, refactor, tests, behavior change | `project-iteration` |
| `ui` | UI/UX, page, component, visual behavior | `project-frontend` + `project-iteration` or `project-bootstrap` |
| `release` | version, tag, build, deploy, rollout, rollback | `project-release` |
| `sync` | machines, skills, config distribution, SSH fleet work | `project-sync` |
| `handoff` | docs, README, AGENTS, newcomer readiness | `project-docs` |
| `learn` | lessons, incident review, repeated mistakes | `project-retrospective` |
| `polish` | refine a high-value project artifact through iterations | `project-refine` |

## Entry Policy

- **All software-project requests enter here first**: new projects, existing
  project code edits, bug fixes, tests, UI, docs, release, sync, architecture,
  planning, review-after-implementation, and plan advancement.
- This controller chooses the downstream capability. Do not let user wording
  such as "修一下", "改个 bug", "写文档", or "发布" bypass the controller.
- **User asks to execute an existing plan end to end**: create an agenda and
  keep ownership until the agenda reaches a stop condition.
- **Any project request creates a multi-item agenda or independent work
  surfaces**: evaluate automatic parallel dispatch through
  `references/goal-subagent-orchestration.md`. If the work is safe, disjoint,
  executable, materially worth dispatching, and the runtime exposes subagent
  tools, choose the smallest correct `parallel_execution_mode` and parallelize
  automatically; do not wait for the user to say "并行". Do not merely count
  available agents. Build the task graph, dependency edges, conflict edges,
  runtime capability probe, parallel ROI, merge strategy, join barrier, and
  selected antichain first. Preserve exact fields:
  `runtime_capability_probe`, `parallel_roi`, `merge_strategy`,
  `subagent_spawn_mechanism`, `join_barrier`, `same_worktree_disjoint`,
  `isolated_worktree_if_supported`, and `main_applies_patch`.
- **User asks to finish, close out, deliver, complete a version/phase, keep going
  until done, or optimize project/goal/subagent/Codex controls**: use
  goal-backed concierge unless explicitly single-point.
- **User starts a project request with `目标!` or `目标！`**: treat the rest of
  the message as an explicit goal-backed project objective. The user supplies
  only the desired outcome; this controller must synthesize the control-system goal:
  goal preflight, task-specific optimality law, target layer, state model,
  feedback sensors, actuator skill chain, loop policy, stop condition,
  verification, commit/push/deploy applicability, review depth/scope,
  clean-pass count, escalation boundary, perspective model, plan state sink,
  automatic parallel dispatch policy, runtime capability probe, parallel
  execution mode, task graph, parallel ROI, merge strategy, join barrier, and
  agenda. Read
  `references/goal-subagent-orchestration.md` before creating or maintaining a
  Codex goal. Create or maintain a Codex goal only after the goal prompt passes
  the elegance gate. Then show `goal_runtime`, synthesized `goal_synthesis`/
  `goal_preflight`/`perspective_model`/`plan_state_sink`/
  `subagent_dispatch_policy`/`parallel_execution_mode`/`cyclic_goal_loop`,
  `protocol_evidence`, and the initial agenda.
- **Project request that asks for "三步分析"**: route to `project-analysis` as
  the adapter around the three-step-analysis core, then return control here for
  any requested execution.
- **Non-project request that asks for "三步分析"**: use `three-step-analysis`.
- **Software-project analysis without implementation**: route to
  `project-analysis` and stop after the analysis Handoff Record.
- **Fuzzy software-project request**: route to `project-brief` before choosing
  the chain.
## Lifecycle Gates

Before building the chain, state:

1. current phase,
2. selected call chain,
3. assumption and tradeoff,
4. verifiable success criterion.

Do not ask for preferences that do not change the call chain. Ask only when a
wrong chain would waste work or risk data loss.

### Mandatory Project Analysis Gate

Before handing project work to an executor, include `project-analysis` in the
chain by default. The default assumption is that a local request may be a symptom
of a broader project issue unless the user explicitly says full-project/systemic
analysis is unnecessary.

Only bypass full `project-analysis` when the user clearly says to keep the work
local, diff-only, no broader analysis, no systemic analysis, or equivalent. In
that case record `analysis_gate: explicitly_skipped_by_user` and preserve the
user's narrow boundary. Do not infer this skip from the change looking small.

`project-analysis` is especially mandatory when any of these are true:
- root direction, PRD, requirements, architecture, tech stack, MVP, version
  boundary, or acceptance criteria may change,
- a bug, UI flaw, failed test, performance issue, or user-visible defect may be
  a symptom of a broader pattern instead of a single local line,
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

### Root-State Changes

Treat these requests as root-state changes: new project creation, project
initialization, scaffolding from a product idea, PRD, requirements document,
MVP boundary, root architecture/design document, tech-stack decision, and
version target such as `v0.x`.

Before handing root-state work to `project-bootstrap`, `project-docs`, or
`project-iteration`, produce or consume a frozen charter:

```yaml
frozen_charter:
  intent: <user-visible product goal>
  target_user: <primary user/operator>
  core_workflow: <main scenario>
  non_goals: <explicit exclusions>
  success_criterion: <observable completion criterion>
  constraints: <hard limits>
  project_shape: <profile from docs-deliverables when docs/assets are involved>
  docs_ia: <authorized root docs and docs/ subdirectories when standalone docs are involved>
```

Use `project-brief` for fuzzy scope and `project-analysis` for root decisions
or architecture tradeoffs. Use question governance for missing charter fields:
ask only when a user-private variable would alter project direction; otherwise
resolve, verify, assume, or carry each key question as risk before proceeding
through the authorized chain. Do not let an executor infer a root direction from
one broad sentence and write durable project files.

### Version-State Changes

Treat these requests as version-state changes: "做一个版本", "实现一个版本",
"MVP", "v0.x", "milestone", "sprint", "完成当前阶段", and equivalent
phase-completion language.

Version-state work must enter the agenda loop. If the user supplies no existing
plan, create a version agenda from the frozen charter and current request; do
not downgrade it to a single local iteration. Each item must record source,
status, result, and verification evidence.

While a version agenda is active, any new user requirement that changes scope is
a `change_request`, not a side note:

```yaml
change_request:
  source: <user message or evidence>
  requested_change: <what changed>
  impact: <agenda item, root direction, docs/assets, tests, release, or none>
  decision: <add_now | replace_item | defer | reject | ask>
  reason: <why this preserves the user goal and current version boundary>
```

Only `add_now` or `replace_item` changes the active agenda. `defer`, `reject`,
or `ask` must be visible in the trace or final response.

### Goal-Backed Project Concierge

The recommended explicit trigger is `目标!` or `目标！` at the start of a
project request. Natural-language completion wording may still imply concierge
mode, but do not teach or rely on a long keyword list as the primary trigger.
Use concierge mode for explicit `目标!` / `目标！` requests, version closeout,
plan completion, release readiness, project skill system, goal system, subagent
orchestration, or Codex self-iteration control optimization, including Codex skills, global
instructions, config, and custom agents that govern future project behavior.
Default to goal-backed unless the user explicitly narrows the work to a
single-point/local/diff-only edit. For `目标!` / `目标！`, never require the
user to write the loop, review depth, review scope, clean-pass count,
commit/push/deploy requirements, stop condition, target layer, state variables,
sensors, actuator chain, review/optimization perspectives, optimality law, or
elegance gate, plan state sink, automatic parallel dispatch policy, or agenda
split; infer them from the project objective and evidence.
Read `references/goal-subagent-orchestration.md` first, then write the project
goal control prompt yourself from the user's incomplete target. The prompt passed
to the Codex goal tool must embed the selected loop contract when the goal uses
`bounded_goal_loop` or `cyclic_until_clean`; do not rely on sidecar fields,
conversation text, or the agenda to remember the loop. Do not create or maintain
a Codex goal, maintain `cyclic_goal_loop`, spawn subagents, or join subagent
receipts before that reference has been read and applied. Do not activate a goal
prompt that has not first passed its `goal_preflight`, loop-contract, and
elegance gates.

## Call Chain Protocol

This controller keeps the decision rules here and moves mechanical protocol
details to references. Read `references/controller-protocol.md` before any work
that crosses lifecycle phases, advances a plan/version, needs Context Packets or
Handoff Records, creates a trace, or prepares the final project-lifecycle
response.

Referenced protocols are binding, not advisory. When this file requires a
reference, the controller must read it before the governed action, apply its
required schemas, gates, and stop conditions, and record `protocol_evidence`.
Do not claim progress or completion from a governed action when the required
reference was not read or its evidence fields were not carried forward.

The controller itself remains responsible for:

- selecting the phase and downstream skill chain,
- enforcing analysis, state-boundary, goal, and standard gates,
- preserving the user's boundary and explicit exclusions,
- owning the agenda and goal state,
- accepting or rejecting downstream `new_work`,
- deciding whether the stop condition is actually satisfied.

Use `references/goal-subagent-orchestration.md` in addition to
`references/controller-protocol.md` whenever goal-backed concierge,
`cyclic_goal_loop`, subagents, automatic parallel dispatch,
`parallel_execution_mode`, task graphs, or a multi-item agenda with independent
work surfaces is active.
