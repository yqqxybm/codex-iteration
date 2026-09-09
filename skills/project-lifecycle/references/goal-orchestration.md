# Goal Integration For Software Projects

Use this software-only adapter when an explicit goal is a software-project
commission. Read `~/.agents/skills/goal/SKILL.md` as the universal owner and
this reference as `project-lifecycle`'s domain contribution.

## Ownership Boundary

- `goal` owns explicit goal activation, current native goal-tool state, the
  whole-commission synthesis, quality and strategy, goal-level loops, and the
  final completion or blocked judgment.
- `project-lifecycle` remains the sole entry and phase owner for software work.
  It owns software inquiry routing, accepted project state, the software agenda,
  downstream owner selection, execution, verification, delivery facts, and
  software state transitions.
- The same main thread enacts both skills. Do not call them recursively, create
  a second root analysis, duplicate the goal, or run a parallel scheduler.
- A non-software goal never activates `project-lifecycle`. An ordinary software
  request without an explicit goal request does not activate a native goal;
  plans and agendas still continue normally.
- Only `goal` may use `get_goal`, `create_goal`, or `update_goal` for this
  commission. `create_goal` is permitted only for an explicit user request.
  The current `update_goal` surface can complete or block a goal but cannot edit
  its objective: never fake completion to replace an active objective.

## Software Contribution

Give `goal` the smallest software judgment needed to direct the whole request:

- the user's full requested software outcome and why it matters,
- the accepted software target, task-specific quality bar, success evidence,
  and any project-specific preservation commitments,
- explicit scope limits, forbidden mutations, and non-goals,
- the earliest unresolved software phase and accepted analysis, discovery,
  brief, charter, version, release, or sync state,
- the original Stage 2 dialogue state when three-step analysis is active,
- requested review depth and scope, controlling work sources, and readiness
  evidence,
- delivery authorization for commit, push, sync, and deploy,
- reversal conditions or unresolved user decisions that could change the
  software commitment.

Do not restate universal goal schemas or invent another optimality law, state
machine, ledger, or completion mechanism. The software judgment can refine the
goal's strategy, but it cannot silently widen or replace the user's commission.

If discovery, brief formation, or analysis must come first, keep the full user
outcome open in the goal. The initial software agenda contains only the inquiry
work and its controller-owned adoption or acceptance gate. Materialize later
implementation, test, documentation, release, and delivery items only after the
gate makes them meaningful. Completing the inquiry is not completing the
commission.

When the user explicitly requested three-step analysis, preserve the original
visible sequence and exact Stage 2 question. Wait for the user's answer before
Stage 3 or execution. Goal synthesis must consume that dialogue; it must not
rerun, compress, or answer the dialogue on the user's behalf.

## Same-Thread Flow

1. Recognize an explicit goal through the universal `goal` contract and decide
   whether its object is software.
2. For software, keep `project-lifecycle` active in the same main thread and
   load this adapter. For non-software, do not enter the software lifecycle.
3. Reuse accepted project inquiry and state. Locate only the earliest unresolved
   software commitment; do not repeat a completed root analysis.
4. Return the software contribution above to `goal` for whole-commission
   synthesis and any explicit native goal activation.
5. Let `project-lifecycle` build and advance the software agenda through its
   existing controller protocol, state transitions, downstream owners, and
   verification gates.
6. Feed ordinary Handoffs and decisive software evidence back to the same main
   thread. `goal` judges how that result changes whole-commission strategy,
   loops, and completion; the lifecycle applies only software state changes.

## Agenda And Context

The live software agenda must preserve both its current executable boundary and
continuity with the full request. It records source, status, result, and
verification for accepted software work; it does not become a second goal.

Reuse the existing Context Packet and Handoff Record. Include task-specific
purpose and quality only when a downstream decision depends on them. Do not add
a goal packet, goal ledger, lifecycle mirror, or new state schema.

Keep explicit narrow boundaries narrow, including for a tiny goal. A `目标!` /
`目标！` marker changes ownership and continuity, not scope, review depth, or
analysis-waiver status. Preserve any user instruction not to parallelize as
`parallel_blocker: user_explicit_no_parallel`; the goal contract cannot weaken
that preference. Otherwise, software task graphs and delegation remain governed
only by `references/subagent-execution.md`.

Research-then-implementation work begins with discovery and adoption only, but
the goal remains the full research-and-delivery commission. A `v0.1` goal keeps
the frozen charter, controlling plan, readiness source, and version agenda; it
is never reduced to one local iteration.

## Review And Improvement

Preserve the review depth and scope the user requested. Ordinary implementation
gets the lifecycle's focused closeout review; do not relabel it deep or global.
Independent deep or exhaustive review still belongs to `review` and remains
bounded by the software target and explicit mutation limits.

For an explicitly cyclic deep-review or optimization goal, load
`~/.agents/skills/goal/references/cyclic-improvement.md`. That universal
reference owns the improvement loop and its default of two consecutive clean
reviews. Do not copy its loop state here, infer that default for ordinary goals,
or count verification, a focused closeout, a commit, or a downstream Handoff as
an independent clean review.

## Delivery Policy

- Commit deliverable source, documentation, or configuration changes when the
  project is Git-managed, subject to the lifecycle's focused commit rules.
- Push only when the user or an already accepted delivery contract authorizes
  remote delivery.
- Sync relevant machines when they are already covered by standing user
  authorization and the software target includes that shared behavior.
- Deploy only when actual delivery requires a real deploy target and health
  evidence. A website, app, version label, or completeness claim alone does not
  authorize deployment.

Record delivery results in the existing agenda/Handoff surfaces. They are software
evidence for `goal`, not proof of whole-commission completion by themselves.

## State And Completion

User corrections and changed project reality continue through
`references/state-transitions.md` and State Boundary Enforcement. Preserve
unaffected accepted work; rebuild only descendants of a reopened judgment.
`goal` decides whether the whole commission must be resynthesized, while
`project-lifecycle` changes only the affected software state and agenda.

Report software readiness only when required agenda items are done or explicitly
user-approved as skipped, requested verification and review evidence is current,
authorized delivery is satisfied, controlling sources contain no unresolved
accepted software work, and applicable runtime-resource and subagent join gates
pass. This is a software Handoff to the universal owner, not native goal
completion. Only `goal`, in the main thread, may synthesize the full-request
result and update the explicit goal state.

## Pressure Cases

- Tiny explicit goal: activate goal ownership without broadening the one-point
  software boundary; use targeted evidence and focused review.
- Ordinary no-marker change: run the normal software lifecycle and agenda with
  no inferred native goal.
- Explicit cyclic optimization: use the universal cyclic-improvement reference,
  while software owners perform the accepted edits and requested reviews.
