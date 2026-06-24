# Skill: Codebase Analysis

## Purpose

Collect and evaluate research codebases relevant to a topic.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Required CSV

For topic `<topic>`:

```text
data/codebases/<topic>_codebases.csv
```

Required columns:

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

## Evaluation Questions

For each codebase:

1. What problem does it solve?
2. Is it actively maintained?
3. What language is it written in?
4. Is installation simple?
5. Are examples provided?
6. Is the underlying theory transparent?
7. Can it be modified for research?
8. Does it expose low-level quantities?
9. Does it support batch computation?
10. Is it useful for current or future projects?

## Markdown Output

Update:

```text
topics/<topic>/codebases.md
reviews/codebases/<topic>/
```

## Rating

Use:

```text
A = central and useful
B = useful but limited
C = background or reference only
D = peripheral
X = unclear or not checked
```

## Warning

Do not claim a codebase supports a feature unless verified by documentation, examples, or source inspection.
