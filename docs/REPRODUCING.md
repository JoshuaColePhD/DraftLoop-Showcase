# Reproduce the evidence locally

## 1. Recalculate the recorded metrics

Python 3.12+ is the only dependency. From this repository:

```bash
python3 scripts/reanalyze.py
python3 -m unittest discover -s tests
```

The script reads numeric score pairs and completeness flags from `data/recorded-results.json`. It uses only the Python standard library; no network, model, private repository, or API key is involved. It prints completeness, review counts, exact agreement, adjacent agreement, quadratic weighted kappa, and Pearson correlation for both runs.

Exact agreement counts identical totals. Adjacent agreement includes identical totals and differences of one point. Kappa compares observed squared score distances with the distances expected from the two empirical score distributions. Pearson correlation is undefined if either score series has zero variance; undefined statistics remain `None`, never fabricated zeros.

This reproduces the arithmetic for the **recorded** results. It does not independently recreate the original model calls or prove the scores were correct.

## 2. View the product walkthrough

```bash
python3 -m http.server 8766 --bind 127.0.0.1
```

Open <http://127.0.0.1:8766/demo/>. The walkthrough works offline and makes no API calls. Native disclosure controls explain the steps; the screenshot and text transcript remain readable without JavaScript.

The image was captured from the actual local FastAPI/standalone-coach UI on November 4, 2026 after local Ollama inference on the original synthetic draft in `data/synthetic-walkthrough.json`. It is a recorded product demonstration, not an interactive scorer, an AP evaluation sample, or a human-validated result. The current local model digest is recorded for this screenshot only; it is not retroactively attributed to the November 3 experiment.

## 3. Check the reference material

`data/source-manifest.json` identifies College Board's released 2025 AP English Language Question 3, Set 1 document and human row scores for 3A, 3B, and 3C. Visit the official source to inspect its essays and commentary. This repository intentionally includes no released essay or prompt text.

To recreate the original prepared local input, download that PDF and install Poppler's `pdftotext`, then:

```bash
curl -fL 'https://apcentral.collegeboard.org/media/pdf/ap25-apc-english-language-q3-set-1.pdf' -o /tmp/draftloop-ap-samples.pdf
python3 scripts/prepare_ap_sample.py /tmp/draftloop-ap-samples.pdf --output /tmp/draftloop-samples.local.json
shasum -a 256 /tmp/draftloop-samples.local.json
```

On November 4, 2026, the included preparation script reproduced the recorded checksum from the official PDF. This verifies source preparation, not model inference.

The recorded prepared-input checksum is `c813ca58d07f1adc351fffad98fa7e1cb286d0568cf5e824531b557b63862223`. PDF updates or extraction-version differences can change the bytes; a mismatch is a different input, not a matched reproduction. Local extracts are excluded by `.gitignore`. Do not commit them.

## End-to-end inference boundary

The full app, prompt templates, and scoring rules remain private under an evaluation-only license. This showcase does not imply that raw model output alone reproduces the recorded system scores. An authorized reviewer with the application can run local Ollama `llama3.2:3b`, the app in `CLASS_25` mode, and its evaluator with `--expected-provider ollama --expected-model llama3.2:3b --expected-mode CLASS_25`. No hosted model calls are required. Full inference reproduction requires that implementation; understanding and recalculating this case study does not.
