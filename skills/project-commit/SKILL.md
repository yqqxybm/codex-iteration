---
name: project-commit
description: 使用 Angular 规范创建 focused git commit。当用户要求提交、保存变更、commit 时触发；也由 project-iteration 和 project-bootstrap 在验证通过后的版本管理阶段调用。只负责提交格式、分文件 stage、提交安全检查，不负责实现、部署或文档整理。
---

# Project Commit

使用 Angular 规范创建 git commit。

## Lifecycle Position

这是软件项目生命周期里的版本快照 skill。它只负责把已经验证过、
边界清楚的变更提交成干净历史。

不要用它替代：
- `project-iteration` 的实现、验证、审查
- `project-bootstrap` 的新项目初始化
- `project-release` 的版本 bump、tag、发布、回滚
- `project-docs` 的项目文档整理

## Call Chain Contract

When invoked by `project-lifecycle`, `project-bootstrap`, or `project-iteration`,
consume the Context Packet and stage only files inside `owned_scope`.

Return a Handoff Record with staged files, commit hash/message, skipped files,
security checks, hook result, open risks, and the next recommended skill. Never
treat `.codex/traces/` as Git history; traces are operational context only and
are not committed by default.

## Commit Message 格式

```
<type>(<scope>): <subject>

<body>
```

Codex 不默认添加 `Co-Authored-By` 或其他平台署名。只有用户明确要求或项目已有提交规范要求时，才添加用户指定的 trailer。

## Type 选择

| type | 含义 | 示例 |
|------|------|------|
| feat | 新功能 | 新增 API、新页面、新模块 |
| fix | Bug 修复 | 修复逻辑错误、崩溃、异常处理 |
| refactor | 重构 | 不改变行为的代码调整 |
| perf | 性能优化 | 查询优化、缓存 |
| docs | 文档 | README、注释、接入指南 |
| style | 格式 | 空格、分号、import 排序 |
| test | 测试 | 单元测试、集成测试 |
| chore | 构建/工具 | 依赖更新、CI/CD、Docker |
| ci | CI 配置 | GitHub Actions、K8s manifests |

## Scope 选择

优先使用当前仓库已有 commit 历史和项目模块命名。先看：

```bash
git log --oneline -20
```

如果项目没有既有 scope 规范，再按实际变更选择简短 scope，例如
`frontend`, `backend`, `api`, `auth`, `db`, `infra`, `docs`, `deps`, `test`。

多模块变更时 scope 可省略，或使用最主要模块。不要把无关项目的固定 scope 套到当前仓库。

## 执行流程

1. `git status` 查看变更
2. `git diff --staged` 和 `git diff` 分析变更内容
3. `git log --oneline -5` 参考最近的提交风格
4. 根据变更内容选择 type 和 scope
5. subject 用英文、小写开头、不加句号、祈使语气
6. 多类变更优先用最主要的 type，body 中补充说明其他变更
7. 运行 `git diff --cached --check`，并检查 staged diff 中没有 secrets、token、credential URL 或无关用户改动
8. 使用 HEREDOC 格式提交：

```bash
git add path/to/file1 path/to/file2
git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>
EOF
)"
```

## 注意事项

- 不要 `git add .` 或 `git add -A`，逐个添加文件
- 不要提交 `.env`、credentials、secrets 等敏感文件
- 不要提交未验证、未审查或不属于当前任务的 hunk
- 不要 amend 上一个 commit，除非用户明确要求
- 不要自动 push，除非用户明确要求
- pre-commit hook 失败时，修复问题后创建新 commit，不要 amend

## Final Response

Report:
- staged files,
- commit hash and message,
- hook/security check result,
- skipped files or blocker, if any.
