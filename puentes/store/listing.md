# Store listing — Mi huerto / My Garden (2-week pack)

**STATUS: DRAFT — do not publish yet.** Week 1 is `needs-review` and week 2 is `draft` (see `out/dashboard.html`).
Details of what must happen first are at the bottom under "Before you publish".

> Scope note: you asked for a "month pack". We have made **2 weeks** (10 activities), so this listing sells a 2-week pack.
> If you want to sell a month, weeks 3 and 4 need to be made first, and the numbers below updated.

## Product titles

**Teachers Pay Teachers** (108 characters)
Bilingual Spanish English Garden Preschool Activities | Mi Huerto | Age 3+ | 2 Weeks of Printable Activities

**Etsy** (117 characters)
Bilingual Spanish English Garden Printable Preschool Activities, Mi Huerto, Age 3+, Instant Download PDF, Letter Size

## Description (English)

**Mi huerto / My Garden** is a bilingual Spanish/English printable pack for preschool teachers, childcare centers and families.
It gives you **two weeks of simple garden-themed activities**, five days each, ready to print and use.

Every page has Spanish first and English right beside it. The activities use paper, paper plates, washable paint, tape, plastic cups and other things you already have at home or in the classroom.

Each day has one activity with:
- a name in Spanish and English
- the skill area and age range
- a materials list
- 4 short steps
- a "Di esto / Say this" phrase for the adult
- a supervision note, so you know how close the adult needs to stay
- a box for the child to draw what they did

Week 1 is *Mi huerto: sembramos y aprendemos / We Plant and Learn*. Week 2 is *Mi huerto: agua, sol y crecer / Water, Sun and Growing*.

**Please note:** these are hands-on activities for adults and children to do together. Small-parts, allergy and water notes are on the pages. Always supervise.

## Resumen en español

**Mi huerto** es un paquete imprimible bilingüe (español e inglés) para maestras, maestros, guarderías y familias. Incluye **dos semanas de actividades sencillas** sobre el huerto, con una actividad por día. En cada página el español va primero y el inglés al lado. Cada actividad trae materiales, pasos cortos, una frase para decir, una nota de supervisión y un espacio para dibujar. Los materiales son de casa o del salón. Incluye tarjetas de vocabulario para recortar y doblar. Es para niños desde los 3 años.

## What's included

Two PDF files (one per week), 9 pages each, **18 pages in total**. Each week has:
1. Cover
2. Instructions for teachers and families (Spanish/English)
3. Weekly plan: 3 learning objectives, a Monday–Friday table and the week's materials list
4. Five activity pages, one per day (Monday to Friday)
5. One page of fold-over vocabulary cards (Spanish on one side, English on the other)

Vocabulary: 19 words across the two weeks, plus 1 blank card for a child's own word.

**Not included:** editable files, answer keys, activities for ages 1–2, other themes.

## Ages

Written for **age 3**. Activities are labeled 3–4 or 3–5 years on each page. Not made for ages 1–2.

## Skills

Math, language, art, sensory and motor. Each week has one activity in each skill area.

## Format

Printable PDF, letter size (8.5 x 11 in), instant download.

## 10 search tags (each 20 characters or fewer)

1. bilingual preschool
2. spanish english
3. garden activities
4. preschool printable
5. dual language
6. spanish for kids
7. mi huerto
8. sensory activities
9. instant download
10. daycare activities

## Before you publish (claims check)

What this listing claims, and what backs it up:

| Claim | Backed by |
|---|---|
| 2 weeks, 10 activities, 18 pages, letter size | `out/my-garden/age-3/week-{1,2}/pack.pdf`, 9 pages each |
| Spanish first, English beside it, 4 steps, say-this, supervision, draw box | the pack pages |
| 19 words + 1 blank card | week 1 has 9 words, week 2 has 10 |
| Skills: math, language, art, sensory, motor | one of each per week |
| Instant download | true once the PDFs are uploaded to the store |

Not claimed, because we haven't made or verified it: a full month, ages 1–2 or ages 4–5 as the main level, other themes, editable files, standards alignment, teacher-tested, reviews, black-and-white printing, or "natural Latin American Spanish" (the teacher hasn't signed off yet).

Do these first:
1. Apply the fixes in `review/week-1.md` (choking-hazard items on Friday of week 1 matter most), then get the teacher to sign off on both weeks.
2. Run `set_status.py ... --status approved` for each week. The BORRADOR / DRAFT badge disappears then.
3. Re-export both PDFs with `export_pdf.py`. The current PDFs have the DRAFT badge, so they must not be sold.
4. Re-run `build_preview.py` and screenshot `store/preview.html` after approval. Until then the previews show the DRAFT badge.
5. Do a trademark search for "Pequeños Puentes Bilingües". Confirm you're happy to sell the cover drawing (we drew it ourselves).
6. If the teacher changes the week 1 activities, update this listing to match.
