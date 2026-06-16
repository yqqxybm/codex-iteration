# Project Documentation Contract

Use this reference when `project-lifecycle`, `project-bootstrap`,
`project-docs`, or `review` must decide what project documentation should exist.
It is a document-shape contract, not a filename checklist.

The Standard Development Contract defines coverage and evidence. This contract
decides the smallest document set that fits the project shape, lifecycle stage,
and audience. Do not create a new document merely because a guide item or
example filename exists.

## Decision Order

Before creating, deleting, or declaring a documentation gap, record this profile:

```yaml
doc_profile:
  project_shape: <prototype | frontend-app | backend-api | fullstack-product | library | cli-or-automation | infra-or-ops | codex-skill-or-config | mixed>
  lifecycle_stage: <idea | charter | bootstrap | iteration | version | release | handoff>
  audience: <future-codex | human-developer | operator | external-integrator | end-user>
  current_docs: <existing README/AGENTS/docs/contracts>
  required_docs: <minimal docs required now>
  conditional_docs: <docs required only if condition applies>
  prohibited_by_default: <docs that must not be created without a matching condition>
  docs_ia: <root files and docs/ subdirectories authorized now>
```

Then choose one action:

- `update_existing`: the normal path when an existing authoritative location can
  hold the fact.
- `merge_or_delete`: use when duplicate, stale, or over-specific docs exist.
- `create`: allowed only when the profile requires a missing durable location or
  the user explicitly asked for that document.
- `mark_missing`, `deferred`, `blocked`, or `not_applicable`: use when evidence
  is required but a document should not be created now.

## Shape Profiles

These profiles are defaults. Local repo conventions or explicit user direction
can override them, but the override must be recorded in the ledger.

| Project shape | Required now | Conditional | Prohibited by default |
| --- | --- | --- | --- |
| `prototype` | README section with purpose, run command, and current limit | short `AGENTS.md` only if future Codex sessions need repo rules | PRD, ADR tree, runbook, release checklist, integration guide |
| `frontend-app` | README; project `AGENTS.md` when local conventions matter; one architecture/design section when routing, state, API, or UI system is nontrivial | UI contract/design notes, deployment/runbook, API integration notes, accessibility/test notes | backend data model, SLO, postmortem, rollout plan unless operated in production |
| `backend-api` | README; project `AGENTS.md`; API/route contract; config/env section | architecture, data model/schema, runbook, deployment, security notes, observability/SLO | UI design docs, product PRD, rollout plan unless product/release stage needs them |
| `fullstack-product` | README; project `AGENTS.md`; scope/MVP section; architecture covering frontend/backend boundary | API/data contracts, runbook, deployment, metrics/NFR, release notes | separate PRD/Metrics/NFR files when a compact product section is enough |
| `library` | README with install/use/API examples; project `AGENTS.md` when contributor rules matter | changelog/release notes, contributing, API reference, compatibility matrix | deployment, runbook, SLO, PRD unless the library is operated as a service |
| `cli-or-automation` | README with commands, inputs, outputs, and config; project `AGENTS.md` if automation has local rules | runbook if scheduled/operated, troubleshooting, security/credential notes | PRD, integration guide, architecture doc unless workflows are complex |
| `infra-or-ops` | README/runbook; topology or architecture; rollback/verification commands | security, observability/SLO, release checklist, incident template | product PRD, UI docs, API guide unless exposed to integrators |
| `codex-skill-or-config` | `SKILL.md` or config file itself; short README is normally unnecessary | references/scripts/assets only when directly used by the skill | auxiliary README, install guide, changelog, generic docs |

For `mixed`, select the smallest union of the applicable profiles. Do not stack
every profile's optional docs.

## Documentation Information Architecture

Do not let standalone project docs accumulate as a flat pile. Choose document
placement by audience and function before creating files.

Root-level files are limited to repository entry and tool conventions:
`README.md`, `AGENTS.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, and
project-native config. Other durable project docs belong under `docs/` unless
the user or framework convention explicitly requires a root file.

When standalone docs are required, use this canonical `docs/` shape. Create only
directories that receive at least one authorized, project-specific document; do
not add empty folders or placeholder files just to show structure.

| Directory | Owns | Examples |
| --- | --- | --- |
| `docs/product/` | product intent, scope, requirements, roadmap, metrics, NFR | `charter.md`, `mvp.md`, `requirements.md` |
| `docs/architecture/` | architecture, decisions, module boundaries, data model | `overview.md`, `adr-0001-*.md`, `data-model.md` |
| `docs/development/` | local development, testing, coding workflow, contributors | `setup.md`, `testing.md`, `workflow.md` |
| `docs/operations/` | deploy, runbooks, release, monitoring, rollback | `runbook.md`, `deployment.md`, `release-checklist.md` |
| `docs/integrations/` | external API/SDK/CLI usage and integration contracts | `api.md`, `webhooks.md`, `sdk.md` |
| `docs/handoff/` | stage handoff, migration notes, operational transition | `handoff-YYYY-MM-DD.md`, `migration.md` |

Flat `docs/*.md` is allowed only for `docs/README.md` or for one or two small
standalone docs in a simple project. Once there are three or more standalone
docs, or more than one audience, move them into the canonical subdirectories and
leave `docs/README.md` as a short index when useful.

## Equivalent Evidence Locations

Evidence may live in existing project-native files. Equivalent paths are valid
when the ledger records the mapping:

- MVP, Vision, PRD, Metrics, and NFR can be sections in README, product docs, or
  architecture docs when they remain clear and discoverable.
- Tech stack, architecture, deployment, data model, flows, observability, and
  SLO evidence can be sections, native schema/API files, or dedicated docs when
  the profile requires separation.
- CONTRIBUTING, CODEOWNERS, PR/Issue templates, branch protection, hooks,
  CI/CD, release, SBOM, signing, testing, security, and rollout evidence can
  live in platform-standard config or workflow files when those files are the
  real source of truth.

## Creation Bar

Create a new documentation file only when all are true:

1. the doc profile says the audience and lifecycle stage need a durable
   standalone location,
2. no existing location can hold the information cleanly,
3. the file will contain project-specific facts, commands, decisions, ownership,
   or next actions,
4. the standard ledger records the mapping and status.

If any condition fails, update existing docs or mark the item as
`not_applicable`, `deferred`, `blocked`, or `missing` with evidence. Empty
templates and generic placeholder docs are not valid evidence.

## Documentation-Only Verification Boundary

For docs-only or text-only changes, verification evidence is documentation
evidence, not broad project runtime verification by default. Use the smallest
proof that the documentation is correct:

- inspect the final diff for the touched docs,
- run `git diff --check` in Git repos,
- validate referenced paths, commands, env vars, links, or anchors that the
  touched docs mention when practical,
- run the configured markdown/docs lint or docs build only when it exists and is
  relevant,
- check that durable docs avoid relative time such as `今天`, `昨天`, `最近`,
  `today`, `yesterday`, or `recently`.

Do not run `make verify`, full app test suites, full builds, or broad browser
checks for docs-only edits unless the user explicitly requests full project
verification, the docs change modifies runnable commands/API/deploy/test
instructions that need targeted proof, or a release/security/compliance gate
requires broader evidence.
