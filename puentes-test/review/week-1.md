# Review: Mi jardín / My Garden, age 3, week 1

**Pack status: APPROVED (2026-11-16).** M1-M3 applied; the Should fix and Teacher's call items below are still open.
**Reviewed:** `data/my-garden/age-3/week-1.json` against `REVIEW-CHECKLIST.md`
**Reviewer:** Claude (first pass). The teacher still signs off.
**Resolution (2026-11-16):** M1, M2, and M3 were applied to the content bank, then week 1 was rebuilt and its PDF re-exported. Everything else below was not changed.

Page numbers are the pages of the printed pack, as built from this JSON:
1 cover, 2 instructions, 3 weekly plan, 4 Lunes (math), 5 Martes (language),
6 Miércoles (art), 7 Jueves (sensory), 8 Viernes (motor), 9 vocabulary cards.
The HTML pages were not reviewed, only the JSON.

## Summary

| Priority | Count | Meaning |
|---|---|---|
| Must fix | 3 | Wrong, or a safety gap. Do not sell until fixed. |
| Should fix | 10 | Clearly better with a fix. |
| Teacher's call | 3 | A choice only the teacher can make. |
| Could not check | 2 | Needs a person or a tool I don't have. |

## Must fix

**M1. Page 4, Lunes: "¿En cuál hay más?" has no right answer.**
- Where: `days[0].activity.steps[1]` and `[2]`, `materials[0]`
- Issue: 10 paper seeds. 5 go in one cup, "the rest" (also 5) go in the other. Both cups are equal, so the question "Which has more?" is wrong. Also, the objective says "up to 5", but the activity uses 10.
- Fix: use 5 seeds. Step 2: put 2 seeds in one cup. Step 3: put the other 3 in the second cup and ask which has more. Materials: "5 círculos de papel café". EN to match: "5 brown paper circles", "Count together as you put 2 seeds in one cup", "Put the other 3 in the second cup". Then the "Say this" counting to three still works.

**M2. Page 5, Martes: the stone has no size limit.**
- Where: `days[1].activity.materials[1]`, `supervision`
- Issue: "una piedra lisa grande" / "a large smooth stone" does not say how large. Supervision says "the stone must be large", which is vague. A 3-year-old can still mouth objects.
- Fix: say "una piedra lisa más grande que el puño del niño" / "a smooth stone bigger than the child's fist", or swap it for a safer object like a big wooden spoon or a soft toy.

**M3. Page 7, Jueves: no allergy or soil-hygiene note.**
- Where: `days[3].activity.materials[1]`, `[2]`, `supervision`
- Issue: spaghetti contains wheat and oats can carry gluten. Garden soil can carry germs. Nothing tells the adult to check allergies or what soil to use. Soil mixed with spaghetti also needs to be thrown away.
- Fix: material: "tierra de maceta nueva (no de la calle)" / "new potting soil (not from outdoors)". Add to supervision: "Pregunta por alergias (trigo, avena). Tira todo al terminar." / "Ask about allergies (wheat, oats). Throw everything away when done."

## Should fix

**S1. Pages 4-8: supervision levels are not defined.**
- Where: every `supervision` field
- Issue: "Adulto cerca" (p4, p8), "Adulto sentado junto al niño" (p5), "Adulto muy cerca" (p7), "Adulto presente todo el tiempo" (p6). They sound different but are not defined.
- Fix: use two fixed phrases. "Adulto presente todo el tiempo" (hands-on) for art, sensory, language. "Adulto cerca" (in the room, watching) for math and motor. Same in English: "Adult with the child the whole time" / "Adult nearby".

**S2. Page 8, Viernes: "Diga" is the wrong form.**
- Where: `days[4].activity.steps[1].es`
- Issue: "Diga:" is usted. The rest of the pack uses tú ("Pon", "Pregunta", "Di esto").
- Fix: "Di: \"Sale el sol, cae la lluvia\" y muevan los dedos como gotas."

**S3. Page 6, Miércoles: "Sella el tubo" is not natural.**
- Where: `days[2].activity.steps[2].es`, `steps[3].es`
- Issue: "sellar" means to seal. For stamping with paint, teachers say "estampar". Also, "para hacer forma de pétalo" sounds like a translation.
- Fix: step 1: "Aprieta el tubo para darle forma de pétalo." Step 3: "Moja el tubo en la pintura y estámpalo en el papel." Step 4: "Haz 5 estampados en círculo para formar una flor." EN: "Make 5 prints in a circle to form a flower."

**S4. Page 6, Miércoles: supervision sentence is clumsy.**
- Where: `days[2].activity.supervision.es`
- Issue: "Pintura no tóxica y sin llevarla a la boca" is not a full thought.
- Fix: "Adulto presente todo el tiempo. Usa pintura no tóxica y cuida que no se la lleven a la boca." Also add a line to cover the table (see T-notes).

