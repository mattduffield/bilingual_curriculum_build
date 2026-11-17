# Live Runbook — Monday, November 16, 2026

Keep this open on the presenter laptop. The brief is `project-brief.pdf`; every step below answers one of its six questions.

## Timeline

| Time | What |
|---|---|
| 6:30 | Arrive, projector, Wi-Fi, run the 15-minute check |
| 7:00 | Food and conversation; take show-and-tell names at the door |
| 7:20 | Short show & tell (two or three people, 3 minutes each) |
| 7:30 | **The brief** (5 min): "This is Yanibeth Puente's brief for *Pequeños Puentes Bilingües*." Walk through the PDF: who it's for, how it should work, the six questions |
| 7:35 | **Build** (steps 1–6 below, ~65 min) |
| 8:40 | Recap: the pattern (AI drafts → human approves → system packages and delivers); Q&A |
| 9:00 | Done; ask for December show-and-tell volunteers |

## Before the night

- [x] Yanibeth: permission to show the name and brand on screen (granted Nov 16). Attending (confirmed). Still to ask: availability to attend; 2–3 existing activities or plans to use as style examples
- [x] Full dry run done Nov 16: the **fallback** is `puentes-test/` (*Mi jardín / My Garden*, age 3) plus the two `FALLBACK-PACK-garden-*.pdf` files
- [ ] Check current Teachers Pay Teachers and Etsy rules on digital downloads and AI-assisted content (for step 6)
- [ ] Prepare a few images that are safe to sell (your own, licensed, or Adobe Firefly's own models)
- [ ] Empty `puentes/` folder ready; terminal font ~20pt; browser zoom ~150%

## 15-minute check on site

- [ ] Claude Code signed in; `claude --model sonnet` starts in `puentes/`
- [ ] `project-brief.pdf` open in one window, the fallback pack in another
- [ ] Phone hotspot ready (Claude Code needs the network)
- [ ] Notifications off

## The build

**Step 1 · The teacher's voice** — *Question 1: "How do I keep my style?"*
Create `CLAUDE.md` with the teacher's rules and examples: who the materials are for, tone, simple and inexpensive activities, clear instructions, clean layout, Spanish and English side by side. Paste in one real example activity.
*Say:* "The memory file is how the AI learns the teacher's style instead of inventing one. Same trick as the September tips."

**Step 2 · The generator** — *Question 6: "Drafts by age, theme, skill and language?"*
Define the inputs (age 1–5, theme, skills, language) and have Claude draft one week as structured data: objectives, five daily activities, materials, vocabulary list in both languages.
*Ask the room for a theme.*

**Step 3 · The printable pack** — *Brief: "ready to print, letter size"*
Turn the plan into HTML pages: cover, instructions for the teacher or family, weekly plan, activity pages (counting, vocabulary, art, motor). Print to PDF and show it.

**Step 4 · Quality checks** — *Question 5: "Original, good quality, age-appropriate?"*
Add a review checklist and have Claude check the draft against it: age-appropriate tasks and safety (no small parts under 3), correct Spanish and English, nothing copied, images safe to sell. *A person signs off on every page.*
*Ask a Spanish speaker in the room to review the Spanish.*

**Step 5 · Making many** — *Question 2: "Create, review and organize many printables efficiently?"*
Generate a month of themes into an organized folder structure (theme/age/week), each with a review status, so the teacher reviews a batch instead of starting from blank pages.

**Step 6 · Selling and promotion** — *Questions 3 and 4: "Automate publishing and promotion?" and "Buy and download without me sending it?"*
Draft the product title, description and preview images for the store; draft three Pinterest pin texts. Explain that Teachers Pay Teachers and Etsy deliver digital files automatically after purchase; the teacher uploads once. Mention the current marketplace rules you checked.

## If it stalls

Narrate what Claude is doing; if a step fails, open the matching part of the fallback pack and keep going. Don't debug a single attendee's laptop from the front: "pair with your neighbor; I'll come by."

## Questions you may get

| Question | Short answer |
|---|---|
| "Is it allowed to sell AI-assisted content?" | Depends on the marketplace and changes over time; read the current rules and disclose where required. The teacher's review and editing is what makes it the teacher's work. |
| "Who owns the result?" | Keep it original: the teacher's ideas, edited by the teacher, with images you have rights to. |
| "Can this run without the cloud?" | Drafting can use local models, but quality drops; the printing and packaging are all local. |
| "Why not just use Canva?" | Canva is great for one page. The value here is generating a consistent pack by age, theme and skill, many at a time, in two languages. |
