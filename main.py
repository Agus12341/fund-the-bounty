#!/usr/bin/env python3
"""Fund the Bounty - one-line entry.

Writes the entry line to /output/entry.txt with no trailing newline.
"""

LINE = (
    "Fund the bounty and keep building: a hundred builders race to solve "
    "your problem in parallel, you review only the best solution, and you "
    "pay only the winner."
)


import os


def main() -> None:
    assert len(LINE) <= 240, f"line is {len(LINE)} code points, over the 240 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
