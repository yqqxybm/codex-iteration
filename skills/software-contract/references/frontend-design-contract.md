# Frontend Design Contract

Use this reference from `project-frontend`, `project-bootstrap`,
`project-iteration`, `review`, or `optimize` when UI work needs visual quality,
component quality, accessibility, responsive behavior, or rendered visual QA.

This file owns stable frontend design standards. `project-frontend` owns
workflow, implementation, browser verification, and evidence reporting.

## Design Control Principle

A frontend is not good because it follows many visual tips. It is good when the
same design thesis controls typography, color, layout, components, motion,
states, and verification.

The governing quality law is Simple-Coherent-Elegant:

- **Simple**: no visual, structural, or interaction complexity without product
  value.
- **Coherent**: all visible systems serve the same design thesis and workflow.
- **Elegant**: the expressive move is strong, precise, and proportionate rather
  than loud or decorative.

## Universal Aesthetic Integrity

Aesthetic quality is the core criterion and goal of frontend design. It is not a
Tier 2/3 feature, optional polish pass, or peer checkbox that can be traded away.
Every visible decision must contribute to a product-appropriate, coherent,
deliberate, and beautiful whole.

Functionality, accessibility, state robustness, responsive behavior, and
preservation are hard constraints on how that aesthetic goal is realized. They
do not replace it and cannot reduce completion to "works correctly". UI tier
controls workflow breadth; `aesthetic_target` controls the expected visual level
and proof depth. If the assigned scope cannot satisfy the aesthetic goal and
hard constraints together, return `blocked` instead of shipping a visually
weaker substitute.

Use these levels. The `AQ` prefix distinguishes output quality from the
prototype contract's A/B/C source rating:

- **AQ1 local-integrity**: the change preserves or improves the inherited visual
  system. It introduces no regression in proportion, hierarchy, alignment,
  spacing rhythm, typography, material, action emphasis, or interaction
  feedback. AQ1 is a no-regression claim, not a "beautiful", "premium", or
  production-redesign claim.
- **AQ2 production-grade**: the rendered surface is deliberate, coherent, and
  ready to ship. It has strong proportion, hierarchy, typography, material,
  component craft, and product-specific character, with no material
  generic-template weakness.
- **AQ3 benchmark-grade**: the rendered result is comparable to the best
  inspected A-rated reference or explicit visual target for its page role. It
  may be original in style, but it cannot be materially weaker in composition,
  hierarchy, craft, identity, or first-impression control.
- **AQ0 fail**: usable or technically correct but visibly generic, imbalanced,
  inconsistent, unfinished, or weaker than the inherited surface. AQ0 is never
  an acceptable target.

Select the target before implementation:

```yaml
aesthetic_target:
  level: <AQ1 | AQ2 | AQ3>
  inherited_floor: <AQ1 | AQ2 | AQ3 | unknown>
  benchmark: <before screenshot | sibling surface | design system | A-rated reference | visual_target>
  rationale: <why this level fits the user request and surface>
  evidence_required: <local rendered comparison | rendered screenshot | same-context benchmark comparison>
```

Target rules:

- AQ1 is allowed only for an explicit mechanical preservation instruction such
  as moving one icon, changing one literal token, or fixing one alignment while
  keeping the rest unchanged; it may not fall below the inherited floor;
- a vague visible modification such as "改一下", "优化一下", "调整这个弹窗",
  "做个组件", or "让它更好看" is design-quality work, not a mechanical patch.
  Codex must choose and realize an AQ2 design within the authorized surface even
  when the user names only one symptom;
- a new ordinary surface, explicit component aesthetic improvement, or
  high-trust/high-risk component uses at least AQ2;
- a new full page, redesign, Tier 2/3 extreme-quality task, or request for
  "最美/顶级/作品级/源站级" uses AQ3 unless the user explicitly requests a draft;
- preservation limits mutation scope, not aesthetic responsibility. Match the
  best relevant local grammar instead of preserving an accidental defect;
- if the inherited surface is stronger than the default target, the inherited
  level becomes the floor.

### Aesthetic Score Calibration

