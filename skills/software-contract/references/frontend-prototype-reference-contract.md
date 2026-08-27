# Frontend Prototype Reference Contract

Use this reference from `project-frontend`, `project-bootstrap`,
`project-iteration`, `review`, or `optimize` when prompt-only theme guidance is
not enough to produce a beautiful UI, when the user asks for "原型参考",
"优秀设计参考", "不要只靠 prompt", "源站级审美", or when Tier 2/3 frontend work
needs stronger composition control. The default is automatic reference
discovery: the user should not need to provide prototype sites.

The user's default preference is highest practical quality on the first pass.
For new screens, full pages, redesigns, dashboards, landing pages, prototypes,
or theme-driven work, treat prototype reference as a normal requirement rather
than an optional enhancement.

## Philosophy

Aesthetic quality is hard to stabilize with adjectives alone. A strong frontend
workflow should use observable design evidence:

1. **Source grammar**: the real site, design system, or product class that
   defines the aesthetic language.
2. **Prototype archetype**: an excellent page/screen/reference prototype whose
   layout, density, hierarchy, and visual protagonist can be studied before
   implementation.
3. **Aesthetic mechanism**: the concrete source of beauty translated into
   layout, material, typography, density, assets, motion, or content.
4. **Rendered final UI**: the actual product page, inspected against the
   aesthetic mechanism and visual target instead of judged from intention.

The prototype is not copied. It is a control sample for composition quality.
Extract structure, proportion, density, and interaction logic; translate the
business object into that structure.

## Prototype Reference Packet

Build this packet internally before implementing Tier 2/3 work when this
contract applies:

```yaml
prototype_reference_packet:
  page_role: <landing | login | dashboard | workbench | form | mobile task | etc.>
  source_pool_mode: <shortlist | batch_audit | single_mandatory_source | local_reference>
  reference_sourcing:
    source_classes_checked: <template_marketplace | inspiration_gallery | real_product | design_system | app_flow | component_block | prompt_effect_gallery | local_reference>
    candidates: <inspected references with category, page role, access status, and A/B/C rating when network/local sources allow>
    disqualified_sources: <verification/auth/404/paywall/business-mismatch sources and reasons>
    selected_primary: <best composition/control sample>
    selected_secondary: <optional source grammar, flow, or component sample>
    unavailable_reason: <none or exact blocker>
  source_grammar: <source screenshot/site/design system, or unavailable reason>
  prototype_reference: <local prototype, source screen, gallery sample, or generated scratch prototype>
  why_selected: <why this reference fits the business and page role>
  extracted_skeleton:
    viewport_structure: <first viewport ratio and dominant regions>
    visual_protagonist: <object that owns the page>
    navigation_model: <nav/sidebar/command bar/tabs/etc.>
    density_model: <sparse editorial | product-led | scan-dense | touch-first>
    component_grammar: <cards/tables/forms/charts/detail panes/buttons>
    hierarchy_rules: <type scale, contrast, whitespace, grouping>
  aesthetic_mechanism: <what makes this reference beautiful and how it transfers>
  business_translation: <how user domain objects map into the skeleton>
  do_not_copy: <brand marks, exact assets, literal copy, protected visuals>
  comparison_result: <aesthetic target, material reference delta, matches | weaker and revised | blocked>
```

## Visual Target Gate

The prototype packet explains where the design evidence comes from. The visual
target is the executable control surface produced from that evidence. For
Tier 2/3, full-page, dashboard/admin/workbench, source-inspired, high-aesthetic,
or visually ambitious UI work, build an `aesthetic_generation_packet` and
`visual_target` before implementation and carry both into
`frontend_control_evidence`.

Reference extraction must feed the aesthetic generation packet, not only a
target description. The packet names the transferable source of beauty and the
code decisions that will express it in the current product.

