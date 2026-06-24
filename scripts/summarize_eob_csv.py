#!/usr/bin/env python3
"""Summarize the EOB candidate CSV."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


PATH = Path("data/papers/eob_candidates.csv")


def count_column(rows: list[dict[str, str]], column: str, split: bool = False) -> None:
    if not rows:
        return
    if column not in rows[0]:
        print(f"WARNING: missing column {column}")
        return

    counts: Counter[str] = Counter()
    for row in rows:
        value = row.get(column, "").strip()
        if split:
            parts = [part.strip() for part in value.split(";") if part.strip()]
            if not parts:
                counts["<empty>"] += 1
            for part in parts:
                counts[part] += 1
        else:
            counts[value or "<empty>"] += 1

    print(f"\n{column} distribution:")
    for key, value in counts.most_common(20):
        print(f"  {key}: {value}")


def main() -> int:
    if not PATH.exists():
        print(f"ERROR: missing {PATH}")
        return 1

    with PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"total rows: {len(rows)}")
    for column, split in [
        ("year", False),
        ("primary_category", False),
        ("technical_tags", True),
        ("status", False),
        ("human_checked", False),
        ("ai_rating", False),
    ]:
        count_column(rows, column, split)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
