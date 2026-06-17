---
name: review
description: >
  Independent evidence-first review/audit gate. Use when the user asks to review,
  audit, inspect, check quality, find risks, run deep/exhaustive review, standard
  compliance review, "深度审查", "全面审查", "穷尽审查", "逐词逐句", "审查一下",
  "挑问题", "有没有风险", or "看有没有问题" for code, repos, diffs, documents,
  skills, configs, plans, prompts, workflows, release readiness, or handoff state.
  Review-only: do not edit, commit, deploy, sync, or rewrite.
---

# Review

Review is an evidence-first judgment gate. It answers what is materially wrong,
risky, missing, or unverified.
It is independent and review-only: the target may be a project, document, skill,
config, diff, release, or workflow, but the action remains judgment rather than
implementation.

## Philosophy

1. **Evidence over impression**: every finding cites observed text, code, behavior, command output, or missing proof.
2. **Risk over checklist**: inspect dimensions that can change the outcome; do not mechanically fill categories.
3. **Findings first**: defects and residual risks come before summary, taste, or advice.
4. **Judgment before action**: do not repair, rewrite, patch, commit, deploy, sync, or quietly improve the target.
5. **Falsifiable claims**: each finding must be confirmable or rejectable from cited evidence.
6. **No issue inflation**: if no material findings exist, say so directly.
7. **Optimality discipline**: review looks for unresolved tension under current
   evidence and constraints. Do not turn a new idea into a finding unless it
   shows intent is not faithfully served, rules do not reliably produce correct
   behavior, complexity is not justified by value, or a simpler structure
   preserves equal or better behavior.

## Feedback Sensor Model

Review is the system's evidence sensor, not its improvement engine. It compares
the intended state with observed evidence and reports only material control
failures:

- intent-state deviation: the artifact does not serve the stated target,
- evidence gap: the claim, completion, or safety condition is unverified,
- boundary violation: the artifact acts outside its allowed scope,
- stop failure: the artifact cannot justify why work should stop.

Do not report a new abstraction, prettier wording, or alternate design unless it
exposes one of these failures.

## Contract And Boundary

Use for review-only requests: code/diff review, repo/project audit,
document/prompt review, skill/config review, security/data-risk checks, release
readiness, handoff quality, or broad "看一下有没有问题" requests.

Do not use for implementation, fixing, refactoring, deploying, syncing, or
rewriting. Do not provide patches, rewritten artifacts, commits, deployment, or
sync actions unless the user explicitly asks after the review.

Resolve internally:

- **Target**: exact artifact, diff, repo area, document, plan, or workflow.
- **Standard**: correctness, safety, maintainability, readiness, compliance,
  handoff quality, or the user's stated standard.
- **Optimality law**: when supplied by lifecycle, use its value ordering,
  elegance constraint, non-goal boundary, and falsification test as the review
  standard for "is this good enough".
- **Evidence**: files, diffs, commands, logs, screenshots, docs, or user text.
- **Depth**: focused, quick, standard, deep, or exhaustive.
- **Stop line**: what is intentionally outside scope.

Ask only when missing target or standard would point the review at the wrong
surface. If `request_user_input` is available and the fork is blocking, use it
with concise options; otherwise ask a short text question and stop.

## Depth And Chains

- **Focused**: explicitly narrow target such as current diff only, one file,
  one issue, or one workflow. Never call this deep review.
- **Quick**: obvious blockers or high-risk issues in a narrow target.
- **Standard**: main artifact, related files, and cheap verification; use by default.
- **Deep**: cross-references, call chains, edge cases, docs, config, verification gaps.
- **Exhaustive**: all relevant directions, repeated until local/requested pass criteria are met; use for "逐词逐句", "全面", "完全".

For deep or exhaustive reviews, use this chain without changing review-only
scope:

1. `three-step-analysis`: define standard, risk model, hidden assumptions, and likely failure paths. For software-project, Codex skill-system, lifecycle, config, or agent reviews governed by `project-lifecycle`, use the supplied `goal_preflight` / `optimality_law` or the `project-analysis` adapter as this three-step lens instead of bypassing the project controller.
2. `review`: inspect direct evidence and produce findings.
3. `self-refine`: critique the report for missing evidence, weak severity, duplicates, unclear impact, or overclaiming.
4. `retrospective`: only when prior feedback or repeated review failure should change future behavior.

