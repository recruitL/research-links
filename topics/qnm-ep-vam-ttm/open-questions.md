# 开放问题：QNM EP / 谱不稳定 / VAM-TTM

## 理论问题

- EP frequency 是否比单个 QNM branch 更适合作为近 EP ringdown 的物理频率？
- QNM 本征函数近合并时，标准 damped sinusoid 展开需要怎样的最小修正？
- VAM/TTM 的 reflectionless 条件和 QNM EP 的本征函数合并之间有没有更深的统一结构？
- 半开放 SdS 的复反射率 \(\mathcal K\) 是否有可解释的物理实现，还是主要作为复参数探针？

## 数值问题

- `arXiv:2512.06903` 的二阶 EP 是否能用独立 spectral discretization 复现？
- Puiseux 平方根标度对网格数、截断阶数和 branch tracking 策略是否稳定？
- TTM condition number 是否足以判断 VAM/TTM 根的可信度？
- pseudospectrum 的扰动范数如何选，才和物理势扰动或边界扰动相匹配？

## 与 EOB/ringdown 的问题

- EOB merger-ringdown attachment 是否需要显式避开 EP/avoided crossing 区域？
- overtone extraction 在 resonance 附近的系统误差是否会影响 final black hole 参数估计？
- 如果 ringdown 使用 pySEOBNR/NR-calibrated QNM attachment，哪些 EP 现象会被模型吸收，哪些会暴露为 mismatch？

## 复现优先级

1. 复现 toy model EP 和 Puiseux 标度。
2. 复现半开放 SdS 的模式交换图。
3. 复现 `arXiv:2512.06903` 的二阶 EP 定位。
4. 用 pseudospectrum/condition number 检查同一根的稳定性。
5. 复现一个 VAM/TTM reflectionless 条件。
