# Software Project Optimization

Use this reference for a software repository, product, project artifact, skill,
configuration, release process, or frontend system only after understanding
what the object is for and what prevents it from fulfilling that purpose.

## First Decide Whether There Is An Object To Optimize

Optimization is not selected by the word "optimize" or by the presence of
content that sounds improvable. Ask whether there is an actual, sufficiently
formed object: an accepted purpose, a concrete situation, and an accepted form
or relation through which the project is meant to realize that purpose.
Acceptance of the purpose alone does not make the inherited implementation or
product shape the optimization object.

If the object or the relation through which it should realize its accepted
purpose is still unsettled enough to change the project commitment, return it to
`project-lifecycle`. The lifecycle may choose `project-discovery` or
`project-brief`; optimization cannot settle that prior question by polishing the
current contents.

## Optimize A Formed Object

For a formed object, identify the purpose, its relationship to the surrounding
project, and the contradiction that most prevents its realization. Improve that
relation rather than maximizing isolated qualities or accumulating generic
"improvements." A simpler, truer change may be to remove behavior, replace a
wrong mechanism, reuse an established pattern or native capability, or return a
detail to its real owner. Add a new control, abstraction, document, test, or
compatibility path only when it is genuinely needed to resolve the material
failure.

Select the owner that can change the governing cause: `project-analysis` for
architecture, root cause, and direction-bearing technical decisions;
`project-refine` for project-facing writing; `project-iteration` or
`project-bootstrap` for implementation; `project-frontend` for design;
`project-docs` for durable knowledge; and `project-release`, `project-sync`, or
`project-commit` for their operational boundaries. `project-lifecycle` keeps
the project-level relation coherent; generic optimize wording does not bypass
the owner, verification, or commit boundary.

Use `software-contract` and only the coding, standards, documentation, or
frontend resource that materially constrains the change. Evidence and
verification are proportionate to the risk and claim: enough to show that the
chosen change serves its purpose and has not damaged what must be preserved,
but never a separate product of the work.

## Handoff

The implementing owner carries out and verifies the change under its own
contract. Report the purpose, governing contradiction, chosen change and why it
fits the whole, verification that matters, and remaining limits or questions.
Optimization neither replaces lifecycle judgment nor closes lifecycle state.
