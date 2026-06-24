# EOB（Effective One Body）

EOB 方向的目标是把广义相对论两体问题映射为一个有效一体问题，并用于紧致双星的保守动力学、辐射反作用和并合前-并合-铃降（IMR）波形建模。

本页先按时间线梳理主干，再按技术主题组织文献。完整候选表见 [`data/eob_arxiv_candidates.csv`](../data/eob_arxiv_candidates.csv)。

## 抓取状态

- 最近抓取日期：2026-06-24
- 来源：arXiv API / arXiv 条目页
- 检索词：`effective one body`、`effective-one-body`、`EOBNR`、`SEOBNR`、`TEOBResumS`、`EOB waveform`、`EOB model`、`EOB Hamiltonian`，并手动补入少数核心条目。
- 当前候选表：经过 GR/紧致双星方向过滤后，共 443 条 arXiv 记录。
- 注意：这是工作型参考文献库，不是最终综述。部分条目是下游应用、比较或数据分析论文，并非 EOB 形式主义本身的核心论文。

## 阅读路径

1. 基础框架：先读 Buonanno-Damour 和 Damour-Jaranowski-Schafer 相关论文，理解 EOB 映射、有效 Hamiltonian、light ring/plunge 语言，以及它和 PN 动力学的关系。
2. 波形构造：再读早期重求和、因子化、多极波形论文，尤其是 factorized waveform 和 `rho_lm` 重求和，再进入 NR 校准论文。
3. NR 校准模型族：沿着 EOBNR 到 SEOBNR、TEOBResumS、SEOBNRv5 和 generic-orbit EOB 的路线阅读。
4. 跨方法约束：重点看 GSF 和规范不变量比较，包括 redshift、periastron advance、ISCO shift、EOB potentials，以及后来的 2GSF-informed 模型。
5. 专门方向：按需要进入 spin/precession、潮汐/BNS/NSBH、偏心/散射/任意轨道、EMRI/test-mass 和数据分析加速方向。

## 时间线

