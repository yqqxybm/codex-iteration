---
name: project-refine
description: >
  Downstream project artifact refinement stage selected by project-lifecycle.
  Use for assigned iterative polish of software project docs, README text,
  prompts, UI copy, architecture notes, runbooks, code examples, or
  project-facing written artifacts. Project adapter for the self-refine
  cognitive core. Does not replace implementation, tests, commits, releases, or
  source-code review.
---

# Project Refine

This is the software-project adapter for the `self-refine` cognitive core.
Preserve the generate, critique, refine loop; add only project reality:
source-of-truth checks, verification, lifecycle ownership, and docs boundaries.

## Lifecycle Position

Use this skill when `project-lifecycle` assigns a software-project artifact that
needs generate, critique, and refine loops: README sections, project prompts,
architecture notes, runbooks, UI copy, API examples, handoff notes, or code
examples in docs.

Do not use it for source-code changes. If refinement requires changing
executable code, tests, build config, API behavior, or UI behavior, hand off to
`project-iteration`. If it is a non-project writing or prompt task, use
`self-refine`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet and focus only
on `owned_scope`. Preserve accepted decisions, `do_not_do`, and
`standard_compliance_ledger` when present. When provided, also preserve
`project_goal`, `goal_runtime`, `goal_synthesis` / `control_system_goal`,
`goal_preflight` / `optimality_law`, `perspective_model`,
`plan_state_sink`, `cyclic_goal_loop`, `loop_control_matrix`,
`review_clean_pass_loop`, `optimize_framework_cycle_loop`,
`subagent_dispatch_policy`, `agent_owner`, `write_policy`, and
`protocol_evidence`. Do not reopen lifecycle questions unless the artifact
contradicts them.

Return a Handoff Record with artifact path or content, critique summary,
refinements made, verification result when applicable,
`standard_compliance_delta` when a ledger is active, open risks, and the next
recommended skill. Include any item status, result, and verification evidence
needed by an active `plan_state_sink` and `domain_resource_evidence` when
`software-contract` was loaded. Durable docs changes go through `project-docs` when the task is
broader than the owned artifact.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Return the refinement result
as a receipt or Handoff Record to `project-lifecycle`.

## Adapter Rules

1. **Spec maps to project truth**: identify audience, purpose, project context,
   source of truth, and success criteria before applying `self-refine`.
2. **Critique adds project checks**: evaluate accuracy, project fit,
   completeness, clarity, maintainability, and whether future Codex sessions can
   use the artifact.
3. **Refine within owned scope**: update only the artifact or text in
   `owned_scope`; preserve accepted project decisions.
4. **Preserve standard evidence**: when `standard_compliance_ledger` is active
   and the owned artifact maps to a Standard Development Contract requirement,
   update only the evidence or status that the refined artifact can prove. Do not
   mark unrelated docs, release, branch, or CI requirements `satisfied`; return
   broader coverage work to `project-docs` or `project-lifecycle`. Load
   `software-contract` and read the relevant standard or docs-deliverables
   reference when the refined artifact changes standard evidence. If the
   required reference is unavailable, stop and report the missing resource.
5. **Verify when checkable**: run the relevant check when possible: markdown
   links, command examples, docs references, rendered UI copy, or testable code
   examples.

Default to internal iteration. Show intermediate versions only when the user
asks to see the process.

## Boundaries

- Do not turn polish into feature work.
- Do not invent project facts to make text smoother.
- Do not change global `~/.codex/AGENTS.md` unless the user explicitly asks for
  a cross-project rule.
- Do not claim verification if examples or commands were not actually checked.

## Final Response

Report:
- artifact refined,
- key improvements,
- verification command or reason verification was unavailable,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- remaining project risk, if any.
