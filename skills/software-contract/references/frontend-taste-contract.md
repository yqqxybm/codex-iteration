# Frontend Taste Contract

Use this reference from `project-frontend`, `review`, or `optimize` when UI
work depends on first-impression quality: landing pages, portfolios, brand
pages, redesigns, product pages, prototypes, high-aesthetic screens, or prior UI
output that looks generic. This contract may also apply to a dashboard or
workspace only for its visual language and first-viewport composition; product
state robustness remains owned by `frontend-quality-contract.md`.

This is a local taste control layer inspired by public anti-generic frontend
skill patterns, but it is not an installed copy and does not create a separate
frontend entry point. It compresses useful taste ideas into this skill system's
resource architecture.

## Purpose

Good frontend taste is not a bigger checklist. It is the ability to read the
brief, choose the right visual language, resist model defaults, and verify the
rendered result against that choice.

This contract adds four controls:

1. **Design read**: infer what kind of surface this is, who it serves, and what
   design language follows from that.
2. **Taste dials**: calibrate variance, motion, and density before coding.
3. **Anti-default audit**: identify likely generic AI habits before they enter
   the implementation.
4. **Taste preflight**: run a compact mechanical check before claiming visual
   quality.

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
  anti_default_risks:
    - <specific generic pattern likely for this brief>
  preservation:
    mode: <greenfield | preserve_existing | overhaul_existing | surgical>
    must_preserve: <brand tokens, IA, routes, analytics, copy voice, accessibility wins>
  taste_preflight:
    status: <pass | needs_revision | blocked>
    failed_checks: <none or exact failures>
```

The final response should report only a compact evidence boundary:

```yaml
taste_contract_evidence:
  design_read: <one sentence>
  dials: <variance/motion/density>
  anti_default_risks_checked: <summary>
  preflight: <pass | revised | blocked>
  not_checked: <none or exact reason>
```

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

## Taste Preflight

Run the relevant checks before claiming a Tier 2/3, redesign, landing,
portfolio, prototype, source-inspired, or high-aesthetic UI is visually done.
This is a targeted preflight, not a full matrix for every UI task.

### 1. Design Read

- `taste_control.design_read` exists and matches the user goal.
- Dials are explicit and reasoned, not silently defaulted.
- Any official design system or aesthetic approximation is named honestly.
- Quiet constraints override aesthetics when they conflict.

### 2. First Viewport

- The first viewport has a clear visual protagonist: product screenshot,
  workflow surface, real/generated image, data visualization, 3D/canvas,
  editorial type composition, or domain object.
- Hero/primary screen content fits the initial viewport on desktop and mobile.
- Primary action or core workflow is visible without hunting.
- Trust/logos/metadata do not crowd the hero unless they are essential to the
  product job.

### 3. Composition

- Section layout families are not repeated mechanically.
- Long zigzag sequences, card piles, nested cards, and one-note bento grids are
  corrected unless the product system requires them.
- Dense operational pages use workbench/table/filter/detail-pane structure
  instead of marketing-section rhythm.
- Bento/grid cell count matches actual content; no blank filler cells.
- Mobile collapse is explicit for every high-variance layout.

### 4. Typography And Color

- Font choice serves the product character, existing system, language support,
  and performance; it is not chosen from habit.
- Palette has one dominant logic and stable accent behavior.
- Shape/radius language is consistent or follows an explicit rule.
- Button, form, and critical text contrast are checked against actual surfaces.
- The result does not read as one-note purple/blue, beige/brown, or dark slate
  unless the brand or source grammar demands it.

### 5. Motion

- Every motion effect has a reason: hierarchy, storytelling, feedback, state
  transition, progress, or spatial continuity.
- GSAP usage, reduced-motion behavior, cleanup, mobile/resize checks, and
  debug-marker absence are governed by `frontend-motion-contract.md`.
- Motion claimed in the design direction is visible in the rendered UI; if
  motion cannot be verified, report it as a blocker or residual risk.

### 6. Assets And Content

- Important visual surfaces use real, generated, source, or product-specific
  assets; fake screenshots and empty rectangles are not treated as final.
- Copy, data, names, and metrics are domain-real enough to make the interface
  judgeable.
- Social proof/logos use real marks or coherent generated marks when relevant;
  plain text wordmark rows are not enough for a polished marketing surface.

### 7. Product-State Robustness

- Loading, empty, error, disabled/forbidden, long-content/list, theme,
  localization, and responsive pressure are covered by
  `frontend-quality-contract.md` when relevant.
- A visually beautiful screen that only works for ideal data is not complete.

## Review And Optimization Use

For review:

- Report missing `taste_control` or weak taste evidence as a finding only when
  visual quality is part of the stated standard or surface type.
- Do not turn personal taste into a finding. Tie it to the design read,
  anti-default audit, rendered evidence, user goal, or preflight failure.
- For focused code reviews, inspect taste only inside the requested UI surface.

For optimization:

- Prefer changing the smallest control that fixes the taste failure: design
  read, dials, reference choice, visual protagonist, composition, motion role,
  or preflight gate.
- Reject new aesthetic ideas that do not improve intent fit, evidence, or
  robustness. Taste optimization should converge, not endlessly restyle.
