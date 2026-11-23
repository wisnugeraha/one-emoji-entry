#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji (at most 8 characters) to /output/entry.txt:
the emoji most likely to make a stranger smile.
"""
import os


MAX_EMOJI_CHARS = 8  # the gate's cap: one emoji, no room for a caption

EMOJI = "\U0001F604"


def emoji() -> str:
    """Return the single emoji."""
    return EMOJI


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = emoji().strip()
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) > MAX_EMOJI_CHARS:
        raise ValueError(f"emoji is {len(text)} chars (max {MAX_EMOJI_CHARS})")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # World-readable: the grader collects the file as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
