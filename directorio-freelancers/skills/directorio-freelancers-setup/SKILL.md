---
name: directorio-freelancers-setup
description: >-
  v1.0.0 · Zero-command onboarding of a production team's freelancer directory in Spanish or
  English. Asks the language first (mandatory, final) and writes every file and field in it.
  Mounts the Google Drive folder, interviews the team (who coordinates and approves, the pool
  person by person, job types with principals and required certifications, tone per channel),
  turns a pasted list into cards, schedules the weekly certification sweep and runs it once as
  the heartbeat, then says what the directory knows and does not. Also seeds the demo company.
  The person never runs a command. Use it whenever someone wants to install, set up or try the
  freelancer directory, or when another skill cannot find a directory folder. Triggers: "quiero
  instalarlo", "instala el directorio de freelancers", "configura el directorio de producción",
  "puebla el directorio con la productora de ejemplo", "install the freelancer directory", "seed
  the demo production company". [v1.0.0]
---

# directorio-freelancers-setup

## Version 1.0.0

A production team's freelancer directory is a folder with memory: who they can call, for what,
with which certifications and how each person has delivered, kept in files the team can read
and correct. This skill creates that folder for a new organization, with the person doing
nothing but answering questions, pasting the list they already have, and clicking where their
own identity is needed. When it finishes, the directory exists in the organization's Google
Drive, readable and writable from every surface (Cowork, Claude Code, claude.ai on the web and
on the phone), it already holds one card per freelancer the team named, the weekly sweep is
scheduled and has run once, and the person knows exactly what the directory does not know yet.

## Guiding principle

**The person does not run commands, does not create folders and does not edit files.** You
execute everything executable and create every folder and file. The person only does the
clicks that require their identity (signing in, authorizing a connector, confirming a time
slot, sharing a folder), hands over what they already have, and answers the interview. You
never ask for or type a password.

**Plain language, always.** The person installing may know nothing about computers. Do not
name a language, package, repository, marketplace, connector protocol or error code to them;
say what the thing does. Whenever you find yourself about to ask the person to install or
configure something, install or configure it instead and ask only for the permission prompt.

**Idempotent.** Phase 0 detects what already exists and skips it. Running this skill on an
existing directory never creates a second one.

**Nothing of any organization lives in this skill.** Names, channels, job types, certifications
and rules come from the interview and land in the directory's own files. Where this skill says
"the production coordinator", the directory's `CLAUDE.md` says who that is.

## Where the pieces are

This skill ships inside the `directorio-freelancers` plugin. Next to the plugin's `skills/`
folder you will find:

- `templates/es/` and `templates/en/`: what you fill to create the directory. Read
  `templates/README.md` first: it lists what each template becomes.
- `templates/vocabulary.md`: the dictionary of every folder, file, heading, data field, state,
  tier and role name, by key, in each language.
- `demo/es/directorio/` and `demo/en/directory/`: the fictional production company for demo
  mode, once per language, each with the names of its vocabulary column.
- `docs/es/como-operar-el-directorio.md` and `docs/en/how-to-operate-the-directory.md`: the
  operating guide you copy into the directory.

If you cannot find them (this skill was installed alone, without the plugin), stop and tell
the person the directory comes as a plugin, then give them the one message to paste:

> Instala el directorio de freelancers de producción de mi empresa. Viene del marketplace
> AlgortimoTD/molt-agents, plugin directorio-freelancers. Deja listo todo lo que necesite para
> funcionar y avísame cuando esté, sin explicarme los detalles técnicos.

