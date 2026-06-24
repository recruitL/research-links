# AI Evaluation Protocol

AI evaluation 只是初筛，不是最终学术判断。

每条 AI 评价都必须有人类校验。AI 输出不得直接作为最终学术判断，也不得替代论文阅读、公式检查、代码运行和复现实验。

## 评价维度

| Dimension | Meaning |
| --- | --- |
| Technical centrality | 是否是该方向的关键技术节点 |
| Reproducibility | 是否有清晰公式、代码或数据可复现 |
| Relevance to my work | 是否与我的研究路线直接相关 |
| Mathematical depth | 是否包含关键推导或理论结构 |
| Code usefulness | 是否能直接改造成项目代码 |
| Risk of misunderstanding | AI 是否容易误读该文献 |

## 评分

| Score | Meaning |
| --- | --- |
| A | must read / central |
| B | useful / relevant |
| C | background |
| D | peripheral |
| X | unclear / unreliable / needs human check |

## 风险标记

对 EOB、GSF、BHPT、QNM 等方向，AI 容易混淆：

- 相关和等价；
- 启发和证明；
- 近似公式和严格推导；
- 代码可运行和理论自洽；
- 替换 Hamiltonian 的诊断实验和完整自洽 EOB waveform model。

所有含高风险推断的 AI 评价必须标记 `needs human check`，并在人工阅读后再更新状态。
