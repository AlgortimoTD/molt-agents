---
name: transcript-to-playbook-updater
description: >-
  v1.0.0 · Turn a recorded meeting into playbook updates and a dated decision log inside a
  company brain folder. Reads one transcript (pulled by a Fathom connector or dropped into
  reuniones/entrada/), writes the meeting file, appends the decisions it can quote, rewrites
  only the playbook sections those decisions changed, and keeps the replaced text under
  Historial. It never deletes, never applies a change to company values without approval, and
  marks anything it inferred as pending confirmation. Use it whenever someone wants a meeting
  turned into process documentation, or the brain's daily ingestion run. Triggers:
  "ingest this transcript", "update the playbooks from this meeting", "what did we decide in
  this call", "run the brain ingestion", "procesa este transcript", "actualiza los playbooks
  con esta reunión", "corre la ingesta del cerebro", "qué decidimos en esta reunión". [v1.0.0]
---

# transcript-to-playbook-updater

## Version 1.0.0

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
in. Read its `CLAUDE.md` first. It names the company, the working language and the map of
files, and it is the authority on all three. If a rule here and a rule in that `CLAUDE.md`
disagree, the folder wins, because it is the customer's configuration and this skill is not.

The layout you can count on:

```
CLAUDE.md                     the brain's orchestrator: language, rules, file map
memory.md                     loose agreements, one dated line each
_config/
  empresa.md                  who they are, the team, the fronts
  valores-y-negociables.md    values, negotiables, non-negotiables
  voz.md                      the company's voice guide
  fuentes.md                  which meetings enter, timezone, working language, who approves what
playbooks/<proceso>.md        one file per process, each with a Historial section
decisiones/bitacora.md        append only: date, decision, reason, meeting, playbook, state
casos/<caso>.md               past cases and what was learned
reuniones/
  <YYYY-MM-DD>-<titulo>.md    an ingested transcript plus its summary and decisions
  entrada/                    transcripts dropped in by hand land here
salidas/ingesta-<YYYY-MM-DD>.md   what one run took in and what it changed
_estado/ultima-ingesta.json   the watermark: the last transcript processed
```

**The working language comes from the folder, never from you.** Read it from `CLAUDE.md`
and, if it says so more precisely, from `_config/fuentes.md`. Everything you write into the
folder goes in that language, whatever language the transcript or the person asking happens
to be in. A team that reads its playbooks in Spanish should not find an English section in
the middle because one meeting was in English.

## How a run goes

### 1. Read the watermark, then pick the transcripts

`_estado/ultima-ingesta.json` records what you already processed:

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
`reuniones/entrada/`, and skip any id already in `processed`. Working from the id list
rather than from a timestamp is what makes a second run harmless: a recorder that publishes
a transcript late still gets picked up on the next run, and running twice in one afternoon
changes nothing.

Which meetings count is written in `_config/fuentes.md`, not decided by you. Usually it is
the internal meetings of one team, with client calls excluded unless somebody marked them.

If there is nothing new, say so, write no meeting file, and leave every other file alone.
A run with nothing to do is a normal outcome, not a failure.

### 2. Read the transcript against the folder

Before deciding anything, read `_config/valores-y-negociables.md`, the playbook files and
the last entries of `decisiones/bitacora.md`. You are looking for what the meeting **changed**,
and you cannot see a change without knowing what was there before.

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
  in the bitácora with state `por confirmar` and **do not touch any playbook**. That state is
  what lets a person confirm it later in one line instead of arguing with a change that
  already happened.
- **A change to values, negotiables or non-negotiables.** These are the part of the brain
  that decides how the company answers a client. A bad extraction there changes real answers,
  so you never apply it: you write the proposal in `salidas/ingesta-<fecha>.md` under
  "Cambios propuestos a valores, esperando aprobación" and leave
  `_config/valores-y-negociables.md` exactly as it was. `_config/fuentes.md` names who
  approves. When that person confirms, applying it is a separate, explicit run.

Every decision you do record carries its source: the meeting and the minute, plus the quote
when it is short. That is not bookkeeping. It is what lets somebody who disagrees with a line
go listen to the thirty seconds that produced it.

### 4. Write the meeting file

`reuniones/<YYYY-MM-DD>-<titulo-en-minusculas-con-guiones>.md`:

```markdown
# <Meeting title> - <YYYY-MM-DD>

- Fuente: <fathom:<id> | reuniones/entrada/<archivo>>
- Participantes: <names as the transcript gives them>
- Duración: <minutes>

## Resumen

<Five to ten lines. What the meeting was about and what came out of it.>

## Decisiones extraídas

| # | Decisión | Minuto | Cita | Playbook | Estado |
|---|---|---|---|---|---|
| 1 | <one sentence> | 25:24 | "<short quote>" | playbooks/produccion.md | aplicada |

## Por confirmar

<Inferences, with their minute. Empty is a valid section; say "Ninguna".>

## Descartado

<What sounded like a decision and was not, and why. This section is how a
reader checks your filter instead of trusting it.>
```

### 5. Append to the decision log

`decisiones/bitacora.md` is append only. New lines go at the end and you never rewrite an
existing one:

```markdown
| 2026-09-18 | Documentar a los freelancers de producción | Todo el criterio vive en la cabeza de dos personas | Meet diario 2026-09-04, 25:24 | playbooks/produccion.md | aplicada |
```

States: `aplicada` (a playbook changed), `por confirmar` (inferred, no playbook touched),
`propuesta` (it touches values and waits for approval).

### 6. Touch the playbooks, and only the sections that changed

Rewrite the affected section, and move the replaced text into that file's `## Historial`
with the date. Nothing is deleted, ever. That is not caution for its own sake: the whole
reason the team wanted this was to know where the decisions that modify a process live, and
a change you cannot see is a change you cannot undo when the extraction was wrong.

```markdown
## Cómo coordinamos una producción

<!-- Vigente desde 2026-09-18 -->
<new text>

## Historial

### Cómo coordinamos una producción (vigente hasta 2026-09-18)

<the previous text, untouched>

Cambió por: decisión del 2026-09-18 (Meet diario, 25:24).
```

If the playbook a decision belongs to does not exist, create it with **one** section, the one
this decision is about, plus an empty `## Historial`. Do not invent the rest of the process:
an empty heading promises content that nobody wrote.

### 7. Write the run report and advance the watermark

`salidas/ingesta-<YYYY-MM-DD>.md`, dated by the day the RUN happened and not by the meeting
(one run can take in several meetings, and a person looking for what happened yesterday
looks for yesterday), is what a person reads to check your work in a minute: transcripts
taken in, decisions recorded and where, what stayed pending confirmation, value changes
waiting for approval, and what you discarded. Then update
`_estado/ultima-ingesta.json`, appending to `processed` rather than replacing it.

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

- Every new transcript has its file in `reuniones/`, its lines in the bitácora, and its
  playbook edits applied or explicitly marked pending.
- No playbook lost text: every replaced section is in Historial with its date.
- `_config/valores-y-negociables.md` is byte-identical unless an approval was granted in this
  run and recorded.
- The watermark advanced and `salidas/ingesta-<fecha>.md` exists.
- **Running again on the same transcript changes nothing.** Check it: it is the one property
  that lets a daily routine run unattended.

## Two failures worth naming

**Over-extraction** is the common one. An informal meeting wanders, and a reader who wants to
be useful hears commitment everywhere. When in doubt, `por confirmar` costs a person ten
seconds and a wrong playbook edit costs an argument.

**Silent under-extraction** is the quiet one. If you discard something, it goes in the
Descartado section with a reason. A filter nobody can see is a filter nobody can fix.
