---
name: project-discovery
description: >
  Downstream software-project discovery stage selected by project-lifecycle
  when an unresolved product object, user need, or product commitment must be
  understood before deciding what the project should be or offer. Produces an
  independent, provisional discovery handoff. Does not
  create PRDs, requirements, agendas, designs, implementation plans, code, or
  accepted product decisions.
---

# Project Discovery

Project discovery establishes what is true, what users or other actors are
actually trying to accomplish, and what a project may therefore need before the
project commits to what to build. It is not preliminary implementation planning
and does not presume that either the current shape or its rejection is already
the answer.

## Lifecycle Position

This is not the project entry point. Direct invocation still returns its result
to `project-lifecycle` for handoff and any requested adoption.

Use when `project-lifecycle` determines that an unresolved product object, user
need, or product commitment would decide what the project should be or offer.
The project may already have an artifact, plan, or product category; none proves
that its product commitment is accepted. Make the decision from accepted project
state, not topic words, document names, or the user's action verb.

Do not use merely because a technical explanation, root cause, architecture,
data model, operation, or implementation path remains difficult. Within an
accepted product boundary, those are `project-analysis` questions, even when a
better technical form must be imagined.

Do not use for a bounded factual lookup whose decision and downstream boundary
are already accepted; use `project-analysis` with appropriate sources. Do not
use for implementation feasibility alone, source discovery for a fixed feature,
or research that merely supports review or optimization.

The control chain is:

`project-discovery -> project-lifecycle handoff and, when findings will govern
project state, adoption -> earliest unresolved downstream commitment required by
the requested outcome`

When an adopted finding creates or changes product content, user-visible
information or capability, requirements, scope, or success criteria,
`project-brief` must form that product commitment before `project-analysis` or an
executor may consume it. If the product commitment was already accepted and the
finding does not change it, lifecycle may resume at the next unresolved phase.
`project-analysis` may test a material adoption inside the adoption gate; it
cannot replace product-commitment formation.

A request to "research, then implement" authorizes that sequence. It does not
pre-accept any candidate found in the request, current UI, repository, data
source, or earlier plan.

Consume the lifecycle Context Packet and preserve its research question,
explicit boundaries, accepted project decisions, and downstream decision to be
informed. If the user requests a standalone report, return a finished,
independently readable report plus the handoff below; durable placement remains
owned by `project-docs` and does not promote the report into project authority.

If invoked as a subagent, preserve the assigned `assignment_id`,
`execution_owner_id`, `agent_owner`, and `write_policy`. Do not edit product
artifacts, modify the parent goal or agenda, spawn subagents, commit, push,
deploy, sync, broaden scope, or claim project completion. Return the exact
assignment-required `subagent_receipt`; the discovery handoff may accompany but
never replace it.

## Discovery Standard

Start with the concrete situation rather than the available solution surface.
Identify the actors, relationships, context, time, stakes, and task or judgment
whose outcome the proposed content or capability would change. A service,
permission, or account category is not automatically a user persona or a user
task.

Any conclusion that proposes or rejects a content or capability candidate must
make the explanatory chain reconstructable:

`actor and situation -> task or judgment -> needed information or capability ->
why it changes the outcome -> applicability conditions`

The explanation must remain traceable to appropriate sources and their limits;
source apparatus supports the relation rather than replacing it.

This chain may establish that no fixed content, feature, or common default is
justified. Specificity means a concrete explanatory relation, not merely named
fields, a fixed item count, detailed categories, or an implementable schema.

Treat the following as research leads or constraints, not as proof of need:

- current UI, APIs, database fields, tests, docs, and existing behavior,
- data or integration availability,
- regulatory or domain categories,
- examples, possibilities, and tentative language from the user,
- common patterns or competitor features without a matching user task.

They become relevant only through the discovery model. Feasibility can constrain
an adopted choice later; it cannot independently establish product value.

## Inquiry And Synthesis

Load `three-step-analysis` as the cognitive core, preserving its movement
without turning the report into a three-section template. Begin by expanding the
concrete world: situation, actors, relations, history, stakes, tensions, and
possibilities, alongside the parts of project reality that could correct that
initial account. Sources, user evidence, comparable practice, and contrary cases
are ways to encounter that reality, not a collection stage that precedes or
substitutes for thought.

