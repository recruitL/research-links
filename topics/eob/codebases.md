# EOB Codebases

本页是人工解释层。结构化数据见 [../../data/codebases/eob_codebases.csv](../../data/codebases/eob_codebases.csv)。

## pySEOBNR

- name: pySEOBNR
- url: <https://git.ligo.org/waveforms/software/pyseobnr>
- language: Python
- main use: SEOBNRv5 waveform generation and diagnostics
- status: active; verify current branch
- installation difficulty: medium
- theory transparency: medium-high
- modifiable or not: modifiable, but model architecture must be respected
- relation to my work: useful for PM-informed Hamiltonian diagnostics; not sufficient for a full self-consistent waveform replacement
- AI evaluation: B, highly relevant but requires code reading
- human check: not yet

## SEOBNR / LALSimulation

- name: LALSuite / LALSimulation
- url: <https://git.ligo.org/lscsoft/lalsuite>
- language: C/Python
- main use: production waveform implementations
- status: active
- installation difficulty: high
- theory transparency: medium
- modifiable or not: possible but heavy
- relation to my work: benchmark and validation target
- AI evaluation: B
- human check: not yet

## TEOBResumS / TEOBResumS-Dali

- url: <https://bitbucket.org/eob_ihes/teobresums>
- language: C/Python
- main use: resummed EOB waveform family and generic-orbit extensions
- status: needs verification
- installation difficulty: medium
- theory transparency: high
- modifiable or not: likely modifiable; must verify code layout
- relation to my work: comparison family for resummation and eccentric/scattering extensions
- AI evaluation: A/B, needs human check
- human check: not yet

## Black Hole Perturbation Toolkit

- url: <https://bhptoolkit.org>
- main use: BHPT, GSF, Teukolsky and related resources
- relation to my work: possible source for Teukolsky/Sasaki-Nakamura fluxes and GSF-EOB bridge
- AI evaluation: B
- human check: not yet

## NR Catalogs and Waveform Resources

- SXS catalog: <https://data.black-holes.org>
- main use: NR comparison and waveform validation
- relation to my work: extract gauge-invariant diagnostics such as `E_b(j)` and `Omega(j)`
- human check: not yet

## Scripts for Gauge-Invariant Diagnostics

TODO: create local scripts to extract and compare:

- `E_b(j)`;
- `Omega(j)`;
- scattering angle;
- waveform mismatch;
- flux balance diagnostics.
