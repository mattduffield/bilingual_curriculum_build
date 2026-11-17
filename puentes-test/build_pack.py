#!/usr/bin/env python3
"""Pequeños Puentes Bilingües - print pack builder.

Usage:
  python3 build_pack.py --theme my-garden --age 3 --week 1

Reads  data/{theme-slug}/age-{age}/week-{n}.json
Writes out/{theme-slug}/age-{age}/week-{n}/index.html

Letter size, @page margin 0.5in. Every page is exactly one printed page
(content area 7.5in x 10in, overflow hidden, page break after). DRAFT on every page.
"""
import argparse
import json
import math
import sys
from html import escape
from pathlib import Path

import dashboard
import status

ROOT = Path(__file__).parent

SKILL_LABELS = {
    "math": {"es": "matemáticas", "en": "math"},
    "language": {"es": "lenguaje", "en": "language"},
    "art": {"es": "arte", "en": "art"},
    "sensory": {"es": "sensorial", "en": "sensory"},
    "motor": {"es": "motricidad", "en": "motor"},
}

INSTRUCTIONS = [
    {"es": "Imprime en tamaño carta, al 100 %. No ajustes la escala.",
     "en": "Print on letter size at 100%. Do not scale to fit."},
    {"es": "Lee la actividad antes de empezar y prepara los materiales.",
     "en": "Read the activity first and gather the materials."},
    {"es": "Un adulto siempre está presente. Revisa el cuadro de supervisión.",
     "en": "An adult is always present. Check the supervision box."},
    {"es": "Habla en español primero y luego en inglés. Repite la frase \"Di esto\".",
     "en": "Speak Spanish first, then English. Repeat the \"Say this\" phrase."},
    {"es": "Para niños de 1 a 2 años, nada más pequeño que un tubo de papel higiénico.",
     "en": "For ages 1-2, nothing smaller than a toilet-paper tube."},
    {"es": "Sigue el ritmo de cada niño. Celebra los intentos, no solo los resultados.",
     "en": "Follow each child's pace. Celebrate the trying, not just the result."},
    {"es": "Recorta las tarjetas de vocabulario y dóblalas por la línea punteada.",
     "en": "Cut out the vocabulary cards and fold on the dotted line."},
]


def bi(d, cls=""):
    """Render a {es, en} pair side by side. Missing language is simply left out."""
    parts = [f'<div class="{k}">{escape(d[k])}</div>' for k in ("es", "en") if k in d]
    return f'<div class="bi {cls}">{"".join(parts)}</div>'


def theme_svg(slug):
    """One simple line drawing per theme. Falls back to a little bridge."""
    stroke = 'fill="none" stroke="#2f8f7b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
    if slug == "my-garden":
        cx, cy, r = 100, 70, 30
        petals = "".join(
            f'<circle cx="{cx + r * math.cos(math.radians(a)):.1f}" cy="{cy + r * math.sin(math.radians(a)):.1f}" r="19"/>'
            for a in range(-90, 270, 72))
        return (f'<svg viewBox="0 0 200 200" {stroke} role="img" aria-label="flower">'
                f'{petals}<circle cx="{cx}" cy="{cy}" r="13"/>'
                '<path d="M100 112 C98 140 104 160 100 186"/>'
                '<path d="M100 150 C80 140 66 142 58 130 C76 126 92 134 100 150"/>'
                '<path d="M101 164 C120 154 134 156 142 144 C124 140 108 148 101 164"/>'
                '<path d="M30 186 H170"/></svg>')
    return (f'<svg viewBox="0 0 200 200" {stroke} role="img" aria-label="bridge">'
            '<path d="M20 130 Q100 40 180 130"/><path d="M10 130 H190"/>'
            '<path d="M50 130 V100 M80 130 V80 M110 130 V77 M140 130 V100"/>'
            '<path d="M10 160 Q40 148 70 160 T130 160 T190 160"/></svg>')


