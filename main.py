"""Write one warm line about a small good thing today to /output/entry.txt.

The line: a neighbour's cat who hates everyone chose my lap this morning
and purred like a broken engine finally starting. Warm, surprising, one
concrete detail, fresh wording. Stdlib only, no network, deterministic:
the same bytes on every run. The entry must be 1-200 characters.
"""

import os

LINE = (
    "My neighbour's cat, who hates everyone, chose my lap this morning "
    "and purred like a broken engine finally starting."
)

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
# The line is 115 characters, well inside the 200-character limit.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
