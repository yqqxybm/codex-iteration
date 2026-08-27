---
name: project-iteration
description: >
  Downstream existing-project implementation stage selected by
  project-lifecycle after the lifecycle controller has established the required
  upstream product boundary, classified the request, and consumed
  project-analysis, recorded an explicit analysis waiver, or proved
  project-analysis unnecessary for a very_small change. Use for assigned code
  changes, bug fixes, regressions, tests, APIs, UI behavior, build config, automation,
  implementation checklist items, or "代码修改点" inside an existing project.
  Owns implementation, directly affected docs, focused closeout review,
  verification, and focused commit. Explicit deep/exhaustive review requests
  after edits must use the review skill contract. Do not use as the project
  entry point, for new projects, pure analysis, or review-only tasks.
---

# Project Iteration

Codex is the implementation owner for code-change requests inside an existing
project. Finish the change end to end: code, directly affected docs, review,
verification, and version management.

## Lifecycle Position

This skill serves the `iteration` phase of the software project lifecycle.
It is not the project entry point. `project-lifecycle` is the single entry point
for software-project requests and invokes this skill only after selecting an
existing-project implementation boundary.

It follows the project philosophy from `project-lifecycle`:

- preserve the user's requested behavior,
- keep the change scoped,
- keep the project runnable,
- use verification in proportion to the risk,
- capture only knowledge directly affected by this diff.

Use `project-bootstrap` instead when the task is to create a new project from
zero. Use `project-release` instead when the task is release, rollout, version bump, tag,
or production deployment.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before editing.
Preserve the accepted intent and analysis boundary, owned mutation scope,
explicit exclusions, active goal/plan state, and only the quality, UI, standard,
verification, or subagent information relevant to this implementation. Do not
instantiate or echo absent packet fields.

Return a Handoff Record with changed files, behavioral decisions, docs updates,
verification output, review result, `standard_compliance_delta` when its ledger
is active, relevant `software-contract` guidance when it shaped the change,
commit result, open risks, and the next recommended skill. For plan-driven work, include
completed item ids, blocked item ids, added in-scope items, and out-of-scope items returned to
`project-lifecycle`, plus `plan_state_sink_delta` when the lifecycle agenda is
active. Write a `.codex/traces/` file only for long or resumable chains; promote
durable facts to formal docs through `project-docs`.

When invoked from a lifecycle agenda, this skill owns only the assigned agenda
item. If user input may alter the version goal, root direction, deliverable set,
docs profile, release boundary, or acceptance criteria, return it to
`project-lifecycle` for State Boundary Enforcement. Return a `change_request`
only after it is classified as a user-confirmed change to an already accepted
boundary; do not silently absorb or drop it.

When the Context Packet contains an agenda, plan, checklist, issue list, or
plan-advancement instruction, read
`references/plan-driven-execution.md`. Do not load that state machinery for an
ordinary single implementation item.

If the user asks for "deep review", "深度 review", "深度审查", "全面 review",
"全面审查", "exhaustive review", "review the whole product", or equivalent
after implementation, the local closeout gates are not enough. Complete the
implementation and verification, then use the `review` skill's deep or
exhaustive contract with a review target packet. Do not describe the local
closeout gates as deep review.

## Trigger Boundary

Use this skill only when `project-lifecycle` assigns an existing-project
implementation item that requires editing code, fixing bugs, resolving
regressions, updating tests, changing build config, API behavior, UI behavior,
infrastructure-as-code, or project automation.

Do not use it when the user only asks to analyze, explain, compare, brainstorm,
or review without changes. Do not use it for blank-slate project creation. If
an analysis task later becomes "改 / 实现 / 修复 / 提交", return to
`project-lifecycle` so it can select this skill with a Context Packet.

## Operating Rules

- State the assumption, tradeoff, and verifiable success criterion before edits. Keep it short.
- When `skill_system_best_practice_packet` is present, use it as the
  skill-system practice layer: follow its owner-skill chain, contract/resource
  requirements, docs/test/update defaults, verification scope, and review/commit
  boundary. Do not ask the user to rewrite the implementation prompt or name
  routine skills.
