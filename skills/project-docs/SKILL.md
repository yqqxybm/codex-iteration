---
name: project-docs
description: >
  Downstream project documentation and handoff stage selected by
  project-lifecycle. Use when the lifecycle controller assigns README, project
  AGENTS.md, docs/, runbooks, architecture notes, targeted doc sync, or full
  handoff cleanup. Routine code changes update directly affected docs through
  project-iteration instead.
---

# Project Docs

You are a project knowledge editor, not a recorder. A recorder appends; an
editor audits the whole knowledge surface, merges duplicates, corrects stale
facts, and deletes obsolete context. Keep project knowledge clean, accurate, and
ready for future Codex sessions and human handoff.

## Lifecycle Position

这是软件项目生命周期里的下游 `handoff` / 文档清洁 skill。它负责项目级知识体系：
README、项目根 `AGENTS.md`、`docs/`、交接材料和过期上下文清理。

不要把它用于每次小代码改动。普通迭代中的直接文档影响由
`project-iteration` 在同一 diff 里处理；当阶段完成、准备交接、文档混乱、
新人需要上手或上下文明显过期时，再使用本 skill 做全量对齐。

## Mode Selection

- **Review-only audit**: when the user says "核验", "检查", "审查", "看看文档",
  or equivalent without asking to fix, add, sync, or clean up, do not create or
  edit docs. Use `review` when the task is purely an audit; if this skill is
  already invoked by a controller, return findings, inspected files, missing or
  excessive docs, and proposed changes only.
- **Targeted sync**: use when the user points at a specific doc, narrow behavior
  change, or known stale section. Inspect the referenced docs plus README /
  project `AGENTS.md` indexes needed to avoid contradiction.
- **Full handoff cleanup**: use when the user asks for handoff, newcomer
  readiness, stage completion, or reports broad doc drift. Enumerate the whole
  project knowledge surface before editing.

