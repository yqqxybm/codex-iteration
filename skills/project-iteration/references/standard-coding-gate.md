# Standard Coding Gate

Read this reference for every `material_change`, whenever a
`standard_compliance_ledger` is present, or when a `very_small` change touches a
standard-sensitive area.

Load `software-contract` and read
`~/.agents/skills/software-contract/references/coding-quality-contract.md`.

Use the coding-quality contract to make a focused judgment about whether the
implementation realizes the authorized purpose within its boundary. Consider
the affected workflow and relevant system, data, and trust risks; do not turn
that judgment into a standing ledger, atomic-probe checklist, or prerequisite
packet.

Verification supports the material claims of the change. Select the smallest
direct check that can expose a meaningful failure, and return a blocker or
residual risk when that check cannot be run. Explicit deep or exhaustive review
remains the responsibility of the `review` skill.
