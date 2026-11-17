#!/usr/bin/env python3
"""Review status for each pack week.

Each week folder out/{theme-slug}/age-{age}/week-{n}/ has a status.json:
  {"status": "draft" | "needs-review" | "approved", "date": "YYYY-MM-DD"}

Usage:
  python3 status.py set my-garden 3 1 needs-review     # change a status (also rebuilds the dashboard)
  python3 status.py list                               # print every week and its status
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
STATUSES = ("draft", "needs-review", "approved")


def week_dir(slug, age, week):
    return ROOT / "out" / slug / f"age-{age}" / f"week-{week}"


def read_status(folder):
    path = Path(folder) / "status.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def write_status(folder, status):
    if status not in STATUSES:
        sys.exit(f"Status must be one of {STATUSES}, not '{status}'.")
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    data = {"status": status, "date": date.today().isoformat()}
    (folder / "status.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return data


def ensure_status(folder):
    """Create status.json as 'draft' if the week has none. Never overwrites."""
    return read_status(folder) or write_status(folder, "draft")


def main():
    args = sys.argv[1:]
    if args[:1] == ["set"] and len(args) == 5:
        _, slug, age, week, status = args
        folder = week_dir(slug, int(age), int(week))
        if not (folder / "index.html").exists():
            sys.exit(f"No built pack at {folder.relative_to(ROOT)}. Run build_pack.py first.")
        data = write_status(folder, status)
        print(f"{slug} age-{age} week-{week}: {data['status']} ({data['date']})")
        import dashboard
        dashboard.main()
    elif args[:1] == ["list"]:
        for f in sorted((ROOT / "out").glob("*/age-*/week-*/status.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            print(f"{f.parent.relative_to(ROOT / 'out')}: {d['status']} ({d['date']})")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
