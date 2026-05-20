---
name: project-lifecycle
description: >
  Software project lifecycle controller. Use for new projects, project planning,
  plan advancement such as "根据计划全部推进", architecture or phase transitions,
  and multi-skill project work. Owns the unified philosophy, call-chain
  protocol, agenda loop, and lightweight traces. Do not use for small explicit
  code edits, non-project three-step-analysis requests, or non-project thinking
  tasks.
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

## Phase Map

Classify the request before acting:

| Phase | User intent | Primary skill |
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

- **New project, vague request, phase transition, or multi-skill orchestration**:
  use this skill first.
- **User asks to execute an existing plan end to end**: use this skill first,
  create an agenda, and keep ownership until the agenda reaches a stop condition.
- **Clear code edit in an existing project**: go directly to
  `project-iteration`; it still follows this philosophy.
- **Clear deploy/release request**: go directly to `project-release`.
- **Clear docs handoff request**: go directly to `project-docs`.
- **Project request that asks for "三步分析"**: use `project-analysis` as the adapter around the three-step-analysis core.
- **Non-project request that asks for "三步分析"**: use `three-step-analysis`.
- **Software-project analysis without implementation**: use `project-analysis`.
- **Fuzzy software-project request**: use `project-brief` before choosing the chain.

## Lifecycle Gates

Before building the chain, state:

1. current phase,
2. selected call chain,
3. assumption and tradeoff,
4. verifiable success criterion.

Do not ask for preferences that do not change the call chain. Ask only when a
wrong chain would waste work or risk data loss.

## Call Chain Protocol

Use this protocol when the task crosses lifecycle phases, needs two or more
skills, may run long, or may be interrupted.

### 1. Call Chain Plan

Before downstream work starts, produce a compact plan:

```yaml
phase: <current lifecycle phase>
goal: <user-visible objective>
selected_chain:
  - skill: <skill-name>
    purpose: <why this skill is needed>
success_criterion: <observable finish condition for the whole request>
stop_condition: <when not to continue the chain>
```

Do not include decorative steps. Every selected skill must change the outcome.

### 1.2 Executable Plan Quality

When this controller creates, normalizes, or advances a plan, the plan must be
executable rather than merely descriptive. Each required work item must name:

- the user-visible outcome,
- the owner skill,
- the owned files, modules, artifact, or project area when knowable,
- the exact verification command, artifact, or evidence expected,
- the observable `done_when` condition.

Reject placeholder planning. Items such as `TBD`, `TODO`, "handle edge cases",
"write tests", "similar to previous", or vague "improve/refactor" work are not
ready for execution unless they are expanded into concrete scope and evidence.
If missing detail changes the work, ask or block. If it can be inferred safely
from local context, state the assumption and encode it in the agenda.

### 1.5 Plan Advancement Loop

When the user asks to "按计划推进", "根据计划全部推进", "继续推进到完成",
or otherwise execute an existing plan, enter plan advancement mode.

#### Plan Source Discovery

For "按计划推进", "根据计划全部推进", "继续推进到完成", "按已有重构方案",
or equivalent requests, do not invent, shrink, or substitute the plan.

Before normalizing the agenda, search for plan sources in order:

1. explicit plan in the current user message,
2. active project trace agenda under `.codex/traces/`,
3. project docs, TODO/checklist files, issue files, roadmap files, refactor
   plans, migration plans, architecture notes, and Handoff Records named by the
   user,
4. visible conversation context.

When the user mentions a plan, refactor, migration, roadmap, checklist, or
phase, use targeted search terms such as `重构`, `refactor`, `plan`, `roadmap`,
`todo`, `checklist`, `migration`, `phase`, `handoff`, and `agenda`.

Maintain an internal source ledger:

```yaml
plan_sources:
  - source: <path, trace, document, issue, or conversation>
    evidence: <matched title, checklist, section, or agenda>
    selected: <yes | no>
    reason: <why this is or is not the controlling plan>
```

If no credible plan source is found, stop and ask for the plan location. Do not
proceed with a guessed or reduced agenda. If multiple plausible plans would
produce different work, ask which one controls.

If resuming from a trace, reconcile the agenda against current repo state before
continuing.

The controller owns the agenda. Downstream skills own only their assigned item.
First normalize the plan into a living agenda:

