# Frontend Theme Contract

Use this reference from `project-frontend`, `project-bootstrap`,
`project-iteration`, `review`, or `optimize` when a UI task needs a concrete
aesthetic direction beyond generic "modern / beautiful / high quality" wording.

## Philosophy

Frontend themes are not decorative keywords. They are compact design control
surfaces: they translate aesthetic intent into layout, typography, color,
visual protagonist, component behavior, state pressure, and failure modes.

Keep the core frontend skill responsible for workflow and verification. Keep
theme details here so aesthetic variants can evolve without bloating
`project-frontend/SKILL.md`.

## Theme Contract Schema

```yaml
theme_contract:
  theme_id: <stable id>
  art_direction: <one-sentence aesthetic direction>
  source_grammar: <source-webpage design grammar to extract before drawing>
  best_for: <project/page types>
  avoid: <anti-patterns>
  visual_protagonist: <what owns the first impression>
  composition_archetype: <page structure that should differ from generic templates>
  typography: <font and hierarchy intent>
  color: <background, dominant color, accent, semantic colors>
  layout: <composition and density>
  components: <controls, cards, tables, navigation, motion>
  required_states: <loading, empty, error, long content, mobile, etc.>
```

## Invocation And Evidence

When the user says "主题设计模式", "源站级审美", "源网站对比",
"像 Linear / Apple / Notion / Fluent / Datadog", or names any fixed theme, the
calling frontend skill should treat this file as the active theme control
surface.

Return only a compact evidence boundary, not the whole library:

```yaml
theme_evidence:
  theme_id: <selected fixed theme or custom>
  source_grammar_checked: <source page, local screenshot, or unavailable reason>
  pages_compared: <landing/login/workbench/etc.>
  aesthetic_judgment: <materially matches | weaker with fixes | blocked>
  not_compared: <none or exact reason>
```

## Prompt Stability Rule

A theme is not stable until it can produce several page samples with different
content pressures without collapsing into the same skeleton. Do not treat a
keyword as sufficient evidence of theme quality.

Session-use rule: after this reference is edited, the current Codex session
does not automatically reload it as a skill instruction. When the user asks for
frontend prompt optimization in the same session, explicitly use the updated
prompt text as a user-level design constraint: build the internal
`theme_contract` first, then implement the UI according to that contract.

For source-inspired themes, do not copy only colors, fonts, or radius. Extract
the source-webpage grammar first: first-viewport ratio, navigation hierarchy,
product screenshot or real-asset scale, component tokens, material/motion cues,
information weight, whitespace, and the object that owns persuasion. If several
themes would still produce the same page skeleton with different colors, the
prompt is not optimized.

For prompt/theme optimization, source comparison is mandatory evidence. Compare
desktop screenshots against the real source site or design-system page before
claiming a theme is "good enough". If the available source screenshot is a docs
page, brand guideline, failed capture, or otherwise weaker than the intended
reference, treat it as weak evidence and prefer the strongest live source page
that represents the theme's first-class aesthetic. Check page skeleton, visual
protagonist scale, navigation hierarchy, type weight, component grammar,
information density, whitespace strategy, and business translation.

For Tier 2/3 work or prompt/theme optimization, validate the theme against at
least these three sample modes when practical:

- `landing`: first impression, visual protagonist, narrative structure.
- `workspace`: real product workflow, controls, navigation, and data.
- `pressure`: loading, empty, error, long content, authority, and mobile.

If the samples share the same `hero + three cards + CTA` structure, or if the
pressure sample only changes colors while losing theme identity, the theme
contract is under-specified. Strengthen composition, protagonist, state, and
anti-pattern rules before claiming the prompt is stable.

## Selection Rule

If the user gives a theme word, select the closest fixed theme and preserve the
user's word as intent. If multiple themes fit, choose the one that best serves
the product type and user workflow. Do not combine more than two themes unless
the user explicitly asks; hybrids easily lose aesthetic coherence.

When the project already has a strong design system, treat these themes as
inspiration only and preserve the existing system.

## Execution Prompt

Use this compact prompt internally before implementing Tier 2/3 frontend work
with any fixed theme:

