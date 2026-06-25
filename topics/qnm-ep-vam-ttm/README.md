# QNM EP / 谱不稳定 / VAM-TTM

本方向整理黑洞拟正规模（quasinormal modes, QNMs）中 exceptional points（EPs）、谱不稳定、avoided crossing、ringdown 共振激发，以及 virtual absorption modes（VAM）/ total transmission modes（TTM）之间的技术脉络。

这里不是一般 QNM 方法目录，而是聚焦一个更窄的问题：当 QNM 谱被看成非自伴算子的复谱时，哪些谱结构是真正可观测的，哪些只是边界条件、势扰动或数值离散化导致的敏感性？

## 核心问题

- QNM avoided crossing 什么时候应该解释为 EP 附近的分支结构？
- EP 附近的本征值、本征函数和激发因子如何共同影响 ringdown？
- pseudospectrum 和 condition number 能否判断某个 QNM/TTM 根是否可信？
- 半开放 Schwarzschild-de Sitter（SdS）系统中的复反射率、模式交换和 Puiseux 标度如何复现？
- VAM/TTM 与 QNM EP 共享哪些非厄米谱语言，又在哪些物理问题上不同？

## 推荐阅读顺序

1. `arXiv:2407.15191`：先建立 avoided crossing 与 EP 共振激发的直觉。
2. `arXiv:2504.06072`：再读 QNM resonance/Riemann surface 的直接框架。
3. `arXiv:2512.06903`：进入半开放 SdS 系统和复反射率参数。
4. `arXiv:2004.06434` 与 `arXiv:2107.09673`：补 pseudospectrum 和谱稳定性的数学基础。
5. `arXiv:2509.19451` 与 `arXiv:2512.16372`：转到 VAM/TTM 和 TTM 谱稳定性。
6. `arXiv:2512.02110` 与 `arXiv:2509.06411`：看 EP 如何改变 ringdown time-domain extraction。

## 技术链条

```text
非自伴边值问题
-> QNM / TTM 复频率谱
-> pseudospectrum 与 condition number
-> avoided crossing / EP / exceptional line
-> Riemann surface branch 与 Puiseux 标度
-> ringdown 共振激发与时间域提取
-> SdS 半开放边界、复反射率 K、VAM/TTM
```

## 数据入口

- [候选论文 CSV](../../data/papers/qnm_ep_vam_ttm_candidates.csv)
- [精选论文 CSV](../../data/papers/qnm_ep_vam_ttm_selected.csv)
- [时间线 CSV](../../data/papers/qnm_ep_vam_ttm_timeline.csv)
- [分类 CSV](../../data/papers/qnm_ep_vam_ttm_categories.csv)
- [QNM 代码库 CSV](../../data/codebases/qnm_codebases.csv)

## 分析页面

- [时间线](timeline.md)
- [问题地图](problem-map.md)
- [方法地图](method-map.md)
- [文献整理](literature.md)
- [代码库入口](codebases.md)
- [AI 初评](ai-review.md)
- [开放问题](open-questions.md)
- [笔记目录](notes/README.md)

## 与我当前工作的关系

这一方向和 EOB/ringdown 的关系不只是“QNM 频率表”。更重要的是：

- EOB merger-ringdown attachment 假设的 damped sinusoids 在 EP 附近可能需要修正；
- overtone 提取和模式排序在 avoided crossing/branch exchange 附近可能不稳定；
- SdS 半开放系统提供了一个可复现的 EP/VAM 技术沙盒；
- pseudospectrum 可以作为判断数值根可信度的诊断工具；
- VAM/TTM 提供了与 QNM 不同但相邻的复频率谱问题，适合比较边界条件的物理含义。

## 当前状态

- AI 初筛：已完成，主线文献评分多数为 A。
- 人工校验：未完成，所有条目仍标记为 `human_checked=no`。
- 复现状态：未开始；优先复现 SdS 半开放系统中的 EP、模式交换和 Puiseux 标度。