Then test the leading understanding against genuine alternatives and identify
what only the user's lived purpose or commitment can settle. Finally form a
provisional discovery judgment: what is explained, which possibility is worth
carrying forward, what remains unknown, and what would reverse the judgment.
This judgment is independently readable and revisable; it is not a source count,
requirements draft, or hidden implementation plan.

When the accepted purpose cannot yet be carried by a settled form, test the
inherited frame before proposing its contents. Form genuinely different causal
accounts of how the concrete situation might change, including alternatives
outside the current artifact whenever they are credible and material. Breadth
exists to expose anchoring and reveal the governing relation; it is not a quota
and does not manufacture novelty.

Sources, constraints, available data, and comparable practice may correct the
account of reality or reveal rival mechanisms. Accumulation does not generate a
direction. The synthesis must explain why the leading account changes the
concrete outcome and why credible alternatives do not do so as well under the
accepted boundaries.

Ask and stop only when the user's experience, purpose, value ordering, or real
service commitment is non-substitutable and materially changes the discovery
object or meaning. Resolve inspectable facts and professional research judgment
without transferring that work to the user.

When the lifecycle Context Packet carries `three_step_visibility: explicit`,
make the gate visible before the natural report: compact Stage 1 names the
research-world model and live alternatives; Stage 2 states the dialogue judgment;
Stage 3 states the provisional discovery conclusion and handoff boundary. This
does not turn the report body into a template. If Stage 2 blocks, stop after
Stage 2: do not emit Stage 3, a completed report, or a discovery handoff.

The report must stand on its own. Its main body explains the situation,
relationships, findings, and conclusion. Sources and limitations support that
explanation; requirements, priorities, acceptance criteria, implementation
conditions, and project-plan categories must not organize it from downstream.

## Handoff And Adoption Boundary

Return a compact `discovery_handoff` to `project-lifecycle`:

```yaml
discovery_handoff:
  research_question: <what reality was investigated and which later decision it may inform>
  situation_model: <actors, relations, tasks or judgments, stakes, and time>
  findings: <facts, interpretations, competing explanations, and conclusions>
  unknowns_and_reversal_conditions: <what remains open or would change the conclusion>
  status: <ready_for_adoption | blocked | insufficient | model_reset>
```

Add hypotheses, rejected or adoption candidates, known causal descendants, or
model-reset details only when they materially exist. Do not print empty fields
or manufacture candidates to complete the handoff.

Everything in this handoff remains `evidence_only`. `project-lifecycle` alone
may adopt a conclusion into the project boundary, using `project-analysis` when
the adoption requires a material product or technical decision. Until that
adoption is recorded, do not create or update a charter, requirement, agenda,
priority, data contract, UI content model, acceptance criterion, or executor
Context Packet from the findings.

The research report is not a requirement boundary; after adoption, follow the
downstream-commitment rule in Lifecycle Position.

`evidence_only` is an authority status, not a research method or content shape.
The handoff must still contain an independent, reasoned judgment; a source list
or quantity of evidence cannot substitute for the explanatory synthesis above.

## Model Correction

Distinguish correction level before revising:

- a disputed source, fact, or bounded conclusion can receive local correction;
- a correction to the research object, actor model, task, judgment standard,
  explanatory relation, or method is `model_feedback`.

For `model_feedback`, return `model_reset` with the invalidated finding and every
known dependent adoption candidate or downstream artifact. Stop the discovery
chain and rebuild the model. Do not preserve the old structure by deleting one
candidate, changing a count, renaming a category, or adding a caveat.

This skill does not repair downstream artifacts itself. The controller decides
which dependent decisions, requirements, plans, docs, tests, fixtures, or
implementation work must be invalidated, removed, or rebuilt.

## Final Response

Lead with the discovery judgment and its causal explanation. State the decisive
research boundary, important uncertainty, and whether the handoff is ready for
adoption. Do not present adoption candidates as committed product decisions or
continue into implementation.
