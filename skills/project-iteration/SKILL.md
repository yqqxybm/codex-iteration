---
name: project-iteration
description: >
  Downstream existing-project implementation stage selected by
  project-lifecycle after the lifecycle controller has classified the request
  and run or explicitly skipped project-analysis. Use for assigned code changes,
  bug fixes, regressions, tests, APIs, UI behavior, build config, automation,
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
- verify with concrete evidence,
- capture only knowledge directly affected by this diff.

Use `project-bootstrap` instead when the task is to create a new project from
zero. Use `project-release` instead when the task is release, rollout, version bump, tag,
or production deployment.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before editing.
Preserve `intent`, `constraints`, `decisions_so_far`, `owned_scope`,
`project_goal`, `goal_runtime`, `goal_synthesis` / `control_system_goal`,
`goal_preflight` / `optimality_law`, `perspective_model`,
`plan_state_sink`, `cyclic_goal_loop`, `subagent_dispatch_policy`, `agent_owner`,
`write_policy`, `verification_required`, `verification_scope`,
`standard_compliance_ledger`, `protocol_evidence`, and `do_not_do`.

Return a Handoff Record with changed files, behavioral decisions, docs updates,
verification output, review result, `standard_compliance_delta`,
`domain_resource_evidence` when `software-contract` was loaded, commit result,
open risks, and the next recommended skill. For plan-driven work, include
completed item ids, blocked item ids, added in-scope items, and out-of-scope items returned to
`project-lifecycle`, plus `plan_state_sink_delta` when the lifecycle agenda is
active. Write a `.codex/traces/` file only for long or resumable chains; promote
durable facts to formal docs through `project-docs`.

When invoked from a lifecycle agenda, this skill owns only the assigned agenda
item. If the user adds or changes a requirement that alters the version goal,
root direction, deliverable set, docs profile, release boundary, or acceptance
criteria, return a `change_request` to `project-lifecycle`; do not silently
absorb it into the local iteration and do not drop it.

When invoked inside a `cyclic_goal_loop`, return a machine-usable delta:

```yaml
cyclic_goal_delta:
  material_in_scope_new_work: <agenda items or none>
  clean_pass_reset_required: <true | false, with reason>
  verification_state: <passed | failed | blocked>
  commit_state: <committed | not_applicable | blocked>
  push_state: <not_requested | pushed | blocked | not_applicable>
  deploy_health: <not_applicable | pass | fail | blocked>
  known_residual_issues: <none | list | unknown>
```

Any new required work inside the parent goal boundary must be returned as
`material_in_scope_new_work`; do not hide it as residual risk. If this
iteration changes code, docs, config, release evidence, or acceptance evidence
after a parent clean review pass, set `clean_pass_reset_required: true`.

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
- When invoked inside project concierge mode, preserve the assigned
  `agent_owner` and `write_policy`. If this worker is a subagent, do not edit the parent goal,
  do not spawn subagents, and do not commit, push, deploy, sync remote state, or
  broaden scope or claim project completion. Return a subagent receipt to
  `project-lifecycle`.

## Required Workflow

### 0. Project Analysis Gate

Before editing, run or consume full `project-analysis` by default. Treat every
requested change as a possible local expression of a broader project issue until
the analysis proves the implementation boundary.

Only skip full `project-analysis` when the user explicitly says to keep the work
local, diff-only, no broader analysis, no systemic analysis, or equivalent. Do
not infer this skip from the change looking small. If skipped, record the user's
explicit boundary:

```yaml
analysis_gate:
  user_visible_symptom: <requested behavior, bug, or change>
  mode: <project-analysis | explicitly_skipped_by_user>
  user_boundary: <exact user wording when skipped, or none>
  systemic_hypothesis: <shared component, workflow, data, API, state, config, or standard risk>
  analysis_decision: <implementation boundary from project-analysis, or local-only by explicit user boundary>
  reason: <why this preserves intent and avoids over/under-fixing>
```

Consume the upstream `project-analysis` decision if present. If missing and the
user did not explicitly skip overall analysis, return a required
`project-analysis` agenda item to `project-lifecycle` before implementation
instead of silently proceeding locally.

Proceed locally only after `project-analysis` defines the implementation
boundary, or after the user explicitly narrows the task. Still carry the gate
decision into the final review surfaces.

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
5. If the item exposes version-level or root-state work, return it to
   `project-lifecycle` as a `change_request` instead of adding it locally.
6. Preserve the upstream `source_plan_item` when splitting work, and report the
   source item status back to `project-lifecycle`.
7. Continue to the next `pending` item without finalizing the task.

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
5. For frontend work, also use the `project-frontend` skill when applicable.
   Preserve or derive its `ui_contract`, implement both visual quality and
   product-state robustness, and verify in browser when the app can run.