**S5. Page 8, Viernes: the blanket is listed but never used.**
- Where: `days[4].activity.materials[1]`
- Issue: "una cobija pequeña (opcional)" appears in no step. This also breaks the checklist rule that materials match steps. "Cobija" is also regional.
- Fix: remove it, or add a step ("Siéntense en la cobija como si fuera la tierra"). If kept, use "una manta o cobija".

**S6. Pages 3 and 9: three vocabulary words are never practiced.**
- Where: `vocabulary`; `raíz`, `agua`, `regar` appear in no activity
- Issue: the cards teach words the week never uses.
- Fix: add to Viernes step 2: "Finjan regar la semilla con agua" / "Pretend to water the seed" and step 1: "Las raíces crecen hacia abajo: mueve los dedos de los pies" / "Roots grow down: wiggle your toes". Or swap the words for ones the week does use.

**S7. Page 3: objectives don't match the activities.**
- Where: `objectives[0]`, `objectives[2]`
- Issue: Objective 1 says "count and sort up to 5 garden objects". The week counts paper seeds and never sorts. Objective 3 says "create with natural materials". Only the soil is natural (the rest is paper and paint).
- Fix: Objective 1: "Contar hasta 5 objetos y comparar cuál grupo tiene más." Objective 3: "Moverse, explorar y crear con ideas del jardín."

**S8. Page 3: the weekly materials list is not consolidated.**
- Where: `materials`
- Issue: 14 lines. "2 vasos de papel" and "cucharas y vasos" are separate. Some lines hold several items ("una hoja, una flor de papel, una piedra lisa grande y un cucharón de juguete") or options ("tierra limpia y húmeda o avena seca"). That is hard to shop from. The paper flower on Martes could be the one made on Miércoles.
- Fix: one item per line, merge cups, and give each item a quantity. Consider moving Martes after Miércoles, or say "usa una flor de papel de otro día".

**S9. Pages 5, 7: "niño" is used for every child.**
- Where: `days[1].activity.steps[1].es`, `days[3].activity.steps[1].es`, supervision fields in `days[0]`, `[1]`
- Issue: "El niño saca un objeto", "adulto sentado junto al niño" read as boys only.
- Fix: "Cada niño o niña saca un objeto" / "Adulto sentado junto al niño o la niña". Or use "peque" in the steps.

**S10. Page 5: the Spanish column holds an English word.**
- Where: `days[1].activity.say_this.es`
- Issue: the Spanish column holds an English word and the English column holds a Spanish word. See Teacher's call C1.
- Fix: see C1.

## Teacher's call

**C1. Page 5: bilingual "Say this" phrase.**
- Where: `days[1].activity.say_this`
- ES: "¡Es una hoja verde! Hoja. Leaf." EN: "It's a green leaf! Hoja. Leaf."
- Issue: this models both words on purpose, which is good teaching. But each column then holds both languages, and a Spanish-only or English-only edition would leak the other.
- Options: keep as is (and drop it from single-language editions), or make it one language per column: ES "¡Es una hoja verde!" / EN "It's a green leaf!"

**C2. Pages 5-8: regional words.**
- Where: "café" (p4, brown), "cobija" (p8), "tina" (p7), "cucharón de juguete" (p5)
- Issue: these are common in Mexico but not everywhere. "Café" for brown is widespread. A "cucharón" is a ladle. A "pala" is a scoop.
- Options: "marrón o café", "una manta", "un recipiente grande", "una pala de juguete". Tell me which countries your customers are in.

**C3. Page 8: age label.**
- Where: `days[4].activity.age_range`
- Issue: the printed page says "2-5 años" while the others say "3-4" or "3-5". This pack is for age 3. If kept at 2, the checklist rule for ages 1-2 applies (every item must be bigger than a toilet-paper tube).
- Options: change to "3-5 años", or keep "2-5" and confirm the movement is safe for 2-year-olds.

## Smaller notes

- **Messy play (pages 6, 7):** neither activity says to cover the table or floor. Add "Cubre la mesa con papel o un mantel" / "Cover the table with paper or a cloth".
- **Page 8:** add "Quita juguetes del piso" / "Clear toys off the floor" to supervision.
- **English (pages 4-8):** reads naturally. The only change is "stamps" → "prints" (S3).

## Could not check

- **Originality:** I wrote this text from scratch, and nothing matches a known curriculum, character, or trademark that I can see. I cannot run a plagiarism search. Please search 3 phrases per activity, and check the "Grow, grow, little flower" chant on page 8 against known songs.
- **Images:** the JSON holds no images. The pack's flower drawing is an SVG drawn in code (`build_pack.py`), so it is ours. No fonts are embedded (system fonts only). This is outside the JSON review, so confirm the checklist's image section when the HTML is reviewed.

## Print layout (from the JSON only)

- Every activity has 3-5 steps, and the weekly plan has 14 materials and 10 vocabulary words. All of these fit their pages in the draft build.
- The fixes above add text. Pages 5 (language) and 7 (sensory) are the tightest, so rebuild and look at them again after editing. The drawing box shrinks as text grows.
- Nothing in the JSON can be fully checked for print layout. A test print is still on the checklist.
