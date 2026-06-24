# Roadmap: GSF from MiSaTaQuWa to Second Order

## Motivation

GSF 提供小质量比强场动力学的系统修正，是 EMRI/LISA waveform 和 GSF-informed EOB 的基础。

## Technical Chain

MiSaTaQuWa -> Quinn-Wald -> Detweiler-Whiting decomposition -> mode-sum regularization -> puncture / effective source -> gauge issues -> first-order GSF -> second-order GSF -> EOB potentials -> EMRI/LISA waveform.

## Key Concepts

- MiSaTaQuWa equation
- Detweiler-Whiting decomposition
- mode-sum regularization
- puncture/effective source
- gauge invariance
- first-order GSF
- second-order GSF
- redshift and periastron advance invariants

## Representative Papers

- [gr-qc/9606018](https://arxiv.org/abs/gr-qc/9606018)
- [gr-qc/9610053](https://arxiv.org/abs/gr-qc/9610053)
- [1102.0529](https://arxiv.org/abs/1102.0529)
- [1805.10385](https://arxiv.org/abs/1805.10385)
- [2101.04592](https://arxiv.org/abs/2101.04592)

## Codebases

- Black Hole Perturbation Toolkit.
- TODO: add mode-sum and puncture/effective-source codebases after verification.

## Relation to My Work

GSF is relevant to future EOB potentials, flux corrections and EMRI/test-mass limits. It should not be treated as automatically equivalent to comparable-mass dynamics.

## Open Problems

- Which second-order GSF results are ready for waveform use?
- How to combine GSF-informed flux with PM-informed Hamiltonian?
- What are robust invariants for EOB comparison?

## Data Source Links

- [../data/papers/gsf_candidates.csv](../data/papers/gsf_candidates.csv)
- [../data/codebases/gsf_codebases.csv](../data/codebases/gsf_codebases.csv)