Score only actual rendered evidence, never code, DOM structure, browser smoke,
or intent. Use six aesthetic axes: composition/proportion, hierarchy/rhythm,
typography, color/material, component craft, and product-specific identity/
anti-generic character.

- **5**: benchmark/source-grade; same-context comparison reveals no material
  weakness on the axis.
- **4**: production-polished; clearly deliberate and shippable, with a named
  non-material delta from the benchmark when one exists.
- **3**: coherent and usable but generic, under-resolved, or visibly behind the
  target.
- **2**: material imbalance, weak hierarchy, inconsistent craft, or obvious
  template treatment.
- **1**: broken, off-brief, or aesthetically unacceptable.

AQ1 passes only with no negative delta against the before/sibling benchmark.
AQ2 requires every active axis to score at least 4 from an actual rendered
view. AQ3 requires every active axis to score at least 4, an average of at least
4.5, and same-context comparison against an A-rated reference or explicit
visual target. A score of 5 must name its benchmark evidence; self-awarded
numbers without a screenshot and comparison delta do not count.

### Holistic Aesthetic Judgment

Task acceptance is necessary but not sufficient for design completion. A
visible change is not done merely because the requested element exists, tests
pass, or the interaction works. Codex must inspect the actual screenshot as a
design and issue an `aesthetic_verdict`.

Judge the screenshot itself. A script that confirms image existence, DOM
metrics, CSS tokens, or automated numeric scores cannot replace visual
inspection. Review the surface as one design before assigning the six calibrated
axis scores:

- composition/proportion includes balance, scale, visual weight, tension, and
  negative space;
- hierarchy/rhythm includes visual path, grid, alignment, spacing, grouping,
  line length, and density;
- typography includes family, size, weight, measure, language rendering, and
  character;
- color/material includes palette, contrast, semantic color, surfaces, borders,
  shadows, and overlays;
- component craft includes icon scale, control geometry, action hierarchy, and
  hover/focus/pending/disabled/destructive expression;
- product identity includes purpose and audience fit, local grammar, anti-
  generic character, and Simple-Coherent-Elegant unity.

Use the smallest screenshot set that proves the claim: one representative
rendered view for AQ2, the relevant local comparison for AQ1, and same-context
benchmark comparison for AQ3. If the judgment finds a material design flaw,
revise the design and replace stale evidence with a new rendered view. Stop when
the latest view has a clean `aesthetic_verdict`; do not accumulate screenshots
or pass counts as a substitute for judgment.

For a bounded AQ2 modification, form a compact design decision before code:

```yaml
component_design_decision:
  surface_job: <what this component helps the user understand or decide>
  aesthetic_problem: <what is visually weak, not only what is functionally missing>
  design_thesis: <one sentence>
  visual_path: <first, second, and final attention>
  proportion_rhythm_move: <the concrete scale, spacing, grouping, or material change>
  local_grammar_preserved: <tokens and component language that still govern>
  failure_tests: <what would mean the result merely works but is not well designed>
```

For Tier 2/3 UI work, form an internal `design_contract` before implementation:

```yaml
design_contract:
  aesthetic_target: <AQ2 | AQ3, inherited floor, benchmark, and evidence requirement>
  art_direction: <one-sentence visual thesis>
  aesthetic_mechanism: <why this UI will be beautiful, not just correct>
  visual_protagonist: <object or workflow surface that owns first impression>
  typography: <display/body/mono choices and why>
  color_system: <dominant color, accent, semantic colors, theme mode>
  layout_model: <density, grid, viewport rhythm, responsive strategy>
  component_rules: <buttons, inputs, cards, navigation, modals>
  accessibility_rules: <contrast, keyboard, labels, semantics, reduced motion>
  simple_coherent_elegant:
    simple: <complexity removed or deliberately kept minimal>
    coherent: <how major choices serve one thesis and workflow>
    elegant: <one expressive move kept and why it is proportionate>
  visual_qa_threshold: <Tier 0 | Tier 1 | Tier 2 | Tier 3>
```

Return only a compact evidence boundary in the handoff:

