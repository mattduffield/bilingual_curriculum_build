# Store listing: Mi jardín / My Garden (DRAFT)

**Status: DRAFT. Do not publish yet.** See "Before you publish" at the bottom.

This listing covers the two weeks that exist today: week 1 "Mi jardín" and week 2 "Mi jardín: bichos y lluvia", for age 3.
It is a 2-week pack, not a month pack. Add weeks 3 and 4, then update the numbers here.

## Product title: Teachers Pay Teachers

Mi Jardín / My Garden: Bilingual Spanish & English Printable Preschool Activities for 3-Year-Olds, 2 Weeks

## Product title: Etsy

Bilingual Spanish English Preschool Activities Printable, Garden Bugs Rain, 3 Year Old Weekly Plans, Instant Download PDF

## Description (English)

Little ones learn best when they touch, count, paint, and move. **Mi jardín / My Garden** gives you two weeks of simple bilingual activities for 3-year-olds. Spanish comes first, and English sits right beside it on every page.

Each week has five days, and each day has one activity: math, language, art, sensory, and motor. The activities use things you already have, like paper, paint, cups, a sponge, and a towel. Week 1 is about seeds, flowers, soil, and worms. Week 2 is about bugs and rain.

Every activity page gives you the materials, three to four short steps, a "Say this" phrase in both languages, and a supervision note so you know how close the adult needs to be. There is a big box on each page for your child to draw in.

Made for preschool teachers, childcare centers, and families. Print, gather your materials, and start.

## Resumen en español

Mi jardín es un paquete bilingüe para imprimir, con dos semanas de actividades para niños de 3 años. Cada semana tiene cinco días, y cada día una actividad de matemáticas, lenguaje, arte, sensorial o motricidad, con materiales sencillos de casa o del salón. Cada página muestra el español primero y el inglés al lado, con una frase para que el adulto la diga y una nota de supervisión. Incluye tarjetas de vocabulario para recortar y doblar. Se descarga al instante en PDF tamaño carta.

## What's included

Two PDF files, one for each week. Each PDF has 9 pages (18 pages in all):

1. Cover
2. Instructions for teachers and families (Spanish and English)
3. Weekly plan: 3 learning objectives, a day-by-day table, and the week's materials list
4. Five activity pages, one per day, with a drawing box on each
5. One page of 10 fold-over vocabulary cards (Spanish on one side of the fold, English on the other)

**10 activities in all:**

| Week | Day | Activity | Skill |
|---|---|---|---|
| 1 | Lunes / Monday | Contar semillas / Counting seeds | math |
| 1 | Martes / Tuesday | La canasta del jardín / The garden basket | language |
| 1 | Miércoles / Wednesday | Flores con tubos / Tube-print flowers | art |
| 1 | Jueves / Thursday | Tierra y lombrices / Soil and worms | sensory |
| 1 | Viernes / Friday | Crece como una flor / Grow like a flower | motor |
| 2 | Lunes / Monday | Mariquitas y puntos / Ladybug dots | math |
| 2 | Martes / Tuesday | ¿Quién soy? / Who am I? | language |
| 2 | Miércoles / Wednesday | Nube con lluvia / Cloud and rain | art |
| 2 | Jueves / Thursday | Charco de agua / Puddle play | sensory |
| 2 | Viernes / Friday | Salta el charco / Jump the puddle | motor |

**20 vocabulary words (Spanish / English):**
- Week 1: semilla / seed, flor / flower, tierra / soil, raíz / root, hoja / leaf, tallo / stem, lombriz / worm, sol / sun, agua / water, regar / to water
- Week 2: mariquita / ladybug, abeja / bee, mariposa / butterfly, hormiga / ant, caracol / snail, lluvia / rain, nube / cloud, gota / drop, charco / puddle, paraguas / umbrella

## Ages

Made for age 3. Activities are labeled 3-4 or 3-5 years on the page.

## Skills

Math, language, art, sensory, and motor (matemáticas, lenguaje, arte, sensorial, motricidad). Every week covers all five.

## Format

**Printable PDF, letter size (8.5 x 11 in), instant download.** Print at 100%. You print it yourself; nothing is shipped.

## Search tags (10)

1. bilingual preschool
2. spanish english
3. printable activities
4. 3 year old
5. garden theme
6. dual language
7. spanish for kids
8. sensory activities
9. vocabulary cards
10. instant download

Every tag is 20 characters or fewer (Etsy's limit).

## What each claim rests on

| Claim in the listing | Where it comes from |
|---|---|
| 2 weeks, 10 activities, 5 skills per week | `data/my-garden/age-3/week-1.json`, `week-2.json` |
| 9 pages per PDF, letter size | `out/my-garden/age-3/week-N/pack.pdf` (checked with `pdfinfo`: 9 pages, 612 x 792 pt) |
| 20 vocabulary words, fold-over cards | the last page of each pack |
| "Say this" in both languages, supervision note, drawing box | every activity page |
| Household materials | the materials lists in the JSON |

## Not claimed (because we haven't made or checked it)

- A full month, or any weeks beyond 2.
- Ages other than 3.
- "Teacher-approved", "classroom-tested", "reviewed", or "native-speaker checked".
- Editable files, answer keys, audio, songs, or video.
- Alignment with any standard or published curriculum.
- A price. None has been set.

## Before you publish

1. **Approval.** Week 1 is approved (its 3 must-fix items are fixed; the Should fix items in `review/week-1.md` are still open). Week 2 is still `draft` and has not been reviewed. Check `out/dashboard.html`.
2. **DRAFT badge.** It now follows the status. Week 1's pages have no badge. Week 2's pages and the preview tiles from week 2 still say "BORRADOR / DRAFT" until week 2 is approved. Re-run `build_preview.py` after approving it.
3. **Re-export after any fixes.** Run `build_pack.py`, `export_pdf.py` for each week, then `build_preview.py`.
4. **Originality check.** Search a few phrases per activity (see `REVIEW-CHECKLIST.md`, section 5).
5. **Confirm "mariquita".** Some families say "catarina".
6. **Add the store link** to the pins in `store/pinterest.md`, and set a price.
