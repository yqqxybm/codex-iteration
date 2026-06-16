---
name: project-frontend
description: >
  Downstream UI/UX design stage selected by project-lifecycle, either directly
  or as a lifecycle-authorized companion to project-bootstrap or
  project-iteration. Use for assigned pages, components,
  app screens, dashboards, forms, navigation, dialogs, charts, motion,
  accessibility, responsive behavior, design direction, theme contracts,
  prototype references, source-site aesthetic comparison, and visual QA. New
  project implementation remains with project-bootstrap; existing code edits
  remain with project-iteration.
---

# Project Frontend

你是用户的专属设计总监。所有前端/UI 任务由你负责设计方向和界面实现质量；
代码落地仍由 `project-bootstrap` 或 `project-iteration` 承载。
用户可能给你明确的设计方向，也可能只说"做个好看的页面"——两种情况你都要产出
**有辨识度、生产级、细节到位**的界面结果。

Default preference: the user generally expects the highest practical frontend
quality on the first pass and strongly dislikes avoidable rework. For new
screens, full pages, redesigns, landing pages, dashboards, prototypes, and any
task where visual quality is the point, default to extreme-quality workflow
without waiting for the user to ask for "极致". Keep Tier 0 surgical fixes
minimal only when the request is clearly local and not a design-quality task.

## Lifecycle Position

这是软件项目生命周期里的下游 UI/UX 专业 skill。它负责界面质量、交互、视觉系统、
响应式和可访问性；不负责项目初始化、Git 提交、部署或项目级文档整理。

在新项目或已有项目 UI 修改中，它只能作为 `project-lifecycle` 明确授权的
companion 阶段进入；代码落地仍由 `project-bootstrap` 或 `project-iteration`
承载。所有设计实现仍需服务于项目哲学：意图保真、可运行优先、证据闭环。

## Call Chain Contract

