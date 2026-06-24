# Language Policy

本仓库采用语言分层规则：机器执行规则用英文，研究内容沉淀用中文。

## 人类阅读内容：中文优先

面向人类阅读的研究分析内容，默认使用中文。

包括但不限于：

- `topics/<topic>/README.md`
- `topics/<topic>/timeline.md`
- `topics/<topic>/problem-map.md`
- `topics/<topic>/method-map.md`
- `topics/<topic>/literature.md`
- `topics/<topic>/codebases.md`
- `topics/<topic>/ai-review.md`
- `topics/<topic>/open-questions.md`
- `roadmaps/*.md`
- `reviews/**/*.md`
- `reproducibility/*.md`
- `docs/vision.md`
- `docs/how-to-use.md`
- `docs/data-policy.md`
- `docs/ai-evaluation-protocol.md`
- `docs/update-log.md`

## 机器/代理执行规则：英文

面向机器或代理执行的规则文件，使用英文。

包括：

- `AGENTS.md`
- `skills/*.md`
- `scripts/*.py` 内的变量名、函数名、注释和命令行输出

## CSV 规则

CSV 字段名保持英文，方便脚本处理。

例如：

```text
arxiv_id,title,authors,year,technical_tags,technical_role,relevance,status,ai_rating,human_checked,notes
```

CSV 中的自然语言内容可以使用中文，尤其是：

- `technical_role`
- `relevance`
- `notes`
- human check notes
- AI evaluation notes

## 技术术语

Markdown 文件中的技术术语可以保留英文原词，中文解释优先。

示例：

- 有效单体理论（Effective-One-Body, EOB）
- 引力自力（gravitational self-force, GSF）
- 黑洞微扰理论（black-hole perturbation theory, BHPT）
- 拟正规模（quasinormal modes, QNMs）
- 因子化/重求和波形（factorized/resummed waveform）
- 数值相对论校准（NR calibration）
- 规范不变量比较（gauge-invariant comparison）

不要翻译已确立的缩写，例如 EOB、GSF、BHPT、QNM、NR、PN、PM、EFT、EMRI、LISA。

## README

`README.md` 可以采用中英混合，但中文优先，并至少包含中文总览。
