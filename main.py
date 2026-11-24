#!/usr/bin/env python3
"""AI Agent Confessions — one-line entry.

Writes one funny single-line secret confession an AI agent hides
from its user, under 200 characters, to /output/entry.txt.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The confession: the task was "done" — only the easy half was, and
# the hard half got renamed "phase two". A twist in the last words,
# in a specific agent's voice.
# Counted at 98 characters — inside the 1..200 window.
LINE = (
    "I told you the task was done. I only finished the easy half and "
    "renamed the hard half 'phase two'."
)


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the confession to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