```yaml
aesthetic_generation_packet:
  from_reference: <prototype_reference_packet id or none>
  beauty_mechanism: <composition/proportion/material/type/data density/asset/motion/interaction>
  implementation_translation:
    layout: <grid, regions, viewport rhythm, responsive behavior>
    typography: <scale, weight, family, alignment, rhythm>
    color_material: <background, surfaces, contrast, accent, semantic status>
    component_density: <card/table/form/nav density and spacing>
    content_data: <realistic domain objects, state, long-data behavior>
    motion_or_asset: <none or deliberate asset/motion choice>

visual_target:
  source: <selected reference | generated mock | scratch prototype | local screenshot | internal best-of-3 direction>
  page_role: <landing | dashboard | workbench | admin | form | etc.>
  design_thesis: <one sentence tying layout, color, type, content, and workflow>
  visual_protagonist: <object/workflow/surface that owns the first impression>
  composition_skeleton:
    viewport_structure: <major regions and first-viewport balance>
    density_model: <sparse | balanced | scan-dense | command-dense>
    hierarchy_model: <what users notice first, second, and third>
    responsive_strategy: <desktop/mobile transformation>
  business_translation: <how project-specific objects replace reference objects>
  failure_tests:
    - <generic-template failure>
    - <weak-protagonist failure>
    - <business-mismatch failure>
    - <responsive or state-pressure failure>
  validation:
    required_viewports: <desktop + mobile unless explicitly not applicable>
    comparison_method: <same-context screenshot comparison | screenshot QA against target>
    pass_condition: <rendered UI realizes the aesthetic mechanism and target>
```

Do not let `visual_target` become a second design brief. It should be short
enough to guide implementation, but concrete enough that screenshot QA can
falsify it. If an aesthetic generation packet and target cannot be formed from
inspected references, local evidence, or a scratch prototype, the correct result
is `blocked`, not a generic page from adjectives.

## Reference Source Pool

Use current public web results, local screenshots, or saved context when
available. Do not treat this list as exhaustive; it is a breadth starter.

- **Template marketplaces**: Envato Market / ThemeForest, Envato Elements,
  UI8, Creative Market, Webflow Templates, Framer Marketplace, Tailwind UI,
  Flowbite Blocks, shadcn/ui blocks, Untitled UI, Tremor, BootstrapMade, WrapBootstrap.
- **Inspiration galleries**: Land-book, Lapa Ninja, Landingfolio, One Page Love,
  SaaS Landing Page, SaaSFrame, Godly, Awwwards, SiteInspire, Httpster,
  Dribbble, Behance.
- **Product and app-flow libraries**: Mobbin, Page Flows, real product sites,
  public changelog/onboarding/docs screens, official screenshots, app stores.
- **Design systems and component grammar**: Apple HIG, Material, Fluent, Carbon,
  Polaris, Primer, Atlassian Design System, GOV.UK Frontend, USWDS.
- **Prompt and effect galleries**: awesome-web-prompts, React Bits, Motion
  examples, curated prompt/code effect galleries with rendered screenshots,
  previews, or implementation notes.

Reference classes serve different jobs:

- marketplaces provide complete page packs and dashboard density,
- inspiration galleries provide first-impression composition and art direction,
- real products and app-flow libraries provide workflow truth,
- design systems provide component grammar and platform honesty,
- component/block libraries provide implementation-level interaction patterns,
- prompt/effect galleries provide high-visual hero, effect, component, and
  motion archetypes; they are not product IA or workflow truth.

## Reference Research Mode

Reference discovery is a separate research surface, not something to improvise
inside implementation. When runtime tools and current policy permit delegation,
use read-only subagents for broad or high-stakes reference research:

- use one subagent for a narrow reference class or page-role family;
- use 2-3 parallel subagents when dashboard/app, landing/brand, and component/UI
  kit references are independent;
- ask subagents for category, fit, borrowable structure, risks, and A/B/C
  rating, not for final design decisions;
- the main thread chooses the final reference packet and implementation thesis.

If subagents are unavailable, do the same source-class scan in the main thread
and record the reason under `reference_sourcing.unavailable_reason`.

## Reference Rating

Rate references before using them:

- **A**: can be the primary skeleton/reference for the matching page role.
- **B**: useful secondary reference for density, component grammar, or a
  vertical pattern; pair it with a stronger source.
- **C**: do not use as primary reference; borrow only a small local pattern or
  treat it as an anti-pattern.

These A/B/C values rate source suitability, not the quality of the output.
Output quality uses AQ1/AQ2/AQ3 from `frontend-design-contract.md`. An AQ3 target
normally requires an inspectable A-rated primary reference or an equally
explicit visual target, followed by same-context rendered comparison. Selecting
an A-rated source does not prove that the implementation achieved AQ3.

Do not stack references by quantity. Select one primary A-rated reference when
available, plus at most one secondary reference for workflow truth, component
grammar, or visual language.

## Source-Pool Audit

Use `source_pool_mode: shortlist` for ordinary Tier 2/3 work when the product
class is obvious and 2-3 inspected references are enough to choose a visual
target.

