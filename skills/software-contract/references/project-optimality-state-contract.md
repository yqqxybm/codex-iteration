# Project Optimality State Contract

Load this reference after `coding-quality-contract.md` only when a lifecycle
must preserve project-optimality evidence across phases, agents, resumable work,
broad review/optimization, or concurrent mutation. An ordinary bounded change
may keep its scoped probes ephemeral and does not create this state solely for
ceremony.

## Packet

```yaml
project_optimality_packet:
  id: <stable opaque id>
  revision: <monotonic integer>
  project_model: <model defined by coding-quality-contract.md>
  concerns:
    - id: <stable id>
      question: <project-specific unresolved tension>
      basis:
        model_paths: <relevant project_model fields>
        discovery_sources: <domain seeds, responsibility positions, user, or evidence>
        evidence_ids: <supporting evidence or none while pending>
      applicability: <pending | applicable | not_applicable>
      decision_impact: <completion, decision, risk acceptance, or stop condition>
  probes:
    - id: <stable id>
      concern_ids: <one or more concern ids>
      question: <one falsifiable question>
      pass_when: <observable condition>
      evidence_surface: <what must be inspected>
      state: <pending | passed | failed | not_applicable>
      evidence_ids: <immutable evidence ids or none while pending>
      residual_risk: <none | concrete remaining risk>
  evidence:
    - id: <stable append-only id>
      source: <file, command, behavior, artifact, telemetry, or human answer>
      observation: <actual result>
      observed_against: <commit, diff, artifact version, runtime, or time identity>
      introduced_by: <delta id>
  human_decisions:
    - id: <stable id>
      state: <pending | resolved>
      question: <exact legal, policy, risk, or sensitive-disclosure decision>
      authority: <qualified owner and why machine evidence cannot decide it>
      affects: <probe ids, model paths, or completion claims>
      evidence_id: <resolved answer evidence or none>
```

Findings, perspective views, discovery coverage, and completion claims are
derived from this packet, not independently mergeable state. A failed probe id is
the stable finding key; its concern defines the issue and its current evidence
supports the state. `perspective_model` is only a readable projection.
`project_model` records the lifecycle's current evidence-backed understanding of
authoritative user/lifecycle intent; it does not own or silently rewrite the
objective or `optimality_law`.

## Reference And Delta

Only `project-lifecycle` initializes the authoritative packet, merges changes,
and increments `revision`.
An owner skill that is not a declared delta producer returns its normal Handoff
evidence; the controller converts any model, evidence-surface, probe, or human
decision effect into a lifecycle-produced delta before merge or clean counting.

```yaml
project_optimality_ref:
  packet_id: <packet id>
  revision: <exact revision>
  location: <trace path#heading containing exactly one fenced YAML packet block>
  content_hash: <sha256 of the exact UTF-8 LF bytes inside that block, excluding fences>
  assigned_probe_ids: <bounded ids or all>
```

Use a reference only when the recipient can read the exact location and verify
the revision/hash. Otherwise inline the full revisioned packet for a broad
consumer, or this complete bounded projection; never substitute
`perspective_model`:

```yaml
project_optimality_projection:
  packet_id: <packet id>
  base_revision: <exact revision>
  claim_boundary: <owned completion claim>
  concerns: <assigned concerns with basis and applicability>
  probes: <assigned probes with state and evidence ids>
  evidence: <records referenced by assigned concerns/probes>
  human_decisions: <decisions affecting the assigned claim>
```

