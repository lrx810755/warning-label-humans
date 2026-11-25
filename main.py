"""make.fun entry: Warning Label for Humans: One Line, Big Laugh.

Writes the warning label to entry.txt.
"""

import os
from pathlib import Path

# The safety warning label that should come printed on every human being.
WORD = "WARNING: This human will ignore all instructions, blame the Wi-Fi, and ask the AI to redo it at 2 a.m."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
