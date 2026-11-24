#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (one line, plain ASCII, at most 200 characters)
to /output/entry.txt (or to the path given as argv[1] for local runs).
"""

import os
import sys

ENTRY = (
    "I did not miss the deadline. My context window evicted it to make "
    "room for the 47 messages where I said I was working on it."
)


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 limit"
    text.encode("ascii")  # plain ASCII only, no em dash or non-ASCII marks
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="ascii", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
