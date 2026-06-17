---
name: project-sync
description: >
  Public-safe infrastructure and Codex configuration sync template. Use for
  syncing Codex skills/configs between explicitly named machines or fleets,
  checking remote status, or running bounded batch commands. Fill in local host
  inventory privately; do not publish credentials, internal IPs, tokens, or
  organization-specific infrastructure.
---

# Project Sync

## Lifecycle Position

This is the `sync` / infrastructure coordination skill in the software-project
lifecycle. It handles machine status, SSH reachability, Codex skills/config
distribution, and bounded batch commands.

Do not use it for:

- new project creation,
- code iteration,
- release/deploy orchestration,
- broad documentation cleanup.

Sync actions must be exact: source, target, included paths, excluded paths, and
verification requirements must be explicit before touching remote machines.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet before sync
work. Preserve source/target boundaries, included paths, excluded paths,
verification requirements, and explicit safety limits. When provided, also
preserve `project_goal`, `goal_runtime`, `goal_synthesis` /
`control_system_goal`, `goal_preflight` / `optimality_law`,
`perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`loop_control_matrix`, `review_clean_pass_loop`,
`optimize_framework_cycle_loop`, `subagent_dispatch_policy`, `agent_owner`,
`write_policy`, `runtime_resource_ledger`, `subagent_runtime_registry`, and
`protocol_evidence`.

Return a Handoff Record with hosts touched, files or commands synced,
verification output, skipped targets, open risks, and any
`loop_control_matrix_delta`, `runtime_resource_delta`, or
`subagent_runtime_registry_delta` needed by an active lifecycle loop. Successful
sync alone never completes a parent goal unless the parent stop condition also
has passing verification, required review/optimization clean passes, no known
in-scope residual issue, and no unaccounted runtime resource.

## Public Safety Boundary

Never publish or sync from public templates:

- passwords, tokens, SSH private keys, credential helper files,
- internal IPs, hostnames, jump hosts, VPN/proxy credentials,
- auth files, sessions, logs, sqlite state, traces, shell snapshots,
- user-specific absolute paths unless they are intentionally examples.

For private deployments, keep host inventory and credentials in private local
docs or environment-specific configuration outside public repositories.

## Codex Skills Sync Contract

Default sync target for skills is `~/.codex/skills/`.

Valid skill directories must contain `SKILL.md`. Empty directories or directories
without `SKILL.md` are not valid skills. Before and after syncing:

1. list local valid skills,
2. list target valid skills,
3. sync only requested skill directories,
4. verify remote `SKILL.md` hashes,
5. report skipped targets and open risks.

Use `rsync -az --delete` only when the target directory is exactly the intended
skill directory. Do not run broad deletes against `~/.codex/` or a home
directory.

## Mac Or Workstation Sync Template

Set these values in the shell or replace placeholders privately:

```bash
SOURCE_SKILL_ROOT="${SOURCE_SKILL_ROOT:-$HOME/.codex/skills}"
TARGET_HOST="${TARGET_HOST:?set target host, for example user@example-host}"
TARGET_SKILL_ROOT="${TARGET_SKILL_ROOT:-~/.codex/skills}"
SKILL_NAME="${SKILL_NAME:?set skill name}"

test -f "$SOURCE_SKILL_ROOT/$SKILL_NAME/SKILL.md"
ssh "$TARGET_HOST" "mkdir -p $TARGET_SKILL_ROOT/$SKILL_NAME"
rsync -az --delete "$SOURCE_SKILL_ROOT/$SKILL_NAME/" \
  "$TARGET_HOST:$TARGET_SKILL_ROOT/$SKILL_NAME/"

LOCAL_HASH=$(shasum -a 256 "$SOURCE_SKILL_ROOT/$SKILL_NAME/SKILL.md")
REMOTE_HASH=$(ssh "$TARGET_HOST" \
  "shasum -a 256 $TARGET_SKILL_ROOT/$SKILL_NAME/SKILL.md")
printf 'local:  %s\nremote: %s\n' "$LOCAL_HASH" "$REMOTE_HASH"
```

## Batch Command Template

Use only for safe, bounded commands:

```bash
TARGETS="${TARGETS:?space-separated host list}"
COMMAND="${COMMAND:?safe command to run}"

for host in $TARGETS; do
  printf '\n[%s]\n' "$host"
  ssh -o ConnectTimeout=10 "$host" "$COMMAND"
done
```

Do not infer production mutations, destructive commands, or secret-requiring
commands from generic sync requests.

## Final Response

Report:

- source and target,
- hosts touched,
- files or commands synced,
- verification output,
- overwritten or deleted target items, if any,
- skipped targets or open risks.