(In English: "Install my company's production freelancer directory. It comes from the
marketplace AlgortimoTD/molt-agents, plugin directorio-freelancers. Get everything it needs
ready and tell me when it is done, without explaining the technical details.")

## Language comes first, and it is final

The directory works in Spanish or in English, and the choice belongs to the organization, not
to you and not to the language of their website. It is the **first question of the
installation and it is mandatory**: nothing is created, no folder, no file, no interview block,
until it is answered.

1. **Detect** the language of the person's first message, and ask in it.
2. **Ask one explicit question** and say that the answer is final. In Spanish: "¿En qué idioma
   quieres que trabaje el directorio, español o inglés? Todo va a quedar en ese idioma: los
   nombres de las carpetas, las fichas, las solicitudes, los reportes y mis respuestas. Después
   no se cambia." In English: "Which language should the directory work in, Spanish or
   English? Everything will be in that language: the folder names, the cards, the requests,
   the reports and my answers. It does not change later."
3. **Do not proceed on an unclear answer.** "Both", "whatever you think" or silence get the
   question again, once, with the reason: every file and folder name depends on it.
4. **Do not ask a second language question.** The language each freelancer writes in is a
   field of that person's card, filled in the interview person by person, and the messages go
   out in it. The folder has one language; the people in it may have another, and that is
   recorded where it belongs.

The answer picks the template set (`templates/es/` or `templates/en/`), the operating guide and
the vocabulary column. Do not mix sets and do not translate a template on the fly: a directory
born in English gets every file from `templates/en/`.

### The vocabulary

Every name in the directory comes from `templates/vocabulary.md`, in the chosen language. This
skill refers to them by key, in braces: `{freelancers}` is the folder of cards, `{rules}` the
assignment rules, `{index}` the regenerated index, `{history}` the heading that keeps replaced
text. The root `CLAUDE.md` template already ends with the vocabulary block of its language;
keep it intact and complete, because the other four skills resolve every name from it,
including in cloud sessions that cannot reach the plugin. The only language-neutral pieces are
the marker `<!-- directorio-freelancers -->` on line 1 and the JSON keys of `{state}`.

## Phase 0: diagnosis (silent)

Before saying anything about steps, look:

- Is there already a folder whose `CLAUDE.md` starts with `<!-- directorio-freelancers -->`?
  Check the working folder first, then the platform memory entry
  `directorio-freelancers: <folder>`. If there is one, the directory is mounted: offer the
  audit (`directorio-freelancers-audit`) or help with what is missing, and stop here. Never
  create a second directory. A folder named `Directorio (demo)` or `Directory (demo)` does not
  count: it is the sample company, and its presence never blocks a real install.
- Is Google Drive for desktop installed and syncing on this machine (a mounted drive with the
  person's files)? Is the Google Drive connector available in the app? Is the Google Calendar
  connector available (optional: the shoot's date and clashes)? Is the plugin installed (this
  skill running is evidence that it is)?
- Then ask the language (above), and present the map in one sentence, in that language:
  "Vamos a hacer cinco cosas: la carpeta en Drive, la entrevista sobre tu equipo y tus
  freelancers, las fichas, el barrido semanal de certificaciones y, al final, te digo qué sabe
  el directorio y qué le falta." Nothing more technical than that.

## Phase 1: Google Drive (the storage backbone)

The directory lives in Google Drive so the same files are available to every surface: local
sessions read the synced folder, cloud sessions (claude.ai, the phone, the weekly sweep) read
and write it through the Drive connector, with the computer off.

1. **Google account.** If they do not have one, guide its creation. Never handle the password.
2. **Google Drive for desktop**, for the machines that will consult the directory locally:
   guide the install and sign-in, and locate the mounted drive.
3. **Create the root folder** yourself, once the drive is mounted. Ask only where and what
   name; suggest `Directorio de producción <Organización>` in Spanish,
   `<Organization> production directory` in English.
4. **Mark it "available offline"**: guide the right-click. It makes local sessions robust to
   connectivity.
5. **Connect the Google Drive connector** in the Claude app (Settings, Connectors, Google
   Drive, authorize): the person's click. It is what lets the sweep and the phone reach the
   folder.
6. **Offer the Google Calendar connector**, read-only, if the team keeps its shoots in a
   calendar: it lets the request drafter read the date, the duration and the clashes. If they
   keep no such calendar, skip it and say nothing more; the drafter works from what the person
   types.
7. Explain the sync contract in one sentence: the cloud wins on doubt, duplicates with `(1)`
   are name clashes, and nothing stays loose because everything that arrives gets filed.

Create `{supports}` right away with its README (`soportes-README.template.md`), so the person
has somewhere to drop certificate photos while you go on.

## Phase 1b: environment

**Nothing to install.** The directory is Markdown, one JSON state file, connectors and a
scheduled task. Say nothing about this phase to the person; it exists so every agent of the
marketplace has the same shape. If a future version of any skill of this directory ever needs
a program on the machine, it declares it in a manifest and installs it outside the plugin
folder, and this phase gains a self-check the person can ask for ("¿qué te falta?").

## Phase 2: the organization's context (the interview)

This is the heart of the install and the part Molt accompanies in person in the first
instances. Conduct it yourself in every instance, so the organization can repeat it alone
later. Ask in blocks, one round each, in the directory's language, and fill the templates as
you go. Every fact you write cites its source (interview and date, or the pasted list);
nothing is inferred silently. What they cannot say firmly becomes a `{gap}` line in `{memory}`,
never a guess.

| Block | Ask about | Fills |
|---|---|---|
| Who they are | what the organization produces, for whom, since when, how many people | `{company}` |
| The people and their roles | each person and their title; then who is the **production coordinator** (at least one: operates daily, creates and edits cards, opens and closes requests), who is the **approver** (exactly one: decides who enters the pool and who is marked `{status-do-not-call}`), and who only **consults** | `{company}` roles table, the table in `CLAUDE.md` |
| The pool, person by person | for each freelancer: name, the channel they actually answer on, the handle or group the coordinator uses there, the language they write in, their specialties with a level in the team's words, what not to ask of them, their certifications with the expiry date and whether a document exists. Accept a pasted list, a spreadsheet export or a photo of a note and turn it into cards; ask only for what the list does not say | one card per freelancer from `ficha.template.md` under `{freelancers}` |
| Job types | the kinds of work they staff; for each, the principals in order (the first is the preferred one), whether they ask one at a time with a wait window (`{mode-sequential}`) or everyone at once (`{mode-simultaneous}`), and which certification the job requires; what they do when nobody answers | `{rules}` |
| Certifications | every certification named in the pool block or the job types block, as the team calls it, who requires it, typical validity, which document they keep; confirm the notice tiers (expired, 7, 30, 60 days, undated, no document) as written in the template | `{certifications}` |
| How they write to freelancers | the tone per channel and per language, how long a message is, who signs; confirm the seven things a message always carries | `{message-templates}` |
| Time zone and the routine | their IANA time zone; in whose account the weekly sweep runs and on which day and time; which calendar, if any, holds the shoots | `{sources}` (the literal prompt is already in the template), `{state}` |

Three rules inside this interview carry the whole product:

- **Limits are constraints, never diagnoses.** When a limit arrives as a personal or medical
  condition ("no le pongan a hacer gráficas con texto porque es disléxico"), write only the
  constraint it implies ("no asignarle gráficas con texto"), add `{rephrased}` with the date
  next to it, and tell the person in one sentence why: the card describes a third party who is
  not in the room, and the constraint is all the directory needs to staff a shoot.
- **Reliability is dated facts.** If the team says "Dani siempre entrega tarde", ask for the
  last time it happened and write that occurrence with its date and who said it. An adjective
  with no occurrence behind it is not written.
- **No date, no validity.** A certification the team believes exists but cannot date goes on
  the card as `{tier-undated}` and in `{memory}` as a `{gap}`; the sweep will keep asking. The
  same for a dated certification with no document: on the card as `{tier-unsupported}`.

Do not leave the roles block without an approver. If nobody wants the role, explain in one
sentence why it exists (without someone who decides who is in and who is out, the pool grows
by accident and nobody can mark a person as not to be called) and ask again; if it still has
no owner, write `{gap}` and it becomes the first gap of Phase 6.

Then create the rest of the structure from the templates: `CLAUDE.md` (first line is the
marker, exactly `<!-- directorio-freelancers -->`; last lines the vocabulary block), `{memory}`
with its first dated line, `{state}` with the time zone and null watermarks, the READMEs of
`{supports}` and `{outputs}`, and the operating guide of the chosen language copied to
`{guide}`. Write the marker even if nothing else were written: it is what every other skill and
Phase 0 recognize.

**Save the folder to memory** as `directorio-freelancers: <folder name or Drive path>`, so a
session opened elsewhere (the phone, claude.ai) finds it without asking twice.

## Phase 3: the plugin

The plugin is already installed if this skill is running. Verify it can see `templates/`,
`demo/` and `docs/` (Phase 0 did), and tell the person how updates arrive: on the computer,
"actualiza el plugin directorio-freelancers" in the chat; on claude.ai, automatically.

## Phase 4: the weekly sweep

Create the scheduled task on the platform, in the account the person chose, with the literal
prompt written in `{sources}` (never paraphrase it), weekly on the chosen day and time. The
person only confirms the slot. Explain in one sentence that it only reads the cards and the
certifications catalog, writes the report and the index inside the folder, and sends nothing
to anyone.

If the team has no certifications at all (a pool of editors, say), schedule it anyway: a sweep
that finds nothing leaves a one-line report, and the first certification someone adds is
covered from the next Monday without anyone remembering to set it up.

## Phase 5: the first sweep (the heartbeat)

The first run is not left to the calendar. Run `certification-expiry-tracker` (same plugin)
by hand, from the account the routine will use, and check the three outputs together with the
person: the `{expiry-report}` with every certification of every card in exactly one tier, the
`{index}` regenerated with one row per card, and `{state}` with the watermark advanced. Then
run it a second time, immediately, and show that nothing changed: the same report date, the
same index, the same watermark. If those two runs behave, the system is alive and the weekly
task will do the same thing on its own.

If a certification lands in a tier the person did not expect, do not fix the card from here:
note what the card says, and let the coordinator correct it through `production-pool-roster`
("Dani renovó su curso, vence el ...") so the change carries its trail.

## Phase 6: what the directory knows and what it does not

The risk of a new directory is not being empty; it is being half full while someone trusts it
as complete, and staffing a shoot from it. Close the installation by saying it out loud, in
the directory's language, without technical words. Build it from the folder, not from memory:
count the cards; the certifications with a date and a document, with a date and no document,
and with no date; the job types with principals and the ones without; the people with a
channel and the ones without; then list what is missing. Its shape:

> Tu directorio ya tiene: ocho fichas, cinco con sus certificaciones al día y con documento,
> una con un curso sin fecha y una con un curso sin documento; cuatro tipos de trabajo con sus
> principales; y el barrido de los lunes ya corrió una vez.
> Todavía no tiene: el curso de seguridad de Fausto con fecha (sin fecha no cuenta), el
> documento del curso de Greta, y nadie como principal para producción con dron fuera de una
> sola persona.
> Mientras eso siga así, cuando pidas un fotógrafo con curso de seguridad para mañana, Fausto
> no va a aparecer en la lista aunque diga que lo tiene. Eso es a propósito.

Write the same inventory in `{memory}`: one dated line per gap, each starting with `{gap}`, so
`directorio-freelancers-audit` chases them from the first week.

Then give the **Drive permissions** that match the roles, as the table in `{sources}` says and
as a short list the person applies with their own clicks (sharing is their identity): the
production coordinator and the approver as editors of the folder, the viewers as viewers, the
routine's account as editor. Say why in one sentence: the directory cannot tell who is writing
to it, so the folder's permissions are what decide who can change it.

Close by showing what they can ask for from now on, in their language: "necesito un fotógrafo
mañana a las 7 en <lugar>, exige <certificación>", "<persona> dijo que sí", "agrega a
<persona>", "<persona> renovó su curso", "¿quién sabe hacer X?", "¿qué certificaciones
vencen?", "organiza la carpeta".

## Demo mode: seed the fictional production company

Trigger: "puebla el directorio con la productora de ejemplo", "seed the demo production
company", or a person who wants to learn or demo before having a real pool. Everything in
`demo/` is invented, so it can be shown to anyone.

1. **Pick the language of the demo.** It is the language of the person's directory when they
   have one (the `lang:` line of its vocabulary block). Without a directory, ask the same
   explicit question as the installation, in the language of their message, but say that this
   answer is only for the demo and does not fix the language of a future directory. Never copy
   one language and translate on the fly: each copy is already written in its own vocabulary.

   | Language | Copy from | Into Drive as |
   |---|---|---|
   | Spanish | `demo/es/directorio/` | `Directorio (demo)/` |
   | English | `demo/en/directory/` | `Directory (demo)/` |

2. Copy it into the person's Drive, **next to** their real directory if they have one, never
   inside it.
3. Do not edit the copied files. The folder is already consistent: eight cards whose
   certifications cross every tier, the rules of a team that staffs by priority, one closed
   request, a sweep report and an index dated the Monday before, and a watermark that matches
   them. The copy's own vocabulary block resolves those names, like in any directory.
4. Say what to try, in order and in the demo's language, exactly as `demo/README.md` lists it:
   the bridge case ("necesito un fotógrafo mañana a las 7:00 para las vigas del puente nuevo
   en la vía norte, exige curso de seguridad en obra": three on the shortlist, two excluded
   with reasons, three drafts), the answers ("Ariel no puede; Bel dijo que sí a las 3:40"),
   who knows what ("¿quién edita con detalle?", "¿quién hace gráficas con texto?"), the sweep
   twice, a renewal ("Dani renovó su curso de seguridad, vence el 2027-09-28"), and the audit.
5. **Do not save the demo folder to memory.** The `directorio-freelancers: <folder>` entry is
   for the organization's real directory only; pointing it at the demo would make Phase 0 of
   the real install find "an existing directory" and refuse to create the company's own.
6. When they are done, offer to delete the demo folder; nothing else references it.

## Error handling

- **Drive not mounted locally:** cloud-only mode still works through the connector; say that
  local sessions need Drive for desktop and continue.
- **Connector not authorized:** go back to Phase 1, step 5; the sweep and the phone cannot
  reach the folder without it.
- **Calendar connector declined or absent:** nothing breaks; the request drafter reads the date
  from the person and writes "no se leyó" in the calendar line of each request.
- **Plugin missing its templates:** see "Where the pieces are".
- **A pasted list you cannot parse** (a photo too blurry, a spreadsheet with no headers): say
  which rows you could read, create those cards, and list the rest as gaps instead of guessing
  a channel or a date.
- **The person gets lost on a web step:** ask for a screenshot and guide from what they see.

## Done means

- The language was asked first and answered; one folder with the marker on line 1 of its
  `CLAUDE.md` and the complete vocabulary block at its end, every file and folder name, every
  heading and every data field in that language, nothing from the other set.
- `{company}` has a roles table with at least one production coordinator and exactly one
  approver, or the missing approver is the first gap; no rule in `CLAUDE.md` names a person
  where it should name a role.
- One card per freelancer the team named, each with its five data fields or the missing ones
  listed as gaps; every limit written as a constraint; every reliability line a dated fact;
  every certification dated or marked undated.
- `{rules}`, `{certifications}` and `{message-templates}` filled from the interview, every gap
  marked, not guessed.
- The folder name saved to memory.
- The weekly sweep scheduled with the literal prompt, and run twice by hand with the second run
  changing nothing.
- The inventory said to the person, one `{gap}` line per gap in `{memory}`, and the Drive
  permissions list given.
- The person never typed a command, never created a folder, and never heard the name of a
  tool.
