# DraftLoop: from feedback to a next revision

This is a recorded walkthrough of the actual local writing coach. The original synthetic draft has **no human reference score**. The displayed 5/6 is unvalidated and excluded from the three-essay evaluation.

![Actual DraftLoop interface showing the original synthetic selfie draft, rubric rows, and a suggested revision](../demo/assets/local-coach.jpg)

Captured November 4, 2026 with local Ollama `llama3.2:3b`. No student writing or released AP essay text appears in this screenshot. The displayed 3–6 range is a heuristic, not a calibrated confidence interval.

## 1. Draft an argument

The writer responds to “What is the value of a selfie?” with a claim about preserving shared memories, a graduation example, and a qualification about distracting comparisons. The [original synthetic draft and capture details](../data/synthetic-walkthrough.json) are available for inspection.

## 2. Inspect the rubric feedback

The recorded interface shows thesis 1/1, evidence/commentary 3/4, and sophistication 1/1. These values combine a model proposal with local Python rules. They help illustrate the interface; they do not establish the draft's correct score.

## 3. Decide on a revision

The coach focuses on the line of reasoning and suggests: “This paragraph argues that selfies can record who was present and how they felt at a specific time.” A writer should decide whether that sentence adds reasoning or simply repeats the paragraph before using it. Human judgment remains part of the workflow.

[Read the separate scoring failure case study](CASE_STUDY.md) to see why complete model output did not improve score agreement. To explore the keyboard-accessible HTML version locally, follow [the walkthrough instructions](REPRODUCING.md#2-view-the-product-walkthrough). It makes no model calls and requires no API key.
