# Prompts for the live build — paste, don't type

Run in an empty folder: `mkdir puentes && cd puentes && claude --model sonnet`\
Theme placeholder: **{THEME}**, e.g. *Las manzanas / Apples*. Ask the room for one at step 2.\
*(Question N)* = the teacher's question from her brief; the full list is on the Walkthrough page.\
Paste a prompt, let it finish, show the result (commands are in the **Show guide**), then paste the next one.

---

## Step 1 · The teacher's voice  *(Question 1)*

**What happens:** Claude writes `CLAUDE.md`, a rules file it rereads before every later step. It holds her voice, her safety rules, the bilingual format and one of her real activities as the model to copy. (~10 s)\
**Why it matters:** this is how AI keeps *her* style. Fix a rule here once, and every future page follows it.\
**Say:** "Before AI writes anything, we teach it how this teacher writes. That's this file, and she owns it."

```
Create a CLAUDE.md for this project. It's a bilingual (Spanish/English) printable curriculum
business for children ages 1-5, called "Pequeños Puentes Bilingües" (Little Bilingual Bridges).
Customers are preschool teachers, childcare centers and families who buy a download and print it.

Rules for everything you create:
- Write like an experienced, warm preschool teacher: short sentences, practical, encouraging.
- Activities must be simple and cheap: household or classroom materials only.
- Age-appropriate: for ages 1-2 nothing smaller than a toilet-paper tube (choking hazard);
  every activity lists the adult supervision needed.
- Spanish first, English second, side by side. Natural Latin American Spanish, not a word-for-word translation.
- Every activity has: name (ES/EN), skill area, age range, materials, steps (3-5), and one
  "say this" phrase for the adult in both languages.
- Skill areas: math, language, art, sensory, motor.
- Letter-size, print-ready, clean layout, lots of white space, big readable text.
- Never copy published curricula or characters; everything original.
- Mark everything as DRAFT until the teacher approves it.
- Always draft right away; don't ask clarifying questions first. The teacher will redirect.

Here is one of the teacher's real activities to match the style:
{PASTE YANIBETH'S 2-3 REAL ACTIVITIES HERE, or use the sample below}
```

*Sample activity if you don't have one of hers:*
```
Contar manzanas / Counting apples (matemáticas / math, 3-4 años)
Materiales: 5 manzanas de papel, una canasta / 5 paper apples, a basket
1. Pon las manzanas en la mesa. / Put the apples on the table.
2. Cuenten juntos mientras las ponen en la canasta. / Count together as you put them in the basket.
3. Pregunta: "¿Cuántas hay?" / Ask: "How many are there?"
Di esto / Say this: "¡Una, dos, tres manzanas rojas!" / "One, two, three red apples!"
```

## Step 2 · The generator  *(Question 6)*

**What happens:** Claude writes an **activity bank** (`content/…json`, every activity for the theme) and a small `generate.py` that picks one activity per day and saves a week as structured data. It also checks the rules: 3–5 steps, a supervision line, no small parts for ages 1–2. (~1 min)\
**Why it matters:** the content lives as data, not as a document, so the same week can become a PDF, a listing or a Spanish-only version.\
**Say:** "Here's her answer: yes, by age, theme, skill and language. The AI writes the activities; the script just assembles and checks them." **Then ask Yanibeth: "Does this sound like you?"**

```
Build a small generator. Inputs: age (1-5), theme, skill areas (any of math, language, art,
sensory, motor) and language mode (bilingual by default). Output one week as JSON in
data/{theme-slug}/age-{age}/week-1.json with: title (ES/EN), 3 learning objectives (ES/EN),
5 days with one activity per day following CLAUDE.md, a materials list for the week, and a
vocabulary list of 8-10 words (ES/EN). Then generate one week for: theme "{THEME}", age 3,
all five skill areas. Show me the JSON summary when done.
```

## Step 3 · The printable pack  *(the brief's product)*

**What happens:** Claude writes `build_pack.py`, a template that turns any week's data into 9 letter-size pages: cover, adult guide, weekly plan, 5 activity pages and vocabulary cards. (~1.5 min)\
**Why it matters:** the design is built once. Every future week comes out looking the same, which is what a brand looks like.\
**Say:** "This is the product she sells. Notice it's still stamped DRAFT; nothing is final until she approves it."

