# EOB Open Questions

## PM-informed Hamiltonian

- 如何把 PM scattering input 转换为 EOB radial potential 或 effective Hamiltonian？
- 这种替换在 pySEOBNR / SEOBNRv5HM 中能诊断什么？
- 哪些效应会被 radiation reaction、flux 和 calibration 吸收或掩盖？

## Self-Consistent Waveform Modeling

- 如果只替换 Hamiltonian，哪些 waveform 部分仍不自洽？
- 如何同步更新 radiation reaction、factorized waveform、NQC correction 和 merger-ringdown attachment？

## Gauge-Invariant Comparison

- `E_b(j)` 和 `Omega(j)` 如何从 NR、EOB 和 modified Hamiltonian 计算中一致提取？
- scattering angle 能否作为 PM-to-EOB 的更直接诊断？

## GSF-informed EOB

- 一阶/二阶 GSF 对 EOB potentials 和 flux 的约束如何进入 comparable-mass waveform model？
- GSF-informed EOB 与 PM-informed Hamiltonian 是否能统一进同一个 diagnostics framework？

## EOB-Teukolsky / Flux

- Teukolsky / Sasaki-Nakamura fluxes 能否为 radiation reaction 提供更自洽的 test-mass 极限输入？
- 如何避免把 test-mass flux 直接外推到 comparable-mass 系统？