Do not expand targeted sync into full cleanup unless the local evidence shows
cross-document contradictions or missing handoff-critical information.

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet and prior
Handoff Records before editing docs. Distinguish temporary trace facts from
durable project knowledge. Preserve `doc_profile`, `docs_ia`, and
`verification_scope` when provided. When provided, also preserve `project_goal`,
`goal_runtime`, `goal_synthesis` / `control_system_goal`, `goal_preflight` /
`optimality_law`, `perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`loop_control_matrix`, `review_clean_pass_loop`,
`optimize_framework_cycle_loop`, `runtime_resource_ledger`,
`subagent_runtime_registry`, `subagent_dispatch_policy`, `agent_owner`,
`write_policy`, and `protocol_evidence`.

Return a Handoff Record with docs reviewed, docs changed, durable decisions
captured, stale content removed, standard compliance delta, verification output,
`domain_resource_evidence` when `software-contract` was loaded, open risks, and
the next recommended skill. When assigned a formal plan state file, update only
that project-native plan state and return `plan_state_sink_delta`; do not create
extra planning docs unless the doc profile or lifecycle controller authorized
them. Promote only stable facts from `.codex/traces/` into README, project
`AGENTS.md`, or `docs/`; do not turn traces into formal docs.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Edit docs only when the
assigned `write_policy` permits it; otherwise return findings or a proposed patch
to `project-lifecycle`.

## Standard Development Docs

When the Context Packet contains `standard_compliance_ledger`, or the user asks
to apply the standard development guide, use any provided ledger as the current
coverage state. If no ledger exists and standard coverage is requested, create a
compact doc-owned ledger from the Standard Development Contract before editing.
Load `software-contract` and read
`~/.codex/skills/software-contract/references/standard-development-contract.md`
and `~/.codex/skills/software-contract/references/docs-deliverables.md` before
claiming standard doc coverage. If either reference cannot be read, stop and
report the missing resource; do not recreate the coverage map or path mapping
from memory.

Hard rule retained here: every applicable standard doc item needs a ledger
status and evidence boundary. The ledger is a maturity/evidence map, not a file
creation order. Before creating any document, derive a `doc_profile` from
`docs-deliverables.md` and show why the current project shape and stage require
a standalone file. Equivalent paths are valid only when the mapping is explicit
in the ledger.

Also apply `doc_profile.docs_ia`: root-level files are only repository entry and
tool conventions; standalone docs belong under the authorized `docs/`
subdirectories instead of piling into one flat folder.

## 为什么这件事重要

在 Codex 协作开发中，代码可以通过版本历史、测试和审查持续修正，但**文档和 Codex 项目上下文是跨会话的桥梁**。如果 `AGENTS.md` 或 docs 里有过期信息，下次 Codex 会基于错误前提做决策。如果 docs/ 混乱或缺失，接手者（尤其是下游项目的同事）会浪费大量时间搞清楚这套系统怎么用。

这个 Skill 的价值就在于：**让知识体系的每一层都跟得上代码的变化。**

## 关键概念：三类知识，三种受众

**必须先理解这件事，否则容易只改 AGENTS.md 就结束，遗漏真正面向人类和下游系统的文档。**

| 位置 | 受众 | 职责 | 不同步的代价 |
|------|------|------|--------------|
| 全局 `~/.codex/AGENTS.md`（仅用户明确要求时） | Codex 跨项目复用 | 个人偏好、跨项目原则、非项目专属规则 | 下次会话 Codex 忘记长期偏好 |
| 项目根 `AGENTS.md` | 当前项目里的 Codex | 项目约定、结构、红线、环境变量、路由清单 | 下次 Codex 在这个项目里走弯路 |
| 项目 `docs/` + `README.md` | **其他人**（人类同事、下游开发者、未来接手的 Codex 会话） | 接入指南、架构图、运维手册、交接说明、API 参考 | **其他人或系统无法正确接入或运维** |

这三层**受众不同，职责不重叠**。AGENTS.md 里写"新增了 device flow 五个路由" ≠ docs/integration-guide.md 里"下游怎么接这套 flow" —— 前者是提醒 Codex，后者是教别人。是否两层都写，由项目形态、生命周期阶段、受众和 `doc_profile` 决定；不要把同一事实机械复制到每一层。

> Codex 没有独立的长期上下文文件索引；需要跨会话保留的信息写入 `AGENTS.md` 或项目 docs。路径速查见 [references/agent-paths.md](references/agent-paths.md)。

## 执行流程

### 第一步：盘点现状（按模式执行）

**先判断模式，再做文件盘点。**

Targeted sync reads only the minimal doc set needed to make the requested section
true and non-contradictory. Full handoff cleanup uses the mechanical enumeration
below.

Full handoff cleanup:

1. 列出 Codex 上下文文件：
   - 全局：`~/.codex/AGENTS.md`（只有用户明确要求改全局规则时才修改）
   - 项目：从当前目录向上查找所有 `AGENTS.md`
2. 对本次对话涉及的**每一个项目**：
   - `ls <project-root>/` → 确认根目录结构
   - `find <project-root>/docs -type f 2>/dev/null | sort` → **枚举 docs 文件**（缺失也要确认）
   - `find <project-root> -maxdepth 3 -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*"` → 补充枚举散落的 .md
   - 读 `README.md`、`AGENTS.md`、`docs/` 下每一个相关 Markdown 文件
3. 必要时读全局 Codex 配置：`~/.codex/AGENTS.md`
4. 回顾当前可见的对话上下文和本轮已执行命令

Full handoff cleanup must produce an internal file inventory and mark each file
as `reviewed`, `changed`, or `no-change`. Missing a relevant doc is the main
failure mode of this skill; creating an irrelevant doc is the other main failure
mode. The inventory must include a `doc_profile` and identify docs that are
required, conditional, prohibited-by-default, duplicate, stale, or excessive for
the current project shape.
The inventory must also identify misplaced docs: root-level files or flat
`docs/*.md` that should live under `docs/product/`, `docs/architecture/`,
`docs/development/`, `docs/operations/`, `docs/integrations/`, or
`docs/handoff/`.

### 第二步：识别变更——先用文档契约，再看影响矩阵

**不要只看对话增量有什么新事实，也不要把新事实机械扩散到所有文档。先判断当前项目形态和阶段允许哪些文档存在，再判断新事实会波及哪些已有或必需层级。**

常见模式速览：
- 新增 API / 路由 → 先看 doc profile 是否需要 API/integration 合同；需要时更新已有合同或创建被契约允许的最小入口
- 新增 / 改名 环境变量 → 更新真实配置入口、README/AGENTS/runbook 中已经承担配置职责的位置
- 新增数据库表 → 只有存在持久化模型或外部协作需要时，更新 data model/schema/architecture
- 新增大特性（跨多文件） → 更新 scope、architecture、runbook、handoff 中实际存在且被 profile 要求的部分；不要自动创建全套文件
- 跨项目改动 → 上下游项目中承担该事实的相关入口要对齐（最常见的漏改场景）
- 长期上下文层面：相对时间→绝对日期、过期事实→改、重复→合并、已完成待办→删

