# 代码库入口：QNM EP / 谱不稳定 / VAM-TTM

## 当前判断

这个方向目前以论文和数值方法为主，暂时没有确认过的、可直接复现所有 EP/VAM/TTM 图的统一公开代码库。后续不能把“论文中使用了 spectral method”误写成“存在可复现代码”。

## 已有入口

### Black Hole Perturbation Toolkit

- URL: <https://bhptoolkit.org>
- 作用：BHPT/QNM 相关资源入口，可用于查背景方程、频域方法和现有工具。
- 限制：不是专门为 EP、pseudospectrum、VAM 或 TTM 复现而设计。
- 当前状态：seed entry；尚未做本方向复现测试。

### Berti Ringdown Data

- URL: <https://pages.jh.edu/~eberti2/ringdown/>
- 作用：QNM/ringdown 数据入口，适合作为常规 QNM 频率表参考。
- 限制：不能替代 EP 分支追踪、pseudospectrum 或 TTM 稳定性计算。
- 当前状态：只作为数据参考入口，尚未写入 codebase CSV。

## 建议本地复现脚手架

优先不要一开始追求完整 Kerr。更稳妥的顺序是：

1. 复现一个 1D 非自伴 toy model 的 EP 和 Puiseux 标度。
2. 复现 Schwarzschild/SdS 的 hyperboloidal 或 spectral eigenvalue problem。
3. 在半开放 SdS 中扫描复反射率 \(\mathcal K\)。
4. 画模式交换、branch tracking 和 condition number。
5. 再考虑 VAM/TTM 的 generalized eigenvalue problem。

## 待查代码

- `arXiv:2512.06903` 是否公开 SdS 半开放 EP 代码。
- `arXiv:2512.16372` 是否公开 TTM pseudospectrum 代码。
- `arXiv:2509.06411` 是否公开 Kerr ringdown extraction benchmark。
- 是否已有稳定的 Python/Mathematica package 支持 QNM pseudospectrum 计算。

## 数据文件

- [QNM codebases CSV](../../data/codebases/qnm_codebases.csv)
