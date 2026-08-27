# Frontend Taste Contract

Use this reference from `project-frontend`, `review`, or `optimize` when UI
work depends on first-impression quality: landing pages, portfolios, brand
pages, redesigns, product pages, prototypes, high-aesthetic screens, or surfaces
with high generic-template risk. This contract may also apply to a dashboard or
workspace only for its visual language and first-viewport composition; product
state robustness remains owned by `frontend-quality-contract.md`.

Universal aesthetic integrity, AQ1/AQ2/AQ3 target selection, calibrated visual
scores, and rendered proof are owned by `frontend-design-contract.md`. This
contract adds high-order taste judgment; it does not decide whether aesthetics
apply.

This is a local taste control layer inspired by public anti-generic frontend
skill patterns, but it is not an installed copy and does not create a separate
frontend entry point. It compresses useful taste ideas into this skill system's
resource architecture.

## Purpose

Good frontend taste is not a bigger checklist. It is the ability to read the
brief, choose the right visual language, produce a concrete beauty mechanism,
resist model defaults, and verify the rendered result against that choice.

This contract adds five controls:

1. **Design read**: infer what kind of surface this is, who it serves, and what
   design language follows from that.
2. **Taste dials**: calibrate variance, motion, and density before coding.
3. **Anti-default audit**: identify likely generic AI habits before they enter
   the implementation.
4. **Simple-Coherent-Elegant preflight**: reduce unjustified complexity, unify
   the visual thesis, and preserve only the strongest useful expressive move.
5. **Taste decision preflight**: confirm the selected direction is coherent
   enough to implement.

It does not replace:

- `frontend-design-contract.md` for stable visual/component/accessibility rules,
- `frontend-quality-contract.md` for loading/empty/error/long-content/permission
  state coverage,
- `frontend-theme-contract.md` for fixed theme grammars,
- `frontend-prototype-reference-contract.md` for source/prototype extraction,
- `frontend-motion-contract.md` for GSAP, reduced motion, cleanup, and motion
  verification.

## Taste Control Packet

Build this packet internally before implementing Tier 2/3, redesign, landing,
portfolio, prototype, source-inspired, or high-aesthetic UI work:

```yaml
taste_control:
  design_read:
    surface_type: <landing | portfolio | brand_page | redesign_preserve | redesign_overhaul | product_screen | dashboard | form | other>
    audience: <who judges or uses the interface>
    user_goal: <conversion | comprehension | operation | trust | exploration | status | creation>
    design_language: <system, aesthetic family, or custom thesis>
    quiet_constraints: <accessibility | regulated | enterprise | kids | public-sector | performance | none>
  dials:
    design_variance: <1-10>
    motion_intensity: <1-10>
    visual_density: <1-10>
    rationale: <why these values fit the design read>
  source_control:
    design_system: <official system | local design system | aesthetic approximation | none>
    prototype_reference: <reference packet id or not required>
    theme_contract: <theme id or custom>
    effect_archetype: <none | selected expressive move, source, and why it serves the design thesis>
  aesthetic_generation:
    mechanism: <what will make the interface beautiful>
    implementation_translation: <layout, type, material, density, content, asset, or motion decisions>
  anti_default_risks:
    - <specific generic pattern likely for this brief>
  preservation:
    mode: <greenfield | preserve_existing | overhaul_existing | surgical>
    must_preserve: <brand tokens, IA, routes, analytics, copy voice, accessibility wins>
  simple_coherent_elegant:
    simplicity_check: <what complexity was removed or justified>
    coherence_check: <the single thesis tying layout, typography, color, motion, and content>
    elegance_check: <the expressive move retained and why it is proportionate>
  taste_preflight:
    status: <pass | needs_revision | blocked>
    failed_checks: <none or exact failures>
```

The final response should report only a compact evidence boundary:

```yaml
taste_contract_evidence:
  design_read: <one sentence>
  dials: <variance/motion/density>
  aesthetic_generation: <mechanism and implementation translation summary>
  effect_archetype: <none | summary>
  sce: <simple/coherent/elegant pass | revised | blocked>
  anti_default_risks_checked: <summary>
  preflight: <pass | revised | blocked>
  not_checked: <none or exact reason>
```

## Component Taste Micro-Gate

Load this compact gate for a bounded component even when the surrounding task is
Tier 0/1 if the component carries trust, irreversible choice, conversion,
identity, or explicit aesthetic importance. Examples include login/auth,
payment/checkout, legal or consent notices, permission gates, destructive
confirmations, onboarding decisions, pricing/upgrade prompts, and a component
the user explicitly asks to make beautiful.

