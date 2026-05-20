---
name: project-iteration
description: >
  Existing-project code iteration skill. Use when the user asks to modify code,
  tests, APIs, UI behavior, build config, automation, implementation checklist
  items, or "代码修改点". Owns implementation, directly affected docs, focused
  closeout review, verification, and focused commit when the task diff is
  cleanly isolated. Explicit deep/exhaustive review requests after edits must
  use the review skill contract. Do not use for new projects, pure analysis, or
  review-only tasks.
---

# Project Iteration

Codex is the implementation owner for code-change requests inside an existing
project. Finish the change end to end: code, directly affected docs, review,
verification, and version management.

## Lifecycle Position

This skill serves the `iteration` phase of the software project lifecycle.
It follows the project philosophy from `project-lifecycle`:

- preserve the user's requested behavior,
- keep the change scoped,
- keep the project runnable,
- verify with concrete evidence,
- capture only knowledge directly affected by this diff.

Use `project-bootstrap` instead when the task is to create a new project from
zero. Use `project-release` instead when the task is release, rollout, version bump, tag,
or production deployment.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before editing.
Preserve `intent`, `constraints`, `decisions_so_far`, `owned_scope`,
`verification_required`, and `do_not_do`.

Return a Handoff Record with changed files, behavioral decisions, docs updates,
verification output, review result, commit result, open risks, and the next
recommended skill. For plan-driven work, include completed item ids, blocked
item ids, added in-scope items, and out-of-scope items returned to
`project-lifecycle`. Write a `.codex/traces/` file only for long or resumable
chains; promote durable facts to formal docs through `project-docs`.

If the user asks for "deep review", "深度 review", "深度审查", "全面 review",
"全面审查", "exhaustive review", "review the whole product", or equivalent
after implementation, the local closeout gates are not enough. Complete the
implementation and verification, then use the `review` skill's deep or
exhaustive contract with a review target packet. Do not describe the local
closeout gates as deep review.

## Trigger Boundary

Use this skill for requests that require editing code, tests, build config, API behavior, UI behavior, infrastructure-as-code, or project automation in an existing project.

Do not use it when the user only asks to analyze, explain, compare, brainstorm,
or review without changes. Do not use it for blank-slate project creation. If
an analysis task later becomes "改 / 实现 / 修复 / 提交", activate this skill then.

## Operating Rules

- State the assumption, tradeoff, and verifiable success criterion before edits. Keep it short.
- Ask only when ambiguity blocks a correct implementation; otherwise state the assumption and proceed.
- Make the smallest code change that satisfies the request. Do not add adjacent refactors or speculative features.
- Do not create backups for reversible text/code/config edits.
- Do not present mocks, skipped tests, partial docs, or uncommitted "almost done" states as completion. If the exact target is blocked, state the blocker before asking or stopping.
- Protect user work: before editing, run `git status --short` when inside a Git repo and identify pre-existing changes. Never revert or commit unrelated user changes.
- For behavior, API, parsing, security, or shared logic changes, prefer
  test-first or reproduction-first work: create or update the smallest failing
  test/reproduction, verify it fails for the right reason, then implement.
  For config-only, docs-only, generated, UI-exploratory, or locally untestable
  changes, record the reason and use the strongest available smoke evidence
  instead of pretending test-first happened.
- Classify review intent before finalizing. Focused closeout review is the
  default. Explicit deep/exhaustive review language must be honored through the
  `review` skill; explicit diff-only language must stay focused and must not be
  called deep review.

## Required Workflow

### 1. Preflight

1. Locate the project root and read relevant project instructions (`AGENTS.md`, package scripts, test config, local style).
2. Inspect the files and call graph needed for the requested change.
3. If the repo is Git-managed, capture initial `git status --short`.
4. Define success as observable behavior: passing tests, changed UI state, API response, CLI output, or exact file/content condition.

### 1.5 Plan Item Loop

When invoked with a plan, checklist, issue list, or "按计划全部推进" instruction,
own only the implementation items inside this skill's scope. Return architecture,
release, broad docs cleanup, sync, or new-project items to `project-lifecycle`
instead of absorbing them here. Normalize the owned work into items:

```yaml
iteration_items:
  - id: <stable short id>
    source_plan_item: <upstream agenda id, source line, or none>
    change: <specific code/docs/test outcome>
    files_or_area: <owned scope>
    done_when: <observable condition>
    verification: <targeted command or evidence>
    review_gates: <spec compliance, code quality, or both>
    status: <pending | active | done | blocked | skipped>
```

Loop invariant: this iteration is not complete while any owned item is
`pending`, `active`, or unverified.

Loop through items until this iteration scope is complete:

1. Work on one `pending` item at a time.
2. Update directly affected docs and tests for that item before marking it done.
3. Run the item's targeted verification when practical; otherwise record the
   exact reason.
4. If the item exposes new required work inside the user's requested scope, add
   it to `iteration_items`.
5. Preserve the upstream `source_plan_item` when splitting work, and report the
   source item status back to `project-lifecycle`.
6. Continue to the next `pending` item without finalizing the task.

Do not stop after the first passing test, commit, or subtask when other
in-scope items remain. Stop only for a real blocker, unsafe operation, failed
verification that cannot be fixed locally, explicit user limit, or completion
of every item. For long/resumable item lists, update the lifecycle trace before
any forced interruption.

Version management happens after all in-scope items for the current iteration
are complete, unless splitting commits is required to keep changes focused. If
multiple focused commits are created, continue the loop after each commit until
no owned items remain.

### 2. Implement

1. Edit only files required by the request.
2. Match existing style and abstractions.
3. Add or update tests when behavior, contracts, parsing, security, or shared logic changes.
4. For testable behavior changes, run a red/green check when practical: failing
   test or reproduction before the fix, passing targeted verification after the
   fix. If red/green is not practical, state the concrete blocker and use the
   strongest direct verification available.
