# EOB（Effective One Body）

## Core Question

EOB 试图回答：如何把广义相对论两体问题重写成一个有效一体问题，并把 PN、PM、GSF、BHPT 和 NR 信息组合成可用于紧致双星 IMR 波形建模的动力学框架？

## Why EOB Matters

EOB 是连接解析相对论两体动力学和引力波数据分析的核心框架之一。它把保守动力学、辐射反作用、波形重求和、NR 校准和 merger-ringdown attachment 组织进一个可计算模型族，并形成 EOBNR、SEOBNR、TEOBResumS 等重要 waveform families。

## Historical Development

简略路线：

1. 1998-2000：Buonanno-Damour 提出 EOB 映射，并用于 inspiral-plunge。
2. 2000s：EOB waveform、反冲、test-mass 极限和早期 NR 比较。
3. 2007-2012：factorized/resummed waveform、NR 校准、GSF 规范不变量比较。
4. 2010s：SEOBNR、TEOBResumS、自旋、潮汐、偏心和 BNS 扩展。
5. 2020s：SEOBNRv5、TEOBResumS-Dali、GSF/PM input、generic orbit 和 surrogate/ROM 加速。

详细时间线见 [timeline.md](timeline.md)。

## Main Technical Branches

- 有效 Hamiltonian 与 EOB potentials。
- PN/PM/GSF 信息注入。
- radiation reaction 与 flux。
- factorized/resummed multipolar waveform。
- NQC correction 和 merger-ringdown attachment。
- NR calibration。
- gauge-invariant diagnostics，例如 `E_b(j)`、`Omega(j)`、scattering angle、redshift、periastron advance。
- spin/precession、tides/BNS/NSBH、eccentric/scattering、EMRI/test-mass 扩展。

技术对象图见 [method-map.md](method-map.md)，问题图见 [problem-map.md](problem-map.md)。

## Key Papers

精选文献见 [literature.md](literature.md)。完整候选数据保存在：

- [../../data/papers/eob_candidates.csv](../../data/papers/eob_candidates.csv)
- [../../data/papers/eob_selected.csv](../../data/papers/eob_selected.csv)
- [../../data/papers/eob_timeline.csv](../../data/papers/eob_timeline.csv)
- [../../data/papers/eob_categories.csv](../../data/papers/eob_categories.csv)

完整 EOB 候选数据保存在 `data/papers/eob_candidates.csv`。topic 页面只是人工整理后的研究入口，不能替代 CSV 数据层。

## Important Codebases

代码库入口见 [codebases.md](codebases.md) 和 [../../data/codebases/eob_codebases.csv](../../data/codebases/eob_codebases.csv)。

重点关注：

- pySEOBNR / SEOBNRv5HM；
- LALSuite / LALSimulation；
- TEOBResumS / TEOBResumS-Dali；
- Black Hole Perturbation Toolkit；
- NR waveform catalogs；
- gauge-invariant diagnostics extraction scripts。

## Relation to My Work

当前工作可以定位为 PM-informed effective Hamiltonian diagnostic，而不是完整自洽 EOB waveform model。

需要明确区分：

- 可以尝试在 pySEOBNR / SEOBNRv5HM 中替换或诊断 effective Hamiltonian；
- 这类替换只测试保守动力学的一部分，不能自动说明完整 waveform model 自洽；
- radiation reaction、flux、factorized waveform、NQC correction、merger-ringdown attachment 和 calibration 尚未自洽替换；
- 应通过 `E_b(j)`、`Omega(j)`、scattering angle 等 gauge-invariant quantities 与 NR 或其他模型比较；
- 后续可连接 GSF-informed EOB potentials，尤其是一阶/二阶 GSF 对 EOB potentials 和 flux 的约束；
- 未来也可探索 Teukolsky / Sasaki-Nakamura fluxes 与 EOB radiation reaction 的连接。

## Open Questions

开放问题见 [open-questions.md](open-questions.md)。核心问题包括：

- PM Hamiltonian 信息如何在不破坏 waveform calibration 的情况下进入 SEOBNR？
- 只替换 Hamiltonian 的诊断实验能说明什么，不能说明什么？
- GSF-informed flux 和 PM-informed Hamiltonian 如何同时进入 EOB？
- 如何用 gauge-invariant diagnostics 避免坐标规范误读？

## Roadmaps

- [../../roadmaps/eob-from-origin-to-current.md](../../roadmaps/eob-from-origin-to-current.md)
- [../../roadmaps/pm-to-eob.md](../../roadmaps/pm-to-eob.md)
- [../../roadmaps/eob-teukolsky-connection.md](../../roadmaps/eob-teukolsky-connection.md)
