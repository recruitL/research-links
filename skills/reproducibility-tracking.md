# Skill: Reproducibility Tracking

## Purpose

Track whether papers, formulas, and codebases have been reproduced.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Status Values

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

## Required Files

```text
reproducibility/candidates.md
reproducibility/reproduced.md
reproducibility/failed-or-blocked.md
reproducibility/logs/
```

## Rules

- Do not mark a paper as reproduced unless code or formulas have been checked.
- Do not mark code as running unless commands were executed.
- Record environment details where relevant.
- Record blockers explicitly.
- Link each reproducibility entry to paper CSV or codebase CSV.
- Prefer short logs over vague statements.

## Entry Template

```markdown
# Reproducibility Entry: <Paper or Codebase>
## Target
## Source
## Goal
## Current Status
## What Has Been Checked
## Commands Run
## Results
## Blockers
## Next Step
```