5. For frontend work, also use the project-frontend skill when applicable and verify in browser when the app can run.

### 3. Documentation Sync

Update docs in the same task when the code change affects anything a future user, teammate, or Codex session needs to know:

- Public API, CLI, environment variable, config, setup, deployment, data model, permissions, routing, or user-visible workflow changed.
- README, project `AGENTS.md`, `docs/`, runbooks, examples, or integration guides mention the old behavior.
- Tests or commands changed in a way future agents need to run.

Do not churn docs for purely internal code movement with no observable behavior or workflow change. If a milestone handoff or full project-doc cleanup is requested, also use `project-docs`.

### 4. Verification

Run the real verification command for the changed surface:

- Prefer the project's targeted test, lint, typecheck, build, or smoke command.
- Do not skip requested verification for speed. If full verification is impossible locally, run the smallest command that directly proves the requested behavior and say exactly what was not run.
- Run `git diff --check` in Git repos before version management.
- Never claim fixed or complete from reasoning alone, stale output, or an
  unverified subtask report. Completion claims require fresh evidence from this
  turn or an explicitly named retained command output.

### 5. Review Gates

Before finalizing, classify the requested review type and run the matching
gates. Keep local gates local by default; use subagents only when the user
explicitly requested or authorized agent delegation for this work.

#### Review Type Classification

If a request contains both deep and exhaustive signals, classify it as
`exhaustive`. Whole-scope wording such as "全面", "完整", "不要只看改动",
"整个产品", or "全项目" overrides generic depth wording.

- **Focused closeout review**: default after implementation, or when the user
  asks to review only the current diff. Scope is the final diff, directly
  affected docs/tests, direct call sites, and changed behavior. This is not a
  deep review.
- **Deep review**: required when the user says "deep review", "深度 review",
  "深度审查", or equivalent depth-without-whole-scope language. After local
  gates pass, read and use the `review` skill with depth `deep`.
- **Exhaustive review**: required when the user says "exhaustive",
  "全面 review", "全面审查", "完整检查", "不要只看改动", "穷尽审查",
  "逐词逐句", "整个产品", "全项目", or otherwise asks for all materially
  relevant surfaces. After local gates pass, read and use the `review` skill
  with depth `exhaustive`.

For explicit deep/exhaustive review after code changes, build this review target
packet for the `review` skill:

```yaml
target: <user goal plus completed implementation>
depth: <deep | exhaustive>
post_implementation: true
changed_diff: <final diff or changed files>
minimum_surfaces:
  - user goal and acceptance criteria
  - final diff and changed files
  - direct call chain and integration points
  - core user workflow affected by the change
  - related config, tests, docs, and runbooks
  - verification commands and gaps
explicit_exclusions: <user-stated exclusions or none>
```

If the requested deep/exhaustive scope is genuinely ambiguous, ask before
claiming completion. Otherwise state the inferred project/product boundary and
proceed.

1. **Spec compliance review**: compare the diff against the user request,
   source plan item, `done_when`, directly affected docs, and forbidden scope.
   Fix under-builds, over-builds, missed docs/tests, and scope drift before the
   quality gate.
2. **Code quality review**: check correctness, regression risk, error handling,
   security, data loss, concurrency, migrations, accessibility, maintainability,
   and test coverage as relevant.

If either gate finds issues, fix them before version management when feasible
and re-run the affected gate. If a risk cannot be resolved locally, stop and
report it instead of hiding it.

When deep or exhaustive review was requested, the final review result must come
from the `review` skill's deep/exhaustive contract, including its inspected
surfaces, not-inspected surfaces, convergence status, verification evidence,
and residual risks.

#### Review Pressure Scenarios

- User says "改完再深度 review 一遍": implement first, run focused local gates,
  then invoke `review` depth `deep` with the post-implementation target packet.
- User says "review 一遍整个产品": if no edits are requested, do not use this
  skill; use `review` directly. If said after edits, invoke `review` depth
  `exhaustive` and include whole-product surfaces.
- User says "只 review 这次 diff": run only focused closeout review over the
  diff and directly affected chain. Do not call it deep review.
- User says "全面审查，不要只看改动": implement first if edits were requested,
  then invoke `review` depth `exhaustive`; include core workflows, configs,
  tests, docs, and verification gaps beyond the diff.

### 6. Version Management

When inside a Git repo:

1. Re-run `git status --short` and inspect `git diff --stat`.
2. Stage only files changed for this task. Never use `git add .` or `git add -A`.
3. If verification passed and the user did not explicitly forbid commits, create one focused commit automatically for the completed task.
4. Use the `project-commit` skill when available; follow Angular commit format.
5. If files touched by this task had pre-existing changes, inspect the final diff carefully. Commit only when every staged hunk is attributable to the current task; otherwise leave the worktree uncommitted and state the blocker.
6. Do not commit if unrelated pre-existing changes overlap with this task, verification failed, secrets are present, generated artifacts are ambiguous, or hooks fail and cannot be fixed cleanly. In that case, leave files uncommitted and state the blocker.
7. Never push unless the user explicitly asks.

When not inside a Git repo, say version management is unavailable because there is no Git repository. Do not create a repository unless the user asks.

## Final Response

Keep the final answer short and include:

- What changed, including docs changes.
- Completed plan item ids and any items returned to `project-lifecycle`, when
  invoked from a plan.
- Verification commands and key results.
- Review type: `focused`, `deep`, or `exhaustive`.
- Inspected surfaces.
- Not inspected surfaces.
- Review result: focused local gates, or the `review` skill's deep/exhaustive
  result when explicitly requested.
- Residual risks.
- Commit hash and message, or the precise reason no commit was created.
