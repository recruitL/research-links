# Roadmap: LISA Waveform Modeling

## Motivation

LISA waveform modeling requires long-time phase accuracy, especially for EMRIs and other systems where GSF/BHPT/EOB connections become important.

## Technical Chain

Source class -> orbital dynamics -> flux/self-force -> waveform generation -> detector response -> parameter estimation -> systematic error diagnostics.

## Key Concepts

- EMRI
- phase accuracy
- self-consistent evolution
- response modeling
- parameter estimation
- waveform systematics

## Representative Papers

- TODO: add verified LISA waveform and EMRI data-analysis references.
- GSF review seeds: [1805.10385](https://arxiv.org/abs/1805.10385), [2101.04592](https://arxiv.org/abs/2101.04592).

## Codebases

- Black Hole Perturbation Toolkit.
- TODO: add LISA-specific waveform/data-analysis codebases after verification.

## Relation to My Work

LISA is a long-term motivation for connecting GSF, BHPT, EOB-Teukolsky and waveform systematics. It is not the immediate validation target for Hamiltonian-only pySEOBNR diagnostics.

## Open Problems

- Which waveform errors dominate LISA EMRI parameter estimation?
- How much GSF order is required for target phase accuracy?
- Which codebases are mature enough for local reproduction?

## Data Source Links

- [../data/papers/lisa_candidates.csv](../data/papers/lisa_candidates.csv)