| 时段 | 主线 | 代表文献 |
| --- | --- | --- |
| 1998-2001 | EOB 映射、inspiral-plunge 和早期自旋扩展 | [9811091](https://arxiv.org/abs/gr-qc/9811091), [0001013](https://arxiv.org/abs/gr-qc/0001013), [0005034](https://arxiv.org/abs/gr-qc/0005034), [0103018](https://arxiv.org/abs/gr-qc/0103018) |
| 2002-2006 | 3PN EOB 模板、反冲、test-mass / extreme-mass-ratio 检验 | [0211041](https://arxiv.org/abs/gr-qc/0211041), [0508067](https://arxiv.org/abs/gr-qc/0508067), [0602117](https://arxiv.org/abs/gr-qc/0602117), [0612096](https://arxiv.org/abs/gr-qc/0612096) |
| 2007-2009 | 与 NR 的早期系统比较，以及因子化/重求和波形 | [0706.3732](https://arxiv.org/abs/0706.3732), [0711.2628](https://arxiv.org/abs/0711.2628), [0803.3162](https://arxiv.org/abs/0803.3162), [0811.2069](https://arxiv.org/abs/0811.2069), [0902.0790](https://arxiv.org/abs/0902.0790) |
| 2009-2012 | 潮汐、EMRI、GSF/规范不变量比较、多极 IMR 波形 | [0911.5041](https://arxiv.org/abs/0911.5041), [1008.0935](https://arxiv.org/abs/1008.0935), [1008.4622](https://arxiv.org/abs/1008.4622), [1106.1021](https://arxiv.org/abs/1106.1021), [1209.0964](https://arxiv.org/abs/1209.0964), [1212.4357](https://arxiv.org/abs/1212.4357) |
| 2013-2016 | 任意质量比/自旋、改进非进动模型、高 PN/GSF 输入 | [1311.2544](https://arxiv.org/abs/1311.2544), [1312.2503](https://arxiv.org/abs/1312.2503), [1406.6913](https://arxiv.org/abs/1406.6913), [1409.6933](https://arxiv.org/abs/1409.6933), [1611.03703](https://arxiv.org/abs/1611.03703) |
| 2017-2021 | 探测时代模型、TEOBResumS、降阶/替代模型、偏心扩展 | [1806.01772](https://arxiv.org/abs/1806.01772), [2112.06952](https://arxiv.org/abs/2112.06952) |
| 2022-2026 | SEOBNRv5、2GSF-informed flux、任意轨道 EOB、PM/GSF/NR 融合 | [2207.14002](https://arxiv.org/abs/2207.14002), [2303.18026](https://arxiv.org/abs/2303.18026), [2303.18039](https://arxiv.org/abs/2303.18039), [2503.14580](https://arxiv.org/abs/2503.14580), [2505.11242](https://arxiv.org/abs/2505.11242), [2606.09445](https://arxiv.org/abs/2606.09445) |

## 技术分类

### 基础框架 / Hamiltonian / PN-PM 动力学

- [gr-qc/9811091](https://arxiv.org/abs/gr-qc/9811091) - Buonanno & Damour，EOB 对广义相对论两体问题的原始构造。
- [gr-qc/0001013](https://arxiv.org/abs/gr-qc/0001013) - Buonanno & Damour，将 EOB 用于黑洞双星从 inspiral 到 plunge 的过渡。
- [gr-qc/0005034](https://arxiv.org/abs/gr-qc/0005034) - Damour, Jaranowski & Schafer，在 EOB 框架中讨论 3PN 信息和 last stable orbit。
- [gr-qc/0010104](https://arxiv.org/abs/gr-qc/0010104) - Fiziev & Todorov，相关的 relativistic two-body effective-particle 处理。
- [gr-qc/0103018](https://arxiv.org/abs/gr-qc/0103018) - 早期自旋黑洞 EOB 扩展。
- [1305.4884](https://arxiv.org/abs/1305.4884) - 4PN 两体引力相互作用势。
- [2405.19181](https://arxiv.org/abs/2405.19181) - 将 PM 信息匹配进自旋 EOB 波形模型。
- [2604.09545](https://arxiv.org/abs/2604.09545) - 5PN 黑洞动力学。

### 重求和 / Flux / 因子化波形

- [0705.2519](https://arxiv.org/abs/0705.2519) - 小质量比极限下的 faithful EOB 波形。
- [0712.3003](https://arxiv.org/abs/0712.3003) - 等质量黑洞并合的 faithful EOB 波形。
- [0803.3162](https://arxiv.org/abs/0803.3162) - inspiral 和 coalescence 阶段的高精度 EOB 波形。
- [0811.2069](https://arxiv.org/abs/0811.2069) - PN 多极波形的因子化/重求和形式，以及 `rho_lm` 重求和。
- [1003.0597](https://arxiv.org/abs/1003.0597) - extreme-mass-ratio 极限下的多极分析。
- [1012.2456](https://arxiv.org/abs/1012.2456) - 对 EOB 多极波形的测试和改进。
- [1210.2834](https://arxiv.org/abs/1210.2834) - EOB 任意轨道上的 radiation reaction。
- [2602.08833](https://arxiv.org/abs/2602.08833) - 从 confluent Heun 方程出发的新型因子化/重求和波形构造。

### NR 校准 / EOBNR / SEOBNR / TEOBResumS

- [0706.3732](https://arxiv.org/abs/0706.3732) - 早期用 NR 信息改进非自旋 BBH EOB 模板。
- [0711.2628](https://arxiv.org/abs/0711.2628) - EOB 波形与高精度 NR 数据的比较。
- [0902.0790](https://arxiv.org/abs/0902.0790) - 等质量非自旋 EOB 波形对 NR 的校准。
- [0912.3466](https://arxiv.org/abs/0912.3466) - 等质量自旋 EOB 波形对 NR 的校准。
- [1106.1021](https://arxiv.org/abs/1106.1021) - 非自旋黑洞双星的多极 IMR EOB 波形。
- [1212.4357](https://arxiv.org/abs/1212.4357) - 改进非自旋 EOB 描述及其 NR completion。
- [1311.2544](https://arxiv.org/abs/1311.2544) - 覆盖任意质量比和自旋的 EOB 模型。
- [1406.6913](https://arxiv.org/abs/1406.6913) - 非进动自旋 BBH 的新 EOB 描述。
- [1611.03703](https://arxiv.org/abs/1611.03703) - SEOBNRv4 时代的非进动自旋 BBH 模型，使用大量 NR 波形校准。
- [1806.01772](https://arxiv.org/abs/1806.01772) - TEOBResumS 时域模型，包含非进动自旋、潮汐和 self-spin 效应。
- [2303.18039](https://arxiv.org/abs/2303.18039) - SEOBNRv5HM 的基础论文，面向准圆、非进动 BBH。
- [2503.14580](https://arxiv.org/abs/2503.14580) - TEOBResumS-Dali，面向任意轨道的 generic compact binary EOB 模型。

### GSF / 规范不变量比较 / EOB 势函数

- [0902.0573](https://arxiv.org/abs/0902.0573) - Schwarzschild ISCO 的 GSF 修正，是 EOB 比较的重要基准。
- [1008.0935](https://arxiv.org/abs/1008.0935) - GSF precession invariant 对 EOB 函数的约束。
- [1008.4622](https://arxiv.org/abs/1008.4622) - ISCO self-force shift 与 PN/EOB 方法的比较。
- [1106.3278](https://arxiv.org/abs/1106.3278) - 黑洞双星 periastron advance，连接 NR、GSF 和 EOB 比较。
- [1111.5610](https://arxiv.org/abs/1111.5610) - 质量比一阶的完整非自旋 EOB metric。
- [1209.0964](https://arxiv.org/abs/1209.0964) - ISCO 到 light ring 之间的 GSF 信息，以及 EOB `A(u)` 势。
- [1312.2503](https://arxiv.org/abs/1312.2503) - 由解析 GSF 计算得到的高阶 PN 两体势贡献。
- [1409.6933](https://arxiv.org/abs/1409.6933) - GSF 对两体潮汐相互作用和 EOB 的修正。
- [2303.18026](https://arxiv.org/abs/2303.18026) - 用二阶 GSF flux 改进 SEOBNRv5。
- [2505.11242](https://arxiv.org/abs/2505.11242) - SEOBNR-GSF，将 GSF-informed Hamiltonian 放入 IMR EOB 模型。

### 自旋 / 进动

- [0103018](https://arxiv.org/abs/gr-qc/0103018) - 早期自旋 BBH EOB。
- [0803.0915](https://arxiv.org/abs/0803.0915) - EOB 动力学中的 NLO spin-orbit coupling。
- [0912.3517](https://arxiv.org/abs/0912.3517) - 改进的自旋 EOB Hamiltonian。
- [1106.4349](https://arxiv.org/abs/1106.4349) 和 [1107.2904](https://arxiv.org/abs/1107.2904) - EOB Hamiltonian 中的 NNLO spin-orbit coupling。
- [1202.0790](https://arxiv.org/abs/1202.0790) - 非进动自旋 IMR EOB 原型模型。
- [1307.6232](https://arxiv.org/abs/1307.6232) - 自旋进动 BBH 的 EOB 波形。
- [2303.18143](https://arxiv.org/abs/2303.18143) - SEOBNRv5 的解析 precessing-spin 两体动力学。

### 潮汐 / 双中子星 / NSBH

- [0911.5041](https://arxiv.org/abs/0911.5041) - inspiralling compact binaries 中潮汐效应的 EOB 描述。
- [1009.0521](https://arxiv.org/abs/1009.0521) - BNS inspiral 中潮汐效应的解析建模。
- [1103.3874](https://arxiv.org/abs/1103.3874) - BNS NR 模拟与 EOB 解析模型比较。
- [1202.3565](https://arxiv.org/abs/1202.3565) - 高阶相对论潮汐相互作用的有效作用量方法及其 EOB 描述。
- [1412.4553](https://arxiv.org/abs/1412.4553) - tidally-interacting BNS 到 merger 的动力学建模。
- [1804.02235](https://arxiv.org/abs/1804.02235) - matter imprints 与 TEOBResumS 波形比较。
- [2307.15125](https://arxiv.org/abs/2307.15125) - 用 NR 信息改进 coalescing BNS 的 TEOBResumS 模型。
- [2503.18934](https://arxiv.org/abs/2503.18934) - SEOBNRv5THM，面向快速 BNS 波形生成。

### 偏心 / 双曲轨道 / 散射 / 任意轨道

- [1210.2834](https://arxiv.org/abs/1210.2834) - EOB 任意轨道中的辐射反作用。
- [1402.7307](https://arxiv.org/abs/1402.7307) - 强场黑洞散射中数值结果与解析模型的比较。
- [2112.06952](https://arxiv.org/abs/2112.06952) - SEOBNRv4EHM，偏心、多极、非进动自旋 BBH 波形。
- [2207.14002](https://arxiv.org/abs/2207.14002) - 面向偏心 large-mass-ratio inspirals 的 GSF-informed EOB 模型。
- [2503.14580](https://arxiv.org/abs/2503.14580) - 任意紧致双星动力学，包括偏心、双曲和非平面轨道。
- [2603.19913](https://arxiv.org/abs/2603.19913) - EOB 框架下偏心 test-mass merger-ringdown。
- [2605.28715](https://arxiv.org/abs/2605.28715) - SEOBNRv6EHM，面向 generic planar-orbit BBH。

### EMRI / Test-Mass / EOB-Teukolsky

- [0612096](https://arxiv.org/abs/gr-qc/0612096) 和 [0612151](https://arxiv.org/abs/gr-qc/0612151) - extreme-mass-ratio 极限下的 merger 和波形。
- [0909.4263](https://arxiv.org/abs/0909.4263) - EOB 框架中的 EMRI 建模。
- [1009.6013](https://arxiv.org/abs/1009.6013) - Kerr 背景准圆赤道轨道的 EOB EMRI 波形。
- [1108.0995](https://arxiv.org/abs/1108.0995) - 用数值 flux 构造 IMRI 的 EOB 动力学。
- [2207.14002](https://arxiv.org/abs/2207.14002) - GSF-informed 偏心 large-mass-ratio EOB。
- [2603.05601](https://arxiv.org/abs/2603.05601) - test-mass 极限中的 EOB 框架推进。
- [2606.09445](https://arxiv.org/abs/2606.09445) - generic EMRI 的自洽 EOB-Teukolsky 框架。

### 数据分析 / 降阶模型 / 替代模型 / 加速

- [0902.0307](https://arxiv.org/abs/0902.0307) - 与 EOB 相关的 compact-binary 搜索和参数估计。
- [1211.6184](https://arxiv.org/abs/1211.6184) - 面向 low-mass BBH 搜索的 template bank。
- [1402.4146](https://arxiv.org/abs/1402.4146) - 频域降阶模型。
- [1611.03703](https://arxiv.org/abs/1611.03703) - SEOBNRv4 reduced-order 版本在探测时代数据分析中的使用。
- [2303.18039](https://arxiv.org/abs/2303.18039) - 更快的 SEOBNRv5HM 构造。
- [2604.14270](https://arxiv.org/abs/2604.14270) - multimodal EOB 波形的神经网络替代模型。
- [2606.02690](https://arxiv.org/abs/2606.02690) - 面向长信号的频域 EOB 波形速度和精度改进。

## 维护说明

- 主页面保持精选，不把全部抓取结果展开；大范围候选条目放入 CSV。
- 新增论文时，优先归入上面的中文技术分类；CSV 中可继续使用下面的机器标签：
  `foundations_hamiltonian_pn_pm`, `resummation_flux_waveform`,
  `nr_calibration_eobnr_seobnr_teobresums`, `gsf_gauge_invariants`,
  `spin_precession`, `tides_neutron_stars`,
  `eccentric_hyperbolic_scattering`, `emri_test_mass_teukolsky`,
  `data_analysis_lvkc`。
- 如果某个技术方向需要详细阅读笔记，单独建立主题文件，不要无限扩展本页。
