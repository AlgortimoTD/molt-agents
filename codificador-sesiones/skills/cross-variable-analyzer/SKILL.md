---
name: cross-variable-analyzer
description: >-
  v1.0.0 · Cross the variables of a qualitative study step by step, pausing for the researcher
  at each step. Reads a research folder's coded matrix, codebook, hypotheses and minimums, and
  builds one cross file in three steps: frequencies by target group with their n, candidate
  relations each backed by a count and three quotes from different participants, and a summary of
  what holds and which hypothesis it touches. Never claims causes, flags small samples, never
  skips a step without the researcher's answer, and neither ranks nor writes findings. Use it
  whenever someone wants two variables related, a category compared across groups or patterns
  looked for in coded interviews or focus groups. Triggers: "cruza deporte con alimentación por
  grupo", "compara esta variable entre grupos", "hay relación entre", "cross these two
  variables". [v1.0.0]
---

# cross-variable-analyzer

## Version 1.0.0

After coding comes the part a research team calls analysis: does the group that exercises more
also eat better, is the motivation to use a tool personal or work-driven, does one target group
say something the others do not. The team has tried asking a model for "the analysis" in one go
and lost track of what it related and why. This skill does the cross in small steps, stops after
each one, and writes down what the researcher decided, so they keep control and can later show
where every relation came from.

The discipline that matters is honesty about the sample. Qualitative studies have four to eight
people per group. Two coincidences in a group of five are a thread worth pulling, not a finding,
and a relation stated without its n and its quotes cannot be defended when a stakeholder asks
"how many said that".

## Where you work

The same research folder as `qualitative-session-coder`: its `CLAUDE.md` starts with
`<!-- codificador-sesiones -->`; find it by that marker, then the platform memory entry
`codificador-sesiones: <folder>`, then by asking once. Read its `CLAUDE.md` and resolve every
name from its vocabulary block by key (`{matrix}`, `{crosses}`, `{pause}`); if the block or a key
is missing, stop and say so. Names under a study are relative to `{studies}<study-slug>/`. Pick
the study the person names, or the only active one, or ask.

## What you read

- `{matrix}` of the study: one row per code. Map its columns through the role keys in
  `{output-format}` (group, participant, variable, category, quote, minute, session, state);
  never assume a column by its position or its header text.
- `{codebook}`: the variables and their active categories, so a category is shown by its current
  name and a `{retired}` one is not counted.
- `{study}`: the objectives and the client's hypotheses, so step 3 can say which one the cross
  touches.
- `{quality-criteria}`: the minimums. By default a relation needs at least 3 distinct
  participants, and a group with fewer than 3 coded participants in a variable is a small sample.

**Who is a participant.** Codes restart in every session (P1 of one focus group is not P1 of the
next), so a participant is the pair session plus code. A `{unidentified}` row is shown apart in step
1 with its count and is never added to an n or used to build a relation: nobody knows whose it is.

Before step 1, check the matrix. If any row of the variables involved is `{to-recode}`, say how
many and offer to wait until they are recoded: a cross over stale codes counts a category the
team already changed. If the matrix does not contain every row of the session files' coding tables (compare content, not
file dates, which a copy or a sync can change), it was not regenerated; say so and ask
`qualitative-session-coder` to regenerate it before you count.

## The three steps

Write one file, `{crosses}<AAAA-MM-DD>-<var-a>-x-<var-b>.md` (variable names in lower case, hyphens,
no accents: `2026-09-28-actividades-de-tiempo-libre-x-quien-decide.md`), with the shape of the
plugin's cross template (`templates/es/cruce.template.md`: a header with study, who asked and the
matrix used, then each step followed by `{pause}` and `{decision-at-pause}`), and build
it one step at a time. **After each step, write `{pause}`, show the step in the chat, and stop.**
Continue only when the researcher answers, and write their answer under `{decision-at-pause}`,
in their words. If they ask to adjust (merge two categories for this cross, drop a group, look at
one session), apply it, note it, and redo only that step, keeping the first version above it. An
answer that adjusts and continues at once ("sigue, pero sin el grupo 1") means: apply the
adjustment from the next step on and continue.

A person who says "dame todo de una vez" still gets step 1 and the pause, with one sentence of
why: seeing the frequencies first is what lets them catch a wrong grouping before it becomes a
relation. That refusal is the product, not a limitation of it.

### Step 1: frequencies

Count **participants, not rows**: a participant with two quotes in the same category counts once.
Show, per target group, how many participants fall in each category of each variable, with the n
of coded participants per group. Mark "muestra pequeña" where the n is under the minimum. List
the groups that have no coded participant in a variable instead of leaving them out silently.

### Step 2: candidate relations

Look for co-occurrence at the level of the participant: participants in category X of variable A
who are also in category Y of variable B, or a category that concentrates in one group and is
absent in another. For each candidate:

- the count and the base ("4 de las 6 participantes del grupo 2 que son deportistas también
  dicen comer en casa");
- the direction as a coincidence, never as a cause;
- **three quotes from three different participants**, each with participant, session and minute,
  taken from the matrix.

A candidate that does not reach the minimum of participants is not listed as a relation. Put it
under a short "hilos por revisar" line with its count, so the researcher can decide whether it
deserves a look in the transcripts; a thread may say which way it points, always with its count,
and needs no quotes. A row flagged `{doubtful-quote}` counts like any other, and its quote keeps the
flag wherever it is shown. Also list the relations you looked for and did not find:
"no hay relación visible entre A y B en esta muestra" is information.

### Step 3: summary of the cross

What holds (the relations that passed step 2 and survived the researcher's review), what does
not hold or cannot be said with this sample, and which of the study's hypotheses the cross
touches and in which direction. Every statement keeps its n.

## What you never do

- **Claim causes.** "La gente que hace deporte come mejor porque..." is not something a
  coded matrix of twenty people can support. Say what coincides in this sample.
- **Prioritize or write findings.** Which relations matter to the client and how they are
  told is the lead researcher's judgment. Step 3 hands them the relations with their support;
  it does not rank them or draft the finding.
- **Count without quotes.** A relation without its three quotes is not written.
- **Change the codebook or the matrix.** If the researcher decides at a pause that two categories
  should merge for good, that is a codebook change: say so and let `qualitative-session-coder`
  apply it with its history. For this cross, note the merge and apply it only here.
- **Write outside the folder.**

## Done means

- The cross file exists with the steps reached, each closed by `{pause}` and the researcher's
  decision in their words, or waiting for it.
- Every count is of participants, with its base and the group's n; small samples are marked.
- Every relation has three quotes from three different participants, with session and minute.
- No sentence states a cause; no finding is drafted or ranked.
- A person who reads only the file, without the chat, can see what was counted, what was
  decided at each pause, and where every relation came from.
