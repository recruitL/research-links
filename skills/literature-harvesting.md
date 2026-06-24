# Skill: Literature Harvesting

## Purpose

Collect literature for a research direction and preserve it as structured data.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Sources

Use reliable sources when available:

- arXiv API;
- arXiv search page;
- INSPIRE;
- NASA ADS;
- journal pages;
- review papers;
- references from central papers;
- official collaboration papers;
- codebase documentation references.

## Required CSV Output

For topic `<topic>`:

```text
data/papers/<topic>_candidates.csv
```

Required columns:

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

## Candidate Dataset Rules

- Preserve all candidate records.
- Do not delete old candidate datasets.
- If re-harvesting, either append, deduplicate, or version the dataset.
- Do not silently overwrite.
- Deduplicate by `arxiv_id` when possible.
- If `arxiv_id` is unavailable, deduplicate by normalized title.
- Keep abstracts in CSV if available.
- Do not put full candidate datasets into README.

## Query Strategy

Start with broad queries, then refine.

For EOB:

```text
effective one body gravitational waves
EOB waveform
SEOBNR
TEOBResumS
factorized resummed waveform
EOB self force
EOB PM scattering
```

For GSF:

```text
gravitational self force
MiSaTaQuWa
Detweiler Whiting
mode-sum regularization
second order self force
self force EOB
EMRI waveform self force
```

For QNM:

```text
black hole quasinormal modes
Leaver method
QNM pseudospectral
QNM spectral method
exceptional points black holes
quasinormal mode instability
```

## Output Status

Use:

```text
candidate
selected
needs_review
human_checked
rejected
duplicate
archived
```