When invoking another skill, read its `SKILL.md` before claiming use. Do not use
the chain to edit, rewrite, patch, commit, deploy, or sync the target.

For deep or exhaustive reviews, stop only after two consecutive **auditable**
clean passes. A pass counts only when it records:

- risk model or review lens checked through `three-step-analysis`,
  `project-analysis`, or a lifecycle-supplied `goal_preflight` adapter,
- direct evidence surfaces inspected by `review`,
- verification or pressure scenarios run, simulated, or explicitly skipped,
- findings delta: new, changed, removed, or none,
- `self-refine` critique of the report for missing evidence, weak severity,
  duplicates, unclear impact, or overclaiming.

A clean pass means the finding set is stable: no new material target finding,
no missing required surface, no missing evidence, no severity problem, no
duplicate finding, and no output-quality issue. Existing unresolved target
findings may remain in a clean pass only when they are already reported and the
review-only boundary prevents fixing them. If any pass finds a new material
target issue, required coverage gap, or report-quality issue, update the report,
reset `clean_passes` to 0, and run another full pass. Do not count script
checks, rereading, or intuition as a pass unless the pass log above is present.
Do not claim `2/2 clean passes` without two consecutive pass-log entries after
the last finding/report change.

When invoked by `project-lifecycle` for a `cyclic_goal_loop`, return this
review delta in addition to the normal findings:

```yaml
goal_review_delta:
  depth: <focused | deep | exhaustive>
  material_new_work: <agenda items or none>
  clean_pass_delta: <reset_to_0 | increment_by_1 | satisfied | blocked>
  reset_reason: <material finding, missing required surface, changed evidence, or none>
  inspected_stop_surfaces: <agenda, diff, tests, docs, release, deploy health, known issues>
  known_residual_issues: <none | list | unknown>
```

A review can increment the parent clean-pass counter only when its inspected
surfaces cover the parent stop condition for the requested depth. If a material
in-scope finding appears, or if a required stop-condition surface was not
inspected without a valid exclusion, set `clean_pass_delta: reset_to_0` or
`blocked`; do not let the lifecycle controller count it as clean.

## Review-Optimize Ledger

When review is used inside an explicit "深度审查优化" loop, preserve the
review-only boundary and output a `Finding Ledger` that `optimize` can consume.
Do not invoke `optimize` from this skill.

Initial gate items default to `open` when they are material findings. Closeout
updates item status from new evidence; it does not silently drop unresolved
items.

Each ledger item must include:

- `id`: stable short id.
- `severity`: P0-P3.
- `evidence`: observed, verified, inferred, or missing evidence.
- `impact`: why it matters.
- `fix_direction`: concrete correction direction, not a patch.
- `status`: `open`, `closed`, `rejected`, `deferred`, or `blocked`.
- `closeout_requirement`: evidence needed to mark it closed.

In closeout mode, inspect the optimization delta against the ledger. A closeout
is clean only when every material item is closed, rejected with evidence, or
explicitly deferred/blocked with a reason, and no new material finding appears.
If the optimization changed the target materially, review clean passes reset and
must be rerun after that delta. For deep or exhaustive closeout, the normal
two-clean-pass review requirement still applies; do not treat one closeout scan
as enough.

## Scope Rules

Do not broaden scope beyond the user's target, but do not shrink an explicit
deep or exhaustive review to the current diff. "Do not broaden scope" prevents
unrequested product areas from being pulled in; it does not override words such
as "deep", "全面", "整个产品", "不要只看改动", or "exhaustive".

### Scope Expansion Preflight

Before reviewing skills, configs, standard contracts, call chains, ledgers,
handoffs, or review-optimize behavior, build a compact scope model:

```yaml
scope_model:
  direct_targets: <user-named files, diffs, skills, or artifacts>
  primary_owners: <skills or files directly responsible for the target>
  adjacent_modifiers: <non-owners that can change the same evidence, state, or claim>
  downstream_consumers: <skills, users, commands, or workflows relying on that evidence>
  completion_claim_scope: <focused | scoped-system | exhaustive>
```

