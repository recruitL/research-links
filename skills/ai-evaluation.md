# Skill: AI Evaluation

## Purpose

Use AI as a preliminary screening tool while keeping human judgment separate.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Required Principle

AI evaluation is not final academic judgment.

Every AI evaluation must include:

- what AI claims;
- why it might be useful;
- possible misunderstanding;
- required human check;
- final status.

## Evaluation Dimensions

```text
technical_centrality
reproducibility
relevance_to_my_work
mathematical_depth
code_usefulness
risk_of_misunderstanding
```

## Rating Scale

```text
A = must read / central
B = useful / relevant
C = background
D = peripheral
X = unclear / unreliable / needs human check
```

## Common AI Failure Modes

In EOB:

- confusing calibrated waveform models with first-principles models;
- ignoring distinction between conservative Hamiltonian and dissipative radiation reaction;
- overstating self-consistency;
- mixing PN, PM, GSF, and NR roles.

In GSF:

- confusing black-hole perturbation theory with self-force;
- ignoring gauge dependence;
- treating regularization as optional;
- confusing first-order and second-order self-force.

In QNM:

- confusing numerical artifacts with physical modes;
- ignoring boundary conditions;
- ignoring branch cuts and late-time tails;
- overstating exceptional point evidence.

In PM/EFT:

- confusing amplitude, potential, Hamiltonian, and scattering angle;
- ignoring gauge/canonical transformations;
- treating matching results as unique.

## Output

Update:

```text
topics/<topic>/ai-review.md
reviews/ai-evaluations/<topic>/
data/papers/<topic>_selected.csv
```

Do not mark `human_checked = yes` unless the user explicitly confirms or a human note exists.
