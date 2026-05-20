---
name: optimize
description: >
  General optimization orchestrator. Use when the user asks to optimize, deeply optimize, improve, polish, refine,
  strengthen, or "优化/深度优化/改进/提升" an artifact, prompt, plan, workflow, decision, configuration, skill, or
  thinking process, including explicit "深度审查优化" review-then-optimize loops. Deep mode requires auditable framework pass logs and stops only after two consecutive full
  framework-exhaustion cycles find no material optimization point; use project adapters for software-project artifacts.
---

# Optimize

Optimize defines what "better" means, chooses the smallest existing framework
chain that can achieve it, and returns a concrete delta or bounded plan. It is
not a new thinking core; it routes and composes existing cores.

## Philosophy

1. **Objective before effort**: define target, success standard, constraints,
   non-goals, and stop line before improving anything.
2. **Constrained alignment**: optimize fit to the user's target under real
   constraints; more depth, length, abstraction, or compatibility is not
   automatically better.
3. **Principles must change behavior**: every philosophy claim must affect a
   boundary, decision, verification step, or output.
4. **Correct framework first**: use the smallest matching existing framework;
   do not invent a parallel method.
5. **No silent downgrade**: if the exact target cannot be met, state the
   blocker instead of substituting a weaker result.
6. **Concrete delta**: report what changed, why it is better, how it was
   checked, and what risk remains.
7. **Reflective equilibrium**: optimality is reflective equilibrium under
   current evidence and constraints: intent is faithfully served, rules
   reliably produce correct behavior, and complexity remains justified by value.
   Optimization seeks convergence, not novelty.

## Optimality Standard

Treat a proposal as material only when it exposes unresolved tension in the
current artifact or restores equilibrium with less structure. Check four axes:
correctness, elegance, robustness, and stability.

A new proposal may change an artifact only when it dominates the current one:

- same or better fit to the user's target,
- same or better protection against realistic failure modes,
- same or lower cognitive and procedural complexity, or a justified complexity
  increase for a verified risk,
- same or better resistance to future re-optimization drift.

If a proposal is merely a new angle, wording preference, theoretical edge case,
or added coverage without behavior-changing value, reject it as
`non-material drift`. Do not reset clean cycles for rejected drift.

## Control-Law Evolution

Treat skills, prompts, configs, and workflows as finite control laws in
cybernetic pragmatism: intent is the objective, evidence is feedback, boundary
is the action constraint, and verified state change is completion.

Optimization may change a control law only when evidence shows the current law:

- miscontrols the user's intent,
- lacks feedback or verification,
- violates or blurs an action boundary,
- cannot stop reliably,
- or can be simplified while preserving equal or better behavior.

A philosophy change counts only when it changes sensed evidence, allowed action,
verification, or stop condition. Otherwise reject it as `non-material drift`.

## Contract

Resolve internally before optimizing:

- **Target**: exact object to improve.
- **Objective**: what "better" means here.
- **Constraints**: scope, style, length, safety, tools, preferences, no-go areas.
- **Evidence**: artifact, examples, symptoms, feedback, or verification output.
- **Framework chain**: skills to use and their order.
- **Stop line**: what must not change.

Ask only when objective or stop line ambiguity would materially change the
result. If `request_user_input` is available and the fork is blocking, use it
with concise options. Otherwise state the assumption and proceed.

## Routing

Use this skill when the user asks to optimize, improve, polish, strengthen, or
"优化/深度优化/改进/提升" prompts, instructions, plans, workflows, configs,
skills, documents, reasoning processes, decisions, or standalone artifacts.
Use `深度审查优化` as the concise explicit entry for a review-then-optimize
loop.

Route to the specific owner when it fully covers the request:

- `review`: review-only, audit-only, risk finding, "有没有问题".
- `self-refine`: non-project artifact polishing.
- `three-step-analysis`: deep non-project decisions.
- `co-star`: fuzzy quick task specification or prompt shaping.
- `retrospective`: lessons, repeated failure, future behavior improvement.
- `project-refine`: software project docs, prompts, copy, or written artifacts.
- `project-analysis`: architecture, debugging strategy, or technical decision.
- `project-iteration`: code, tests, build config, UI behavior, implementation.
- `project-bootstrap`: new software project creation.

For deep, repeated, best-possible, or multi-framework optimization, this skill may orchestrate those owners.
When invoking another skill, read its `SKILL.md` before claiming use and preserve its boundary.

For implementation tasks, define strategy, then hand off to the owner. Edit files only when the user explicitly asked to change the artifact.

## Framework Chains

Choose the shortest chain that satisfies the requested depth:

- **Simple polish**: `self-refine`.
- **Deep optimization**: run the framework exhaustion loop below. `review` may
  be used as an evidence gate, but it never replaces framework exhaustion.