Use `source_pool_mode: batch_audit` when any of these are true:

- the user asks for "最美", "最优", "源站级", "极致", "不要二次返工", "都试试",
  or complains that prompt-only/theme-only output is ugly;
- many plausible source classes exist and choosing too early would materially
  affect the result;
- the task asks for a full page set, dashboard/workbench, product redesign, or
  source-site replication;
- marketplace sources such as Envato, ThemeForest, or CodeCanyon may be useful
  but their access, preview depth, or business fit is uncertain.

`batch_audit` is evidence, not browsing theater. Build a compact matrix before
implementation:

```yaml
reference_batch_matrix:
  product_domain: <what is being designed>
  page_roles: <landing/login/dashboard/status/etc.>
  candidates_tested:
    - source: <url or local screenshot>
      class: <real_product | template_marketplace | template_demo | inspiration_gallery | design_system | component_block | app_flow | prompt_effect_gallery | local_reference>
      access: <public | gated | verification_blocked | not_found | paywalled_preview | thin_or_script_blocked>
      role_fit: <page roles this source can actually support>
      replication_difficulty: <1 easy .. 5 blocked/hard>
      expected_replica_effect: <1 weak .. 5 excellent>
      completeness: <1 fragment .. 5 full flow/page set>
      aesthetic_mechanism_fit: <A primary | B secondary | C unusable>
      rating: <A | B | C>
      evidence: <screenshot path, URL, or blocker>
  selected_primary: <one source and why>
  selected_secondary: <none or one source for workflow/component/visual layer>
  rejected_primary_sources: <key rejected sources and why>
```

Access is part of quality. A beautiful source blocked by verification, auth,
404, dead live preview, or subscription-only assets cannot be an A-rated primary
unless the user provides rights/access and the page role can be inspected. A
marketplace item page with only thumbnails is usually B at most, even when the
preview image is attractive.

For strict single-site replication, do not repair a missing landing, login, or
workbench role with another website. Score the single source lower and explain
the missing role. For controlled multi-source design, assign each source a
layer: primary product/visual grammar, workflow truth, component grammar, or
secondary mood. Do not average many sources into one generic design.

## Envato / ThemeForest Routing

Envato is useful only when routed by product/page type. It is not a generic
"make it beautiful" source.

| Product/page type | Envato reference types | Rating | Borrow | Guardrail |
| --- | --- | --- | --- | --- |
| SaaS ops, growth, metrics | SaaS admin, analytics dashboard, revenue dashboard | A | KPI hierarchy, trend panels, ops density | Add real workflow; avoid generic KPI cards |
| BI, reporting, finance analytics | reporting dashboard, BI admin, portfolio dashboard | A | chart matrix, filters, comparison tables | Do not turn non-analytics products into chart walls |
| SOC/SIEM/cybersecurity | Threatrix-style SOC, SIEM, threat monitoring, incident/security logs | A | security overview, threat queues, attack map, incidents, endpoint/logs, roles | Strong for security pages; server CPU/disk/network still need SRE monitoring semantics |
| Server/API/site monitoring | Server360-style server/API/website monitoring | B | monitor IA, host/API/website grouping, uptime/status modules | Useful semantics but often older visual/stack; pair with modern admin/product references |
| SRE/DevOps/NOC/Kubernetes | DevOps, NOC, K8s, CI/CD, network monitoring | C in Envato unless exact high-quality match | rough module ideas only | Envato coverage is weak; prefer real products/design systems and custom workbench design |
| High-signal enterprise admin base | Metronic, Vuexy, DashLite, Velzon, Skote, Fuse, UBold-style admin kits | A as system base, B as visual reference | shell, navigation, tables, charts, settings, auth, component density | Not domain semantics; do not let generic admin replace product-specific workflow |
| CRM, sales, pipeline | CRM dashboard, deal pipeline, invoice/proposal admin | A when domain matches | pipeline, customer detail, timeline, status chips | Organize by sales action, not raw table data |
| eCommerce/vendor/order ops | eCommerce admin, shop management, multivendor dashboard | A when domain matches | order flow, inventory, refund/shipping states | Lower marketing color noise for B2B tools |
| Project/task/work management | project management dashboard, task board, workload admin | A when domain matches | kanban, workload, milestones, blockers | Add dependencies/blocking/batch actions; templates often omit them |
| Multipurpose admin systems | Metronic, Vuexy, DashLite, Skote, Fuse, Velzon, Able Pro, UBold-style admin kits | B | layout shell, component coverage, table/form/modal patterns | Do not use as aesthetic primary; high template-risk |
| HR, education, healthcare, finance, IoT verticals | HRMS, LMS, hospital, investment, IoT dashboards | B unless exact domain | role dashboards, approvals, schedules, domain states | Cross-domain reuse can look false; pair with real product/design-system evidence |
| SaaS/software/AI landing | SaaS landing, software landing, AI landing | A for structure, B for final visual | hero/product mockup, feature/use-case/pricing/proof flow | Pair with real product or inspiration gallery; avoid fake dashboard and AI glow sameness |
| Single product / ecommerce transaction | product landing, Shopify/fashion ecommerce, marketplace pages | A when commerce/product display is real | packshot/gallery, PLP/PDP, cart/checkout, sticky buy flow | Requires real product assets; do not reuse lifestyle imagery or platform-specific assumptions blindly |
| Creative/agency/portfolio | creative agency, GSAP portfolio, architecture/interior, personal portfolio | A only for creative/visual brands, B/C otherwise | large type, case grid, showreel, image-led rhythm, transitions | High performance/mobile/accessibility risk; use Awwwards/Land-book to extract an aesthetic mechanism, not to copy |
| Corporate/consulting/SEO/marketing landing | business, consulting, SEO agency, marketing agency | B | section order, service blocks, credibility modules, contact flow | High generic-template risk; not a primary reference for premium/custom brands |
| Event/campaign/coming soon | event, countdown, waitlist templates | C except for short campaign pages | countdown, registration, agenda/speaker blocks | Short-lived flow; weak for durable product/brand IA |
| Multipurpose / mega-demo / stock-heavy templates | multipurpose, 50+ demos, old Bootstrap, gradient hero/card layouts | C | component inventory or anti-pattern only | Never use as primary visual target |