```yaml
design_contract_evidence:
  aesthetic_target: <level, inherited floor, and benchmark>
  art_direction: <summary>
  aesthetic_mechanism: <summary>
  visual_protagonist: <summary>
  sce_evidence: <simple/coherent/elegant pass | revised | blocked>
  rendered_qa: <viewports/screenshots/commands checked>
  aesthetic_result: <level achieved, six-axis scores or local delta, and comparison evidence>
  score_or_judgment: <pass | weaker with fixes | blocked>
  not_verified: <none or exact reason>
```

For Tier 0/1 work that must match an existing UI, build a smaller local
reference packet instead of a full aesthetic contract:

```yaml
local_style_reference:
  target_component: <dialog | drawer | popover | form | table action | card | toast | empty state | etc.>
  aesthetic_target: <AQ1 minimum or higher target, plus inherited floor>
  local_sources: <existing project files, rendered screens, component docs, screenshots inspected>
  extracted_grammar:
    dimensions: <width buckets, min/max, height, density, viewport rules>
    spacing: <padding, gap, row height, section rhythm>
    structure: <header/body/footer, action placement, close affordance, tabs, sections>
    typography: <title/body/label scale, weight, line-height>
    materials: <surface, border, shadow, radius, overlay, backdrop>
    states: <hover, focus, disabled, loading, error, empty, long content>
    responsive: <mobile/tablet/desktop adaptation>
  external_fill: <component/design-system reference used only if local equivalent is missing>
  aesthetic_delta: <improved | no-regression | regressed>
  fit_judgment: <matches | revised | blocked>
```

Report compact evidence when this packet is used:

```yaml
local_style_evidence:
  aesthetic_target: <level and inherited floor>
  local_sources: <what was inspected>
  extracted: <dimensions/spacing/structure summary>
  aesthetic_delta: <improved | no-regression | blocked>
  external_fill: <none or reference>
  fit_judgment: <matches | revised | blocked>
```

## Simple-Coherent-Elegant Gate

Run a compact version of this gate for every visible design change. Run the
full gate before implementation and again after rendered QA for Tier 2/3,
redesign, dashboard, landing, high-aesthetic UI, or any AQ3 target:

1. **Simplicity**: remove or justify every extra card, section, ornament, motion
   effect, color accent, dense block, and control. If removal preserves or
   improves the workflow, remove it.
2. **Coherence**: check that typography, color, spacing, layout, components,
   content, assets, state handling, and motion point to the same design thesis.
   If two theses compete, choose the one closer to the user goal.
3. **Elegance**: keep one strongest expressive move and polish its proportion,
   hierarchy, rhythm, and feedback. Replace multiple weak flourishes with one
   controlled protagonist.

Do not use this gate to make every UI minimal. Operational workspaces may stay
dense; editorial or brand pages may stay expressive. The test is whether the
complexity is controlled by the product job.

## Aesthetic Generation Gate

For Tier 2/3, dashboard/admin/workbench, redesign, landing, product page,
source-inspired, or high-aesthetic UI, the design is ready for code only after
it names an aesthetic mechanism. Valid mechanisms include composition tension,
precision grid, instrument-like data density, material contrast, typography
rhythm, product object scale, real image/asset presence, semantic status
choreography, or motion that clarifies hierarchy.

A plan fails this gate if it only names a theme, palette, source, checklist, or
"premium" mood. It must state the transferable mechanism plus code-level
translation: layout, type, color/material, component density, content/data, and
motion or asset choice. If the rendered result reads as a generic card grid, KPI
wall, sidebar shell, or table skin, the mechanism is missing or untranslated.

## Anti-Template Aesthetic

High-risk defaults that usually need correction:

- generic `hero + three cards + CTA` structure without product-specific object;
- no first-viewport visual protagonist;
- large gray-blue, blue-purple, or purple-gradient surfaces without domain
  reason;
- floating card sections, card-in-card layouts, or cards over 8px radius unless
  the existing design system requires it;
- placeholder-like copy, data, or empty workflows;
- repeated cross-project font/color/layout choices that ignore domain context.

Corrective rules:

- Choose typography from the product's character, not from habit. System fonts
  are valid when platform, performance, existing design system, or Chinese font
  availability makes them the best fit.
- Make one color family or material direction carry the visual weight. Do not
  distribute many accents evenly.
