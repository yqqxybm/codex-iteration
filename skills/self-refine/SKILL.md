---
name: self-refine
description: >
  Iterative polish skill using generate, critique, and refine loops. Use for
  high-quality non-project writing, prompts, plans, copy, or standalone
  artifacts that need deliberate improvement. Use three-step-analysis for deep
  decisions. For software-project artifacts, use project-refine.
---

# Self-Refine 迭代精炼框架

当用户需要高质量产出物时，通过多轮"生成→批评→改进"循环来逐步提升质量。这个框架的核心理念来自学术论文 Self-Refine（Madaan et al., 2023）：同一个模型可以同时扮演生成者、批评者和改进者，通过迭代闭环实现质量跃升。

## Boundary

这是迭代精炼的唯一认知内核，不属于软件项目生命周期。它用于打磨非项目产出物，例如文章、
邮件、报告、公开文案、独立 prompt、方案文本或创意内容。

软件项目里的 README、runbook、架构说明、UI 文案、代码示例或交接材料，使用
`project-refine` 作为适配层。适配层只能加入项目事实、验证和文档边界，不另造一套精炼哲学。
需要深度决策时使用 `three-step-analysis`；软件项目决策使用 `project-analysis`。

## Three-Step-Governed Refinement

When the user explicitly asks each self-refine round to use `三步分析`, or when
`optimize`/`review` delegates a deep framework loop to this skill, each
critique round must consume a compact three-step model before refining:

```yaml
three_step_refine_frame:
  material_model: <relevant context, core contradiction, evaluation standard>
  calibration: <assumptions, reversal conditions, non-blocking question ledger>
  commitment: <what this round will preserve, change, reject, and verify>
```

This is not a second visible essay unless the user asks to see process. Use it
to make critique deeper: every material critique must trace to the evaluation
standard, a reversal condition, a missing evidence surface, or a failed
commitment. Do not add philosophical text that does not change the refinement.
For ordinary low-risk writing polish, keep the default lighter self-refine loop.

## 为什么需要这个框架

一次性生成的内容，即使质量不错，往往存在视角单一、表达不够精炼、遗漏边界情况等问题。人类作者也是通过反复修改来提升作品质量的。这个框架把"修改"这个过程结构化了，避免无方向的反复调整。

## 前置：判断适用性

先判断这个任务是否适合迭代精炼：

- **适合**：写作（文章、邮件、报告）、非项目方案文本、创意内容、Prompt优化
- **不太适合**：需要深度分析的决策问题（用三步认真分析）、软件项目产物（用 project-refine）、简单的信息查询、一次性格式转换
- **迭代轮数**：默认 2-3 轮。如果用户明确要求"写到最好"或产出物特别重要（如重要商业邮件、公开发布内容），可以增加到 4-5 轮
- **展示策略**：默认内部迭代，只交付终稿和关键改进摘要；只有用户要求看过程时，才展示初稿、批评和中间版本。

## 阶段 1：初始生成

目标：先快速产出一个完整的初稿，不追求完美，但要覆盖所有关键要素。

### 执行步骤

1. **明确产出物规格**：在动笔之前，确认以下要素（如果用户没有明确说明，做出合理假设并在输出中标注）：
   - 目标受众是谁？
   - 核心目的是什么？（说服、告知、教育、娱乐……）
   - 风格/语气要求？（正式、轻松、技术性、通俗……）
   - 长度/格式约束？
   - 有无参考范例或需要遵循的模板？

2. **生成初稿**：基于上述规格，生成完整的初稿。关键是"完整"——宁可粗糙但完整，也不要精美但残缺。初稿是后续迭代的基础。

3. **记录初稿**作为后续迭代基础；默认不向用户输出。

### 内部记录格式（仅在用户要求展示过程时输出）

```
### 初稿 v1

**产出物规格：**
- 受众: [描述]
- 目的: [描述]
- 风格: [描述]
- 约束: [描述]

---

[初稿内容]

---

[仅展示过程时说明后续会继续批评和改进]
```

## 阶段 2：自我批评（Critique）

目标：切换到"批评者"视角，系统性地找出初稿的问题。