```text
Build a production-grade, desktop-first frontend. Do not start from a generic
template.

Before code, form an internal theme_contract:
1. source_grammar: extract first-viewport ratio, navigation hierarchy, product
   screenshot or real-asset scale, component tokens, information weight,
   whitespace, material, and motion from the specified source/design system.
2. composition_archetype: choose a theme-specific page skeleton. It must not
   collapse into the same hero + cards + CTA, left-copy/right-mockup, or generic
   dashboard skeleton used by other themes.
3. visual_protagonist: define what real object owns the first impression and
   core workbench: product screenshot, workflow, data object, editorial object,
   instrumented system object, mobile task surface, or dense operations surface.
4. business_translation: translate the business object into the source grammar;
   do not paste source decoration onto the business.
5. failure_tests: fail and redesign if the result only changes color, font, or
   radius; uses generic marketing copy; lacks real workflow; stacks cards; or
   looks materially weaker than the source reference in desktop screenshots.

After implementation, inspect desktop screenshots page by page for composition,
hierarchy, type, color, source-webpage quality, real business object, and
operability. Fix prompt-control problems first; edit implementation only when
the prompt is already correct but the page did not follow it. Mobile is a
fallback check unless the user makes it primary.
```

## Page-Level Desktop Gates

Every fixed theme must satisfy page-level desktop gates. A beautiful landing
page is not enough.

```text
landing gate: the first viewport must express the source-webpage grammar. Do
not default to left copy + right small mockup. Linear-like sources may use black
field + giant title + dimmed product screenshot; Datadog-like sources must make
the product dashboard more dominant than copy; HIG/Fluent/Notion-like sources
must look like real documentation/application systems, not marketing heroes.
For HIG, Fluent, and Notion source grammar, the source shell itself must own the
landing page. Do not keep a separate marketing hero above an embedded workbench.
Linear/AI landing pages must not place ordinary KPI/proof cards over the dimmed
product surface. Commercial SaaS/Datadog landing pages must give the product
visual more weight than copy or proof cards.

login gate: the sign-in page must preserve the theme, not fall back to a generic
form. Keep business context visible through native sheets, enterprise workbench
access, dark secure console, mobile task authentication, editorial access brief,
or premium instrument unlock depending on the theme. Different themes must not
share the same oversized marketing headline + left context + right form
skeleton; form placement, title scale, context object, and control grammar
should change with the source webpage.

monitor/workbench gate: the core workbench must be the theme's strongest page.
Different themes must not share one sidebar + metrics + grid + detail rail
skeleton. Datadog/Grafana must be dashboard-first; Fluent must be command bar +
evidence/detail; Notion must be sidebar/page/database block; Material must be
touch-first task surface; Linear/AI must be trace/checkpoint/workflow-first;
luxury must turn the system object into a precision instrument; editorial must
be a readable live brief.

current failure tests: fail if several themes only recolor the same layout; if
the product object becomes decoration; if the core object is placed inside an
unrelated small panel instead of owning the page; if charts, tables, or system
screens have large empty regions; if screenshots are clipped so key content is
lost; if Material desktop looks like a narrow phone floating in empty space or
clips its companion context; if commercial SaaS lacks a large credible product
visual; if editorial/luxury/commercial pages rely on color and type without a
strong asset, product object, publication image, or high-fidelity physicalized
system object; or if HIG/Fluent/Notion still read as ordinary landing/dashboard
pages.

layout ownership gate: the visual protagonist must control the page skeleton,
not merely appear as a component inside a generic skeleton. A theme may replace
the whole landing/login/monitor structure with its source-webpage grammar:
HIG/Fluent/Notion do not need a huge marketing headline column; Datadog-like
systems may let the dashboard occupy most of the viewport; Linear/AI may stage
a dimmed product surface below the claim. Do not preserve a shared code layout
when it weakens the source grammar.

workbench density gate: operational, monitoring, and power-user workbenches
must close their grids. Every column track should carry a real business object:
charts, queues, logs, runbooks, SLOs, resource matrices, approval state, or
audit evidence. Do not leave large right-column or lower-viewport blanks as a
layout artifact. Density must improve scan speed, not merely simulate complexity.
```

## Fixed Themes

### platform-native-clarity

- Triggers: 苹果风, Apple-like, iOS, macOS, platform-native.
- Best for: personal tools, settings, lightweight productivity, native-feeling apps.
- Avoid: white page + oversized rounded cards + glass blur as a shallow Apple imitation.
- Visual protagonist: actual workflow, content object, or clean application shell.
- Source grammar: Apple HIG quality, with two-level navigation, stable content
  width, toolbar/content/inspector hierarchy, high-quality resource tiles, and
  harmony/consistency as visible structure.
