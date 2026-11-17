#!/usr/bin/env python3
"""Build a print-ready HTML pack from a weekly plan JSON (bilingual plans only).

Usage: python3 build_pack.py --theme my-garden --age 3 --week 1
Reads  data/{theme}/age-{age}/week-{n}.json
Writes out/{theme}/age-{age}/week-{n}/index.html
"""
import argparse, datetime, json, sys
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).parent
ACCENT, ACCENT_LIGHT = "#5b9a6b", "#eaf4ec"

CSS = f"""
@page {{ size: 8.5in 11in; margin: 0.5in; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: "Helvetica Neue", Arial, sans-serif; color: #2b2b2b; font-size: 15pt; line-height: 1.35; background: #e8e8e8; }}
.page {{ width: 7.5in; height: 10in; overflow: hidden; position: relative; background: #fff; margin: 0.3in auto;
  padding: 0.1in 0.1in 0.1in; display: flex; flex-direction: column; break-after: page; page-break-after: always; }}
.page:last-child {{ break-after: auto; page-break-after: auto; }}
.draft {{ position: absolute; top: 0; right: 0; font-size: 10pt; font-weight: 700; letter-spacing: 2px; color: #b5483a; border: 1.5px solid #b5483a; padding: 1px 8px; border-radius: 4px; }}
.brand {{ font-size: 10pt; color: {ACCENT}; letter-spacing: 1px; text-transform: uppercase; }}
h1 {{ font-size: 34pt; margin: 0; line-height: 1.1; }} h2 {{ font-size: 24pt; margin: 0.1in 0 0.05in; }}
.en {{ color: #555; }} .sub {{ font-size: 13pt; color: #666; }}
.cover {{ text-align: center; justify-content: center; align-items: center; gap: 0.25in; }}
.cover svg {{ width: 4.6in; height: 3.6in; }}
.cover .age {{ font-size: 20pt; color: {ACCENT}; border: 2px solid {ACCENT}; border-radius: 30px; padding: 4px 24px; }}
.cols {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0.3in; }}
.cols h3 {{ margin: 0 0 6px; font-size: 13pt; color: {ACCENT}; text-transform: uppercase; letter-spacing: 1px; }}
ol, ul {{ margin: 0; padding-left: 1.2em; }} li {{ margin-bottom: 8px; }}
table {{ width: 100%; border-collapse: collapse; font-size: 13pt; margin: 0.1in 0; }}
th {{ background: {ACCENT_LIGHT}; text-align: left; }} th, td {{ border: 1px solid #cfd8d1; padding: 8px 10px; vertical-align: top; }}
.box {{ border: 2px solid {ACCENT}; border-radius: 10px; padding: 10px 14px; background: {ACCENT_LIGHT}; margin-top: 0.12in; }}
.box b.l {{ font-size: 11pt; color: {ACCENT}; text-transform: uppercase; letter-spacing: 1px; display: block; }}
.draw {{ flex: 1; border: 2px dashed #9bb8a2; border-radius: 12px; margin-top: 0.15in; padding: 8px 12px; font-size: 11pt; color: #888; }}
.tag {{ font-size: 12pt; color: {ACCENT}; }}
.cards {{ display: grid; grid-template-columns: 1fr 1fr; grid-auto-rows: 1.6in; gap: 0.12in 0.2in; margin-top: 0.1in; }}
.card {{ display: grid; grid-template-columns: 1fr 1fr; border: 1.5px solid #9bb8a2; border-radius: 8px; }}
.card div {{ display: flex; align-items: center; justify-content: center; font-size: 22pt; font-weight: 700; text-align: center; padding: 4px; }}
.card div + div {{ border-left: 2px dashed #9bb8a2; color: #555; font-weight: 400; }}
.card.blank div {{ color: #bbb; font-size: 12pt; font-weight: 400; }}
.mats {{ font-size: 10pt; line-height: 1.25; columns: 2; column-gap: 0.3in; }} .mats li {{ margin-bottom: 3px; break-inside: avoid; }}
.objs {{ font-size: 12pt; }} .objs li {{ margin-bottom: 4px; }} .plan td, .plan th {{ padding: 5px 8px; }}
@media print {{ body {{ background: #fff; }} .page {{ margin: 0; }} }}
"""

