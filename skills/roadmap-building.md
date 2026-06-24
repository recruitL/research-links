# Skill: Roadmap Building

## Purpose

Build technical roadmaps that explain how a research direction developed and how its concepts are connected.

Human-facing Markdown outputs should be written primarily in Chinese, while this skill file itself remains in English.

## Required Roadmap Structure

```markdown
# Roadmap: <Title>
## Motivation
## Technical Chain
## Key Concepts
## Representative Papers
## Relevant Codebases
## Relation to My Work
## Open Problems
## Data Sources
```

## Technical Chain Style

Use explicit chains such as:

```text
PN dynamics
-> EOB mapping
-> effective Hamiltonian
-> radiation reaction
-> waveform resummation
-> NR calibration
-> production waveform model
```

or:

```text
black-hole perturbation theory
-> singular field
-> Detweiler-Whiting split
-> regularization
-> self-force
-> long-time orbital evolution
-> EMRI waveform
```

## Rules

- Do not make the roadmap a bibliography.
- Explain why each stage is technically needed.
- Separate historical order from logical dependency.
- Mark uncertain relations as tentative.
- Link to CSV data files.