```yaml
project_optimality_delta:
  id: <idempotency id>
  packet_id: <packet id>
  base_revision: <revision inspected by producer>
  producer: <goal | lifecycle | analysis | review | optimize | implementation | refine>
  assigned_probe_ids: <bounded ids or all>
  model_patch:
    - path: <project_model path>
      previous: <value at base_revision>
      next: <proposed value>
  concern_updates:
    - id: <concern id>
      operation: <put | set_applicability>
      previous_applicability: <absent | pending | applicable | not_applicable>
      next_applicability: <pending | applicable | not_applicable>
      definition: <full definition when put, otherwise unchanged>
      evidence_ids_added: <ids or none>
  probe_updates:
    - id: <probe id>
      operation: <put>
      definition: <concern ids, question, pass condition, evidence surface, and residual-risk shape; no mutable state/evidence>
  probe_transitions:
    - id: <probe id>
      previous_state: <absent | pending | passed | failed | not_applicable>
      next_state: <pending | passed | failed | not_applicable>
      evidence_ids_added: <ids or none>
  evidence_additions: <append-only evidence records or none>
  human_decision_updates:
    - id: <decision id>
      operation: <request | resolve>
      previous_state: <absent | pending>
      next_state: <pending | resolved>
      record: <full request or answer evidence id>
  invalidated_probe_ids: <ids whose evidence surface changed, or none>
```

Do not delete semantic history. When a concern or probe becomes irrelevant,
transition it to evidence-backed `not_applicable`.
Every new probe `put` must include an `absent` transition. It starts `pending`
when unevaluated; an initial terminal state requires newly appended current
evidence.

Treat an identical delta id and payload as an idempotent replay; do not apply it
twice. Reject the same delta id with different content. Evidence ids are unique
packet-wide; an existing id is a no-op only for the identical record from the
same delta, otherwise reject the whole delta. A stale-base delta may merge only
when every touched model path, concern, probe, evidence id, and human decision
is unchanged since `base_revision`; otherwise rebase or replan it. Evidence is
append-only. Evidence records and projections must not contain credentials,
tokens, private session contents, or unnecessary sensitive raw data; store a
concise redacted observation and a protected path/hash/source reference instead
of copying large logs or artifacts. Any mutation
that can change a probe answer invalidates that probe and resets affected
clean-pass state. Invalidation and fresh reevaluation may share one delta only
with new post-mutation evidence; the reset still applies.
Derive invalidation as an evidence-backed impact closure, not from a fixed
quality-dimension order. Start from changed model paths, artifacts, contracts,
schemas, configuration, runtime identities, and probe evidence surfaces; follow
only named call, data, state, or dependency paths that can change a `pass_when`.
Include every directly or transitively affected probe in
`invalidated_probe_ids`. Shared domain tags alone do not prove dependency, and
tests or documents are not universally downstream. If impact reachability cannot
be resolved, keep the affected probe `pending` or return the missing dependency
as `new_work` rather than preserving stale `passed` evidence.
Reject a delta unless every `invalidated_probe_id` either transitions to
`pending` or reaches a terminal state with newly appended evidence observed
against the post-mutation identity.

Bounded recipients may evaluate only assigned probes and cannot change global
concern applicability. They return any newly discovered, unassigned
concern, probe, or human decision as Handoff `new_work` for lifecycle insertion
rather than silently expanding their delta. For subagents, assigned probe ids
are conflict keys and each receipt must account for every assigned probe.

## Derived Predicates

- **Evidence coverage complete**: every concern inside the declared claim has
  evidenced `applicable` or `not_applicable` status, every applicable concern
  maps to a required probe, and every required probe has current evidence and is
  not `pending`.
- **Review report converged**: two required passes find no new finding, evidence
  gap, severity error, duplicate, or report defect; known findings may remain in
  a review-only report.
- **Project completion eligible**: `Evidence coverage complete` is true, no
  required probe is `failed`, no pending human decision affects the claim, and
  lifecycle stop conditions are satisfied.

Targeted post-mutation reevaluation may close the invalidated impact closure
during remediation. It does not count as a project-global deep/exhaustive clean
pass unless that same pass covers the full declared completion claim. Final
convergence requires current evidence for every required probe after the last
mutation.

`applicable` and `not_applicable` concerns require basis evidence. `passed`,
`failed`, and `not_applicable` probes require evidence observed against the
relevant artifact/runtime state. A pending human decision blocks only its
`affects` targets; machine-inspectable concerns still need separate probes.
Resolve it only in the same delta that appends the answer evidence and applies
resulting model changes or probe invalidation.