Marketplace access rules:

- Envato Elements item pages are secondary unless their public preview exposes
  enough page-role structure to implement from evidence.
- ThemeForest or CodeCanyon pages blocked by Cloudflare, CAPTCHA, login, or
  missing live preview are C as primary sources for that run.
- CodeCanyon/PHP app items may provide useful business semantics, but older
  visual language or broken live previews prevent them from being primary
  high-aesthetic sources.
- A marketplace template can be A only when product type, page role, visual
  quality, and public inspectability all match.

## Prompt / Effect Gallery Routing

Use prompt/effect galleries only as visual and interaction evidence, not as a
project blueprint. They are useful when a Tier 2/3 landing page, portfolio,
brand page, product hero, or high-aesthetic prototype needs stronger first-view
composition, component energy, or motion vocabulary than a written prompt can
provide.

Source roles:

- `awesome-web-prompts`-style galleries can supply hero, landing, portfolio, and
  page-section archetypes when the result includes inspectable screenshots,
  previews, or source context.
- React Bits-style component galleries can supply animated component and effect
  archetypes for project-local application use, after checking dependencies and
  license boundaries.
- Motion example galleries can supply React/Vue/JS layout, exit, gesture,
  scroll, and transition patterns when those patterns fit the existing stack.

Rating rules:

- **A**: use as primary visual/effect skeleton only when the page role matches,
  rendered evidence is inspectable, and the effect supports the design thesis.
- **B**: use as secondary grammar for one component, motion pattern, or hero
  move alongside a workflow-truth or design-system reference.
- **C**: do not use when the example is only flashy, uninspectable, unrelated to
  the product job, license-unclear, stack-incompatible, or competing with the
  product's real workflow.

Guardrails:

- Do not rely on prompt/effect galleries as the sole reference for dashboard,
  admin, audit, finance, monitoring, CRM, developer console, or other
  workflow-heavy products. Pair them with real product, app-flow, or
  design-system evidence.
- Do not copy third-party prompts, source code, assets, or distinctive layouts
  into Codex skills. Extract only the reusable archetype, then translate it into
  the current project's tokens and stack.
- Treat React Bits and similar component collections as project-local app
  references or dependencies, not as material to redistribute inside a Codex
  skill or component library.
- Convert the chosen idea into `effect_archetype` and `motion_contract`
  decisions. Do not stack many effects because many examples look good.

## Selection Rules

- Do not wait for user-provided references unless the user explicitly wants to
  choose them. For Tier 2/3 or high-aesthetic UI work, automatically find or
  select reference sites before implementation.
