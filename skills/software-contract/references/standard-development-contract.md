# Standard Development Contract

Use this reference when a software project is created, phase-advanced, prepared
for handoff/release, or reviewed against the user's `标准开发指南`.

This contract defines maturity coverage and evidence. It does not by itself
authorize creating files. Before creating documentation, load
`docs-deliverables.md` and apply the project documentation profile.

## Core Rule

Full standard enforcement means every requirement in the guide is accounted for
with one of these statuses:

- `satisfied`: evidence exists and is current.
- `not_applicable`: the condition does not apply, with a concrete reason.
- `blocked`: cannot be completed without missing input, access, secret, or safe approval.
- `deferred`: intentionally postponed by user/project phase, with next action.
- `missing`: required and not yet provided.

Do not treat optional guide items as invisible. Evaluate the condition; if it
applies, the item becomes required.

Equivalent paths are valid. For example, `docs/architecture.md` may satisfy
`Architecture.md`, and `docs/development.md` may satisfy `开发文档.md`, if the
ledger records the mapping.
For new or reorganized documentation, also record the information architecture
mapping from `docs-deliverables.md`; root-level files must remain repository
entry/tool-convention files, while standalone docs live under the appropriate
`docs/` subdirectory.

Required evidence is not a required filename. If the project profile does not
need a standalone document, satisfy the item through an existing authoritative
section, native config/schema/workflow file, or mark it `not_applicable`,
`deferred`, `blocked`, or `missing` with a concrete reason.

## Ledger Shape

```yaml
standard_compliance_ledger:
  source: 标准开发指南
  entries:
    - requirement: <phase/item>
      owner_skill: <project-lifecycle | project-brief | project-analysis | project-bootstrap | project-iteration | project-docs | project-release | project-commit | project-retrospective | project-refine | review>
      status: <satisfied | not_applicable | blocked | deferred | missing>
      evidence: <path, command, setting, test, or reason>
      next_action: <agenda item, none, or user decision needed>
```

## Required Coverage Map

| Guide area | Required evidence | Primary owner |
| --- | --- | --- |
| Requirements and scope | MVP boundary, target user, core scenarios, acceptance criteria; Vision/PRD, Metrics, and NFR evaluated | `project-brief`, `project-lifecycle`, `project-bootstrap`, `project-docs` |
| Tech stack | language/runtime/framework versions, data stores, deploy platform, third-party services, key tradeoffs, ADR when material | `project-bootstrap`, `project-analysis`, `project-docs` |
| Architecture | module boundaries, data model/schema, API contracts, flows, deployment topology, observability/SLO when applicable | `project-analysis`, `project-bootstrap`, `project-docs` |
| Repository | README, LICENSE, `.gitignore`, CODEOWNERS, pre-commit/secret-scan applicability | `project-bootstrap`, `project-docs` |
| Code intelligence | CodeGraph initialized and indexed in the project root; `.codegraph/` ignored unless deliberately versioned; `codegraph status <project-root>` evidence recorded | `project-bootstrap`, `project-lifecycle` |
| Version workflow | `CONTRIBUTING.md` or equivalent collaboration guide covering commit convention, branch/PR/review policy; PR template; branch protection setting evidence or `branch-protection.yml`; issue template; commit hooks; release notes policy | `project-docs`, `project-commit` |
| CI/CD | pipeline config or explicit blocker/deferred item, lint/type/test/build thresholds, coverage thresholds, dependency/SAST scan, release trigger alignment, SBOM, artifact signing, signing-key management | `project-bootstrap`, `project-iteration`, `project-release`, `project-docs` |
| Dev environment | lockfile, toolchain version, `.env.example`, dependency scopes, container/compose/editor config, runtime config injection, SBOM/vulnerability-scan applicability | `project-bootstrap`, `project-docs` |
| Coding concerns | errors, trust boundary, config, resources, timeouts/retry/idempotency, logs, security, contracts, testability, performance | `project-iteration`, `review` |
| Testing | test layout, `TESTING.md`, unit/integration/e2e/contract/perf/security/IaC-smoke applicability, performance baseline and security scan reports when relevant | `project-bootstrap`, `project-iteration`, `project-docs` |
| Documentation | development doc entry, README, CONTRIBUTING, docstrings for public APIs, ADR, runbook, API docs, changelog applicability, docs information architecture | `project-docs`, `project-iteration` |
| Rollout | dogfood/integration/gray release/feature flag/rollback applicability, data compatibility, feedback triage, and `Rollout-Plan.md` when relevant | `project-release`, `project-docs` |
| Release | `Release-Checklist.md`, tag/release traceability, config audit, migration/rollback readiness, release notes | `project-release`, `project-docs` |
| Monitoring and iteration | metrics, alerts/on-call, SLO/error budget, postmortem template, incident/postmortem records, tech debt log | `project-release`, `project-docs`, `project-retrospective` |

## Anti-Bloat Rule

The contract requires status and evidence, not maximal paperwork. Prefer short,
true, linked project assets over long generic documents. A skeleton is acceptable
only when it names the real owner, command, boundary, or next action. Empty
templates are `missing`, not `satisfied`.