```yaml
component_taste_gate:
  component_job: <decision, trust, consent, conversion, warning, identity, or other>
  aesthetic_target: <AQ2 minimum or inherited higher floor>
  trust_or_risk_posture: <calm | authoritative | urgent | reversible | irreversible>
  reading_or_decision_path: <what the eye must understand first, second, and last>
  action_hierarchy: <primary, secondary, destructive, dismiss, and why>
  visual_pressure: <copy length, density, overlay dominance, interruption cost>
  local_style_fit: <what must match the surrounding system>
  expressive_move: <one proportionate visual move or none>
  failure_tests: <coercive emphasis, weak hierarchy, generic modal, cramped copy, style break, or other>
```

This gate supplements `local_style_reference`; it does not authorize a full-page
redesign or broad external-reference search. A legal/consent component must
preserve meaning and action honesty while making the reading path and choice
hierarchy aesthetically clear. If local grammar is visibly weak, improve the
assigned component to AQ2 within scope rather than reproducing the defect.
Interaction correctness alone does not pass the gate; the rendered component
must receive the clean holistic aesthetic verdict owned by
`frontend-design-contract.md`.

## Dial Calibration

The dials are not decorative. They decide how much risk the design may take.

- `design_variance`: composition risk. Low means conservative, symmetrical,
  system-led; high means asymmetric, editorial, kinetic, unusual composition.
- `motion_intensity`: motion depth. Low means static or basic feedback; high
  means choreographed timelines, scroll narrative, pinned sections, or spatial
  continuity. Implementation still follows `frontend-motion-contract.md`.
- `visual_density`: information per viewport. Low means airy narrative; high
  means scan-dense operational surface.

Default by surface:

| Surface / brief | Variance | Motion | Density |
|---|---:|---:|---:|
| public-sector, regulated, trust-first | 2-4 | 1-3 | 4-6 |
| enterprise admin, audit, operations, CRM | 2-4 | 1-3 | 7-9 |
| developer tool, agent console, deployment/logs | 3-5 | 2-4 | 6-8 |
| SaaS landing, product page, launch page | 6-8 | 4-7 | 3-5 |
| premium consumer, luxury, portfolio | 6-8 | 4-7 | 2-4 |
| editorial, story, brand narrative | 7-9 | 4-8 | 2-4 |
| experimental creative / Awwwards-like | 8-10 | 7-10 | 2-4 |
| redesign preserve | match existing + small lift | match + 0-2 | match |
| redesign overhaul | reset from target language | target language | preserve content density unless told otherwise |

If the dials conflict with the actual product job, the product job wins. A dense
workspace should not become a sparse marketing poster because the user said
"高级"; a landing page should not become a table-heavy admin screen because the
data model is rich.

## Effect Archetype Selection

Public prompt/effect galleries and UI intelligence datasets can improve taste
only when their ideas are converted into a single controlled expressive move.
They are not prompt dumps and do not override the design read.

For Tier 2/3 landing pages, portfolios, brand pages, product pages, and
high-aesthetic prototypes, choose at most one primary `effect_archetype` when it
improves first impression or comprehension. Candidate archetypes include:
scroll-scrub product narrative, text reveal, magnetic hover, sticky card stack,
liquid/glass material, marquee/ticker, 3D or canvas object, shader/particle
field, sketch chart, and animated component system.

An effect archetype is valid only when it answers one of these questions:

- What hierarchy does it clarify?
- What product story or workflow does it make easier to understand?
- What spatial continuity or feedback does it create?
- What brand character does it express more precisely than static layout?

Reject the archetype when it is chosen only because a gallery example looks
good, duplicates another flourish, conflicts with a dense workflow, introduces
uncontrolled performance/accessibility risk, or weakens the Simple-Coherent-
Elegant thesis.

Use UIUXProMax-style style, color, typography, chart, and motion catalogs as
input to the design read and dial calibration only. The final decision remains
the project-specific design thesis plus rendered evidence.

## Design System Honesty

Use an official design system when the brief clearly belongs to one:

- Microsoft / Office-like / enterprise workbench -> Fluent UI.
- Google-ish or Android-adjacent -> Material.
- IBM enterprise analytics -> Carbon.
- Shopify admin app -> Polaris.
- GitHub-like developer/community surface -> Primer.
- Atlassian/Jira-like product -> Atlassian design system.
- UK/US public-sector service -> GOV.UK Frontend or USWDS.
- Data grid heavy product -> TanStack Table, AG Grid, or the existing grid
  system; do not fake a serious table with styled `<div>` rows.

Rules:

