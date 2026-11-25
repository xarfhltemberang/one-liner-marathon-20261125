#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single original one-line joke to /output/entry.txt."""

import os

JOKE = (
    "My smoke detector beeps every 47 minutes to remind me it exists, which "
    "is the same rate my landlord texts \"just checking in\" after I ask him "
    "to fix the sink."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
