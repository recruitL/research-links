# Skill: Paper Classification

## Purpose

Classify papers by technical role rather than only by chronology.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Classification Dimensions

Each paper should be classified by:

1. historical stage;
2. technical object;
3. approximation scheme;
4. waveform/modeling role;
5. relation to code;
6. relation to user research;
7. reproducibility status.

## Technical Role Examples

For EOB:

```text
original EOB formulation
effective Hamiltonian
PN input
PM input
radiation reaction
factorized waveform
resummed flux
NQC correction
merger-ringdown attachment
NR calibration
SEOBNR model
TEOBResumS model
GSF-informed potential
gauge-invariant comparison
spin extension
precession extension
eccentric extension
tidal extension
ROM / surrogate / speed-up
```

For GSF:

```text
MiSaTaQuWa foundation
Detweiler-Whiting decomposition
mode-sum regularization
puncture method
effective source
Lorenz gauge
radiation gauge
first-order self-force
second-order self-force
EMRI evolution
EOB potential extraction
redshift invariant
periastron advance
spin-precession invariant
```

For QNM:

```text
Leaver continued fraction
shooting method
WKB method
time-domain extraction
spectral method
pseudospectral method
matrix eigenvalue problem
exceptional point
mode instability
branch cut / tail
spurious mode diagnostics
```

## Output Files

For topic `<topic>`:

```text
data/papers/<topic>_categories.csv
topics/<topic>/literature.md
topics/<topic>/method-map.md
```

## Rule

Do not overstate classification certainty.

Use:

```text
needs verification
tentative
human checked
```

where appropriate.
