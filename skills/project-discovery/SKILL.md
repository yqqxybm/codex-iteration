---
name: project-discovery
description: >
  Downstream software-project discovery stage selected by project-lifecycle
  when user, market, competitor, domain, or product research must determine
  product content, target users, requirements, priorities, or scope before a
  charter or implementation can be accepted. Produces an independent,
  provisional discovery handoff. Does not create PRDs, requirements, agendas,
  designs, implementation plans, code, or accepted product decisions.
---

# Project Discovery

Project discovery establishes what is true, what users or other actors are
actually trying to accomplish, and what a project may therefore need before the
project commits to what to build. It is not preliminary implementation planning
and does not search for reasons to preserve an existing product shape.

## Lifecycle Position

This is not the project entry point. Direct invocation still returns its result
to `project-lifecycle` for handoff and any requested adoption.

Use only when `project-lifecycle` determines that research must decide product
content, target users, requirements, priorities, positioning, or scope. Typical
requests include "先调研再决定功能", user or market research that will shape a
product, competitor research before a product decision, and domain research
whose result may remove or replace the assumed solution.

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

Load `three-step-analysis` as the cognitive core without turning an ordinary
discovery report into a three-section template:

1. establish the research question, the decision it may inform, the governing
   standard, current hypotheses, and what could overturn them;
2. inspect the smallest sufficient mix of project reality, authoritative domain
   sources, user or operator evidence, comparable alternatives, and contrary
   evidence;
3. synthesize facts, interpretations, competing explanations, conclusions,
   unknowns, and reversal conditions into an independently readable account.

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