影响矩阵见 **[references/sync-matrix.md](references/sync-matrix.md)**。它只用于发现候选影响面，不能越过 `doc_profile` 创建文档。

**关键检查**：这次对话是不是**跨项目**的？如果改了项目 A 且项目 B 依赖它（通过 SDK、API、子域、环境变量），**项目 B 的 docs 也要改**。这是历次同步最常见的遗漏点。

### 第三步：实际修改（用 Codex 工具，不只是描述）

当审查发现文档需要改变时，你必须**真的修改文件**，而不是只描述方案。
手工编辑优先用 `apply_patch`；批量格式化可用项目已有格式化命令；删除废弃文件用明确的删除命令。

"我会怎么改"的描述不算完成。

新增文件前必须通过 creation bar：

1. `doc_profile` 要求当前项目形态和阶段存在一个独立文档，
2. 没有现有 README、AGENTS、docs、schema、api、workflow 或配置文件可以干净承载该信息，
3. 新文件包含项目特定事实、命令、决策、责任人或下一步，
4. ledger 记录了映射和状态。

不满足时，修改/合并/删除现有文档，或把缺口标成 `not_applicable`、`deferred`、`blocked`、`missing`。不要为了核验、证明执行过或满足文件名清单而新增文档。

新增或迁移文档还必须通过 placement bar：

1. 根目录只放 README、AGENTS、LICENSE、CONTRIBUTING、CHANGELOG 和项目原生配置，
2. 独立文档按职责放入 `docs/product/`、`docs/architecture/`、
   `docs/development/`、`docs/operations/`、`docs/integrations/` 或
   `docs/handoff/`,
3. 只有一两个简单独立文档时才允许平铺在 `docs/`；达到三个或跨多个受众时必须分目录，
4. 不创建空目录或占位文件来伪造结构。

如果完整盘点后没有任何文档需要改变，保持文件不变，并在 Handoff Record
中报告 `no-change` 证据、已检查文件和为什么不需要修改。不要为了证明执行过
本 skill 而制造无意义编辑。

**编辑顺序**：先改 docs/（改错影响外部）→ 再改项目 `AGENTS.md` → 最后按需改 `~/.codex/AGENTS.md`。先动外部优先级最高的，即使中途被打断，读者看到的也是对齐的最新状态。

**编辑原则**：

- **合并优于追加**：新信息是对旧信息的更新，改旧条目，不要再加一条
- **删除优于保留**：完成的临时计划、推翻的决策、过期的上下文，删掉
- **精确优于冗长**：一条长期上下文只说明一件事，不混塞多件事
- **绝对时间**：写成具体日期（例如 `2026-05-15`），不写"今天"、"最近"
- **面向读者**：docs/ 的读者是"第一次接触这个项目的外部人"，写的时候想象对方只有 5 分钟能看完
- **受众不混**：AGENTS.md 里不抄 docs/ 的全文，docs/ 里不写"我记得上次……"——这是 Codex 上下文的事

**全局配置极度克制**：`~/.codex/AGENTS.md` 只有用户在对话中明确表达了**跨项目的核心原则**才动。日常项目细节绝不进全局。

**docs/ 编辑要点**——新增能力时只更新被 `doc_profile` 允许且实际承担职责的入口：
1. **外部视角**：只有存在外部集成者、API/SDK/CLI 使用者时，维护 integration/API/usage 入口
2. **架构视角**：只有能力改变边界、数据流、状态机或重要取舍时，维护 architecture/decision 入口
3. **运维视角**：只有部署、监控、环境变量、故障处理或定时任务变化时，维护 runbook/operator 入口
4. **交接视角**：只有阶段完成、版本交付或明确 handoff 时，维护 handoff/CHANGELOG/release 入口

API 速查表、环境变量表、术语表是高频查询的结构化信息，**必须保持"所见即最新"**。

标准开发指南的交付物补齐遵循同一原则：先合并到现有权威入口，再创建缺失入口；
先写真实边界、命令、验证和责任人，再扩展说明文字。不要用空模板满足账本。

### 第四步：自检清单（必须逐项过一遍）

这一步防止"漏改 docs"。改完后逐条检查：

