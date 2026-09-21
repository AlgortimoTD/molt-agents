---
name: cerebro-setup
description: >-
  v1.0.0 · Zero-command onboarding of the operating brain for a new organization, in Spanish or
  English. Detects the language of the first message and confirms it with one explicit question
  before creating anything; then mounts the Google Drive folder, fills the brain's context files
  from the plugin templates through a guided interview (who they are, values, negotiables,
  processes, meetings, time zone, who approves what), schedules the daily ingestion routine and
  runs a first transcript end to end. Also seeds the fictional demo organization. The person
  never runs a command or hears a technical term. Use it whenever someone wants to install, set up or
  try the brain, even without naming it, or when another skill cannot find a brain folder.
  Triggers: "quiero instalarlo", "instala el cerebro", "configura el cerebro de mi empresa",
  "puebla el cerebro con la empresa de ejemplo", "install the brain", "set up the operating
  brain", "seed the demo organization". [v1.0.0]
---

# cerebro-setup

## Version 1.0.0

An organization's brain is a folder with memory: how the team does things, why, and what
happened the previous times, kept in files the team can read and correct. This skill creates
that folder for a new organization, with the person doing nothing but answering questions and
clicking where their own identity is needed. When it finishes, the brain exists in the
organization's Google Drive, readable and writable from every surface (Cowork, Claude Code,
claude.ai on the web and on the phone), the daily routine is scheduled, and one real transcript
has already gone through it.

## Guiding principle

**The person does not run commands, does not create folders and does not edit files.** You
execute everything executable and create every folder and file. The person only does the
clicks that require their identity (signing in, authorizing a connector, confirming a time
slot) and answers the interview. You never ask for or type a password.

**Plain language, always.** The person installing may know nothing about computers. Do not
name a language, package, repository, marketplace, connector protocol or error code to them;
say what the thing does. Whenever you find yourself about to ask the person to install or
configure something, install or configure it instead and ask only for the permission prompt.

**Idempotent.** Phase 0 detects what already exists and skips it. Running this skill on an
existing brain never creates a second one.

## Where the pieces are

This skill ships inside the `cerebro-operativo` plugin. Next to the plugin's `skills/` folder
you will find:

- `templates/es/` and `templates/en/`: what you fill to create the brain (root `CLAUDE.md`,
  `_config/`, the decision log, a playbook, a case, memory, state, two READMEs). Read
  `templates/README.md` first: it lists what each template becomes.
- `demo/cerebro/`: the fictional organization for demo mode.
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

## Language comes first

The brain works in Spanish or in English, and the choice belongs to the organization, not to
you and not to the language of their website. So, before creating anything:

1. **Detect** the language of the person's first message.
2. **Confirm it with one explicit question**, in that language. In Spanish: "¿Quieres que el
   cerebro trabaje en español o en inglés? Es el idioma de los playbooks, la bitácora y mis
   respuestas; se puede cambiar después." In English: "Do you want the brain to work in
   Spanish or in English? It is the language of the playbooks, the decision log and my
   answers; it can be changed later."
3. If the organization serves clients in a different language, ask a second question: which
   language drafts for clients should use. It is a separate setting, written next to the
   first.

The answer picks the template set (`templates/es/` or `templates/en/`) and the operating guide,
and it is written into the brain's `CLAUDE.md` ("Idioma de trabajo" / "Working language") and
`_config/fuentes.md`. From then on every skill of the brain reads the language there. Do not
mix sets: a brain born in English gets every file from `templates/en/`.

**What never translates.** Folder and file names, the `## Historial` heading of a playbook,
the `<!-- Vigente desde -->` marker and the decision states (`aplicada`, `por confirmar`,
`propuesta`, `abierta`, `revertida`) are canonical tokens; the other skills navigate by them.
The English templates already keep them and explain them once. Do not "fix" them.

## Phase 0: diagnosis (silent)

Before saying anything about steps, look:

- Is there already a folder whose `CLAUDE.md` starts with `<!-- cerebro-operativo -->`? Check
  the working folder first, then the platform memory entry `cerebro-operativo: <folder>`. If
  there is one, the brain is mounted: offer the audit (`cerebro-audit`) or help with what is
  missing, and stop here. Never create a second brain. A folder named `Cerebro (demo)` does
  not count: it is the sample organization, and its presence never blocks a real install.
