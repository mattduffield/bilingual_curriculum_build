#!/usr/bin/env python3
"""Build out/dashboard.html: every pack week with its review status.

Usage: python3 dashboard.py
Reads out/*/age-*/week-*/status.json and data/{slug}/age-{age}/week-{n}.json.
Run again (or run build_pack.py / status.py set) to refresh.
"""
import json
import re
from html import escape
from pathlib import Path

from status import ROOT, STATUSES

LABELS = {"draft": "Borrador / Draft", "needs-review": "Por revisar / Needs review",
          "approved": "Aprobado / Approved"}


def find_review(title_es, age, week):
    """review/week-{n}.md, but only if its first heading names this theme and age."""
    path = ROOT / "review" / f"week-{week}.md"
    if not path.exists():
        return None
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return path if title_es in first and f"age {age}" in first else None


def collect():
    rows = []
    for f in sorted((ROOT / "out").glob("*/age-*/week-*/status.json")):
        slug, age_dir, week_dir = f.parent.relative_to(ROOT / "out").parts
        age, week = int(age_dir.split("-")[1]), int(week_dir.split("-")[1])
        st = json.loads(f.read_text(encoding="utf-8"))
        data_file = ROOT / "data" / slug / age_dir / f"{week_dir}.json"
        title = json.loads(data_file.read_text(encoding="utf-8"))["title"] if data_file.exists() else {}
        base = title.get("es", slug).split(":")[0]
        review = find_review(base, age, week)
        rows.append({
            "slug": slug, "age": age, "week": week, "status": st["status"], "date": st["date"],
            "title": title, "pack": f"{slug}/{age_dir}/{week_dir}/index.html",
            "review": f"../review/{review.name}" if review else None,
        })
    return sorted(rows, key=lambda r: (r["slug"], r["age"], r["week"]))


CSS = """
:root { --accent: #2f8f7b; --tint: #eaf5f2; --ink: #222; --muted: #666; }
* { box-sizing: border-box; }
body { font-family: "Avenir Next", "Trebuchet MS", Arial, sans-serif; color: var(--ink); background: #f6f6f4;
       margin: 0; padding: 0.4in; }
main { max-width: 1000px; margin: 0 auto; }
h1 { color: var(--accent); margin: 0 0 4px; }
.sub { color: var(--muted); margin: 0 0 20px; }
.tiles { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
.tile { background: #fff; border: 2px solid #ddd; border-radius: 10px; padding: 10px 18px; cursor: pointer;
        font: inherit; color: inherit; text-align: left; }
.tile b { display: block; font-size: 24pt; line-height: 1; }
.tile.on { border-color: var(--accent); background: var(--tint); }
table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; }
th { background: var(--tint); color: var(--accent); text-align: left; padding: 10px 12px; font-size: 10pt;
     text-transform: uppercase; letter-spacing: 1px; }
td { padding: 12px; border-top: 1px solid #e5e5e5; vertical-align: top; }
td .en { color: var(--muted); }
.badge { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 10pt; font-weight: 700;
         border: 2px solid; white-space: nowrap; }
.draft { color: #555; background: #eee; border-color: #999; }
.needs-review { color: #7a4d00; background: #fff1cc; border-color: #d9a400; }
.approved { color: #1d6b3b; background: #dff3e6; border-color: #3a9b5c; }
a { color: var(--accent); font-weight: 600; }
code { background: #eee; padding: 1px 6px; border-radius: 4px; }
.empty { padding: 20px; color: var(--muted); }
.note { color: var(--muted); font-size: 10pt; margin-top: 18px; }
"""

JS = """
const rows = [...document.querySelectorAll('tbody tr')];
document.querySelectorAll('.tile').forEach(t => t.addEventListener('click', () => {
  document.querySelectorAll('.tile').forEach(x => x.classList.toggle('on', x === t));
  rows.forEach(r => r.hidden = t.dataset.f !== 'all' && r.dataset.s !== t.dataset.f);
}));
"""


def build(rows):
    counts = {s: sum(r["status"] == s for r in rows) for s in STATUSES}
    tiles = f'<button class="tile on" data-f="all"><b>{len(rows)}</b>Todas / All</button>' + "".join(
        f'<button class="tile" data-f="{s}"><b>{counts[s]}</b>{escape(LABELS[s])}</button>' for s in STATUSES)
    body = ""
    for r in rows:
        t = r["title"]
        title = "".join(f'<div class="{k}">{escape(t[k])}</div>' for k in ("es", "en") if k in t) or escape(r["slug"])
        review = f'<a href="{escape(r["review"])}">Notas / Notes</a>' if r["review"] else "—"
        body += (f'<tr data-s="{r["status"]}"><td>{title}</td><td>{r["age"]}</td><td>{r["week"]}</td>'
                 f'<td><span class="badge {r["status"]}">{escape(LABELS[r["status"]])}</span></td>'
                 f'<td>{r["date"]}</td><td><a href="{escape(r["pack"])}">Abrir / Open</a></td><td>{review}</td></tr>')
    table = (f'<table><thead><tr><th>Semana / Week</th><th>Edad / Age</th><th>#</th><th>Estado / Status</th>'
             f'<th>Fecha / Date</th><th>Paquete / Pack</th><th>Revisión / Review</th></tr></thead>'
             f'<tbody>{body}</tbody></table>') if rows else '<div class="empty">No packs built yet.</div>'
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>Review dashboard - Pequeños Puentes Bilingües</title><style>{CSS}</style></head><body><main>'
            f'<h1>Panel de revisión / Review dashboard</h1>'
            f'<p class="sub">Pequeños Puentes Bilingües. Everything stays DRAFT until the teacher approves it.</p>'
            f'<div class="tiles">{tiles}</div>{table}'
            f'<p class="note">To change a status: <code>python3 status.py set &lt;theme&gt; &lt;age&gt; &lt;week&gt; '
            f'approved</code> (or <code>needs-review</code>, <code>draft</code>). This page is rebuilt whenever you build a pack or change a status. '
            f'Sign off with <code>REVIEW-CHECKLIST.md</code>.</p></main><script>{JS}</script></body></html>')


def main():
    rows = collect()
    out = ROOT / "out" / "dashboard.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(rows), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}  ({len(rows)} weeks)")


if __name__ == "__main__":
    main()
