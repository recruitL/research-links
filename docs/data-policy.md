# Data Policy

CSV 是本仓库的原始结构化数据层。Markdown 页面是解释层和展示层，不得替代 CSV。

## 保留原则

- 所有从 arXiv API 抓取的候选记录必须保留。
- 完整 EOB 候选数据保存在 `data/papers/eob_candidates.csv`。
- 原始迁移前文件 `data/eob_arxiv_candidates.csv` 暂时保留，用于追溯字段来源。
- 人工精选、技术分类、AI 评价、人工校验可以另建 CSV 或 Markdown。
- 不允许把全量 CSV 缩减成少量精选条目后静默覆盖原文件。

## 更新规则

- 重新抓取 arXiv 时，应保留旧版本或在 `docs/update-log.md` 记录更新方式、行数变化和字段变化。
- 清洗字段时，应保留原始字段或记录变更原因。
- 如果合并重复 arXiv ID，必须记录重复处理规则。
- 如果补充 `abstract`、`updated`、`journal` 等字段，应说明数据来源。

## 分层结构

- 数据层：CSV / YAML / JSON，面向筛选、脚本和统计。
- 分析层：Markdown，面向技术脉络、人工分析、AI 初评、人工校验和复现状态。
- 展示层：README、topic 首页、roadmap、GitHub Pages。

## 禁止事项

- 禁止删除完整 EOB CSV。
- 禁止用 Markdown 替代 CSV 数据层。
- 禁止伪造 arXiv ID、标题、作者或代码库状态。
- 禁止把 AI 评价写成最终人工判断。
