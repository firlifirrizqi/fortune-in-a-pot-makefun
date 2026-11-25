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

# Safety cap on the encoded payload so a future entry can never
# silently balloon past what the grader will read.
MAX_BYTES = 256

# Characters the entry is allowed to contain: printable ASCII plus
# the curly apostrophe used in "you'll". Anything else (control
# characters, stray unicode) must fail loudly instead of being
# written out.
ALLOWED_CHARS = set(
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    " .,;:!?-'’"
)


def validate_characters(text: str) -> None:
    """Reject any character outside the allowed set, including control chars."""
    for i, ch in enumerate(text):
        if ch in ALLOWED_CHARS:
            continue
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"control character at position {i}: U+{ord(ch):04X}")
        raise ValueError(f"disallowed character at position {i}: {ch!r}")
    encoded = text.encode("utf-8")
    if len(encoded) > MAX_BYTES:
        raise ValueError(f"entry is {len(encoded)} bytes, over the {MAX_BYTES} cap")


def normalize_entry(text: str) -> str:
    """Lightly normalize the entry before it is written.

    Strips leading/trailing whitespace, collapses any accidental
    double spaces left by line joins, and guarantees the result is
    still a single line within the character limit. The selected
    line is already clean, so this is a no-op for it — but any
    future edit to ENTRY passes through the same gate.
    """
    cleaned = " ".join(text.strip().split())
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not (1 <= len(cleaned) <= MAX_CHARS):
        raise ValueError(
            f"entry length {len(cleaned)} out of range 1-{MAX_CHARS}"
        )
    return cleaned


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
    output_dir = os.path.dirname(OUTPUT_PATH)
    if not output_dir:
        raise ValueError("OUTPUT_PATH must include a directory")
    if os.path.exists(OUTPUT_PATH) and os.path.isdir(OUTPUT_PATH):
        raise ValueError(f"{OUTPUT_PATH} is a directory, not a file")
    if os.path.islink(OUTPUT_PATH):
        raise ValueError(f"{OUTPUT_PATH} must not be a symlink")
    text = normalize_entry(ENTRY)
    validate_characters(text)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    verify()


if __name__ == "__main__":
    main()