### 2.5 Standard Coding Gate

When `standard_compliance_ledger` is present, or when the change touches a
standard-sensitive area, load `software-contract` and read
`~/.codex/skills/software-contract/references/coding-quality-contract.md`.
Evaluate the applicable coding requirements from that reference. If the
reference cannot be read, stop and report the missing resource; do not replace it
with a generic checklist.

Only report applicable items. A small diff does not need a long checklist, but
any applicable standard item must be satisfied, marked not applicable, or
returned as missing/blocking work with evidence.

### 3. Documentation Sync

Update docs in the same task when the code change affects anything a future user, teammate, or Codex session needs to know:

- Public API, CLI, environment variable, config, setup, deployment, data model, permissions, routing, or user-visible workflow changed.
- README, project `AGENTS.md`, `docs/`, runbooks, examples, or integration guides mention the old behavior.
- Tests or commands changed in a way future agents need to run.
- A Standard Development Contract ledger entry changes status or evidence.

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
    configured markdown/docs lint or docs build only when relevant, and grep
    durable docs for relative time. Do not run `make verify`, full app tests,
    full builds, or browser checks merely because the project has them.
  - code/API/shared behavior: run the smallest targeted test/lint/typecheck or
    reproduction that proves the behavior, plus `git diff --check`.
  - UI: run targeted app/browser/visual verification for the affected workflow
    and relevant product states, plus `git diff --check`.
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
  unverified subtask report. Completion claims require fresh evidence from this
  turn or an explicitly named retained command output.
- For UI changes, carry a `frontend_evidence_packet` before finalizing:

```yaml
frontend_evidence_packet:
  core_workflow: <workflow verified>
  verified_conditions: <operating conditions actually checked>
  motion_contract: <none | summary and evidence when UI motion/GSAP is used>
  not_verified:
    - condition: <relevant but unchecked condition>
      reason: <not applicable | impossible locally | out of scope>
  browser_or_visual_evidence: <screenshots, viewports, commands, or none>
  neighboring_surface_risk: <same-pattern pages/components at risk, or none>
  residual_risk: <remaining risk or none>
```

Happy-path-only UI verification is insufficient for data-heavy or async surfaces.
If a relevant operating condition from `project-frontend` is not verified, the
final state is either blocked or carries an explicit residual risk; do not call it
complete without the evidence boundary. If the user asks for strict or complete
frontend verification, no relevant dimension may be skipped without evidence and
reason.

### 5. Review Gates

Before finalizing, classify the requested review type and run the matching
gates. Keep local gates local by default; use subagents automatically only when
`project-lifecycle` provides `subagent_dispatch_policy.runtime_permission` =
`auto_parallel_safe` in a Context Packet. If the policy is blocked or unsafe, run
the review gate in the main thread and return the concrete fallback reason.

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
  - frontend_evidence_packet, UI Contract, motion_contract, and sibling-surface risk when UI is involved
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
2. If this iteration is running as a subagent, do not stage, commit, push, tag,
   or mutate Git history. Return `commit_needed: true` with candidate files,
   verification evidence, and message scope to `project-lifecycle`.
3. If running in the main thread, stage only files changed for this task. Never
   use `git add .` or `git add -A`.
4. If verification passed and the user did not explicitly forbid commits, create
   one focused commit automatically for the completed task.
5. Use the `project-commit` skill when available; follow Angular commit format.
5. If files touched by this task had pre-existing changes, inspect the final diff carefully. Commit only when every staged hunk is attributable to the current task; otherwise leave the worktree uncommitted and state the blocker.
6. Do not commit if unrelated pre-existing changes overlap with this task, verification failed, secrets are present, generated artifacts are ambiguous, or hooks fail and cannot be fixed cleanly. In that case, leave files uncommitted and state the blocker.
7. Never push unless the user explicitly asks.

When not inside a Git repo, say version management is unavailable because there is no Git repository. Do not create a repository unless the user asks.

## Final Response

Keep the final answer short and include:

- What changed, including docs changes.
- Completed plan item ids and any items returned to `project-lifecycle`, when
  invoked from a plan.
- Verification scope, commands or evidence, and key results.
- UI `frontend_evidence_packet` summary, when UI was changed.
- Standard compliance delta, when a ledger was active.
- `domain_resource_evidence`, when `software-contract` was loaded.
- Review type: `focused`, `deep`, or `exhaustive`.
- Inspected surfaces.
- Not inspected surfaces.
- Review result: focused local gates, or the `review` skill's deep/exhaustive
  result when explicitly requested.
- `cyclic_goal_delta`, when invoked inside a lifecycle cyclic goal.
- Residual risks.
- Commit hash and message, or the precise reason no commit was created.