```
Write build_pack.py that reads data/{theme-slug}/age-{age}/week-{n}.json and writes one print-ready
file, out/{theme-slug}/age-{age}/week-{n}/index.html. Letter size, @page margins 0.5in, and every
page exactly one printed page (fixed 10in height, overflow hidden, page break after). Pages:
cover (title ES/EN, age, "Pequeños Puentes Bilingües", one simple line-drawn SVG of the theme),
teacher/family instructions (ES/EN), weekly plan table with objectives, one page per activity
(big text, ES/EN side by side, Say this and Supervision boxes, a box to draw in that fills the
rest of the page), and one page of 10 fold-over vocabulary cards (ES/EN). Every page shows DRAFT.
Simple CSS, light accent color, no other images. Run it for week 1.
```
*Then:* `open out/*/age-3/week-1/index.html` → **⌘P** → check it says **9 pages** → **Save as PDF**.

## Step 4 · Quality checks  *(Question 5)*

**What happens:** Claude writes `REVIEW-CHECKLIST.md` (safety, Spanish, English, originality, image rights, layout), then reviews week 1 against it and writes `review/week-1.md`. **That review is where the "must-fix" items come from.** It sorts every problem into *Must fix* (safety or plain wrong), *Should fix* and *Teacher's call*, each with the page and a suggested fix. It changes nothing; the week is marked *Needs review*. (~2 min)\
**Why it matters:** the AI checks its own work against her standards, but the decisions stay with her.\
**Say:** read one *Must fix* aloud. In the test run: "the math question has no right answer, the cups are 5 and 5." Then ask **Yanibeth** to read a Spanish line aloud and decide one *Teacher's call* item (e.g. *mariquita* or *catarina*).

```
Create REVIEW-CHECKLIST.md with checks a teacher signs off on: age-appropriateness and safety
(choking hazards, supervision), Spanish correctness and natural phrasing, English correctness,
originality (no copied text, characters or trademarks), images we have the right to sell,
print layout. Then review data/{theme-slug}/age-3/week-1.json (not the HTML pages) against it and write review/week-1.md listing
every issue with page and fix. Don't change anything yet; mark the pack status as NEEDS REVIEW.
```

## Step 5 · Making many  *(Question 2)*

**What happens:** Claude writes 5 new activities for week 2 and runs the same `build_pack.py`. It adds a status to every week (draft → needs-review → approved) and a dashboard listing them all. (~3 min)\
**Why it matters:** making more is now cheap. Weeks 3, 4 or a new theme are the same request again, and the dashboard shows what's waiting for her.\
**Say:** "This is how one teacher manages 50 printables: one page shows what's draft, what needs review and what's approved."

```
Make week 2 for the same theme and age with five new activities, then run build_pack.py for it.
Add status.json to each week folder ("status": "draft" | "needs-review" | "approved" and the date),
and a dashboard.html that lists every week with its status, so the teacher can review a batch at once.
Show the BORRADOR / DRAFT badge on the pages only while a week is not approved.
```

## Step 6 · Selling and promotion  *(Questions 3 and 4)*

**What happens:** Claude writes the Teachers Pay Teachers and Etsy listings, 3 Pinterest pins and a preview collage for the product image. It's told to claim only what exists. In the test run it wrote "2-week pack, not a month pack" and listed what *not* to claim. (~2 min)\
**Why it matters:** this answers how she sells without emailing files. She uploads the PDF once, and the marketplace delivers it to every buyer.\
**Say:** "AI writes the listing, but she publishes it. And it won't oversell; it called two weeks two weeks."

```
For the {THEME} month pack, write store/listing.md with: a product title for Teachers Pay
Teachers and one for Etsy (each under 140 characters), a description in English with a Spanish
summary, what's included, ages, skills, "printable PDF, letter size, instant download", and
10 search tags. Then write store/pinterest.md with 3 pin titles and descriptions. Finally, make
a 4-image preview set: preview.html laying out the cover and 3 sample pages as a collage I can
screenshot. Don't claim anything we haven't made.
```

## Step 7 · Approve a week  *(the teacher's sign-off; optional live, 1–2 min)*

**What happens:** acting on the teacher's "approved", Claude applies the step 4 must-fix items, marks week 1 *Approved*, rebuilds it **without** the DRAFT stamp and re-exports the PDF. Week 2 stays a draft. (~1 min)\
**Why it matters:** this closes the loop. AI drafts, a human approves, and only approved weeks get sold.\
**Before pasting:** ask Yanibeth to look at week 1 and say "approved".\
**Say:** "Claude never approves on its own. She says 'approved', and only then does the stamp come off."

```
The teacher has reviewed week 1. Apply the must-fix items from review/week-1.md, rebuild week 1 and
re-export its pack.pdf. Then mark week 1 approved with status.py. If the DRAFT badge doesn't follow the
status yet, make build_pack.py show it only when a week is not approved. Rebuild, then show me the
dashboard: week 1 should be Approved with no DRAFT badge, and week 2 still Draft.
```