```yaml
agenda:
  - id: <stable short id>
    objective: <user-visible outcome>
    owner_skill: <project skill>
    prerequisites: <ids or none>
    source_plan_item: <source id, line, section, or none>
    owned_scope: <files, modules, artifact, or project area>
    done_when: <observable completion criterion>
    verification: <command, artifact, or evidence>
    status: <pending | active | done | blocked | skipped>
    result: <artifact, commit, decision, or none>
```

Loop invariant: the plan is not complete while any required item is `pending`,
`active`, or unverified.
Before invoking downstream skills, run the Executable Plan Quality gate over the
agenda. Do not start a vague item and hope the downstream skill discovers the
missing scope.

Loop until the agenda reaches a real stop condition:

1. Select the highest-priority `pending` item whose prerequisites are met.
2. Build a Context Packet for that item and invoke the owning skill.
3. Record the Handoff Record and update the agenda.
4. Mark the item `done` only when its `done_when` and verification evidence are
   satisfied and the source plan requirement is preserved.
5. If the handoff creates new required work, add it to the agenda instead of
   leaving it implicit.
6. If a handoff recommends another skill, convert that recommendation into an
   agenda item or explicitly reject it as outside scope.
7. Continue to the next eligible `pending` item without returning a final answer.

Do not stop merely because one downstream skill, commit, or verification step
finished. Stop only when:

- all agenda items are `done` or explicitly `skipped` with a user-approved
  reason,
- a blocker requires user input, secret access, destructive approval, or an
  unsafe operation,
- verification fails after reasonable local fixes and further work would hide
  the failure,
- the environment forces interruption; in that case write or update the trace,
  name the next agenda item, and do not claim the plan is complete.

For plan advancement with more than two items, create or update a trace from the
start before the first item begins, then update it after each item. The trace
must include the source ledger, agenda table, last completed item, current
blocker if any, and next item. It is a recoverability ledger and completion
proof, not a backup.

An agenda item can be `done` only when:

- its source plan requirement is satisfied,
- its `done_when` condition is met,
- its verification evidence is recorded,
- any newly discovered in-scope required work has been added or completed.

If verification cannot run, mark the item `blocked` unless the user explicitly
accepts an unverified completion status.

### 2. Context Packet

Before using a downstream skill, carry forward only the context it needs:

```yaml
intent: <user goal>
constraints: <hard limits and preferences>
decisions_so_far: <accepted decisions>
owned_scope: <files, modules, project area, or phase responsibility>
verification_required: <actual command or evidence expected>
do_not_do: <explicit exclusions, quality-reduction bans, or boundaries>
```

### 3. Handoff Record

After each downstream skill finishes, record a short handoff:

```yaml
skill: <skill-name>
status: <done | blocked | skipped>
changed_artifacts: <files, commands, docs, commits, or none>
decisions: <new decisions made>
verification: <command and key result>
open_risks: <remaining blockers or risks>
next_recommended_skill: <next skill or none>
agenda_update: <done, blocked, added, or remaining items>
```

If the handoff changes the original plan, update the call chain before
continuing.

## Trace Placement

Use the lightest trace that preserves recoverability:

1. **Short chain**: keep the trace in the conversation and final response only.
2. **Long, cross-phase, or resumable chain**: create a project-local trace at
   `.codex/traces/<YYYY-MM-DD>-<task-slug>.md`.
3. **Durable project knowledge**: promote only long-lived facts into
   `README.md`, project `AGENTS.md`, or `docs/` through `project-docs`.

Trace files are operational working records, not backups and not formal docs.
Do not commit `.codex/traces/` by default. Commit them only if the user asks for
trace history to be part of the repository. If `.codex/traces/` reveals a durable
decision, command, environment variable, API, deployment detail, or lesson,
promote that fact to formal docs and keep the trace minimal.

## Final Response

A project-lifecycle task is complete only when the selected downstream skills
have finished their own verification gates and, in plan advancement mode, every
required agenda item is `done` or explicitly user-approved as `skipped`.

The final response names:

- phase handled,
- call chain used,
- agenda completion status, if plan advancement mode was used,
- concrete artifact or decision produced,
- verification evidence,
- trace location, if a trace file was created,
- remaining lifecycle gap, if any.
