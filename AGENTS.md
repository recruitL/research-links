# AGENTS.md

## Repository Role

This repository is a long-term research knowledge base, not a simple link dump.
It organizes research directions, literature, codebases, technical roadmaps, AI-assisted evaluations, human checks, and reproducibility status.
The repository must preserve structured data and separate it from interpretive Markdown pages.

## Core Principle

CSV / YAML / JSON files are the data layer.
Markdown files are the interpretation and presentation layer.

Never replace structured data with Markdown summaries.
Never delete complete candidate datasets after generating curated pages.
Never fabricate paper metadata, codebase capabilities, arXiv IDs, or human-check status.

## Language Policy

- Human-facing research analysis should be written primarily in Chinese.
- Agent-facing workflow documents should be written in English.
- CSV column names should remain in English for machine processing.
- CSV natural-language content may use Chinese, especially `technical_role`, `relevance`, `notes`, human-check notes, and AI-evaluation notes.
- Technical terms may keep their standard English forms with Chinese explanations.
- Do not translate established technical abbreviations such as EOB, GSF, BHPT, QNM, NR, PN, PM, EFT, EMRI, LISA.

## Main Workflow

When the user gives a research direction, the agent should perform this workflow:

1. Identify the research direction and canonical topic name.
2. Create or update the corresponding topic directory under `topics/`.
3. Harvest literature from reliable sources such as arXiv, INSPIRE, NASA ADS, journal pages, known review papers, or official collaboration pages.
4. Save complete candidate records into CSV under `data/papers/`.
5. Create selected, timeline, and category CSV files.
6. Classify papers by technical role.
7. Identify relevant codebases and save them under `data/codebases/`.
8. Build or update topic Markdown pages.
9. Build or update roadmaps.
10. Add AI evaluation only as preliminary analysis.
11. Add human-check placeholders.
12. Update reproducibility tracking.
13. Run integrity checks.
14. Record changes in `docs/update-log.md`.
15. Commit the result when requested or when the task explicitly includes commit.

## Data Layer Rules

All literature datasets must be stored under `data/papers/`.

For each topic, use these files when applicable:

```text
<topic>_candidates.csv
<topic>_selected.csv
<topic>_timeline.csv
<topic>_categories.csv
```

All codebase datasets must be stored under `data/codebases/`.

Use:

```text
<topic>_codebases.csv
```

Required paper CSV columns:

```text
arxiv_id,
title,
authors,
year,
published,
updated,
primary_category,
categories,
abstract,
url,
pdf_url,
topic,
technical_tags,
technical_role,
relevance,
status,
ai_rating,
human_checked,
notes
```

If a value is unknown, leave it blank or write `needs verification`.
Do not fabricate arXiv IDs, publication information, authors, or claims.

## Markdown Layer Rules

Markdown topic pages should not contain full raw datasets.

They should contain:

- curated summaries;
- technical maps;
- representative papers;
- links to CSV data;
- links to roadmaps;
- links to codebase notes;
- AI evaluation status;
- human-check status.

Each topic should usually contain:

```text
topics/<topic>/
├── README.md
├── timeline.md
├── problem-map.md
├── method-map.md
├── literature.md
├── codebases.md
├── ai-review.md
├── open-questions.md
└── notes/
```

## AI Evaluation Policy

AI evaluation is preliminary screening only.
It must not be presented as final academic judgment.
Every AI evaluation must include a human-check field.

Use the rating scale:

```text
A = must read / central
B = useful / relevant
C = background
D = peripheral
X = unclear / unreliable / needs human check
```

The agent must explicitly flag possible AI misunderstandings, especially in EOB, GSF, BHPT, QNM, Teukolsky formalism, PM/EFT, LISA waveform modeling, and numerical relativity.

Common risks:

- confusing related work with equivalent work;
- treating a heuristic argument as a derivation;
- missing gauge dependence;
- confusing PN, PM, GSF, and NR inputs;
- treating calibrated waveform models as first-principles models;
- overstating code reproducibility;
- ignoring approximation regimes.

## Research Direction Analysis Workflow

When analyzing a new direction, follow `skills/research-direction-analysis.md`.

The output must include:

- topic directory;
- candidate CSV;
- selected CSV;
- timeline CSV;
- category CSV;
- topic README;
- literature page;
- codebase page;
- roadmap;
- AI review page;
- open questions;
- update log entry.

## Codebase Analysis Workflow

When collecting codebases, follow `skills/codebase-analysis.md`.

For each codebase, record:

- name;
- URL;
- language;
- license if available;
- maintainer or organization if available;
- main purpose;
- installation difficulty;
- theory transparency;
- modifiability;
- relation to user research;
- AI evaluation;
- human check;
- notes.

## Reproducibility Rules

Use `reproducibility/` to track whether a paper or codebase has been reproduced.

Status options:

```text
not_started
reading
formula_checked
code_found
code_runs
partially_reproduced
fully_reproduced
failed
blocked
archived
```

Do not mark an item as reproduced unless there is concrete evidence.

## Commit Rules

Before committing, run:

```text
find . -maxdepth 4 -type f | sort
python scripts/check_csv_integrity.py || python3 scripts/check_csv_integrity.py
python scripts/summarize_eob_csv.py || python3 scripts/summarize_eob_csv.py
python scripts/build_topic_index.py || python3 scripts/build_topic_index.py
python scripts/check_links.py || python3 scripts/check_links.py
```

If a script is topic-specific and not applicable, explain why in `docs/update-log.md`.

Use specific commit messages, for example:

- `Add GSF research direction knowledge base`
- `Update EOB literature categories`
- `Add QNM methods roadmap`

## Forbidden Actions

Do not:

1. Delete complete CSV candidate datasets.
2. Replace CSV data with Markdown summaries.
3. Fabricate paper metadata.
4. Fabricate codebase capabilities.
5. Present AI evaluation as final human judgment.
6. Mark papers as human-checked without actual human confirmation.
7. Mark papers as reproduced without running or verifying code/formulas.
8. Put hundreds of raw candidate entries into README.
9. Break existing topic links.
10. Ignore `docs/update-log.md`.
