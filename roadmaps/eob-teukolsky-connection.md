# Roadmap: EOB-Teukolsky Connection

## Motivation

EOB-Teukolsky connections may provide a route from test-mass/BHPT fluxes to EOB radiation reaction and EMRI waveform modeling.

## Technical Chain

EOB trajectory -> Teukolsky/Sasaki-Nakamura source -> fluxes and waveform modes -> radiation reaction -> self-consistent evolution -> EMRI waveform.

## Key Concepts

- Teukolsky equation
- Sasaki-Nakamura transformation
- flux balance
- test-mass limit
- EOB trajectory
- radiation reaction

## Representative Papers

- [2606.09445](https://arxiv.org/abs/2606.09445) - self-consistent EOB-Teukolsky framework, needs human check.
- Earlier EOB EMRI papers: [0909.4263](https://arxiv.org/abs/0909.4263), [1009.6013](https://arxiv.org/abs/1009.6013).

## Codebases

- Black Hole Perturbation Toolkit.
- pySEOBNR for EOB trajectory experiments.
- TODO: verify Teukolsky/Sasaki-Nakamura public code paths.

## Relation to My Work

This roadmap is a future path beyond Hamiltonian-only diagnostics. It may help make dissipative dynamics and flux replacement more self-consistent.

## Open Problems

- How to map modified EOB trajectories into Teukolsky source terms?
- What test-mass flux information can safely inform comparable-mass EOB?
- How to validate phase accuracy over long inspirals?

## Data Source Links

- [../data/papers/eob_candidates.csv](../data/papers/eob_candidates.csv)
- [../data/papers/bhpt_candidates.csv](../data/papers/bhpt_candidates.csv)
