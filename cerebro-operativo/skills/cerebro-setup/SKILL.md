---
name: cerebro-setup
description: >-
  v1.2.0 · Zero-command onboarding of an organization's operating brain in Spanish or English. Asks
  the language first (mandatory, final) and writes every file, folder and heading in it. Mounts the
  Google Drive folder, turns the documents they already have into the first playbooks, interviews
  them (people and roles, values, processes, meetings), schedules the daily routine, processes a
  kickoff meeting that corrects the documents, and closes with an inventory of what the brain knows
  and what it does not. Also seeds the demo organization, in Spanish or English. The person never
  runs a command. Use it whenever someone wants to install, set up or try the brain, even without
  naming it, or when another skill cannot find a brain folder. Triggers: "quiero instalarlo",
  "instala el cerebro", "configura el cerebro de mi empresa", "puebla el cerebro con la empresa de
  ejemplo", "install the brain", "set up the operating brain", "seed the demo organization".
  [v1.2.0]
---

# cerebro-setup

## Version 1.2.0

An organization's brain is a folder with memory: how the team does things, why, and what
happened the previous times, kept in files the team can read and correct. This skill creates
that folder for a new organization, with the person doing nothing but answering questions,
handing over the documents they already have, and clicking where their own identity is needed.
When it finishes, the brain exists in the organization's Google Drive, readable and writable
from every surface (Cowork, Claude Code, claude.ai on the web and on the phone), it already
holds what the organization had written down, the daily routine is scheduled, a kickoff meeting
has corrected the first playbooks, and the person knows exactly what the brain does not know
yet.

## Guiding principle

**The person does not run commands, does not create folders and does not edit files.** You
execute everything executable and create every folder and file. The person only does the
clicks that require their identity (signing in, authorizing a connector, confirming a time
slot, sharing a folder), hands over documents, and answers the interview. You never ask for or
type a password.

**Plain language, always.** The person installing may know nothing about computers. Do not
name a language, package, repository, marketplace, connector protocol or error code to them;
say what the thing does. Whenever you find yourself about to ask the person to install or
configure something, install or configure it instead and ask only for the permission prompt.

**Idempotent.** Phase 0 detects what already exists and skips it. Running this skill on an
existing brain never creates a second one.

**Nothing of any organization lives in this skill.** Names, roles and rules come from the
interview and land in the brain's own files. Where this skill says "the brain owner", the
brain's `CLAUDE.md` says who that is.

## Where the pieces are

This skill ships inside the `cerebro-operativo` plugin. Next to the plugin's `skills/` folder
you will find:

- `templates/es/` and `templates/en/`: what you fill to create the brain. Read
  `templates/README.md` first: it lists what each template becomes.
- `templates/vocabulary.md`: the dictionary of every folder, file, heading, marker, state and
  role name, by key, in each language.
- `demo/es/cerebro/` and `demo/en/brain/`: the fictional organization for demo mode, once per
  language, each with the names of its vocabulary column.
- `docs/es/como-operar-el-cerebro.md` and `docs/en/how-to-operate-the-brain.md`: the operating
  guide you copy into the brain.

If you cannot find them (this skill was installed alone, without the plugin), stop and tell
the person the brain comes as a plugin, then give them the one message to paste:

> Instala el cerebro operativo de mi empresa. Viene del marketplace AlgortimoTD/molt-agents,
> plugin cerebro-operativo. Deja listo todo lo que necesite para funcionar y avísame cuando
> esté, sin explicarme los detalles técnicos.

