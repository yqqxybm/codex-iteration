# 变更影响矩阵

遇到不确定"这次改动要同步哪些文件"时查这张表。

这张表只发现候选影响面，不决定新增文件。新增、删除或保留文档必须先符合
`software-contract/references/docs-deliverables.md` 的 `doc_profile`。

## 代码层变更 → 文档层变更

| 本次对话发生的事 | 要改的文件（按受众） |
|---|---|
| 新增 API / 路由 | 真实 API/usage/integration 入口；只有 profile 要求时才同时更新 architecture |
| 新增 / 改名 环境变量 | 真实配置入口；README/AGENTS/runbook 中已经承担配置职责的位置 |
| 新增数据库表 / 列 | schema/data model/architecture 中 profile 要求的入口 |
| 新增 / 改动 用户流程 | README/AGENTS/product scope/architecture 中已经承担流程职责的位置 |
| 新增大特性（跨多文件） | 先按 profile 判断外部视角、架构视角、运维视角、交接视角哪些适用，再更新对应入口 |
| 新增术语 / 改命名 | `docs/integration-guide.md` 术语表（如果有）+ 全局搜索旧术语并只替换本项目相关命中 |
| 部署参数 / 基础设施变化 | `docs/operator-runbook.md` · 项目根 markdown 部署章节 |
| 下游项目接入方式变化 | 下游项目的 `docs/<integration>.md` · 上游项目的 `integration-guide.md` |

## Codex 上下文变更

| 情况 | 处理方式 |
|---|---|
| 过期事实 | 改对应 `AGENTS.md` 或 docs 条目 |
| 相对时间("今天"、"最近") | 全部转成绝对日期(例如 `2026-05-15`，而非"今天") |
| 重复记录(多条说同一件事) | 合并为一条 |
| 已完成的待办 | 删除——知识库不是历史档案 |
| 推翻的决策 | 删除旧条目，保留新决策 |
| 跨会话只用一次的临时上下文 | 删除 |

## 跨项目影响检查

最容易漏改的场景:

- **上游 API 变了 → 下游 SDK 文档**：协议变化必须两边对齐
- **共享子域 / 路由 / 环境变量改了 → 已知 consumer 项目的 setup 文档**
- **认证中台变更 → 已知接入应用的 integration guide**
- **公共组件 / 基础设施升级 → 相关项目的 operator-runbook 提及版本号的地方**

判断方法：这次改的东西有没有 SDK、子域、共享配置、跨进程协议？有就要在已知依赖项目里搜一遍提到这件事的文档。

## 文档结构通用约定

新增一个能力（API、flow、特性）的标准动作不是四处都补，而是四类视角逐项判定：

1. **外部视角**：存在外部集成者、API/SDK/CLI 使用者时，维护 usage/integration/API 入口
2. **架构视角**：改变边界、数据流、状态机或重要取舍时，维护 architecture/decision 入口
3. **运维视角**：改变部署、监控、环境变量、故障处理或定时任务时，维护 runbook/operator 入口
4. **交接视角**：阶段完成、版本交付或明确 handoff 时，维护 handoff/CHANGELOG/release 入口

API 速查表、环境变量表、术语表是高频查询的结构化信息，**必须保持"所见即最新"**。