- **Fuzzy input**: `co-star` -> `self-refine`.
- **Failure-driven improvement**: `retrospective` -> relevant optimizer.
- **Software project optimization**: project adapter skill first; this skill is
  only the orchestrator.

For skills, configs, prompts, workflows, and decision processes, default to the
framework exhaustion loop unless the user clearly wants wording polish. Add
`retrospective` only when prior failures should change future behavior.

Deep optimization overrides shortest-chain minimization. Do not shorten, skip,
or replace the required framework exhaustion sequence.

## Review-Optimize Loop

When the user says `深度审查优化`, `深度 review + 深度优化`, or equivalent,
or asks to review, optimize, and re-review in one request, run this explicit
loop:

```text
review initial gate
-> Finding Ledger
-> Optimization Target Queue
-> framework exhaustion loop
-> review closeout gate
-> restart if a material review finding remains or appears
```

For `深度审查优化`, use `review` depth `deep` for both the initial gate and
closeout unless the user explicitly narrows the target or asks for
`exhaustive`/`全面`/`逐词逐句`.

After a target has passed a deep review-optimize loop, later calls start from
preservation, not reinvention. Change it only if new failure evidence appears,
a pressure scenario fails, active instructions conflict, or the change
simplifies the artifact while preserving behavior.

`review` remains review-only. `optimize` owns edits only when the user allowed
changes. Convert each review ledger item into one queue item:

- `fix now`: solve in this optimization.
- `defer`: leave out with reason and residual risk.
- `reject`: reject with evidence.
- `blocked`: cannot solve without missing permission, context, or unsafe action.

Counters do not transfer across skills. A material review finding resets
`framework_clean_cycles` to 0 and restarts optimization from `co-star`. A
material optimization delta resets review clean passes and requires closeout
after the delta. Stop only when the optimization loop has two consecutive clean
framework-exhaustion cycles and the final review closeout has completed the
`review` skill's required clean passes for its depth, unless the user set a
smaller limit, a blocker appears, or the edit boundary prevents closure.

## Framework Exhaustion Loop

Use this loop when the user asks for deep optimization, best-possible quality,
repeated optimization, or explicitly says to keep using thinking frameworks.

One framework-exhaustion cycle is the full required sequence:

```text
co-star -> three-step-analysis -> self-refine -> three-step-analysis -> self-refine -> co-star
```

Each framework pass must actually read that skill's `SKILL.md` and apply its
lens. Mentioning a framework, using intuition, or running a validation command
does not count:

- `co-star`: check whether the task definition, objective, audience, style,
  constraints, or response format can be made sharper.
- `three-step-analysis`: check the problem essence, evaluation standard,
  hidden assumptions, competing paths, and dialectical objections.
- `self-refine`: generate or inspect the current artifact, critique it, and
  identify concrete refinement points.

In the exhaustion loop, `co-star` is a task-definition audit lens, not the owner
of multi-skill orchestration. Preserve the invoked skill's boundary while using
its cognitive role.

A framework pass is a **no-point pass** only when it finds no material
optimization point under that lens. Script validation, grep checks, line counts,
or ordinary clean passes do not count as framework no-point passes.

A framework-exhaustion cycle is **clean** only when all six passes in the
sequence are no-point. Individual no-point passes do not count as a clean cycle.
Non-consecutive clean cycles do not accumulate across a later material finding.

If any framework finds a material optimization point, apply the smallest correct
change, record which framework found it, reset `framework_clean_cycles` to 0,
and restart the required sequence from `co-star`. Stop only after two
consecutive clean framework-exhaustion cycles, unless a blocker, safety
boundary, or explicit user limit is reached.

If `review` is used as an evidence gate and finds a material issue, treat it as
a material optimization point: apply or report the correction according to the
user's edit boundary, log the review finding, reset `framework_clean_cycles` to
0, and restart from `co-star`.

For software-project artifacts, preserve the same roles through project
adapters when needed: `project-brief` for the CO-STAR role, `project-analysis`
for the three-step role, and `project-refine` for the self-refine role. An
adapter pass counts only when both the adapter `SKILL.md` and the underlying
framework `SKILL.md` are read, the framework role is applied, and the final pass
log names the adapter.

### Framework Pass Log Requirement

For deep optimization, a framework pass counts only when it records an auditable
log entry:

```yaml
cycle: <N>
pass: <1-6>
framework: <co-star | three-step-analysis | self-refine>
skill_read: <SKILL.md path read after the latest reset, or in this turn when no reset occurred>
adapter: <project-brief | project-analysis | project-refine | none>
adapter_skill_read: <adapter SKILL.md path, or none>
inspected_target: <artifact, file, section, or behavior inspected>
lens_applied: <what this framework specifically checked>
result: <found | no-point>
evidence: <line, section, command output, or concrete reason>
action: <patch applied | reset | none>
```

