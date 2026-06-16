---
name: project-bootstrap
description: >
  Downstream new-project bootstrap stage selected by project-lifecycle. Use
  when the lifecycle controller assigns creation, scaffolding, initialization,
  or first-version work from zero. Produces a runnable vertical slice with docs,
  tests or smoke checks, Git hygiene, and an initial focused commit. Do not use
  as the project entry point or for routine changes in an existing mature
  project.
---

# Project Bootstrap

## Lifecycle Position

This skill creates a new production-grade software project after
`project-lifecycle` assigns the bootstrap phase. It owns bootstrap execution;
`project-lifecycle` owns project entry, phase classification, and call-chain
orchestration.

## Default Standard

Default to production-grade, not throwaway scaffolding, but do not turn a brief
idea into a template bundle. Bootstrap creates the smallest runnable foundation
authorized by the frozen charter:

- runnable vertical slice,
- clear project structure,
- `standard_compliance_ledger` covering the Standard Development Contract,
- project documentation assets required by the current `doc_profile`,
- documentation information architecture under `docs/` when standalone docs are
  required,
- README/run commands or an equivalent project-native entry,
- project `AGENTS.md` only when local conventions, commands, or boundaries must
  persist for future Codex sessions,
- tests or smoke checks,
- lint/typecheck/build scripts when supported by the stack,
- CodeGraph initialized and indexed in the project root,
- `.env.example` when configuration exists,
- `.gitignore`,
- focused initial commit when inside or creating a Git repo.

When applying the standard, load `software-contract` and read
`~/.codex/skills/software-contract/references/standard-development-contract.md`.
Before creating documentation assets, also read
`~/.codex/skills/software-contract/references/docs-deliverables.md` and apply
the project documentation profile.
For UI projects, also read
`~/.codex/skills/software-contract/references/frontend-quality-contract.md`.
If a required reference cannot be read, stop and report the missing resource;
do not scaffold from a generic remembered checklist.

Skip only items that are genuinely irrelevant to the chosen stack, and say why.
For conditional standard assets, initialize ledger entries first. Create files
only when the doc profile or project-native config requires them; otherwise use
existing sections, native config/schema/workflow files, or ledger statuses such
as `not_applicable`, `deferred`, `blocked`, or `missing`.

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
files. Preserve `intent`, `constraints`, `decisions_so_far`,
`verification_required`, `doc_profile`, `docs_ia`, `standard_compliance_ledger`,
and `do_not_do`. When provided, also preserve `project_goal`, `goal_runtime`,
`goal_synthesis` / `control_system_goal`, `goal_preflight` /
`optimality_law`, `perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`loop_control_matrix`, `review_clean_pass_loop`,
`optimize_framework_cycle_loop`, `subagent_dispatch_policy`, `agent_owner`,
`write_policy`, and `protocol_evidence`.

Return a Handoff Record with project path, generated artifacts, stack decisions,
verification output, `standard_compliance_delta`, `domain_resource_evidence`
when `software-contract` was loaded, `codegraph_status`, commit result, open
risks, the next recommended skill, and any item status, result, and verification
evidence needed by an active `plan_state_sink`.
If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Create or change files only
when the assigned `write_policy` permits it; return commit/release/sync needs to
the main `project-lifecycle` thread.
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
2. Consume `analysis_gate` evidence from `project-lifecycle`. If the Context
   Packet lacks `analysis_gate: project-analysis required` results or
   `analysis_gate: explicitly_skipped_by_user`, return
   `requires_project_analysis` to `project-lifecycle`; do not bootstrap from an
   unanalyzed root-state request.
3. Consume the `frozen_charter` from `project-lifecycle` when present. If no
   frozen charter exists and the request is a broad new-project idea, stop and
   return `requires_charter` to `project-lifecycle` instead of scaffolding from
   assumptions.
4. Determine project type, primary users, runtime, package manager, deployment
   target, `doc_profile`, and `docs_ia` from the charter and local conventions.
5. Ask only when the product type, platform, target directory, or charter field
   is ambiguous enough that a wrong assumption would create the wrong project.
   Otherwise state the assumption and proceed.
5. For major stack or architecture tradeoffs, use `project-analysis` first.
6. Treat CodeGraph initialization as required for software project bootstrap
   unless the target is explicitly not a code project.

### 2. Project Charter

Create or encode the frozen charter facts in the smallest project-native
location allowed by the doc profile:

- purpose,
- target user,
- core workflow,
- non-goals,
- success criteria,
- local run/test/build commands.

Also initialize the Standard Development Contract ledger. Account for every
guide area as `satisfied`, `not_applicable`, `blocked`, `deferred`, or
`missing`; do not silently drop optional items. Equivalent file paths or native
config/schema/workflow evidence are fine when recorded in the ledger.

### 3. Scaffold

Create the smallest production-grade structure that can run:

- source directory,
- test or smoke-test directory,
- config files,
- docs directory only when the doc profile requires standalone docs, using the
  `docs-deliverables.md` information architecture rather than a flat pile,
- environment example if needed,
- first vertical slice.

Create short, true assets rather than long generic placeholders. Empty templates
do not satisfy the standard. If a required standard item cannot be created
correctly during bootstrap, record it as `missing`, `blocked`, or `deferred` and
return it to `project-lifecycle` as agenda instead of creating speculative docs.

Documentation placement rules during bootstrap:

- Keep root-level docs limited to repository entry and conventions: `README.md`,
  `AGENTS.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, and native config.
