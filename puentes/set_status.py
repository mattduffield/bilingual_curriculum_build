#!/usr/bin/env python3
"""Set a week's status (draft | needs-review | approved), rebuild its pack and the dashboard.
Usage: python3 set_status.py --theme my-garden --age 3 --week 1 --status approved
The BORRADOR / DRAFT badge is hidden only when the status is 'approved'."""
import argparse
from build_pack import STATUSES, week_folder, write_status, build_pack, build_dashboard

ap = argparse.ArgumentParser(); ap.add_argument("--theme", required=True); ap.add_argument("--age", type=int, required=True)
ap.add_argument("--week", type=int, required=True); ap.add_argument("--status", required=True, choices=STATUSES); a = ap.parse_args()
write_status(week_folder(a.theme, a.age, a.week), a.status)
print(build_pack(a.theme, a.age, a.week)); print(build_dashboard())
