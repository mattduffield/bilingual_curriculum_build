# Setup Guide — Build Along

**Full Stack Devs PDX · Monday, November 16, 2026 · 7:00 PM**\
*Build Night: From a Teacher's Idea to an AI-Powered Printable Business*

Nothing is required: you can come and watch. If you want to build along, pick **one lane** and set it up at home first. Venue Wi-Fi is not the place for a first install.

---

## What we're building

A small system that drafts **bilingual (Spanish/English) printable curricula for children ages 1–5**, from a real teacher's brief:

1. You choose an **age**, a **theme** (e.g. *Las manzanas / Apples*), a **skill** (math, language, art, sensory, motor) and a **language**.
2. AI drafts a **weekly plan** with learning objectives and matching **activities**, in the teacher's style.
3. The system lays it out as a **letter-size, print-ready PDF**: cover, instructions, weekly plan and activity pages.
4. A **checklist** catches problems: age-appropriateness, bilingual accuracy, originality, images that are safe to sell.
5. We draft the **store listing** and **Pinterest pins**, and look at how marketplaces deliver downloads automatically.

---

## Lane 1 · Browser — nothing to install

Open **claude.ai** (a free account works) and follow along by describing each step. You'll get the plan, activity text and listing copy; for the PDF, ask for a single HTML page, open it in your browser and use **File → Print → Save as PDF**.

## Lane 2 · Terminal — Claude Code

1. Install Node.js from **nodejs.org** (the LTS button).
2. Install Claude Code once:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
3. Make a folder and start it there:
   ```bash
   mkdir puentes && cd puentes
   claude --model sonnet
   ```
4. Sign in when it asks. Claude Code needs a **paid Claude plan** (Pro or Max) or an Anthropic API account; on a free account, use Lane 1. We use **Sonnet** because it's fast; Opus is slower and spends minutes thinking. That's it; we'll create every file together during the build.

**PDFs:** we'll generate HTML pages and print them to PDF from the browser, so no extra tools are needed. (If you prefer a command-line route, `pip install weasyprint` works too.)

---

## Bring

- [ ] One setup above, tested at home
- [ ] **A theme idea** for a preschool week (seasons, animals, colors, food, community helpers…)
- [ ] Optional: if you speak Spanish, you'll be our bilingual reviewer. *¡Hablantes de español bienvenidos!*

## Good to know

- We'll keep the **teacher in charge**: AI drafts, a person approves every page.
- Images: only use pictures you made, licensed, or generated with a tool whose terms allow selling the result.
- Marketplaces such as Teachers Pay Teachers and Etsy have their own rules for digital downloads and AI-assisted content. We'll look at them together; check the current rules before you sell anything.

---

*Full Stack Devs PDX · Gladstone Park SDA Church, 8378 Cason Rd, Gladstone, OR 97027 · Free · meetup.com/full-stack-dev-pdx/events/317302767*
