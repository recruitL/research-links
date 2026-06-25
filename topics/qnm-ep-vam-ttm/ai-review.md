# AI 初评：QNM EP / 谱不稳定 / VAM-TTM

AI evaluation 只是初筛，不是最终学术判断。以下评分必须经过人工校验后才能用于正式引用或研究判断。

## 评分摘要

| 文献 | AI 评分 | 初步理由 | 人工校验 |
| --- | --- | --- | --- |
| `arXiv:2407.15191` | A | avoided crossing -> EP resonance 的直接入口 | no |
| `arXiv:2504.06072` | A | QNM resonance、EP 和 Riemann surface 框架 | no |
| `arXiv:2512.06903` | A | 半开放 SdS EP 的核心实现对象 | no |
| `arXiv:2512.02110` | A | EP ringdown 建模框架 | no |
| `arXiv:2509.19451` | A | VAM/TTM 主线入口 | no |
| `arXiv:2512.16372` | A | TTM 谱稳定性和 condition number | no |
| `arXiv:2004.06434` | A | pseudospectrum 基础 | no |
| `arXiv:2407.20850` | A | Kerr EP/hysteresis，补充强相关 | no |
| `arXiv:2511.17067` | A | exceptional line 和 EP pseudospectrum 标度 | no |
| `arXiv:2507.11663` | B | 谱不稳定综述，适合补背景 | no |
| `arXiv:2603.22261` | B | hairy black hole EP 扩展案例 | no |

## 主要误读风险

- 把 avoided crossing 和 EP 混为一谈；EP 需要本征函数合并和分支结构证据。
- 把 QNM 谱点漂移直接当成可观测 ringdown 漂移。
- 把 VAM/TTM 当作 EP 的同义词；它们只是使用相邻的复谱/非厄米边界条件语言。
- 忽略 inner product、扰动范数和离散化方案对 pseudospectrum 的影响。
- 在 branch tracking 时用频率远近重新编号，导致把模式交换误判为连续模式。
- 把复反射率 \(\mathcal K\) 的数学延拓过度解释成物理边界。

## 与当前工作的优先级

优先级最高的是 `arXiv:2512.06903`，因为它直接对应 SdS 半开放系统、复反射率、二阶 EP 和 Puiseux 标度。第二层是 `arXiv:2407.15191`、`arXiv:2504.06072` 和 `arXiv:2004.06434`，它们分别提供物理直觉、EP 框架和数学稳定性语言。VAM/TTM 线可作为并行方向，在理解 EP 之后继续推进。
