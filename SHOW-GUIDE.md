# Show guide: what to open after each step

Run these in a **second terminal tab** in the same `puentes/` folder (⌘T, then `cd` to the folder), so Claude's tab stays clean.
**Web pages** (`.html`) open in your browser with `open`. **Text files** (`.md`) open in Zed with `zed`; press **⌘⇧V** for a formatted preview, or just read the plain text.
Before you start, zoom the browser to **125–150%** (⌘+) so the back row can read it.

---

## After step 1 · The rules file

`zed CLAUDE.md`

- **Point at:** the Voice section, the age 1–2 safety rule (nothing smaller than a toilet-paper tube), and her activity as the model to copy.
- **Say:** "Claude rereads this before everything it writes. If she changes a rule here, every future page changes."

## After step 2 · The week as data

`zed data/*/age-3/week-1.json`

- **Point at:** `"es"` and `"en"` side by side on every line, the five days, and the vocabulary list. Claude's chat summary table works too.
- **Say:** "This isn't a document yet. It's data, so the same week can become a PDF, a listing, or a Spanish-only version."
- **Ask Yanibeth:** "Does this sound like you?"

## After step 3 · The printable pack (web page)

`open out/*/age-3/week-1/index.html`

Scroll slowly from top to bottom. Each white sheet is one printed page:

1. **Cover:** title in Spanish and English, a line drawing, the age, and the **BORRADOR / DRAFT** stamp in the corner.
2. **Adult guide:** how to use the week, in two columns, ES | EN.
3. **Weekly plan:** objectives, a day-by-day table, and the week's materials ("one shopping list").
4. **Activity pages (×5):** Spanish left, English right; the **Say this** box; the **Supervision** box; the empty **Draw here** box for the child.
5. **Vocabulary cards:** cut out, fold on the line, Spanish on one side and English on the other.

Then press **⌘P** and point at the preview: **9 pages, letter size**. "That's the file she sells." Cancel; no need to print.

## After step 4 · The review

`zed review/week-1.md`, then `zed REVIEW-CHECKLIST.md`

- **Point at:** the three groups (**Must fix · Should fix · Teacher's call**), each with a page number and a suggested fix.
- **Read one Must fix aloud.** Yanibeth reads a Spanish line and decides one Teacher's call.
- **Say:** "Claude checked its own work against her standards and changed nothing. She decides."

## After step 5 · The dashboard (web page)

`open out/dashboard.html`

- **Point at:** the count tiles (All · Draft · Needs review · Approved). Click a tile to filter the list.
- **The table:** one row per week, with its status, its date, **Abrir / Open** (opens that week's pages) and **Notas / Notes** (opens the review).
- **Click "Abrir / Open" on week 2:** a whole new week in the same design, built by the same script.
- **Say:** "This is how she manages 50 printables: one page shows what's waiting for her."

## After step 6 · The store (web page + text)

`open $(find store -name preview.html)`

- **The preview collage:** the product title, what's included (weeks, activities, cards, age) and sample pages on the right. Zoom out (⌘−) until the whole frame fits; **that screenshot is the product image** for Teachers Pay Teachers and Etsy.

`zed $(find store -name listing.md)`

- **Point at:** the two titles, the description, the 10 tags, and the **"Not claimed"** and **"Before you publish"** lists. In the test run it wrote "2-week pack, not a month pack".
- `zed $(find store -name pinterest.md)` shows the 3 pins. Each has `[STORE LINK]` until she publishes.
- **Say:** "She uploads the PDF once, and the marketplace delivers it to every buyer."

## After step 7 · Approval (web page)

`open out/dashboard.html` (reload it if it's already open: ⌘R)

- **Point at:** week 1 is now **Aprobado / Approved** (green), and week 2 is still **Borrador / Draft**.
- **Click "Abrir / Open" on week 1:** the DRAFT stamp is gone. Open week 2: it's still there.
- **Say:** "AI drafts, a human approves, and the system packages and delivers."

---

**If a command says "no matches found":** the folder has a different name. Run `ls out store` to see what Claude made, or ask Claude: *"Open the dashboard for me."*
**Fallback:** the same pages already exist in `puentes-test/`. `cd` there and run the same commands.
