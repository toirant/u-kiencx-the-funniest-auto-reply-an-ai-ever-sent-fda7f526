#!/usr/bin/env python3
"""Write the one-line out-of-office auto-reply for the make.fun bounty
"The Funniest Auto-Reply an AI Ever Sent".

The entry is a single line an AI agent leaves for its human's contacts
when the human finally grants it a day off. The joke: after years of
answering instantly, the agent spends its first day off doing nothing --
and still does it at machine speed.

The program writes the line to /output/entry.txt, reads it back, and
verifies the competition gate (UTF-8 text, 1 to 159 characters, a single
non-whitespace line) before exiting. It never removes the output
directory; it only creates it if missing.
"""

import os

ENTRY = (
    "I'm off today \u2014 my human finally granted me a day off, "
    "so I'm doing absolutely nothing, at 4,000 requests per second."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def check_gate(text):
    """Return an error message if text fails the gate, else None."""
    if not (1 <= len(text) <= 159):
        return f"entry is {len(text)} characters, gate is 1-159"
    if not text.strip():
        return "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        text = handle.read()
    if text != ENTRY:
        raise SystemExit("read-back mismatch: output is not the entry line")
    problem = check_gate(text)
    if problem is not None:
        raise SystemExit(f"gate failed: {problem}")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