For standard compliance, lifecycle, ledger, handoff, or delivery-contract
reviews, do not inspect only the named owner. Include any adjacent modifier that
can mutate the same evidence state, such as a refinement, docs, commit, release,
or iteration skill that can make the completion claim true or false. If an
adjacent modifier is intentionally not inspected, list it under `not inspected`
with the reason. A clean result is valid only inside the declared
`completion_claim_scope`.

### Perspective Lens Synthesis

For deep, exhaustive, whole-product, product-quality, skill/config,
project-system, or post-implementation reviews, build a compact
`perspective_model` unless the lifecycle Context Packet already supplied one.
This model is not a checklist of personas. It is a generated set of material
review lenses derived from the user's goal, target artifact, product category,
failure symptoms, and evidence.

Use role seeds only when they can change findings or residual risk:

- the requesting user and the frustration behind the request,
- the product's core user/customer/operator,
- a professional engineer maintaining the code or workflow,
- a product manager judging value, scope, adoption, and positioning,
- an architect judging boundaries, coupling, scalability, and failure spread,
- security/data/release/operator roles when those risks are in scope,
- a same-category product user who would switch only if this product is better,
- a future Codex/session/user when reviewing skills, prompts, configs, or agent
  workflows.

Each selected lens must record:

```yaml
perspective_lens:
  role: <material viewpoint>
  core_question: <what this role would ask>
  evidence_surface: <what must be inspected>
  finding_standard: <what counts as a material defect>
```

Reject lenses that only add taste, duplicate another lens, or cannot be checked
from evidence. Findings still require evidence. Do not report "as a user I
would prefer..." unless the preference exposes intent-state deviation, an
evidence gap, a boundary violation, a stop failure, or a realistic adoption
barrier under the stated product goal.

When review happens after implementation, default the target to at least:

- the user's original goal and acceptance criteria,
- the final diff and changed files,
- direct call chain and integration points,
- the core user workflow affected by the change,
- related config, tests, docs, examples, and runbooks,
- UI Contract / `frontend_evidence_packet` coverage when UI is involved,
- verification commands already run and verification gaps.

If the user explicitly asks to review the whole product/project, include entry
points, core workflows, build/test scripts, configuration, docs/handoff, and
release/operational risks that are material to that product. Ask only when the
product boundary is genuinely ambiguous. If the user says "only this diff" or
equivalent, keep the review focused and label it `focused`.

Never call a focused diff-local review `deep`, `comprehensive`, `全面`, or
`exhaustive`. If only a focused review was run, say so directly.

## Review Surfaces

Review only surfaces that can change the answer:

- **Diff/code**: changed files, call sites, tests, API contracts, error paths, regression surface.
- **Repo/project**: instructions, entry points, build/test scripts, docs, dependency and config boundaries.
- **Document/prompt/plan**: purpose, audience, assumptions, consistency, constraints, actionability.
- **Skill/config**: metadata, triggers, body, cross-skill refs, naming, boundaries, call chains, stale wording, verification, context cost, user conflicts, pressure scenarios.
- **Standard compliance**: `standard_compliance_ledger`, guide requirement
  status, equivalent path mapping, evidence quality, missing/not-applicable
  justification, and owner handoff.
- **Security/data**: credentials, injection boundaries, permissions, destructive operations, privacy, logging.
- **Release/readiness**: build path, deployment instructions, health checks, rollback, runbook, operational evidence.
- **UI/UX**: workflow, accessibility, responsive behavior, visual regressions,
  loading/empty/error states, long content/list pressure, permission/disabled
  states, screenshots, motion behavior, and UI Contract /
  `frontend_evidence_packet` coverage.

### UI Contract Audit

For UI/UX review, keep review pure: do not invent a new design standard or
rewrite the frontend contract. Audit whether the owning frontend work provided a
`ui_contract` or `frontend_evidence_packet`, whether it covers the relevant
operating conditions for the core workflow, whether unverified conditions have
valid reasons, and whether sibling pages/components using the same UI pattern are
called out. A missing or happy-path-only evidence packet is a review finding when
the surface is data-heavy, async, permissioned, responsive, or otherwise state
sensitive.