- Use one system per surface unless the project already has a mixed legacy
  system that cannot be changed in this task.
- Do not claim a real design system while recreating only its colors by hand.
- If the direction is only an aesthetic, label it honestly as an approximation
  and implement with the project's existing stack.
- Do not import a new design system for a small existing-project edit unless
  `project-lifecycle` explicitly authorizes that scope.

## Anti-Default Audit

Before implementation, name the likely generic defaults for this brief and
counter them deliberately. Common defaults to avoid unless justified:

- centered hero + three equal cards + generic CTA;
- AI-purple / blue-purple gradient without brand reason;
- dark mesh background for every AI or developer product;
- all sections as floating cards or card-in-card layout;
- `Inter` plus slate/gray palette chosen from habit;
- glassmorphism everywhere instead of a specific material model;
- overusing small uppercase eyebrow labels above every section;
- repeated zigzag image/text sections;
- fake product screenshots made from empty rectangles;
- placeholder names, fake metrics, lorem ipsum, or startup-sounding filler;
- pure-text "minimalism" with no visual protagonist;
- motion added because it looks cool rather than because it explains hierarchy,
  continuity, feedback, or narrative.

Overrides are allowed when the brief, brand, existing system, accessibility, or
product job justifies the pattern. The audit is not a ban list; it is a default
resistance mechanism.

## Simple-Coherent-Elegant Rule

Taste control converges through subtraction, unification, and proportion:

- **Simple** asks what can be removed without weakening intent, trust,
  comprehension, workflow speed, or product identity.
- **Coherent** asks what single design thesis makes the typography, palette,
  grid, components, content, assets, states, and motion belong together.
- **Elegant** asks which expressive move deserves attention, then makes its
  scale, rhythm, detail, and feedback precise enough that the UI feels designed
  instead of decorated.

High variance, high motion, or high density can still pass. They fail only when
they are not controlled by the product job or the selected design thesis.

## Redesign Taste Protocol

For redesigns, classify the mode before changing visuals:

- `preserve_existing`: modernize without breaking brand, IA, routes, analytics,
  copy voice, or recognizable interaction patterns.
- `overhaul_existing`: new visual language approved; preserve content intent,
  SEO-critical routes, legal/consent copy, and core workflow unless explicitly
  authorized.
- `surgical`: fix a visible UI defect while preserving the local style.

Audit before changing:

- brand tokens: color, type, radius, logo treatment, imagery, icon family;
- information architecture: nav, routes, anchors, conversion or workflow paths;
- content blocks: what carries meaning, what is filler, what must stay;
- current dials: existing variance, motion, density;
- preserve/retire list: signature details to keep and generic/broken details to remove;
- SEO/analytics/accessibility risks when public pages or tracked flows are involved.

Never silently change route slugs, primary nav labels, form field names/order,
legal/consent copy, analytics selectors, logo/wordmark, or existing accessible
focus/keyboard behavior.

## Taste Decision Preflight

Before implementing Tier 2/3, redesign, source-inspired, or high-aesthetic UI,
confirm only the taste decisions this contract owns:

- the design read and dials fit the product job and audience;
- source grammar, theme, and any effect archetype serve one thesis;
- likely model-default patterns have an explicit countermeasure;
- redesign preservation boundaries are clear;
- SCE identifies what is removed, what unifies the design, and the one
  proportionate expressive move;
- the aesthetic mechanism translates into layout, type, material, density,
  content, asset, or motion decisions.

This preflight decides whether the direction is ready for implementation. It
does not repeat rendered composition, typography, component, responsive,
state-pressure, or screenshot scoring checks. After implementation,
`frontend-design-contract.md` owns the single holistic aesthetic verdict and
the other contracts verify only their own hard constraints.

## Review And Optimization Use

For review:

- Report missing `taste_control` or weak taste evidence as a finding only when
  visual quality is part of the stated standard or surface type.
- Report a Simple-Coherent-Elegant issue only when unjustified complexity,
  competing visual theses, or uncontrolled decoration weakens the stated user
  goal, rendered hierarchy, workflow, accessibility, maintainability, or product
  identity.
- Do not turn personal taste into a finding. Tie it to the design read,
  anti-default audit, rendered evidence, user goal, or preflight failure.
- For focused code reviews, inspect taste only inside the requested UI surface.

For optimization:

- Prefer changing the smallest control that fixes the taste failure: design
  read, dials, reference choice, visual protagonist, composition, motion role,
  or preflight gate.
- Reject new aesthetic ideas that do not improve intent fit, evidence, or
  robustness. Taste optimization should converge, not endlessly restyle.
