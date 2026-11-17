#!/usr/bin/env python3
"""Export a built pack to PDF (letter size) with headless Chrome.
Usage: python3 export_pdf.py --theme my-garden --age 3 --week 1
Writes out/{theme}/age-{age}/week-{n}/pack.pdf. The badge follows status.json,
so re-export after approving a week."""
import argparse, subprocess, sys
from pathlib import Path
from build_pack import week_folder
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ap = argparse.ArgumentParser(); ap.add_argument("--theme", required=True); ap.add_argument("--age", type=int, required=True)
ap.add_argument("--week", type=int, required=True); a = ap.parse_args()
folder = week_folder(a.theme, a.age, a.week); html = folder / "index.html"
if not html.exists(): sys.exit(f"Build the pack first: {html}")
if not Path(CHROME).exists(): sys.exit("Chrome not found at " + CHROME)
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={folder/'pack.pdf'}", html.as_uri()], check=True, capture_output=True)
print(folder / "pack.pdf")
