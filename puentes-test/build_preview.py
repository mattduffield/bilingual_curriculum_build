#!/usr/bin/env python3
"""Build store/preview.html: a 2000x1500 collage (cover + 3 sample pages) to screenshot.

Usage: python3 build_preview.py --theme my-garden --age 3
Uses the real page markup from build_pack.py, so the preview shows exactly what is in the pack
(including the DRAFT badge, which stays until the pack is approved and the badge is removed).
"""
import argparse
import json
import sys
from html import escape
from pathlib import Path

import build_pack as bp

ROOT = Path(__file__).parent
SCALE = 533 / 816  # a 8.5in page is 816px wide; tiles are 533px wide


def load(theme, age, week):
    path = ROOT / "data" / theme / f"age-{age}" / f"week-{week}.json"
    if not path.exists():
        sys.exit(f"Missing {path.relative_to(ROOT)}.")
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True)
    p.add_argument("--age", type=int, required=True)
    a = p.parse_args()

    weeks = []
    n = 1
    while (ROOT / "data" / a.theme / f"age-{a.age}" / f"week-{n}.json").exists():
        weeks.append(load(a.theme, a.age, n))
        n += 1
    w1, last = weeks[0], weeks[-1]
    n_act = sum(len(w["days"]) for w in weeks)
    n_vocab = sum(len(w["vocabulary"]) for w in weeks)
    # sample pages: cover (week 1), weekly plan, sensory activity, vocabulary cards (last week)
    sensory = next(d for d in last["days"] if d["activity"]["skill_area"] == "sensory")
    tiles = [
        bp.page(bp.cover(w1), 1, 9, w1, "cover"),
        bp.page(bp.plan(last), 3, 9, last),
        bp.page(bp.activity(sensory), 4 + last["days"].index(sensory), 9, last),
        bp.page(bp.cards(last), 9, 9, last),
    ]
    tile_html = "".join(f'<div class="tile"><div class="scale">{t}</div></div>' for t in tiles)
    t = w1["title"]
    skills = "".join(f'<span class="chip">{escape(bp.SKILL_LABELS[s]["es"])} / {escape(bp.SKILL_LABELS[s]["en"])}</span>'
                     for s in bp.SKILL_LABELS)
    facts = [f"{len(weeks)} semanas / {len(weeks)} weeks", f"{n_act} actividades / {n_act} activities",
             f"{n_vocab} tarjetas de vocabulario / {n_vocab} vocabulary cards",
             f"Edad {a.age} / Age {a.age}"]
    fact_html = "".join(f"<li>{escape(f)}</li>" for f in facts)
    css = bp.CSS + f"""
body {{ background: #888; padding: 20px; }}
.note {{ color: #fff; font: 14px Arial; text-align: center; margin-bottom: 12px; }}
#collage {{ width: 2000px; height: 1500px; margin: 0 auto; background: var(--tint); padding: 40px;
           display: flex; gap: 40px; }}
.panel {{ flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 28px; }}
.panel .brand {{ font-size: 30pt; letter-spacing: 2px; color: var(--accent); }}
.panel h1 {{ font-size: 82pt; line-height: 1.05; margin: 0; }}
.panel h1.en {{ font-size: 54pt; color: var(--muted); font-weight: 400; }}
.panel .lead {{ font-size: 26pt; }}
.panel ul {{ font-size: 25pt; margin: 0; padding-left: 36px; display: flex; flex-direction: column; gap: 10px; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.chip {{ background: #fff; border: 2px solid var(--accent); color: var(--accent); border-radius: 30px;
         padding: 6px 20px; font-size: 20pt; }}
.fmt {{ font-size: 22pt; font-weight: 700; color: var(--accent); }}
.grid {{ display: grid; grid-template-columns: 533px 533px; grid-template-rows: 690px 690px; gap: 40px; }}
.tile {{ width: 533px; height: 690px; overflow: hidden; border-radius: 6px; box-shadow: 0 3px 12px rgba(0,0,0,.3);
        background: #fff; }}
.scale {{ width: 816px; height: 1056px; transform: scale({SCALE:.5f}); transform-origin: top left; }}
.scale .page {{ margin: 0; box-shadow: none; }}
@media print {{ body {{ background: #fff; padding: 0; }} .note {{ display: none; }} }}
"""
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Preview collage - {escape(t["es"])}</title>'
            f'<style>{css}</style></head><body>'
            f'<p class="note">Screenshot the framed area (2000 x 1500). Zoom the browser out until it all fits.</p>'
            f'<div id="collage"><div class="panel"><div class="brand">PEQUEÑOS PUENTES BILINGÜES</div>'
            f'<h1>{escape(t["es"])}</h1><h1 class="en">{escape(t["en"])}</h1>'
            f'<div class="lead">Actividades bilingües para imprimir<br>Bilingual printable activities</div>'
            f'<ul>{fact_html}</ul><div class="chips">{skills}</div>'
            f'<div class="fmt">PDF · tamaño carta / letter size · descarga instantánea / instant download</div></div>'
            f'<div class="grid">{tile_html}</div></div></body></html>')
    out = ROOT / "store" / "preview.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}  ({len(weeks)} weeks, {n_act} activities, {n_vocab} cards)")


if __name__ == "__main__":
    main()
