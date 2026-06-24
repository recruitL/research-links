# GSF（Gravitational Self-Force）

## Core Question

GSF 研究小质量物体在弯曲时空中的自力和辐射反作用，目标是超越 test-particle approximation，得到长期相位精确的 EMRI/IMRI 动力学和波形。

## Why GSF Matters

GSF 是连接 BHPT、EMRI、LISA waveform、EOB potentials 和高精度两体动力学的重要桥梁。它提供小质量比强场区域的规范不变量和动力学修正，可用于校验或约束 EOB/PN/PM 模型。

## Historical Development

- 1996-1997：MiSaTaQuWa 和 Quinn-Wald 给出自力方程基础。
- 2000s：mode-sum regularization、Detweiler-Whiting 分解、puncture/effective source 方法发展。
- 2010s：规范不变量、EOB potentials、review consolidation。
- 2020s：二阶 GSF、post-adiabatic expansion、EMRI waveform generation 和 LISA 需求。

## Main Technical Branches

- point-particle motion in curved spacetime；
- singular/regular field decomposition；
- mode-sum regularization；
- puncture/effective source；
- gauge problem；
- first-order and second-order GSF；
- EMRI self-consistent evolution；
- connection to EOB potentials and fluxes。

## Key Papers

- [gr-qc/9606018](https://arxiv.org/abs/gr-qc/9606018) - MiSaTaQuWa。
- [gr-qc/9610053](https://arxiv.org/abs/gr-qc/9610053) - Quinn-Wald。
- [1102.0529](https://arxiv.org/abs/1102.0529) - Poisson-Pound-Vega review。
- [1805.10385](https://arxiv.org/abs/1805.10385) - Barack-Pound review。
- [2101.04592](https://arxiv.org/abs/2101.04592) - Pound-Wardell BHPT/GSF review。

## Data Layer

- [../../data/papers/gsf_candidates.csv](../../data/papers/gsf_candidates.csv)
- [../../data/codebases/gsf_codebases.csv](../../data/codebases/gsf_codebases.csv)

## Relation to My Work

GSF 可作为未来 EOB potentials、flux 和 EMRI/test-mass 极限的一致性检查来源。当前阶段先建立技术谱系：BHPT -> regularized self-force -> gauge invariants -> EOB constraints -> LISA/EMRI waveform。

## Open Questions

- 二阶 GSF 如何进入 waveform generation？
- 哪些 GSF invariants 最适合约束 EOB potentials？
- GSF-informed flux 与 EOB radiation reaction 如何匹配？
- Kerr generic orbit 的自洽演化如何与 Teukolsky/Sasaki-Nakamura 工具连接？
