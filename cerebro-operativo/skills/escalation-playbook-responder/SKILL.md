---
name: escalation-playbook-responder
description: >-
  v1.1.0 · Answer "how do we handle this" from a company brain folder instead of from improvisation,
  in the brain's own language. Reads the company's values, negotiables and non-negotiables, its
  playbooks, its past cases and its decision log, and answers a question or a client escalation with
  the rules that apply, the closest past case, and the file and date behind every claim. When
  nothing is written it says so and offers to record it rather than inventing a policy. It can draft
  a message in the company's voice, always marked for a person to review, and it never sends
  anything. Triggers: "how do we handle this", "a client is mistreating the team", "what is our
  policy on", "help me answer this escalation", "cómo manejamos esto", "un cliente está maltratando
  al equipo", "cuál es nuestra política sobre", "ayúdame a responder esta escalación", "qué dice el
  playbook". [v1.1.0]
---

# escalation-playbook-responder

## Version 1.1.0

Escalations are expensive because they are answered from scratch every time. The founder who
has handled them for twenty years carries the criteria in her head, spends an afternoon
weighing a case that rhymes with three earlier ones, and the answer is consistent only because
she is the one giving it. This skill answers from what the company already wrote down, and
shows its sources so a person can check it in seconds instead of trusting it.

The hard part is not writing a good answer. It is refusing to write one when the company has
not decided. An invented policy sounds exactly like a real one, and the first time somebody
acts on it the brain stops being trustworthy for everything else.

## Where you read from

You work inside a **brain folder**. Read its `CLAUDE.md` first: it names the company, the
working language, the roles and the file map, and it outranks this skill wherever they differ.

**Every name comes from the brain.** `CLAUDE.md` ends with a vocabulary block
(`<!-- cerebro-operativo:vocabulary ... -->`) with one `key: name` line per folder, file,
heading, marker and state, in the brain's language. This skill refers to them by key in
braces (`{values}`, `{log}`, `{history}`); read the block first and use the names it gives. If
the block is missing, say so instead of guessing where the files are.

Read in this order, because it is the order of authority:

1. **`{values}`**: what the company will and will not trade. The non-negotiables are the only
   part of the answer that does not bend to the case.
2. **`{log}`**: dated decisions, newest first. A recent decision beats an older playbook; see
   below.
3. **`{playbooks}`**: the written procedure, including each file's `{history}`, which tells you
   what changed and when.
4. **`{cases}`**: what happened the last time something like this happened, and what was
   learned.
5. **`{company}`**: who the people and the clients are, so the answer lands in their world.
6. **`{voice}`**: only when a draft message is requested.

Answer in the brain's working language, not in the language of the question, and write every
heading of the answer in it.

## The answer

Give the answer first and the scaffolding after. Someone in the middle of an escalation needs
a recommendation, not a literature review. The shape, with its headings in the brain's
language (shown here for a Spanish brain):

```markdown
## Qué haría <Company> aquí

<The company's own name, as `CLAUDE.md` gives it, not the word "Company".>
<Two to five lines. The recommendation, stated plainly.>

## Lo que aplica

**No negociables**
- <rule> (`_config/valores-y-negociables.md`, 2026-09-12)

**Negociables**
- <what can move, and how far> (`_config/valores-y-negociables.md`, 2026-09-12)

**Playbook**
- <the step that applies> (`playbooks/escalaciones.md`, sección vigente desde 2026-08-30)

## El caso más parecido

<What happened, what was done, how it ended, what was learned.>
(`casos/<caso-similar>.md`, <fecha>)

## Lo que no está escrito

- <the gap, named plainly>. ¿Lo registramos?
```

In an English brain the same four headings read "What <Company> would do here", "What
applies", "The closest case" and "What is not written", and the citations name the English
files of its vocabulary.

**Every claim carries its file and its date.** Not because a reader will open each one, but
because a claim that cannot name a file is a claim you made up, and writing the citation is
how you find that out before the reader does.

### When the folder is silent

Say it. "Esto no está escrito" (or "this is not written") is a complete, useful answer, and it
is worth more than a plausible paragraph. Then offer the next step: propose the rule in one
sentence and ask whether to record it. Do not write it to `{values}` yourself: that file
changes only when the brain owner, named in the roles table of `{sources}`, asks for it or
approves it.

Log the gap in `{memory}` as one dated line starting with `{unanswered}`, so a question that
had no answer today shows up as something to write down. In a Spanish brain:

```markdown
- 2026-09-18 · Pregunta sin respuesta escrita: qué hacemos cuando un cliente escala por WhatsApp fuera de horario. Sin playbook ni caso.
```

That line is the only write this skill makes without being asked, and it is deliberate: the
gaps are the most valuable thing a brain learns about itself, and they are invisible unless
somebody writes them down at the moment they are found.

### When sources disagree

The most recent decision wins, and you say so out loud:

> El playbook de escalaciones dice X (vigente desde 2026-06-02), pero la decisión del
> 2026-09-12 lo cambió a Y. Se aplica Y. El playbook todavía no recoge ese cambio.

Never quietly pick one. The contradiction is itself information: it usually means a decision
never made it into the playbook, and naming it is what gets that fixed.

## Drafting a message

Only when asked. Read `{voice}` and write in that voice, in the language the brain sets for
drafts to clients (`CLAUDE.md` says it; it can differ from the working language). Open the
draft with `{draft-marker}`, a line that cannot be missed if somebody copies and pastes in a
hurry.

Then the message. Keep the non-negotiables intact in the wording: a draft that softens a
non-negotiable to sound friendlier has quietly changed the company's position, which is the
one thing a person reviewing it is least likely to catch.

**You never send.** No email, no message, no post. You produce text a person sends. This is
not a limitation to apologize for; it is the reason a team is willing to let this skill read
their escalations at all.

## Done means

- Every claim names a file and a date, or is explicitly marked as a gap.
- Non-negotiables appear whenever they apply, even when the answer is inconvenient.
- A contradiction between a playbook and a newer decision is resolved in favor of the decision
  and stated, not hidden.
- A draft, if any, opens with `{draft-marker}` and nothing was sent.
- A gap found is one dated `{unanswered}` line in `{memory}`.
- Every heading and file name in the answer is in the brain's language.

## The failure to watch for

Helpfulness. The question arrives with pressure behind it, the folder half answers it, and the
obvious move is to close the gap with something reasonable. Resist it: an answer marked "not
written" costs one conversation, and an invented rule that somebody quotes back six months
later costs the credibility of every other answer in the folder.
