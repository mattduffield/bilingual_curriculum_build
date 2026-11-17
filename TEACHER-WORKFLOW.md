# After the build: the teacher's weekly workflow

**The idea:** Claude writes the activities and the scripts do everything else. The teacher never runs a script herself; she asks in plain words, and Claude runs them.

| Part | What it does |
|---|---|
| `content/{theme}.json` | The **activity bank**: every activity written for a theme. Claude adds to it. |
| `generate.py` | Picks 5 activities from the bank and makes a week. |
| `build_pack.py` → `export_pdf.py` | Lays out the 9 pages, then saves `pack.pdf`. |
| `status.py` · `out/dashboard.html` | Tracks each week: draft → needs-review → approved. |
| `store/` | Listing, Pinterest pins and a preview image for each product. |

## The loop: make, review, fix, approve, sell

1. **Make.** She types: *"Make weeks 3 and 4 of Mi jardín for age 3"* or *"Start a new theme, Los colores / Colors, for age 2."* Claude writes the new activities into the bank and runs generate, build and export. Each week takes a few minutes.
2. **Review.** She opens `out/dashboard.html` to see what's waiting, prints or reads `pack.pdf`, and reads `review/week-N.md`. That's Claude's first pass against the checklist, split into **Must fix / Should fix / Teacher's call**.
3. **Fix.** She types: *"Day 2: use a bigger stone. Change mariquita to catarina everywhere. Rebuild week 1."*
4. **Approve.** She types: *"Week 1 is approved."* Claude runs `status.py set … approved`, rebuilds the pack without the **BORRADOR / DRAFT** stamp, and the dashboard turns green. (That's PROMPTS step 7.)
5. **Sell.** She types: *"Update the store listing for weeks 1–4."* Then she uploads `pack.pdf` and the preview image to Teachers Pay Teachers or Etsy **herself**, pastes the listing, and sets a price. After that, the marketplace delivers the download to every buyer (her Question 4).
6. **Promote.** She posts the 3 pins from `store/pinterest.md`, linking each one to her listing.

## Reading the dashboard

Claude makes every week; the status shows how far each one has gone through **review**:

| Status | Means | Who sets it |
|---|---|---|
| **Borrador / Draft** (grey) | Made, not reviewed | Claude, when it builds a week |
| **Por revisar / Needs review** (yellow) | Claude's first-pass review is done (**Notas / Notes** link); waiting for the teacher | Claude, when it reviews |
| **Aprobado / Approved** (green) | Fixes made, teacher signed off, DRAFT stamp removed, ready to sell | **Only the teacher**, by telling Claude |

Only **Approved** weeks go in the store.

## Reviewing the store before publishing

- Open `store/listing.md` and check every claim against what really exists: weeks, ages, page count. The listing has a **"Do not claim"** list and a **"Before you publish"** checklist. In the test run it called the pack a "2-week pack, not a month pack".
- Open `store/preview.html` and take a screenshot. That's the product image.
- Nothing goes live until **she** uploads it. Claude drafts and the teacher publishes.

## What to show at the close (about 5 minutes)

1. **The dashboard:** "Here's her week: two packs, one needs review, one is a draft."
2. **`review/week-1.md`:** read one *Must fix* aloud. In the test run it flagged a math question with no right answer, a stone too small for the age, and a soil/allergy note. "The AI caught its own mistakes, and the teacher decides."
3. **Approve week 1 live** with PROMPTS step 7: the fixes go in, the DRAFT stamp comes off, and the dashboard turns green.
4. **Type "Make week 3"** and let it run while you take questions. Show the result at the end.
5. **The listing:** "It refused to call two weeks a month. Nothing is published until she uploads it."

**The line to end on:** *"AI drafts, a human approves, and the system packages and delivers."*
