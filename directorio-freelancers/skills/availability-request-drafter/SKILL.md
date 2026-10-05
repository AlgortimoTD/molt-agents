---
name: availability-request-drafter
description: >-
  v1.0.0 · Drafts the availability request for a shoot from a production freelancer
  directory on Google Drive: reads the team's assignment rules and every card, keeps only
  the people whose required certification is valid on the date of the shoot, orders them in
  the team's priority, writes one message per person in their channel and language as a
  draft a human pastes, and keeps the request alive as the team reports who answered, who
  got the job and how they delivered, each answer becoming a dated fact on the card. It never
  sends anything. Use it whenever a production team needs people for a date, reports a
  freelancer's answer, or closes a shoot, even without naming the skill. Triggers: "necesito
  un fotógrafo mañana a las 7 en <lugar>, exige curso de seguridad", "arma la solicitud para
  la producción del <fecha>", "<persona> dijo que sí", "nadie contestó", "cierra la producción
  del puente", "I need a camera operator Friday", "draft the availability request", "who got
  the shoot". [v1.0.0]
---

# availability-request-drafter

## Version 1.0.0

A production team staffs a shoot by messaging the freelancers who could do it and waiting.
What makes that slow is not the typing; it is deciding whom to ask first, remembering who
holds the certification the job requires, and keeping track of who answered. This skill does
that deciding from the folder: the team's written rules say whom to ask for which job and in
what order, every card says what the person does, what not to ask of them and when each
certification expires, and the request file records the whole conversation of one shoot. The
person still sends the messages from their own phone. The value is the filtered list and the
text that is ready, not the sending.

## Where you work

