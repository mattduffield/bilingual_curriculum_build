#!/usr/bin/env python3
"""Pequeños Puentes Bilingües - weekly plan generator (DRAFT output).

Usage: python3 generate.py --theme "my-garden" --age 3 \
         --skills math language art sensory motor [--mode bilingual|es|en] [--week 1]

Content lives in library.py (themes -> skill -> activities). Add a theme there
to support it. Every plan is validated against CLAUDE.md rules before writing.
"""
import argparse, json, re, sys
from pathlib import Path
from library import LIBRARY

SKILLS = ["math", "language", "art", "sensory", "motor"]
ROOT = Path(__file__).parent

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def pick(theme, skill, age, week):
    for a in LIBRARY[theme]["activities"][skill]:
        if a.get("week", 1) == week and a["ages"][0] <= age <= a["ages"][1]:
            return a
    sys.exit(f"No '{skill}' activity for age {age}, week {week} in theme '{theme}'. Add one to library.py.")

def validate(plan, age):
    for d in plan["days"]:
        a = d["activity"]
        assert 3 <= len(a["steps"]) <= 5, f"{a['name']['en']}: needs 3-5 steps"
        assert a["skill_area"]["key"] in SKILLS
        assert a["supervision"] and a["say_this"] and a["materials"]
        if age <= 2:
            assert a["safety_ok_under_3"], f"{a['name']['en']}: not cleared for ages 1-2"
    assert len(plan["objectives"]) == 3
    assert 8 <= len(plan["vocabulary"]) <= 10

def collapse(o, mode):
    if mode == "bilingual": return o
    if isinstance(o, dict):
        if set(o) == {"es", "en"}: return o[mode]
        return {k: collapse(v, mode) for k, v in o.items()}
    if isinstance(o, list): return [collapse(x, mode) for x in o]
    return o

def build(theme, age, skills, mode, week):
    t = {**LIBRARY[theme], **LIBRARY[theme].get("weeks", {}).get(week, {})}
    days, mats, seen = [], [], set()
    names = [("lunes","Monday"),("martes","Tuesday"),("miércoles","Wednesday"),("jueves","Thursday"),("viernes","Friday")]
    for i in range(5):
        a = dict(pick(theme, skills[i % len(skills)], age, week))
        a["age_range"] = {"es": f"{a['ages'][0]}-{a['ages'][1]} años", "en": f"ages {a['ages'][0]}-{a['ages'][1]}"}
        a.pop("ages"); a.pop("week", None)
        days.append({"day": {"es": names[i][0], "en": names[i][1]}, "activity": a})
        for m in a["materials"]:
            if m["es"] not in seen: seen.add(m["es"]); mats.append(m)
    plan = {"status": "DRAFT", "theme": t["theme"], "age": age, "week": week,
            "title": t["title"], "objectives": t["objectives"], "days": days,
            "materials_week": mats, "vocabulary": t["vocabulary"]}
    validate(plan, age)
    return collapse(plan, mode)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--theme", required=True); p.add_argument("--age", type=int, required=True, choices=range(1, 6))
    p.add_argument("--skills", nargs="+", choices=SKILLS, default=SKILLS)
    p.add_argument("--mode", choices=["bilingual", "es", "en"], default="bilingual")
    p.add_argument("--week", type=int, default=1)
    a = p.parse_args()
    key = slug(a.theme)
    if key not in LIBRARY: sys.exit(f"Unknown theme '{key}'. Known: {', '.join(LIBRARY)}")
    out = ROOT / "data" / key / f"age-{a.age}" / f"week-{a.week}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(build(key, a.age, a.skills, a.mode, a.week), ensure_ascii=False, indent=2), encoding="utf-8")
    print(out)
