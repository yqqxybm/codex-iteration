---
name: project-retrospective
description: >
  Downstream project retrospective / 项目复盘 stage selected by
  project-lifecycle when the lifecycle controller enters the learn phase.
  Extracts reusable lessons from completed project work. Does not implement,
  commit, deploy, or replace project-docs. Project adapter for the retrospective
  cognitive core.
---

# Project Retrospective（经验提炼/复盘）

## Overview

做完就忘是最大的浪费。复盘不是写流水账，而是提取**非显而易见的经验**，写入 Codex 可检索的项目文档，让未来的自己和后续 Codex 会话都能受益。

**核心原则：** 区分"结果质量"和"决策质量"。好结果可能是运气，坏结果可能决策没错。复盘的对象是决策过程，不是结果。

## Lifecycle Position

这是软件项目生命周期里的下游 `learn` skill，也是 `retrospective` 认知内核的项目适配层。
它把已发生的项目经验转化为未来可复用的判断和操作规则。
非软件项目复盘使用 `retrospective`。

不要用它替代：
- `project-analysis` 的事前复杂项目决策
- `project-iteration` 的实现与验证
- `project-docs` 的项目文档全量整理

复盘产出的经验必须服务于项目哲学中的知识沉淀和证据闭环。

## Call Chain Contract

When invoked by `project-lifecycle`, consume its Context Packet and prior
Handoff Records before reviewing the work. Use actual decisions, commands,
failures, fixes, verification evidence, and `standard_compliance_ledger` instead
of vague impressions. When provided, preserve `project_goal`, `goal_runtime`,
`goal_synthesis` / `control_system_goal`, `goal_preflight` /
`optimality_law`, `perspective_model`, `plan_state_sink`, `cyclic_goal_loop`,
`subagent_dispatch_policy`, `agent_owner`, `write_policy`, and
`protocol_evidence`.

Return a Handoff Record with lessons extracted, decisions audited, durable
experience entries written or skipped, `standard_compliance_delta`, open risks,
`domain_resource_evidence` when `software-contract` was loaded, and the next
recommended skill. Include any item status, result, and verification evidence
needed by an active `plan_state_sink`. Use `.codex/traces/` as source material
only; durable lessons must follow the active `doc_profile` / `docs_ia` and go
through `project-docs` when a project doc needs to be created or moved.

If invoked as a subagent, preserve the assigned `agent_owner` and `write_policy`;
do not edit the parent goal, do not spawn subagents, commit, push, deploy, sync
remote state, broaden scope, or claim project completion. Write durable lessons only
when the assigned `write_policy` permits it; otherwise return findings or a
proposed lesson entry to `project-lifecycle`.

When the Standard Development Contract is active, update learn-phase entries:
Postmortem template applicability, incident/postmortem records, Tech-Debt log,
SLO/error-budget lessons, runbook updates, and ADR/retrospective follow-ups.
If the retrospective discovers a standard gap, return it to `project-lifecycle`
or `project-docs` instead of treating the lesson as complete.
When standard learn-phase details affect status, load `software-contract` and
read `~/.codex/skills/software-contract/references/standard-development-contract.md`.
If the required reference is unavailable, stop and report the missing resource.

## Learn Phase Timing

**总控分派：** `project-lifecycle` 在用户提出"复盘"、"总结经验"、"这次学到什么"
等项目复盘意图，或进入 learn phase 时调用本 skill。

**Codex 标记复盘价值：** 在以下场景完成后，向 `project-lifecycle` 标记复盘价值，
不中断当前任务：
- 修复了耗时 > 30 分钟的 bug
- 完成了跨多文件的大功能
- 部署过程中遇到了意外问题
- 方案经历了重大方向调整
- 第三次犯同类错误

**不要在这些时候进入 learn phase：**
- 常规小改动、配置调整
- 一切顺利没有意外的任务
- 用户明显赶时间

## 复盘流程

### 轻量版（< 3 分钟，适合单个任务/bug）

用三个问题审查已有证据，每个只需一两句话：

```
1. 意外是什么？ — 什么事情和预期不同？（如果没有意外，可能不需要复盘）
2. 根因是什么？ — 为什么会出现这个意外？是认知盲区、流程缺陷、还是环境因素？
3. 下次怎么做？ — 具体的行为改变，不是空泛的"下次注意"
```

### 深度版（10-15 分钟，适合项目阶段/大功能）

```
1. 目标回顾 — 最初的目标是什么？最终达成了多少？偏差在哪里？
2. 决策审计 — 过程中做了哪些关键决策？每个决策当时的信息和理由是什么？
   → 哪些决策现在看仍然正确？（好决策，记住为什么）
   → 哪些决策现在看是错的？（识别当时的认知盲区）
   → 哪些决策结果好但过程有问题？（运气，不可复制）
3. 意外清单 — 列出所有出乎意料的事情，无论好坏
4. 经验提取 — 从上面提炼出 2-3 条可复用的经验
5. 行为改变 — 下次遇到类似情况，具体怎么做不同
```

