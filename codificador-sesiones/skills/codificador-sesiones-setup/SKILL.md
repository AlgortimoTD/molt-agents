---
name: codificador-sesiones-setup
description: >-
  v1.0.0 · Zero-command installation of the research session coder for a research team. Creates the
  team's research folder on Google Drive, interviews them (people and roles, how they code today),
  takes the formats and a previous study they coded by hand and turns them into the folder's
  output format, quality criteria and calibration example, loads the current study with its
  codebook from their own spreadsheet, checks the Fathom connector, codes a first session as a
  heartbeat and offers the fidelity test. Also seeds a fictional demo study. The person never
  runs a command. Use it whenever someone wants to install, set up or try the session coder,
  or when another skill of the plugin cannot find a research folder. Triggers: "instala el
  codificador", "quiero instalarlo", "configura el codificador de sesiones", "puebla el
  codificador con el estudio de ejemplo", "install the session coder", "seed the demo study".
  [v1.0.0]
---

# codificador-sesiones-setup

## Version 1.0.0

A research team already knows how to code: they have done it for years in spreadsheets and on
whiteboards. What they do not have is a folder where the agent can learn how they do it and then
do the first pass for them. This skill builds that folder with the team doing nothing but
answering questions and handing over the files they already use. When it finishes, the folder
exists in their Google Drive, open as a project on every researcher's machine, it holds their
format, their criteria and an example of their own work, the current study is loaded with its
codebook, and one session has been coded end to end.

## Guiding principle

**The person does not run commands, create folders or edit files.** You do everything
executable. They only do what needs their identity (signing in, authorizing a connector, sharing
a folder), hand over files and answer. You never ask for or type a password. Speak in plain
language: say what a thing does, not the name of a tool, package or protocol. The names of the
apps the person sees and clicks (Google Drive, Cowork, Claude Code, Fathom) are fine.

**Their way of working is the specification.** The team's formats, criteria and a study they
already coded are worth more than any rule you could write. Ask for them early, keep the
originals untouched in `{templates}` and `{examples}`, and derive the folder's configuration from
them, citing the file each rule came from.

**Idempotent.** Phase 0 detects what exists and skips it; running this skill on an installed
folder never creates a second one.

**Nothing of any team lives in this skill.** Names, roles and rules come from the interview and
land in the folder's own files.

## Where the pieces are

This skill ships inside the `codificador-sesiones` plugin. Next to its `skills/` folder you find
`templates/es/` (what you fill; `templates/README.md` says what each becomes),
`templates/vocabulary.md` (the name of every folder, file, heading and state, by key), `demo/es/`
(a fictional study for demo mode) and `docs/es/` (the operating guide you copy into the folder).
If they are missing, this skill was installed alone: stop and give the one message to paste,

> Instala el codificador de sesiones de investigación. Viene del marketplace
> AlgortimoTD/molt-agents, plugin codificador-sesiones. Deja listo todo lo que necesite para
> funcionar y avísame cuando esté, sin explicarme los detalles técnicos.

