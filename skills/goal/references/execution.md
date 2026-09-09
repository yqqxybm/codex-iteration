# Goal Execution

The main thread keeps one whole-request responsibility while domain owners
carry out bounded work. Use the existing plan and state mechanisms of the task;
this reference does not create a second project controller.

## Native Goal State

Inspect `get_goal` before activation, when resuming or reconciling an active
goal, and before any status transition. Create a goal only when explicitly
requested and the live tool permits it. Reuse an unfinished goal for the same
commission rather than creating a duplicate. Use the synthesized prompt from
`goal/SKILL.md`; do not replace it with a title. Do not invent a token budget.

Respect the live tool's actual operations. The current `update_goal` changes
completion or blocked status, not objective text, budget, or pause state.
Within the same commission, carry a corrected interpretation and revised plan
in current task state, grounded in the user's latest instructions. Do not claim
the stored objective was rewritten. If a genuinely different commission
conflicts with an unfinished goal, disclose the conflict and resolve it with
the user through available controls; never mark unfinished work complete to
make a replacement goal possible. The prior goal text cannot override the
user's current explicit instruction.

If the tool is unavailable, disclose that native goal activation is unavailable
and continue authorized work through the task's existing plan when possible.
Do not claim a native continuation loop exists. A final response without an
active continuation mechanism cannot promise unattended work after this turn.

## Plan And Allocate

Turn the next accepted commitment into ready work, preserving the whole
commission in the goal even when later stages cannot yet be specified. Prefer
the current plan, issue list, or conversation; use a durable file only when the
user requested it or interruption/recovery actually needs it. Software uses
lifecycle's selected plan sink. Other work does not acquire a software docs
tree, release checklist, or trace just to appear organized.

Keep enough state to recover the accepted outcome and quality judgment, current
approach, actionable work, dependencies, ownership, status, meaningful results,
verification where needed, unresolved decisions, and the next action. Store
each fact once in its useful home and reference it elsewhere. A result or item
status without the judgment needed to resume it is incomplete recovery state.

Prioritize by contribution to the requested outcome and dependencies. Inspect
available capabilities and reuse suitable work before building another tool.
Use independent parallel reads and disjoint writes whenever they improve total
completion time or quality; reassess opportunities as work changes. A concrete
dependency, conflict, coordination cost, capacity, or tool restriction can
justify serial execution, not habit or absence of an explicit parallel request.

For delegation, read
`~/.agents/skills/project-lifecycle/references/subagent-execution.md` as the
shared native dispatch protocol. Reading that resource does not invoke the
software lifecycle. Reuse its model/effort selection, assignment, receipt, join,
and persistence decision instead of inventing another scheduler. Non-software
writers use `analysis_consumed` with the actual accepted inquiry and boundary;
software writers retain their project analysis gate. Do not replay root
analysis or create nested goals for each child.

Give each child the relevant purpose, quality judgment, accepted constraints,
and what its result must establish for the whole, as well as its bounded task.
The child need not receive the entire goal prompt or every review direction.
The parent judges whether the joined results advance the whole commission;
individually successful receipts do not establish overall success.

## Advance And Reconsider

After an accepted result, update the existing work state and take the next
ready action. A stage handoff returns control to the main thread, not to the
user merely because that stage has finished. Continue through later requested
stages once their prerequisites exist. Track actual processes and wait on live
handles; a promise to continue is not a running process.

At meaningful changes, judge whether current work still serves the purpose.
Keep the course when its basis holds; revise the means when a better route
becomes apparent. Use `reorient` when that relationship materially breaks or
becomes obscure, and honor its explicit `继续！` account. Its reassessment
does not automatically authorize a different outcome or reopen unrelated work.

When user input arrives, preserve recoverable work, understand the input, then
reconcile the plan before further affected action. Distinguish a new commitment
from correction of a mistaken interpretation. Retain unaffected work and
invalidate only results dependent on the rejected judgment. Domain owners
apply their own state transitions; do not turn every correction into a durable
rule or a new document. Explain material direction changes and the next action
without repeating the entire plan.

Select checks for the consequence that could correct the judgment, not for
their availability or a universal baseline ritual. A failed check may require
repair, changed verification, or renewed inquiry; classify the cause before
acting. Inspect command outcomes before any completion call. Naming uncertainty
does not discharge necessary investigation that can still be performed.

## Finish Or Remain Open

Judge completion against the user's current commission and its material
qualities, not solely the generated goal, plan, current artifacts, or tests.
Required work, unresolved substantive findings, unaccepted child results,
necessary verification, and authorized delivery must be resolved. A research
report must answer its research question; a product delivery must function as
promised; neither inherits the other's completion test.

Apply any requested loop's real stopping condition. Review counts, subagent
waves, tests, commits, publication, or sync cannot substitute for each other or
for the result. Do not turn future opportunities into endless obligations, or
relabel current required work as optional to make the goal complete.

Call `update_goal(status="complete")` only when the full commission is actually
achieved. A stage alone may close the goal only when the user commissioned that
stage alone. Keep a known multi-stage request active through all requested
stages, even when the stored objective was mistakenly narrowed to one stage;
carry the corrected commission in current task state as above. Report final
token usage only when the user set a token budget.

A missing user decision or external dependency can block one branch while
independent authorized work continues. Ask the concrete necessary question;
do not repeat unproductive checks. Mark the goal `blocked` only under the live
tool's threshold: the same genuine impasse on at least three consecutive goal
turns, with no meaningful progress possible without external change or user
input. A resumed blocked goal starts a fresh audit. Otherwise retain the active
goal and recoverable state. Never confuse blockage, an observation timeout,
an interrupted turn, or inability to alter the stored prompt with achievement.

At closeout, account for children and task-created runtime resources through
their owners. Keep intended deliverables such as a running preview available;
close obsolete temporary work, not the user's existing services or sessions.
Report what was achieved, what that establishes, material limits, and remaining
work or the exact blocker. Partial progress may be useful without being final.
