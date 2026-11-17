#!/usr/bin/env python3
"""Build store/preview.html: a 2x2 collage (cover + 3 sample pages) to screenshot.
Uses the real pack pages, so the BORRADOR / DRAFT badge shows until the week is approved.
Usage: python3 build_preview.py --theme my-garden --age 3 --week 2"""
import argparse, json
import build_pack as b

ap = argparse.ArgumentParser(); ap.add_argument("--theme", required=True); ap.add_argument("--age", type=int, required=True)
ap.add_argument("--week", type=int, default=2); a = ap.parse_args()
p = json.loads((b.ROOT / "data" / a.theme / f"age-{a.age}" / f"week-{a.week}.json").read_text(encoding="utf-8")); p["theme_slug"] = a.theme
b.SHOW_DRAFT = b.read_status(b.week_folder(a.theme, a.age, a.week))["status"] != "approved"
by_skill = {d["activity"]["skill_area"]["key"]: d for d in p["days"]}
pages = [b.cover(p), b.activity(by_skill["math"]), b.activity(by_skill["art"]), b.vocab(p)]
css = b.CSS + """
body{background:#f4f1ea}
.canvas{width:1500px;height:2000px;margin:0 auto;padding:40px;display:flex;flex-direction:column;gap:30px;background:#f4f1ea}
.bar{text-align:center;color:#3d6b4a;font-family:"Helvetica Neue",Arial,sans-serif}
.bar b{display:block;font-size:46px;color:#2b2b2b}.bar span{font-size:26px}
.grid{display:grid;grid-template-columns:648px 648px;gap:60px;justify-content:center}
.slot{width:648px;height:864px;box-shadow:0 6px 22px rgba(0,0,0,.18);background:#fff}
.slot .page{transform:scale(.9);transform-origin:top left;margin:0}
"""
bar = f'<div class="bar"><b>Mi huerto · My Garden</b><span>Pequeños Puentes Bilingües · Edad {a.age} · Age {a.age}</span></div>'
html = f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Preview</title><style>{css}</style></head><body><div class="canvas">{bar}<div class="grid">' + "".join(f'<div class="slot">{x}</div>' for x in pages) + '</div></div></body></html>'
out = b.ROOT / "store" / "preview.html"; out.write_text(html, encoding="utf-8"); print(out)
