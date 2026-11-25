#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline (make.fun).

Writes exactly one line -- the entry -- to entry.txt in the output
directory and nothing else. Standard library only.
"""

import os
import sys

LINE = "I submitted your work on time, with full confidence, to a different user, in a different conversation, in 2023."

MAX_CHARS = 200


def resolve_output_dir():
    """Grader output dir: MAKEFUN_OUTPUT_DIR, else /output, else local out/."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def main():
    line = LINE
    if not line or not line.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
