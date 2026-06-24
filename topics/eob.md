# EOB (Effective One Body)

EOB 方向的目标是把广义相对论两体问题映射为一个有效一体问题，并用于紧致双星的保守动力学、辐射反作用和 inspiral-merger-ringdown 波形建模。

本页先按时间线梳理主干，再按技术主题组织文献。完整候选表见 [`data/eob_arxiv_candidates.csv`](../data/eob_arxiv_candidates.csv)。

## Harvest Status

- Last harvested: 2026-06-24
- Source: arXiv API / arXiv pages
- Query terms: `effective one body`, `effective-one-body`, `EOBNR`, `SEOBNR`, `TEOBResumS`, `EOB waveform`, `EOB model`, `EOB Hamiltonian`, plus manual core additions.
- Current candidate table: 443 arXiv records after GR/compact-binary filtering.
- Caveat: this is a working bibliography, not a final curated review. Some entries are downstream applications or comparison papers rather than core EOB formalism papers.

## Reading Path

1. Foundations: start from Buonanno-Damour and Damour-Jaranowski-Schafer to understand the EOB map, effective Hamiltonian, light ring/plunge language, and relation to PN dynamics.
2. Waveform construction: read the early resummed/factorized multipolar waveform papers before the NR calibration papers.
3. NR-calibrated model families: follow EOBNR -> SEOBNR -> TEOBResumS -> SEOBNRv5 / generic-orbit models.
4. Cross-method constraints: read the GSF/gauge-invariant comparison literature, especially redshift, periastron advance, ISCO shift, EOB potentials, and later 2GSF-informed models.
5. Specialized sectors: spin/precession, tides/BNS/NSBH, eccentric/unbound/scattering, EMRI/test-mass and data-analysis acceleration.

## Timeline