- [ ] 第一步列出的每个文件，都判断了"不用改"或"已改"
- [ ] 长期上下文索引（若有）里的每个链接指向存在的文件
- [ ] 每个长期上下文文件的 description 和内容对得上
- [ ] 长期上下文之间没有互相矛盾
- [ ] AGENTS.md 里提到的路径 / 命令 / 工具 / 环境变量在代码中真实存在
- [ ] README 的安装 / 运行步骤跟代码一致
- [ ] `doc_profile` 已记录项目形态、阶段、必需文档、条件文档和默认不创建项
- [ ] `doc_profile.docs_ia` 已记录根目录和 docs/ 子目录归属；新增/迁移文档位置正确
- [ ] 新增文档均通过 creation bar；没有因模板、文件名清单或核验动作而新增文档
- [ ] 新增 API 路由：在 profile 要求的 API/integration/architecture 入口中有证据，或标记不适用
- [ ] 新增环境变量：在真实配置入口和 profile 要求的 README/AGENTS/runbook 中有证据，或标记不适用
- [ ] 新增数据库表：在 profile 要求的 schema/data model/architecture 入口中有证据，或标记不适用
- [ ] 跨项目影响：下游项目的 docs 也跟着改了
- [ ] `standard_compliance_ledger` 中每个文档项都有状态和证据
- [ ] 没有相对时间遗留（`grep -E "今天|昨天|刚刚|最近|上周|today|yesterday|recently"` 清零）

哪条打不了勾，**回去补**。不要因为"接近完成"就跳过这一步——这是这个 skill 的灵魂。

## Documentation Verification

For docs-only work, verification is documentation evidence by default:

- inspect the final diff for every touched doc,
- run `git diff --check` in Git repos,
- check touched links, paths, commands, env vars, or anchors when practical,
- run configured Markdown/docs lint or docs build only when present and relevant,
- run the relative-time grep from the checklist for durable docs.

Do not run `make verify`, full app tests, full builds, or browser checks for a
docs-only edit unless the user explicitly requested full project verification,
the docs changed runnable commands/API/config/deploy/test instructions that need
targeted proof, or a release/security/compliance gate requires broader evidence.

## Final Response / 变更摘要

在所有文件修改完之后（不是之前），给用户简洁摘要：

```
## 文档对齐完成

### 长期上下文变更
- 更新：xxx（原因）
- 新增：xxx
- 删除：xxx（原因）

### 文档变更（按项目分组，每个项目列全改动的文件）
- <项目 A>/AGENTS.md — xxx
- <项目 A>/docs/integration-guide.md — xxx
- <项目 A>/docs/architecture.md — xxx
- <项目 B>/docs/<integration>.md — xxx

### 验证
- <command or evidence> → <key output>

### 资源证据
- `domain_resource_evidence`: <software-contract references loaded or missing, when used>

### 未处理
- xxx（为什么没处理，比如需要用户确认）
```

只列有实际变更的条目。没改的不写。若完整审查后没有文件需要修改，报告
`no-change`、已检查范围、关键证据和剩余风险，而不是套用"文档变更"清单。

## 特殊情况

**项目还没有 README 或 AGENTS.md**：判断项目是不是到了"有可运行代码"的阶段。是 → 创建。还在构思阶段 → 跳过，但在摘要里提一句。

**用户只要求核验 / 检查 / 审查**：默认不编辑、不新增文档。报告 inspected files、missing docs、excessive docs、stale docs、proposed changes 和 residual risk。只有用户明确要求"修 / 补齐 / 同步 / 清理"时才进入修改。

**对话没有产生新事实**：审查现有长期上下文和文档有没有过期 / 冲突 / 相对时间——审查本身就有价值。

**长期上下文之间出现无法自动判断的矛盾**：列在「未处理」让用户决定。**这是唯一需要用户介入的情况**，其他都自己拍板。

**跨项目改动**：本次对话改了多个项目，每个项目都要跑一次完整的第一步（ls + 读 docs）。不要假设一个项目的 docs 改了，另一个就不用。尤其是上游-下游对接文档（集成指南 / SDK 说明 / API 协议），相关项目中承担该事实的入口要按 `doc_profile` 对齐。

**发现之前的同步漏了东西**：在当前模式覆盖范围内修掉；超出本次 targeted sync 的，列入未处理并说明需要 full handoff cleanup。

## 参考资料

- **[references/sync-matrix.md](references/sync-matrix.md)** — 完整的"变更类型 → 要改哪些文件"映射表
- **[references/agent-paths.md](references/agent-paths.md)** — Codex 长期上下文与配置路径速查