- Is Google Drive for desktop installed and syncing on this machine (a mounted drive with the
  person's files)? Is the Google Drive connector available in the app? Is the plugin
  installed (this skill running is evidence that it is)?
- Then present the map in one sentence: "Vamos a hacer cuatro cosas: la carpeta en Drive, la
  entrevista sobre tu empresa, la rutina diaria y una primera reunión de prueba." Nothing more
  technical than that.

## Phase 1: Google Drive (the storage backbone)

The brain lives in Google Drive so the same files are available to every surface: local
sessions read the synced folder, cloud sessions (claude.ai, the phone, the daily routine) read
and write it through the Drive connector, with the computer off.

1. **Google account.** If they do not have one, guide its creation. Never handle the password.
2. **Google Drive for desktop**, for the machines that will consult the brain locally: guide
   the install and sign-in, and locate the mounted drive.
3. **Create the root folder** yourself, once the drive is mounted. Ask only where and what
   name; suggest `Cerebro <Organización>`.
4. **Mark it "available offline"**: guide the right-click. It makes local sessions robust to
   connectivity.
5. **Connect the Google Drive connector** in the Claude app (Settings, Connectors, Google
   Drive, authorize): the person's click. It is what lets the routine and the phone reach the
   folder.
6. Explain the sync contract in one sentence: the cloud wins on doubt, duplicates with `(1)`
   are name clashes, and nothing stays loose because everything that arrives gets filed.

## Phase 1b: environment

**Nothing to install.** The brain is Markdown, one JSON state file, connectors and a scheduled
task. Say nothing about this phase to the person; it exists so every agent of the marketplace
has the same shape. If a future version of any skill of this brain ever needs a program on the
machine, it declares it in a manifest and installs it outside the plugin folder, and this phase
gains a self-check the person can ask for ("¿qué te falta?").

## Phase 2: the organization's context (the interview)

This is the heart of the install and the part Molt accompanies in person in the first
instances. Conduct it yourself in every instance, so the organization can repeat it alone
later. Ask in blocks, one round each, in the confirmed language, and fill the templates as you
go. Every fact you write cites its source (interview and date); nothing is inferred silently.

| Block | Ask about | Fills |
|---|---|---|
| Who they are | what the organization does in their own words, when it started, how many people, how they work | `_config/empresa.md` (from `config/empresa.template.md`) |
| The team | each person, their role, and the two roles the brain needs: who approves values and who executes | `_config/empresa.md`, the "Quién trabaja conmigo" table of `CLAUDE.md`, `_config/fuentes.md` |
| Values | values in their words (not the site's), negotiables, non-negotiables, when a client is let go and how it is said | `_config/valores-y-negociables.md` (the four blocks; leave what they cannot say firmly as pending confirmation) |
| Processes | the processes that exist today, even undocumented ones (proposals, escalations, production, social, events) | one `playbooks/<proceso>.md` per process from `playbook.template.md`, with a single seed section and an empty `## Historial`; canonical file names in lower case, hyphens, no accents |
| Cases | one or two past cases with a client that taught them something | `casos/<AAAA>-<cliente>.md` from `caso.template.md`, with the five parts; ask for the lesson and the value if they do not come up |
| Key clients and tools | who the important clients are, where proposals and projects live, what they use to meet | `_config/empresa.md` |
| Meetings | which recurring meeting is the source of decisions, whether it is recorded (Fathom team, owner), which meetings never enter | `_config/fuentes.md` |
| Time zone and language of clients | their IANA time zone; the clients' language if different | `_config/fuentes.md`, `CLAUDE.md` |
| The routine | in whose account it should run, and at what time (after the main meeting, with margin) | `_config/fuentes.md` (account, days, time; the literal prompt is already in the template) |

Then create the rest of the structure from the templates: `CLAUDE.md` (first line is the
marker, exactly `<!-- cerebro-operativo -->`), `memory.md` with its first dated line,
`decisiones/bitacora.md` empty with its format, `_estado/ultima-ingesta.json` with the time
zone, `reuniones/entrada/README.md`, `salidas/README.md`, and the operating guide of the chosen
language copied into `salidas/`. Write the marker even if nothing else were written: it is what
every other skill and Phase 0 recognize.

**Save the folder to memory** as `cerebro-operativo: <folder name or Drive path>`, so a session
opened elsewhere (the phone, claude.ai) finds it without asking twice.

## Phase 2b: the voice

Run `brand-voice-style-guide` (it ships in the same plugin) over the organization's public site
and channels, plus any texts the team hands over (emails, proposals are the best evidence), and
leave `_config/voz.md`. Ask the person to read one rewrite and say whether it sounds like them;
that is the only test that matters. If they cannot do it now, leave the file with its gaps
named at the top and a task in `memory.md`.

## Phase 3: the plugin

The plugin is already installed if this skill is running. Verify it can see `templates/`,
`demo/` and `docs/` (Phase 0 did), and tell the person how updates arrive: on the computer,
"actualiza el plugin cerebro-operativo" in the chat; on claude.ai, automatically.

## Phase 4: the daily routine

Create the scheduled task on the platform, in the account the person chose, with the literal
prompt written in `_config/fuentes.md` (never paraphrase it), daily on working days at the
chosen time. The person only confirms the slot. Explain in one sentence that it is the only
part of the system that talks to an outside service, that it only fetches transcripts, and
that it writes only inside the folder.

If the organization does not use Fathom, do not block: explain `reuniones/entrada/` (a
transcript dropped there does the same job) and schedule the routine anyway; it will find
nothing until something arrives, and finding nothing is a normal outcome.

## Phase 5: the first heartbeat

Ask for any transcript or the notes of their last meeting and process it end to end with
`transcript-to-playbook-updater` (same plugin). Then check the four outputs together with the
person: the meeting file in `reuniones/`, the lines in `decisiones/bitacora.md`, a playbook
section rewritten with its `## Historial` (or "nothing changed, and here is why"), and
`salidas/ingesta-<fecha>.md`. If those exist, the system is alive.

Close by showing what they can ask for from now on, in their language: "¿cómo manejamos
esto?", "procesa este transcript", "escribe esto con nuestra voz", "¿qué decidimos sobre X?",
"organiza la carpeta".

## Demo mode: seed the fictional organization

Trigger: "puebla el cerebro con la empresa de ejemplo", "seed the demo organization", or a
person who wants to learn or demo before having real documents. Everything in `demo/` is
invented, so it can be shown to anyone.

1. Copy `demo/cerebro/` into the person's Drive as `Cerebro (demo)/`, **next to** their real
   brain if they have one, never inside it.
2. Do not edit the copied files. The folder is already consistent: two playbooks, a three-line
   decision log, a closed case, one ingested meeting with its summary and watermark, and one
   transcript waiting in `reuniones/entrada/`.
3. Say what to try, in order: process the waiting transcript (it adds a decision, rewrites a
   section with history and leaves one inference pending), ask "¿cómo manejamos un cliente
   que maltrata al equipo?", ask what was decided about proposals, request a draft in the
   voice, correct a decision, run the audit. Then process the transcript a second time and
   show that nothing changes.
4. The demo organization is written in Spanish. If the person chose English, say so before
   copying and offer to proceed anyway or to wait for the English demo.
5. **Do not save the demo folder to memory.** The `cerebro-operativo: <folder>` entry is for
   the organization's real brain only; pointing it at the demo would make Phase 0 of the real
   install find "an existing brain" and refuse to create the company's own.
6. When they are done, offer to delete `Cerebro (demo)/`; nothing else references it.

## Error handling

- **Drive not mounted locally:** cloud-only mode still works through the connector; say that
  local sessions need Drive for desktop and continue.
- **Connector not authorized:** go back to Phase 1, step 5; the routine and the phone cannot
  reach the folder without it.
- **Plugin missing its templates:** see "Where the pieces are".
- **The person gets lost on a web step:** ask for a screenshot and guide from what they see.

## Done means

- One folder with the marker on line 1 of its `CLAUDE.md`, in the confirmed language, with
  `_config/` filled from the interview and every gap marked as pending confirmation, not
  guessed.
- The folder name saved to memory.
- The routine scheduled with the literal prompt, or explicitly deferred with `reuniones/
  entrada/` explained.
- One transcript processed end to end and its four outputs shown to the person.
- The person never typed a command, never created a folder, and never heard the name of a
  tool.