CSS = """
@page { size: letter; margin: 0.5in; }
* { box-sizing: border-box; }
:root { --accent: #2f8f7b; --tint: #eaf5f2; --ink: #222; --muted: #666; }
html, body { margin: 0; padding: 0; }
body { font-family: "Avenir Next", "Trebuchet MS", Arial, sans-serif; color: var(--ink);
       font-size: 14pt; line-height: 1.35;
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { position: relative; width: 7.5in; height: 10in; overflow: hidden;
        display: flex; flex-direction: column; gap: 0.15in;
        break-after: page; page-break-after: always; }
.page:last-child { break-after: auto; page-break-after: auto; }
@media screen {
  body { background: #ddd; padding: 0.3in 0; }
  .page { background: #fff; margin: 0 auto 0.3in; padding: 0.5in; width: 8.5in; height: 11in;
          box-shadow: 0 2px 8px rgba(0,0,0,.25); }
}
.draft { position: absolute; top: 0; right: 0; border: 2px solid var(--accent); color: var(--accent);
         font-weight: 700; font-size: 10pt; letter-spacing: 1px; padding: 2px 8px; border-radius: 4px;
         background: #fff; }
.footer { margin-top: auto; font-size: 9pt; color: var(--muted); display: flex; justify-content: space-between;
          border-top: 1px solid #ddd; padding-top: 0.06in; flex: none; align-self: stretch; }
h1, h2, h3, p { margin: 0; }
h2 { font-size: 22pt; color: var(--accent); }
.page h2 { padding-right: 1.6in; }
.bi { display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; column-gap: 0.25in; }
.bi > div + div { border-left: 2px solid var(--tint); padding-left: 0.2in; }
.sub { font-size: 11pt; color: var(--muted); }
.box { border: 2px solid var(--accent); border-radius: 10px; padding: 0.1in 0.15in; flex: none; }
.box .label { font-size: 10pt; font-weight: 700; color: var(--accent); text-transform: uppercase;
              letter-spacing: 1px; margin-bottom: 2px; }
.tint { background: var(--tint); }

/* cover */
.cover { align-items: center; justify-content: center; text-align: center; gap: 0.25in; }
.cover .brand { font-size: 16pt; color: var(--accent); letter-spacing: 1px; }
.cover h1 { font-size: 46pt; line-height: 1.1; }
.cover h1.en { font-size: 34pt; color: var(--muted); font-weight: 400; }
.cover svg { width: 3.2in; height: 3.2in; }
.cover .age { font-size: 20pt; border: 2px solid var(--accent); border-radius: 30px; padding: 0.06in 0.3in; }

/* instructions + plan */
ol.rules { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.12in; }
ol.rules li { font-size: 13pt; }
table { width: 100%; border-collapse: collapse; font-size: 12pt; }
th { background: var(--tint); color: var(--accent); text-align: left; padding: 0.06in 0.1in; font-size: 10pt;
     text-transform: uppercase; letter-spacing: 1px; }
td { padding: 0.08in 0.1in; border-bottom: 1px solid #ddd; vertical-align: top; }
td .en, .small .en { color: var(--muted); }
ul.list { margin: 0; padding-left: 0.2in; font-size: 11pt; }
.two { display: grid; grid-template-columns: 1fr 1fr; column-gap: 0.25in; }

/* activity */
.act-head .skill { display: inline-block; background: var(--accent); color: #fff; border-radius: 20px;
                   padding: 2px 14px; font-size: 11pt; margin-right: 8px; }
.act-head h2 { font-size: 26pt; line-height: 1.15; }
.act-head h2 .en { color: var(--muted); font-size: 20pt; font-weight: 400; }
.steps { display: flex; flex-direction: column; gap: 0.08in; font-size: 15pt; }
.step { display: grid; grid-template-columns: 0.35in 1fr; align-items: start; }
.step .n { background: var(--accent); color: #fff; border-radius: 50%; width: 0.28in; height: 0.28in;
           font-size: 11pt; text-align: center; line-height: 0.28in; margin-top: 3px; }
.step .en { color: var(--muted); }
.say { font-size: 17pt; font-weight: 600; }
.say .en { color: var(--muted); font-weight: 400; }
.mat { font-size: 12pt; }
.draw { flex: 1 1 0; min-height: 0; border: 2px dashed var(--accent); border-radius: 12px; padding: 0.08in 0.15in;
        font-size: 10pt; color: var(--accent); font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }

/* cards */
.cards { flex: 1; display: grid; grid-template-columns: 1fr 1fr; grid-auto-rows: 1fr; gap: 0.12in; min-height: 0; }
.card { border: 1.5px solid #888; border-radius: 6px; display: grid; grid-template-columns: 1fr 1fr; }
.card div { display: flex; align-items: center; justify-content: center; text-align: center;
            font-size: 22pt; font-weight: 600; padding: 0.05in; }
.card div + div { border-left: 2px dotted var(--accent); color: var(--muted); font-weight: 400; }
"""


def is_draft(week):
    """DRAFT shows on every page unless this week's status.json says "approved"."""
    st = status.read_status(status.week_dir(week["theme_slug"], week["age"], week["week"]))
    return not (st and st["status"] == "approved")


def page(inner, n, total, week, extra_cls=""):
    title = week["title"]
    label = " / ".join(title[k] for k in ("es", "en") if k in title)
    badge = '<div class="draft">BORRADOR / DRAFT</div>' if is_draft(week) else ""
    return (f'<section class="page {extra_cls}">{badge}{inner}'
            f'<div class="footer"><span>Pequeños Puentes Bilingües · {escape(label)} · '
            f'{"Semana / Week"} {week["week"]}</span><span>{n} / {total}</span></div></section>')


def cover(week):
    t, slug = week["title"], week["theme_slug"]
    age = f'{week["age"]} años / {week["age"]} years' if "es" in t and "en" in t else str(week["age"])
    head = "".join(f'<h1 class="{k}">{escape(t[k])}</h1>' for k in ("es", "en") if k in t)
    return (f'<div class="brand">PEQUEÑOS PUENTES BILINGÜES</div>{head}{theme_svg(slug)}'
            f'<div class="age">{escape(age)}</div>')


