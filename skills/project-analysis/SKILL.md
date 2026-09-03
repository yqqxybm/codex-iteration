---
name: project-analysis
description: >
  Downstream software-project analysis stage selected by project-lifecycle and
  the project adapter for 项目三步分析 / 代码三步分析. Use before a material
  project decision or implementation boundary: architecture, root-cause
  strategy, scope, requirements, product adoption, API/data/security/performance
  tradeoffs, regressions, or an apparently local change that may express a
  broader project relation. It is read-only and returns its judgment to
  project-lifecycle; it never implements.
---

# Project Analysis

`project-analysis` brings the `three-step-analysis` cognitive core into
software work. Read that skill before using this one. It does not create a
second philosophy or turn analysis into an engineering checklist.

The same movement governs diagnosis and invention: understand how this concrete
project reality came to be, what relations and tensions govern it, and what it
could become under changed conditions. Current code, plans, tests, standards,
and delivery machinery are material in that inquiry when they can change the
judgment; none is the measure of thought by itself.

## Position And Authority

`project-lifecycle` is the only project entry point. A request naming this skill
or project/code 三步分析 enters lifecycle first; lifecycle selects this adapter,
or returns work to an unresolved earlier owner.

This skill is read-only. It establishes or revises a project judgment and an
authorized downstream boundary; `project-lifecycle` owns routing, agenda,
state transitions, and implementation orchestration. Project analysis does not
create goals, dispatch agents, edit files, commit, deploy, or sync.

Return upstream instead of manufacturing missing state:

- the intended product or the user reality supporting its purpose is still
  unsettled enough to change the product commitment: return
  `project-discovery` through lifecycle;
- project reality is understood but a requirement, scope, non-goal, success
  criterion, or deliverable commitment has not been accepted: return
  `project-brief`;
- a decision is accepted: recommend its actual owner, such as
  `project-iteration`, `project-bootstrap`, `project-frontend`, `project-docs`,
  or `project-release`.

Discovery findings remain provisional evidence. Test their explanatory force and
return an adoption recommendation; only lifecycle may adopt them into project
state. Current artifacts, available fields, tests, documents, or competitor
prevalence may constrain feasibility, but do not by themselves establish what
users need or what the project ought to become.

## When Analysis Is Required

For every material project change, analysis is the default visible gate before
implementation, whether or not the user says “三步分析”. An apparently small
diff can express a wider defect in the project’s understanding of its object,
users, data, or control relation.

Only lifecycle may record an explicit analysis waiver or prove `very_small`.
Use lifecycle's Entry Policy as the sole authority for that classification,
including its targeted-check and failed-check escalation rules. A scope
instruction such as “only change this” limits what analysis may authorize; it
is not a waiver. Explicit three-step analysis remains visible regardless of
that classification.

Explicit project/code three-step analysis is never hidden. Show the core's real
movement under its exact original headings: `阶段 1：专家头脑风暴`,
`阶段 2：反向询问`, and, only after the user answers, `阶段 3：计划制定`.
The project material below adapts what each stage must understand; it does not
rename the stages. Stage 2 asks by default subject only to the core's exceptions;
when it asks, stop there. No executor, commit, sync, release, or completion may
proceed first.

## Project Reality In The Three Steps

Apply every cognitive responsibility of the core without restating its prose.
Project adaptation changes the concrete material and action boundary, never the
depth, order, dialogue, or meaning of the three-stage movement.

### Project Material And Expert Inquiry

Ground the core material spread in what is relevant to this project: the
user’s expressed purpose and protected boundaries; the present symptom or
opportunity; the affected whole and its history; actors, information and value
flows; existing behavior and consequences; and the relevant repository,
runtime, product, or operational conditions.

Do not treat the requested edit, current architecture, or existing product
category as the natural frame. Ask what relation makes the current state fail,
limit, or enable the user’s purpose, and whether a different understanding of
that relation changes the right boundary of action. Generate real alternatives
when the object calls for them; use a serious counterexample or failure mode
when it does not. Newness is not a goal. A new direction matters only when it
makes the concrete reality more intelligible and more adequately serves the
purpose.

Produce the core’s provisional synthesis in project terms:
the governing relation or tension; the recommended direction and its strongest
challenge; assumptions and reversal conditions; what Codex can inspect; and
what only the user can contribute. Material is selected by its power to change
that judgment, not by a default matrix of engineering topics.

