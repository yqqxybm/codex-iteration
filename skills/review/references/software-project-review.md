# Software Project Review

Use this reference for repositories, products, project skills, configuration,
releases, and post-implementation project work. It adapts review to software
reality; it does not impose a second quality framework.

## Judgment

Begin with the object in its concrete situation: what the project is for, whose
work or life it changes, what has been promised, what has actually been made,
and what conditions now govern its success or failure. Read the relevant
history, implementation, affected workflow, and consequences together before
classifying defects.

Form an independent judgment about whether the object realizes its purpose and
what contradiction most governs the answer. Do not turn ordinary review into
fixed judgment axes, an opportunity hunt, or a checklist whose
completion substitutes for understanding. A named diff, file, issue, or
workflow remains focused; whole-project language broadens the situation to the
degree needed for a sound judgment, not by default to exhaustive inspection.

Where the project object or the form through which it should realize the
accepted purpose is genuinely unresolved, say so plainly and route the question
to `project-lifecycle`, which may select `project-discovery` or `project-brief`.
An implementation defect cannot settle that upstream question.

## Material Directions

Choose only directions that can alter the judgment, completion claim, or next
action. Depending on the object, this may include code and functional behavior;
system logic and boundaries; data integrity and lifecycle; UI/UX, accessibility,
and responsive states; documentation and handoff truth; security and privacy;
tests and realistic verification; and release, operations, observability,
rollback, or maintainability. Complexity matters when it obscures responsibility
or makes the purpose harder to sustain: favor deletion, local patterns, native
capability, and smaller truthful abstractions when they preserve the object.

Inspect the source, runtime, user-facing, operational, and historical reality
capable of confirming or correcting the governing claim. Treat stale docs,
fixtures, or tests as claims to examine when they conflict with the expressed
purpose or lived behavior.

Load `software-contract` and the relevant specialized resource only when its
domain is material. Use the coding-quality contract for engineering judgment;
the standard-development and docs-deliverables contracts for requested
standards; and applicable frontend quality, design, taste, prototype/reference,
or motion contracts for visible UI. These resources sharpen judgment; they do
not manufacture requirements or displace the object's own structure.

## Result

State the judgment, the purpose and governing contradiction from which it
follows, material findings, the reasoning or evidence that bears on them,
and what should happen next. Distinguish a defect in the present object from an
unsettled upstream question. Keep uncertainty, verification gaps, and residual
risk visible when they materially limit confidence. Review does not implement,
invent a new product direction, or create lifecycle state.
