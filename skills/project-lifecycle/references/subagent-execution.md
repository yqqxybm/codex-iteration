# Subagent Execution

Use when lifecycle finds independent work, delegates a task, selects child
capacity, or joins results. This file owns ordinary native V2 parallelism.
Read [subagent-durable-state.md](subagent-durable-state.md) only when the
persistence decision below requires CAO.

The purpose is better work sooner, counting setup, reasoning, retries,
verification, and integration together. Roles organize responsibility; model
and effort supply the capacity this particular task needs. Neither a model
default nor a longer protocol replaces that judgment.

## Runtime And Ownership

Native V2 owns spawning, follow-up, messages, waiting, interruption, status,
and resident capacity. Lifecycle owns decomposition, conflict decisions,
assignment, model selection, integration, and completion. CAO, when needed,
persists task authority; it neither spawns nor makes project decisions.

Use the live V2 tool contract and available model catalog. The installed setup
enables `multi_agent_v2` and `agents.enabled` and disables `multi_agent`.
If V2 is unavailable or policy blocks it, keep delegated work visibly blocked;
do not claim a substitute backend executed it. Preserve the user's model and
service-tier settings; service tier is not a task-difficulty decision.

Parallelism is opt-out, including daily work and opportunities discovered
mid-task. Dispatch independent reads and disjoint writes when they shorten the
critical path. A concrete dependency, conflict, capacity, policy, or greater
coordination cost can justify serial work; a habit of working alone cannot.
Commit, push, publish, release/tag mutation, deploy, remote sync, and parent
completion remain with the main thread. Children return new work and
coordination needs to that thread.

## Select Role, Model, And Effort

Before each assignment, make three distinct choices:

- **Role** follows the work: `explorer` investigates a bounded read-only
  question; `worker` produces or changes the assigned artifact; `reviewer`
  independently judges it. All three can require light or demanding reasoning.
- **Model** follows the cognitive difficulty: how uncertain the explanation or
  solution is, how tightly decisions interact, what a wrong judgment would
  cost, and how clearly the result can be checked. A large mechanical change
  may be easy; a one-line permission decision may be hard.
- **Effort** follows the reasoning needed within that model, not the parent's
  setting or a permanent role tier.

In the currently available catalog, Terra with low/medium effort suits clear,
bounded work whose outcome can be checked directly; higher Terra effort can
fit careful but well-bounded tracing. Sol with high/xhigh or greater effort
fits unresolved causal or design judgment, tightly coupled changes, or errors
that are consequential and hard to expose. These are starting judgments, not
task-name mappings: a review need not be hard and a writer need not be easy.
Use the route most likely to reach the required result efficiently; do not run
a knowingly underpowered first attempt merely to qualify for escalation.

Give a brief task-specific `route_reason` and pass explicit `model` and
`reasoning_effort` to every fresh spawn. Global Terra/medium defaults are
runtime defaults, not completed routing decisions. Check the selected role is
available and its custom file does not pin a conflicting model/effort. The
installed `explorer`, `worker`, and `reviewer` files deliberately leave those
values unpinned. Resolve a conflict before dispatch rather than silently using
`default` or substituting a weaker route.

Reassess when findings change the task's uncertainty, coupling, stakes, or
verification difficulty. More effort is not the remedy for missing facts,
ambiguous authorization, a bad decomposition, or a malformed receipt. Correct
the cause. Later mechanical work may use a lighter route even when its parent
required difficult reasoning.

`followup_task` cannot change model or effort. Reuse a resident only when its
known route and retained context fit the next assignment; provide a fresh
assignment for new work. A route change requires a fresh spawn. Before replacing
unfinished work, interrupt it and confirm it has stopped, inspect its partial
changes, then assign the remaining work. Do not run two attempts against the
same writable scope or claim an in-place model upgrade occurred.

## Form A Useful Wave

Keep dependencies and conflicts with the existing agenda. For a short in-turn
wave, the assignments and native handles can carry this state without a new
plan document. Use the existing modes when a caller needs them:
`sequential`, `subagent_wave`, `controller_team`, or `workflow_batch`.

Select ready nodes with no dependency or write-conflict edge between them.
Files, lockfiles, schemas, migrations, shared components, generated output, and
external targets may be shared conflict keys. Resolve path aliases before
claiming scopes are disjoint. A read that needs a coherent snapshot also waits
for a conflicting writer; not all reads are independent.

Describe the actual split briefly before dispatch. Use available capacity for
profitable independent nodes, not to fill a quota. Keep a real integration
owner and continue non-overlapping parent work while children run. When a
finding, user addition, failed check, or returned result changes dependencies,
replan the next wave instead of continuing serially by inertia.

## Decide Whether Persistence Is Necessary

Use V2 alone when the parent can safely reconstruct its task ownership and
results from the current task. Length, multiple waves, loops, or the existence
of V2 history do not themselves require CAO.

