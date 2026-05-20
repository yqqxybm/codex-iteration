---
name: project-bootstrap
description: >
  New software project bootstrap skill. Use when the user asks to create,
  scaffold, initialize, or build a first version from zero. Produces a runnable
  vertical slice with docs, tests or smoke checks, Git hygiene, and an initial
  focused commit. Do not use for routine changes in an existing mature project.
---

# Project Bootstrap

## Lifecycle Position

This skill creates a new production-grade software project. It owns bootstrap
execution; `project-lifecycle` owns phase classification and call-chain
orchestration.

## Default Standard

Default to production-grade, not throwaway scaffolding:

- runnable vertical slice,
- clear project structure,
- README with run/test/build commands,
- project `AGENTS.md` with local conventions,
- `docs/architecture.md`,
- `docs/runbook.md`,
- `docs/decisions/0001-initial-architecture.md`,
- `.env.example` when configuration exists,
- tests or smoke checks,
- lint/typecheck/build scripts when supported by the stack,
- `.gitignore`,
- focused initial commit when inside or creating a Git repo.

Skip only items that are genuinely irrelevant to the chosen stack, and say why.

## Philosophy Contract

Apply the software-project principles:

- **Intent fidelity**: preserve the product purpose and target user in README and
  architecture docs.
- **Structure first**: choose boundaries, directories, and quality gates before
  adding broad features.
- **Runnable first**: the first delivery must run end to end.
- **Evidence loop**: execute the real run/test/build or smoke command.
- **Knowledge capture**: record setup, architecture, operations, and decisions.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before creating
files. Preserve `intent`, `constraints`, `decisions_so_far`, `verification_required`,
and `do_not_do`.

Return a Handoff Record with project path, generated artifacts, stack decisions,
verification output, commit result, open risks, and the next recommended skill.
When invoked from a plan advancement agenda, bootstrap owns only the runnable
project foundation and first vertical slice. Return remaining product,
iteration, release, or handoff work to `project-lifecycle` as agenda items
instead of treating the whole plan as complete. Write a `.codex/traces/` file
only when the chain is long, cross-phase, or likely to be resumed; promote
durable facts to docs through `project-docs`.

## Workflow

### 1. Bootstrap Preflight

1. Identify target directory. If it already exists and is non-empty, inspect it
   and do not overwrite unrelated files.
2. Determine project type, primary users, runtime, package manager, and deployment
   target from the request and local conventions.
3. Ask only when the product type, platform, or target directory is ambiguous
   enough that a wrong assumption would create the wrong project. Otherwise state
   the assumption and proceed.
4. For major stack or architecture tradeoffs, use `project-analysis` first.

### 2. Project Charter

Create or encode these facts in README/docs:

- purpose,
- target user,
- core workflow,
- non-goals,
- success criteria,
- local run/test/build commands.

### 3. Scaffold

Create the smallest production-grade structure that can run:

- source directory,
- test or smoke-test directory,
- config files,
- docs directory,
- environment example if needed,
- first vertical slice.

For UI projects, use `project-frontend` for visual and interaction decisions.
For OpenAI API projects, use `openai-docs` when current API details matter.

### 4. Quality Gates

Run the actual verification commands available for the stack:

- install or dependency check,
- lint/typecheck when configured,
- tests or smoke checks,
- build when applicable,
- browser render check for frontend apps that need one.

Do not skip verification for speed. If a command is impossible locally, stop and
state the blocker; do not silently replace it with a weaker check.

### 5. Version Management

When the scaffold is valid:

1. initialize Git if the target is not already a repo and the user did not forbid it,
2. stage only bootstrap files,
3. use the `project-commit` skill format,
4. create an initial focused commit.

Never push or deploy unless the user explicitly asks.

## Final Response

Report:

- project path,
- stack and structure chosen,
- generated docs,
- verification command and key result,
- commit hash and message, or why no commit was created.
