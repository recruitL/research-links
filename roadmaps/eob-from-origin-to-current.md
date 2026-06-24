# Roadmap: EOB from Origin to Current

## Motivation

梳理 EOB 从 1998 年原始形式主义到现代 SEOBNR/TEOBResumS waveform model 的技术演化，帮助判断当前 Hamiltonian diagnostic 应放在技术链条的哪个位置。

## Technical Chain

PN two-body dynamics -> EOB mapping -> effective Hamiltonian -> radiation reaction -> inspiral-plunge-merger-ringdown waveform -> resummation -> NR calibration -> SEOBNR / TEOBResumS -> modern PM/GSF-informed extensions.

## Key Concepts

- effective Hamiltonian
- EOB potentials
- factorized waveform
- NQC correction
- NR calibration
- GSF-informed potentials
- PM scattering input

## Representative Papers

- [gr-qc/9811091](https://arxiv.org/abs/gr-qc/9811091)
- [gr-qc/0001013](https://arxiv.org/abs/gr-qc/0001013)
- [0811.2069](https://arxiv.org/abs/0811.2069)
- [0902.0790](https://arxiv.org/abs/0902.0790)
- [1611.03703](https://arxiv.org/abs/1611.03703)
- [2303.18039](https://arxiv.org/abs/2303.18039)

## Codebases

- pySEOBNR
- LALSuite / LALSimulation
- TEOBResumS
- Black Hole Perturbation Toolkit

## Relation to My Work

当前工作主要对应 effective Hamiltonian diagnostics。不能把局部 Hamiltonian 替换写成完整自洽 EOB model；后续必须处理 radiation reaction、flux、waveform、NQC 和 calibration。

## Open Problems

- PM/GSF information 如何与 calibration 同时共存？
- 哪些 gauge-invariant diagnostics 最适合比较 modified Hamiltonian？
- 如何从 Hamiltonian diagnostic 走向 self-consistent waveform update？

## Data Source Links

- [../data/papers/eob_candidates.csv](../data/papers/eob_candidates.csv)
- [../data/papers/eob_timeline.csv](../data/papers/eob_timeline.csv)
- [../data/codebases/eob_codebases.csv](../data/codebases/eob_codebases.csv)
