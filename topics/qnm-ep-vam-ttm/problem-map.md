# 问题地图：QNM EP / 谱不稳定 / VAM-TTM

## 1. 谱不稳定是否有物理意义

QNM 谱点对算子扰动敏感，并不自动意味着可观测 ringdown 信号同样敏感。需要区分频域本征值漂移、初始数据激发系数、本征函数近合并、时间域可提取的 damped sinusoid，以及有限时间窗和噪声下的可辨识性。

## 2. avoided crossing 与 EP 的关系

当两个 QNM 频率在参数空间中接近时，表面上可能只是 avoided crossing；但如果本征值和本征函数同时合并，则进入 EP 语言。关键证据包括模式交换、Berry phase、hysteresis、Riemann surface branch 和 Puiseux 平方根标度。

## 3. 标准 QNM 展开在 EP 附近是否失效

EP 附近本征函数近合并，标准“独立 damped sinusoids 叠加”可能不足。需要检查是否出现线性时间因子、Jordan block 类结构、EP frequency 的稳定性，以及 time-domain fitting 是否能区分 EP ansatz 和普通 QNM ansatz。

## 4. SdS 半开放系统的特殊性

半开放 SdS 系统把边界反射率 \(\mathcal K\) 作为可调参数，尤其是复参数时可以显式寻找 EP。这里要判断 \(\mathcal K\) 的复延拓是数学工具还是有物理边界解释，二阶 EP 是否数值稳健，模式交换和 Puiseux 标度能否独立复现。

## 5. VAM/TTM 与 QNM EP 的区别

VAM/TTM 不是 EP 的同义词。它们和 EP 相邻，是因为都依赖复频率、非厄米边界条件和谱稳定性诊断：

- QNM：outgoing boundary conditions；
- TTM：total transmission / reflectionless boundary behavior；
- VAM：通过 tailored time-dependent scattering 激发的 virtual absorption；
- EP：本征值和本征函数在参数空间中的非厄米退化。

## 6. 数值可信度问题

本方向容易被数值误差误导。每个结果至少应检查网格/截断阶数收敛、branch labeling 是否连续、pseudospectrum contour 是否支持该根稳定、condition number 是否异常、复参数路径是否真的包围 EP，以及时间域信号是否支持频域解释。