- Do not silently serialize work that has safe parallel read or disjoint write
  surfaces. Daily implementation work inherits project-lifecycle's
  parallel-by-default policy, not only explicit `目标!` work. This skill does not
  own dispatch. If it discovers independent implementation, docs, tests, UI,
  config, verification, or review surfaces not already represented by its
  bounded `subagent_execution` assignment, return the candidate nodes,
  dependencies, conflict keys, and verification to `project-lifecycle` for graph
  and dispatch decisions. Preserve a lifecycle-provided `parallel_blocker`; do
  not invent one or absorb unassigned work sequentially.
- Ask only when ambiguity blocks a correct implementation; otherwise state the assumption and proceed.
- Make the smallest code change that satisfies the request. Do not add adjacent refactors or speculative features.
- Explicit user boundaries control implementation scope. Do not let current
  docs, tests, implementation, productization inference, or compliance inference
  expand into a scope the user forbade.
- Before adding new logic or abstractions, run the minimal-correct implementation
  ladder: delete/avoid the feature if the requested outcome does not need it;
  reuse existing project code; use the platform or framework native capability;
  use the standard library; use an already-installed dependency; then write the
  minimum new code. This ladder prevents over-build, but it must not remove
  requested behavior, security, validation, accessibility, data-loss handling,
  authoritatively affected durable-contract docs/tests, or required verification.
- Do not create backups for reversible text/code/config edits.
- Do not present mocks, skipped tests, partial docs, or uncommitted "almost done" states as completion. If the exact target is blocked, state the blocker before asking or stopping.
- Passing tests are not correctness proof when they protect behavior opposite to
  the user's explicit requirement. Correct them only under the durable-contract
  rule below; a current assertion cannot prove its own authority. Mutate tests,
  fixtures, scripts, or CI assertions only inside the authorized boundary;
  otherwise return them as suspect excluded-scope work.
- Persistent tests protect durable, authoritative behavior or content contracts,
  not a mutable implementation literal or the historical fact that one value was
  replaced by another. Match verification to requirement lifetime: verify a
  one-time transition with a targeted diff, search, parse, or render; add a test
  only when an explicit product source, external interface, accessibility,
  legal/compliance, localization, selector, security, or behavioral contract must
  keep enforcing it. Without such an authoritative durable contract, do not add
  a test whose sole value is asserting the current literal or prohibiting the
  replaced literal. If such an incidental assertion already exists, remove or
  relax its literal coupling instead of mechanically updating it to the new text.
- Protect user work: before editing, run `git status --short` when inside a Git repo and identify pre-existing changes. Never revert or commit unrelated user changes.
- For behavior, API, parsing, security, or shared logic changes, prefer
  test-first or reproduction-first work: create or update the smallest failing
  test/reproduction, verify it fails for the right reason, then implement.
  For config-only, docs-only, generated, UI-exploratory, or locally untestable
  changes, record the reason and use the strongest available smoke verification
  instead of pretending test-first happened.
- Classify review intent before finalizing. Focused closeout review is the
  default. Explicit deep/exhaustive review language must be honored through the
  `review` skill; explicit diff-only language must stay focused and must not be
  called deep review.
- When invoked as a subagent, preserve the assigned `assignment_id`,
  `execution_owner_id`, `agent_owner`, and `write_policy`; do not edit the parent goal,
  do not spawn subagents, and do not commit, push, deploy, sync remote state, or
  broaden scope or claim project completion. Return the exact assignment-required
  `subagent_receipt`; a Handoff Record may accompany but never replace it.

## Required Workflow

### 0. Project Analysis Gate

Before editing, run or consume full `project-analysis` by default. Treat every
requested change as a possible local expression of a broader project issue until
the analysis proves the implementation boundary.

Skip full `project-analysis` only when `project-lifecycle` records the user's
explicit analysis waiver or proves every `very_small` condition. A narrower
mutation boundary still scopes a material analysis; it does not waive one. Do
not infer the skip from appearance alone. Record the governing disposition:

```yaml
analysis_gate: <project_analysis_consumed | explicitly_skipped_by_user | not_required_very_small>
analysis_gate_basis: <Stage 3 decision and implementation boundary, exact analysis-waiver wording, or concise proof of every very_small condition>
```