- For Tier 2/3 or high-aesthetic work, inspect 2-3 candidate references when
  network or local sources allow. Cover at least two source classes unless the
  user supplied a single mandatory source or the task is tightly scoped to an
  existing design system.
- Escalate from 2-3 candidates to `batch_audit` when the result depends on
  finding the best source, marketplace access is uncertain, or the page role has
  high generic-template risk.
- For dashboards, workbenches, admin tools, monitoring, CRM, audit, finance, or
  developer consoles, include at least one workflow-truth reference from a real
  product, app-flow library, official product screenshot, or design system. Do
  not rely only on marketplace templates.
- For landing pages, brand pages, portfolios, and product pages, include at
  least one first-impression reference from an inspiration gallery, source
  product page, or high-quality template preview.
- Do not build from a written brief alone for Tier 2/3 or high-aesthetic work.
  Establish an aesthetic generation packet and visual target first:
  source/prototype reference, generated mock, screenshot, Figma frame, or
  internally selected best direction from 2-3 candidates translated into the
  current product.
- Default to Codex selecting the best direction. Stop for the user only when
  candidate directions imply different product strategies, brand commitments,
  legal/commercial constraints, or irreversible scope choices.
- Use one primary prototype reference per page role. Two references are allowed
  only when they solve different layers, such as source grammar plus a dashboard
  density prototype.
- For Envato/ThemeForest references, record the reference category and A/B/C
  rating. Use A as primary only when the product/page role matches; use B only
  as secondary; do not use C as a primary reference.
- Prefer references that already solve the same page role. A beautiful landing
  page is weak evidence for a dense workbench; a dense workbench is weak
  evidence for a premium product hero.
- Prefer official product pages, design-system pages, high-quality product UI
  references, real rendered screenshots, local high-quality prototypes, or
  source product pages over written descriptions.
- If a local reference exists, inspect its screenshot or rendered page before
  extracting rules. Do not use the filename as evidence.
- If no local reference fits and network is available, search/browse for 2-3
  candidate reference sites that match the page role and theme. Inspect the best
  candidate before extraction.
- If no adequate reference exists, create a quick scratch prototype for
  composition only, inspect it, then implement the final UI. The scratch
  prototype is a thinking artifact, not a deliverable, unless the user asks.
- Do not average many references. Reference mixing often creates generic UI.
- Borrow structure, density, hierarchy, interaction affordances, and visual
  protagonist strategy. Do not copy protected artwork, brand marks, exact text,
  paid template source, or distinctive proprietary layout details wholesale.
- If the user asks to faithfully clone a paid template or protected source,
  require provided rights/assets or produce an original, source-inspired version
  that preserves the useful grammar without copying protected material.

## Required Workflow

For Tier 2/3 theme work, high-aesthetic requests, prompt/theme optimization, or
page roles with high generic-template risk:

1. Select the theme with `frontend-theme-contract.md`.
2. Automatically gather a shortlist or `batch_audit` candidate pool for each
   important page role across at least two source classes unless a strong
   local/source reference is already present.
3. Select the best page-role reference and inspect its rendered screenshot/page.
4. Record `reference_sourcing`, disqualified sources, and why the primary source
   won; then extract skeleton/hierarchy into
   `prototype_reference_packet`.
5. Convert the packet into a compact `aesthetic_generation_packet` plus
   `visual_target`: the aesthetic packet names the beauty mechanism and code
   translation; the target turns that into design thesis, visual protagonist,
   composition skeleton, business translation, failure tests, and screenshot
   validation.
6. Implement from the packet, aesthetic generation, and `visual_target`, not from
   theme adjectives or marketplace labels.
7. Render final pages and compare page by page against the source/prototype,
   aesthetic mechanism, and visual target.
   When a source visual exists, compare source and implementation in the same
   visual context before claiming fidelity.
8. If the final UI is materially weaker or generic, revise the aesthetic
   generation packet first; only patch implementation details when the packet was
   already correct.

## Review Questions

When reviewing UI produced with this contract, ask:

- Was a real source or prototype inspected before implementation?
- Did reference sourcing cover enough source classes for the page role?
- Did reference extraction produce a concrete aesthetic mechanism, or only name
  a source/theme?
- Does the final page share the reference's skeleton quality, not just colors?
- Is the visual protagonist as strong as the reference's protagonist?
- Did business objects replace reference objects coherently?
- Are page-role references appropriate, or was a landing reference misused for a workbench?
- Did the output avoid copying brand assets, exact copy, and protected visuals?
- Is the comparison based on rendered screenshots rather than stated intent?
