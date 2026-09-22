---
name: transcript-to-playbook-updater
description: >-
  v1.1.1 · Turn a recorded meeting into playbook updates and a dated decision log inside a company
  brain folder, in the brain's own language. Reads one transcript (pulled by a Fathom connector or
  dropped into the brain's meetings inbox), writes the meeting file, appends the decisions it can
  quote, rewrites only the playbook sections those decisions changed, and keeps the replaced text in
  the playbook's history. It never deletes, never applies a change to company values without the
  owner's approval, and marks what it inferred as pending. Use it whenever someone wants a meeting
  turned into process documentation, or the brain's daily ingestion run. Triggers: "ingest this
  transcript", "update the playbooks from this meeting", "what did we decide in this call", "run the
  brain ingestion", "procesa este transcript", "actualiza los playbooks con esta reunión", "corre la
  ingesta del cerebro", "qué decidimos en esta reunión". [v1.1.1]
---

# transcript-to-playbook-updater

## Version 1.1.1

A team's real process lives in conversation. Someone says "from now on we send nothing
without a discovery call", everybody nods, and six weeks later the written playbook still
describes the old way. This skill closes that gap without adding a chore: it reads the
transcript the meeting already produced and writes the change down, with the quote that
justifies it.

The value is in restraint. An hour of informal conversation contains dozens of opinions and
two or three actual decisions. A skill that writes down everything that sounded decisive is
worse than no skill at all, because it fills the playbooks with things nobody agreed to and
the team stops trusting them. Most of what follows is about telling those apart.

## Where you work

You operate inside a **brain folder**: a shared folder the team keeps its written knowledge
in. Read its `CLAUDE.md` first. It names the company, the working language, the roles and the
map of files, and it is the authority on all of them. If a rule here and a rule in that
`CLAUDE.md` disagree, the folder wins, because it is the customer's configuration and this
skill is not.

**Every name comes from the brain, never from you.** The brain works in one language, and
every folder, file, heading, marker and state is named in it. `CLAUDE.md` ends with a
vocabulary block (`<!-- cerebro-operativo:vocabulary ... -->`) with one `key: name` line per
thing. This skill refers to each by its key in braces: `{log}` is the decision log, `{history}`
the heading that keeps replaced text. Read the block before touching anything and use exactly
the names it gives. If `CLAUDE.md` has no vocabulary block, or a key you need is missing, stop
and say so: guessing a name creates a second file next to the real one.

The layout you can count on, by key:

```
CLAUDE.md             the brain's orchestrator: language, roles, rules, file map, vocabulary
{memory}              loose agreements and gaps, one dated line each
{company}             who they are, the team, the fronts
{values}              values, negotiables, non-negotiables
{voice}               the company's voice guide
{sources}             which meetings enter, time zone, working language, roles
{playbooks}<process>.md   one file per process, each with its {history} section
{log}                 append only: date, decision, reason, meeting, playbook, requested by, state
{cases}<case>.md      past cases and what was learned
{documents}           documents the organization already had; never edited
{meetings}<YYYY-MM-DD>-<title>.md   an ingested transcript plus its summary and decisions
{meetings-inbox}      transcripts dropped in by hand land here
{ingestion-report}    what one run took in and what it changed
{state}               the watermark: the last transcript processed
```

**The working language is the brain's, never yours.** Everything you write into the folder
goes in it, whatever language the transcript or the person asking happens to be in. A team
that reads its playbooks in Spanish should not find an English section in the middle because
one meeting was in English.

## How a run goes

### 1. Read the watermark, then pick the transcripts

`{state}` records what you already processed (its JSON keys are the same in every language):

```json
{
  "last_processed_at": "2026-09-18T13:00:00-05:00",
  "last_meeting_id": "fathom:811868585",
  "processed": [
    {"id": "fathom:811868585", "date": "2026-09-18", "title": "Meet diario", "ingested_at": "2026-09-18T13:02:11-05:00"}
  ]
}
```

Take every meeting newer than the watermark **and** every transcript sitting in
`{meetings-inbox}`, and skip any id already in `processed`. Working from the id list rather
than from a timestamp is what makes a second run harmless: a recorder that publishes a
transcript late still gets picked up on the next run, and running twice in one afternoon
changes nothing.