- Put standalone project docs under the canonical `docs/` subdirectories from
  `docs-deliverables.md`: `product/`, `architecture/`, `development/`,
  `operations/`, `integrations/`, or `handoff/`.
- Create only subdirectories that contain real, authorized project-specific
  docs. Do not create empty folders or placeholder files.
- If more than two standalone docs are required at bootstrap, do not place them
  flat under `docs/`; create the relevant subdirectories and add a short
  `docs/README.md` index only when it helps discovery.

For UI projects, use `project-frontend` for visual, interaction, and UI Contract
decisions. The first vertical slice must establish a baseline `ui_contract` for
the core workflow and include representative states when relevant: loading,
empty, error, long/high-density content, permission or disabled action, desktop,
and mobile. Skip a condition only when it is genuinely irrelevant or impossible
locally, and record the reason in the handoff.
For OpenAI API projects, use `openai-docs` when current API details matter.

### 3.5 CodeGraph Initialization

After the project root, `.gitignore`, and initial source structure exist,
initialize CodeGraph in the project root:

```bash
codegraph init -i <project-root>
codegraph status <project-root>
```

If `.codegraph/` already exists, run `codegraph sync <project-root>` or
`codegraph status <project-root>` and record the result instead of
reinitializing.

Rules:

- Do not ask before running CodeGraph during bootstrap; the user's default is
  that new software projects must be indexed.
- Add `.codegraph/` to `.gitignore` unless the project has a documented reason
  to commit CodeGraph state. Treat the index as local machine state by default.
- If the `codegraph` CLI is missing, initialization fails, or status cannot be
  read, mark the CodeGraph item `blocked` in the standard ledger and return it
  to `project-lifecycle`; do not claim bootstrap is fully complete.
- Do not delete an existing `.codegraph/` directory during bootstrap.

### 4. Quality Gates

Run the actual verification commands available for the stack:

- install or dependency check,
- lint/typecheck when configured,
- tests or smoke checks,
- build when applicable,
- browser render check for frontend apps that need one,
- baseline `frontend_evidence_packet` for frontend apps,
- `codegraph status <project-root>` reports an initialized/indexed project,
- standalone docs follow the `doc_profile.docs_ia` placement,
- standard compliance ledger contains no unaccounted guide item.

Do not skip verification for speed. If a command is impossible locally, stop and
state the blocker; do not silently replace it with a weaker check.

### 5. Version Management

When the scaffold is valid:

1. If this bootstrap is running as a subagent, do not initialize, stage, commit,
   push, or tag. Return `commit_needed: true` with candidate files and message
   scope to `project-lifecycle`.
2. If running in the main thread, initialize Git if the target is not already a
   repo and the user did not forbid it.
3. Stage only bootstrap files.
4. Use the `project-commit` skill format.
5. Create an initial focused commit.

Never push or deploy unless the user explicitly asks.

## Final Response

Report:

- project path,
- stack and structure chosen,
- generated docs,
- docs information architecture applied,
- baseline `frontend_evidence_packet`, when the project has UI,
- standard compliance status and remaining gaps,
- CodeGraph initialization/index status,
- `domain_resource_evidence`, when `software-contract` was loaded,
- verification command and key result,
- commit hash and message, or why no commit was created.