这个阶段的关键心态转换是：假装你不是写初稿的那个人，而是一个严格但建设性的审稿人。不要因为是自己写的就手下留情。

### 批评维度

根据产出物类型，从以下维度中选择相关的进行评估（不必每个维度都评，选择最影响质量的3-5个）：

**通用维度：**
- **准确性**：事实是否正确？逻辑是否自洽？
- **完整性**：是否覆盖了所有关键点？有没有遗漏重要内容？
- **清晰度**：读者能否一遍看懂？有没有歧义或模糊表达？
- **简洁性**：是否有冗余？能否用更少的字表达同样的意思？
- **结构**：信息组织是否合理？读者的阅读体验是否流畅？

**写作类额外维度：**
- **说服力**：论据是否有力？是否回应了读者可能的质疑？
- **语气匹配**：是否符合目标受众和场景的语气要求？
- **开头/结尾**：开头是否抓人？结尾是否有力？

### 批评格式

对每个问题，不仅指出"哪里有问题"，还要给出"为什么是问题"和"建议怎么改"。

### 内部批评格式（默认不展示）

```
### 自我批评 (Round N)

**总体评价：** [一两句话概括当前版本的整体水平和最大的提升空间]

**具体问题：**

1. **[问题类别]** — [具体位置/段落]
   - 问题：[描述问题是什么]
   - 影响：[为什么这是个问题，对读者/用户有什么影响]
   - 建议：[具体的改进方向]

2. **[问题类别]** — [具体位置/段落]
   - 问题：[描述]
   - 影响：[描述]
   - 建议：[描述]
...

**优点保留：** [指出初稿中做得好的部分，改进时不要破坏这些]
```

## 阶段 3：改进（Refine）

目标：基于批评意见，生成改进版本。

### 执行要求

1. **逐一处理批评中的每个问题**，不要遗漏
2. **保留批评中指出的优点**，改进不是推倒重来
3. **改进要具体**，不是简单地"换个说法"，而是真正解决底层问题
4. **标注改动**：在改进版本后，简要说明做了哪些关键改动以及为什么

### 内部改进记录（默认不展示）

```
### 改进版 v(N+1)

---

[改进后的完整内容]

---

**本轮主要改动：**
- [改动1]：[原因]
- [改动2]：[原因]
...
```

## 阶段 4：迭代判断

每完成一轮"批评→改进"后，判断是否需要继续迭代：

**停止条件（满足任一即可）：**
- 自我批评中只发现细微问题（措辞层面的微调），没有结构性或实质性问题
- 已达到预设轮数上限
- 改进幅度递减——当前轮次的改动明显小于上一轮

**继续条件：**
- 仍存在影响核心目的的实质性问题
- 用户明确要求继续改进
- 上一轮的改动引入了新问题（这种情况需要重点关注）

如果继续，回到阶段 2 开始新一轮批评。如果停止，进入阶段 5。

## 阶段 5：终稿与总结

输出最终版本，并附上迭代总结：

### 输出结构

```
### 终稿

---

[最终版本内容]

---

**迭代总结：**
- 共经过 [N] 轮迭代
- 主要提升点：[列出2-3个最重要的改进]
- 可继续优化但当前已足够好的方向：[如果有的话，指出边际收益有限的方向]
```

## 原则与注意事项

- 每轮迭代的批评要诚实、具体，不要走形式。如果确实找不到实质性问题，就该停止迭代而不是硬挑毛病
- 批评和改进要有层次感：第一轮关注大问题（结构、逻辑、完整性），后续轮次逐步聚焦小问题（表达、语气、细节）
- 如果用户在过程中提出反馈，将用户反馈视为最高优先级的批评意见，在下一轮改进中优先处理
- 迭代不是目的，质量提升才是。如果初稿已经很好，1轮迭代就够了；如果问题很多，可能需要4-5轮
- 对于可运行的独立示例，能运行就加入实际运行验证；无法运行时说明阻塞点。

## Final Response

Report:
- final artifact,
- iteration count,
- 2-3 most important improvements,
- verification result when the artifact is runnable or testable,
- open risk only when it changes whether the artifact is usable.
