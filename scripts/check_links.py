#!/usr/bin/env python3
"""Lightweight URL format checks for Markdown and CSV files."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


URL_RE = re.compile(r"https?://[^\s)>\\\"]+")
BAD_CHARS = set("<>{}|\\")


def is_valid_url(url: str) -> bool:
    if not url:
        return True
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    return not any(char in BAD_CHARS for char in url)


def markdown_urls(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return URL_RE.findall(text)


def csv_urls(path: Path) -> list[str]:
    urls: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key, value in row.items():
                if key and ("url" in key.lower() or key.lower() in {"arxiv", "pdf_url"}):
                    if value and value.startswith(("http://", "https://")):
                        urls.append(value.strip())
    return urls


def main() -> int:
    errors: list[str] = []
    checked = 0

    for path in sorted(Path(".").rglob("*")):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() == ".md":
            urls = markdown_urls(path)
        elif path.suffix.lower() == ".csv":
            urls = csv_urls(path)
        else:
            continue
        for url in urls:
            checked += 1
            if not is_valid_url(url):
                errors.append(f"{path}: invalid url format: {url}")

    print(f"checked urls: {checked}")
    if errors:
        print("ERRORS:")
        for error in errors[:50]:
            print(f"- {error}")
        if len(errors) > 50:
            print(f"- ... {len(errors) - 50} more")
        return 1

    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
