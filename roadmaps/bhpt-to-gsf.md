# Roadmap: BHPT to GSF

## Motivation

BHPT 是 GSF 的计算基础之一。理解 BHPT 到 GSF 的技术链条，有助于连接 Teukolsky flux、EMRI 和 EOB test-mass limits。

## Technical Chain

Black-hole background -> perturbation equations -> small object as source -> regularization -> self-force on worldline -> self-consistent evolution -> EMRI waveform.

## Key Concepts

- Regge-Wheeler equation
- Zerilli equation
- Teukolsky equation
- Sasaki-Nakamura transformation
- source terms
- regularization
- worldline backreaction

## Representative Papers

- Regge-Wheeler / Zerilli classic references: TODO: verify bibliographic entries.
- Teukolsky formalism: TODO: verify bibliographic entry.
- GSF reviews: [1805.10385](https://arxiv.org/abs/1805.10385), [2101.04592](https://arxiv.org/abs/2101.04592).

## Codebases

- Black Hole Perturbation Toolkit.
- Teukolsky/Sasaki-Nakamura tools: TODO: verify.

## Relation to My Work

BHPT treats the small object as a source of perturbation. GSF accounts for backreaction on the worldline. Test-particle approximation is insufficient for long-time phase accuracy, so EMRI waveform modeling requires self-consistent evolution.

## Open Problems

- Which BHPT flux tools can be reliably connected to EOB radiation reaction?
- What is the cleanest reproducible path for Kerr generic orbits?
- How should numerical boundary conditions be validated?

## Data Source Links

- [../data/papers/bhpt_candidates.csv](../data/papers/bhpt_candidates.csv)
- [../data/codebases/bhpt_codebases.csv](../data/codebases/bhpt_codebases.csv)
