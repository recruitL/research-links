# Update Log

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
