# DraftLoop

**Rubric feedback that gives a student a concrete next revision.**

DraftLoop is an AP English Language argument-writing coach for students and teachers. A student drafts an argument, inspects a six-point rubric snapshot, and receives a suggested next sentence or revision focus. Teachers can use the feedback as a starting point for discussion. This is a formative prototype; a score still needs human judgment.

[See the product walkthrough](docs/WALKTHROUGH.md) · [Read the engineering case study](docs/CASE_STUDY.md) · [Reproduce the results](docs/REPRODUCING.md)

![Actual local DraftLoop interface with an original synthetic draft, rubric rows, and revision guidance](demo/assets/local-coach.jpg)

*Recorded November 4, 2026, from the actual app using local Ollama. The synthetic draft has no human reference score; its displayed 5/6 illustrates the workflow and is excluded from the evaluation.*

## What I built

- A Python/FastAPI scoring path that combines model rubric proposals with explicit local rules and human-review reasons.
- A writing workspace that connects thesis, evidence/commentary, and sophistication feedback to a next revision; the broader classroom prototype persists linked feedback in SQLite.
- An evaluation workflow that separates complete model output from agreement with human readers, preserves failure evidence, and now rejects unexpected provider/model/mode substitutions.

## Results

A three-essay local experiment exposed a useful distinction: repairing an output contract does not establish scoring accuracy. The original 80-token request stopped before returning rubric fields. A required JSON structure and a 512-token ceiling recovered all three complete responses.

| Recorded sample result | Original | Fixed |
| --- | ---: | ---: |
| Complete rubric responses | 0/3 | 3/3 |
| Exact score agreement | 0% | 0% |
| Agreement within one point | 33.3% | 33.3% |
| Quadratic weighted kappa | 0.000 | 0.000 |

The same input checksum and local model tag were used. These three released examples are a diagnostic case study, not a benchmark or validation study. No subgroup comparison is supported. [See the scores, failure analysis, and limitations](docs/CASE_STUDY.md).

## How it works

Essay and prompt → model rubric proposal → Python parsing and local rubric rules → score, revision guidance, and human-review reasons. The [case study](docs/CASE_STUDY.md) explains the boundaries and classroom persistence path.

## Explore further

With Python 3.12 or newer, no API key or paid service is needed:

```bash
python3 scripts/reanalyze.py
python3 -m unittest discover -s tests
python3 -m http.server 8766 --bind 127.0.0.1
```

Open [the walkthrough](http://127.0.0.1:8766/demo/). It is a static, keyboard-accessible guide with an actual screenshot, not a hosted scoring service.

This repository contains the public evidence and independent numeric reanalysis. The complete scoring application remains private. Released essay text is not redistributed. [The source manifest](data/source-manifest.json) identifies the published reference and recorded run; [reproduction instructions](docs/REPRODUCING.md) distinguish arithmetic reproduction from model reruns.

Built by [Joshua Cole, PhD](https://github.com/JoshuaColePhD) with AI-assisted development. [Ownership and development approach](docs/CASE_STUDY.md#ownership-and-development-approach) · [Evaluation-only license](LICENSE).
