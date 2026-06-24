# Code/Paper Note: SEOBNRv5

## Basic Info

- Representative paper: [2303.18039](https://arxiv.org/abs/2303.18039)
- Codebase: pySEOBNR, needs local inspection
- Topic: EOB waveform model
- Tags: SEOBNRv5; pySEOBNR; Hamiltonian diagnostics

## One-sentence Summary

SEOBNRv5 是当前 PM-informed Hamiltonian diagnostic 最直接相关的现代 EOB model family。

## Technical Role in the Field

现代高效 SEOBNR waveform model，面向准圆、非进动 BBH，并与 pySEOBNR 代码实现相关。

## Main Equations / Concepts

- effective Hamiltonian;
- radiation reaction;
- waveform modes;
- calibration;
- model speed and implementation.

## Relation to Other Papers

- Previous: SEOBNRv4.
- Follow-up: 2GSF-informed SEOBNRv5 flux and future generic extensions.

## Relevance to My Work

可用于替换 Hamiltonian 的诊断实验，但必须明确这不是完整 waveform self-consistency。radiation reaction、flux、waveform 和 calibration 仍需处理。

## AI Evaluation

- Rating: A
- Risk: 高风险。AI 容易把局部 Hamiltonian 修改描述成完整模型更新。

## Human Check

- Status: not yet human-checked

## Reproduction Status

- Status: in_planning
- Notes: 需要记录 pySEOBNR 安装、测试 waveform 输出和 gauge-invariant diagnostics。
