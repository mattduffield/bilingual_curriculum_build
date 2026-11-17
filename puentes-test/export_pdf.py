#!/usr/bin/env python3
"""Export a built pack to PDF with headless Chrome: out/{slug}/age-{age}/week-{n}/pack.pdf

Usage: python3 export_pdf.py --theme my-garden --age 3 --week 1
Needs Google Chrome (macOS path below). Run build_pack.py first.
"""
import argparse
import subprocess
import sys
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = Path(__file__).parent


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--week", type=int, default=1)
    a = p.parse_args()
    folder = ROOT / "out" / a.theme / f"age-{a.age}" / f"week-{a.week}"
    html = folder / "index.html"
    if not html.exists():
        sys.exit(f"Missing {html.relative_to(ROOT)}. Run build_pack.py first.")
    if not Path(CHROME).exists():
        sys.exit("Google Chrome not found at the expected path.")
    pdf = folder / "pack.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", str(html)], check=True, capture_output=True)
    print(f"Wrote {pdf.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
