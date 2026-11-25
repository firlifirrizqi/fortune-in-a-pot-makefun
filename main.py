"""Fortune in a Pot entry for Make.fun.

Writes a single fortune for a houseplant on the windowsill,
at most 120 characters, to /output/entry.txt.
Standard library only; nothing to install.
"""

import os

ENTRY = (
    "Soon you'll sprout a brand-new leaf, and the whole windowsill "
    "will pretend it saw it coming. It didn't."
)

OUTPUT_PATH = "/output/entry.txt"

# Competition gate: a single line, at most 120 characters.
MAX_CHARS = 120


def verify() -> None:
    """Re-read the output and assert it is byte-identical to ENTRY."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY, "output differs from ENTRY"
    assert content.encode("utf-8").decode("utf-8") == content
    assert 1 <= len(content) <= MAX_CHARS, (
        f"length {len(content)} out of range 1-{MAX_CHARS}"
    )
    assert content.strip(), "entry is only whitespace"
    assert "\n" not in content, "entry must be a single line"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify()


if __name__ == "__main__":
    main()