### 选择哪个版本

```
刚修完一个 bug？ → 轻量版
完成了一个功能模块？ → 看复杂度，简单的轻量版，复杂的深度版
项目阶段结束？ → 深度版
部署出了问题？ → 轻量版（先恢复服务；阶段结束后再深度版）
```

## 产出与沉淀

**关键规则：复盘的价值在于产出可检索的经验，不是对话里聊完就算了。**

### 跨项目复用经验 → 写入 Codex 可检索位置

适合多个软件项目复用的经验。Codex 没有独立的长期上下文文件索引，默认沉淀到项目文档：

- 跨项目通用规则：只有用户明确要求全局沉淀时，更新 `~/.codex/AGENTS.md`
- 当前项目可复用经验：优先更新项目根 `AGENTS.md`
- 需要较长上下文或阶段记录：先使用 `doc_profile.docs_ia` 授权的复盘/决策/运维文档；
  如果没有授权落点，返回给 `project-docs` 建立或选择最小合适落点，不自行创建
  `docs/retrospective/`

**沉淀写法要求：**
- 标题或首句必须包含**触发场景**的关键词，这样未来相似场景才能匹配到
- 内容结构：经验结论 → **Why:**（为什么得出这个结论）→ **How to apply:**（什么场景下应用）

```markdown
# 好的 Codex 经验条目
## SSH 隧道调试：先检查 RemoteForward 端口占用

SSH 隧道不通时先 `lsof -i :端口` 检查目标端口是否被占用，再检查 sshd 配置。
**Why:** `YYYY-MM-DD`（写入时替换为实际日期）花了 40 分钟调试隧道，最后发现是端口被另一个进程占了。未先排除端口占用导致了无效重试。
**How to apply:** 任何 SSH 隧道/端口转发问题，先排除端口占用再看其他原因。
```

```markdown
# 差的经验条目（太模糊，未来匹配不到）
下次调试要更仔细。
```

### 项目特定经验 → 写入项目文档

适合项目内复用但不通用的经验。写入 active `doc_profile.docs_ia` 授权的项目文档落点；
`docs/retrospective/` 或 `CHANGELOG.md` 只有在该项目文档结构已经授权时才使用。
如果没有授权落点，返回给 `project-docs` 选择或建立最小合适落点，不自行创建。

例如：特定 API 的坑、项目架构的历史决策原因、部署流程的注意事项。

### 判断写哪里

```
这个经验换一个项目还适用吗？
  → 是 → 项目根 `AGENTS.md`（当前项目内可检索；全局仅在用户明确要求时写 `~/.codex/AGENTS.md`）
  → 否 → active `doc_profile.docs_ia` 授权的项目文档（跟代码一起版本控制）
  → 都有 → 项目根 `AGENTS.md` 写通用版，授权项目文档写具体版
```

## 认知偏差防御

复盘时容易掉入的陷阱：

| 偏差 | 表现 | 对策 |
|------|------|------|
| **结果偏差** | 成功了就觉得决策全对 | 拆分：决策过程对不对？结果好是能力还是运气？ |
| **后见之明** | "我早就知道会这样" | 回忆当时实际掌握的信息，不要用现在的信息评判过去 |
| **归因偏差** | 成功归自己，失败归环境 | 反过来想：成功有没有环境因素？失败有没有自身原因？ |
| **空泛总结** | "下次要更仔细" | 必须给出**具体行为**："下次先跑 X 命令确认 Y" |

## 常见反模式

**"没什么好复盘的"**
→ 如果一切如预期，确实不需要。但"一切如预期"本身值得问一句：是真的没意外，还是意外被忽略了？

**"写了经验但太笼统"**
→ 差的经验："部署要小心"。好的经验："K8s 滚动更新时先检查 PDB 配置，否则可能同时杀掉所有 pod"

**"只复盘失败不复盘成功"**
→ 成功的经验同样重要。"这次为什么顺利？"的答案可以变成未来的 checklist

**"复盘变成责任归咎"**
→ 焦点是"下次怎么做更好"，不是追究个人责任

## Quick Reference

```
轻量版（3 问）：
  1. 意外是什么？
  2. 根因是什么？
  3. 下次怎么做？
  → 产出 1 条 Codex 可检索经验

深度版（5 步）：
  1. 目标回顾
  2. 决策审计（对/错/运气）
  3. 意外清单
  4. 经验提取（2-3 条）
  5. 行为改变
  → 产出项目根 `AGENTS.md` 经验 + 项目文档（视情况）
```

## Final Response

Report:
- lessons extracted,
- concrete behavior changes,
- docs or AGENTS entries written, if any,
- `domain_resource_evidence`, when `software-contract` was loaded,
- unresolved uncertainty or follow-up review point.