For project adapter passes, both `adapter` and `adapter_skill_read` are required.
No framework pass log means the pass does not count.
No six ordered pass logs means the cycle does not count.
No two consecutive complete clean cycle logs means deep optimization is not complete.

Do not claim "two clean cycles completed" from validation commands, broad review, memory, or a summary judgment.
Only the ordered framework pass log counts.

## Workflow

### 1. Frame

Briefly state target, objective, constraints, and framework chain when they
affect the result. Reject false optimization:

- complexity without measurable benefit,
- expanding scope beyond the user's target,
- preserving unrequested legacy behavior,
- changing tone or architecture because it is familiar,
- replacing the target with an easier substitute.

### 2. Diagnose

Find the limiting factor: unclear objective, weak philosophy-to-behavior map,
weak structure, missing evidence, low signal-to-noise, inconsistent logic, poor
audience fit, unsafe action, stale assumptions, or wrong call chain. For complex
strategic targets, use `three-step-analysis`.

### 3. Improve

Apply the selected chain:

- With `three-step-analysis`, finish the analysis before committing to a path;
  do not edit during analysis-only requests.
- With `review`, lead with evidence-backed findings and do not fix them unless
  optimization edits were requested.
- With `self-refine`, run generate -> critique -> refine loops until material
  improvement stops or the requested round count is reached.
- With project adapters, preserve their handoff, documentation, verification,
  and commit rules.

Make the smallest change that satisfies the objective and preserves what works.

### 4. Converge

After each pass, run a convergence check.

A material optimization point improves objective fit, reduces risk, removes
ambiguity, improves verification, simplifies without losing capability, or
better matches the user's stated preferences.

A clean pass finds no material optimization point, verification gap, framework
mismatch, over-broad scope, stale wording, or output-quality issue.

For ordinary optimization, if a material point is found, apply another pass and
reset `clean_passes` to 0; otherwise increment it. Stop after two consecutive
clean passes, a fixed round count, blocker, or safety boundary.

For deep optimization, `clean_passes` are only auxiliary checks. The stop
condition is the Framework Exhaustion Loop: two consecutive full cycles must
complete with no material points. Do not continue for wording-only polish or
added complexity without measurable benefit.

For deep optimization, the final report must list each framework pass in order
and mark it as `found: <material point>` or `no-point`; otherwise the exhaustion
loop is not auditable and does not count. The report must include the two most
recent consecutive complete six-pass no-point cycles and any reset history
caused by a framework finding a material point.

### 5. Verify

Use target-specific verification:

- text/prompt/plan: critique against objective, audience, constraints, and
  clarity.
- skill/config: metadata, trigger, boundaries, cross-skill references, stale
  wording, philosophy-to-behavior alignment, context cost, validation commands,
  and pressure scenarios for trigger, boundary, failure, and handoff behavior.
- workflow/process: trigger scenario, behavior change, failure mode, and
  measurable outcome.
- code/project artifact: verification owned by the relevant project skill.

Do not claim completion without saying how it was checked. If verification is
not runnable, state why.
For skill/config optimization, say whether pressure scenarios were executed,
simulated locally, or not run; do not count scenario checks as framework passes
unless the required framework lens was actually applied.

## Output

Default report:

```markdown
Optimization Result
- Target: <what was optimized>
- Objective: <what better means>
- Framework chain: <skills used or selected>
- Review-optimize loop: <used | not used>

Changes
- <material change and why it improves the target>

Review-Optimize Loop
- Finding Ledger: <initial review items and statuses, or N/A>
- Optimization Target Queue: <fix now | defer | reject | blocked items, or N/A>
- Review Closeout: <clean | reopened | blocked | N/A>

Convergence
- Optimization passes: <N ordinary passes, or N framework passes inspected in deep mode>
- Clean passes: <clean_passes>/2 for ordinary optimization, or N/A for deep framework exhaustion
- Framework clean cycles: <framework_clean_cycles>/2 for deep optimization, or N/A for ordinary optimization
- Framework exhaustion: <two consecutive clean cycles completed | reset after finding by framework | not required>
- Framework pass log:
  - Reset history: <framework, material point, action, restart point, or none>
  - Clean cycle 1: <six ordered pass log entries with evidence>
  - Clean cycle 2: <six ordered pass log entries with evidence>
- Stop reason: <two consecutive framework-exhaustion clean cycles | two consecutive clean passes | requested round count | blocker | safety boundary>

Verification
- <check performed or Not run: reason>

Residual Risk
- <remaining risk or none>
```

For analysis-only requests, output the recommended optimization strategy and
stop. For edit requests, apply the change and report the concrete delta.
