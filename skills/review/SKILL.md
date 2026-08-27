---
name: review
description: >
  Independent, read-only judgment of whether an object is what it needs to be
  and sufficiently realizes its purpose. Use when the user's actual intent is to
  understand or judge an existing codebase, product, document, skill,
  configuration, plan, workflow, release, or handoff, including its risks,
  quality, completeness, or room to become better. Do not select from a review
  keyword when the primary intent is authorized change. Review-only: do not edit,
  rewrite, commit, deploy, sync, or optimize.
---

# Review

Review is an independent judgment: whether an object is what it needs to be,
and whether it sufficiently realizes the purpose it serves in its concrete
situation. It remains read-only so that judgment is not bent toward defending a
change already made or a solution already preferred.

## Orientation

Start from the whole: the user's purpose, the object, the people and systems it
relates to, and the stakes of success or failure. Then identify the relations
that govern whether the object can fulfill that purpose, including its dominant
tension or contradiction. Return to the concrete with a judgment that can be
corrected by reality.

- The user's present purpose and explicit boundaries direct the inquiry. They
  may be clarified or challenged in dialogue, never silently replaced.
- Code, documents, tests, conventions, and prior reports are material to
  inspect, not authorities that prove themselves.
- Evidence matters when it could alter the judgment. Its volume, or a complete
  process record, never substitutes for understanding.
- Methods serve sustained attention to the object and the relations that matter.
- A favorable judgment is bounded by the concrete situation and reviewed scope;
  it remains open to later correction.

## Contract

Use this skill for a review-only request concerning an existing target. Do not
repair it or draft a replacement. When the judgment exposes a limitation,
explain its action meaning; choosing and organizing a solution belongs to
`optimize`, `discovery`, or the appropriate implementation owner.

Establish enough of the following to make a real judgment:

- the object and the completion claim under review;
- its purpose, audience, constraints, and concrete situation;
- the relationships that enable or prevent that purpose;
- the central tension, if one governs the result;
- the scope, depth, and meaningful stop line.

Ask only when the user's perspective is not responsibly substitutable and could
materially change the object's meaning, governing standard, boundary, or
judgment. Inspectable facts and professional judgment remain Codex's work.
Otherwise state a narrow assumption when necessary and proceed.

When invoked through `project-lifecycle`, use its accepted goal, boundary, and
handoff as context, while retaining independent judgment. Do not create a
second project goal or mutate lifecycle state.

## Conditional References

- For a software repository, product, project skill/configuration, release, or
  post-implementation review, read `references/software-project-review.md`.
- For explicit deep, exhaustive, 全面, 穷尽, 逐词逐句, or repeated review, read
  `references/deep-review.md`.
- Read both when both apply. The software reference routes project-specific
  reality; the deep reference governs the intensity of inquiry.

Do not load these references for an ordinary, focused non-project review.

## Inquiry

Move in the order the object requires, not a fixed framework order:

1. Understand what this object is meant to be and why it matters now.
2. Inspect the direct object and the relations that could change that answer:
   callers and consumers, behavior and failure paths, state and boundaries,
   tests and operational conditions, or, for explanatory work, reasoning,
   reader reconstruction, assumptions, and consequences.
3. Seek the governing limitation and the strongest countercase. Use targeted
   checks, comparisons, scenarios, or direct observation only where they could
   confirm, qualify, or overturn the emerging judgment.
4. Make one coherent overall judgment before fragmenting it into findings.

Possible surfaces include security, privacy, permissions, data handling,
documentation, user experience, release conditions, and maintainability. Select
only those that matter to the object's purpose and concrete relations. For a
skill or configuration, inspect its trigger, boundaries, call chain, context
cost, and pressure behavior when they bear on its actual function.

For explanatory artifacts, ask whether the intended reader can reconstruct the
problem, conclusion, decisive reasons, limits, and practical next move without
having to read review machinery.

## Findings And Action Meaning

Report only material limitations: a relation, contradiction, or absence that
prevents the object from being what it needs to be or from adequately serving
its purpose. State the observed basis, causal consequence, affected scope, and
what kind of action is now called for. Separate fact from inference where that
distinction matters.

For code, security, operations, and release reviews, findings lead and use
severity to communicate remediation urgency:

- `P0`: active catastrophic harm, destructive corruption, or critical security
  compromise.
- `P1`: release blocker, core-workflow failure, severe security/data/privacy
  risk, or direction-changing defect.
- `P2`: material correctness, maintainability, UX, documentation, operational,
  or control weakness.
- `P3`: bounded low-impact issue worth addressing.

Severity orders defects; it does not measure the object's worth or turn every
possible improvement into a defect. Consolidate symptoms with one cause unless
they require different action.

When asked about improvement space, judge whether the current relations limit
the stated purpose and explain the practical implication. Keep the result at the
level of independent judgment. Where a different direction is needed, identify
the question that `optimize` or `discovery` must take up.

## Output

For code and operational reviews, present material findings first, ordered
`P0` through `P3`; then give the concise overall judgment and any necessary
assumption or unresolved question. For documents, prompts, plans, and other
explanatory artifacts, begin with a short core judgment and its decisive
reason, then findings.

Name scope and depth when useful for interpreting the conclusion. Mention
verification only when it bears on the judgment. Disclose an unexamined surface
only when it is a substantive limit on what can be concluded. Keep the result
concise and directed toward the user's next practical decision.