**Language.** This version works in Spanish. Say it once at the start ("la carpeta y todo lo que
escriba van a quedar en español; las citas quedan en el idioma en que se dijeron") and use
`templates/es/`. Do not translate templates on the fly.

## Phase 0: diagnosis (silent)

- Is there a folder whose `CLAUDE.md` starts with `<!-- codificador-sesiones -->`? Check the
  working folder, then the platform memory entry `codificador-sesiones: <folder>`. If there is,
  the coder is installed: offer to add a study, load an example or run the fidelity test, and
  stop. A folder named `Investigación (demo)` does not count. A folder without the marker whose
  name matches the one you would suggest is the person's own: ask before using it, never
  overwrite it.
- Is Google Drive for desktop syncing on this machine? Is the Google Drive connector available?
  Is the Fathom connector available?
- Present the map in one sentence: "Vamos a hacer seis cosas: la carpeta en Drive, quiénes son y
  cómo trabajan, sus formatos y un estudio que ya codificaron, el estudio de ahora con su libro de
  códigos, la conexión con Fathom y una primera sesión codificada."

## Phase 1: the folder on Google Drive

The folder lives in a shared Drive so the same files reach every researcher; Drive for desktop
makes it a local folder that Cowork or Claude Code open as a project, and that is how the agent
loads its instructions. Nothing lives only on one machine.

1. Guide Drive for desktop's install and sign-in if it is missing, and locate the mounted drive.
2. Create the root folder yourself; ask only where and what name (suggest `Investigación
   <Equipo>`).
3. Guide opening it as the project in Cowork (or Claude Code) on this machine.
4. Create `{templates}` and `{examples}` right away, with the examples README, so the person has
   somewhere to drop files while the interview goes on.

## Phase 2: who they are

Fill `{team}` and the table of `CLAUDE.md`:

| Ask | Fills |
|---|---|
| each person, title, and who moderates sessions | the people table |
| who is **lead** (changes anything, owns each study's codebook), who are **researchers** (code, cross, accept or reject categories, edit the codebook), who only **consults** | roles |
| where sessions are recorded (the Fathom team or account) and how a research recording is told apart from any other call (a code in the title, a naming rule) | Fathom section |
| the languages sessions are held in | language |

There is always at least one lead. If nobody takes the role, say in one sentence why it exists
(someone has to decide the codebook when two researchers disagree) and ask again.

## Phase 3: their formats and a study they already coded

This is the phase the whole agent depends on. Ask, with this intent: "¿Me compartes cómo lo
hacen hoy? Me sirven la plantilla o el Excel donde vacían las respuestas después de una sesión,
la matriz de un estudio que ya hayan codificado, y si pueden, ese estudio completo: su libro de
códigos, dos o tres transcripciones y los hallazgos. No importa que esté desordenado."

1. **Formats.** Save what they hand over, as is, in `{templates}`. Derive `{output-format}` from
   them: the matrix columns in their order and with their headers, each mapped to its role key
   (group, participant, variable, category, quote, minute, session, state, note); how they write
   a quote; how they name a category; how they code participants. Cite the file each rule came
   from. When their spreadsheet lacks a column the agent needs (minute, state), add it at the end
   and say so.
2. **The previous study.** Before it enters the folder, **check that it is anonymized**: no
   participant names, no client, no brand that identifies the client. Read it; if you find a name,
   do not store it, say what you found and ask them to remove it or authorize you to replace it
   with codes. Then store it in `{examples}<study>/`: its codebook (reconstruct it from the hand
   matrix when they have none, and show it to them: categories, how many rows each), the
   transcripts, their matrix as `matriz-a-mano.csv`, and the findings if any. Update the examples
   README with what was anonymized.
3. **Criteria.** With the example open, interview the lead for `{quality-criteria}`: when two
   answers are the same category, when something deserves a new one, one code they consider good
   and one they would correct, and the minimums for a cross (default 3 participants). Quote them.
   Keep one hand-coded session of the example aside for the fidelity test and take the criteria's
   good and bad examples from the other sessions: an example quoted in the criteria is an answer
   the test already gives away.
4. **No example available** is a valid answer, and it has a cost: say that the coding will not
   be measured against theirs until one arrives, and write a `{gap}` line in `{memory}`.

## Phase 4: the current study

Create `{studies}<study-code>/` with `{study}` (objectives, client hypotheses, target groups,
field dates, lead), the `{codebook}` from their own spreadsheet (every variable with its fixed
categories, a definition and an example quote when they give one, the first `{history}` line
saying where it came from), the moderator guides in `{guides}` if they have them, the empty
`{proposals}`, the matrix header from `{output-format}`, `{sessions-inbox}` with its README and
`{state}` from its template. A variable they name without categories enters with none; a session
will propose them.

Then write the root `CLAUDE.md` from its template: the marker exactly
`<!-- codificador-sesiones -->` on line 1, the vocabulary block intact at the end. Write
`{memory}` with its first dated line, copy the operating guide to `{guide}` at the root of the
folder, and **save the folder to memory** as `codificador-sesiones: <folder>`.

## Phase 5: Fathom

If the team records in Fathom, the person authorizes the connector in the app (their click).
Check it by listing the recordings the rule of Phase 2 identifies; show two titles and ask if
those are research sessions. The connector is read only. Without Fathom, explain
`{sessions-inbox}`: a transcript pasted there does the same job.

## Phase 6: the heartbeat and the fidelity test

1. **Code one real session** of the current study with `qualitative-session-coder`, the latest
   one or the one they choose. Open the session file with them: the coding table with its quotes
   and minutes, what went to uncategorized, any proposal. Ask one researcher to review it the way
   they review today.
2. **Offer the fidelity test** when there is an example: the agent codes a session of the example
   and compares it with their hand coding. Say what the number means (how often it chose the same
   category they did) and that the differences are the useful part.

## Phase 7: what the folder knows and what it does not

Close by saying it plainly, from the folder: the study loaded (variables, categories, groups),
the example and whether it passed the fidelity threshold, the sessions coded; and what is missing
(no example, a variable without categories, no guide for a group, Fathom not connected). Write
one `{gap}` line per missing piece in `{memory}`.

Give the **Drive permissions** as a short list the person applies with their own clicks: the lead
and the researchers as editors, the viewers as viewers. The agent cannot tell who writes to it;
the folder's permissions are the control.

Tell each researcher what to install on their own machine: Drive for desktop signed into the
account with access, and the plugin from the same message. Several researchers can code at the
same time: each session is its own file and the matrix is rebuilt from them.

## Demo mode

Trigger: "puebla el codificador con el estudio de ejemplo", or someone who wants to try it before
bringing their own material. Everything in `demo/es/` is invented.

Phase 0's check runs, but its six-step overview does not: it describes a real install.

1. Copy `demo/es/investigacion/` to the person's Drive as `Investigación (demo)`, next to a real
   folder if they have one, never inside it. If `Investigación (demo)` already exists, ask whether
   to replace it with a fresh copy or keep it as it is.
2. Do not edit the copied files: the folder is consistent. It holds a fictional team, an example
   study coded by hand, a current study with a three-variable codebook, one coded session with its
   matrix and watermark, and one focus-group transcript waiting in the inbox.
3. Tell them to open `Investigación (demo)` as the project in Cowork or Claude Code: that is how
   the other skills find it (by its marker), without saving anything to memory.
4. Say what to try, in order: code the waiting transcript (it adds rows with quotes, leaves one
   passage uncategorized and raises a proposal), accept the proposal, cross two variables and see
   the pause, ask what one group said about a variable, run the fidelity test. Then ask again to code what
   is in the inbox and show that nothing changes: the session is already coded, the inbox empty.
5. Do not save the demo folder to memory: it would make Phase 0 of a real install find an
   existing folder.
6. When they say they are done with it, offer to delete it, saying that deleting is permanent,
   and delete only after they confirm.

## Done means

- One folder, marker on line 1 of its `CLAUDE.md`, vocabulary block complete, every name in
  Spanish.
- `{team}` with at least one lead; `{output-format}` and `{quality-criteria}` derived from the
  team's own files and interview, each rule with its origin.
- The team's files untouched in `{templates}`; the example study anonymized in `{examples}`, or
  its absence written as a gap.
- The current study with its codebook from their spreadsheet.
- Fathom checked, or the inbox explained.
- One session coded end to end and reviewed by a researcher; the fidelity test run or offered.
- The inventory said, the gaps in `{memory}`, the permissions list given, the folder in memory.
- The person never typed a command or heard the name of a tool.

In demo mode, done means: the demo copied next to (never inside) any real folder, byte-identical
to the plugin's copy; the person told to open it as the project and what to try; nothing saved
to memory.