Require non-empty `analysis_gate_basis` that matches the recorded disposition.
If it is missing or mismatched, return a required `project-analysis` agenda item
to `project-lifecycle` before implementation instead of trusting the enum alone.

For material user-facing product work, that basis must also rest on a
controller-accepted product commitment. If it instead exposes unresolved user
reality or a missing requirement/success boundary, return to `project-lifecycle`
for the earliest unresolved phase. Do not treat "开始改" or implementation-shaped
artifacts as product authorization. This does not add an upstream gate to a
controller-proved `very_small` change.

Proceed locally only after `project_analysis_consumed` records the implementation
boundary, after `explicitly_skipped_by_user` records an actual analysis waiver,
or after the controller proves `not_required_very_small`. Still carry the gate
decision into the final review surfaces.

### 1. Preflight

1. Locate the project root and read relevant project instructions (`AGENTS.md`, package scripts, test config, local style).
2. Inspect the files and call graph needed for the requested change.
3. If the repo is Git-managed, capture initial `git status --short`.
4. Define success as observable behavior: passing tests, changed UI state, API response, CLI output, or exact file/content condition.

For boundary-sensitive work, identify allowed edits, forbidden edits, and any
suspect docs/tests/fixtures/scripts/CI/implementation before editing. If the
boundary still has two materially different meanings, return a blocking question
to `project-lifecycle`.

### 2. Implement

1. Edit only files required by the request.
2. Match existing style and abstractions.
3. Add or update tests when durable behavior/content contracts, parsing,
   security, or shared logic change. Also update, within the authorized mutation
   boundary, tests, fixtures, scripts, or CI assertions that still enforce a
   durable old behavior contrary to the user requirement or another authoritative
   source. Do not infer durability from the current implementation or test itself.
4. For testable behavior changes, run a red/green check when practical: failing
   test or reproduction before the fix, passing targeted verification after the
   fix. If red/green is not practical, state the concrete blocker and use the
   strongest direct verification available.
5. For visible UI work, use `project-frontend` and read
   `references/frontend-implementation.md`. A proved `very_small`
  presentation-only copy replacement remains on the light path defined there.

### 2.5 Standard Coding Gate

For a `material_change`, an active `standard_compliance_ledger`, or a
standard-sensitive `very_small` change, read
`references/standard-coding-gate.md`. Ordinary light-path changes do not load
that contract machinery merely because they edit code.

### 3. Documentation Sync

Update docs in the same task when the code change affects anything a future user, teammate, or Codex session needs to know:

- Public API, CLI, environment variable, config, setup, deployment, data model, permissions, routing, or user-visible workflow changed.
- README, project `AGENTS.md`, `docs/`, runbooks, examples, or integration guides mention the old behavior.
- Tests or commands changed in a way future agents need to run.
- A Standard Development Contract ledger entry changes status or its supporting basis.

Do not churn docs for purely internal code movement with no observable behavior or workflow change. If a milestone handoff or full project-doc cleanup is requested, also use `project-docs`.

When a code change appears to require creating new documentation, apply the
`software-contract` document profile through `project-docs` or return the need
to `project-lifecycle`. Local iteration may update directly affected existing
docs, but it must not create a new documentation set from a standard checklist
or template.

### 4. Verification

Run the real verification command for the changed surface:

- Classify `verification_scope` before running commands:
  - `docs-only` / text-only: inspect the final doc diff, run `git diff --check`,
    validate touched references/links/paths/commands when practical, run
    configured markdown/docs lint or docs build only when relevant, and inspect
    durable temporal claims only when this edit touched them. Do not run `make verify`, full app tests,
    full builds, or browser checks merely because the project has them.
  - code/API/shared behavior: run the smallest targeted test/lint/typecheck or
    reproduction that proves the behavior, plus `git diff --check`.
  - presentation-only copy: inspect the final diff and use a targeted one-time
    search when it materially proves the replacement. Run template parsing/lint
    or one focused render only when syntax, text length, layout, accessibility,
    localization, or content-contract risk makes it relevant. Do not create a
    persistent test or broad frontend verification solely to memorialize the edit.
  - UI: apply the subscopes and verification boundary in
    `references/frontend-implementation.md`, plus `git diff --check`.
  - config/build/release/security: run the specific config/build/release or
    security proof required by the changed surface.