- Composition archetype: native app shell with toolbar, focused content pane,
  inspector/detail surface, and calm state continuity. For landing pages, the
  native shell must own the whole page instead of preserving an external
  marketing headline column.
- Typography: system-like clean sans; strong hierarchy, low visual noise. Avoid
  heavy display fonts, all-caps mono navigation, and retro brand buttons.
- Color/layout: restrained palette, generous whitespace, soft surfaces, subtle depth.
- Required states: loading, empty, error, long content, mobile, dark mode.

Prompt core:

```text
Use platform-native-clarity with Apple HIG source grammar: two-level native
navigation, stable content width, toolbar, content pane, inspector/detail
surface, high-quality resource tiles, clear hierarchy/harmony/consistency, and
system semantic color. The first impression must be a real workflow or core
content object organized like a high-quality native app or developer-system
page. Do not reduce Apple style to white backgrounds, oversized rounded cards,
glass blur, heavy display type, all-caps mono navigation, or retro buttons.
```

### precision-developer-console

- Triggers: Linear 风, Vercel 风, developer tool, console, terminal, engineering.
- Best for: developer tools, AI agent consoles, logs, deployment, API platforms.
- Avoid: black background with random glowing cards.
- Visual protagonist: commands, task traces, logs, code, API state, data flow.
- Source grammar: Linear quality, with black field, oversized hero claim,
  dimmed product screenshot below the fold, fine borders, low-noise nav, and
  engineering evidence as atmosphere.
- Composition archetype: trace console with command rail, live log surface,
  checkpoint/status pane, and failure boundary.
- Typography: mono for operational data; crisp sans for labels and navigation.
- Color/layout: dark or near-black, fine dividers, strong grid, sparse accent.
- Required states: long logs, pending, failed, success, readonly/forbidden, mobile compression.

Prompt core:

```text
Use precision-developer-console with Linear source grammar: black field,
oversized hero claim, dimmed product screenshot under the fold, fine dividers,
low-noise navigation, and real commands/logs/traces/checkpoints as the visual
protagonist. Make engineering structure itself beautiful. Avoid glow-card
cyberpunk, equal-weight dashboard cards, and foreground KPI/proof cards that
interrupt the dimmed product surface on the landing page.
```

### commercial-saas-narrative

- Triggers: Stripe 风, Framer 风, modern SaaS, startup landing page.
- Best for: SaaS marketing sites, AI tool landing pages, pricing and conversion pages.
- Avoid: generic gradient hero plus three feature cards.
- Visual protagonist: product screenshot, workflow diagram, data flow, or credible abstract product graphic.
- Source grammar: Stripe/Datadog quality, with a large credible product visual,
  platform IA, proof metrics, restrained brand field, component clarity, and
  conversion story carried by the product.
- Composition archetype: commercial narrative page led by product workflow,
  followed by proof, conversion, pricing, or case structure. Critical product
  UI must stay readable; do not crop away the evidence that makes the screenshot
  persuasive.
- Typography: polished commercial sans with strong hero scale and readable body.
- Color/layout: one dominant brand color, one accent, clear story sections.
- Required states: mobile hero, real copy, pricing/case section, clear CTA.

Prompt core:

```text
Use commercial-saas-narrative with Stripe/Datadog source grammar: large
credible product screenshot or workflow visual, clear platform IA, proof
metrics, restrained but memorable brand field, polished commercial type, and
business-value narration grounded in real product language. The hero must
persuade through product evidence, not gradients or generic feature cards. Copy
and proof cards must not outweigh the product surface; integrate proof into
customer impact, platform evidence, or the product visual.
```

### quiet-productivity-workspace

- Triggers: Notion 风, document workspace, knowledge base, productivity.
- Best for: notes, task management, docs, light collaboration, editors.
- Avoid: empty white document mockups with no operations.
- Visual protagonist: organized content blocks, sidebar, search, inline operations.
- Source grammar: Notion quality, with sidebar, page/block structure, inline
  metadata, lightweight database, restrained monochrome system, and content
  organization as the design event.
- Composition archetype: quiet document workspace with sidebar, block editor,
  ownership metadata, and inline actions. For landing pages, the page/database
  object must own the whole composition instead of sitting beside an external
  marketing column.
- Typography: calm readable sans; subtle hierarchy.
- Color/layout: low-saturation neutrals, block rhythm, clear navigation.
- Required states: long text, empty page, search, readonly, pending edit, mobile reading.

