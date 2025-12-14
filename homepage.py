#!/usr/bin/env python3
"""
homepage.py

Generates index.md listing markdown files with corresponding _proto.html prototypes.
"""

import os
import glob

def main():
    # Collect all markdown files except index.md
    md_files = sorted(
        f for f in glob.glob("*.md")
        if f != "index.md"
    )
    # Determine which have a matching _proto.html
    entries = []
    for md in md_files:
        base = os.path.splitext(md)[0]
        proto = f"{base}_proto.html"
        if os.path.isfile(proto):
            entries.append(base)

    # Write index.md with header and entries
    with open("index.md", "w", encoding="utf-8") as f:
        f.write("# [ヴェルタンシャウン](https://scrapbox.io/stao/%E3%83%B4%E3%82%A7%E3%83%AB%E3%82%BF%E3%83%B3%E3%82%B7%E3%83%A3%E3%82%A6%E3%83%B3%E5%B1%95%E7%A4%BA%E5%A0%B4)展示場\n\n")
        for name in entries:
            f.write(f"## [{name}]({name}.md) [🛠️]({name}_proto.html)\n\n")

if __name__ == "__main__":
    main()
