# EOB Method Map

## Effective Hamiltonian

EOB 用 effective Hamiltonian 表示两体保守动力学。当前 PM-informed Hamiltonian 诊断应放在这里，而不是直接声称替换了完整 waveform model。

## EOB Potentials

常见对象包括 `A(u)`、`D(u)`、`Q(u,p_r)` 等 potentials。GSF 和 PN/PM 结果可以为 potentials 提供约束。

## Tortoise Coordinate / Radial Potentials

在波形和 plunge/ringdown 处理中，tortoise coordinate 和 radial potential 可能影响数值稳定性和边界行为。具体实现依赖模型和代码库，需要逐个检查。

## Radiation Reaction

radiation reaction 描述耗散动力学，通常与 flux 和 waveform modes 绑定。只替换 Hamiltonian 时 radiation reaction 并未自动自洽更新。

## Factorized Waveform

factorized waveform 将多极波形拆解为源项、尾项、相位、残差幅度等结构，是 EOB waveform resummation 的核心技术。

## NQC Correction

NQC correction 用于修正接近 merger 的波形形状，通常与 NR 校准相关。它是 model calibration 的关键位置之一。

## Merger-Ringdown Attachment

EOB 通过匹配 QNM 或 ringdown ansatz 延伸到 merger-ringdown。该步骤与 QNM 频率、匹配时间和模式选择有关。

## NR Calibration

NR calibration 用数值相对论波形约束自由参数、NQC correction 和 merger-ringdown attachment。需要记录校准数据范围。

## Gauge-Invariant Diagnostics

优先诊断：

- `E_b(j)`；
- `Omega(j)`；
- scattering angle；
- self-force redshift；
- periastron advance；
- spin-precession invariant。

这些量有助于比较 PM、GSF、NR 和 EOB，而不直接依赖坐标变量。