Prompt core:

```text
Use quiet-productivity-workspace with Notion source grammar: sidebar, page/block
structure, inline metadata, database-like records, restrained color, and visible
ownership. Calmness must organize real work and keep risk, owner, next action,
and long content readable. The page/database object must own landing pages;
do not add a separate marketing hero above it. Do not create an empty document
mockup.
```

### material-mobile-expressive

- Triggers: Material 3, Android, mobile-first, expressive.
- Best for: mobile apps, cross-platform consumer tools.
- Avoid: rounded colorful cards without navigation or state logic.
- Visual protagonist: task screen with top/bottom navigation, touch actions, or surfaced content.
- Source grammar: Material 3 Expressive quality, where color, shape, size,
  motion, and containment jointly guide emotion and usability.
- Composition archetype: mobile task surface with top app bar, bottom navigation,
  chips/FAB only when they serve the workflow, and touch-first state feedback.
  Desktop is a readable extension of the task surface; companion context must
  not be clipped into decoration. Companion metric summaries should stack
  vertically or in a compact two-column layout, not reuse a horizontal desktop
  metric strip inside a narrow panel.
- Typography: mobile-readable scale; tokenized type and spacing.
- Color/layout: dynamic color feel, clear surfaces, touch-friendly shapes.
- Required states: touch size, focus, disabled, loading, empty, error.

Prompt core:

```text
Use material-mobile-expressive with Material 3 Expressive source grammar: color,
shape, size, motion, and containment must guide touch-first task decisions.
Use meaningful chips, primary action/FAB only when workflow-driven, bold state
hierarchy, and clear surface levels. Desktop should feel like a natural Material
task extension, not a shrunken admin table or random colorful cards. Keep
companion context readable with stacked or two-column state summaries, never
clipped horizontal metric strips.
```

### fluent-enterprise-workbench

- Triggers: Fluent, Microsoft, enterprise, office, B2B.
- Best for: enterprise tools, admin, permissions, configuration, collaboration.
- Avoid: dull generic dashboard or marketing hero.
- Visual protagonist: command bar + data workspace + detail surface.
- Source grammar: Fluent 2 quality, with component-token clarity, command bar,
  accessible data workspace, evidence/detail pane, stable feedback states, and
  enterprise information architecture.
- Composition archetype: enterprise workbench with command bar, data table/list,
  detail/evidence pane, and accessible state controls. For landing pages, the
  workbench/document information architecture must own the whole page instead of
  preserving an external marketing headline column.
- Typography: neutral readable sans, high accessibility.
- Color/layout: calm surfaces, fine dividers, stable density, subtle depth.
- Required states: keyboard access, long lists, errors, forbidden, disabled, mobile fallback.

Prompt core:

```text
Use fluent-enterprise-workbench with Fluent 2 source grammar: command bar,
component-token clarity, accessible data workspace, evidence/detail pane, stable
feedback states, and enterprise accountability. Make it feel like a production
Microsoft-grade workbench; the source workbench/document shell must own landing
pages. Avoid dull generic admin UI or marketing hero layout.
```

### editorial-brand-story

- Triggers: editorial, magazine, brand story, portfolio, art direction.
- Best for: brand pages, portfolios, people pages, content features.
- Avoid: card collage that loses narrative rhythm.
- Visual protagonist: large type, strong image/object, or editorial composition.
- Source grammar: Apple Newsroom or premium editorial quality, with strong title
  rhythm, asymmetric grid, captioned object/image, strict whitespace, and
  evidence shaped into a story.
- Composition archetype: editorial asymmetry with type-as-image, object panel,
  and paced narrative sections. At least one first-viewport object should read
  like a news image, annotated hero image, publishable information graphic, or
  strong real-content asset; type and beige tone alone are not enough.
- Typography: display serif or distinctive display face plus readable body.
- Color/layout: strong contrast, asymmetry, deliberate whitespace.
- Required states: mobile type fit, no overflow, real content, accessible contrast.

Prompt core:

```text
Use editorial-brand-story with Apple Newsroom source grammar: strong title
rhythm, asymmetric editorial grid, captioned evidence object, strict whitespace,
and narrative pacing. If the domain is operational, translate evidence into a
premium live brief with annotations and a strong image/object asset. Do not
recolor a dashboard beige, rely only on serif type, or bury product readability
under literary styling.
```

### luxury-product-focus

