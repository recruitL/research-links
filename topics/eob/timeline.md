# EOB 时间线

本页按技术发展阶段组织 EOB，从原始形式主义到现代 waveform model。

## 1998-2000: Original EOB Formulation

- 核心问题：把 GR 两体问题映射为 effective one-body dynamics。
- 代表文献：[gr-qc/9811091](https://arxiv.org/abs/gr-qc/9811091)、[gr-qc/0001013](https://arxiv.org/abs/gr-qc/0001013)、[gr-qc/0005034](https://arxiv.org/abs/gr-qc/0005034)。
- 技术关键词：effective Hamiltonian、EOB potentials、last stable orbit、inspiral-plunge。

## 2000s: Inspiral-Plunge-Merger-Ringdown Modeling

- EOB 被用于连接 inspiral、plunge、merger 和 ringdown。
- 代表文献：[gr-qc/0211041](https://arxiv.org/abs/gr-qc/0211041)、[gr-qc/0508067](https://arxiv.org/abs/gr-qc/0508067)。
- 关注点：从 PN inspiral 到 merger-ringdown 的统一模板。

## 2007-2012: Factorized and Resummed Waveform

- 发展 factorized waveform、`rho_lm` resummation、多极波形和 radiation reaction 表示。
- 代表文献：[0803.3162](https://arxiv.org/abs/0803.3162)、[0811.2069](https://arxiv.org/abs/0811.2069)、[1012.2456](https://arxiv.org/abs/1012.2456)。

## 2008-2015: NR Calibration and EOBNR/SEOBNR

- EOB 波形开始系统地与 NR 波形比较和校准。
- 代表文献：[0711.2628](https://arxiv.org/abs/0711.2628)、[0902.0790](https://arxiv.org/abs/0902.0790)、[1212.4357](https://arxiv.org/abs/1212.4357)、[1406.6913](https://arxiv.org/abs/1406.6913)。

## 2010s: Spin, Precession, Tides, Eccentricity

- 拓展到自旋、进动、潮汐、BNS/NSBH 和偏心轨道。
- 代表文献：[0911.5041](https://arxiv.org/abs/0911.5041)、[1202.0790](https://arxiv.org/abs/1202.0790)、[1307.6232](https://arxiv.org/abs/1307.6232)、[2112.06952](https://arxiv.org/abs/2112.06952)。

## 2010s-2020s: GSF-informed EOB Potentials and Gauge-Invariant Comparisons

- 通过 GSF 的 redshift、periastron advance、spin-precession invariant 和 ISCO/light-ring 信息约束 EOB potentials。
- 代表文献：[1008.0935](https://arxiv.org/abs/1008.0935)、[1008.4622](https://arxiv.org/abs/1008.4622)、[1209.0964](https://arxiv.org/abs/1209.0964)、[2303.18026](https://arxiv.org/abs/2303.18026)。

## 2020s: SEOBNRv5, TEOBResumS-Dali, Surrogate/ROM Acceleration

- 现代 EOB 模型强调速度、精度、可用于参数估计，以及 generic-orbit 扩展。
- 代表文献：[2303.18039](https://arxiv.org/abs/2303.18039)、[2503.14580](https://arxiv.org/abs/2503.14580)、[2604.14270](https://arxiv.org/abs/2604.14270)、[2606.02690](https://arxiv.org/abs/2606.02690)。

## 2020s: PM Scattering Input and Modern EOB Hamiltonians

- PM scattering angle 和高阶 two-body dynamics 为 EOB Hamiltonian 提供新的 gauge-invariant input。
- 对当前工作的意义：PM-informed effective Hamiltonian 可以作为诊断项进入 pySEOBNR/SEOBNRv5HM，但不能被描述为完整自洽 waveform model，除非 radiation reaction、flux、waveform 和 calibration 也相应处理。

## 数据入口

- [../../data/papers/eob_timeline.csv](../../data/papers/eob_timeline.csv)
- [../../data/papers/eob_candidates.csv](../../data/papers/eob_candidates.csv)
