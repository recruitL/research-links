# EOB (Effective One Body)

EOB 方向的目标是把广义相对论两体问题映射为一个有效一体问题，并用于紧致双星的动力学和引力波波形建模。

## Reading Path

1. 先读原始提出和 inspiral-plunge 过渡论文，理解 EOB 的基本映射、重求和和有效哈密顿量思想。
2. 再读综述，整理 EOB 与 post-Newtonian、numerical relativity、gravitational self-force 的关系。
3. 最后按具体问题补充：自旋、偏心、潮汐、中子星、校准波形模型、数据分析实现。

## Timeline

| Period | Thread | Notes |
| --- | --- | --- |
| 1998-2000 | Foundational EOB construction | 建立 EOB 两体动力学映射，并用于 inspiral 到 plunge 的过渡描述。 |
| 2000s | Waveform and resummation development | 发展重求和波形、多极波形和与 PN 信息的结合。 |
| 2010s | NR calibration and detector-era waveform models | 与数值相对论波形校准，形成可用于引力波数据分析的模型族。 |
| 2020s | Cross-mass-ratio information and broader compact-binary modeling | 吸收 GSF、PM、NR、潮汐和偏心信息，提升跨质量比和复杂轨道适用性。 |

## Seed References

- A. Buonanno and T. Damour, "Effective one-body approach to general relativistic two-body dynamics" (1998/1999).  
  <https://arxiv.org/abs/gr-qc/9811091>
- A. Buonanno and T. Damour, "Transition from inspiral to plunge in binary black hole coalescences" (2000).  
  <https://arxiv.org/abs/gr-qc/0001013>
- T. Damour, "Introductory lectures on the Effective One Body formalism" (2008).  
  <https://arxiv.org/abs/0802.4047>
- T. Damour and A. Nagar, "The Effective One Body description of the Two-Body problem" (2009).  
  <https://arxiv.org/abs/0906.1769>
- T. Damour, "The General Relativistic Two Body Problem and the Effective One Body Formalism" (2012).  
  <https://arxiv.org/abs/1212.3169>

## To Add

- EOBNR / SEOBNR / TEOBResumS 等模型线索
- 自旋、偏心、潮汐和中子星相关 EOB 文献
- EOB 与 GSF、PM、NR 信息融合的关键论文
- 可复现代码库、教程和 notebook
