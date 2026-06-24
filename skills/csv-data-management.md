# Skill: CSV Data Management

## Purpose

Maintain CSV files as the structured data layer of the repository.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Rules

1. CSV files are persistent data assets.
2. Do not delete candidate CSV files.
3. Do not replace complete datasets with curated subsets.
4. Use selected CSV files for curated entries.
5. Use timeline CSV files for historical milestones.
6. Use categories CSV files for technical classification.
7. Use scripts for validation and summaries.
8. Preserve old data when re-harvesting.
9. Deduplicate explicitly.
10. Record changes in `docs/update-log.md`.

## Required Paper CSV Columns

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

## Required Codebase CSV Columns

```text
name,
url,
repository,
documentation,
language,
license,
maintainer,
status,
main_purpose,
installation_difficulty,
theory_transparency,
modifiable,
inputs,
outputs,
relation_to_my_work,
ai_rating,
human_checked,
notes
```

## Validation

Run:

```text
python scripts/check_csv_integrity.py || python3 scripts/check_csv_integrity.py
python scripts/check_links.py || python3 scripts/check_links.py
```
