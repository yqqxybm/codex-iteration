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
on its owned scope. Preserve accepted decisions and boundaries, active goal/plan
state, and only the project-quality, standard, verification, or subagent
projection relevant to this artifact. Do not instantiate or echo absent packet
fields, and do not reopen lifecycle questions unless the artifact contradicts
them.

Return an ordinary Handoff Record: the refinements or conclusions that change the
project judgment, plan, or action; unresolved questions; and the verification
boundary. Include the next recommended skill only when the result directs a
subsequent action. Durable docs changes go through `project-docs` when the task
is broader than the owned artifact.

If invoked as a subagent, preserve the assigned `assignment_id`,
`execution_owner_id`, `agent_owner`, and `write_policy`; do not edit the parent
goal, spawn subagents, commit, push, deploy, sync remote state, broaden scope, or
claim project completion. Return the exact assignment-required
`subagent_receipt`; a Handoff Record may accompany but never replace it.

## Project Refinement Rules

1. **Spec maps to project truth**: identify audience, purpose, project context,
   source of truth, and success criteria before applying `self-refine`. Explicit
   user requirements and approved boundaries outrank current prose. Inspected
   implementation or command output may prove observed facts; current prose
   cannot self-prove a conflicting intended direction. When current user
   direction supersedes an owned-scope statement, replace or remove the old
   statement instead of preserving both as accumulated qualifications. If it
   may invalidate an accepted project decision, return it to `project-lifecycle`
   for `project-analysis` and State Boundary Enforcement rather than silently
   rewriting it or assuming it is a `change_request`.
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
6. **Reader reconstruction**: for explanatory project artifacts, check that the
   intended reader can reconstruct the problem or purpose, core conclusion or
   decision, decisive reasons with their evidence anchors, applicable boundary or
   unknown, and next action from the artifact alone. This may be a clearly labeled
   simulated reader check unless the user supplies a real reviewer. It never
   substitutes narrative fluency for factual traceability.

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
- reader outcome: what the intended reader can now correctly understand or do,
  when the artifact is explanatory,
- standard compliance delta, when a ledger was active,
- `domain_resource_evidence`, when `software-contract` was loaded,
- remaining project risk, if any.
