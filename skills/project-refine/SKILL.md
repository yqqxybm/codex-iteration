---
name: project-refine
description: >
  Project artifact refinement skill. Use for iterative polish of software
  project docs, README text, prompts, UI copy, architecture notes, runbooks,
  code examples, or project-facing written artifacts. Project adapter for the
  self-refine cognitive core. Does not replace implementation, tests, commits,
  releases, or source-code review.
---

# Project Refine

This is the software-project adapter for the `self-refine` cognitive core.
Preserve the generate, critique, refine loop; add only project reality:
source-of-truth checks, verification, lifecycle ownership, and docs boundaries.

## Lifecycle Position

Use this skill when the artifact belongs to a software project and needs
generate, critique, and refine loops: README sections, project prompts,
architecture notes, runbooks, UI copy, API examples, handoff notes, or code
examples in docs.

Do not use it for source-code changes. If refinement requires changing
executable code, tests, build config, API behavior, or UI behavior, hand off to
`project-iteration`. If it is a non-project writing or prompt task, use
`self-refine`.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet and focus only
on `owned_scope`. Preserve accepted decisions and do not reopen lifecycle
questions unless the artifact contradicts them.

Return a Handoff Record with artifact path or content, critique summary,
refinements made, verification result when applicable, open risks, and the next
recommended skill. Durable docs changes go through `project-docs` when the task
is broader than the owned artifact.

## Adapter Rules

1. **Spec maps to project truth**: identify audience, purpose, project context,
   source of truth, and success criteria before applying `self-refine`.
2. **Critique adds project checks**: evaluate accuracy, project fit,
   completeness, clarity, maintainability, and whether future Codex sessions can
   use the artifact.
3. **Refine within owned scope**: update only the artifact or text in
   `owned_scope`; preserve accepted project decisions.
4. **Verify when checkable**: run the relevant check when possible: markdown
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
- remaining project risk, if any.
