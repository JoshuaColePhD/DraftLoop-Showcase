"""Recalculate recorded DraftLoop scores; no model calls or third-party packages."""

import json
import math
from pathlib import Path
from statistics import mean


def metrics(human: list[int], predicted: list[int]) -> dict[str, float | None]:
    """Use squared distances on the shared ordinal score scale for QWK."""
    if not human or len(human) != len(predicted):
        raise ValueError("Metrics require nonempty, aligned score lists.")
    n = len(human)
    distances = [abs(a - b) for a, b in zip(human, predicted, strict=True)]
    observed = mean(d**2 for d in distances)
    expected = sum((a - b) ** 2 for a in human for b in predicted) / n**2
    mean_h, mean_p = mean(human), mean(predicted)
    centered_h = [a - mean_h for a in human]
    centered_p = [b - mean_p for b in predicted]
    denominator = math.sqrt(
        sum(x * x for x in centered_h) * sum(y * y for y in centered_p)
    )
    return {
        "Quadratic weighted kappa": 1 - observed / expected if expected else None,
        "Exact agreement": sum(d == 0 for d in distances) / n,
        "Adjacent agreement (within one point, including exact)": sum(
            d <= 1 for d in distances
        )
        / n,
        "Pearson r": sum(x * y for x, y in zip(centered_h, centered_p, strict=True))
        / denominator
        if denominator
        else None,
    }


def load_record(path: Path) -> dict:
    record = json.loads(path.read_text())
    rows = record["rows"]
    if not rows or len({row["id"] for row in rows}) != len(rows):
        raise ValueError("Expected nonempty rows with unique sample IDs.")
    for row in rows:
        if any(
            type(row[key]) is not int or not 0 <= row[key] <= 6
            for key in ("human", "original", "fixed")
        ):
            raise ValueError("Scores must be integers on the 0–6 scale.")
        if any(
            type(row[key]) is not bool
            for key in (
                "original_complete",
                "fixed_complete",
                "original_review",
                "fixed_review",
            )
        ):
            raise ValueError("Completeness and review fields must be booleans.")
    return record


def summarize(record: dict, run: str) -> dict:
    rows = record["rows"]
    return {
        "samples": len(rows),
        "complete_rubrics": sum(row[f"{run}_complete"] for row in rows),
        "human_review_flags": sum(row[f"{run}_review"] for row in rows),
        **metrics([row["human"] for row in rows], [row[run] for row in rows]),
    }


def main() -> None:
    path = Path(__file__).resolve().parents[1] / "data" / "recorded-results.json"
    record = load_record(path)
    print("Recorded DraftLoop experiment — arithmetic reproduction, not new inference")
    print(
        f"Date: {record['recorded_date']}; model: {record['provider']}/{record['model']}; mode: {record['mode']}"
    )
    print(
        json.dumps(
            {run: summarize(record, run) for run in ("original", "fixed")}, indent=2
        )
    )


if __name__ == "__main__":
    main()
