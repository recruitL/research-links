# Roadmap: PM to EOB

## Motivation

理解 PM 散射信息如何进入 EOB，是当前 PM-informed effective Hamiltonian diagnostic 的理论背景。

## Technical Chain

Two-body scattering -> PM scattering angle -> gauge-invariant dynamics -> EOB radial potential / effective Hamiltonian -> waveform model -> comparison with NR / GSF.

## Key Concepts

- scattering angle
- radial action
- PM Hamiltonian
- EOB potentials
- gauge-invariant comparison
- conservative versus dissipative dynamics

## Representative Papers

- TODO: verify PM/EFT core papers before citing.
- EOB foundation: [gr-qc/9811091](https://arxiv.org/abs/gr-qc/9811091)
- Modern EOB target: [2303.18039](https://arxiv.org/abs/2303.18039)

## Codebases

- pySEOBNR for diagnostic experiments.
- LALSuite for waveform benchmark.
- Custom scripts for `E_b(j)`, `Omega(j)` and scattering diagnostics.

## Relation to My Work

当前工作可视为 PM-informed effective Hamiltonian diagnostic。必须明确：

- 只替换 Hamiltonian 不是完整自洽 EOB model；
- 后续必须处理 radiation reaction、flux、waveform modes 和 calibration；
- gauge-invariant diagnostics 是避免坐标误读的核心。

## Open Problems

- PM Hamiltonian 和 SEOBNR calibrated Hamiltonian 的差异如何解释？
- 是否能找到不依赖 waveform calibration 的 clean diagnostics？
- 如何把 PM conservative input 与 dissipative flux 自洽结合？

## Data Source Links

- [../data/papers/pm_eft_candidates.csv](../data/papers/pm_eft_candidates.csv)
- [../data/papers/eob_candidates.csv](../data/papers/eob_candidates.csv)
