#!/usr/bin/env python3
"""The Printer Apology — make.fun entry (program/v1).

Writes one apology line from an office printer to /output/entry.txt.
Deterministic, no network, no input: the same line every run.
"""

import os

ENTRY = "I'm sorry I printed your salary spreadsheet 40 times. In colour. HR sends its regards."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
