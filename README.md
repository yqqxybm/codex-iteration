# Codex Iteration

Public, sanitized Codex skill framework for self-iteration, review, optimization,
and software-project lifecycle work.

The system is built around cybernetic pragmatism:

> A skill is a finite control law for Codex in an uncertain world: user intent is
> the objective, evidence is feedback, boundaries constrain action, verified
> state change defines completion, and rules evolve only when real failures show
> the old control law is insufficient.

## What Is Included

- `skills/three-step-analysis`: deep non-project reasoning core.
- `skills/review`: evidence-first review gate.
- `skills/optimize`: optimization and review-then-optimize orchestrator.
- `skills/project-lifecycle`: software-project lifecycle controller.
- `skills/project-*`: project adapters and execution skills.
- `skills/co-star`, `skills/self-refine`, `skills/retrospective`: lightweight
  thinking frameworks.
- `config/config.example.toml`: public-safe Codex config example.

## What Is Not Included

This repository intentionally excludes:

- auth files, tokens, SSH keys, API keys, and credentials,
- sessions, traces, logs, sqlite state, shell snapshots, caches, and imports,
- machine-specific paths, private hostnames, internal IPs, server passwords, and
  company infrastructure details,
- bundled/system skills that are not authored as part of this framework.

`skills/project-sync` is included as a public template. It does not contain
private hostnames, IP addresses, passwords, jump hosts, or organization-specific
Git credentials.

## Install

Copy the skills you want into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
rsync -az skills/ ~/.codex/skills/
```

Then start a fresh Codex session so updated skill metadata is loaded.

For config, copy the example and adapt paths to your machine:

```bash
cp config/config.example.toml ~/.codex/config.toml
```

Do not copy the example blindly if your local Codex install already has working
plugin, MCP, or authentication settings.

## Operating Model

Use the smallest skill that owns the work:

- ordinary writing or prompt shaping -> `co-star` or `self-refine`,
- non-project deep decisions -> `three-step-analysis`,
- software-project decisions -> `project-analysis`,
- existing-project code changes -> `project-iteration`,
- new projects or multi-skill plan advancement -> `project-lifecycle`,
- review-only work -> `review`,
- material improvement or self-iteration -> `optimize`,
- review plus optimization -> `深度审查优化`.

The heavy loops are intentionally expensive. Use them for high-value artifacts,
repeated failures, skill changes, and configuration changes, not for every small
task.

## Safety

Before publishing any local Codex configuration, run a secret and infrastructure
scan. Do not publish private paths, sessions, logs, auth files, internal network
details, or credentials.
