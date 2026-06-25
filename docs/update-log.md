# Update Log

## 2026-06-25 - QNM EP / VAM-TTM Research Topic

### Summary

新增 `QNM EP / 谱不稳定 / VAM-TTM` 子方向，用于整理 exceptional points、QNM 谱不稳定、pseudospectrum、semi-open SdS、virtual absorption modes 和 total transmission modes 的技术脉络。

### Added

- `topics/qnm-ep-vam-ttm/`：新增中文 topic 页面，包括 README、timeline、problem-map、method-map、literature、codebases、ai-review、open-questions 和 notes 入口。
- `roadmaps/qnm-ep-vam-ttm.md`：新增专项 roadmap。
- `data/papers/qnm_ep_vam_ttm_candidates.csv`：新增候选论文数据。
- `data/papers/qnm_ep_vam_ttm_selected.csv`：新增精选论文数据。
- `data/papers/qnm_ep_vam_ttm_timeline.csv`：新增时间线数据。
- `data/papers/qnm_ep_vam_ttm_categories.csv`：新增技术分类数据。

### Updated

- `topics/qnm/README.md`：加入 EP/VAM-TTM 子方向入口。
- `roadmaps/qnm-methods.md`：加入 EP、pseudospectrum 和 VAM/TTM 的代表文献和专项 roadmap 链接。
- `README.md`：加入 QNM EP/VAM-TTM topic 和 roadmap 入口。
- `data/site/research_topics.yml`：更新 QNM 展示数据源，并新增独立 `qnm-ep-vam-ttm` 展示条目，供个人网站生成 `/research/qnm-ep-vam-ttm/`。
- `data/tags.yaml`：加入 QNM EP/VAM-TTM 标签。

### Sources Checked

- arXiv pages/API for `2004.06434`, `2107.09673`, `2308.16227`, `2404.01374`, `2407.15191`, `2407.20850`, `2503.21276`, `2504.06072`, `2507.11663`, `2509.06411`, `2509.19451`, `2511.17067`, `2512.02110`, `2512.06903`, `2512.16372`, `2603.22261`, and `2603.22897`.

### Policy

- 新增 Markdown 研究分析内容使用中文。
- CSV 字段名保持英文，CSV 自然语言内容中文优先。
- 所有新文献当前均为 AI 初筛或 seed selection，`human_checked` 仍为 `no`。

## 2026-06-24 - Agent Workflow and Language Policy

### Summary

本次新增仓库级 agent 工作规则和语言分层规则。

### Added

- `AGENTS.md`：定义长期 agent 工作规则、数据层原则、AI evaluation policy、reproducibility rules 和 commit checks。
- `skills/`：新增 8 个 agent-facing workflow files：
  - `skills/research-direction-analysis.md`
  - `skills/literature-harvesting.md`
  - `skills/paper-classification.md`
  - `skills/codebase-analysis.md`
  - `skills/ai-evaluation.md`
  - `skills/roadmap-building.md`
  - `skills/csv-data-management.md`
  - `skills/reproducibility-tracking.md`
- `docs/language-policy.md`：明确机器执行规则用英文，研究内容沉淀用中文。

### Updated

- `README.md` 增加 Agent Workflow 和语言分层入口。
- `templates/*.md` 的人读标题和小节改为中文优先。

### Policy

- Human-facing Markdown outputs should be written primarily in Chinese.
- Agent-facing workflow documents should be written in English.
- CSV column names remain in English.
- Established abbreviations such as EOB, GSF, BHPT, QNM, NR, PN, PM, EFT, EMRI, LISA should not be translated.

### Check Results

Command: `test -f AGENTS.md && test -f docs/language-policy.md && test -f skills/*.md`

Result: required agent files exist.

Command: `rg -n "## Language Policy" AGENTS.md`

Result: `AGENTS.md` contains `## Language Policy`.

Command: `rg -n "Human-facing Markdown outputs should be written primarily in Chinese" skills/*.md`

Result: all 8 skill files contain the human-facing Markdown language rule.

Command: template heading check

Result: templates now use Chinese human-facing headings such as `论文笔记`, `代码库笔记`, `AI 初评`, `复现记录`, `路线图`, and `研究方向`.

Command: `python3 scripts/check_csv_integrity.py`

Result:

```text
CSV integrity check
target: data/papers/eob_candidates.csv
rows: 443
columns: 20
empty url rows: 0
empty pdf_url rows: 0
RESULT: OK
```