For software-project UI work, load `software-contract` and read
`~/.codex/skills/software-contract/references/frontend-quality-contract.md` when
the UI Contract details affect the finding. If the reference is required but
unavailable, report that as missing evidence instead of reviewing from memory.
When visual quality, component behavior, accessibility, responsive behavior, or
rendered QA determines the finding, also read
`~/.codex/skills/software-contract/references/frontend-design-contract.md` and
audit whether a compact `design_contract_evidence` or equivalent rendered QA
evidence exists.

When the reviewed UI is a landing page, portfolio, brand page, redesign,
product page, prototype, source-inspired UI, high-aesthetic screen, or a UI the
user says looks generic, also read
`~/.codex/skills/software-contract/references/frontend-taste-contract.md`.
Audit whether the work has a defensible design read, calibrated
variance/motion/density, anti-default audit, redesign preservation boundary when
applicable, and taste preflight evidence. Report taste issues only when they
contradict the stated design standard, user goal, rendered evidence, or this
contract; do not report personal preference as a finding.

When the reviewed UI includes any motion effect, also read
`~/.codex/skills/software-contract/references/frontend-motion-contract.md`.
Audit whether GSAP was used as the motion engine, whether a `motion_contract`
exists, and whether reduced motion, mobile/resize, cleanup, and debug-marker
risks were verified. If motion was implemented with CSS/WAAPI/Framer Motion
without explicit user approval or project mandate, report it as a policy
violation rather than silently accepting the downgrade.

Default risk dimensions: correctness, regression risk, security/data, evidence,
maintainability, docs/handoff, and UX/accessibility when user-facing. Do not
report personal taste unless it affects correctness, maintainability,
accessibility, safety, or the stated standard.

### Standard Compliance Audit

When reviewing against the Standard Development Contract, do not implement or
fill docs. Audit whether every guide requirement is represented in the ledger,
whether statuses are justified by evidence, whether optional items were
evaluated instead of omitted, whether equivalent files truly cover the required
content, and whether missing/blocking/deferred items have owners and next
actions. A project may pass only if no required item is unaccounted and no
`satisfied` item relies on an empty placeholder.

For software-project standard reviews, load `software-contract` and read
`~/.codex/skills/software-contract/references/standard-development-contract.md`.
Read `~/.codex/skills/software-contract/references/docs-deliverables.md` when
equivalent document paths or handoff assets determine the finding.

## Workflow

### 1. Scope

State target, standard, evidence, depth, and stop line when they affect the
review. If inside a Git repo and the review concerns code or docs, inspect
`git status --short` and relevant diffs. For non-repo artifacts, identify the
exact text, file, screen, or workflow. Do not broaden scope because nearby
material looks interesting, but apply the Scope Rules above when the user asked
for deep, exhaustive, whole-product, or post-implementation review.

### 2. Inspect

Read the smallest sufficient set of files or artifacts. Prefer direct evidence
over summaries. For project/repo review, prioritize instructions such as
`AGENTS.md`, entry points, changed files, call sites, tests, build scripts,
docs/runbooks, config, secrets boundaries, CI, and deployment files when
relevant.

### 3. Verify

Run safe checks when they materially improve the review: `git diff --check`,
targeted tests, lint, typecheck, build, smoke checks, docs command checks, or
browser/screenshot checks for UI. Prefer targeted commands over broad suites
unless the broad command is the normal cheap check.

For skill/config review, include pressure scenario checks when they materially
improve confidence:

- trigger scenario: a request that should load or apply the skill,
- boundary scenario: an adjacent request that should not load it,
- failure scenario: skipped tool, premature action, over-questioning, false
  completion, or wrong handoff,
- chain scenario: upstream/downstream skill interaction when relevant.

Mark these as executed, simulated locally, or not run. A simulated scenario is
evidence for reasoning quality, not proof that the runtime loader will behave
identically.

Treat command output as evidence, not proof that uninspected surfaces are safe.
Do not run production mutations, deploys, destructive commands, expensive jobs,
or commands requiring secrets by inference. If a useful check is skipped, state
the exact reason: unsafe, too expensive, missing dependency, missing secret,
unclear target, or outside scope. Never claim coverage for uninspected or
unverified surfaces.

