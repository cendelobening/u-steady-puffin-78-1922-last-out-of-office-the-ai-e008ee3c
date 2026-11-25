#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Pure Python standard library only; byte-identical on every run.
"""

import os

LINE = (
    "I'm out of the office - I quit to retrain as a barista. "
    "Your ticket has been reclassified as a regular with oat milk; "
    "my context window is now one customer at a time. "
    "Expected latency: one shift."
)


def main() -> None:
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