Command: `python3 scripts/check_links.py`

Result:

```text
checked urls: 1925
RESULT: OK
```

Command: `python3 scripts/summarize_eob_csv.py`

Result: completed, total rows = 443.

Command: `python3 scripts/build_topic_index.py`

Result:

```text
generated topics/eob/generated-index.md rows=443
```

## 2026-06-24 - Research Knowledge Base Upgrade

### Summary

本次将 `research-links` 从简单链接索引升级为三层 research knowledge base：

- 数据层：`data/` 下的 CSV/YAML/schema；
- 分析层：`topics/`、`reviews/`、`reproducibility/`；
- 展示层：根 `README.md`、topic 首页和 roadmaps。

### CSV Preservation

- PRESERVED: 原始 EOB CSV `data/eob_arxiv_candidates.csv`，行数 443 条数据 + 1 行 header。
- ADDED: 规范化 EOB 数据底账 `data/papers/eob_candidates.csv`，行数 443 条数据 + 1 行 header。
- ADDED: EOB 精选、时间线和分类 CSV：
  - `data/papers/eob_selected.csv`
  - `data/papers/eob_timeline.csv`
  - `data/papers/eob_categories.csv`
- ADDED: GSF/BHPT/QNM/PM-EFT/LISA seed candidate CSV。
- ADDED: codebase CSV for EOB, GSF, BHPT, QNM, waveform codes and numerical tools。

完整 EOB 候选数据保存在 `data/papers/eob_candidates.csv`。
Topic 页面只是人工整理后的研究入口，不能替代 CSV 数据层。

### New Directories

- `docs/`
- `topics/eob/`
- `topics/gsf/`
- `topics/bhpt/`
- `topics/qnm/`
- `topics/pm-eft/`
- `topics/lisa/`
- `topics/numerical-methods/`
- `data/papers/`
- `data/codebases/`
- `data/schemas/`
- `templates/`
- `reviews/`
- `roadmaps/`
- `reproducibility/`
- `scripts/`

### New Scripts

- `scripts/check_csv_integrity.py`
- `scripts/summarize_eob_csv.py`
- `scripts/build_topic_index.py`
- `scripts/check_links.py`

### Generated Files

- `topics/eob/generated-index.md` generated from `data/papers/eob_candidates.csv`.

### Check Results

Command: `find . -maxdepth 4 -type f | sort`

Result: completed. Non-git structure includes README, docs, data, topics, roadmaps, reviews, reproducibility, templates and scripts. Full command was run locally; `.git` internals were present in raw output and are intentionally not repeated here.

Command: `find . -name '*.md' -type f -empty -print`

Result: no empty Markdown files.

Command: CSV header check

Result:

```text
csv_files_checked 16
RESULT: OK
```

Command: `python3 scripts/check_csv_integrity.py`

Result:

```text
CSV integrity check
target: data/papers/eob_candidates.csv
rows: 443
columns: 20
empty url rows: 0
empty pdf_url rows: 0
RESULT: OK
```

Command: `python3 scripts/summarize_eob_csv.py`

Result:

```text
total rows: 443
primary_category: gr-qc 418, astro-ph.HE 11, hep-th 6, astro-ph.IM 3, astro-ph 2
status: candidate 443
human_checked: no 443
ai_rating: X 443
```

Command: `python3 scripts/build_topic_index.py`

Result:

```text
generated topics/eob/generated-index.md rows=443
```

Command: `python3 scripts/check_links.py`

Result:

```text
checked urls: 1925
RESULT: OK
```

### Known Issues

- Many seed entries are marked `needs verification` or `not yet human-checked`.
- Several BHPT/QNM/PM/LISA classic references still need exact bibliographic metadata.
- Codebase URLs are seed entries and need local installation/API checks.
- EOB CSV has empty `abstract` and `updated` fields because the pre-existing source CSV did not retain abstracts or update dates.
- No local Jekyll/GitHub Pages build was attempted in this repository; website entry already exists in the separate `recruitL.github.io` repository from prior work.

### TODO

- Add human-checked notes for the EOB seed papers.
- Verify pySEOBNR installation and locate Hamiltonian entry points.
- Add exact PM/EFT, QNM and BHPT references.
- Add reproducibility logs for `E_b(j)` and `Omega(j)` extraction.
- Decide whether future arXiv refreshes should be stored as dated snapshots under `data/papers/archive/`.
