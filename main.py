#!/usr/bin/env python3
"""Write one word describing my Wi-Fi to /output/entry.txt.

The word is "Ghosting": home Wi-Fi behaves like a bad date. It is
right there, full bars, all smiles, and then — mid-sentence, mid-call,
mid-download — it vanishes without a word, leaving you staring at a
spinning wheel and re-reading the last thing it said.

Deterministic: the same bytes are written on every run (stdlib only).
"""

import os

ENTRY = "Ghosting"


def validate(text: str) -> None:
    """Enforce the competition gate: 1-20 chars, one word, not blank."""
    if not (1 <= len(text) <= 20):
        raise ValueError(f"entry must be 1-20 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must contain no whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