- Match density to workflow. SaaS, CRM, admin, audit, logs, and operations
  surfaces should be scan-dense and restrained; editorial, portfolio, game, or
  brand pages can be more expressive.
- Use composition deliberately: asymmetry, overlap, split workbench, dense
  table, command surface, narrative scroll, or product-led first viewport only
  when it improves the specific domain.
- Every major visual decision should trace back to the same art direction.

## Design Tokens

When there is no existing design system, create the smallest useful token set:

```text
--color-bg
--color-surface
--color-text
--color-text-secondary
--color-accent
--color-accent-hover
--color-border
--color-success / --color-warning / --color-error when needed

--font-display
--font-body
--font-mono when needed

--text-xs / --text-sm / --text-base / --text-lg / --text-xl
--text-2xl / --text-3xl / --text-4xl

--space-1 / --space-2 / --space-3 / --space-4
--space-5 / --space-6 / --space-8 / --space-10
--space-12 / --space-16 / --space-20 / --space-24

--radius-sm / --radius-md / --radius-lg / --radius-full
--shadow-sm / --shadow-md / --shadow-lg
```

Prefer 4px or 8px spacing rhythm. Cards default to 8px radius or less unless
the existing system requires another radius.

## Component Baseline

Before creating or changing a visible component inside an existing product,
inspect local equivalents first. Match the product's actual component grammar
before seeking outside inspiration. This is mandatory for dialogs, drawers,
popovers, forms, table actions, settings panels, navigation items, toasts,
empty/error states, and compact cards.

Local style matching means copying the system, not cloning one file blindly:
reuse tokenized widths, spacing rhythm, radius, borders, shadows, title scale,
footer/action order, density, state treatment, and responsive behavior. If the
project has no equivalent component, use a component/block library or official
design-system reference as `external_fill`, then translate it into the project's
tokens and visual language. Good external fill sources include Tailwind UI,
Flowbite Blocks, shadcn/ui blocks, Untitled UI, Tremor, Radix UI examples,
React Aria examples, Material, Fluent, Carbon, Polaris, Primer, and Atlassian
Design System.

Envato/ThemeForest can fill local component gaps only after local/sibling UI is
checked. Rate external component references before using them:

- **A**: mega admin kits and maintained Tailwind/headless/admin kits for modal,
  auth, settings, pricing, table/list, wizard, drawer, toast, and form state
  patterns.
- **B**: app-specific modules and Figma/Sketch dashboard kits for local
  structure, spacing, and variants; translate interaction and accessibility
  yourself.
- **C**: old Bootstrap/jQuery/stock-heavy admin templates; use only as
  anti-patterns or tiny spacing/component cues.

Use Envato component references for dimensions, arrangement, density, states,
and component grammar, not for code, brand skin, images, or plugin stack.

## Data Visualization Style Routing

Chart style must follow the data job, not visual novelty.

Precise dashboards, finance, operations, security, monitoring, compliance,
audit, and SLA/SLO surfaces require serious chart behavior: accurate axes,
legends, labels, tooltips, tables or drill-downs when needed, responsive
constraints, and a maintained charting stack such as the project's existing
library, Tremor, Recharts, ECharts, Observable Plot, D3, or an equivalent.

Rough/sketch chart language, including roughViz-style visuals, is appropriate
only when the communication goal is intent, generality, early concept,
education, editorial storytelling, or a creative/portfolio tone where exact
numeric precision is not the primary promise.

If a rough/sketch chart is used:

- record why precision is not the primary job of that chart;
- keep labels and fallback text clear enough that users are not misled;
- verify responsive sizing and legibility;
- do not use it for alarms, financial figures, monitoring, audit evidence,
  security risk, SLA/SLO status, compliance, or exact KPI decisions.

Buttons:
- minimum target 44x44px, or 48x48dp on touch-first mobile;
- visible hover, active, focus, disabled, and pending states;
- primary and secondary actions have clear visual hierarchy.

Inputs:
- visible label; placeholder alone is not a label;
- visible focus state;
- error state includes border or icon plus text, not color alone.

Cards:
- use consistent `gap`, not margin hacks;
- clickable cards need feedback;
- long content needs truncation, wrapping, or scroll strategy.

