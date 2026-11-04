"""Extract released AP argument samples from a locally downloaded source PDF."""

import argparse
import json
import re
import subprocess
from pathlib import Path

SOURCE = "https://apcentral.collegeboard.org/media/pdf/ap25-apc-english-language-q3-set-1.pdf"
OUTPUT = Path("data/ap-2025-q3-set-1.local.json")
# Published reader scores in the scoring commentary (Rows A/B/C).
ROWS = {"3A": (1, 4, 1), "3B": (1, 3, 0), "3C": (1, 1, 0)}


def prepare(pdf: Path, output: Path) -> None:
    text = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
    prompt = re.search(
        r"In a 2022 interview with People magazine.*?(?=In your response you should)",
        text,
        re.DOTALL,
    )
    if prompt is None:
        raise ValueError("Expected the 2025 AP English Language Q3 Set 1 PDF.")
    essays: dict[str, list[str]] = {}
    for page in text.split("\f"):
        match = re.match(r"\s*Sample (3[A-C]) \((\d+) of \d+\)[^\n]*\n", page)
        if not match:
            continue
        label, page_number = match.groups()
        body = page[match.end() :].strip("\n")
        # Preserve paragraph indents without treating wrapped PDF lines as paragraphs.
        body = re.sub(r"\n(?= {2,}\S)", "\n\n", body)
        paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", body)]
        content = "\n\n".join(p for p in paragraphs if p)
        chunks = essays.setdefault(label, [])
        if int(page_number) != len(chunks) + 1 or not content:
            raise ValueError(
                f"Missing or unreadable sample page: {label} {page_number}"
            )
        chunks.append(content)

    if {key: len(value) for key, value in essays.items()} != {
        "3A": 2,
        "3B": 1,
        "3C": 1,
    }:
        raise ValueError("Expected four essay pages across samples 3A, 3B, and 3C.")
    records = [
        {
            "id": label,
            "source_url": SOURCE,
            "prompt": " ".join(prompt.group().split()),
            "essay": " ".join(essays[label]),
            "human_score": sum(rows),
        }
        for label, rows in ROWS.items()
    ]
    output.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    prepare(args.pdf, args.output)