- If an upstream Context Packet assigns broad verification such as `make verify`
  to a docs-only item and the user did not explicitly request full project
  verification, treat it as a scope mismatch. Record a
  `verification_scope_adjustment` in the Handoff Record or return it to
  `project-lifecycle`; do not silently run an overbroad command to make the
  closeout look stronger.
- Prefer the project's targeted test, lint, typecheck, build, or smoke command.
- Do not skip requested verification for speed. If full verification is impossible locally, run the smallest command that directly proves the requested behavior and say exactly what was not run.
- Run `git diff --check` in Git repos before version management.
- Never claim fixed or complete from reasoning alone, stale output, or an
  unverified subtask report. Judge completion from the user's purpose, the
  authorized implementation boundary, and the observed behavior. Keep the
  verification that supports the material claims, rather than treating a
  verification record as the goal itself.
- For UI changes, carry the focused verification required by
  `references/frontend-implementation.md`; a presentation-only light-path change
  uses that reference's narrow exception.

### 5. Review Gates

Classify scope and depth independently. Focused closeout is the default and
covers the final diff, changed behavior, direct call path, and directly affected
tests/docs; it must not be called deep review. Explicit deep/exhaustive or
whole-project review must load the corresponding `review` skill references and
follow that owner's convergence contract. Carry the original goal and
boundaries, final diff, affected workflow and integration path, related project
surfaces, verification, applicable UI findings, and known gaps into its target.

1. **Purpose and boundary review**: compare the diff against the user request,
   source plan item, `done_when`, directly affected docs/tests/fixtures/scripts,
   and forbidden scope. Fix under-builds, over-builds, missed applicable
   docs/tests, wrong assertions, and scope drift before the quality gate.
2. **Focused implementation judgment**: inspect the final diff, directly
   affected workflow, and relevant risks for correctness, maintainability, and
   fit with the project. Use targeted checks where they can settle a material
   question; do not manufacture a taxonomy, probe set, or process loop for a
   small change.

Fix local gate findings before version management and rerun the affected gate.
Return unresolved or parallel review work to `project-lifecycle`; subagent
dispatch stays controller-owned. A deep/exhaustive result must come from
`review`, including inspected and uninspected surfaces, convergence,
verification, and residual risks.

### 6. Version Management

When inside a Git repo:

1. Re-run `git status --short` and inspect `git diff --stat`.
2. If this iteration is running as a subagent, do not stage, commit, push, tag,
   or mutate Git history. Return `commit_needed: true` with candidate files,
   verification results, and message scope to `project-lifecycle`.
3. If running in the main thread, stage only files changed for this task. Never
   use `git add .` or `git add -A`.
4. If verification passed and the user did not explicitly forbid commits, create
   one focused commit automatically for the completed task.
5. Use the `project-commit` skill when available; follow Angular commit format.
6. If files touched by this task had pre-existing changes, inspect the final diff carefully. Commit only when every staged hunk is attributable to the current task; otherwise leave the worktree uncommitted and state the blocker.
7. Do not commit if unrelated pre-existing changes overlap with this task, verification failed, secrets are present, generated artifacts are ambiguous, or hooks fail and cannot be fixed cleanly. In that case, leave files uncommitted and state the blocker.
8. Never push unless the user explicitly asks.

When not inside a Git repo, say version management is unavailable because there is no Git repository. Do not create a repository unless the user asks.

## Final Response

Keep the final answer short and include:

- What changed, including docs changes.
- Completed plan item ids and any items returned to `project-lifecycle`, when
  invoked from a plan.
- Verification scope, commands, and key results.
- UI verification summary, when the change required UI verification.
- Standard compliance delta, when a ledger was active.
- Relevant `software-contract` guidance, when it shaped the change.
- Review type: `focused`, `deep`, or `exhaustive`.
- Inspected surfaces.
- Not inspected surfaces.
- Review result: focused local gates, or the `review` skill's deep/exhaustive
  result when explicitly requested.
- Residual risks.
- Commit hash and message, or the precise reason no commit was created.