Navigation:
- active state must be clear;
- mobile navigation follows information architecture, not a fixed template;
- keep hierarchy shallow unless the product is a complex workspace.

Dialogs:
- provide overlay, close affordance, keyboard handling, and internal scrolling
  for long content.
- match existing modal/sheet dimensions before inventing new ones: width bucket,
  max-height, header/body/footer padding, title scale, close button placement,
  destructive/primary action order, overlay opacity, radius, shadow, and mobile
  full-screen or bottom-sheet behavior.

## Accessibility And Responsive Rules

Accessibility minimum:
- body text contrast at least WCAG AA level in normal conditions;
- keyboard can reach and activate all interactive controls;
- icon-only buttons have accessible names;
- meaningful images have alt text; decorative images use empty alt;
- semantic landmarks/headings are used where appropriate;
- focus is visible;
- color is never the only carrier of meaning;
- reduced-motion strategy exists when motion exists.

Responsive minimum:
- mobile-first constraints or equivalent responsive strategy;
- no horizontal overflow at relevant breakpoints;
- body text at least 16px on mobile-form surfaces to avoid iOS zoom;
- line length remains readable;
- touch targets are large enough and separated;
- mobile hides or reprioritizes secondary content instead of merely shrinking
  desktop layout.

## Rendered QA

Every visible design change requires rendered inspection before claiming an
aesthetic pass. Match evidence to the selected target:

- AQ1: inspect the changed surface at its primary viewport and compare it with a
  before view or the strongest relevant sibling/local component. Record the
  visual delta; code inspection alone cannot prove no regression.
- AQ2: capture the actual rendered surface and apply the calibrated six-axis
  aesthetic score.
- AQ3: capture the actual rendered surface and compare it in the same visual
  context with the selected A-rated reference or explicit visual target.

Tier 2/3 tasks additionally require this full rendered workflow:

1. Start the dev server or open the runnable HTML target.
2. Inspect at least desktop and about 375px mobile width.
3. Capture screenshots or inspect the real rendered UI with browser tooling.
4. If rendering reveals a material issue, return to the controlling design
   decision, revise it, and replace the stale rendered evidence; if the verdict
   is clean, stop without manufacturing another round.
5. If rendering is blocked, report the blocker and the strongest static checks
   actually completed. Do not convert static checks into an aesthetic pass.

Use the right screenshot evidence for the claim. First-viewport aesthetics and
composition should be judged from viewport screenshots at the target size;
full-page screenshots are secondary evidence for scroll continuity, long
content, and below-fold layout. If a screenshot appears to contradict DOM
metrics, element hit tests, viewport size, or another screenshot mode, treat the
first failure as a capture/tooling ambiguity. Re-capture with the correct
viewport, record the conflicting evidence, and only then classify the issue as
UI implementation, aesthetic, or responsive failure. Do not patch the UI or the
skill from a single contradictory screenshot.

Use `Holistic Aesthetic Judgment` once for the rendered design, then apply
`Aesthetic Score Calibration`; do not rerun the same principles as another
checklist. Separately verify only non-overlapping evidence: required assets
actually load, active content/state checks are truthful, and responsive
adaptation does not introduce overlap, truncation, horizontal scroll, unusable
controls, or a materially weaker composition. These hard constraints do not
raise an aesthetic score or excuse a lower one. Score another viewport only
when its composition materially differs.

Rendered visual QA is not browser smoke. `browser_smoke` may use the same
browser session or screenshot, but it only proves runtime reachability, fatal
error absence, assigned interaction viability, and blocking viewport/overflow
issues. Aesthetic checks such as art direction, composition, hierarchy, and
craft remain separate evidence and are mandatory for every visible mutation.
Domain-real copy/content checks run when `content_copy_qa` or the selected UI
contract requires them.

AQ2/AQ3 require a clean holistic verdict from the latest rendered evidence or
an explicit environment blocker.

`state_pressure_qa` still comes from `frontend-quality-contract.md`. Motion QA
still comes from `frontend-motion-contract.md`. Theme/source comparison comes
from `frontend-theme-contract.md` and `frontend-prototype-reference-contract.md`.
