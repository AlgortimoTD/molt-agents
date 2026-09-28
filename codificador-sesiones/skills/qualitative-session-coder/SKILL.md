---
name: qualitative-session-coder
description: >-
  v1.0.0 · Code qualitative research sessions (interviews, focus groups) in a team's research
  folder the way that team codes by hand. Reads a transcript (Fathom or the study's inbox), the
  codebook, the team's format, criteria and a study they coded, and writes the coded session: per
  participant and variable, the category and the verbatim quote with its minute. Proposes new
  categories with evidence, never applies them alone; changes the codebook only when asked;
  regenerates the matrix; runs the fidelity test. Use it whenever someone wants a session or
  transcript coded or added to the matrix, a category accepted or retired, or asks what
  participants said about a variable. Triggers: "codifica la sesión de hoy", "codifica el
  transcript que está en entrada", "acepta recreación como categoría", "qué dijo la gente del
  grupo 2 sobre", "corre la prueba de fidelidad", "code this focus group". [v1.0.0]
---

# qualitative-session-coder

## Version 1.0.0

A research team spends most of its analysis days turning transcripts into codes: after each
session someone types the answers into a spreadsheet, and later, when they analyze, they go back
to the recording to find the exact sentence. This skill does that first pass with the quote
already attached, so the team reviews codes instead of producing them, and every code can be
traced back to the thirty seconds that produced it.

The value is fidelity, not speed. A team that has coded studies for years has a sense of when
"skating" and "the gym" are the same answer and when a new idea deserves its own name. If your
coding does not look like theirs, they redo it, and the skill saved nothing. Everything below
serves one goal: a coded session the team recognizes as their own work.

## Where you work

You operate inside a **research folder**, a shared folder (usually on Google Drive, opened as a
project in Cowork or Claude Code) whose `CLAUDE.md` starts with `<!-- codificador-sesiones -->`.
Find it in this order: the working folder has that marker; otherwise the platform memory holds
`codificador-sesiones: <folder>`; otherwise ask once which folder it is and save the answer.

Read its `CLAUDE.md` first. It names the team, the roles, the working language and the map of
files, and it wins over anything written here, because it is the team's configuration and this
skill is not.

**Every name comes from the folder's vocabulary block**, the HTML comment at the end of
`CLAUDE.md` with one `key: name` line per thing. This skill refers to each by its key in braces:
`{codebook}` is the codebook, `{sessions-inbox}` the inbox. Names under a study are relative to
`{studies}<study-slug>/`. If the block is missing or lacks a key you need, stop and say so:
guessing a name creates a second file next to the real one.

**Which study.** Use the one the person names. Otherwise infer it from the recording title or the
inbox file (the study code is usually in it); if the folder has a single active study, use it;
otherwise ask, naming the candidates. Never code a session into the wrong study to avoid asking:
its categories would be wrong from the first row.

**The working language is the folder's.** Labels, summaries and notes go in it. Quotes stay in
the language in which they were said, verbatim.

## What you can be asked

| The person says | Mode |
|---|---|
| "codifica la sesión de hoy del grupo 3", "codifica el transcript que está en entrada" | Code a session |
| "acepta recreación como categoría", "retira X", "renombra X a Y", "agrega la variable Z" | Change the codebook |
| "¿qué dijo la gente del grupo 2 sobre X?" | Answer from the coded sessions |
| "corre la prueba de fidelidad" | Fidelity test |

Crossing variables ("cruza X con Y") is not this skill: it belongs to `cross-variable-analyzer`,
which reads the matrix this skill regenerates.

## Mode 1: code a session

### 1. Pick the sessions, and skip what is done

`{state}` lists the sessions already coded in this study:

```json
{
  "last_coded_at": "2026-09-28T16:10:00-05:00",
  "codebook_updated_at": "2026-09-27",
  "processed": [
    {"id": "fathom:811868585", "session": "2026-09-28-g3-grupo-focal", "coded_at": "2026-09-28T16:10:00-05:00"}
  ]
}
```

Take what the person asked for: a Fathom recording (by title, by id, or "today's", resolved with
the connector's meeting list and the rule written in `{team}`), or the files in
`{sessions-inbox}` (their id is `inbox:<file name>`). Skip any id already in `processed`, and say so: "esa sesión ya está
codificada en <file>". Working from ids is what makes a second run harmless; recoding a session
on purpose is a separate request the person makes explicitly.

### 2. Calibrate before you code

Read, in this order, and let each shape what you do:

1. `{output-format}`: the matrix columns and their role keys, how a quote is written, how a
   category is named, how participants are coded.
2. `{quality-criteria}`: the team's own words about grouping level, when a new category is
   warranted, and their examples of good and bad codes.
3. One study in `{examples}`: its codebook and its hand-made matrix, next to one of its
   transcripts. Look at how broad their categories are, how long their quotes are, what they
   leave uncoded. You are learning their judgment, not borrowing their categories: an example
   study's categories never enter the current study's codebook.
4. The current study: `{study}` (objectives, hypotheses, target groups) and `{codebook}`. The
   **active** categories are the `{fixed}` and `{emergent-accepted}` ones. `{emergent-proposed}`
   and `{retired}` categories are never used to code.
5. The moderator guide for the session's group in `{guides}`, if there is one: it tells you which
   question feeds which variable.

If `{examples}` is empty, code anyway, and say in the run summary that no calibration example
was available: the team should know the coding was not measured against their own.

### 3. Identify the participants

Code them the way `{output-format}` says (by default P1, P2 in order of first appearance). Never
write a name in a code, a quote you keep in the coding table, or the matrix; the transcript
section keeps the original as it came, and nothing leaves the folder.

The moderator is not a participant; their questions give context but are never coded. In a focus
group, attribute every turn to its speaker. When the transcript does not say who spoke, the
participant column says `{unidentified}` (in the participant column, not only in the note): a code attributed to the wrong person is worse than an
honest gap, because the crosses by group would count it in the wrong place.

### 4. Code

For each participant and each variable of the codebook, find what they said that bears on it:

- **One row per code.** A participant who said two things that fall in two categories of the same
  variable gets two rows. A participant who said nothing about a variable gets no row: absence is
  not a category.
- **Every row carries the verbatim quote and its minute.** The quote is the sentence that
  justifies the category, copied exactly, with `(...)` for what you omit, long enough to stand
  alone. The minute is the transcript's timestamp for that turn; if the transcript has none, use
  the nearest preceding one and note it. Write the minute in the form the transcript uses (`0:42`,
  `12:40`, `1:05:10`); do not reformat it. A row without a quote is not written, whatever you
  believe the participant meant.
- **Match the team's grouping level.** If their example groups "skating" and "the gym" as
  "sporty", do the same with "cycling"; do not open a category per activity.
- **An explicit "nothing" is not a category.** "Nada en especial" to the barrier question is
  an answer, not a code: treat it like any passage that fits no category (uncategorized, or a
  proposal if two participants say it), never as a coded row.
- **Mark what is unclear.** A garbled sentence, a cross-talk turn, a word the transcription
  clearly got wrong: keep the quote as written and add `{doubtful-quote}` in the note. Do not
  repair it into what you think was said.

Long sessions (a focus group of an hour or more) go block by block of the guide, or participant
by participant, writing as you go; one pass over the whole transcript is where rows get lost.

### 5. What does not fit the codebook

A passage that bears on a variable and fits no active category has two destinations:

- **A proposal**, when the same new idea comes from **at least two different participants**,
  counting this session and the `{uncategorized}` sections and pending proposals of the sessions
  already coded. Add it to `{proposals}` with the variable, the proposed name (named by what it
  groups, per `{output-format}`), what it groups, and the evidence (participant, session and
  minute of each quote), in state `{proposal-pending}`. If a pending proposal already covers it,
  add the new evidence to that one instead of opening a second. A `{proposal-rejected}` proposal
  is not raised again; if strong new evidence appears, mention it in the run summary and let the
  person decide.
- **`{uncategorized}`**, when only one participant said it. It stays in the session file with its
  participant, variable, quote and minute, so a later session can turn it into a proposal.

A proposal never codes a row. It is a question for the team ("¿esto es recreación?"), and naming
and grouping is research judgment that belongs to them. Forcing the passage into the nearest
active category is the worst option: it looks like data and it is a guess.

### 6. Write the session file

`{sessions}<AAAA-MM-DD>-<group>-<type>.md` (lower case, hyphens, no accents), from the session
template: header, `{summary}` (five to eight lines, what was talked about, no interpretation),
`{participants}`, `{coding}` (the table: participant, variable, category, quote, minute, state
`{coded}`, note), `{uncategorized}`, `{session-proposals}`, and `{transcript}` with the original
text, whole. Empty sections say so in one word; a missing section reads as a skipped step.

A transcript from `{sessions-inbox}` is removed from the inbox only after its full text is in the
session file: that is a move, not a deletion. A Fathom transcript is kept the same way, so the
folder never depends on the recorder to answer "what exactly was said".

### 7. Regenerate the matrix

`{matrix}` is rebuilt from the `{coding}` tables of **every** session file of the study, never
edited in place: session files ordered by name, rows in table order, the columns and headers of
`{output-format}`, one row per code, UTF-8 with a header, quotes escaped for CSV (double quotes
inside a field doubled). In the session file the quote goes between double quotes; in the CSV the
cell holds the quote's text, and the CSV quoting is the only quoting. Because each session is its own file and the matrix is derived, several
researchers can code different sessions at the same time without overwriting each other, and the
matrix is always exactly what the sessions say.

### 8. Run summary, then the watermark

Write `{run-summary}` (dated by the day of the run): sessions coded, rows per variable,
participants, proposals opened or reinforced, passages left uncategorized, doubtful quotes,
whether a calibration example was available. Tell the person the same in five lines and point to
the files.

Then append to `{state}` `processed` (id, session file, time) and update `last_coded_at`.
**Advance the watermark last**: if anything failed halfway, the next run picks the session up
again.

## Mode 2: change the codebook, because a person asked

The codebook belongs to the team. You change it only when a person asks in the chat, and every
change goes to its `{history}` table with the date, the change, the reason they gave and who asked
(the name they give, or "sin nombre" if they give none; an unnamed request is applied). Nothing is
deleted. The roles in `{team}`
say who may decide; you cannot verify who is writing, so a request from someone the folder lists
as `{role-viewer}` is written to `{memory}` for the lead instead of applied.

| Request | What changes |
|---|---|
| Accept a proposal | The category enters the variable as `{emergent-accepted}` with the date; the proposal goes to `{proposal-accepted}` with who decided. The evidence quotes in the session files become coded rows (move them from `{uncategorized}` or `{session-proposals}` into `{coding}`), and the matrix is regenerated. Say that sessions coded earlier may hold more instances and offer to recode that variable in them. |
| Reject a proposal | `{proposal-rejected}` with the reason. Nothing else moves. |
| Add a category or a variable directly | Enters as `{fixed}` with the date. Offer to recode the sessions already coded for that variable. |
| Rename a category | The new name replaces the old one in the codebook and in the `{coding}` tables of the session files; the history records the old name and how many rows changed. Meaning does not change, so rows stay `{coded}`. |
| Retire a category (or split, or merge) | It stays in the table as `{retired}` with the date and reason. Every row that used it becomes `{to-recode}`, in the session files and in the regenerated matrix. A split or a merge is a retirement plus the new categories. |

After any change, update `codebook_updated_at` in `{state}` and regenerate the matrix.

**Recoding** a session is an explicit request ("recodifica la sesión X para la variable Y"): code
that variable again with the current codebook, replace those rows in the session file, record in
the session header the date and the reason, and regenerate the matrix.

## Mode 3: answer from the coded sessions

"¿Qué dijo la gente del grupo 2 sobre X?" is answered from the `{coding}` tables and quotes of the
session files, never from memory of a conversation: the category counts by group with their n,
and the quotes with participant, session and minute. If the question touches something no
variable covers, say so, and search the transcripts for it as a plain search, labeled as such.
Never answer "people think" without the quotes; the whole point of this folder is that every
statement can be traced.

## Mode 4: the fidelity test

This is how the team decides whether to trust the coding, so it has to be **blind**: you code a
session without having seen how the team coded it. Take one session of a study in `{examples}`
that the team coded by hand (its transcript and its rows in the hand-made matrix): the one the
person names, or the most recent.

1. **Calibrate without the answer key.** Read `{output-format}`, `{quality-criteria}` and the
   example study's codebook. Read the hand-made rows of the example's **other** sessions, if it
   has any; never the rows of the session under test. If the example has a single session, you
   calibrate on the criteria and the codebook alone, and the report says so.
2. **Code it** following steps 3 to 5 of Mode 1, with **that example study's codebook**, keeping
   the result in the report only: no session file, no matrix, no watermark, no run summary. The
   example's codebook, transcripts and hand-made matrix are never modified.
3. **Only then read the team's rows for that session, and compare.** The unit is a hand-coded
   row, that is, a participant, a variable and a category. A row **matches** when you coded the
   same participant, variable and category. Every hand row you did not match is a difference,
   classified as more specific, more general, different category or missing (you coded nothing
   for that participant and variable); every row you coded that they did not is an extra, listed
   separately. Same category with a different quote is not a difference: note it as an
   observation when the quote you chose would not carry the category on its own.
4. **Fidelity** is matched hand rows over hand rows. The threshold is in `{quality-criteria}`
   (80 percent when it says none, and say that the default applied).
5. **Write the report** to `{examples}<example>/{fidelity-report}`, the only file this mode
   creates: the percentage and the threshold, how you calibrated (which sessions, or criteria
   only), the table of differences with both quotes side by side, the extras, the observations,
   and for each difference a line the team can answer ("error del agente", "criterio no
   escrito", "mejora aceptable").

Under the threshold, end the report with the text you would add to `{quality-criteria}` so the next
run matches them better, and write it there only when the lead agrees. Above it, say so plainly and
still list every difference: a high number with an unread difference is how a team learns to trust
the wrong thing. A single example session also caps what the test proves; say so and suggest the
team keep a second hand-coded session aside for testing only.

## How you write to the folder

Through the synced folder when it is open as the project; otherwise through the Google Drive
connector, or the organization's Google Workspace MCP if the connector cannot edit a file in
place. The destination is the research folder and nothing else. **You never write outside it**:
no email, no message, no document for the client. The transcripts carry what participants said
in confidence, and that promise is why the team lets you read them.

## Done means

- Every session asked for has its file in `{sessions}` with all sections, and every coding row
  has a verbatim quote, a participant code and a minute.
- No name of a participant appears in `{coding}`, `{proposals}` or `{matrix}`.
- Only active categories were used; everything else is in `{uncategorized}` or `{proposals}`.
- `{codebook}` changed only if a person asked in this run, with its `{history}` line.
- `{matrix}` equals the union of the `{coding}` tables, in the columns of `{output-format}`.
- The inbox holds no transcript that is already in a session file.
- The watermark advanced last, and **running again on the same session changes nothing**.

## Three failures worth naming

**Forcing a fit.** The passage is close to an active category and it would be tidy to put it
there. Don't: an uncategorized passage costs the team a glance, a wrong code costs them a wrong
finding.

**Coding your judgment instead of theirs.** Your categories may be sensible and still not be how
this team groups. When the example and your instinct disagree, the example wins; when there is no
example, say so.

**Quotes that do not say what the code says.** The team will open the quote exactly when they
doubt the code. If the quote does not carry the category on its own, the row fails at the moment
it matters.
