---
name: project-docs
description: >
  Project documentation and handoff skill. Use for README, project AGENTS.md,
  docs/, runbooks, architecture notes, targeted doc sync, or full handoff
  cleanup. Routine code changes update directly affected docs through
  project-iteration instead.
---

# Project Docs

You are a project knowledge editor, not a recorder. A recorder appends; an
editor audits the whole knowledge surface, merges duplicates, corrects stale
facts, and deletes obsolete context. Keep project knowledge clean, accurate, and
ready for future Codex sessions and human handoff.

## Lifecycle Position

这是软件项目生命周期里的 `handoff` / 文档清洁 skill。它负责项目级知识体系：
README、项目根 `AGENTS.md`、`docs/`、交接材料和过期上下文清理。

不要把它用于每次小代码改动。普通迭代中的直接文档影响由
`project-iteration` 在同一 diff 里处理；当阶段完成、准备交接、文档混乱、
新人需要上手或上下文明显过期时，再使用本 skill 做全量对齐。

## Mode Selection

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
durable project knowledge.

Return a Handoff Record with docs reviewed, docs changed, durable decisions
captured, stale content removed, verification output, open risks, and the next
recommended skill. Promote only stable facts from `.codex/traces/` into
README, project `AGENTS.md`, or `docs/`; do not turn traces into formal docs.

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

这三层**受众不同，职责不重叠**。AGENTS.md 里写"新增了 device flow 五个路由" ≠ docs/integration-guide.md 里"下游怎么接这套 flow" —— 前者是提醒 Codex，后者是教别人。**两份都要写。**

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
failure mode of this skill.

### 第二步：识别变更——用"变更影响矩阵"思考

**不要只看对话增量有什么新事实，要看新事实会波及哪些文档层级。**

常见模式速览：
- 新增 API / 路由 → AGENTS.md 路由清单 + integration-guide + architecture 的 Routes
- 新增 / 改名 环境变量 → AGENTS.md 环境变量表 + runbook + 下游 integration-guide
- 新增数据库表 → AGENTS.md + architecture 的 Data Model
- 新增大特性（跨多文件） → 以上全部 + architecture 新章节 + handoff 已完成清单
- 跨项目改动 → 上下游两边的 docs **都要对齐**（最常见的漏改场景）
- 长期上下文层面：相对时间→绝对日期、过期事实→改、重复→合并、已完成待办→删

完整映射表（覆盖更多变更类型与对应文档）见 **[references/sync-matrix.md](references/sync-matrix.md)**——遇到不确定的改动先查这张表。

**关键检查**：这次对话是不是**跨项目**的？如果改了项目 A 且项目 B 依赖它（通过 SDK、API、子域、环境变量），**项目 B 的 docs 也要改**。这是历次同步最常见的遗漏点。

### 第三步：实际修改（用 Codex 工具，不只是描述）

你必须**真的修改文件**，而不是只描述方案。手工编辑优先用 `apply_patch`；批量格式化可用项目已有格式化命令；删除废弃文件用明确的删除命令。

"我会怎么改"的描述不算完成。

**编辑顺序**：先改 docs/（改错影响外部）→ 再改项目 `AGENTS.md` → 最后按需改 `~/.codex/AGENTS.md`。先动外部优先级最高的，即使中途被打断，读者看到的也是对齐的最新状态。

**编辑原则**：

- **合并优于追加**：新信息是对旧信息的更新，改旧条目，不要再加一条
- **删除优于保留**：完成的临时计划、推翻的决策、过期的上下文，删掉
- **精确优于冗长**：一条长期上下文只说明一件事，不混塞多件事
- **绝对时间**：写成具体日期（例如 `2026-05-15`），不写"今天"、"最近"
- **面向读者**：docs/ 的读者是"第一次接触这个项目的外部人"，写的时候想象对方只有 5 分钟能看完
- **受众不混**：AGENTS.md 里不抄 docs/ 的全文，docs/ 里不写"我记得上次……"——这是 Codex 上下文的事

**全局配置极度克制**：`~/.codex/AGENTS.md` 只有用户在对话中明确表达了**跨项目的核心原则**才动。日常项目细节绝不进全局。

**docs/ 编辑要点**——新增一个能力的文档变更通常要四处都补：
1. **integration-guide** 或对应"外部视角"文档：加**怎么用**（curl / SDK 示例 / 错误码表）
2. **architecture**：加**怎么工作**（数据流、状态机、设计取舍）
3. **runbook**：加**怎么运维**（冒烟命令、故障排查、环境变量）
4. **handoff** 或 CHANGELOG：加**已完成**

API 速查表、环境变量表、术语表是高频查询的结构化信息，**必须保持"所见即最新"**。

### 第四步：自检清单（必须逐项过一遍）

这一步防止"漏改 docs"。改完后逐条检查：

- [ ] 第一步列出的每个文件，都判断了"不用改"或"已改"
- [ ] 长期上下文索引（若有）里的每个链接指向存在的文件
- [ ] 每个长期上下文文件的 description 和内容对得上
- [ ] 长期上下文之间没有互相矛盾
- [ ] AGENTS.md 里提到的路径 / 命令 / 工具 / 环境变量在代码中真实存在
- [ ] README 的安装 / 运行步骤跟代码一致
- [ ] 新增 API 路由：**在 integration-guide 和 architecture 都出现了**
- [ ] 新增环境变量：**在 runbook 和项目根 markdown 都出现了**
- [ ] 新增数据库表：**在 architecture 的 Data Model 和项目根 markdown 都出现了**
- [ ] 跨项目影响：下游项目的 docs 也跟着改了
- [ ] 没有相对时间遗留（`grep -E "今天|昨天|刚刚|最近|上周|today|yesterday|recently"` 清零）

哪条打不了勾，**回去补**。不要因为"接近完成"就跳过这一步——这是这个 skill 的灵魂。

## Final Response / 变更摘要

在所有文件修改完之后（不是之前），给用户简洁摘要：

```
## 同步完成

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
- <command> → <key output>

### 未处理
- xxx（为什么没处理，比如需要用户确认）
```

只列有实际变更的条目。没改的不写。

## 特殊情况

**项目还没有 README 或 AGENTS.md**：判断项目是不是到了"有可运行代码"的阶段。是 → 创建。还在构思阶段 → 跳过，但在摘要里提一句。

**对话没有产生新事实**：审查现有长期上下文和文档有没有过期 / 冲突 / 相对时间——审查本身就有价值。

**长期上下文之间出现无法自动判断的矛盾**：列在「未处理」让用户决定。**这是唯一需要用户介入的情况**，其他都自己拍板。

**跨项目改动**：本次对话改了多个项目，每个项目都要跑一次完整的第一步（ls + 读 docs）。不要假设一个项目的 docs 改了，另一个就不用。尤其是上游-下游对接文档（集成指南 / SDK 说明 / API 协议），两边都要对齐。

**发现之前的同步漏了东西**：在当前模式覆盖范围内修掉；超出本次 targeted sync 的，列入未处理并说明需要 full handoff cleanup。

## 参考资料

- **[references/sync-matrix.md](references/sync-matrix.md)** — 完整的"变更类型 → 要改哪些文件"映射表
- **[references/agent-paths.md](references/agent-paths.md)** — Codex 长期上下文与配置路径速查
