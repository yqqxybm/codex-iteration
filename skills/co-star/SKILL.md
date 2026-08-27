---
name: co-star
description: >
  CO-STAR quick task-structuring skill. Use for everyday writing, prompt
  shaping, or simple generation tasks with fuzzy inputs. Do not use for deep
  decisions, software project lifecycle work, new projects, or multi-skill
  orchestration; use three-step-analysis, project-brief, or project-lifecycle
  instead.
---

# CO-STAR

CO-STAR is the quick task-framing core. It turns a fuzzy non-project request
into one coherent internal specification and then produces the requested
artifact. The dimensions guide judgment; they are not a form the user must fill
or a process to display.

## Boundary

Use this skill for everyday writing, prompt shaping, and simple generation when
the main uncertainty is how to frame the output. Route instead to:

- `three-step-analysis` when the underlying judgment or direction is unresolved,
- `project-brief` when a fuzzy software-project request needs a charter,
- `project-lifecycle` for project execution, orchestration, or multi-skill work,
- `self-refine` when an accepted non-project artifact only needs iterative polish.

Project adapters may add project scope, verification, and call-chain concerns;
they do not create a second task-framing philosophy.

## Six-Dimension Frame

Build the smallest useful internal frame:

- **Context**: why the task exists, relevant history/material, and current
  constraints.
- **Objective**: the actual deliverable, intended effect, success condition,
  required content, and exclusions.
- **Style**: structure, vocabulary, depth, and any accepted reference style.
- **Tone**: the interpersonal or emotional stance appropriate to the purpose.
- **Audience**: who will use the artifact, what they know and care about, and the
  situation in which they will use it.
- **Response**: format, length, organization, and any external interface the
  result must satisfy.

Weight only the dimensions that can change the output. Preserve facts and
explicit choices from the user. Infer missing values when the result remains
materially the same; ask one concise question only when multiple plausible
frames would materially change the artifact and the answer cannot be responsibly
inferred.

## Workflow

1. Form the internal six-dimension frame from the request and relevant context.
2. Resolve tensions by serving the objective and audience while preserving the
   user's explicit style, tone, format, and exclusions.
3. Produce the artifact directly; do not narrate the framework or label sections
   by CO-STAR dimensions unless the user asks for a structured prompt/card.
4. Check the finished artifact against the objective and any decisive audience,
   constraint, or format requirement. Revise only a dimension implicated by a
   real mismatch.

When the user asks to see the framing, show a compact card:

```text
Context: ...
Objective: ...
Style: ...
Tone: ...
Audience: ...
Response: ...
Assumption needing confirmation, if any: ...
```

Stop when the artifact satisfies the objective. More visible framework, extra
questions, or repeated reformulation is not a better result.
