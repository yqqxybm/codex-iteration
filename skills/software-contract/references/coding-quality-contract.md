# Coding Quality Contract

Use this reference from `project-iteration` or `review` when
`standard_compliance_ledger` is present or when a change touches a
standard-sensitive coding area.

Evaluate only applicable items. A small diff does not need a long checklist, but
any applicable standard item must be satisfied, marked not applicable, or
returned as missing/blocking work with evidence.

## Coding Concerns

- error handling and user/developer error separation,
- input validation and trust boundaries,
- configuration, secrets, hosts, paths, and timeouts,
- resource lifecycle and cleanup on failure paths,
- concurrency, cancellation, retry, and idempotency,
- structured logging, metrics, trace context, and sensitive-data redaction,
- security, query/output escaping, and dependency risk,
- interface compatibility and deprecation path,
- testability, dependency isolation, time/random/IO substitution,
- performance measurement points for critical paths.
