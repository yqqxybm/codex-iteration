# Frontend Motion Contract

Use this reference from `project-frontend`, `project-bootstrap`,
`project-iteration`, `review`, or `optimize` when UI work includes any front-end
motion effect, including micro-interactions, advanced motion, GSAP, scroll
narrative, animation choreography, or motion QA.

## Philosophy

Motion is a product control surface, not decoration. It should explain hierarchy,
causality, spatial continuity, progress, or narrative. The correct question is
not "can this animate?" but "what does the motion make easier to understand or
feel?"

Keep `project-frontend` responsible for art direction and UI evidence. Keep
library-specific motion rules here so the system can use GSAP consistently
without bloating every frontend task.

## Motion Contract Schema

```yaml
motion_contract:
  interaction_thesis: <one sentence explaining why motion belongs here>
  motion_role: <feedback | hierarchy | narrative | delight | spatial_continuity>
  library_choice: <gsap | gsap+threejs>
  why_this_library: <why GSAP is applied, or why the task is blocked>
  choreography:
    - trigger: <load | hover | click | scroll | route | data-change>
      target: <element, state, or workflow surface>
      behavior: <transition | timeline | stagger | scrub | pin | flip | path | etc>
      exit_or_cleanup: <how it ends, reverses, or cleans up>
  accessibility:
    reduced_motion: <disable | simplify | preserve essential feedback>
  performance:
    properties: <transform/opacity/autoAlpha preferred, layout props avoided>
    cleanup: <unmount, route change, ScrollTrigger kill/refresh, timers/listeners>
  verification:
    desktop: <checked | not_applicable | missing>
    mobile: <checked | not_applicable | missing>
    reduced_motion: <checked | not_applicable | missing>
    resize_or_long_content: <checked | not_applicable | missing>
    route_or_unmount_cleanup: <checked | not_applicable | missing>
```

## GSAP-Required Policy

The user's current default is GSAP-first and GSAP-required for front-end motion.
If a UI implementation includes motion, use GSAP as the motion engine.

- CSS remains valid for static layout, colors, focus visibility, reduced-motion
  static states, and no-motion fallback styles. Do not use CSS
  `transition`/`animation` as the primary motion implementation.
- WAAPI and Framer Motion are not default substitutes. Use them only when the
  user explicitly asks, the existing project mandates them, or GSAP cannot be
  used and the task is reported as blocked or user-approved.
- Three.js / canvas can own real 3D/canvas rendering. GSAP still owns UI motion
  choreography around it when motion is present. Do not substitute flat GSAP
  effects for a requested 3D scene.
- If GSAP cannot be installed, imported, or verified in the current project,
  stop and report the blocker. Do not silently downgrade to CSS, WAAPI, Framer
  Motion, or no animation.

## GSAP Contract

For all UI motion:

- Install only what is needed: usually `gsap`; add `@gsap/react` for React.
- Register plugins once at module/app boundary where practical.
- Prefer timelines for sequencing; do not chain many delays to fake a timeline.
- Prefer `transform`, `opacity`, and `autoAlpha`; avoid animating layout props
  such as `top`, `left`, `width`, or `height` when transform can express the
  same motion.
- Keep selectors scoped. In component frameworks, do not animate global selector
  text that can affect sibling instances.
- Do not leave `markers: true`, debug overlays, or development-only controls in
  production UI.

For React:

- Prefer `useGSAP()` from `@gsap/react` with a scoped container ref.
- Use `contextSafe()` for animations created in click handlers, delayed
  callbacks, timers, or other code that runs after the hook body.
- In SSR/app-router environments, GSAP code belongs in client-side components.
- On updates where dependencies change the animation, use the appropriate
  dependency config and cleanup behavior rather than stacking duplicate tweens.

For ScrollTrigger:

- Use it when scroll is part of the product story or comprehension, including
  reveal-on-scroll when the requested aesthetic benefits from GSAP-level
  orchestration. Do not use it for scroll effects that make the core workflow
  harder to operate.
- Check `pin`, `scrub`, and `snap` behavior on mobile, resized desktop, and long
  content. Scroll-triggered layouts are fragile under content changes.
- Refresh after layout-changing async content, image/font loading, or dimension
  changes when those affect trigger positions.
- Use responsive branching for touch/mobile when a desktop scroll narrative
  would become cramped or disorienting.

## Accessibility And Reduced Motion

Every motion implementation must include a reduced-motion strategy:

- disable decorative motion;
- simplify narrative motion into static or short state changes;
- preserve essential feedback such as focus, pending, success, or error states.

Motion must not hide required content, block keyboard operation, rely on color
alone, or make the only path to information depend on scroll timing.

## Verification

Advanced motion is incomplete until verified in the rendered UI. At minimum,
record evidence for:

- desktop viewport,
- mobile/narrow viewport,
- reduced-motion behavior,
- resize or long-content behavior for scroll-triggered scenes,
- unmount/route cleanup for component frameworks,
- absence of visible jank, debug markers, duplicate animations, or broken focus.

If any relevant check cannot run locally, list it in
`frontend_evidence_packet.not_verified` with a concrete residual risk.

## Official Source Alignment

GSAP's official docs and AI skills split the domain into core API, timelines,
ScrollTrigger, plugins, React/framework lifecycle, and performance. Preserve that
separation when debugging or expanding a GSAP implementation. If exact API,
plugin behavior, licensing, or version-specific behavior matters, check the
current official GSAP docs or installed package before coding from memory.
