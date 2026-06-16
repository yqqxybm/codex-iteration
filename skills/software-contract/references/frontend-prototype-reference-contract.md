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
3. **Rendered final UI**: the actual product page, inspected against the
   reference instead of judged from intention.

The prototype is not copied. It is a control sample for composition quality.
Extract structure, proportion, density, and interaction logic; translate the
business object into that structure.

## Prototype Reference Packet

Build this packet internally before implementing Tier 2/3 work when this
contract applies:

```yaml
prototype_reference_packet:
  page_role: <landing | login | dashboard | workbench | form | mobile task | etc.>
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
  business_translation: <how user domain objects map into the skeleton>
  do_not_copy: <brand marks, exact assets, literal copy, protected visuals>
  comparison_result: <matches | weaker and revised | blocked>
```

## Selection Rules

- Do not wait for user-provided references unless the user explicitly wants to
  choose them. For Tier 2/3 or high-aesthetic UI work, automatically find or
  select reference sites before implementation.
- Do not build from a written brief alone for Tier 2/3 or high-aesthetic work.
  Establish a visual target first: source/prototype reference, generated mock,
  screenshot, Figma frame, or internally selected best direction from 2-3
  candidates.
- Default to Codex selecting the best direction. Stop for the user only when
  candidate directions imply different product strategies, brand commitments,
  legal/commercial constraints, or irreversible scope choices.
- Use one primary prototype reference per page role. Two references are allowed
  only when they solve different layers, such as source grammar plus a dashboard
  density prototype.
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

## Required Workflow

For Tier 2/3 theme work, high-aesthetic requests, prompt/theme optimization, or
prior ugly output:

1. Select the theme with `frontend-theme-contract.md`.
2. Automatically gather 2-3 candidate prototype/source references for each
   important page role unless a strong local/source reference is already present.
3. Select the best page-role reference and inspect its rendered screenshot/page.
4. Extract skeleton and hierarchy into `prototype_reference_packet`.
5. Implement from the packet, not from theme adjectives.
6. Render final pages and compare page by page against the source/prototype.
   When a source visual exists, compare source and implementation in the same
   visual context before claiming fidelity.
7. If the final UI is materially weaker, revise the prompt/control packet first;
   only patch implementation details when the packet was already correct.

## Review Questions

When reviewing UI produced with this contract, ask:

- Was a real source or prototype inspected before implementation?
- Does the final page share the reference's skeleton quality, not just colors?
- Is the visual protagonist as strong as the reference's protagonist?
- Did business objects replace reference objects coherently?
- Are page-role references appropriate, or was a landing reference misused for a workbench?
- Did the output avoid copying brand assets, exact copy, and protected visuals?
- Is the comparison based on rendered screenshots rather than stated intent?
