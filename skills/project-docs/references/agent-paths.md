# Codex 长期上下文与配置路径速查

此 skill 只面向 OpenAI Codex。执行文档同步时只检查 Codex 相关路径。

| 用途 | 路径 |
|---|---|
| 全局 Codex 指令 | `~/.codex/AGENTS.md` 或 `$CODEX_HOME/AGENTS.md` |
| 项目级指令 | 项目根 `AGENTS.md`，可按目录层级嵌套 |
| 全局 skills | `~/.codex/skills/<name>/SKILL.md` |
| 项目 skills | `.codex/skills/<name>/SKILL.md` |

Codex 没有独立的“长期上下文文件 + 索引”机制。需要跨会话保留的信息按以下规则沉淀：

- 当前项目事实、约定、红线：写入项目根或相关目录的 `AGENTS.md`
- 面向人类或下游系统的说明：写入 `README.md` 或 `docs/`
- 跨项目长期偏好：只有用户明确要求时，写入 `~/.codex/AGENTS.md`

盘点时从当前工作目录向上查找 `AGENTS.md`，并枚举项目内 `docs/` 与 `README.md`。若项目自己定义了其他上下文文件，把它当普通项目文档审查，不假定它会被 Codex 自动覆盖加载。
