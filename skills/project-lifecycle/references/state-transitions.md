# Discovery, Root, And Version State Transitions

Read this reference only for a discovery-to-adoption, root-state, or
version-state request identified by `project-lifecycle`. The controller owns
these transitions; downstream skills act only on accepted state.

## Discovery-To-Adoption Changes

Use `project-discovery` when user, market, competitor, product, or domain
research must determine product content, target users, requirements,
priorities, positioning, or scope. A bounded fact lookup or feasibility check
for an already accepted decision stays with `project-analysis`.

Discovery produces a provisional handoff whose authority status is
`evidence_only`; that label does not reduce it to source collection or replace
its independent judgment. It does not change project authority by itself:

```yaml
discovery_gate:
  status: <required | ready_for_adoption | adopted | rejected | model_reset |
    blocked | insufficient | not_applicable>
  discovery_handoff: <project-discovery result or resolvable reference>
  adoption:
    decision: <adopt | adopt_partial | reject | ask | pending>
    accepted_conclusions: <exact findings promoted into project direction, or none>
    rejected_or_unresolved: <findings not promoted and why>
    rationale: <actor/situation -> task or judgment -> need -> outcome relation>
    boundary_and_reversal: <where the decision applies and what would reopen it>
    dependent_state: <charter, requirements, agenda, docs, tests, or implementation decisions created from it>
```

Only `project-lifecycle` records adoption. For a material product or technical
commitment, route the handoff through `project-analysis`; its result is an
adoption recommendation, not self-authorizing project state. Current product
shape, implementation feasibility, available data, category labels, detailed
field names, or a fixed item count cannot replace the explanatory relation in
`rationale`.

For "research, then implement" or an equivalent goal-backed request, the
initial agenda contains exactly the discovery work and its controller-owned
adoption gate. Rebuild the downstream brief, requirements, plan, and executor
nodes after adoption; do not prefill them from hypotheses merely because later
implementation is authorized.

A corrected source, fact, or bounded finding may receive local revision. A
correction to the research object, actors, task, judgment standard,
explanatory relation, or method is `model_feedback`: set `status: model_reset`,
identify the model's causal descendants, and remove their authority before
rebuilding. This applies to dependent adopted decisions, charter fields,
requirements, agenda items, docs, tests, fixtures, and implementation decisions,
not to unrelated project state. Actual artifact repair remains subject to the
user's mutation boundary and the owning downstream skill.

## Root-State Changes

Root-state requests include new project creation, project initialization,
scaffolding from a product idea, PRD, requirements, MVP boundary, root
architecture/design, tech-stack decisions, and defining or changing what a
version boundary such as `v0.x` means.

Before `project-bootstrap`, `project-docs`, or `project-iteration` receives
root-state work, produce or consume:

```yaml
frozen_charter:
  intent: <user-visible product goal>
  target_user: <primary user/operator>
  core_workflow: <main scenario>
  requirement_boundary: <in-scope product content/capability and its acceptance boundary>
  non_goals: <explicit exclusions>
  success_criterion: <observable completion criterion>
  constraints: <hard limits>
  project_shape: <application, repository, or deliverable shape>
  doc_profile: <standard docs profile or not_applicable>
  docs_ia: <authorized root docs and docs/ subdirectories when standalone docs are involved>
```

Start at the earliest unresolved commitment: use `project-discovery` when
actors, situations, tasks, needed information or capability, or their value
relation would decide the product; use adopted discovery conclusions plus
`project-brief` when that reality is accepted but root product direction is not;
use `project-analysis` for root decisions or architecture tradeoffs after the
product commitment exists.
Unadopted discovery material cannot fill a charter field. Ask and wait only when
the user's perspective is non-substitutable and materially affects the
understanding or commitment;
otherwise resolve, verify, assume, or carry uncertainty as risk. An executor
cannot infer root direction from one broad sentence and write durable project
files.

## Version-State Changes

Version-state requests implement, advance, or close an already accepted version
boundary: "做一个版本", "实现一个版本", milestone, sprint, phase completion,
and equivalent language. A token such as MVP or `v0.x` does not decide the
classification by itself; defining its boundary is root-state work, while
executing the accepted boundary is version-state work.

Version work enters the lifecycle agenda loop. If no controlling plan exists,
create the version agenda from the frozen charter and current request; do not
reduce it to one local iteration. Each item records source, status, result, and
verification.

While a version agenda is active, only a user-confirmed change to an already
accepted goal, scope, or priority becomes:

```yaml
change_request:
  source: <user message or evidence>
  requested_change: <what changed>
  impact: <agenda item, root direction, docs/assets, tests, release, or none>
  decision: <add_now | replace_item | defer | reject | ask>
  reason: <why this preserves the user goal and current version boundary>
```

Only `add_now` or `replace_item` changes the active agenda. Make `defer`,
`reject`, or `ask` visible in the trace or final response.
A correction that exposes an earlier misunderstanding or invalid judgment
follows State Boundary Enforcement instead of this transition.