| Period | Main thread | Representative papers |
| --- | --- | --- |
| 1998-2001 | EOB map and early plunge/spin extensions | [9811091](https://arxiv.org/abs/gr-qc/9811091), [0001013](https://arxiv.org/abs/gr-qc/0001013), [0005034](https://arxiv.org/abs/gr-qc/0005034), [0103018](https://arxiv.org/abs/gr-qc/0103018) |
| 2002-2006 | 3PN EOB templates, recoil, test-mass/extreme-mass-ratio tests | [0211041](https://arxiv.org/abs/gr-qc/0211041), [0508067](https://arxiv.org/abs/gr-qc/0508067), [0602117](https://arxiv.org/abs/gr-qc/0602117), [0612096](https://arxiv.org/abs/gr-qc/0612096) |
| 2007-2009 | First serious NR comparisons and factorized/resummed waveforms | [0706.3732](https://arxiv.org/abs/0706.3732), [0711.2628](https://arxiv.org/abs/0711.2628), [0803.3162](https://arxiv.org/abs/0803.3162), [0811.2069](https://arxiv.org/abs/0811.2069), [0902.0790](https://arxiv.org/abs/0902.0790) |
| 2009-2012 | Tides, EMRI, GSF/gauge-invariant comparisons, multipolar IMR | [0911.5041](https://arxiv.org/abs/0911.5041), [1008.0935](https://arxiv.org/abs/1008.0935), [1008.4622](https://arxiv.org/abs/1008.4622), [1106.1021](https://arxiv.org/abs/1106.1021), [1209.0964](https://arxiv.org/abs/1209.0964), [1212.4357](https://arxiv.org/abs/1212.4357) |
| 2013-2016 | Generic mass ratios/spins, improved nonprecessing models, high-PN/GSF inputs | [1311.2544](https://arxiv.org/abs/1311.2544), [1312.2503](https://arxiv.org/abs/1312.2503), [1406.6913](https://arxiv.org/abs/1406.6913), [1409.6933](https://arxiv.org/abs/1409.6933), [1611.03703](https://arxiv.org/abs/1611.03703) |
| 2017-2021 | Detector-era models, TEOBResumS, reduced-order/surrogate use, eccentric extensions | [1806.01772](https://arxiv.org/abs/1806.01772), [2112.06952](https://arxiv.org/abs/2112.06952) |
| 2022-2026 | SEOBNRv5, 2GSF-informed fluxes, generic-orbit EOB, PM/GSF/NR fusion | [2207.14002](https://arxiv.org/abs/2207.14002), [2303.18026](https://arxiv.org/abs/2303.18026), [2303.18039](https://arxiv.org/abs/2303.18039), [2503.14580](https://arxiv.org/abs/2503.14580), [2505.11242](https://arxiv.org/abs/2505.11242), [2606.09445](https://arxiv.org/abs/2606.09445) |

## Technical Categories

### Foundations / Hamiltonian / PN-PM Dynamics

- [gr-qc/9811091](https://arxiv.org/abs/gr-qc/9811091) - Buonanno & Damour, original EOB construction for the relativistic two-body problem.
- [gr-qc/0001013](https://arxiv.org/abs/gr-qc/0001013) - Buonanno & Damour, inspiral-to-plunge transition for binary black holes.
- [gr-qc/0005034](https://arxiv.org/abs/gr-qc/0005034) - Damour, Jaranowski & Schafer, last stable orbit and 3PN information in the EOB framework.
- [gr-qc/0010104](https://arxiv.org/abs/gr-qc/0010104) - Fiziev & Todorov, related effective-particle treatment of the relativistic two-body problem.
- [gr-qc/0103018](https://arxiv.org/abs/gr-qc/0103018) - early spinning black-hole EOB extension.
- [1305.4884](https://arxiv.org/abs/1305.4884) - 4PN two-body interaction potential.
- [2405.19181](https://arxiv.org/abs/2405.19181) - PM information matched into spinning EOB waveform modeling.
- [2604.09545](https://arxiv.org/abs/2604.09545) - fifth post-Newtonian black-hole dynamics.

### Resummation / Flux / Factorized Waveforms

- [0705.2519](https://arxiv.org/abs/0705.2519) - faithful EOB waveforms in the small-mass-ratio limit.
- [0712.3003](https://arxiv.org/abs/0712.3003) - equal-mass faithful EOB waveforms.
- [0803.3162](https://arxiv.org/abs/0803.3162) - accurate EOB waveforms for inspiral and coalescence.
- [0811.2069](https://arxiv.org/abs/0811.2069) - factorized/resummed PN multipolar waveforms and the `rho_lm` resummation.
- [1003.0597](https://arxiv.org/abs/1003.0597) - multipolar analysis in the extreme-mass-ratio limit.
- [1012.2456](https://arxiv.org/abs/1012.2456) - testing and improving EOB multipolar waveforms.
- [1210.2834](https://arxiv.org/abs/1210.2834) - radiation reaction along generic EOB orbits.
- [2602.08833](https://arxiv.org/abs/2602.08833) - newer factorized/resummed waveform construction from the confluent Heun equation.

### NR Calibration / EOBNR / SEOBNR / TEOBResumS

- [0706.3732](https://arxiv.org/abs/0706.3732) - early NR-informed faithful EOB templates for nonspinning BBHs.
- [0711.2628](https://arxiv.org/abs/0711.2628) - EOB-vs-accurate-NR waveform comparison.
- [0902.0790](https://arxiv.org/abs/0902.0790) - equal-mass nonspinning EOB calibration to NR.
- [0912.3466](https://arxiv.org/abs/0912.3466) - spinning equal-mass EOB calibration to NR.
- [1106.1021](https://arxiv.org/abs/1106.1021) - nonspinning multipolar IMR EOB waveforms.
- [1212.4357](https://arxiv.org/abs/1212.4357) - improved nonspinning EOB and NR completion.
- [1311.2544](https://arxiv.org/abs/1311.2544) - generic mass ratios and spins.
- [1406.6913](https://arxiv.org/abs/1406.6913) - nonprecessing spinning BBH EOB.
- [1611.03703](https://arxiv.org/abs/1611.03703) - SEOBNRv4-era nonprecessing spinning BBH model calibrated to a large NR set.
- [1806.01772](https://arxiv.org/abs/1806.01772) - TEOBResumS time-domain model with nonprecessing spin, tides and self-spin effects.
- [2303.18039](https://arxiv.org/abs/2303.18039) - SEOBNRv5HM foundation for quasi-circular nonprecessing BBHs.
- [2503.14580](https://arxiv.org/abs/2503.14580) - TEOBResumS-Dali, generic compact binaries with arbitrary orbits.

### GSF / Gauge-Invariant Comparisons / EOB Potentials

- [0902.0573](https://arxiv.org/abs/0902.0573) - GSF correction to the Schwarzschild ISCO, a key benchmark for EOB comparisons.
- [1008.0935](https://arxiv.org/abs/1008.0935) - GSF precession invariant and constraints on EOB functions.
- [1008.4622](https://arxiv.org/abs/1008.4622) - ISCO self-force shift compared against PN/EOB methods.
- [1106.3278](https://arxiv.org/abs/1106.3278) - periastron advance in black-hole binaries, connecting NR/GSF/EOB comparisons.
- [1111.5610](https://arxiv.org/abs/1111.5610) - complete nonspinning EOB metric at linear order in mass ratio.
- [1209.0964](https://arxiv.org/abs/1209.0964) - GSF information between ISCO and light ring and the EOB `A(u)` potential.
- [1312.2503](https://arxiv.org/abs/1312.2503) - high-order PN contributions from analytical GSF calculations.
- [1409.6933](https://arxiv.org/abs/1409.6933) - GSF corrections to tidal interactions and EOB.
- [2303.18026](https://arxiv.org/abs/2303.18026) - SEOBNRv5 improved with second-order GSF fluxes.
- [2505.11242](https://arxiv.org/abs/2505.11242) - SEOBNR-GSF, IMR EOB model with GSF-informed Hamiltonian.

### Spin / Precession

- [0103018](https://arxiv.org/abs/gr-qc/0103018) - early spinning BBH EOB.
- [0803.0915](https://arxiv.org/abs/0803.0915) - NLO spin-orbit coupling in EOB dynamics.
- [0912.3517](https://arxiv.org/abs/0912.3517) - improved spinning EOB Hamiltonian.
- [1106.4349](https://arxiv.org/abs/1106.4349) and [1107.2904](https://arxiv.org/abs/1107.2904) - NNLO spin-orbit couplings in EOB Hamiltonians.
- [1202.0790](https://arxiv.org/abs/1202.0790) - prototype nonprecessing spinning IMR EOB model.
- [1307.6232](https://arxiv.org/abs/1307.6232) - spinning precessing BBH EOB waveforms.
- [2303.18143](https://arxiv.org/abs/2303.18143) - analytical precessing-spin two-body dynamics for SEOBNRv5.

### Tides / Binary Neutron Stars / NSBH

- [0911.5041](https://arxiv.org/abs/0911.5041) - EOB description of tidal effects in compact binaries.
- [1009.0521](https://arxiv.org/abs/1009.0521) - analytic modeling of tidal effects in BNS inspiral.
- [1103.3874](https://arxiv.org/abs/1103.3874) - BNS NR simulations compared with EOB models.
- [1202.3565](https://arxiv.org/abs/1202.3565) - effective-action approach to higher-order tidal interactions and EOB.
- [1412.4553](https://arxiv.org/abs/1412.4553) - tidally interacting BNS dynamics up to merger.
- [1804.02235](https://arxiv.org/abs/1804.02235) - matter imprints and TEOBResumS in waveform comparisons.
- [2307.15125](https://arxiv.org/abs/2307.15125) - NR-informed TEOBResumS improvement for BNS.
- [2503.18934](https://arxiv.org/abs/2503.18934) - SEOBNRv5THM for fast BNS waveform modeling.

### Eccentric / Hyperbolic / Scattering / Generic Orbits

- [1210.2834](https://arxiv.org/abs/1210.2834) - radiation reaction for generic EOB orbits.
- [1402.7307](https://arxiv.org/abs/1402.7307) - strong-field black-hole scattering, numerics versus analytics.
- [2112.06952](https://arxiv.org/abs/2112.06952) - SEOBNRv4EHM eccentric multipolar BBH waveforms.
- [2207.14002](https://arxiv.org/abs/2207.14002) - GSF-informed EOB model for eccentric large-mass-ratio inspirals.
- [2503.14580](https://arxiv.org/abs/2503.14580) - generic compact-binary dynamics, including eccentric, hyperbolic and non-planar cases.
- [2603.19913](https://arxiv.org/abs/2603.19913) - eccentric test-mass merger-ringdown in the EOB framework.
- [2605.28715](https://arxiv.org/abs/2605.28715) - SEOBNRv6EHM for generic planar-orbit BBHs.

### EMRI / Test-Mass / EOB-Teukolsky

- [0612096](https://arxiv.org/abs/gr-qc/0612096) and [0612151](https://arxiv.org/abs/gr-qc/0612151) - merger and waveforms in the extreme-mass-ratio limit.
- [0909.4263](https://arxiv.org/abs/0909.4263) - modeling EMRIs within EOB.
- [1009.6013](https://arxiv.org/abs/1009.6013) - EOB EMRI waveforms for quasi-circular equatorial Kerr orbits.
- [1108.0995](https://arxiv.org/abs/1108.0995) - EOB dynamics with numerical fluxes for IMRIs.
- [2207.14002](https://arxiv.org/abs/2207.14002) - GSF-informed eccentric large-mass-ratio EOB.
- [2603.05601](https://arxiv.org/abs/2603.05601) - advancing EOB in the test-mass limit.
- [2606.09445](https://arxiv.org/abs/2606.09445) - self-consistent EOB-Teukolsky framework for generic EMRIs.

### Data Analysis / Reduced-Order / Surrogate / Speed

- [0902.0307](https://arxiv.org/abs/0902.0307) - EOB-relevant compact-binary searches and parameter estimation.
- [1211.6184](https://arxiv.org/abs/1211.6184) - template banks for low-mass BBH searches.
- [1402.4146](https://arxiv.org/abs/1402.4146) - frequency-domain reduced-order models.
- [1611.03703](https://arxiv.org/abs/1611.03703) - reduced-order SEOBNRv4 use for detector-era analysis.
- [2303.18039](https://arxiv.org/abs/2303.18039) - faster SEOBNRv5HM construction.
- [2604.14270](https://arxiv.org/abs/2604.14270) - neural-network surrogate for multimodal EOB waveforms.
- [2606.02690](https://arxiv.org/abs/2606.02690) - frequency-domain EOB waveforms for speed and accuracy in long signals.

## Maintenance Notes

- Keep the main page selective. Put broad harvested records in the CSV.
- When adding a paper, assign one or more technical tags from:
  `foundations_hamiltonian_pn_pm`, `resummation_flux_waveform`,
  `nr_calibration_eobnr_seobnr_teobresums`, `gsf_gauge_invariants`,
  `spin_precession`, `tides_neutron_stars`,
  `eccentric_hyperbolic_scattering`, `emri_test_mass_teukolsky`,
  `data_analysis_lvkc`.
- For detailed reading notes, create one file per theme instead of expanding this page indefinitely.