- Triggers: luxury, premium, high-end, jewelry, fragrance, architecture, boutique.
- Best for: high-end product/service showcase.
- Avoid: cheap black-gold gradients, excessive glow, big rounded UI cards.
- Visual protagonist: product/material quality, photography, fine detail.
- Source grammar: Apple Vision Pro or high-end product-page quality, with
  full-bleed product stage, sparse copy, real material/light, precision labels,
  disciplined CTA, and slow premium pacing.
- Composition archetype: product stage with fine labels, purchase/booking action,
  material close-up, and minimal surrounding UI. Non-physical domains must still
  physicalize the core system object into a product-like instrument that could
  plausibly be photographed at hero scale.
- Typography: refined serif or restrained sans; small precise labels.
- Color/layout: quiet dark or ivory surface, hairlines, low-saturation metal accent.
- Required states: product detail, purchase/booking CTA, mobile hero, readable contrast.

Prompt core:

```text
Use luxury-product-focus with Apple Vision Pro source grammar: full-bleed
product stage, sparse copy, material depth, precision labels, disciplined CTA,
and a high-quality product or instrument object as the visual protagonist. If
the domain is not a physical product, turn the core system object into a precise
premium instrument with large-scale material presence. Avoid cheap black-gold
gradients, excessive glow, and stacked UI cards.
```

### ai-control-room

- Triggers: AI 风, AI product, agent, workflow automation, model platform.
- Best for: AI agents, RAG, automation, tool calling, task orchestration.
- Avoid: purple neon, glowing orbs, sci-fi decoration without workflow.
- Visual protagonist: context panel, tool calls, checkpoints, model state, editable result.
- Source grammar: Linear AI workflow quality, with AI embedded in issue/context,
  tool trace, checkpoint timeline, approval boundary, editable result, and
  controlled intelligence rather than decoration.
- Composition archetype: AI operations room with context rail, tool trace,
  checkpoint cards, approval boundary, and editable output.
- Typography: structured system labels, mono for traces.
- Color/layout: controlled dark or light workspace, clear state tokens.
- Required states: pending, failed tool call, empty context, long output, permission limits, mobile.

Prompt core:

```text
Use ai-control-room with Linear AI workflow source grammar: AI lives inside
context rail, tool trace, checkpoint timeline, approval boundary, and editable
result. Show controlled intelligence in the user's real workflow. Do not reuse
a generic topology, dashboard, or dimmed product screenshot skeleton as the AI
visual protagonist; the first viewport must show how the agent reads context,
calls tools, waits for approval, and produces an editable result. Avoid
blue-purple neon, glowing orbs, and generic AI decoration.
```

### operational-density

- Triggers: dashboard, CRM, audit, customer service, finance, monitoring, admin.
- Best for: high-frequency professional tools and power-user workspaces.
- Avoid: marketing hero, oversized cards, sparse fake data.
- Visual protagonist: scan-efficient table/list/workbench with sticky controls
  and closed grid columns.
- Source grammar: Datadog/Grafana quality, with large dashboard protagonist,
  time range/filter bars, metric/log/trace relationship, dense status matrix,
  semantic status color, and rapid scanning as the aesthetic.
- Composition archetype: power-user workbench with sticky filters, compact
  toolbar, dense rows, batch action, detail drawer, semantic status, and no
  unused lower/right grid regions.
- Typography: compact readable sans, tabular numbers where useful.
- Color/layout: neutral surfaces, semantic status colors, strong alignment.
- Required states: long list, long text, loading, empty, error, forbidden, disabled, mobile fallback.

Prompt core:

```text
Use operational-density with Datadog/Grafana source grammar: large dashboard
protagonist, time range and filter bars, metric/log/trace relationship, dense
rows, semantic status color, batch actions, detail drawer, and closed grid
columns where every visible track carries a real operational object. Optimize
scan speed and decision clarity. Avoid marketing filler, oversized cards,
sparse fake data, decorative mini-charts, and blank layout residue.
```

## Review Questions

When reviewing a themed UI, ask:

- Did the theme materially change layout, type, color, and component behavior?
- Did the implementation extract source-webpage grammar, rather than copy only color/font/radius?
- Did the theme materially change composition archetype, not just colors?
- Is there a visual protagonist appropriate to the product?
- Are anti-patterns from the chosen theme avoided?
- Does the UI Contract cover state pressure and mobile behavior?
- Would a different theme produce a visibly different but equally coherent result?
