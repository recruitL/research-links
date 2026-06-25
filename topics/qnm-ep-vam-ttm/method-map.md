# 方法地图：QNM EP / 谱不稳定 / VAM-TTM

## 非自伴算子与边值问题

黑洞 QNM/TTM 通常来自带 outgoing、ingoing 或 transmission 条件的开放系统边值问题。相应算子非自伴，因此本征值可能对微扰高度敏感。

## Pseudospectrum

Pseudospectrum 用来回答：如果算子受到范数为 \(\epsilon\) 的扰动，本征值可能移动到哪里。它比单独列 QNM 频率更适合诊断谱稳定性，尤其适合判断高阶 overtone、TTM 根和 EP 附近谱点是否可信。

## Exceptional point 与 Puiseux 标度

EP 是非厄米系统中的退化点，本征值和本征函数同时合并。二阶 EP 附近常见平方根型 Puiseux 展开：

```text
omega(lambda) ~= omega_EP + c sqrt(lambda - lambda_EP)
```

需要检查的不只是频率接近，还包括本征函数近合并、模式交换和绕行后的分支结构。

## Riemann surface 与 branch tracking

`arXiv:2504.06072` 的关键观点是：EP 附近两条 QNM 模式可以是同一个复函数在 Riemann surface 上的两个 sheet。实际追踪模式时应避免按频率远近粗暴编号。

## Hyperboloidal framework

很多现代谱稳定性和 EP ringdown 工作使用 hyperboloidal compactification，把开放边界条件吸收到有限区间上的非自伴特征值问题中。优点是适合 spectral discretization 和 pseudospectrum 计算；风险是离散化规范、内积和扰动范数都要人工校验。

## Semi-open SdS 与复反射率

半开放 SdS 系统把一侧边界设为可调反射率 \(\mathcal K\)。当 \(\mathcal K\) 允许取复值时，可以在二维参数空间中显式寻找 EP。最小复现实验应包括扫描复 \(\mathcal K\)、追踪两支 QNM、定位二阶 EP、绕行 EP 检查模式交换，并拟合 Puiseux 平方根标度。

## VAM/TTM 方法

TTM 关注 reflectionless / total transmission 的复频率条件。VAM 则从时变散射角度理解 tailored incoming signal 的 total absorption。方法上要关注 TTM 广义特征值问题、reflection amplitude 的零点、condition number、TTM pseudospectrum 和 time-domain scattering signal。
