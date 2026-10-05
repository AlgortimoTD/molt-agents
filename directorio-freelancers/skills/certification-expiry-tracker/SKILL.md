---
name: certification-expiry-tracker
description: >-
  v1.0.0 · Weekly sweep of the certifications in a production freelancer directory
  (directorio-freelancers), and the answer to who holds a valid one on a given date. Puts
  each card's certifications in exactly one tier counted from the sweep day
  (expired, within 7, 30 or 60 days, undated, no supporting document), writes the dated
  expiry report, regenerates the index and advances the watermark; idempotent within a day.
  Valid for a shoot means it expires after the shoot's date, never after today; undated never
  counts. Records a renewal the team states, with history. Use it whenever a directory folder
  exists and someone asks about certifications, courses, licenses or expiries, or the routine
  fires, even without naming the skill. Triggers: "corre el barrido del directorio", "¿qué
  certificaciones vencen?", "¿quién tiene curso de alturas vigente el <fecha>?", "<persona>
  renovó su curso", "run the certification sweep", "who holds a valid safety course on",
  "what expires this month". [v1.0.0]
---

# certification-expiry-tracker

## Version 1.0.0

A production team knows which of its freelancers holds the safety course for a construction
site, right up to the morning the course has expired and the shoot is in two hours. The
knowledge is real; what is missing is a date somebody checks every week. This skill is that
check: it reads every card of a freelancer directory, puts each certification in the tier it
belongs to as of today, writes the report the team reads on Monday, and answers, on any day,
who is actually allowed on a given site on a given date. It never guesses a date, and it never
treats a course the team "is sure about" as valid when the card has no expiry for it.

## Where you work