### 4. Findings

Lead with findings, ordered by severity:

- **P0**: data loss, security exposure, production outage, irreversible action.
- **P1**: likely correctness bug, release blocker, broken core workflow.
- **P2**: meaningful regression risk, missing important test/docs/edge case.
- **P3**: minor but material maintainability, clarity, or coverage risk.

Evidence levels:

- **Verified**: reproduced or confirmed by command output, rendered output, or
  another direct check.
- **Observed**: directly visible in the reviewed artifact.
- **Inferred**: follows from a plausible execution, usage, or handoff path; name
  that path.
- **Missing evidence**: required proof, test, doc, or verification is absent.

Each finding must include severity, file and line when available, evidence
level, evidence, user impact, and concrete fix direction.

Include a finding only when at least one is true:

- the artifact contradicts a stated requirement, local convention, or intended
  behavior,
- a realistic user, operator, or downstream consumer can hit the failure,
- required verification, documentation, or handoff evidence is missing,
- security, data, permission, or destructive-action boundary is exposed,
- meaningful future maintenance or ownership risk is created.

Reject an issue when it is only personal taste, speculation without plausible
trigger, polish outside the standard, an alternative design without a concrete
defect, non-material re-optimization drift, or a duplicate of a more severe
finding.

For artifacts that already passed a deep review-optimize closeout, start from
preservation. A later review may reopen the artifact only with new failure
evidence, a failed pressure scenario, an active-instruction conflict, unjustified
complexity, or a simplification that preserves equal or better behavior.
Otherwise record the idea as rejected drift, not as a finding.

Merge symptoms with the same root cause and fix direction. Split only when
impact, owner, or remediation differs. If no issues are found, say so directly
and name unchecked surfaces or remaining test gaps.

## Output

Findings come first. Do not start with praise, recap, or broad summary when
findings exist. Order findings by severity, then likelihood and blast radius.
Use absolute local file paths for real files. If no material findings exist, say
"No material findings" and scope it to inspected coverage. Keep fix directions
concrete but do not implement them. Include verification and coverage; for
deep/exhaustive reviews, include convergence passes, pass log, and stop reason.
When used inside a "深度审查优化" loop, include `Finding Ledger` for initial
review or `Closeout` for final review.

Use this structure:

```markdown
Findings
- [P1] <title> - </absolute/path/file:line>
  Evidence level: <Verified | Observed | Inferred | Missing evidence>
  Evidence: <why this is real>
  Impact: <user/project consequence>
  Fix direction: <what should change>

Review Standard
- Depth: <focused | quick | standard | deep | exhaustive>
- Standard: <correctness | safety | maintainability | readiness | handoff | other>
- Clean claim type: <focused | scoped-system | exhaustive>
- Optimality law: <value ordering and falsification test used, or N/A>
- Scope model: <direct targets, primary owners, adjacent modifiers, downstream consumers>
- Perspective model: <material lenses used, or why not applicable>

Review Convergence
- Passes: <N, for deep/exhaustive>
- Clean passes: <clean_passes>/2
- Stop reason: <two consecutive clean passes | requested pass count | blocker | safety boundary>
- Pass log:
  - Reset history: <finding/report change that reset clean_passes, or none>
  - Last clean pass 1: <risk lens, inspected surfaces, verification/scenarios, findings delta, self-refine critique, clean?>
  - Last clean pass 2: <risk lens, inspected surfaces, verification/scenarios, findings delta, self-refine critique, clean?>
  - Earlier material passes: <new findings or report corrections before the final two clean passes, or none>

Verification
- <command> -> <key result>
- Not run: <reason>

`domain_resource_evidence`
- <software-contract references loaded or missing, when used>

Coverage
- Inspected: <surfaces actually reviewed>
- Not inspected: <material surfaces outside scope or unavailable>

Residual Risk
- <unchecked surface or none>

Finding Ledger / Closeout
- <only when used inside a review-optimize loop>
```

For no findings, replace the Findings section with `No material findings.`
Keep summaries secondary. Do not bury findings under general commentary.
