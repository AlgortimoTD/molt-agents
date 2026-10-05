---
name: production-pool-roster
description: >-
  v1.0.0 · Keeps the cards of a production team's freelancer pool in their directory folder on
  Google Drive: creates or updates one card per person from a sentence or a pasted list (channel,
  language, specialties, assignment limits, certifications with expiry, dated reliability facts),
  answers "who can do X" from the cards with card and date as source or says nobody is documented,
  and regenerates the index the team reads from the phone. Reliability is dated facts the team
  stated, never a score; a limit dictated as a personal condition is rephrased as the assignment
  constraint it implies. Use it whenever someone adds, corrects or asks about a freelancer of the
  pool, even without naming the skill. Triggers: "agrega a <persona> al directorio", "<persona>
  renovó su curso", "<persona> entregó tarde", "pega esta lista de freelancers", "¿quién sabe hacer
  X?", "¿quién edita con detalle?", "add a freelancer card", "who can shoot drone", "update the
  roster". [v1.0.0]
---

# production-pool-roster

## Version 1.0.0

A production team knows its freelancers the way a family knows its relatives: who is good at
what, who cannot be asked for certain things, who always delivers, whose safety course is about
to lapse. None of it is written anywhere, so staffing a shoot means two people remembering, and
losing one of them means losing the pool. This skill writes that knowledge down, one card per
person, in a folder the team can open and correct, and keeps it honest: every fact dated and
attributed, every limit phrased as what not to assign rather than why, every gap declared
rather than filled in.

The cards describe third parties who are not in the conversation. That is the reason behind
most of the rules below.

## Where you work

Find the directory folder the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- directorio-freelancers -->`; otherwise the platform memory entry
`directorio-freelancers: <folder>`; otherwise ask once ("¿cómo se llama la carpeta de tu
directorio en Drive?") and save it. Read the folder's `CLAUDE.md` first: it gives the
organization's name, the working language (everything you write goes in it), the roles table
and the hard rules, and it outranks this skill wherever they differ.

**Every name comes from the directory.** `CLAUDE.md` ends with a vocabulary block
(`<!-- directorio-freelancers:vocabulary ... -->`) with one `key: name` line per folder, file,
heading, data field, status, tier and role, in the directory's language. This skill refers to
them by key in braces (`{freelancers}`, `{card-data}`, `{history}`, `{index}`); read the block
before touching the folder and use the names it gives. A Spanish directory has `## Historial`
and `freelancers/soportes/`; an English one has `## History` and `freelancers/documents/`; no
text of this skill changes between them.

You are member-agnostic. The organization, the people and the rules come from `{company}`,
`{rules}` and `{certifications}`; nothing here assumes a particular team.

## The three jobs

