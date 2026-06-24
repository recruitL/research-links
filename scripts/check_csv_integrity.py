#!/usr/bin/env python3
"""Check the EOB CSV data layer integrity."""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path


REQUIRED_COLUMNS = [
    "arxiv_id",
    "title",
    "authors",
    "year",
    "url",
    "pdf_url",
    "topic",
    "technical_tags",
    "status",
]


def main() -> int:
    path = Path("data/papers/eob_candidates.csv")
    errors: list[str] = []
    warnings: list[str] = []

    print("CSV integrity check")
    print(f"target: {path}")

    if not path.exists():
        print("ERROR: data/papers/eob_candidates.csv does not exist")
        return 1

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        columns = reader.fieldnames or []

    print(f"rows: {len(rows)}")
    print(f"columns: {len(columns)}")

    if len(rows) <= 400:
        errors.append(f"expected more than 400 rows, found {len(rows)}")

    missing = [col for col in REQUIRED_COLUMNS if col not in columns]
    if missing:
        errors.append("missing required columns: " + ", ".join(missing))

    ids = [row.get("arxiv_id", "").strip() for row in rows]
    empty_ids = sum(1 for item in ids if not item)
    if empty_ids:
        errors.append(f"empty arxiv_id rows: {empty_ids}")

    dupes = [item for item, count in Counter(ids).items() if item and count > 1]
    if dupes:
        errors.append("duplicate arxiv_id values: " + ", ".join(dupes[:10]))

    empty_title = sum(1 for row in rows if not row.get("title", "").strip())
    if empty_title:
        errors.append(f"empty title rows: {empty_title}")

    empty_url = sum(1 for row in rows if not row.get("url", "").strip())
    empty_pdf = sum(1 for row in rows if not row.get("pdf_url", "").strip())
    both_empty = sum(
        1
        for row in rows
        if not row.get("url", "").strip() and not row.get("pdf_url", "").strip()
    )
    print(f"empty url rows: {empty_url}")
    print(f"empty pdf_url rows: {empty_pdf}")
    if both_empty:
        errors.append(f"rows with both url and pdf_url empty: {both_empty}")

    empty_tags = sum(1 for row in rows if not row.get("technical_tags", "").strip())
    if empty_tags:
        warnings.append(f"rows with empty technical_tags: {empty_tags}")

    if warnings:
        print("WARNINGS:")
        for item in warnings:
            print(f"- {item}")

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
