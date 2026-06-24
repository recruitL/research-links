# Skill: Research Direction Analysis

## Purpose

Analyze a new research direction and integrate it into the repository as a structured topic.

Use this skill when the user asks for a direction such as EOB, GSF, BHPT, QNM, PM/EFT, LISA waveform modeling, numerical relativity, spectral/pseudospectral methods, EMRI waveform modeling, or Teukolsky/Sasaki-Nakamura formalism.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Required Outputs

For topic `<topic>`, create or update:

```text
topics/<topic>/README.md
topics/<topic>/timeline.md
topics/<topic>/problem-map.md
topics/<topic>/method-map.md
topics/<topic>/literature.md
topics/<topic>/codebases.md
topics/<topic>/ai-review.md
topics/<topic>/open-questions.md
topics/<topic>/notes/
```

Create or update:

```text
data/papers/<topic>_candidates.csv
data/papers/<topic>_selected.csv
data/papers/<topic>_timeline.csv
data/papers/<topic>_categories.csv
data/codebases/<topic>_codebases.csv
roadmaps/<topic>-roadmap.md
```

## Workflow

1. Normalize topic name.
2. Define the core research question.
3. Identify major technical branches.
4. Search for seed review papers and foundational papers.
5. Harvest candidate literature.
6. Save complete candidate data to CSV.
7. Select central papers into selected CSV.
8. Build timeline CSV.
9. Build category CSV.
10. Write topic README.
11. Write problem map.
12. Write method map.
13. Write literature page.
14. Write codebase page.
15. Write AI review page.
16. Write open questions.
17. Write or update roadmap.
18. Run integrity checks.
19. Update `docs/update-log.md`.
20. Commit if requested or if the task explicitly requires a commit.

## Required Sections for Topic README

```text
# <Topic Name>
## Core Question
## Why This Direction Matters
## Historical Development
## Main Technical Branches
## Key Papers
## Important Codebases
## Relation to My Work
## Data Layer
## Roadmaps
## Open Questions
```

## Required Technical Classification

Each paper should be assigned one or more technical tags, for example:

```text
foundation
hamiltonian
radiation-reaction
waveform
resummation
flux
nr-calibration
self-force
gauge-invariant
teukolsky
sasaki-nakamura
qnm
spectral-method
pseudospectral-method
pm
eft
lisa-response
surrogate
rom
data-analysis
```

## Human Check

All topic pages must distinguish between:

- verified information;
- AI-generated preliminary evaluation;
- needs verification;
- human-checked content.