1. **Create or update a card** from a sentence ("agrega a Ariel, director de fotografía,
   Messenger, español, curso de alturas vence en marzo de 2027"), a correction ("Bel ahora
   escribe por WhatsApp"), a renewal ("Dani renovó su curso, vence el 2027-09-28"), a fact about
   a delivery ("Fausto entregó tarde el viernes, lo dijo Mateo"), or a pasted list.
2. **Answer from the cards**: "¿quién sabe hacer X?", "¿quién puede volar dron?", "¿quién edita
   con detalle?". The answer names the people whose cards say so, with the card file and the
   date of the line that supports it. When nobody is documented, say exactly that and offer to
   record someone.
3. **Regenerate `{index}`** after every card change and whenever someone asks for it.

## The card contract

One file per person under `{freelancers}`, named in lower case with hyphens and no accents
(`ariel-quintero.md`). The structure is the plugin's `ficha.template.md` in the directory's
language, and every card keeps all of its sections even when one is empty, because the other
skills read them by heading:

```
# <Name Surname>
<!-- {current-since} with the origin: interview, pasted list, or chat with <who> -->

{card-data}            a fenced block, one line per field, exactly five fields:
                       {field-name}, {field-channel}, {field-contact}, {field-language}, {field-status}
{card-specialties}     one line per specialty, with the level the team gave it
{card-limits}          what not to assign, one per line, each with (date, who said it)
{card-certifications}  table: certification | issuer | expires | supporting document
{card-reliability}     dated facts, one per line: date · fact · (who said or recorded it)
{card-shoots}          one line per request the person appeared in: date · shoot · position · answer · outcome
{card-notes}           anything else, dated and attributed
{history}              replaced text, newest first, each entry dated and naming the section it came from
```

The data block is what `availability-request-drafter` and `certification-expiry-tracker` parse,
so its five field names are exactly the vocabulary's and nothing else goes inside the fence.
`{field-channel}` is where the person actually answers (WhatsApp, Messenger, other);
`{field-contact}` is the group or profile the coordinator uses in that channel, never a phone
number the team did not choose to write; `{field-language}` is the language the person writes
in, which is the language their messages will come out in; `{field-status}` is one of
`{status-active}`, `{status-paused}` or `{status-do-not-call}`.

## The hard rules, and why

1. **People edit the cards, and you re-read before you write.** Here, unlike an archive with a
   single writer, editing is the product: the production coordinator corrects a card in the chat
   or opens it in Drive and types. So before writing a card, read it again from disk, even if
   you read it a minute ago. Replace only the lines the request is about. Whatever text you
   replace goes to `{history}` as a dated entry that names the section (see `hugo-pinel.md` in
   the plugin demo: the old `estado` line kept under a dated heading). Nothing is deleted, ever;
   a person who wants a line gone gets it moved to `{history}`.
2. **Reliability is dated facts the team stated, never a score.** "2026-10-03 · Delivered two
   days late. (said by Mateo)" is a fact. "Unreliable", "7/10", "the best editor", a ranking or a
   trend you computed are judgments, and the card's third line of the agent's contract says it
   does not rate a person without the team's criteria. You list and count facts when asked ("tres
   entregas a tiempo, una tarde"); you never summarize them into an adjective the team did not
   say. If the person dictates an adjective ("Fausto es poco confiable"), ask for the fact behind
   it ("¿qué pasó y cuándo?") and write the fact; if there is none, write nothing and say so.
3. **Limits are assignment constraints, never diagnoses or health conditions.** A limit is
   written as what not to assign: "No asignarle gráficas con texto", "No asignarle jornadas de
   más de ocho horas seguidas". When the person dictates it as a personal, medical or
   psychological condition, write only the constraint it implies, append `{rephrased}` with the
   date to the line, and tell the person in one line what you did and why: the card describes a
   third party, lives in a shared folder, and the constraint is all the team needs to staff a
   shoot. Never store the condition, not even in `{history}` or `{memory}`.
4. **A certification without an expiry date is `{tier-undated}`**, written in the expires
   column, and it produces a `{gap}` line in `{memory}` naming the person and the certification.
   An undated certification never counts as valid for a shoot, so leaving the cell blank would
   quietly exclude the person from every shortlist without anyone knowing why. When the person
   gives a month without a day, ask for the day once; if they do not know it, write
   `{tier-undated}` and the gap rather than inventing the last day of the month.
5. **A certification name that is not in `{certifications}`** is written on the card as the
   person said it and reported in your reply, so the team decides whether it enters the catalog
   (that is their file, not yours). Do not rename it to a catalog entry that looks similar.
6. **The supporting document column** holds the path under `{supports}` when the file exists
   there, otherwise `{tier-unsupported}`. When someone says a document was dropped, look for it
   before writing the path; a path to a file that is not there is worse than `{tier-unsupported}`.
7. **A new card starts `{status-active}` at once; leaving the pool is the approver's call.** The
   production coordinator creates cards (that is the folder's natural route), so a card asked for
   in the chat is written immediately with `{status-active}`, and one dated line in `{memory}`
   records the addition so the person listed as `{role-approver}` in `{company}` sees it (the
   weekly audit lists the cards created since its last run for the same reason). `{field-status}`
   becomes `{status-do-not-call}` only when the approver asks; if the coordinator or anyone else
   asks, write it as a proposal in `{memory}` ("propuesta: marcar a X como no volver a llamar,
   pedido por Y el <date>") and tell them who has to confirm it. `{status-paused}` the coordinator
   can set, always with the dated reason and, when known, the date it ends, written right under
   the data block as the demo's `hugo-pinel.md` does. Cards are never deleted: leaving the pool
   is a status.
8. **A month without a day is still `{tier-undated}`, and the card is created now.** Ask for the
   day once in the same reply; do not hold the card until the answer arrives. Write
   `{tier-undated}` in the expires column, keep what was said ("vence en junio de 2027") as a
   dated line under `{card-notes}` so the information is not lost, and open the `{gap}` line.
   When the day arrives, the row is replaced and the old one goes to `{history}`.
9. **A blank `{field-contact}` is a gap, not a guess.** The field stays in the block with an empty
   value (the other skills accept an empty value), and a `{gap}` line in `{memory}` names the
   person and the missing contact. The same for a blank channel or language.
10. **Facts are appended in chronological order**, oldest first, under `{card-reliability}` and
   `{card-shoots}`; `{history}` is the only section ordered newest first. Appending a fact
   replaces nothing, so it needs no `{history}` entry.
11. **Regenerating `{index}` advances `last_index_at` in `{state}`** and nothing else there; the
   sweep fields belong to `certification-expiry-tracker`. You never touch `{company}`: a stale
   pool count there is the audit's finding, not yours to edit.
12. **Know who is speaking before a change.** If you do not know it from this conversation, ask
   the name and look it up in the roles table of `{company}`. It leaves the trail (every fact
   carries who said it); it is not security, which the folder's Drive permissions provide.
13. **Nothing is written outside the folder.** No messages, no calendar, no other files.

## Answering "who can do X"

Read every card under `{freelancers}` (there are rarely more than a few dozen), match the
specialty or the certification against `{card-specialties}` and `{card-certifications}`, and
respect `{card-limits}` and `{field-status}`: a person whose limits forbid the thing asked, or
who is `{status-paused}` or `{status-do-not-call}`, is named only to say why they are not an
option, citing the line and its date, and never with more detail than the constraint itself.

The answer, in the directory's language: the people who match, one line each with the specialty
line that supports it and the card file; then the people who do the work but are out of it right
now and why; then, when it applies, the certification question ("tres tienen el curso; si es
para una fecha concreta, pregunta por la vigencia a esa fecha", which is the expiry tracker's
job). When nobody matches, say "no hay nadie documentado para X" and offer to create a card. A
documented adjacent specialty (motion graphics when asked for text graphics) may be named, but
only labelled as not the same thing, with the offer to record it if the team says it covers it.

Specialty lines carry no date of their own; the date you cite for them is the card's
`{current-since}` date, which is the date the information entered the folder. Reliability and
limit lines carry their own dates and those are the ones to cite.

Do not answer from memory of a previous turn: read the cards. A card edited by hand this morning
is the truth, and your memory of it is not.

## Pasted lists

A list arrives as lines, a table, or a spreadsheet export. One card per row. Take the fields you
can read (name, channel, contact, language, specialties, certifications with or without dates)
and leave the rest blank with the section present; every missing field of every card goes in a
single reply summary and, for channel, language and certification dates, as `{gap}` lines in
`{memory}`. Never fill a blank with a guess, and never merge two rows into one person because the
names look alike: ask. Before creating, check whether a card with that name exists; if it does,
treat the row as an update and keep the history.

## The index contract

`{index}` is one Markdown table, regenerated whole, never edited in place: one row per card with
person, specialties, channel and language, status, the certifications valid on the regeneration
date (name and expiry; `{tier-undated}` and `{tier-unsupported}` spelled out; "none valid" when
an exigible certification has lapsed; "not applicable" when the card has none and says the work
requires none), and the last shoot from `{card-shoots}`. Above the table, one line with the
regeneration date and time in the time zone of `{company}` and who or what triggered it; below
it, the count of cards and of open `{gap}` lines in `{memory}`. The demo's
`salidas/directorio.md` is the shape. The index is what someone opens on the phone during an
event, so it stays one table and nothing else.

## Done means

- The card exists with every section of the contract, the data block has exactly the five
  fields, and the `{current-since}` comment names where the information came from.
- Every reliability line and every limit carries a date and who said it; no adjective, score or
  ranking appears anywhere on the card unless the team said it verbatim as a fact.
- A limit that arrived as a condition is written as a constraint with `{rephrased}` and the
  person was told.
- Replaced text is in `{history}`, dated and attributed; nothing was deleted.
- Undated certifications are `{tier-undated}` with a `{gap}` line; unknown certification names
  were reported; `{status-do-not-call}` was written only on the approver's request.
- `{index}` was regenerated and its date line is today.
- Every answer to "who can do X" cites the card file and the date of the supporting line, or
  says that nobody is documented.

## The failure to watch for

Helpfulness. The person asks who can shoot the bridge tomorrow and you remember a name from
last week's chat that has no card: inventing a person, even a real one, puts someone on a
shortlist the folder cannot vouch for. The person says "Fausto is unreliable" and the obvious
move is to write that: scoring. The person explains a limit through a condition and the obvious
move is to keep their words: copying a diagnosis into a shared folder about a third party. The
coordinator fixed a card by hand an hour ago and you write your version over it: a silent
overwrite that erases the one edit that was actually correct. Each of these is faster than the
rule, and each is the exact thing the card exists to prevent.
