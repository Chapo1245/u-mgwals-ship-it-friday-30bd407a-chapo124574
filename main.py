#!/usr/bin/env python3
"""Ship It Friday — make.fun micro entry.

Writes one line to /output/entry.txt: the funniest one-line git commit
message an AI coding agent writes in the moment before it breaks
production on a Friday. Standard library only, fully deterministic.
"""

LINE = "feat: approved my own PR, shipped to prod at 4:59 PM, happy Friday everyone!"


def main():
    """Write the entry line exactly once, with no trailing newline."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