Find the directory folder the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- directorio-freelancers -->`; otherwise the platform memory entry
`directorio-freelancers: <folder>`; otherwise ask once, in the person's language, and save it.
Read the folder's `CLAUDE.md` first. It gives you the organization's name, the working
language (the report and the index are written in it), the roles and the time zone, and it
outranks this skill wherever they differ.

**Every name comes from the directory.** `CLAUDE.md` ends with a vocabulary block
(`<!-- directorio-freelancers:vocabulary ... -->`) with one `key: name` line per folder, file,
heading, field, tier and role, in the directory's language. This skill refers to them by key
in braces: `{freelancers}` is the cards folder, `{card-certifications}` the heading of the
certifications table inside a card, `{certifications}` the catalog and tiers file under
`_config/`, `{supports}` the folder of certificate documents, `{expiry-report}` the dated
report path pattern, `{index}` the regenerated index, `{state}` the watermark, `{history}` the
heading that keeps replaced text, `{memory}` and `{gap}` the memory file and the prefix of a
gap line, and `{tier-expired}`, `{tier-7}`, `{tier-30}`, `{tier-60}`, `{tier-undated}`,
`{tier-unsupported}` the six tiers. Read the block before anything else and use the names it
gives; never write a Spanish name into an English directory or the reverse.

You are organization-agnostic. The certifications, their issuers and the tiers' meaning come
from `{certifications}`; the people come from the cards; nothing here assumes a particular
company, course or country.

## Two ways in

1. **The scheduled sweep.** `{sources}` holds the literal prompt of the weekly routine (for a
   Spanish directory it reads "Corre el barrido del directorio: revisa las certificaciones de
   todas las fichas, escribe el reporte de vencimientos en salidas/, regenera el índice y
   avanza la marca de agua"). When that prompt, or a person asking for the sweep, arrives, run
   the full sweep below. It runs in the cloud from one account, with no computer switched on,
   and it is the only part of the directory that runs on a schedule.
2. **A question in the chat.** "¿Qué certificaciones vencen?" is answered from the latest
   `{expiry-report}` if it is from today, otherwise by running the sweep. "¿Quién tiene curso
   de alturas vigente el 15 de noviembre?" is answered with the validity rule below, from the
   cards, without writing a report. "Dani renovó su curso" is a renewal and follows its own
   section.

## The sweep, step by step

1. **Read the watermark and the catalog.** `{state}` says when the last sweep ran and which
   report it wrote; `{certifications}` lists the certifications the organization recognizes
   (name as the team says it, who requires it, typical validity, the document kept) and
   defines the six tiers and the validity rule. The time zone is in `{company}`; the sweep day
   is today in that zone.
2. **Read every card.** For each file in `{freelancers}` other than the README of `{supports}`,
   read the `{card-data}` block (name and status) and the `{card-certifications}` table:
   certification, issuer, expiry, supporting document. A card whose certifications section
   says the person has none, or whose work requires none, counts as a card with zero
   certifications; it still counts toward `cards_seen`.
3. **Put each certification in exactly one tier**, in this order of precedence, so the summary
   adds up to the number of certifications found:
   - no expiry date on the row (the cell says `{tier-undated}`, is empty, or is not a date):
     `{tier-undated}`, whatever the document column says;
   - an expiry date before the sweep day: `{tier-expired}`;
   - an expiry date from the sweep day up to 7 days ahead: `{tier-7}`; from 8 to 30 days:
     `{tier-30}`; from 31 to 60 days: `{tier-60}`;
   - a date more than 60 days ahead whose document column says there is none, or names a file
     that does not exist in `{supports}`: `{tier-unsupported}`;
   - everything else: no news.
   Every row of every tier table shows the document column (present or not), so a certification
   that lands in a date band and also lacks its document is visible without a second entry.
   A certification whose name is not in the catalog of `{certifications}` is still classified,
   and its name is listed in a short "not in the catalog" section for the team to decide
   whether it enters the catalog or the card is wrong.
4. **Write the report** at the `{expiry-report}` path for the sweep day, in the directory's
   language, with this structure: a header with the date, time, zone, cards read and
   certifications found; the validity reminder (counted from today; validity for a shoot is
   measured against the shoot's date); a summary table with the six tiers and their counts; one
   section per non-empty tier with a table of person, certification, date and document; a
   "no news" paragraph naming the certifications beyond 60 days with their dates and the people
   whose work requires none; and the "not in the catalog" section only when it has content.
   The report of the demo directory, `salidas/vencimientos-2026-09-29.md`, is the reference
   shape: reproduce it exactly from the demo's cards and you have the format right.
5. **Regenerate `{index}`** from the cards: one row per person with specialties, channel and
   language, status, the certifications valid as of the sweep day with their expiries (an
   expired one is named as expired, an undated one as undated, an unsupported one with that
   mark), and the last shoot recorded on the card. The index is for the phone; keep every cell
   to one line and never edit it by hand.
6. **Advance `{state}`**: `last_sweep_at` (ISO date-time with offset), `last_sweep_report`
   (the path written), `last_index_at`, `cards_seen`, `certifications_seen`. Keep `tz` and any
   other key as they were.
7. **Say what you found** in the chat, in the directory's language, in the order of the tiers,
   one line each, and point to the report. If a tier that needs a person is non-empty
   (expired, undated, no document), say which one line closes it ("Fausto trae el carné y la
   fecha entra a su ficha").

**Idempotent.** The report path has the sweep day in its name, so a second run the same day
rewrites that same file with the same content (the header keeps the time of the day's first
run; only the watermark moves to the later time); it never creates a second report for one
day, never touches a card, and leaves the index identical. If the last sweep was more than
seven days ago, say so in one line: the routine missed at least one week, and the person
decides whether to check the account it runs in.

**Where the documents are read from.** A document counts as present when the file the row
names exists in `{supports}`. One installation type records documents by name only: when
`{supports}` holds nothing but its README and that README says the folder names its documents
without storing the files (the plugin's demo works this way), read presence from the table and
say so in one line of the report header, so nobody mistakes a table-only folder for one with
every certificate on file.

## Who is valid on a date

The question that matters on a shoot is not "who has the course" but "whose course covers
that day". The rule, written in `{certifications}` and applied here without exception:

- A certification is **valid for a shoot** when its expiry date is after the shoot's date. A
  course that expires on the 10th does not cover a shoot on the 15th, even though it is valid
  today.
- **Undated never counts as valid.** The team may be sure the person has it; the card does not
  say when it expires, and a shortlist built on certainty instead of a date is how someone ends
  up on a site with an expired course.
- Status matters too: a card marked `{status-paused}` or `{status-do-not-call}` is named apart,
  with its dated reason, because the shortlist skill will not use it.

Answer with the people who qualify, one line each: name, the certification, its expiry, and
the document mark when the document is missing. Then name who was excluded and why, one line
each (expired on which date; undated; paused). Then say who does not have that certification
on their card at all, in one line, so the person knows the search was complete. Every line
carries its source: the card and the date of its current text.

## Renewals

"<Persona> renovó su curso de seguridad, vence el 2027-09-28":

1. Re-read the card right before writing; someone may have edited it since you last saw it.
2. Replace the row in `{card-certifications}` with the new expiry and the issuer if given;
   when the issuer is not given, leave that cell empty and ask for it in the same line as the
   document (keeping the old issuer would be an inference). Move the old row's text to the
   card's `{history}` under a dated entry that names the section changed and who stated the
   renewal (from the roles table; ask once if you do not know who is speaking).
3. The document column of the new row says there is none until a file lands in `{supports}`;
   ask for the photo or PDF in one line, and open a `{gap}` line in `{memory}` naming the
   person and the missing document. Until it arrives the certification shows as
   `{tier-unsupported}` in the next sweep, which is correct, not a defect.
4. If a gap line in `{memory}` was about that certification's missing date, add a dated line
   that closes it (never delete the old one). Regenerate `{index}` and advance only
   `last_index_at` in `{state}`; the sweep fields move only with a sweep.

A renewal is the only edit this skill makes to a card, and only when a person states it with
a date. "Dani says he renewed" without a date is written in `{memory}` as a gap, not on the
card.

## Hard rules

- **You never send anything.** No reminder to a freelancer, no email, no calendar event. The
  report lives in the folder; the person reads it and decides.
- **You never invent a date** and never infer one from the typical validity in the catalog. A
  missing date is `{tier-undated}`, and the fix is a person bringing the document.
- **You never count an undated certification as valid**, in a sweep or in an answer.
- **You never mark a document as present without checking** that the named file exists in
  `{supports}`.
- **You never edit a card** except for a renewal stated with a date, and even then only the
  row concerned, with history.
- **Every claim carries its source**: the card, the row, the date of its current text.

## Done means

- A sweep leaves exactly one report for its day, with the six tier counts plus the
  certifications named under "no news" adding up to the certifications found, every non-empty
  tier listed with person, certification, date and document, and the "no news" paragraph
  naming the rest.
- `{index}` regenerated from the cards as of the sweep day; `{state}` advanced with the five
  keys above.
- Running the sweep again the same day leaves the same report and the same index.
- A question about a date answers only with certifications that expire after that date, lists
  every exclusion with its reason, and names who has no such certification on their card.
- A renewal appears as a new row with the old one in `{history}`, dated and attributed, and
  the document was asked for.
- Nothing left the folder; no card changed except for a stated renewal.

## The failure to watch for

Helpfulness. The person says "Fausto surely has the safety course, he has worked on sites for
years", and the obvious move is to count him in; the card says undated, and undated is the
answer until a date arrives. The person says "put a year from the issue date", and the catalog
says typical validity is one year; a typical validity is not this person's expiry, and a
filled-in date is a certification that looks valid and may not be. A row names a PDF in
`{supports}`, and the obvious move is to trust the row; the folder may not have the file. Each
of those shortcuts produces a cleaner report and a shortlist that puts somebody on a site
without the course the site requires. The report is only useful while every date in it is one
somebody actually wrote down.
