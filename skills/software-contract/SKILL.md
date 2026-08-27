---
name: software-contract
description: >
  Resource-only software project contract skill. Use as the domain resource
  layer for software-project work when project-lifecycle, project-bootstrap,
  project-iteration, project-docs, project-frontend, review, or optimize needs
  software standards, standard development guide coverage, frontend
  quality/taste contracts, coding quality judgment, or docs deliverable mappings.
  Does not implement, edit, review, commit, deploy, or sync by itself.
---

# Software Contract

This is a resource-only skill for software-project domain standards. It keeps
shared judgment available without turning methods, evidence, or checklists into
the purpose of project work.

## Position In The Skill Stack

Use the project skill stack by control ownership, not by file importance:

1. **Global / AGENTS rules**: user preferences, hard safety rules, no silent
   downgrade, verification discipline.
2. **Cognitive cores**: `three-step-analysis`, `co-star`, `self-refine`,
   `review`, and `optimize`.
3. **Project controller**: `project-lifecycle`.
4. **Project adapters and executors**: `project-brief`, `project-analysis`,
   `project-bootstrap`, `project-iteration`, `project-frontend`,
   `project-docs`, `project-release`, `project-commit`,
   `project-retrospective`, and `project-sync`.
5. **Domain resource skills**: this skill for software-project contracts, loaded
   only when a controller or executor needs the standard.
6. **References / future MCP resources**: large standards, mappings, rubrics,
   templates, and domain datasets.

## Hardness Rule

This skill is not an execution owner. Hard control remains in the calling skill:

- when to stop,
- whether fallback is allowed,
- which verification must run,
- whether a question is blocking,
- how to hand off,
- what can be claimed complete.

The calling skill must load the required reference before using the standard. If
a required reference cannot be read, stop and report the missing resource. Do not
replace it with generic memory or a weaker checklist.

Mention the loaded resource in a handoff or final response only when that
context materially affects the judgment or completion claim:

```yaml
domain_resource_evidence:
  resource_skill: software-contract
  loaded_references:
    - <reference path or none>
  missing_references: <none | paths>
  fallback_used: false
```

## References

- `references/standard-development-contract.md`: standard development guide
  coverage, ledger shape, owner map, and anti-bloat rule.
- `references/docs-deliverables.md`: project documentation profile contract for
  deciding what docs should exist, where standalone docs belong, what can be
  merged, what should not be created, and how docs-only changes should be
  verified for each project shape and lifecycle stage.
- `references/coding-quality-contract.md`: shared practical quality judgment
  for implementation, optimization, and review.
- `references/frontend-quality-contract.md`: UI Contract schema, frontend state
  pressure dimensions, and realistic verification boundary.
- `references/frontend-theme-contract.md`: fixed frontend aesthetic themes,
  theme contract schema, and anti-template prompt expansions.
- `references/frontend-prototype-reference-contract.md`: source/prototype
  reference workflow for high-aesthetic UI composition beyond prompt-only
  theme words.
- `references/frontend-motion-contract.md`: advanced frontend motion selection,
  GSAP usage boundaries, cleanup, accessibility, and verification rules.
- `references/frontend-design-contract.md`: aesthetic quality as the core
  frontend criterion and goal, universal AQ1/AQ2/AQ3 target levels and score
  calibration, stable visual design, component, accessibility, responsive, and
  rendered QA standards.
- `references/frontend-taste-contract.md`: high-aesthetic frontend taste control
  for design read, component taste micro-gates, variance/motion/density dials,
  anti-default audit, redesign preservation, and compact taste preflight.

## Boundary

Do not use this skill directly to edit files, review findings, create commits,
deploy, sync machines, or run project work. It supplies standards; the caller
owns action, verification, and completion.
