---
name: self-refine
description: >
  Iterative polish skill for high-quality non-project writing, prompts, plans,
  copy, and standalone artifacts whose meaning and direction are already accepted.
  Uses generate, critique, and refine loops. Use three-step-analysis for deep
  decisions, optimize for structural optimization, and project-refine for
  software-project artifacts.
---

# Self Refine

Self-refine improves an artifact by finding and correcting the mechanism that
limits its purpose. Iteration is useful only when it changes the artifact for the
better; more versions, critique items, or visible process are not quality.

## Boundary

Use for non-project text, prompts, plans, copy, or standalone artifacts whose
goal and meaning are already sufficiently clear. Route instead to:

- `three-step-analysis` when the underlying decision or direction is unresolved,
- `optimize` when the task is to decide what should improve and why,
- `project-refine` for software-project docs, prompts, UI copy, architecture
  notes, runbooks, handoff text, or code examples,
- the relevant execution owner when refinement changes runnable behavior.

## Refinement Model

Before changing the artifact, establish the smallest useful specification:

- purpose and intended reader,
- accepted meaning, facts, and source-of-truth boundary,
- voice, form, and constraints worth preserving,
- the quality failure that matters most,
- the condition for stopping.

Make reasonable assumptions when they do not change the artifact materially.
Ask only when the user's private purpose, meaning, voice, or acceptance boundary
would change the result and cannot be responsibly inferred.

## Loop

### 1. Generate Or Read

Create a complete first version, or read the current artifact as a whole. Do not
optimize isolated sentences before understanding the artifact's purpose and
structure.

### 2. Critique

Identify only material limitations. Start with objective, reasoning, structure,
reader understanding, and completeness; consider wording, tone, and detail after
the larger structure is sound. For each retained critique, explain:

- what fails,
- why it fails for this purpose or reader,
- what causal or structural change would correct it,
- what already works and must be preserved.

Facts and sources may challenge or bound the critique, but their quantity cannot
replace the explanation. Do not invent a problem to justify another round.

### 3. Refine

Revise the complete artifact so the underlying limitation is removed. Prefer
deletion, replacement, reordering, or clarification before adding qualifications,
rules, sections, or disclaimers. Preserve accepted meaning and strengths; do not
turn polish into a new direction.

When user feedback arrives, first decide whether it reveals a local expression
problem, a structural failure, or a mistaken goal model. Correct it at that level
and within its real scope. One correction does not become a universal rule.

### 4. Reconstruct And Stop

Test the latest artifact against its specification. For explanatory work, check
whether the intended reader can reconstruct the purpose, main judgment or
message, decisive reasons, relevant boundary, and next action without seeing the
refinement process.

Repeat only while a material issue remains or the previous change introduced one.
Stop when a full critique finds no material improvement, further changes are
preference variants, or marginal gain no longer justifies the change. If a user
limit stops the loop while a material issue remains, disclose that issue.

## Three-Step-Governed Refinement

When the user explicitly requires three-step analysis in each round, consume a
compact model:

```yaml
three_step_refine_frame:
  material_model: <purpose, governing structure, explanatory relation, standard>
  calibration: <assumptions, reversal conditions, dialogue judgment>
  commitment: <preserve, change, reject, and verify>
```

Each material critique must trace to that model. It governs the refinement of the
owned non-project artifact; executable project artifacts remain with their
project execution owner.

## Verification And Output

Use direct factual, link, example, render, or runnable checks only when they can
test a claim the artifact makes. If verification is unavailable and matters to
usability, say so.

Return the final artifact first, followed by the few changes that materially
improved it and any remaining issue that changes whether it is usable. Keep
drafts, critique logs, and intermediate versions internal unless the user asks
to inspect them.