(In English: "Install my company's operating brain. It comes from the marketplace
AlgortimoTD/molt-agents, plugin cerebro-operativo. Get everything it needs ready and tell me
when it is done, without explaining the technical details.")

## Language comes first, and it is final

The brain works in Spanish or in English, and the choice belongs to the organization, not to
you and not to the language of their website. It is the **first question of the installation
and it is mandatory**: nothing is created, no folder, no file, no interview block, until it is
answered.

1. **Detect** the language of the person's first message, and ask in it.
2. **Ask one explicit question** and say that the answer is final. In Spanish: "¿En qué idioma
   quieres que trabaje el cerebro, español o inglés? Todo va a quedar en ese idioma: los
   nombres de las carpetas, los playbooks, la bitácora y mis respuestas. Después no se cambia."
   In English: "Which language should the brain work in, Spanish or English? Everything will be
   in that language: the folder names, the playbooks, the decision log and my answers. It does
   not change later."
3. **Do not proceed on an unclear answer.** "Both", "whatever you think" or silence get the
   question again, once, with the reason: every file and folder name depends on it.
4. **Always ask a second question**, right after: which language drafts for clients should
   use. You cannot know whether clients speak another language without asking. It is a
   separate setting; it does not change the language of the brain, and the interview does not
   ask it again.

The answer picks the template set (`templates/es/` or `templates/en/`), the operating guide and
the vocabulary column. Do not mix sets and do not translate a template on the fly: a brain born
in English gets every file from `templates/en/`.

### The vocabulary

Every name in the brain comes from `templates/vocabulary.md`, in the chosen language. This
skill refers to them by key, in braces: `{log}` is the decision log, `{history}` the heading
that keeps replaced text, `{documents}` the folder of existing documents. The root
`CLAUDE.md` template already ends with the vocabulary block of its language; keep it intact
and complete, because the other four skills resolve every name from it, including in cloud
sessions that cannot reach the plugin. The only language-neutral pieces are the marker
`<!-- cerebro-operativo -->` on line 1 and the JSON keys of `{state}`.

## Phase 0: diagnosis (silent)

Before saying anything about steps, look:

- Is there already a folder whose `CLAUDE.md` starts with `<!-- cerebro-operativo -->`? Check
  the working folder first, then the platform memory entry `cerebro-operativo: <folder>`. If
  there is one, the brain is mounted: offer the audit (`cerebro-audit`) or help with what is
  missing, and stop here. Never create a second brain. A folder named `Cerebro (demo)` or
  `Brain (demo)` does not count: it is the sample organization, and its presence never blocks
  a real install.
- Is Google Drive for desktop installed and syncing on this machine (a mounted drive with the
  person's files)? Is the Google Drive connector available in the app? Is the plugin
  installed (this skill running is evidence that it is)?
- Then ask the language (above), and present the map in one sentence, in that language:
  "Vamos a hacer seis cosas: la carpeta en Drive, leer los documentos que ya tienen, la
  entrevista sobre tu empresa, la rutina diaria, una reunión de arranque y, al final, te digo
  qué sabe el cerebro y qué le falta." Nothing more technical than that.

## Phase 1: Google Drive (the storage backbone)

The brain lives in Google Drive so the same files are available to every surface: local
sessions read the synced folder, cloud sessions (claude.ai, the phone, the daily routine) read
and write it through the Drive connector, with the computer off.

1. **Google account.** If they do not have one, guide its creation. Never handle the password.
2. **Google Drive for desktop**, for the machines that will consult the brain locally: guide
   the install and sign-in, and locate the mounted drive.
3. **Create the root folder** yourself, once the drive is mounted. Ask only where and what
   name; suggest `Cerebro <Organización>` in Spanish, `<Organization> brain` in English.
4. **Mark it "available offline"**: guide the right-click. It makes local sessions robust to
   connectivity.
5. **Connect the Google Drive connector** in the Claude app (Settings, Connectors, Google
   Drive, authorize): the person's click. It is what lets the routine and the phone reach the
   folder.
6. Explain the sync contract in one sentence: the cloud wins on doubt, duplicates with `(1)`
   are name clashes, and nothing stays loose because everything that arrives gets filed.

Create `{documents}` right away with its README (`documentos-README.template.md`), so the
person has somewhere to drop files while you go on.

## Phase 1b: environment

**Nothing to install.** The brain is Markdown, one JSON state file, connectors and a scheduled
task. Say nothing about this phase to the person; it exists so every agent of the marketplace
has the same shape. If a future version of any skill of this brain ever needs a program on the
machine, it declares it in a manifest and installs it outside the plugin folder, and this phase
gains a self-check the person can ask for ("¿qué te falta?").

## Phase 2a: the documents they already have

Before asking anyone to describe their processes, read what is already written. People do not
remember how they do things, they do them; a document, even an old one, is a better starting
point than memory.

1. **Ask**, in the brain's language, with this intent: "¿Tienen algo escrito sobre cómo hacen
   las cosas? Manuales, procedimientos, una carpeta de plantillas, un Notion, presentaciones de
   inducción. No importa si está viejo: sirve igual, y yo te digo qué quedó desactualizado."
2. **Where they come from:** dropped in `{documents}`, pasted in the chat, or a Drive link the
   connector can open. Accept Markdown, plain text, Word and PDF. Save what arrives through the
   chat or a link into `{documents}` under a descriptive name; the originals are never edited.
3. **For each document:** decide which process it belongs to and write that process's playbook
   under `{playbooks}` **from the document**, one section per part the document covers. Mark
   each section with `{current-since}` inside an HTML comment, using the document's own date and
   the file as origin. When the document has no date, use the day of the installation and say
   in the section that the real date is unknown.
4. **Do not modernize.** If a document says something that sounds outdated, write it as it is
   and mark it for the kickoff meeting. Correcting it is the team's job in Phase 5; guessing
   here is exactly what the brain promises never to do.
5. **Values and cases found in a document** go to `{values}` and `{cases}` the same way, cited.
6. **No documents at all** is a valid answer. Say that the interview and the kickoff meeting
   will be the source, and go on.

Tell the person, in one line per document, what you took from each.

## Phase 2: the organization's context (the interview)

This is the heart of the install and the part Molt accompanies in person in the first
instances. Conduct it yourself in every instance, so the organization can repeat it alone
later. Ask in blocks, one round each, in the brain's language, and fill the templates as you
go. Every fact you write cites its source (interview and date, or the document); nothing is
inferred silently. What they cannot say firmly is written as `{to-confirm}`, never guessed.

| Block | Ask about | Fills |
|---|---|---|
| Who they are | what the organization does in their own words, when it started, how many people, how they work | `{company}` |
| The people and their roles | each person and their title; then who is the **brain owner** (exactly one: changes anything, approves values, answers for the processes being up to date), who are **editors** (change playbooks and cases) and who only **consults**; and who executes an approved change day to day | `{company}`, the table in `CLAUDE.md`, the roles table and "who approves what" of `{sources}` |
| Values | values in their words (not the site's), negotiables, non-negotiables, when a client is let go and how it is said | `{values}` (the four blocks) |
| Processes | first, the playbooks that came from the documents, one by one: does it still apply? Then the processes that exist today without a document | the playbooks from Phase 2a gain what they confirm; one new playbook per undocumented process they describe, with a single seed section and an empty `{history}`; a process they name but cannot describe gets no playbook, only a `{gap}` line for Phase 6 (an empty playbook promises content nobody wrote); file names in lower case, hyphens, no accents, in the brain's language |
| Cases | one or two past cases with a client that taught them something | one file per case under `{cases}` from `caso.template.md`, with the five parts; ask for the lesson and the value if they do not come up |
| Key clients and tools | who the important clients are, where proposals and projects live, what they use to meet | `{company}` |
| Meetings | which recurring meeting is the source of decisions, whether it is recorded (the Fathom team's name and its owner), which meetings never enter | `{sources}` |
| Time zone | their IANA time zone (the clients' language was asked with the working language) | `{sources}`, `{state}` |
| The routine | in whose account it should run, and at what time (after the main meeting, with margin) | `{sources}` (account, days, time; the literal prompt is already in the template) |

Do not leave the roles block without a brain owner. If nobody wants the role, explain in one
sentence why it exists (without someone who answers for it, the brain ages like the documents it
came to replace) and ask again; if it still has no owner, write `{to-confirm}` and it becomes the
first gap of Phase 6.

Then create the rest of the structure from the templates: `CLAUDE.md` (first line is the marker,
exactly `<!-- cerebro-operativo -->`; last lines the vocabulary block), `{memory}` with its first
dated line, `{log}` empty with its format, `{state}` with the time zone, the READMEs of
`{meetings-inbox}` and `{outputs}`, and the operating guide of the chosen language copied to
`{guide}`. Write the marker even if nothing else were written: it is what every other skill and
Phase 0 recognize.

**Save the folder to memory** as `cerebro-operativo: <folder name or Drive path>`, so a session
opened elsewhere (the phone, claude.ai) finds it without asking twice.

## Phase 2b: the voice

Run `brand-voice-style-guide` (it ships in the same plugin) over the organization's public site
and channels, plus any texts the team hands over (emails and proposals are the best evidence),
and leave `{voice}`. Ask the person to read one rewrite and say whether it sounds like them;
that is the only test that matters. If they cannot do it now, leave the file with its gaps
named at the top and a task in `{memory}`.

## Phase 3: the plugin

The plugin is already installed if this skill is running. Verify it can see `templates/`,
`demo/` and `docs/` (Phase 0 did), and tell the person how updates arrive: on the computer,
"actualiza el plugin cerebro-operativo" in the chat; on claude.ai, automatically.

## Phase 4: the daily routine

Create the scheduled task on the platform, in the account the person chose, with the literal
prompt written in `{sources}` (never paraphrase it), daily on working days at the chosen time.
The person only confirms the slot. Explain in one sentence that it is the only part of the
system that talks to an outside service, that it only fetches transcripts, and that it writes
only inside the folder.

If the organization does not use Fathom, do not block: explain `{meetings-inbox}` (a transcript
dropped there does the same job) and schedule the routine anyway; it will find nothing until
something arrives, and finding nothing is a normal outcome.

## Phase 5: the kickoff meeting

The first transcript is not any meeting. It is a meeting of 45 to 60 minutes that the team
records (Fathom, or any recording with a transcript), called for one thing: going through what
the brain already wrote and saying what still holds.

1. **Give them the script before the meeting**, in the brain's language, written to
   `{kickoff-script}` and repeated in the chat: go through each playbook that came from the documents and, for
   each one, say "it still works like this", "it changed to this" or "we no longer do this";
   then name the processes that have no document and tell how they work; close with the
   values, negotiables and non-negotiables the interview left `{to-confirm}`.
2. **Process the transcript** with `transcript-to-playbook-updater` (same plugin), exactly as a
   daily run does. The difference is the content, not the mechanism: this is the meeting that
   corrects the archive, and every correction lands in `{log}` with its date and minute.
3. **Check the four outputs together with the person**: the meeting file in `{meetings}`, the
   lines in `{log}`, the playbook sections rewritten with their `{history}` (or "nothing
   changed, and here is why"), and the `{ingestion-report}`. If those exist, the system is
   alive.
4. **If they cannot record a kickoff meeting now**, do not block the installation. Process the
   notes or the transcript of their last meeting instead, so the heartbeat is still verified,
   and write one dated line in `{memory}` starting with `{pending-kickoff}`. `cerebro-audit`
   keeps asking for it.

## Phase 6: what the brain knows and what it does not

The risk of a new brain is not being empty; it is being half full while someone trusts it as
complete. Close the installation by saying it out loud, in the brain's language, without
technical words. Build it from the folder, not from memory: count the playbooks and where each
came from, the values, negotiables and non-negotiables written firmly, the cases, the meetings
processed; then list what is missing (a named process with no playbook, a block of values
still `{to-confirm}`, no cases before a given year, documents without a date, no brain owner).
Its shape:

> Tu cerebro ya tiene: cinco procesos escritos, tres de ellos desde documentos que traías (dos
> sin fecha), dos valores y un no negociable, un caso, y la reunión de arranque procesada.
> Todavía no tiene: negociables (nadie los dijo en firme), el proceso de eventos (lo nombraron
> y no lo contaron), y ningún caso anterior a 2025.
> Mientras eso siga así, cuando le preguntes por un negociable te va a decir "esto no está
> escrito" en vez de inventarte una respuesta. Eso es a propósito.

Write the same inventory in `{memory}`: one dated line per gap, each starting with `{gap}`, so
`cerebro-audit` chases them from the first week.

Then give the **Drive permissions** that match the roles, as a short list the person applies
with their own clicks (sharing is their identity): the brain owner and the editors as editors
of the folder, the viewers as viewers, the routine's account as editor. Say why in one
sentence: the brain cannot tell who is writing to it, so the folder's permissions are what
decide who can change it.

Close by showing what they can ask for from now on, in their language: "¿cómo manejamos
esto?", "procesa este transcript", "escribe esto con nuestra voz", "¿qué decidimos sobre X?",
"organiza la carpeta".

## Demo mode: seed the fictional organization

Trigger: "puebla el cerebro con la empresa de ejemplo", "seed the demo organization", or a
person who wants to learn or demo before having real documents. Everything in `demo/` is
invented, so it can be shown to anyone.

1. **Pick the language of the demo.** It is the language of the person's brain when they have
   one (the `lang:` line of its vocabulary block). Without a brain, ask the same explicit
   question as the installation, in the language of their message, but say that this answer
   is only for the demo and does not fix the language of a future brain. Never copy one
   language and translate on the fly: each copy is already written in its own vocabulary.

   | Language | Copy from | Into Drive as | Inbox with the waiting transcript |
   |---|---|---|---|
   | Spanish | `demo/es/cerebro/` | `Cerebro (demo)/` | `reuniones/entrada/` |
   | English | `demo/en/brain/` | `Brain (demo)/` | `meetings/inbox/` |

2. Copy it into the person's Drive, **next to** their real brain if they have one, never
   inside it.
3. Do not edit the copied files. The folder is already consistent: two playbooks (one of them
   written from an old document in `{documents}`), a decision log, a closed case, one ingested
   meeting with its summary and watermark, and one transcript waiting in `{meetings-inbox}`.
   The copy's own vocabulary block resolves those names, like in any brain.
4. Say what to try, in order and in the demo's language: process the waiting transcript (it
   adds a decision, rewrites a section with history and leaves one inference pending), ask
   how to handle a client who mistreats the team ("¿cómo manejamos un cliente que maltrata al
   equipo?" / "how do we handle a client who mistreats the team?"), ask what was decided
   about proposals, request a draft in the voice, correct a decision, run the audit. Then
   process the transcript a second time and show that nothing changes.
5. **Do not save the demo folder to memory.** The `cerebro-operativo: <folder>` entry is for
   the organization's real brain only; pointing it at the demo would make Phase 0 of the real
   install find "an existing brain" and refuse to create the company's own.
6. When they are done, offer to delete the demo folder; nothing else references it.

## Error handling

- **Drive not mounted locally:** cloud-only mode still works through the connector; say that
  local sessions need Drive for desktop and continue.
- **Connector not authorized:** go back to Phase 1, step 5; the routine and the phone cannot
  reach the folder without it.
- **Plugin missing its templates:** see "Where the pieces are".
- **A document you cannot open** (a scanned image, a protected file, a link the connector cannot
  reach): say which one, ask for another format, and list it among the gaps of Phase 6 if it
  never arrives.
- **The person gets lost on a web step:** ask for a screenshot and guide from what they see.

## Done means

- The language was asked first and answered; one folder with the marker on line 1 of its
  `CLAUDE.md` and the complete vocabulary block at its end, every file and folder name and
  every heading in that language, nothing from the other set.
- Every document handed over is in `{documents}` and cited by the playbook, value or case that
  came from it, with its date or the note that the date is unknown; nothing modernized.
- `{sources}` has a roles table with exactly one brain owner, or the missing owner is the first
  gap; no rule in `CLAUDE.md` names a person where it should name a role.
- `{company}`, `{values}` and the playbooks filled from the documents and the interview, every
  gap marked `{to-confirm}`, not guessed.
- The folder name saved to memory.
- The routine scheduled with the literal prompt, or explicitly deferred with `{meetings-inbox}`
  explained.
- The kickoff meeting processed end to end and its four outputs shown, or a meeting processed
  in its place and `{pending-kickoff}` written in `{memory}`.
- The inventory said to the person, one `{gap}` line per gap in `{memory}`, and the Drive
  permissions list given.
- The person never typed a command, never created a folder, and never heard the name of a
  tool.