# Simple line drawings per theme (stroke only, no fills)
ART = {
 "my-garden": """<svg viewBox="0 0 460 360" fill="none" stroke="#5b9a6b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 300 H440"/><path d="M60 300 q10 -14 22 0 M370 300 q12 -14 24 0"/>
  <path d="M230 300 V150"/><path d="M230 220 q-60 -10 -70 -70 q60 0 70 70"/><path d="M230 190 q60 -10 70 -70 q-60 0 -70 70"/>
  <circle cx="230" cy="110" r="18"/><path d="M230 92 q-6 -30 -28 -26 q-4 24 28 26 M248 110 q30 -6 26 -28 q-24 -4 -26 28 M230 128 q6 30 28 26 q4 -24 -28 -26 M212 110 q-30 6 -26 28 q24 4 26 -28"/>
  <path d="M90 300 q-30 -60 0 -120 q30 60 0 120 M90 180 q-14 -26 -4 -42 M90 180 q14 -26 4 -42"/>
  <path d="M350 300 c-30 0 -34 -50 0 -50 c34 0 30 50 0 50 M350 250 q-6 -20 6 -30 M350 250 q14 -14 26 -10"/>
 </svg>""",
}
FALLBACK = """<svg viewBox="0 0 460 360" fill="none" stroke="#5b9a6b" stroke-width="4" stroke-linecap="round"><path d="M20 300 H440 M230 300 V160 M230 220 q-60 -10 -70 -70 q60 0 70 70 M230 190 q60 -10 70 -70 q-60 0 -70 70"/></svg>"""

INSTR = {
 "es": ["Lee la actividad del día antes de empezar. Toma solo unos minutos.",
        "Reúne los materiales. Todo es de casa o del salón.",
        "Siéntate al nivel del niño y usa la frase \"Di esto\".",
        "Repite las palabras en español y en inglés. La repetición ayuda.",
        "Celebra el esfuerzo, no solo el resultado. ¡Cada intento cuenta!",
        "Un adulto siempre supervisa. Revisa el recuadro de supervisión.",
        "Usa el recuadro en blanco para que el niño dibuje lo que hizo."],
 "en": ["Read the day's activity before you start. It takes just a few minutes.",
        "Gather the materials. Everything is from home or the classroom.",
        "Sit at the child's level and use the \"Say this\" phrase.",
        "Repeat the words in Spanish and in English. Repetition helps.",
        "Celebrate effort, not only the result. Every try counts!",
        "An adult always supervises. Check the supervision box.",
        "Use the blank box for the child to draw what they did."],
}

def pair(d, tag="div"): return f'<{tag}>{e(d["es"])}</{tag}>', f'<{tag} class="en">{e(d["en"])}</{tag}>'
SHOW_DRAFT = True
def draft(): return '<span class="draft">BORRADOR / DRAFT</span>' if SHOW_DRAFT else ''
def page(cls, body): return f'<section class="page {cls}">{draft()}{body}</section>'

def cover(p):
    return page("cover", f"""<div class="brand">Pequeños Puentes Bilingües</div>
      <h1>{e(p['title']['es'])}</h1><h1 class="en" style="font-size:24pt">{e(p['title']['en'])}</h1>
      {ART.get(p['theme_slug'], FALLBACK)}
      <div class="age">{e(p['days'][0]['activity']['age_range']['es'].split(' ')[0] if False else '')}Edad {p['age']} · Age {p['age']}</div>
      <div class="sub">Semana {p['week']} · Week {p['week']}</div>""")

def instructions(p):
    es = "".join(f"<li>{e(x)}</li>" for x in INSTR["es"]); en = "".join(f"<li>{e(x)}</li>" for x in INSTR["en"])
    return page("", f"""<div class="brand">Pequeños Puentes Bilingües</div><h2>Para maestros y familias <span class="en">/ For teachers and families</span></h2>
      <div class="cols"><div><h3>Español</h3><ol>{es}</ol></div><div class="en"><h3>English</h3><ol>{en}</ol></div></div>""")

