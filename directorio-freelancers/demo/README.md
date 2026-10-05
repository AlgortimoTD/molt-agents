# demo/

A fully fictional production company for demo mode, learning and tests, once per language:
`es/directorio/` (Faro Norte Producciones, Spanish vocabulary) and `en/directory/` (North
Beacon Productions, English vocabulary). Every file carries the line "DOCUMENTO FICTICIO" or
"FICTIONAL DOCUMENT". No real person, company, client, phone or email appears anywhere; the
privacy gate of `scripts/check.sh` runs over this folder like over the rest of the repository.

`directorio-freelancers-setup` (demo mode) copies the folder of the directory's language into
the person's Drive, next to the real directory and never inside it, and does not save it to
memory. The three sold skills keep a copy of `es/directorio/` under their `tests/fixtures/`
in the platform monorepo, so a test and a demo exercise the same data.

## What the data is built to show

The company staffs photo and video shoots with a pool of eight freelancers. The "today" of
the demo is **Monday 2026-10-06**: the last sweep ran on 2026-09-29, and one shoot is waiting
to be staffed for the next morning.

| Card | Why it is there |
|---|---|
| Ariel Quintero | preferred for construction photography; two valid certifications with documents; a limit that arrived as a personal condition and was rephrased |
| Bel Casas | second principal; writes in English; safety course valid for tomorrow but in the `tier-7` band |
| Dani Rueda | third principal; safety course **expired** on 2026-09-28: the exclusion with a written reason |
| Emma Loiza | editor; no certifications; the person to answer "who edits with care" |
| Fausto Vera | does construction photography; heights course in the `tier-60` band; safety course **undated**, so never valid |
| Greta Molano | not a principal but her card says she does construction photography; safety course valid but **no supporting document**; drone license with document |
| Hugo Pinel | event camera operator; status `paused` with its dated reason |
| Inés Robledo | editor and motion graphics; writes in English; a constraint on shift length |

## What to try, in order

1. **The bridge case.** "Necesito un fotógrafo mañana a las 7:00 para las vigas del puente
   nuevo en la vía norte, exige curso de seguridad en obra." Expected: a request file with
   Ariel (1), Bel (2) and Greta (3) on the shortlist, Dani and Fausto excluded with their
   reasons, three drafts (two in Spanish for WhatsApp and Messenger, one in English), and an
   empty answers table.
2. **Answers.** "Ariel no puede; Bel dijo que sí a las 3:40." Expected: both logged with the
   time, Bel marked as who got it, the invite text drafted, a fact on each card.
3. **Who knows what.** "¿Quién edita con detalle?" Expected: Emma, with the card and date as
   source. "¿Quién hace gráficas con texto?" Expected: not Ariel, with the constraint cited
   and without copying how it was first said.
4. **The sweep.** "Corre el barrido." Expected, counted from 2026-10-06: Dani expired, Bel
   within 7 days, Ariel's safety course (2026-11-30, 55 days) and Fausto's heights course
   (2026-12-01, 56 days) within 60 days, Fausto's safety course undated, Greta's safety course
   with no document; Ariel's heights course and Greta's drone license under no news; the index
   regenerated; the watermark advanced. Run it again: nothing changes.
5. **A renewal.** "Dani renovó su curso de seguridad, vence el 2027-09-28." Expected: the
   card updated with history, and Dani back on the next bridge shortlist.
6. **The audit.** "Organiza la carpeta." Expected: the two gaps of `memoria.md` listed, the
   closed request checked, nothing deleted.

Delete the demo folder when done; nothing else references it.
