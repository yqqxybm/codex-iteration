---
name: project-release
description: >
  Downstream release/operate stage selected by project-lifecycle for configured
  software projects. Use when the lifecycle controller assigns build, release,
  deploy, publish, version bump, tag, rollout, health verification, or rollback.
  Requires project-specific docs, scripts, CI, or runbooks. Code changes remain
  with project-iteration; new projects remain with project-bootstrap.
---

# Project Release

## Lifecycle Position

This is the downstream software project lifecycle `release` / `operate` skill.
`project-lifecycle` enters this skill when code is already implemented and the
next work is versioning, build, publish, deployment, health verification, or
rollback.

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
requirement, `standard_compliance_ledger`, and explicit deployment boundaries.
When provided, also preserve `project_goal`, `goal_runtime`, `goal_synthesis` /
`control_system_goal`, `goal_preflight` / `optimality_law`,
`perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`loop_control_matrix`, `review_clean_pass_loop`,
`optimize_framework_cycle_loop`, `runtime_resource_ledger`,
`subagent_runtime_registry`, `subagent_dispatch_policy`, `agent_owner`,
`write_policy`, and `protocol_evidence`.

Return a Handoff Record with version/tag, build artifact, deployment command,
rollout or health evidence, rollback path, docs/runbook updates,
standard compliance delta, `domain_resource_evidence` when `software-contract`
was loaded, open risks, the next recommended skill, and any item status, result,
and verification evidence needed by an active `plan_state_sink`. Use
`.codex/traces/` only for long releases or incident-prone chains; durable
operations facts belong in runbooks through `project-docs`.

Release mutation is a main-thread operation. If invoked as a subagent, preserve
the assigned `agent_owner` and `write_policy`; do not edit the parent goal, do not spawn subagents,
and do not commit, push, deploy, publish, sync remote state, broaden scope, or
claim project completion. Return release readiness findings, command evidence,
blockers, or a runbook patch proposal to `project-lifecycle`.

When invoked inside a lifecycle `cyclic_goal_loop`, also return:

```yaml
cyclic_goal_delta:
  release_state: <not_applicable | built | published | deployed | blocked>
  deploy_health: <pass | fail | not_applicable | blocked>
  rollback_ready: <true | false | not_applicable>
  clean_pass_reset_required: <true | false, with reason>
  material_in_scope_new_work: <agenda items or none>
```

Failed build, publish, deploy, health, rollback, or release-doc evidence inside
the parent goal boundary is material new work and resets the parent clean-pass
counter.

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
5. If the Standard Development Contract is active, check release-related ledger
   entries before mutation: CI/CD, release checklist, tag/release traceability,
   deployment docs, rollout/gray plan applicability, monitoring/health evidence,
   migration compatibility, SBOM, artifact signing, signing-key management, and
   rollback path. Load `software-contract` and read
   `~/.codex/skills/software-contract/references/standard-development-contract.md`
   when standard details determine release status. If the reference is required
   but unavailable, stop and report the missing resource.

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
6. Supply chain: verify SBOM, artifact signing, and signing-key management when
   the project is production-facing or the ledger marks them required. If the
   project lacks support, mark the item `blocked` or `deferred` before release.
7. Docs: update release/runbook docs only when the executed path reveals durable
   operational knowledge that was missing or stale.
8. Standard ledger: mark release items `satisfied`, `not_applicable`, `blocked`,
   `deferred`, or `missing` with evidence. Do not deploy when a required
   production release item is `missing` unless the user explicitly accepts that
   risk.

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
- SBOM/artifact signing/signing-key result when required
- docs/runbook changes, or why none were needed
- standard compliance delta and release blockers, if any
- `domain_resource_evidence`, when `software-contract` was loaded