def plan(p):
    obj = "".join(f"<li>{e(o['es'])}<br><span class='en'>{e(o['en'])}</span></li>" for o in p["objectives"])
    rows = "".join(f"<tr><td>{e(d['day']['es'])}<br><span class='en'>{e(d['day']['en'])}</span></td>"
        f"<td><b>{e(d['activity']['name']['es'])}</b><br><span class='en'>{e(d['activity']['name']['en'])}</span></td>"
        f"<td>{e(d['activity']['skill_area']['es'])}<br><span class='en'>{e(d['activity']['skill_area']['en'])}</span></td></tr>" for d in p["days"])
    mats = "".join(f"<li>{e(m['es'])} <span class='en'>/ {e(m['en'])}</span></li>" for m in p["materials_week"])
    return page("plan", f"""<div class="brand">Pequeños Puentes Bilingües</div><h2>Plan de la semana <span class="en">/ Weekly plan</span></h2>
      <h3 class="tag">Objetivos / Objectives</h3><ol class="objs">{obj}</ol>
      <table><tr><th>Día / Day</th><th>Actividad / Activity</th><th>Área / Skill</th></tr>{rows}</table>
      <h3 class="tag">Materiales de la semana / Materials for the week</h3><ul class="mats">{mats}</ul>""")

def activity(d):
    a = d["activity"]
    es = "".join(f"<li>{e(s['es'])}</li>" for s in a["steps"]); en = "".join(f"<li>{e(s['en'])}</li>" for s in a["steps"])
    mes = ", ".join(m["es"] for m in a["materials"]); men = ", ".join(m["en"] for m in a["materials"])
    return page("", f"""<div class="tag">{e(d['day']['es'])} / {e(d['day']['en'])} · {e(a['skill_area']['es'])} / {e(a['skill_area']['en'])} · {e(a['age_range']['es'])} / {e(a['age_range']['en'])}</div>
      <h1 style="font-size:28pt">{e(a['name']['es'])}</h1><div class="en" style="font-size:20pt">{e(a['name']['en'])}</div>
      <div class="cols" style="margin-top:0.12in"><div><h3>Materiales</h3>{e(mes)}</div><div class="en"><h3>Materials</h3>{e(men)}</div></div>
      <div class="cols" style="margin-top:0.12in"><ol>{es}</ol><ol class="en">{en}</ol></div>
      <div class="box"><b class="l">Di esto / Say this</b>“{e(a['say_this']['es'])}”<br><span class="en">“{e(a['say_this']['en'])}”</span></div>
      <div class="box" style="background:#fff"><b class="l">Supervisión / Supervision</b>{e(a['supervision']['es'])}<br><span class="en">{e(a['supervision']['en'])}</span></div>
      <div class="draw">Dibuja aquí / Draw here</div>""")

def vocab(p):
    cards = [f'<div class="card"><div>{e(v["es"])}</div><div>{e(v["en"])}</div></div>' for v in p["vocabulary"][:10]]
    while len(cards) < 10: cards.append('<div class="card blank"><div>Mi palabra</div><div>My word</div></div>')
    return page("", f"""<div class="brand">Pequeños Puentes Bilingües</div><h2>Tarjetas de palabras <span class="en">/ Word cards</span></h2>
      <div class="sub">Recorta y dobla por la línea punteada. / Cut out and fold on the dotted line.</div><div class="cards">{''.join(cards)}</div>""")

STATUSES = ("draft", "needs-review", "approved")

def build(p, status="draft"):
    global SHOW_DRAFT
    SHOW_DRAFT = status != "approved"
    pages = [cover(p), instructions(p), plan(p)] + [activity(d) for d in p["days"]] + [vocab(p)]
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(p['title']['es'])}{' (DRAFT)' if SHOW_DRAFT else ''}</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""

def week_folder(theme, age, week): return ROOT / "out" / theme / f"age-{age}" / f"week-{week}"

def read_status(folder):
    f = folder / "status.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None

