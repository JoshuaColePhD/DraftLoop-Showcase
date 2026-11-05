# DraftLoop

**Rubric feedback that gives a student a concrete next revision.**

DraftLoop helps AP English Language students develop an argument and decide what to improve next. Students inspect a six-point rubric snapshot, consider a suggested revision, and discuss the feedback with a teacher. It is a formative coaching prototype; scores still need human judgment.

[See the product walkthrough](docs/WALKTHROUGH.md) · [Read the engineering case study](docs/CASE_STUDY.md) · [Recalculate the recorded results](docs/REPRODUCING.md)

<a href="demo/assets/local-coach-demo.gif"><img src="demo/assets/local-coach-demo.gif" alt="Current DraftLoop React workspace showing synthetic writing, simulated coaching, and progress" width="640"></a>

*Current React interface, recorded November 5, 2026. Original synthetic writing with clearly labeled simulated feedback; no model calls. Displayed scores are interface examples and are excluded from evaluation. [Recording details](demo/RECORDING.md).*

## What I built

- A Python/FastAPI backend combining model feedback with explicit scoring and review rules.
- A writing workspace connecting thesis, evidence, and sophistication feedback to a next revision, with SQLite storage for classroom feedback.
- An evaluation runner comparing scores with human readers, checking the expected model, and preserving previous reports when a run fails.

## Engineering decisions

**Measure completeness and accuracy separately.** In a three-essay experiment, an 80-token response limit truncated feedback before the rubric fields appeared. Requiring structured fields and raising the limit to 512 tokens recovered complete responses; exact score agreement remained 0%. The repair exposed a separate scoring problem. [Failure analysis](docs/CASE_STUDY.md)

## Results

| Recorded sample result | Original | Fixed |
| --- | ---: | ---: |
| Complete scoring responses | 0/3 | 3/3 |
| Exact score agreement | 0% | 0% |
| Agreement within one point | 33.3% | 33.3% |

Three examples cannot establish scoring reliability. The [case study](docs/CASE_STUDY.md) shows each score, explains the failed responses and repair, and identifies the remaining scoring limitations.

## How it works

Essay and prompt → model feedback → Python scoring rules → rubric score, revision guidance, and review reasons.

Python checks the model feedback and computes the score. [Architecture and responsibility](docs/CASE_STUDY.md#architecture-and-responsibility).

## Explore further

The [product walkthrough](docs/WALKTHROUGH.md) is readable here on GitHub. The [reproduction guide](docs/REPRODUCING.md) explains how to recalculate the recorded metrics locally with no API key or paid service.

This showcase includes recorded results and standalone analysis tools. The complete scoring application remains private. Released essay text is not redistributed; the [source manifest](data/source-manifest.json) identifies the reference material.

Built by [Joshua Cole, PhD](https://github.com/JoshuaColePhD) with AI-assisted development. [Ownership and development approach](docs/CASE_STUDY.md#ownership-and-development-approach) · [Evaluation-only license](LICENSE).