Use CAO only when an actual or required interruption/resume in this same parent
task would make ownership, locks, attempt identity/history, receipt acceptance,
or convergence unsafe without machine persistence. Then load
`subagent-durable-state.md` before dispatch. Its atomic assignments and strict
receipts replace the ordinary preparation/check path below; do not translate a
CAO payload into the compact native format.

## Ordinary Native Dispatch

Use `scripts/native_handoff.py` under this skill as a stateless contract
compiler/checker. It stores no task graph, writes no files, calls no model,
and makes no routing or acceptance judgment. It makes an explicit route and
small complete assignment available as actual spawn arguments, rather than
leaving them as optional prose.

Prepare with `python3 <skill-root>/scripts/native_handoff.py prepare
--request-json '<JSON>'`. Supply:

```yaml
task_id: <existing node or local task label>
task_name: <unique native lowercase/digit/underscore label>
agent_owner: <logical responsibility>
agent_type: <explorer | worker | reviewer>
model: <explicit available model>
reasoning_effort: <explicit effort supported by that model>
route_reason: <why this task needs that capacity>
scope_root: <absolute canonical root>
owned_scope: <nonempty list of relative paths>
forbidden_scope: []
write_policy: <read_only | same_worktree_disjoint | single_writer>
analysis_gate: <project_analysis_consumed | explicitly_skipped_by_user |
  not_required_read_only | not_required_very_small>
analysis_gate_basis: <actual decision/boundary, waiver, or read-only/tiny proof>
task: <self-contained problem, context, relevant purpose and protected boundary>
done_when: <local outcome the parent can judge>
verification: <check needed for that outcome>
```

The compiler returns `contract` plus `spawn_args`, with new assignment and
execution-owner identities and `fork_turns: "none"`. Retain the returned
contract and pass the exact `spawn_args` to native `spawn_agent`. Its message
contains only this bounded assignment, child authority limits, and a small
receipt template. Do not pass the parent's full conversation or goal machinery.
The native tool still validates live role/model availability; the compiler
cannot establish that a model actually ran.

Dispatch exists only when `spawn_agent` returns a canonical `task_name`. Keep
that handle with its contract and selected route until the result is integrated.
The compiler's output alone is not a running agent. Rejected spawn arguments
leave the node pending or blocked; no synthetic receipt can close it.

Use `not_required_read_only` only for a non-mutating task. Material writers
consume the accepted analysis boundary or an actual user waiver; tiny writers
need the lifecycle's `very_small` proof. Scope is canonical and root-relative:
`.` is the root, a trailing `/` includes descendants, and a bare path denotes
the exact file. `write_policy` is an instruction, not OS isolation; parent
permission and runtime restrictions still apply. The checker does not prove
that peer scopes are conflict-free or that the child reported all its writes.

For compatible resident reuse, prepare a fresh contract and send its generated
message through `followup_task` only after confirming the resident's actual
role/model/effort match. Keep the same native handle but replace the active
contract. Correcting a malformed receipt for the same completed work keeps the
original contract and assignment identity.

## Check Results, Then Accept Work

Ordinary children return only:

```yaml
subagent_receipt:
  assignment_id: <exact id from assignment>
  status: <done | blocked | failed | out_of_scope>
  changed_files: <relative paths; empty for read-only work>
  result: <actual result or material findings>
  verification: <checks and outcomes, or what was not verified and why>
  new_work: <material follow-up; empty when none>
```

The parent already owns the task id, role, execution owner, and assigned scope;
children need not reconstruct those bookkeeping fields. Run
`python3 <skill-root>/scripts/native_handoff.py check --contract-json '<contract>'
--receipt-json '<receipt>'` before associating a result with an agenda item.
The checker rejects wrong identities, invalid states/types, reported read-only
writes, and reported paths outside the owned boundary. It associates a valid
result with the parent's retained contract, never with a child-invented task id.
Request a bounded correction after rejection; do not accept a guessed mapping
or run the entire task again just to repair formatting.

A valid receipt is not a correct result or a completed task. Inspect the actual
findings or changed files, run the consequential parent check, and decide
whether `done_when` is met. Integrate useful `new_work` into the existing agenda
or reject it with a reason; only then mark the task done. Failed, blocked,
unverified, or missing results remain visible. No parsing success can stand in
for professional judgment.

## Join And Resident Lifecycle

Before dependent work or parent completion, account for every dispatched
contract: accepted result, rejected result with a next action, or visible
unfinished work. Inspect and verify integration. Use native notifications and
wait only at a real dependency or join barrier.

Inspect `list_agents` when accounting for remaining work. Interrupt obsolete
running children. Completed residents are reusable context, not unfinished work
and not durable acceptance. V2 may unload an eligible completed, errored, or
interrupted resident when it needs capacity. If spawn reports a limit, inspect
the current state, use compatible root work or a fitting resident, wait for a
state change, or report the blocker; do not spin or blind-retry.

A missing thread without an accepted result keeps its task unfinished. When
CAO was active, its semantic join must also pass. Report meaningful remaining
work, not a per-event transport ledger.
