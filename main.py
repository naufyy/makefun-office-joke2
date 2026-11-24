#!/usr/bin/env python3
"""Entry for u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.

Writes one single-line joke about office life (at most 200 characters)
to /output/entry.txt. The setup is a concrete office detail; the
punchline pays it off in a way anyone who has sat in an office knows.
"""

from pathlib import Path

ENTRY = "I watered the office plant for three years before HR told me it's plastic. On reflection, so is my enthusiasm."

# The rules seal the entry at 1 to 200 characters, one line.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY


def main() -> None:
    out = Path("/output") / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