def instructions():
    items = "".join(f"<li>{bi(i)}</li>" for i in INSTRUCTIONS)
    return (f'<h2>Para maestros y familias / For teachers and families</h2><ol class="rules">{items}</ol>')


def plan(week):
    objs = "".join(f"<li>{bi(o)}</li>" for o in week["objectives"])
    rows = ""
    for d in week["days"]:
        a, sk = d["activity"], SKILL_LABELS[d["activity"]["skill_area"]]
        rows += (f"<tr><td>{bi(d['day'])}</td><td>{bi(a['name'])}</td><td>{bi(sk)}</td></tr>")
    mats = "".join(f"<li>{bi(m)}</li>" for m in week["materials"])
    return (f'<h2>Plan de la semana / Weekly plan</h2>'
            f'<div><div class="label sub">Objetivos / Objectives</div><ul class="list">{objs}</ul></div>'
            f'<table><tr><th>Día / Day</th><th>Actividad / Activity</th><th>Área / Skill</th></tr>{rows}</table>'
            f'<div><div class="label sub">Materiales de la semana / Materials for the week</div>'
            f'<ul class="list" style="columns:1">{mats}</ul></div>')


def activity(day):
    a = day["activity"]
    sk = SKILL_LABELS[a["skill_area"]]
    name = "".join(f'<span class="{k}">{escape(a["name"][k])}</span><br>' for k in ("es", "en") if k in a["name"])
    chips = " / ".join(sk[k] for k in ("es", "en") if k in sk)
    dayname = " / ".join(day["day"][k] for k in ("es", "en") if k in day["day"])
    age = " / ".join(a["age_range"][k] for k in ("es", "en") if k in a["age_range"])
    head = (f'<div class="act-head"><span class="skill">{escape(chips)}</span>'
            f'<span class="sub">{escape(dayname)} · {escape(age)}</span><h2>{name}</h2></div>')
    mats = "".join(f"<li>{bi(m)}</li>" for m in a["materials"])
    mat_box = (f'<div class="small"><div class="label sub">Materiales / Materials</div>'
               f'<ul class="list mat">{mats}</ul></div>')
    steps = "".join(f'<div class="step"><div class="n">{i}</div>{bi(s)}</div>'
                    for i, s in enumerate(a["steps"], 1))
    say = f'<div class="box tint"><div class="label">Di esto / Say this</div>{bi(a["say_this"], "say")}</div>'
    sup = (f'<div class="box"><div class="label">Supervisión / Supervision</div>'
           f'{bi(a["supervision"])}</div>')
    draw = '<div class="draw">Dibuja aquí / Draw here</div>'
    return f'{head}{mat_box}<div class="steps">{steps}</div>{say}{sup}{draw}'


def cards(week):
    vocab = week["vocabulary"]
    cells = "".join(
        f'<div class="card">{"".join(f"<div>{escape(v[k])}</div>" for k in ("es", "en") if k in v)}</div>'
        for v in vocab)
    return (f'<h2>Tarjetas de vocabulario / Vocabulary cards</h2>'
            f'<div class="sub">Recorta cada tarjeta y dóblala por la línea punteada. / '
            f'Cut out each card and fold on the dotted line.</div><div class="cards">{cells}</div>')


def build(week):
    bodies = [(cover(week), "cover"), (instructions(), ""), (plan(week), "")]
    bodies += [(activity(d), "") for d in week["days"]]
    bodies.append((cards(week), ""))
    total = len(bodies)
    pages = "".join(page(inner, i, total, week, cls) for i, (inner, cls) in enumerate(bodies, 1))
    t = week["title"]
    title = " / ".join(t[k] for k in ("es", "en") if k in t)
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<title>{"DRAFT - " if is_draft(week) else ""}{escape(title)} - Pequeños Puentes Bilingües</title>'
            f'<style>{CSS}</style></head><body>{pages}</body></html>')


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--theme", required=True, help="theme slug, e.g. my-garden")
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--week", type=int, default=1)
    args = p.parse_args()

    src = ROOT / "data" / args.theme / f"age-{args.age}" / f"week-{args.week}.json"
    if not src.exists():
        sys.exit(f"Missing {src.relative_to(ROOT)}. Run generate.py first.")
    week = json.loads(src.read_text(encoding="utf-8"))
    out = ROOT / "out" / args.theme / f"age-{args.age}" / f"week-{args.week}" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(week), encoding="utf-8")
    st = status.ensure_status(out.parent)  # new weeks start as "draft"; existing status is kept
    print(f"Wrote {out.relative_to(ROOT)}  ({len(week['days']) + 4} pages)  status: {st['status']}"
          f"{'' if is_draft(week) is False else '  [DRAFT badge on]'}")
    dashboard.main()


if __name__ == "__main__":
    main()
