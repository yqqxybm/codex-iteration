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

For Tier 2/3 UI work, form an internal `design_contract` before implementation:

```yaml
design_contract:
  art_direction: <one-sentence visual thesis>
  visual_protagonist: <object or workflow surface that owns first impression>
  typography: <display/body/mono choices and why>
  color_system: <dominant color, accent, semantic colors, theme mode>
  layout_model: <density, grid, viewport rhythm, responsive strategy>
  component_rules: <buttons, inputs, cards, navigation, modals>
  accessibility_rules: <contrast, keyboard, labels, semantics, reduced motion>
  visual_qa_threshold: <Tier 0 | Tier 1 | Tier 2 | Tier 3>
```

Return only a compact evidence boundary in the handoff:

```yaml
design_contract_evidence:
  art_direction: <summary>
  visual_protagonist: <summary>
  rendered_qa: <viewports/screenshots/commands checked>
  score_or_judgment: <pass | weaker with fixes | blocked>
  not_verified: <none or exact reason>
```

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

Tier 2/3 tasks require rendered inspection before claiming completion:

1. Start the dev server or open the runnable HTML target.
2. Inspect at least desktop and about 375px mobile width.
3. Capture screenshots or inspect the real rendered UI with browser tooling.
4. Fix at least one round of material issues found in rendering.
5. If rendering is blocked, report the blocker and the strongest static checks
   actually completed.

Visual QA checks:
- first viewport has a visual protagonist or clear workbench object;
- hierarchy makes the primary action/content obvious within a few seconds;
- typography, spacing, and color fit the selected art direction;
- content looks domain-real, not placeholder-like;
- images, icons, charts, and motion load and align correctly;
- mobile has no overlap, truncation, horizontal scroll, or unusable controls.

Tier 2 should pass all material checks. Tier 3 / extreme quality should complete
two visual QA passes or report an explicit environment blocker.

State and pressure QA still comes from `frontend-quality-contract.md`. Motion QA
still comes from `frontend-motion-contract.md`. Theme/source comparison comes
from `frontend-theme-contract.md` and `frontend-prototype-reference-contract.md`.
