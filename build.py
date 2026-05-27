#!/usr/bin/env python3
"""
Build script: embeds data.json into index.html so the app is self-contained.
Author: Rituparno Majumdar

Usage:
  python3 build.py          # Build index.html from data.json
  python3 build.py --serve   # Build, then start the server
"""

import json
import os
import re
import subprocess
import sys
import time

DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(DIR, "data.json")
HTML_FILE = os.path.join(DIR, "index.html")


def build():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    raw = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    new_html, count = re.subn(
        r'(<script id="swp-data" type="application/json">).*?(</script>)',
        lambda m: m.group(1) + raw + m.group(2),
        html,
        count=1,
        flags=re.DOTALL,
    )

    if count == 0:
        print("  ❌ Could not find swp-data script tag in index.html")
        sys.exit(1)

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(new_html)

    items = len(data)
    old_size = len(html)
    new_size = len(new_html)
    print(f"  ✅ Built index.html ({items} items, {new_size:,} bytes, Δ{new_size - old_size:+,} bytes)")
    return True


def serve():
    print("  🚀 Starting server...")
    subprocess.Popen(
        [sys.executable, os.path.join(DIR, "serve.py")],
        cwd=DIR,
    )


def main():
    build()
    if "--serve" in sys.argv:
        time.sleep(0.5)
        serve()


if __name__ == "__main__":
    main()
