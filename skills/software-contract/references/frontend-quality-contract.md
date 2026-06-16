# Frontend Quality Contract

Use this reference from `project-frontend`, `project-iteration`, `review`, or
`project-bootstrap` when UI work needs product-state robustness or UI evidence.

## UI Contract

Frontend quality is not a single ideal-data screenshot. It is a contract that
the core workflow remains usable under realistic data, state, permission,
interaction, and environment pressure.

Every UI task has two quality axes:

- visual quality: art direction, hierarchy, typography, color, spacing, assets, motion;
- product-state robustness: the core workflow under realistic operating conditions.

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

## State And Pressure QA

For variable data or async UI surfaces, happy-path screenshots alone are not
enough. Verify relevant operating conditions:

- content pressure: empty, normal, long text, long list, dense records, abnormal names or values;
- system state: loading, success, empty, error, stale data, retry;
- authority and interaction: enabled, disabled, readonly/forbidden, hover, focus, pending, failed action;
- environment: desktop, mobile, theme, Chinese/English or likely long localized text;
- neighboring surfaces: pages/components using the same list, table, log, alert, card, filter, or action pattern.

If a relevant condition cannot be rendered locally, list it in
`frontend_evidence_packet.not_verified` with the exact reason. Do not mark the UI
complete as if it was covered.
