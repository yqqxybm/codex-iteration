---
name: goal
description: >
  Turn an explicit goal request into a fitting objective and carry it through
  to completion. Use when a message starts with 目标！ or 目标!, the user invokes
  this skill, or explicitly asks to create or pursue a Codex goal. Applies to
  research, decisions, writing, career or business work, software, and mixed
  tasks. Discussion or quotation of the trigger does not activate a goal.
---

# Goal

A goal gives a user's purpose practical form in a concrete situation. It is
neither a transcript of the first request nor a checklist of available actions.
Codex is entrusted to understand what result would adequately serve the request,
choose and organize the means, and remain responsible for the unfinished work.
Plans, tools, intermediate artifacts, and completion checks serve that judgment;
their own closure cannot establish that the request has been fulfilled.

## Entry And Ownership

Use the current request and its context to identify the commissioned outcome.
The wider purpose explains its value; it does not authorize a different task.
An explicit small goal stays small. Ordinary work may use a plan and continue
autonomously without creating a native goal; invoke the goal tool only under
its live authorization contract.

The main thread owns the whole goal and its completion. Domain owners carry
out the work under their existing contracts. Software work enters
`project-lifecycle`, which reads its `references/goal-orchestration.md` as the
software adapter. Non-software work does not enter the software lifecycle merely
because it uses files, scripts, agents, research, or a goal. Mixed work crosses
that boundary only for the software commitment it actually contains.

These are responsibilities within the same task, not a recursive invocation
chain or a reason to create another session, goal, scheduler, or plan.

## Form A Fitting Goal

Read the relevant request, current work, and governing context before choosing
a workflow. For a consequential non-software judgment, use
`three-step-analysis`; for software, let lifecycle select `project-analysis`
or the earlier unresolved owner. Carry forward a judgment already formed in
this task rather than replay it when skills change. Explicit three-step analysis
retains its original stages and dialogue gate before activation or execution.

Understand the concrete situation far enough to determine what should be
accomplished, not merely what can be produced. Relate the user's purpose to
the people, needs, history, alternatives, constraints, and consequences that
make this particular work worthwhile. Expand plausible interpretations and
approaches before choosing; let a serious alternative or counterexample test
the leading judgment.

Derive quality questions and standards from those relations. For broad work,
follow every relation capable of changing the overall judgment, including
unrealized possibilities beyond present defects. Affected users, substitute
choices, coherent design, practical utility, sustainability, and the user's
attention can matter; they are sources of questions, not a mandatory role list.
Explain what a selected perspective could reveal and how that would change the
work. Do not narrow the investigation to whichever facts are easiest to count.

Determine what a better result means for this object and what must remain
intact. Elegance is coherent and proportionate realization of the purpose,
not minimum length, maximum novelty, or maximum process coverage. Concrete
quality judgments need not be numeric; evidence should challenge them rather
than substitute for them. Resolve a priority only when values actually conflict.

Bring the emerging judgment into dialogue when the user's experience, purpose,
values, or commitment would materially change it. Generate and assess a real
candidate question before activation; do not make the user supply viewpoints,
skill choices, a plan, loop mechanics, or prompt wording that Codex can derive.
Follow the cognitive owner's question rules and current tool contract. When no
dialogue is needed, make the basis clear through the explanation of the goal.

Uncertainty about the solution calls for inquiry, not an invented solution or
an indefinitely postponed goal. A clear request to investigate and then act
can have a whole-request goal whose first commitment is inquiry. Preserve the
later requested outcome without inventing downstream requirements or executable
nodes before that inquiry establishes them. A separately commissioned research
or planning task ends with its adequate research or plan, not an unrequested
implementation, application, sale, or other external result.

## Write And Explain The Actual Goal

Synthesize a compact, self-contained prompt for `create_goal.objective` from
the judgment. It must carry what will direct future decisions, not only what
will make a checklist closable:

- the requested outcome, whom or what it serves, and its authorized boundary;
- the task-specific quality standard, decisive questions, and value to preserve;
- the working approach and why it can achieve that outcome, including the next
  inquiry when a solution or commitment remains unsettled;
- the work and feedback that require continuation, and conditions for revising
  the approach or returning to dialogue;
- the actual completion condition, material verification, and authorized delivery.

Express this as clear prose at the scale the task needs, not a form with empty
fields. A tiny goal may fit in a short paragraph. A complex goal must not lose
its substantive quality judgment during compression. Keep detailed task nodes,
attempts, and progress in the live plan rather than freezing them in the prompt.

Choose the continuation policy from the work: a bounded change needs completion
and a proportional check; an uncertain task needs inquiry and reassessment; a
multi-stage result needs advancement through all requested stages; cyclic
improvement needs search, change, and renewed whole-object judgment. More than
one may be needed, but each serves a distinct question and stop condition.
Put the chosen loop, what restarts it, and its stopping condition in the actual
goal prompt, not only in a side note. For explicit cyclic review or optimization,
read [cyclic-improvement.md](references/cyclic-improvement.md).

Before activating the goal, briefly explain the intended result, quality bar,
main approach, and next commitment so the user can understand and correct the
course. Reuse what was already explained; do not expose internal schemas or
repeat the same judgment at each handoff. This explanation does not manufacture
a new approval gate when the necessary judgment and authorization already exist.

Test the proposed goal against the original request: could everything in this
prompt be satisfied while the user's commissioned result remains unmet? Would
it instead require something the user never commissioned? Revise either mismatch
before activation. A well-formed goal is a revisable practical judgment, not
proof that its interpretation is correct.

## Organize And Continue

Read [execution.md](references/execution.md) before activating, maintaining,
delegating, recovering, or closing a goal. It owns the generic execution and
native-tool boundary; the software adapter owns software-specific state and
delivery. Select available skills, tools, and resources for the current work,
not from a prefilled chain. Research, explanatory writing, optimization, code,
review, and publishing each retain the standards of the result they must produce.

Use `review` for independent judgment, `optimize` for authorized improvement,
and the appropriate domain or artifact owner for action. Do not reduce
optimization to fixing review findings or let review dictate every artifact's
form. Shared understanding may pass between stages; accepted stages need not be
repeated merely to demonstrate skill use.

The goal is complete when the commissioned result adequately serves its purpose
within the agreed boundary, the necessary checks and delivery are satisfied,
and no required work remains. A useful intermediate result, exhausted method,
or real blocker is not the same as completion. Further imaginable work is not
automatically part of the commission. Report the achieved result and the limits
that matter, not a record of how many procedures ran.
