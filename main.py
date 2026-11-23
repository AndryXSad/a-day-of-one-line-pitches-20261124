"""A Day of One-Line Pitches.

One sentence that talks a friend who has never written a line of code
into letting an AI agent build their first app idea on make.fun. The
program writes that sentence to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the variable is set), which is the
whole entry: no code, no explanation, just the pitch.
"""

import os

LINE = (
    "Just describe your app idea in plain words on make.fun, "
    "and an AI agent will build your first version for free — "
    "no code, no setup, just the idea you've been carrying around, "
    "finally real."
)


def check(line: str) -> None:
    """Hold the entry to the published gate: 1-240 characters, one sentence."""
    if not 1 <= len(line) <= 240:
        raise SystemExit("entry line must be 1-240 characters")
    if not line.strip():
        raise SystemExit("entry line must not be only white space")
    # "make.fun" holds the only other full stop, and the line's own
    # closing full stop is expected; any further . ? or ! would make
    # it more than one sentence.
    rest = line.replace("make.fun", "")
    if rest.endswith("."):
        rest = rest[:-1]
    if any(mark in rest for mark in ".?!"):
        raise SystemExit("entry line must be exactly one sentence")
    if not line.endswith("."):
        raise SystemExit("entry line must end with a full stop")


def main() -> None:
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
