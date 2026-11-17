# Walkthrough — Build Night, Monday, November 16, 2026

*Build Night: From a Teacher's Idea to an AI-Powered Printable Business* · Full Stack Devs PDX · Gladstone Park SDA Church · 7:00–9:00 PM

Every prompt is in **PROMPTS** (next pages) so nothing has to be typed live. After each step, the **SHOW GUIDE** gives the exact command to open what Claude made and what to point at.

## Before you leave

- [x] **Dry run:** done Nov 16 in `puentes-test` (*Mi jardín / My Garden*, age 3, all 7 steps). That folder is the **fallback**: week 1 approved, week 2 draft.
- [x] **Yanibeth:** permission to show her name and *Pequeños Puentes Bilingües* (granted Nov 16). Use her name when you introduce the brief. If she sends a real activity, paste it into step 1; otherwise use the sample in PROMPTS.
- [ ] **Marketplace rules:** check Teachers Pay Teachers and Etsy rules on AI-assisted content for step 6.
- [ ] **On site at 6:30:** Claude Code signed in and started with `claude --model sonnet` (Opus took 7+ min per step in the first dry run) · empty `puentes/` folder · brief PDF and fallback pack open · terminal font ~20pt · phone hotspot ready.

## How each step works

1. **Paste** the step's prompt from PROMPTS into Claude Code and press Enter. First fill any `{...}` placeholder: in step 1 paste the sample activity, and in steps 2 and 6 type the theme.
2. **Wait.** Claude Code asks before it creates files or runs commands. Choose **"Yes, and don't ask again"**, or press **Shift+Tab** once at the start to auto-accept edits. Each step takes about 1–3 minutes, so narrate while it works.
3. **Show** what it made (the "Show the room" column). For the pack, run `open out/*/age-3/week-1/index.html`.
4. **Say** which of the teacher's questions it answers, then go to the next step. If something looks wrong, just tell Claude in plain words, e.g. "make the text bigger on the activity pages".

## The teacher's six questions (from her brief)

| Q | Her question | Answered in |
|---|---|---|
| 1 | How can AI turn my ideas into complete curricula without losing my style as a teacher? | Step 1 |
| 2 | What process creates, reviews and organizes many printables efficiently? | Step 5 |
| 3 | How can I automate publishing, promotion and sales? | Step 6 |
| 4 | What tools let a customer buy and download the file without me sending it? | Step 6 |
| 5 | How can I make sure the content is original, high quality and age-appropriate? | Step 4 |
| 6 | Could a system generate drafts by age, theme, skill and language? | Step 2 |

## The build (7:35–8:40)

| # | Step | Answers the brief's question | Paste from PROMPTS | Show the room |
|---|---|---|---|---|
| 1 | **The teacher's voice** | "How do I keep my style?" | CLAUDE.md prompt + one real activity | The rules file: Spanish first, cheap materials, safety by age, everything marked DRAFT |
| 2 | **The generator** | "Drafts by age, theme, skill and language?" | Generator prompt; **ask the room for a theme** | A full week as structured data: objectives, 5 activities, ES/EN vocabulary |
| 3 | **The printable pack** | The product itself | Pack prompt → **File → Print → Save as PDF** | Cover, instructions, weekly plan, activity pages, vocabulary cards, letter size |
| 4 | **Quality checks** | "Original, good quality, age-appropriate?" | Review prompt | Checklist and issues found; **a Spanish speaker reads the Spanish aloud** |
| 5 | **Making many** | "Create and organize many printables efficiently?" | Week 2 prompt | A second week built by the same script, plus a draft / needs-review / approved dashboard |
| 6 | **Selling and promotion** | "Automate publishing?" · "Buy and download without me sending it?" | Store prompt | Store listings, 3 Pinterest pins, preview images; marketplaces deliver the file automatically |
| 7 | **Approve a week** *(optional)* | "How do I stay in charge?" | Approve prompt | Fixes applied, DRAFT stamp gone, week 1 green on the dashboard |

**Test-run times (Nov 16, Sonnet, final prompts):** step 1 · 10 s · step 2 · 1 min · step 3 · 1.5 min · step 4 · 2 min · step 5 · 3 min · step 6 · 2 min. **Total: about 10 min of Claude time**, which leaves most of the hour for talking and showing results. Remember to replace `{THEME}`: in the test run it was left blank and Claude picked "Mi jardín" on its own.

**Pacing:** start step 1 by 7:35. While Claude works, talk through the "Show the room" column for the previous step. If you're behind at 8:15, skip the live step 5 and show the fallback instead: `FALLBACK-PACK-garden-week1-approved.pdf`, `FALLBACK-PACK-garden-week2-draft.pdf` and `puentes-test/out/dashboard.html`. Always do step 6 live: it's quick, and it's what the teacher cares about most.

## Close (8:40)

- **What happens next for the teacher (5 min):** follow "What to show at the close" on the Teacher Workflow page: the dashboard, one review finding, one live fix, then "make week 3" running during Q&A.
- **The pattern:** "AI drafts, a human approves, and the system packages and delivers."
- **Q&A:** short answers are in the runbook's last table.
- **Ask for December show-and-tell volunteers** before people leave.

**If it stalls:** narrate what Claude is doing and switch to the matching part of the fallback pack. Don't troubleshoot one attendee's laptop from the front: "pair with your neighbor; I'll come by."

## Notes

&nbsp;

&nbsp;

&nbsp;
