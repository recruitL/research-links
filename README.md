# research-links

个人研究方向知识库，用于长期沉淀 EOB、GSF、BHPT、QNM、PM/EFT、LISA waveform modeling 和 numerical methods 的技术脉络、关键文献、代码库入口、AI 初评、人工校验、复现状态和开放问题。

This repository is a research knowledge base, not a plain link list.

完整 EOB 候选数据保存在 `data/papers/eob_candidates.csv`。topic 页面只是人工整理后的研究入口，不能替代 CSV 数据层。

The complete EOB candidate dataset is stored in `data/papers/eob_candidates.csv`.
Topic pages are curated interpretive views and must not replace the CSV data layer.

## 仓库定位

本仓库用于回答：

- 一个研究方向的技术链条如何从原始论文发展到当前模型？
- 哪些论文是基础、方法、校准、应用或代码实现？
- 哪些代码库可用于复现、诊断或改造？
- AI 初评给出了什么线索，哪些地方必须人工校验？
- 哪些结果已经复现，哪些仍被依赖、环境或理论细节阻塞？

## 三层结构

| 层级 | 作用 | 文件形式 |
| --- | --- | --- |
| 数据层 | 全量记录、可筛选、可更新、可脚本处理 | CSV / YAML / JSON |
| 分析层 | 技术脉络、人工判断、AI 评价、复现记录 | Markdown |
| 展示层 | README、topic 首页、roadmap、GitHub Pages | Markdown / HTML |

核心原则：

- CSV 是底账。
- Markdown 是解释层和展示层。
- Markdown 不得替代 CSV。
- 从 arXiv API 抓取的完整候选记录必须保留。
- 后续更新只能 append、version 或明确记录覆盖原因，不得静默覆盖旧数据。

## 如何使用

1. 从 topic 首页了解方向定位和主问题。
2. 阅读 roadmap 理清技术链条。
3. 查 `data/` 下的 CSV 获取全量候选记录。
4. 用 `templates/` 中的模板写论文、代码库、AI 评价和复现笔记。
5. 用 `scripts/` 检查 CSV 和生成轻量索引。
6. 把复现状态记录到 `reproducibility/`。

## Topics

| Topic | Entry | Data |
| --- | --- | --- |
| EOB | [topics/eob/README.md](topics/eob/README.md) | [data/papers/eob_candidates.csv](data/papers/eob_candidates.csv) |
| GSF | [topics/gsf/README.md](topics/gsf/README.md) | [data/papers/gsf_candidates.csv](data/papers/gsf_candidates.csv) |
| BHPT | [topics/bhpt/README.md](topics/bhpt/README.md) | [data/papers/bhpt_candidates.csv](data/papers/bhpt_candidates.csv) |
| QNM | [topics/qnm/README.md](topics/qnm/README.md) | [data/papers/qnm_candidates.csv](data/papers/qnm_candidates.csv) |
| PM/EFT | [topics/pm-eft/README.md](topics/pm-eft/README.md) | [data/papers/pm_eft_candidates.csv](data/papers/pm_eft_candidates.csv) |
| LISA | [topics/lisa/README.md](topics/lisa/README.md) | [data/papers/lisa_candidates.csv](data/papers/lisa_candidates.csv) |
| Numerical methods | [topics/numerical-methods/README.md](topics/numerical-methods/README.md) | [data/codebases/numerical_tools.csv](data/codebases/numerical_tools.csv) |

## Roadmaps

- [EOB from origin to current](roadmaps/eob-from-origin-to-current.md)
- [PM to EOB](roadmaps/pm-to-eob.md)
- [GSF from MiSaTaQuWa to second order](roadmaps/gsf-from-mi-sa-ta-qu-wa-to-second-order.md)
- [BHPT to GSF](roadmaps/bhpt-to-gsf.md)
- [QNM methods](roadmaps/qnm-methods.md)
- [EOB-Teukolsky connection](roadmaps/eob-teukolsky-connection.md)
- [LISA waveform modeling](roadmaps/lisa-waveform-modeling.md)

## Data Schema

- Paper schema: [data/schemas/paper_schema.md](data/schemas/paper_schema.md)
- Codebase schema: [data/schemas/codebase_schema.md](data/schemas/codebase_schema.md)
- Review schema: [data/schemas/review_schema.md](data/schemas/review_schema.md)
- Status schema: [data/schemas/status_schema.md](data/schemas/status_schema.md)
- Tags: [data/tags.yaml](data/tags.yaml)
- Status values: [data/status.yaml](data/status.yaml)

## AI Evaluation Policy

AI evaluation 只是初筛，不是最终学术判断。所有 AI 评价必须有人类校验。

评分采用：

- A = must read / central
- B = useful / relevant
- C = background
- D = peripheral
- X = unclear / unreliable / needs human check

详细规范见 [docs/ai-evaluation-protocol.md](docs/ai-evaluation-protocol.md)。

## Reproduction Tracking

复现入口：

- [reproducibility/candidates.md](reproducibility/candidates.md)
- [reproducibility/reproduced.md](reproducibility/reproduced.md)
- [reproducibility/failed-or-blocked.md](reproducibility/failed-or-blocked.md)

复现记录必须区分：

- 只读过论文；
- 复现了公式；
- 跑通了代码；
- 复现了图表或数值；
- 发现阻塞。

## Update Rule

- 修改 CSV 前先确认是否会覆盖旧数据。
- 重新抓取 arXiv 后记录行数、字段变化和时间。
- 不确定条目写 `needs verification` 或 `not yet human-checked`。
- 新增 AI 评价时必须补 `human_checked` 状态。
- 新增复现时必须记录环境、命令、输出和误差。

## 当前 EOB 数据统计

- 完整候选文件：`data/papers/eob_candidates.csv`
- 原始迁移文件：`data/eob_arxiv_candidates.csv`
- 候选记录：443 条
- 覆盖年份：1998-2026
- 当前人工精选入口：`data/papers/eob_selected.csv`

## Scripts

- `python3 scripts/check_csv_integrity.py`
- `python3 scripts/summarize_eob_csv.py`
- `python3 scripts/build_topic_index.py`
- `python3 scripts/check_links.py`