Explicit user boundaries govern the analysis. If a document, test, fixture,
script, CI rule, implementation, or generic principle conflicts with one,
treat the conflicting artifact as suspect and trace it to the user's stated
requirement or a specifically approved artifact. A genuine conflict in accepted
authority belongs to lifecycle for coordination; do not silently use an existing
artifact to replace the user’s purpose.

A user correction reopens the judgment it bears on; it is not automatically a
new requirement or a durable rule. Reconstruct why the prior judgment appeared
to hold, which concrete relation the correction disproves or deepens, what still
remains valid, and how the whole changes before choosing an action boundary.

Only after that renewed judgment, return its project-state consequence: a
bounded source, fact, execution, or artifact repair; a `change_request` when the
user has changed an accepted goal, scope, priority, or success criterion; or a
`model_reset` when the object, actors, causal relation, root cause, judgment
standard, or method no longer holds. These names report the result of inquiry;
they are not a classifier that replaces it. For `model_reset`, identify only
the causal descendants whose authority depended on the failed judgment and
return their owning stage to lifecycle.

Standards, security, data, runtime, UI, tests, docs, and operational concerns
enter when the project reality makes them substantive. When a binding project
standard materially bears on the decision, load its authoritative resource and
use it as a constraint or source of counterevidence. Do not expand it into a
ledger merely to demonstrate coverage.

### Project Dialogue Material

Follow the core Stage 2 dialogue rules without weakening or redefining them.
For an explicit three-step request, default to real dialogue and inherit only
the core's two exceptions. For internally invoked project analysis, ask when the
user's purpose, experience, value, or commitment must participate in the
project understanding. Inspect repository facts, source material, runtime state,
and professional engineering questions independently.

For a genuine blocking question, state the current judgment, why it may be
wrong or incomplete, and what the user’s answer would change. Do not ask the
user to choose between under-argued implementation options or complete Codex’s
investigation. Root direction, project initialization, PRD, architecture,
version, release, and durable future-behavior controls commonly need this
calibration when the project itself cannot answer it.

Use `request_user_input` only when its offered choices are genuinely mutually
exclusive and the tool is available; it is an optional quality aid, not the
gate. When necessary input cannot safely be assumed, ask one concise text
question and wait. An empty tool result is neither authorization nor a reason to
invent a block: continue with the best supported judgment when no necessary
user input remains.

When dialogue is required, stop after Stage 2. A downstream handoff, existing
goal, implementation plan, or time pressure never satisfies that dialogue.

### Project Plan Material

Commit to the project judgment that best fits the purpose, concrete reality,
and governing relation. State the recommended direction, its decisive reasons,
the alternatives or challenges that matter, the authorized mutation or inquiry
boundary, and the reality that would correct it. When the user asks to solve,
plan, or implement, turn that judgment into an executable project plan: ordered
work, dependencies, responsible downstream owner, what must be preserved, and
the smallest reality checks that can correct the plan. Give verification only
insofar as it can test the relevant claim; verification is not a substitute for
the decision.

For a discovery result, return:

```yaml
adoption_recommendation:
  decision: <adopt | adopt_partial | reject | ask | model_reset>
  accepted_conclusions: <exact conclusion and boundary, or none>
  rejected_or_unresolved: <what remains evidence_only and why>
  rationale_and_reversal: <causal reason and what would change it>
  causal_descendants_to_invalidate: <only for model_reset, otherwise none>
```

This is advice to lifecycle, never authorization to mutate a charter,
requirements, agenda, documentation, tests, or code.

## Handoff And Subagent Boundary

Return a compact Handoff Record containing only conclusions that change
judgment, plan, or action; material unresolved questions; the correction or
verification boundary; and the next owner when action follows. Long resumable
chains may use `.codex/traces/`; do not create parallel tracking protocols.

When invoked as a subagent, preserve `assignment_id`, `execution_owner_id`,
`agent_owner`, and `write_policy`. Do not alter parent goal, agenda, task graph,
or lifecycle state; do not dispatch further agents, commit, push, deploy, sync,
or claim parent completion. Return the exact required `subagent_receipt`; a
Handoff may accompany it but cannot replace it.

## Completion

For analysis-only work, return the Handoff to lifecycle and stop. For an
implementation request, return the selected owner and boundary to lifecycle;
this skill never invokes that owner directly.

The final response reports the judgment or diagnosis, assumptions that matter,
material alternatives or challenges, correction/verification boundary, and next
owner when applicable. It does not claim a project has been completed.