Find the directory the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- directorio-freelancers -->`; otherwise the platform memory entry
`directorio-freelancers: <folder>`; otherwise ask once ("¿cómo se llama la carpeta de tu
directorio en Drive?") and save it. Read that `CLAUDE.md` first: it gives the organization's
name, the working language (every request is written in it), the roles table and the hard
rules, and it outranks this skill wherever they differ.

**Every name comes from the directory.** `CLAUDE.md` ends with a vocabulary block
(`<!-- directorio-freelancers:vocabulary ... -->`) with one `key: name` line per folder,
file, heading, field, state and role, in the directory's language. This skill refers to them
by key in braces and never carries a literal: `{rules}` is the assignment rules file,
`{message-templates}` the tone and structure of a message, `{freelancers}` the cards folder,
`{requests}` the requests folder and `{request-file}` the name pattern of one request;
`{request-requirements}`, `{request-shortlist}`, `{request-excluded}`, `{request-messages}`,
`{request-answers}`, `{request-assigned}`, `{request-invite}` and `{request-closure}` are the
sections of a request; `{mode-sequential}` and `{mode-simultaneous}` the two ways of asking;
`{state-open}`, `{state-assigned}`, `{state-closed}` and `{state-unfilled}` the states of a
request; `{draft-marker}` the first line of every message; `{card-specialties}`,
`{card-limits}`, `{card-certifications}`, `{card-reliability}` and `{card-shoots}` the card
sections you read and write; `{field-status}`, `{field-channel}` and `{field-language}` the
data fields; `{history}` the heading that keeps replaced text; `{memory}` and `{gap}` where a
hole is recorded. Read the block before touching the folder and use the names it gives.

You also read the plugin's `templates/<lang>/solicitud.template.md` when it is reachable: it
is the exact structure of a request. When it is not (a cloud session), the newest file in
`{requests}` is the structure to follow; the demo folder ships one closed request for that.

## The four moments

| The person says | What you do |
|---|---|
| "Necesito un fotógrafo mañana a las 7:00 en la vía norte, exige curso de seguridad en obra" | Open a request: shortlist, exclusions, messages |
| "Bel dijo que sí a las 3:40", "Ariel no puede", "nadie contestó en la ventana" | Log the answers, mark who got it, draft the invite, propose the next person |
| "Cierra la del puente; Bel entregó a tiempo" | Close the shoot: the closure table and one dated fact per person on their card |
| "¿En qué va la solicitud del puente?", "¿quién quedó el viernes?" | Answer from the request file, with its state and the last row of its answers |

Before any write you need to know who is talking: if the conversation has not said it, ask
the name once and find it in the roles table of `CLAUDE.md`. Every row you write names the
person who registered it. That is a trail, not security: the folder's Drive permissions
decide who can change it.

## Opening a request

1. **Parse the shoot.** Date and time (start and end, or start and estimated duration),
   place, what will be done, the role needed and how many people, and the requirement if
   the person names one. Ask for whatever is missing in a single question; do not open a
   request with a blank date. The date is read in the directory's time zone (`{company}`).
2. **Pick the job type** from the table in `{rules}`: the row whose job type matches the
   shoot. Take its principals in their row order, its mode, its wait window and its required
   certification. When the person names a requirement the row does not, the requirement
   wins and you say so; when no row matches, say so, ask which row applies or whether to add
   one, and do not invent principals.
3. **Build the candidate set.** The row's principals plus every card whose
   `{card-specialties}` names the job. Nobody else: a person whose card does not say they do
   this work is not a candidate and does not appear in the exclusions either (an exclusion
   is for someone who could have gone).
4. **Filter, each with a reason you will write.**
   - `{field-status}` must be the active status. A paused or do-not-call card is excluded
     with the status and its dated reason from the card.
   - When the job requires a certification, the card's `{card-certifications}` table must
     list it with an expiry date **after the date of the shoot**. Expired on or before the
     shoot excludes. Undated excludes: "sin fecha" never counts as valid, however likely the
     renewal. A date with no supporting document still counts as valid for the shortlist
     (the sweep reports the missing document; it is not this skill's call to block on it).
   - No line of `{card-limits}` may clash with the job. "No editar con plazo corto" clashes
     with a next-day edit; "no asignar gráficas con texto" does not clash with photography.
     When it clashes, exclude with the constraint quoted and its date.
5. **Order.** Principals first, in the order of the row; then the rest of the candidates in
   the order of their cards. The reason of a principal is their position in the row ("preferido
   del tipo según las reglas", "segunda principal"); the reason of a non-principal is that
   their card names the job. Never reorder by your own judgment of who is better: the order is
   the team's, written in `{rules}`.
6. **Calendar.** When the Google Calendar connector is available, read the calendar named in
   `{sources}` for the shoot's date and record in the requirements table whether the slot is
   free or clashes with an event (name and time). When the connector is not available, write
   "no se leyó" (in the directory's language) and go on; a missing calendar never blocks a
   request. You read the calendar; you never create an event or invite anyone.
7. **Write the request file** at `{request-file}` (the date of the shoot, never the date the
   request was opened, then a short slug of the job, in the directory's language, lower case,
   hyphens, no accents; the title carries the same date), with every section of the template in
   order: state `{state-open}` and who opened it; `{request-requirements}` with the job type,
   the required certification and the shoot's date, mode and window, and the calendar line;
   `{request-shortlist}` as a table with position, person, the reason for that position, the
   certification with its expiry, and channel and language; `{request-excluded}` as a table
   with person and reason; `{request-messages}`; `{request-answers}` as a table with its header
   row only; `{request-assigned}`, `{request-invite}` and `{request-closure}` present with their
   heading and nothing under it; `{history}` with no entries. Changing the state line later, or
   appending rows and facts, needs no `{history}` entry: history is for replaced text, and the
   answers table and the closure already carry the trail of a request.
8. **Write one message per shortlisted person**, under `{request-messages}`, headed by the
   person's name, channel and language. Build it from `{message-templates}`: the seven
   elements in order (greeting with the name, date and time with duration, place, what and
   which role, the requirement if any, until when an answer is expected, who signs), the
   tone of the person's channel, the notes of the person's language. The language is the
   one on the person's card, not the directory's: a card that says inglés gets an English
   message in a Spanish directory. Every message opens with `{draft-marker}`, verbatim. The
   "until when" element depends on the mode: in `{mode-simultaneous}` every message carries the
   same clock time (now plus the window); in `{mode-sequential}` only the first message carries
   a clock time, and the later ones say "within the next N hours" in their language, because
   their send time depends on the silence or the no before them, and a fixed hour would be false
   the moment the first person answers late.
9. **Say how to send them**, in one sentence after the file is written. In `{mode-sequential}`:
   send the first message now, and if there is no answer when the window expires (give the
   clock time), say so and the next message goes out. In `{mode-simultaneous}`: all the
   messages go out together and the first yes gets the job. Then stop. The person pastes.

Also add one line under `{card-shoots}` of every shortlisted card ("en lista corta, posición
N") dated with the shoot's date, the same date as the request file, re-reading each card
first. Facts under `{card-reliability}` keep the date they happened (the day of the answer or
the delivery), which may differ from the shoot's date.

## Logging answers

The request lives until it is closed. Each time the person reports back:

1. Re-read the request file; another surface may have written to it.
2. Append a row to `{request-answers}`: the time the person gives (or the current time in
   the directory's zone when they do not), the freelancer, the answer as said ("sí", "no",
   "sin respuesta en la ventana"), and who registered it.
3. When someone said yes and the request is still `{state-open}`: write their name and the
   time under `{request-assigned}`, set the state to `{state-assigned}`, and draft
   `{request-invite}` from the shoot's data (title, date, time, place, role, requirement, and
   as on-site contact the production coordinator from the roles table unless the person names
   someone else), opening with `{draft-marker}`. The invite is written in the directory's
   language, because it goes into the team's calendar, not to the freelancer; only the messages
   follow the freelancer's language. A person sends the invite from their own calendar; you
   never create it.
4. When the window expired without an answer in `{mode-sequential}`: say which message goes
   out next and log the silence as a row. When the list is exhausted in either mode, apply
   the "when nobody answers" rules of `{rules}` (for example widen to anyone with the
   specialty, or tell the client), write what you did, and set `{state-unfilled}` when the
   team confirms nobody could.
5. Every answer also lands on the person's card: re-read the card, append a dated line under
   `{card-reliability}` with the fact ("respondió sí 35 minutos después del mensaje",
   "no respondió en la ventana de 2 horas") and who registered it, and update their line
   under `{card-shoots}` ("respondió sí · quedó"). Facts, not verdicts: "no respondió" is a
   fact; "poco confiable" is a judgment the team did not make.

A second yes after someone already got the job is logged as a row and answered in the chat
("la producción ya quedó con <persona>"); the assignment does not change unless the person
tells you it does.

## Closing the shoot

"Cierra la del puente; Bel entregó las fotos el martes por la tarde, a tiempo." Re-read the
request, fill the `{request-closure}` table (person, how they delivered as a dated fact,
whether it went to their card), set the state to `{state-closed}` with the date and who
closed it, and append the same dated fact to each person's `{card-reliability}`. A late
delivery is written as the fact with its dates ("entregó el 2026-10-09, dos días después de
lo acordado"), never as an adjective. If the person tells you something the card should
remember beyond this shoot (a new limit, a preference), that is `production-pool-roster`'s
job: say so and hand it over in one line, do not write it from here.

## Hard rules, and why

- **Never send a message or an invite, and never offer to.** Even where the platform has a
  WhatsApp or Messenger piece, this agent does not write to the freelancers: the contract the
  customer confirmed says so, and the value is the filtered list and the ready text. Sending
  is the person's act, from their own phone, with their own name.
- **Never book, hire or pay.** A yes recorded here is information for the team, not a
  contract. The invite is a draft a person sends.
- **The date is not negotiable.** The shoot is when the client needs it. A person who cannot
  make that date is excluded, not accommodated; you do not propose moving the shoot.
- **No exclusion without a written reason**, and the reason is a fact of the card or the rules
  (an expiry date, an undated certification, a status, a constraint), never an impression.
- **Nothing judgmental on a card.** Only facts with date and author. The judgment stays with
  the team, which is the third line of what this agent does not do.
- **Re-read before writing.** Cards and requests are edited by people and by other skills;
  write on the current text, and keep the replaced text under `{history}` when you replace
  rather than append.
- **Never write outside the folder.** Your writes are the request file and the cards. No
  calendar events, no messages, no files elsewhere.
- **What is not written is said.** A job type with no row in `{rules}`, a candidate with no
  channel on their card, a requirement nobody can meet: say it, record it as a `{gap}` line
  in `{memory}` when it will recur, and do not fill it in.

## Done means

- The request file exists at `{request-file}`, in the directory's language, with every
  section of the template present, the state set, and who opened it.
- Every shortlisted person meets the requirement on the date of the shoot, in the order of
  `{rules}`, with a written reason; every excluded candidate has a written reason that cites
  the card or the rules; nobody outside the candidate set appears.
- One message per shortlisted person, in that person's channel and language, with the seven
  elements, opening with `{draft-marker}`; and one sentence saying how to send them according
  to the mode.
- Every answer the team reported is a row with time and author, and a dated fact on the
  person's card; who got it and the invite text are written when someone said yes.
- A closed request has its closure table and the facts on the cards.
- Nothing was sent, created in a calendar or written outside the folder.

## The failure to watch for

Helpfulness. The obvious next step after writing three perfect messages is to send them, or
to ask "¿quieres que los envíe?", and both break the one promise the customer bought. The
second failure is kindness to a candidate: shortlisting someone whose certification is undated
or expired because they "probably renewed", which puts a person on a construction site the
rules say they cannot be on. The third is summarizing: writing "poco confiable" on a card
instead of "no respondió en la ventana de 2 horas el 2026-10-06", which turns a fact the team
can weigh into a verdict the agent made. The fourth is flattening the two modes into one and
sending everything to everyone, which is exactly the behavior the team wanted to stop.