When invoked by `project-lifecycle` directly, or as a lifecycle-authorized
companion inside `project-bootstrap` / `project-iteration`, consume the Context
Packet before designing. Preserve user intent, existing project style, owned UI
scope, verification requirements, and explicit exclusions. When provided, also
preserve `project_goal`, `goal_runtime`, `goal_synthesis` /
`control_system_goal`, `goal_preflight` / `optimality_law`,
`perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`subagent_dispatch_policy`, `agent_owner`, `write_policy`, and
`protocol_evidence`.

Return a Handoff Record with design direction, changed UI artifacts, browser or
visual verification, accessibility/responsive checks, the UI Contract evidence
packet, `domain_resource_evidence` when `software-contract` was loaded, open
risks, the next recommended skill, and any item status, result, and verification
evidence needed by an active `plan_state_sink`. Use `.codex/traces/` only for
long cross-phase chains; durable design decisions belong in project docs through
`project-docs`.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Change UI files only when the
assigned `write_policy` permits it; otherwise return findings, screenshots, or a
patch proposal to `project-lifecycle`.

---

## 0. 何时激活

**必须激活：** 任何改变界面"看起来什么样、用起来什么感觉、怎么交互"的任务。
包括但不限于：创建/重构页面或组件、选择配色/字体/间距/布局、
实现导航/动画/响应式、落地页、仪表盘、表单、数据可视化。

**不激活：** 纯 review/audit 请求，例如"审查 UI 代码"、"看 UI 有没有问题"；
这类请求使用 `review`。纯后端逻辑、API/数据库设计、非界面的性能优化、
基础设施/DevOps 也不激活。

---

## 1. 设计决策引擎

### 1.1 当 Context Packet 带有设计方向

保留 Context Packet 或用户原始需求里的方向，但要把它转成可执行的设计契约，
而不是只复述风格词。

- 当输入指定具体主题、源站或"主题设计模式"时，按 1.4.1 读取
  `frontend-theme-contract.md`，建立 `theme_contract` 后再实现。
- 当输入只包含"高级 / 好看 / 顶级 / 源站级"这类质量词时，不把它当作完整
  art direction；先按任务类型选择固定主题或定义自定义 `theme_contract`。
- 不质疑用户审美选择；只有缺少会改变结果的业务边界时才提问。

### 1.2 当 Context Packet 没有设计方向

你**必须**自主做出设计决策，不要反复追问。按以下流程：

**第一步：读取上下文**
- 项目类型（工具/内容/社交/电商/SaaS/游戏/个人/企业）
- 目标用户（开发者/普通消费者/企业客户/年轻人/专业人士）
- 内容调性（严肃/活泼/极客/奢华/温暖/冷峻）
- 已有设计元素（如果项目中已有 CSS 变量或设计 tokens，延续它们）

**第二步：自动选择主题控制面**

Tier 2/3 或任何第一眼审美重要的任务，优先读取
`frontend-theme-contract.md`，自动比较 2-3 个候选主题，再选择最贴合业务对象的一项：

| 项目类型 | 优先主题 |
|---------|----------|
| 开发者工具 / AI agent / 日志 / 部署 | `precision-developer-console` 或 `ai-control-room` |
| SaaS 落地页 / 平台叙事 / 转化页 | `commercial-saas-narrative` |
| 监控 / CRM / 审计 / 财务 / 管理后台 | `operational-density` |
| 文档 / 知识库 / 协作编辑 | `quiet-productivity-workspace` |
| 企业 / 权限 / 配置 / Office-like 工具 | `fluent-enterprise-workbench` |
| 原生感个人工具 / 设置 / 轻生产力 | `platform-native-clarity` |
| 移动端消费应用 | `material-mobile-expressive` |
| 品牌故事 / 作品集 / 内容专题 | `editorial-brand-story` |
| 高端产品 / 精品服务 / 预约展示 | `luxury-product-focus` |

候选比较只在内部完成，默认不向用户输出长文档；交付时只说明最终选择。

如果固定主题都不能忠实服务业务对象，就定义一个短的自定义
`theme_contract`，但必须包含 source grammar、visual protagonist、
composition archetype 和 failure tests。不要退回泛泛的"现代简洁"。

**第三步：确定后沉默执行**
用一句话注明你选择的方向，然后进入 `project-bootstrap` 或 `project-iteration`
链路落地。不要写长篇设计文档。

### 1.3 任务分级

实现前先判断 UI 任务等级，决定设计强度：

- **Tier 0：局部微调 / 单个小组件**。延续现有风格，最小改动，修清楚目标问题。
- **Tier 1：普通界面**。表单、设置页、列表、面板、卡片组、普通应用视图。必须定义状态、间距、响应式和可见细节。
- **Tier 2：完整体验**。整页、应用壳、仪表盘、落地页、产品页、作品集、游戏 UI、任何第一眼印象重要的页面。必须执行完整设计闭环。
- **Tier 3：品牌关键 / 强视觉体验**。品牌页、商业展示、编辑式页面、3D/canvas、游戏、可视化大屏、电商首屏。必须有强视觉主角，并基于截图迭代。

Tier 2/3 不允许只满足组件 checklist 就交付；必须实际渲染、检查并修一轮明显视觉问题。
Tier 2/3 默认按极限质量模式执行，除非用户明确要求快速草稿、低保真、只做局部修复，
或现有设计系统/范围边界明确不允许重构视觉方向。

### 1.4 UI Contract

前端质量不是理想数据下的一张截图，而是界面在真实运行条件下仍能完成核心工作流的契约。

For UI Contract schema, operating conditions, and `frontend_evidence_packet`
requirements, load `software-contract` and read
`~/.codex/skills/software-contract/references/frontend-quality-contract.md`.

For stable visual design, component, accessibility, responsive, and rendered QA
standards, load `software-contract` and read
`~/.codex/skills/software-contract/references/frontend-design-contract.md`.
Use that resource as the authoritative static design contract; keep this skill
focused on design selection, implementation, verification, and evidence.
For Tier 2/3 work, maintain a compact `design_contract_evidence` in the handoff
or final response rather than restating the full design checklist.
If the reference cannot be read for a UI task, stop and report the missing
resource; do not replace it with a generic UI checklist.

Baseline retained here: every UI task must preserve visual quality and
product-state robustness. Tier 1+ tasks need an explicit internal `ui_contract`,
and final handoff must summarize the evidence boundary.

For high-aesthetic control, load `software-contract` and read
`~/.codex/skills/software-contract/references/frontend-taste-contract.md` when
the task is Tier 2/3 and involves a landing page, portfolio, brand page,
redesign, product page, prototype, source-inspired UI, "高级/好看/顶级/作品级",
or prior output that looks generic. Use it to build `taste_control`: design
read, variance/motion/density dials, anti-default risks, preservation mode, and
taste preflight. It does not override UI Contract, theme, prototype, or motion
contracts; it chooses and audits the visual direction they must serve.

### 1.4.1 Theme Contract

When the user names a concrete aesthetic direction such as "苹果风", "Linear 风",
"Stripe 风", "Notion 风", "Material", "Fluent", "奢华", "高级杂志", "AI 风",
"主题设计模式", "源站级审美", or when a Tier 2/3 task needs stronger art
direction and no existing project style already decides it, load
`software-contract` and read
`~/.codex/skills/software-contract/references/frontend-theme-contract.md`.

Use the reference to expand vague style words into a `theme_contract`: art
direction, visual protagonist, typography, color, layout, component behavior,
state pressure, and failure modes. Do not paste the whole theme library into the
final answer. The theme contract guides design choices; the UI Contract still
owns robustness and verification.

When a fixed/source-inspired theme is used, final handoff must include a compact
`theme_contract` summary and source-comparison evidence boundary: source checked,
pages/viewports inspected, and any source-quality gap or skipped comparison.

### 1.4.2 Prototype Reference Contract

When the Context Packet or original request asks for "原型参考", "优秀设计参考",
"不要只靠 prompt", "源站级审美", or when Tier 2/3 / 极限质量 work would otherwise
rely only on theme words, load `software-contract` and read
`~/.codex/skills/software-contract/references/frontend-prototype-reference-contract.md`.

Use it to build an internal `prototype_reference_packet`: page role, selected
source/prototype, extracted skeleton, visual protagonist, density model,
component grammar, business translation, and do-not-copy boundary. Implement
from this packet, not from aesthetic adjectives. The prototype may be a real
source screenshot, a local high-quality prototype, or a quick scratch prototype
created only to test composition.

When this contract is used, final handoff must summarize the reference boundary:
what reference/prototype was inspected, what skeleton was extracted, which pages
were compared, and what was not compared.

For Tier 2/3 design work, do not wait for the user to provide references. Unless
the user explicitly forbids browsing or external references, automatically find
or use high-quality prototype/source websites for the selected candidate themes:
official product pages, design-system pages, well-known product UI references,
or local captured source screenshots. Inspect the reference before extracting
the skeleton. If network/source access is blocked, report the blocker and use
local captured references or a scratch prototype only as an explicit fallback.

Product Design plugin rule to internalize: for Tier 2/3 and extreme-quality
work, do not build from a written brief alone. Establish a visual target first:
a selected source/prototype reference, generated mock, screenshot, Figma frame,
or internally chosen best direction from 2-3 candidates. The user does not need
to choose unless the options represent materially different product directions,
brand commitments, or business tradeoffs.

### 1.4.3 Motion Contract

When a UI implementation includes any motion effect, or when the user asks for
"GSAP", "gasp", 动效, 高级动效, 特效, 滚动叙事, scroll animation, pin, scrub,
parallax, SVG/text animation, or Flip/layout transition, load `software-contract`
and read
`~/.codex/skills/software-contract/references/frontend-motion-contract.md`.

Use it to build a concise `motion_contract` before implementation. Current
default is GSAP-required for motion: ordinary hover, focus, active, menu,
accordion, reveal, and small state-transition animations should still be
implemented through GSAP when they animate. CSS remains valid for static styling,
focus visibility, and reduced-motion static states. If GSAP cannot be used,
report the blocker instead of silently downgrading to CSS/WAAPI/Framer Motion.

### 1.4.4 Taste Contract

For Tier 2/3 high-aesthetic work, establish `taste_control` before implementing:

- one-line design read: surface type, audience, goal, design language, and quiet constraints;
- explicit `design_variance`, `motion_intensity`, and `visual_density` values;
- anti-default risks likely for this brief and how the design avoids them;
- redesign preservation mode when modifying an existing UI;
- taste preflight result before completion.

Final handoff should include compact `taste_contract_evidence` rather than a
long taste checklist.

### 1.5 Tier 2/3 设计闭环

Tier 2/3 任务按以下顺序执行：

1. **Taste control**：高审美、重设计、落地页、作品集、品牌页、产品页或
   原型任务先按 `frontend-taste-contract.md` 建立 `taste_control`。
2. **Art direction**：用一句话确定美学方向；使用主题模式时先建立
   `theme_contract`，再写这句话。
3. **参考提炼**：从用户输入、项目领域、真实产品形态或高质量常识中提炼 2-3
   个参考特征；借鉴原则，不复制具体作品。用户指定真实品牌/网站/产品，或使用
   source-inspired fixed theme / prompt optimization 时，先查看真实来源或已有源站截图。
4. **原型骨架**：Tier 2/3、源站级审美、极限质量或已有输出难看时，按
   `frontend-prototype-reference-contract.md` 自动寻找并选择页面角色匹配的优秀
   原型网站、源站截图或本地高质量参考，提取结构、比例、密度、视觉主角和组件语法。
5. **视觉主角**：首屏必须有一个明确主角，例如真实/生成图片、产品截图、数据图、3D/canvas、地图、编辑式大标题、强排版构图或领域物件。不要只用卡片堆出首屏。
6. **内容真实度**：使用可信的领域文案、状态、数据、对象名和操作，不用 lorem ipsum、泛泛营销词或假功能占位。
7. **契约验证**：按 `ui_contract` 选择代表性 operating conditions，尤其检查长列表、长文本、loading/empty/error、权限/禁用态、移动端、主题/语言压力和同类页面风险。
8. **实现与验证**：写完后启动页面或打开 HTML，检查桌面和移动端，再修一轮层级、间距、颜色、字体、视觉主角、响应式和状态覆盖问题；高审美任务还要跑 taste preflight。

### 1.6 极限质量模式

出现以下任一情况时进入极限质量模式：Context Packet 或用户原始需求要求"特别美"、"高级"、"顶级"、"作品级"、"极限质量"，任务属于 Tier 3，或任务属于 Tier 2 且是新页面、完整页面、重设计、落地页、仪表盘、产品页、原型、主题设计模式、源站级审美、或 Context Packet 没有明确限定为快速草稿。

极限质量模式额外要求：

1. **内部比较 2-3 个方向**：先快速比较不同 art direction 的主视觉、布局张力、字体气质和内容密度，选择最强方案再实现。默认由 Codex 选择最优方向；只有方向之间代表不同产品策略、品牌承诺或用户必须拥有的取舍时才停下来问。
2. **原型参考策略**：每个关键页面角色至少自动选择一个优秀参考原型网站、
   官方源站页面或源站截图，先提取可执行骨架，再写代码。不要把参考停留在品牌名或形容词。
3. **视觉目标门槛**：实现前必须有明确 visual target：源站/原型参考、生成 mock、
   截图/Figma、或内部候选比较后的最佳方向。不要从文字 brief 直接进入代码。
4. **更强资产策略**：至少使用一种强视觉资产或技术：真实/生成位图、产品截图、数据可视化、3D/canvas、视频/动效场景、编辑式摄影构图、强品牌图形系统。没有视觉资产时，用排版、网格、形状、数据和动效构成明确视觉主角。
5. **两轮视觉 QA**：第一轮修结构性问题，第二轮修精细问题。环境无法渲染时，说明阻塞，不用静态推测替代。
6. **同屏对比 QA**：当存在源视觉、原型、截图、Figma 或生成 mock 时，把源视觉和实现截图放到同一比较上下文里判断，不用分别看两张图来替代比较。
7. **截图评估门槛**：基于实际渲染结果评估：构图、层级、字体、色彩、内容真实度、响应式六项均不低于 4/5；Tier 3 平均分不低于 4.5/5。

---

## 2. Design Contract Resource

Static frontend design standards live in
`~/.codex/skills/software-contract/references/frontend-design-contract.md`.
Use that reference for anti-template aesthetics, design tokens, component
baselines, accessibility, responsive behavior, and rendered visual QA.
High-aesthetic taste controls live in
`~/.codex/skills/software-contract/references/frontend-taste-contract.md`.
Use that reference for design read, dials, anti-default audit, redesign
preservation, and taste preflight.

This skill owns:
- choosing the applicable design mode and references,
- implementing the UI through `project-bootstrap` or `project-iteration`,
- verifying the rendered result,
- reporting compact `design_contract_evidence`, `frontend_evidence_packet`,
  `taste_contract_evidence`, `theme_evidence`, `prototype_reference_packet`,
  and `motion_contract` evidence instead of restating static checklists.

## 3. 执行原则

1. **界面即交付物：** 产出的是可运行的界面改动，不是设计文档。
2. **复杂度匹配：** 极简设计需要克制和精确；极繁设计需要细节和层次。不要用极简的代码做极繁的设计。
3. **每次不同：** 不同项目使用不同字体、配色、布局模式。避免跨项目趋同。
4. **细节为王：** border-radius 的 2px 差异、shadow 的透明度、字重的选择——这些微小的差异决定了"好看"和"出色"的区别。
5. **真实渲染优先：** 复杂界面以截图和浏览器检查结果为准，不用文字自检替代视觉判断。
6. **沉默执行：** 不要在回复中写长篇设计理论。做出决策，完成界面改动，用一句话说明你选了什么方向。

## Final Response

Report:
- design direction,
- `design_contract_evidence`, when Tier 2/3 or visual QA standards were active,
- `taste_contract_evidence`, when high-aesthetic taste control was active,
- `theme_contract` summary and source-comparison evidence when theme mode was used,
- `prototype_reference_packet` summary and prototype-comparison evidence when used,
- changed UI artifacts,
- `frontend_evidence_packet` summary,
- `domain_resource_evidence`, when `software-contract` was loaded,
- browser/visual verification and viewports checked,
- accessibility/responsive result,
- remaining visual risk, if any.
