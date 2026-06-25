# Roadmap：QNM EP / 谱不稳定 / VAM-TTM

## Motivation

QNM 通常被当作 ringdown 的复频率表使用，但 EP、pseudospectrum 和 VAM/TTM 说明：开放黑洞系统的复谱并不只是“查表”问题。模式的稳定性、分支结构、边界条件和时间域激发同样重要。

## Technical Chain

```text
black-hole perturbation equation
-> open boundary conditions
-> non-self-adjoint eigenvalue problem
-> pseudospectrum / condition number
-> avoided crossing / exceptional point
-> branch tracking / Puiseux scaling
-> ringdown resonance and extraction
-> semi-open SdS reflectivity
-> VAM / TTM spectral stability
```

## Key Concepts

- 拟正规模（quasinormal modes, QNMs）
- 非自伴算子（non-self-adjoint operator）
- pseudospectrum 与 spectral instability
- avoided crossing、exceptional point（EP）和 exceptional line
- Riemann surface branch 与 Puiseux square-root scaling
- hyperboloidal framework
- semi-open system 与 complex reflectivity \(\mathcal K\)
- virtual absorption modes（VAM）
- total transmission modes（TTM）
- condition number

## Representative Papers

### 基础与稳定性

- `arXiv:2004.06434`：QNM pseudospectrum 基础。
- `arXiv:2107.09673`：RN 黑洞 pseudospectrum。
- `arXiv:2404.01374`：谱不稳定的物理意义。

### EP 与 resonance

- `arXiv:2407.15191`：avoided crossing 与 EP 共振激发。
- `arXiv:2504.06072`：QNM resonances、EP 和 Riemann surface。
- `arXiv:2407.20850`：Kerr EP 与 hysteresis。
- `arXiv:2511.17067`：exceptional line 与 pseudospectrum。

### Ringdown 建模

- `arXiv:2503.21276`：不稳定 chords 和破坏性共振激发。
- `arXiv:2509.06411`：Kerr ringdown resonance extraction benchmark。
- `arXiv:2512.02110`：EP ringdown 框架。

### SdS / VAM / TTM

- `arXiv:2512.06903`：半开放 SdS QNM EP。
- `arXiv:2509.19451`：tailored incoming signal 的 total absorption / VAM。
- `arXiv:2512.16372`：TTM pseudospectrum 和稳定性。
- `arXiv:2603.22897`：半开放 SdS 的 VAM。

## Codebases

当前没有确认过的统一复现代码库。先保留：

- Black Hole Perturbation Toolkit：BHPT/QNM 背景工具入口；
- Berti ringdown page：常规 QNM 数据参考；
- 本地待建 spectral/hyperboloidal toy code：用于 EP、Puiseux 标度和 pseudospectrum 复现。

## Relation to My Work

这条线对当前工作最直接的价值是：

- 给 EOB merger-ringdown attachment 提供风险清单；
- 帮助判断 overtone extraction 是否受 EP/resonance 影响；
- 把 SdS 半开放系统作为可控复现实验；
- 为 VAM/TTM 的根稳定性提供诊断；
- 训练对非厄米谱、分支追踪和边界条件的数值直觉。

## Open Problems

- 如何在实际 ringdown 数据分析中识别 EP resonance，而不是过拟合 overtone？
- EP 附近的可观测量应是 branch frequency、EP averaged frequency，还是 time-domain waveform feature？
- VAM/TTM 的谱稳定性是否能给出比 QNM 更稳健的黑洞探针？
- 半开放 SdS 的复反射率能否对应真实物理边界或等效环境？
- pseudospectrum 中的扰动范数如何和物理模型误差对应？

## First Reproduction Targets

1. 复现一个 2x2 非厄米矩阵的 EP、模式交换和 Puiseux 标度。
2. 复现 Schwarzschild/SdS toy potential 的 pseudospectrum。
3. 复现半开放 SdS 复反射率扫描。
4. 复现 `arXiv:2512.06903` 中二阶 EP 的定位和绕行。
5. 复现 `arXiv:2512.16372` 的一个 TTM condition number 诊断。