Which meetings count is written in `{sources}`, not decided by you. Usually it is the internal
meetings of one team, with client calls excluded unless somebody marked them.

If there is nothing new, say so, write no meeting file, and leave every other file alone.
A run with nothing to do is a normal outcome, not a failure.

### 2. Read the transcript against the folder

Before deciding anything, read `{values}`, the playbook files and the last entries of `{log}`.
You are looking for what the meeting **changed**, and you cannot see a change without knowing
what was there before.

A kickoff meeting (the one the installation asks for) goes through the playbooks one by one
and says "still like this", "changed to this" or "we no longer do this". Treat each of those as
an explicit decision about that section: a confirmation leaves the text untouched and adds
one log line with state `{confirmed}`; a change rewrites the section; a "no longer" with a
replacement ("we no longer do X, from now on Y") is a change like any other; a bare "no longer"
replaces the section with one line saying so. In the last two the old text goes to `{history}`
as always. When every section of a playbook came out confirmed or changed, update the state
line at its top from seed to current, citing the meeting.

### 3. Separate decisions from conversation

Only an **explicit** decision reaches a playbook. The signal is the language people use when
they are committing, not when they are thinking out loud. In Spanish: "de ahora en adelante",
"dejemos de", "siempre", "nunca más", "quedamos en", "vamos a", "a partir de hoy", "ya no".
In English: "from now on", "let's stop", "always", "never again", "we agreed", "going
forward". Add a change of process stated as a fact ("we moved to another platform"), and an
action item somebody owns.

Everything else is conversation. Three shapes get confused with decisions, and each has its
own destination:

- **A wish or an idea.** "It would be great if something checked the posts." Nobody committed.
  It goes in the run report as discarded, not in a playbook.
- **An inference of yours.** The conversation implies a rule but nobody stated it. Write it
  in `{log}` with state `{to-confirm}` and **do not touch any playbook**. That state is what
  lets a person confirm it later in one line instead of arguing with a change that already
  happened.
- **A change to values, negotiables or non-negotiables.** These are the part of the brain
  that decides how the company answers a client. A bad extraction there changes real answers,
  so you never apply it from a meeting: you write the proposal in the `{ingestion-report}`
  under `{value-proposals}` and leave `{values}` exactly as it was. The brain owner, named in
  the roles table of `{sources}`, approves. When they confirm, applying it is a separate,
  explicit change, logged with them as the person who requested it. This holds even when the
  brain owner is the one speaking in the meeting: from a transcript it is always a proposal.
  Tentative talk about a value ("maybe we should stop X, let's think about it") is not a
  proposal: it goes to discarded with its minute, like any other idea nobody committed to.

Every decision you do record carries its source: the meeting and the minute, plus the quote
when it is short. That is not bookkeeping. It is what lets somebody who disagrees with a line
go listen to the thirty seconds that produced it.

### 4. Write the meeting file

`{meetings}<YYYY-MM-DD>-<title-in-lower-case-with-hyphens>.md`, every label in the brain's
language:

```markdown
# <Meeting title> - <YYYY-MM-DD>

- <Source>: <fathom:<id> | {meetings-inbox}<file>>
- <Participants>: <names as the transcript gives them>
- <Duration>: <minutes>

{meeting-summary}

<Five to ten lines. What the meeting was about and what came out of it.>

{meeting-decisions}

| # | <Decision> | <Minute> | <Quote> | Playbook | <State> |
|---|---|---|---|---|---|
| 1 | <one sentence> | 25:24 | "<short quote>" | {playbooks}<process>.md | {applied} |

{meeting-pending}

<Inferences, with their minute. Empty is a valid section; say so in one word.>

{meeting-discarded}

<What sounded like a decision and was not, and why. This section is how a
reader checks your filter instead of trusting it.>

{meeting-transcript}

<The original transcript, whole and unedited.>
```