def write_status(folder, status, date=None):
    assert status in STATUSES, f"status must be one of {STATUSES}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "status.json").write_text(json.dumps({"status": status, "date": date or datetime.date.today().isoformat()}, indent=2) + "\n", encoding="utf-8")

def build_pack(theme, age, week):
    src = ROOT / "data" / theme / f"age-{age}" / f"week-{week}.json"
    if not src.exists(): sys.exit(f"Not found: {src}")
    p = json.loads(src.read_text(encoding="utf-8")); p["theme_slug"] = theme
    folder = week_folder(theme, age, week)
    if read_status(folder) is None: write_status(folder, "draft")   # new weeks start as draft
    status = read_status(folder)["status"]
    (folder / "index.html").write_text(build(p, status), encoding="utf-8")
    return folder / "index.html"

LABEL = {"draft": ("Borrador / Draft", "#8a6d1f", "#fbf3d9"), "needs-review": ("Por revisar / Needs review", "#b5483a", "#fbe6e2"), "approved": ("Aprobado / Approved", "#2e7d4a", "#e3f3e8")}

def build_dashboard():
    rows, counts = [], {k: 0 for k in STATUSES}
    for sf in sorted((ROOT / "out").glob("*/age-*/week-*/status.json")):
        folder = sf.parent; theme = folder.parts[-3]; age = int(folder.name and folder.parts[-2].split("-")[1]); week = int(folder.name.split("-")[1])
        st = json.loads(sf.read_text(encoding="utf-8")); counts[st["status"]] += 1
        dj = ROOT / "data" / theme / f"age-{age}" / f"week-{week}.json"
        title = json.loads(dj.read_text(encoding="utf-8"))["title"] if dj.exists() else {"es": "—", "en": "—"}
        label, fg, bg = LABEL[st["status"]]
        rows.append((theme, age, week, f"<tr><td>{e(theme)}</td><td>{age}</td><td>{week}</td><td><b>{e(title['es'])}</b><br><span class='en'>{e(title['en'])}</span></td>"
            f"<td><span class='st' style='color:{fg};background:{bg}'>{label}</span></td><td>{e(st['date'])}</td>"
            f"<td><a href='{theme}/age-{age}/week-{week}/index.html'>Abrir / Open</a></td></tr>"))
    rows.sort(key=lambda r: r[:3])
    summary = " · ".join(f"{LABEL[k][0]}: <b>{counts[k]}</b>" for k in STATUSES)
    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Panel de revisión</title><style>
body{{font-family:"Helvetica Neue",Arial,sans-serif;margin:0;padding:32px;background:#fff;color:#2b2b2b}}
h1{{margin:0 0 4px}} .sub{{color:#666;margin-bottom:20px}} .en{{color:#666}}
table{{border-collapse:collapse;width:100%;max-width:1000px}} th{{background:#eaf4ec;text-align:left}} th,td{{border:1px solid #cfd8d1;padding:10px 12px;vertical-align:top}}
.st{{display:inline-block;padding:3px 10px;border-radius:12px;font-size:13px;font-weight:600;white-space:nowrap}} a{{color:#2e7d4a}} code{{background:#f2f2f2;padding:2px 5px;border-radius:4px}}
</style></head><body><h1>Panel de revisión <span class="en">/ Review dashboard</span></h1>
<div class="sub">Pequeños Puentes Bilingües · {summary}</div>
<table><tr><th>Tema / Theme</th><th>Edad / Age</th><th>Semana / Week</th><th>Título / Title</th><th>Estado / Status</th><th>Fecha / Date</th><th></th></tr>{''.join(r[3] for r in rows)}</table>
<p class="sub">Para cambiar el estado / To change a status: <code>python3 set_status.py --theme my-garden --age 3 --week 1 --status approved</code></p>
</body></html>"""
    (ROOT / "out" / "dashboard.html").write_text(html, encoding="utf-8")
    return ROOT / "out" / "dashboard.html"

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--theme", required=True)
    ap.add_argument("--age", type=int, required=True); ap.add_argument("--week", type=int, default=1); a = ap.parse_args()
    print(build_pack(a.theme, a.age, a.week)); print(build_dashboard())
