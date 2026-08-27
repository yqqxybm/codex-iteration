# Practical Software Quality Contract

Use this reference when implementation, review, or optimization needs a shared
standard for judging a software project. Its purpose is not to manufacture
coverage or proof. It helps the work understand what this project is trying to
make possible, what is presently preventing that, and what proportionate action
would improve the real situation.

## Starting Point

Begin with the concrete whole: the user's purpose and stakes, the people and
work it serves, the existing project and its history, and the constraints that
actually bind. Let the investigation move from that whole toward the governing
tension, then return to a practical judgment that can be corrected by results.

The lifecycle goal and agenda own the stated objective, boundary, and continuity.
Its trace and ordinary Handoffs carry useful context between stages. This
contract creates no separate truth store, ledger, or completion machinery.

A quality judgment is worthwhile when it can change what should be done, what
must be preserved, or whether the result is adequate for its purpose. Evidence
is a means of learning and testing that judgment. It must be sufficient for the
stakes and uncertainty, not accumulated as a ritual or treated as the object of
the work.

## Relations Worth Considering

There is no fixed matrix, mandatory role roster, or universal list of checks.
Choose the relations that could alter the whole judgment for this object and
purpose. They may include:

- behavior, user workflows, product value, scope, and unwanted complexity;
- code, logic, architecture, state, data, integrations, and failure handling;
- UI, interaction, accessibility, responsiveness, content, and realistic use;
- security, privacy, authority, retention, compliance, and irreversible harm;
- tests, runtime behavior, performance, reliability, release, and recovery;
- documentation, operability, maintainability, compatibility, and evolution.

These are directions for inquiry, not boxes to tick. A relation matters only
when it bears on the project's purpose, contradiction, constraints, or likely
consequences. A narrow change follows the few relations that can change its
outcome. A broad review follows every relation that could materially change the
overall judgment, including project-specific ones not named above; it does not
turn every noun into a separate question or demand an explicit dismissal of
everything else.

## Review And Optimization

Review asks whether the current object adequately realizes its purpose and
where a material contradiction, risk, or loss of coherence remains. Optimization
asks a prior question: whether there is a formed object whose present condition
prevents it from serving that purpose better, and whether a change is genuinely
called for. Neither should be selected from wording alone.

For either, form a concise working understanding: intended outcome, current
reality, governing tension, relevant constraints and preservation commitments,
and the practical alternatives. Inspect code, behavior, user experience, data,
tests, documents, runtime signals, and human/domain authority only as needed to
test that understanding. State uncertainty plainly when it cannot be resolved.

An improvement is not justified because it is novel, comprehensive, or easily
measured. It needs a credible expectation of better realization of the purpose,
after considering disruption, added complexity, cost, risk, and what must remain
intact. A real issue remains a real issue even when it is not presently feasible
to repair; feasibility changes the action, not the judgment.

## Proportionate Realization

Avoid overbuilding: do not add features, abstractions, dependencies,
configuration, documentation, or process that the purpose and situation do not
need. Prefer existing coherent behavior and platform capability when they serve
the work well.

This is a demand for proportionate sufficient realization, not a mechanical
command to write the least code. Build enough to preserve requested behavior,
clarity, accessibility, data integrity, trust boundaries, safety, and the
verification warranted by the consequence of being wrong. A smaller change that
leaves the governing problem untouched is not restrained; it is incomplete.

## Handoff

Carry forward the current understanding, the judgment reached, what was changed
or found, the verification that matters, unresolved risks, and the next
practical question in a normal Handoff. Keep it concise and tied to the object;
do not create parallel state merely to demonstrate process.
