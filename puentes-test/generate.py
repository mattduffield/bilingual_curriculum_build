#!/usr/bin/env python3
"""Pequeños Puentes Bilingües - weekly plan generator.

Usage:
  python3 generate.py --theme "Mi jardín" --age 3 --skills math language art sensory motor
  python3 generate.py --theme my-garden --age 3 --mode es

Reads content/{theme-slug}.json (the authored activity bank), picks one activity
per day for the requested age and skills, validates against CLAUDE.md rules,
and writes data/{theme-slug}/age-{age}/week-{n}.json.
Everything is marked DRAFT until the teacher approves it.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
SKILLS = ["math", "language", "art", "sensory", "motor"]
DAYS = [("Lunes", "Monday"), ("Martes", "Tuesday"), ("Miércoles", "Wednesday"),
        ("Jueves", "Thursday"), ("Viernes", "Friday")]
# Words that signal small parts; never allowed in activities for ages 1-2.
SMALL_PARTS = ["bean", "frijol", "button", "botón", "boton", "bead", "cuenta",
               "coin", "moneda", "rice", "arroz", "seed", "semilla de verdad"]


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def find_bank(theme):
    """Match by slug of the input against the bank slug or either title."""
    wanted = slugify(theme)
    for path in sorted((ROOT / "content").glob("*.json")):
        bank = json.loads(path.read_text(encoding="utf-8"))
        names = {bank["slug"], slugify(bank["title"]["es"]), slugify(bank["title"]["en"])}
        if wanted in names:
            return bank
    sys.exit(f"No content bank for theme '{theme}'. Add content/{wanted}.json first.")


def week_meta(bank, week):
    """Week 1 uses the bank's top-level fields; later weeks need a bank['weeks'][n] entry."""
    if week == 1:
        return bank
    meta = bank.get("weeks", {}).get(str(week))
    if not meta:
        sys.exit(f"Theme '{bank['slug']}' has no week {week} in its content bank.")
    return meta


def pick_activities(bank, age, skills, week):
    chosen = []
    for skill in skills:
        options = [a for a in bank["activities"]
                   if a["skill"] == skill and a["age_min"] <= age <= a["age_max"]
                   and a.get("week", 1) == week]
        if not options:
            sys.exit(f"No '{skill}' activity for age {age}, week {week} in theme '{bank['slug']}'.")
        chosen.append(options[0])
    # Five days: cycle through the chosen skills if fewer than five.
    return [dict(chosen[i % len(chosen)]) for i in range(5)]


def validate(activity, age):
    problems = []
    if activity["skill"] not in SKILLS:
        problems.append("unknown skill area")
    if not 3 <= len(activity["steps"]) <= 5:
        problems.append("steps must be 3-5")
    for key in ("name", "say_this", "supervision"):
        if not activity.get(key, {}).get("es") or not activity[key].get("en"):
            problems.append(f"missing {key}")
    if age <= 2:
        text = json.dumps(activity["materials"], ensure_ascii=False).lower()
        hits = [w for w in SMALL_PARTS if w in text]
        if hits:
            problems.append(f"possible choking hazard for age {age}: {hits}")
    return problems


def strip_lang(obj, keep):
    """Recursively keep only one language when mode is es or en."""
    if isinstance(obj, dict):
        if set(obj) <= {"es", "en"} and keep in obj:
            return {keep: obj[keep]}
        return {k: strip_lang(v, keep) for k, v in obj.items()}
    if isinstance(obj, list):
        return [strip_lang(v, keep) for v in obj]
    return obj


SUPERVISION_LEVELS = ("Adulto presente todo el tiempo", "Adulto cerca")


def warnings_for(acts, meta):
    """Non-fatal checks from REVIEW-CHECKLIST.md."""
    warns = []
    es_text = " ".join(
        json.dumps({k: a[k] for k in ("name", "materials", "steps", "say_this")}, ensure_ascii=False)
        for a in acts).lower()
    for v in meta["vocabulary"]:
        if v["es"].lower() not in es_text:
            warns.append(f"vocabulary word '{v['es']}' is not used in any activity")
    for a in acts:
        if not a["supervision"]["es"].startswith(SUPERVISION_LEVELS):
            warns.append(f"'{a['name']['en']}': supervision should start with one of {SUPERVISION_LEVELS}")
    return warns


def build_week(bank, age, skills, week):
    meta = week_meta(bank, week)
    acts = pick_activities(bank, age, skills, week)
    days, materials, seen = [], [], set()
    for i, act in enumerate(acts):
        problems = validate(act, age)
        if problems:
            sys.exit(f"Activity '{act['name']['en']}' failed: {'; '.join(problems)}")
        day_es, day_en = DAYS[i]
        days.append({
            "day": {"es": day_es, "en": day_en},
            "activity": {
                "name": act["name"],
                "skill_area": act["skill"],
                "age_range": {"es": f"{act['age_min']}-{act['age_max']} años",
                              "en": f"{act['age_min']}-{act['age_max']} years"},
                "materials": act["materials"],
                "steps": act["steps"],
                "say_this": act["say_this"],
                "supervision": act["supervision"],
            },
        })
        for m in act["materials"]:
            if m["es"] not in seen:
                seen.add(m["es"])
                materials.append(m)
    vocab = meta["vocabulary"]
    assert 8 <= len(vocab) <= 10, "vocabulary must be 8-10 words"
    assert len(meta["objectives"]) == 3, "need exactly 3 objectives"
    materials = meta.get("materials", materials)  # a week may supply its own consolidated list
    for w in warnings_for(acts, meta):
        print(f"WARNING: {w}", file=sys.stderr)
    return {
        "status": "DRAFT",
        "theme_slug": bank["slug"],
        "age": age,
        "week": week,
        "skill_areas": skills,
        "title": meta.get("title", bank["title"]),
        "objectives": meta["objectives"],
        "days": days,
        "materials": materials,
        "vocabulary": vocab,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--theme", required=True)
    p.add_argument("--age", type=int, required=True, choices=range(1, 6))
    p.add_argument("--skills", nargs="+", choices=SKILLS, default=SKILLS)
    p.add_argument("--mode", choices=["bilingual", "es", "en"], default="bilingual")
    p.add_argument("--week", type=int, default=1)
    args = p.parse_args()

    bank = find_bank(args.theme)
    week = build_week(bank, args.age, args.skills, args.week)
    if args.mode != "bilingual":
        week = strip_lang(week, args.mode)
    week["language_mode"] = args.mode

    out = ROOT / "data" / bank["slug"] / f"age-{args.age}" / f"week-{args.week}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(week, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)}  [DRAFT]")


if __name__ == "__main__":
    main()