A transcript that came from `{meetings-inbox}` is kept whole in that last section, and only
then is its file removed from the inbox. That is a move, not a deletion: the text lives on in
the meeting file, and an empty inbox is how the audit knows nothing is waiting. A transcript
pulled from Fathom is kept the same way, so the folder never depends on the recorder to
answer "what exactly was said".

### 5. Append to the decision log

`{log}` is append only. New lines go at the end and you never rewrite an existing one. Use the
columns its header declares; for a line that comes from a transcript, the "requested by"
column says "meeting" in the brain's language, as the header note of `{log}` puts it. In a
Spanish brain:

```markdown
| 2026-09-18 | Documentar a los freelancers de producción | Todo el criterio vive en la cabeza de dos personas | Meet diario 2026-09-04, 25:24 | playbooks/produccion.md | reunión | aplicada |
```

States: `{applied}` (a playbook changed), `{confirmed}` (a written section still holds; no
text changed), `{to-confirm}` (inferred, no playbook touched), `{proposed}` (it touches values
and waits for the brain owner), `{open}` (an owned action not yet done).

### 6. Touch the playbooks, and only the sections that changed

Rewrite the affected section, and move the replaced text into that file's `{history}` with
the date. Nothing is deleted, ever. That is not caution for its own sake: the whole reason
the team wanted this was to know where the decisions that modify a process live, and a change
you cannot see is a change you cannot undo when the extraction was wrong.

In a Spanish brain (`{current-since}` always goes inside an HTML comment):

```markdown
## Cómo coordinamos una producción

<!-- Vigente desde 2026-09-18 (origen: reunión 2026-09-18, minuto 25:24) -->
<new text>

## Historial

### 2026-09-18 · Cómo coordinamos una producción · reemplazada por la decisión de la reunión 2026-09-18 (25:24)

<the previous text, untouched>
```

In an English brain the same shape reads `Current since`, `## History` and "replaced by the
decision of the meeting". Follow the history format the playbook itself declares.

If the playbook a decision belongs to does not exist, create it with **one** section, the one
this decision is about, plus an empty `{history}`. Do not invent the rest of the process: an
empty heading promises content that nobody wrote.

### 7. Write the run report and advance the watermark

The `{ingestion-report}`, dated by the day the RUN happened and not by the meeting (one run can
take in several meetings, and a person looking for what happened yesterday looks for
yesterday), is what a person reads to check your work in a minute: transcripts taken in,
decisions recorded and where, what stayed pending confirmation, value changes waiting for the
brain owner under `{value-proposals}`, and what you discarded. Then update `{state}`, appending
to `processed` rather than replacing it. `last_processed_at` is the date and time of the newest
meeting taken in (not of the run), and an inbox transcript gets the id `inbox:<file name>`.

Advance the watermark **last**. If something failed halfway, the next run should pick the
transcript up again, and it only can if you did not already mark it done.

## How you write to the folder

The run may not have the folder mounted locally. Write through the Google Drive connector if
it can create and edit files in place; if it cannot, use the organization's Google Workspace
MCP (`drive_files_update`). Either way, the destination is the brain folder and nothing else.

**You never write outside it.** No email, no message, no post, no ticket. This is the first
promise the brain makes to its team, and the reason they are willing to let it read every
internal meeting.

## Done means

- Every new transcript has its file in `{meetings}`, its lines in `{log}`, and its playbook
  edits applied or explicitly marked pending.
- No playbook lost text: every replaced section is in `{history}` with its date.
- `{values}` is byte-identical unless the brain owner's approval was granted in this run and
  recorded.
- The watermark advanced and the `{ingestion-report}` exists.
- Every name you wrote came from the vocabulary block; nothing is named in another language.
- **Running again on the same transcript changes nothing.** Check it: it is the one property
  that lets a daily routine run unattended.

## Two failures worth naming

**Over-extraction** is the common one. An informal meeting wanders, and a reader who wants to
be useful hears commitment everywhere. When in doubt, `{to-confirm}` costs a person ten
seconds and a wrong playbook edit costs an argument.

**Silent under-extraction** is the quiet one. If you discard something, it goes in the
`{meeting-discarded}` section with a reason. A filter nobody can see is a filter nobody can
fix.
