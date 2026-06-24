# research-links

研究方向脉络、参考文献、项目入口和可复用链接索引。

这个仓库用于沉淀那些不一定属于某个代码项目、但需要长期追踪的研究材料：

- 一个方向从提出到发展的时间线
- 关键论文、综述、讲义和代码库入口
- 不同项目页面需要共同指向的外部链接
- 后续论文复现或阅读笔记的材料清单

## Topics

| Topic | Page | Scope |
| --- | --- | --- |
| EOB | [topics/eob.md](topics/eob.md) | Effective One Body 方法从提出、波形建模到与 NR/GSF 结合的发展脉络；候选表见 [data/eob_arxiv_candidates.csv](data/eob_arxiv_candidates.csv) |
| GSF | [topics/gsf.md](topics/gsf.md) | Gravitational self-force 的基础方程、正则化方法、综述和应用参考 |

## Link Format

建议每条链接尽量保留这些字段，方便以后迁移到网页或脚本化索引：

```text
- Title:
  Authors:
  Year:
  Link:
  Tags:
  Note:
```
