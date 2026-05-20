---
name: project-release
description: >
  Release/operate skill for configured software projects. Use for build,
  release, deploy, publish, version bump, tag, rollout, health verification, or
  rollback. Requires project-specific docs, scripts, CI, or runbooks. Code
  changes go through project-iteration; new projects go through
  project-bootstrap.
---

# Project Release

## Lifecycle Position

This is the software project lifecycle `release` / `operate` skill. Enter this
skill when code is already implemented and the next work is versioning, build,
publish, deployment, health verification, or rollback.

Use `project-iteration` first when release requires code changes. Use
`project-bootstrap` first when the project does not yet have a runnable release
path.

Release work must follow the project lifecycle philosophy:
- Runnable truth: the build artifact must be produced by real project commands.
- Evidence closure: rollout, health, logs, or smoke checks must be verified.
- Project locality: commands must come from the current project's own docs,
  scripts, CI, or runbook.
- Operational knowledge: durable release facts belong in the project's runbook or
  docs, not only in chat.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before release
work. Preserve release target, environment, version/tag decision, rollback
requirement, and explicit deployment boundaries.

Return a Handoff Record with version/tag, build artifact, deployment command,
rollout or health evidence, rollback path, docs/runbook updates, open risks,
and the next recommended skill. Use `.codex/traces/` only for long releases or
incident-prone chains; durable operations facts belong in runbooks through
`project-docs`.

## Release Preflight

Before executing release commands:

1. Identify the repository, worktree state, target environment, and intended
   release scope. Ask only when the target or action is ambiguous enough to
   mutate the wrong environment.
2. Read project-local release sources in this order when present:
   `docs/runbook*`, `docs/deploy*`, `README.md`, `AGENTS.md`, `Makefile`,
   package scripts, CI config, deployment scripts.
3. Identify the artifact, version/tag policy, publish destination, deployment
   command, health check, and rollback path.
4. If project-local release instructions are missing, stale, or unsafe, stop and
   state the exact blocker. Do not invent a deployment path from another
   project.

## Release Workflow

1. Version: apply the project's documented version/tag process and verify the
   resulting version, tag, or changelog.
2. Build: run the documented build command and verify the artifact exists or the
   image/package digest is available.
3. Publish or deploy: run only the project-approved command for the requested
   environment.
4. Verify: run the documented rollout, smoke test, health check, log check, or
   equivalent production-readiness signal.
5. Rollback readiness: identify the rollback command or previous known-good
   artifact before claiming completion.
6. Docs: update release/runbook docs only when the executed path reveals durable
   operational knowledge that was missing or stale.

## Safety Rules

- Do not push tags, publish artifacts, deploy, or rollback by inference.
- Do not print production credentials, tokens, private keys, or secret values.
- Do not present a failed build, publish, health check, or rollout as complete
  through weaker evidence; state the blocker first.
- Do not reuse commands, namespaces, paths, registries, or service names from
  another project.
- If rollback is unknown, state that before deployment and treat it as a release
  risk.

## Final Response

Report:
- target environment and release scope
- version/tag/commit result
- artifact or image/package identifier
- exact commands run and key output
- health or rollout evidence
- rollback path
- docs/runbook changes, or why none were needed
