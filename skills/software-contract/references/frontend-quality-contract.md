# Frontend Quality Contract

Use this reference from `project-frontend`, `project-iteration`, `review`, or
`project-bootstrap` when UI work needs product-state robustness or UI evidence.

## UI Contract

Frontend quality is not a single ideal-data screenshot. It is a contract that
the core workflow remains usable under realistic data, state, permission,
interaction, and environment pressure.

Every UI task has one frontend design objective plus hard operating constraints:

- **core objective**: achieve the selected aesthetic target through art
  direction, composition, hierarchy, typography, color, spacing, assets,
  component craft, and motion;
- **hard constraint**: keep the core workflow robust under realistic data,
  system state, authority, interaction, and environment pressure.

Robustness cannot replace the aesthetic objective, and aesthetics cannot hide a
broken workflow. The design must satisfy both without treating "works under
pressure" as proof that it is visually complete.

Keep verification scopes separate:

- `browser_smoke`: narrow runtime proof that the route/page loads, has no fatal
  console/runtime error, the assigned core interaction does not crash, and the
  checked viewport has no blocking overlap or horizontal overflow.
- `state_pressure_qa`: representative loading, empty, error, long-content,
  permission, theme, language, mobile, or neighboring-surface checks.
- `content_copy_qa`: copy/content quality, domain realism, action labels, empty
  and error message usefulness, and terminology consistency.
- `visual_qa`: hierarchy, layout, typography, color, assets, motion, responsive
  polish, and design-system fit.

Do not report `state_pressure_qa`, `content_copy_qa`, or `visual_qa` as part of
`browser_smoke`. `visual_qa` is mandatory for every visible design mutation,
with depth set by AQ1/AQ2/AQ3 in `frontend-design-contract.md`; it may be
`not_applicable` only for a genuinely non-visual UI change with evidence.
Select `state_pressure_qa` and `content_copy_qa` when the user asks, the UI
Contract requires them, or the changed surface makes them material.

Build an internal `ui_contract` before implementation. Keep it concise for Tier
0, make it explicit for Tier 1+, and treat data-heavy pages, logs, dashboards,
admin tools, tables, alerts, audits, access screens, and agent/task consoles as
state-sensitive by default.

```yaml
ui_contract:
  core_workflow: <what the user must be able to complete>
  operating_conditions:
    content_pressure: <empty | normal | long_content | high_density | abnormal_content>
    system_state: <loading | empty | success | error | stale | retry>
    authority: <actionable | readonly | forbidden | disabled>
    interaction: <default | hover | focus | pending | failure>
    environment: <viewport | theme | language | input_method>
    neighboring_surfaces: <same pattern across pages/components, if relevant>
  evidence:
    browser_smoke: <used | not_applicable | skipped_with_reason>
    state_pressure_qa: <used | not_applicable | skipped_with_reason>
    content_copy_qa: <used | not_applicable | skipped_with_reason>
    visual_qa: <used | not_applicable | skipped_with_reason>
    verified: <screenshots, browser checks, tests, or commands>
    not_verified:
      - condition: <condition>
        reason: <not applicable | impossible locally | out of scope>
    residual_risk: <remaining risk or none>
```

Strict verification does not require every Cartesian product of conditions when
combinations are irrelevant. It requires a reasoned representative set that
protects the core workflow. Return key evidence as `frontend_evidence_packet` in
the handoff or final response.

When multiple frontend controls are active, wrap their compact evidence in one
`frontend_control_evidence` envelope instead of scattering unrelated blocks:

```yaml
frontend_control_evidence:
  tier: <0 | 1 | 2 | 3>
  aesthetic_target: <AQ1 | AQ2 | AQ3, inherited floor, and benchmark>
  aesthetic_result: <latest screenshot visually inspected, holistic verdict, local delta or calibrated scores, and comparison evidence>
  active_controls: <aesthetic_integrity | local_style | quality | design | taste | theme | prototype | aesthetic_generation | visual_target | motion>
  local_style: <none | local_style_evidence>
  quality: <none | frontend_evidence_packet summary>
  design: <none | design_contract_evidence>
  taste: <none | taste_contract_evidence>
  theme: <none | theme_evidence>
  prototype: <none | prototype_reference_packet summary, including reference_sourcing>
  aesthetic_generation: <none | aesthetic_generation_packet summary>
  visual_target: <none | visual_target summary and screenshot comparison status>
  motion: <none | motion_contract summary>
  not_active: <controls intentionally not used and why; never aesthetic_integrity>
```

The envelope is a reporting shape, not a new checklist. Each nested value comes
from its owning contract and should stay compact.

## State And Pressure QA

For variable data or async UI surfaces, happy-path screenshots alone are not
enough. Verify relevant operating conditions:

- content pressure: empty, normal, long text, long list, dense records, abnormal names or values;
- system state: loading, success, empty, error, stale data, retry;
- authority and interaction: enabled, disabled, readonly/forbidden, hover, focus, pending, failed action;
- environment: desktop, mobile, theme, Chinese/English or likely long localized text;
- neighboring surfaces: pages/components using the same list, table, log, alert, card, filter, or action pattern.

`content_pressure` means layout/data pressure such as long text, long lists,
dense records, or abnormal values. It is not a mandate to perform copywriting
review unless `content_copy_qa` is selected.

If a relevant condition cannot be rendered locally, list it in
`frontend_evidence_packet.not_verified` with the exact reason. Do not mark the UI
complete as if it was covered.
