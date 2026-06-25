# Roadmap: QNM Methods

## Motivation

QNM methods are needed for ringdown modeling, EOB merger-ringdown attachment and black-hole spectroscopy.

## Technical Chain

Perturbation equation -> boundary conditions -> eigenvalue problem -> numerical method -> convergence diagnostics -> physical mode interpretation.

## Key Concepts

- shooting
- continued fraction / Leaver
- WKB
- spectral method
- pseudospectral method
- time-domain extraction
- matrix eigenvalue method
- exceptional points
- spurious modes and convergence diagnostics

## Representative Papers

- Leaver continued-fraction method: TODO: verify exact reference.
- WKB QNM methods: TODO: verify.
- Spectral and pseudospectral QNM methods: TODO: verify.
- Pseudospectrum and QNM instability: `arXiv:2004.06434`.
- QNM exceptional points and resonances: `arXiv:2407.15191`, `arXiv:2504.06072`.
- Semi-open SdS EP and VAM/TTM route: `arXiv:2512.06903`, `arXiv:2509.19451`, `arXiv:2512.16372`.

## Codebases

- Black Hole Perturbation Toolkit.
- TODO: add qnm-specific packages after verification.

## Relation to My Work

QNM matters for EOB merger-ringdown attachment and for diagnosing ringdown parts of waveform models. It is also a numerical-methods topic suitable for standalone reproduction.

## Open Problems

- How to separate physical modes from spurious numerical eigenvalues?
- Which convergence diagnostics are reliable near exceptional points?
- How to connect time-domain extraction with frequency-domain eigenvalues?

## Data Source Links

- [../data/papers/qnm_candidates.csv](../data/papers/qnm_candidates.csv)
- [../data/papers/qnm_ep_vam_ttm_candidates.csv](../data/papers/qnm_ep_vam_ttm_candidates.csv)
- [../data/codebases/qnm_codebases.csv](../data/codebases/qnm_codebases.csv)

## Specialized Roadmaps

- [QNM EP / 谱不稳定 / VAM-TTM](qnm-ep-vam-ttm.md)
