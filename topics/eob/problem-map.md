# EOB Problem Map

## 1. GR Two-Body Problem

EOB 的核心是处理 GR 中两个紧致天体的相对运动。直接两体问题没有简单闭式解，因此需要把两体动力学映射为有效一体动力学。

## 2. IMR Waveform Modeling

引力波数据分析需要覆盖 inspiral、merger 和 ringdown 的连续波形。EOB 提供一套把保守动力学、辐射反作用和 ringdown attachment 连接起来的框架。

## 3. Need for Resummation

PN 展开在强场区收敛和表现有限，因此 EOB 使用重求和策略，例如 Padé-like ideas、factorized waveform、`rho_lm` resummation 和 potentials 的重组织。

## 4. Combining PN, PM, GSF, NR and Perturbation Theory

EOB 的优势在于可吸收多个来源的信息：

- PN：弱场低速展开；
- PM：散射和相对论 two-body dynamics；
- GSF：小质量比但强场的规范不变量；
- NR：可比较质量比的强场数值波形；
- BHPT/Teukolsky：test-mass 和 EMRI 极限。

## 5. Calibration Versus First-Principles Modeling

NR calibration 提高模型精度，但也引入拟合和模型选择。当前问题是如何区分 first-principles input、calibrated parameter 和 phenomenological correction。

## 6. Conservative Versus Dissipative Dynamics

替换 effective Hamiltonian 主要影响保守动力学；完整 waveform 还需要一致的 radiation reaction、flux、factorized waveform 和 merger-ringdown attachment。

## 7. Gauge-Invariant Comparison

为避免坐标规范误读，应优先比较：

- `E_b(j)`；
- `Omega(j)`；
- scattering angle；
- redshift invariant；
- periastron advance；
- spin-precession invariant。
