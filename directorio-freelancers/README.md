# Directorio de freelancers

The **production freelancer directory** of a small production company or agency, run by Claude on top of a Google Drive folder: one card per freelancer (what they are good at, what not to ask of them, which certifications they hold and when they expire, how they have delivered, which channel and language to write them in), the shortlist and the messages for every shoot, and a weekly list of certifications about to expire. Usable from the computer (Cowork, Claude Code), the web and the phone against the same folder.

## What it does

- **Keeps one card per freelancer** (`production-pool-roster`): creates or updates a card from a sentence ("agrega a Ariel, director de fotografía, Messenger, inglés, curso de alturas vence en marzo") or a pasted list, answers "who can edit with care" with the card and its source, and regenerates the index the team reads from the phone. Reliability is written as dated facts the team stated, never a score; a limit dictated as a personal condition is rephrased as the assignment constraint it implies.
- **Tracks certifications about to expire** (`certification-expiry-tracker`): a weekly sweep writes the report by tier (expired, 7, 30, 60 days, undated, no supporting document) and answers "who holds a valid heights course on that date". Valid means it expires after the shoot's date; undated never counts.
- **Drafts the availability request** (`availability-request-drafter`): from "tomorrow 7:00, the beams of a bridge, safety course required" it writes the shortlist in the team's priority order with a reason per name and per exclusion, one message per person in their channel and language, and, as the team reports back, who answered when, who got it, and the invite text for a person to send.
- **Keeps itself in order** (`directorio-freelancers-audit`): weekly routine that flags cards broken by hand edits, undated certifications, requests past their date without closure, index and watermark drift, and polices the agent / context separation.
- **Installs itself** (`directorio-freelancers-setup`): "quiero instalarlo" mounts the folder, interviews the organization (who coordinates, job types and preferred people, request mode, certifications per job type, tone per channel), creates the first cards, schedules the weekly sweep and runs it once. The user never runs a command or creates a folder.

## How the directory gets populated

Four ways, each with the name and date of who gave the information: the setup interview (the pool as the team knows it today, specialty by specialty); an existing list pasted in the chat (the agent turns it into cards; it never reads WhatsApp or Messenger groups); every request and every shoot (who answered, how fast, who got it, how they delivered); and the production coordinator editing a card in the chat or by hand in Drive, with the agent re-reading before it writes.

## The three layers

| Layer | Where it lives | Shared |
|---|---|---|
| The engine (skills, templates, routine prompt, demo) | this plugin | yes, 100 percent agnostic |
| The organization's context (`CLAUDE.md`, `_config/`, the memory file, the watermark) | the organization's own Drive folder | no |
| The organization's records (cards, requests, reports) | the same folder | no |

## Installation

In Claude Code or the Claude desktop app, with the future directory folder open as the project, paste this and approve the permission prompts (or switch the app to automatic permissions):

> "Instala el directorio de freelancers de producción de mi empresa. Viene del marketplace AlgortimoTD/molt-agents, plugin directorio-freelancers. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos."

When it answers "listo", say **"quiero instalarlo"**. `directorio-freelancers-setup` takes over: Google Drive (desktop app, offline folder, Drive connector), the root `CLAUDE.md` and `_config/` from the templates through a guided interview, the first cards, the weekly routine, and a first sweep end to end.

claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add. The repository is public: no GitHub App grant is needed. CLI users: `claude plugin marketplace add AlgortimoTD/molt-agents` and `claude plugin install directorio-freelancers@molt-agents`.

## User guide

For the people who use the directory: [docs/user-guide.html](docs/user-guide.html), in Spanish and English, with two views. The quick guide: one card per feature with the exact phrase to say. The complete guide: numbered chapters from installing the directory to testing every feature on the demo company. Its source is [docs/user-guide.json](docs/user-guide.json), built with the `orb-agent-user-guide` skill; regenerate it with that skill, never by hand.

## Try it with the demo production company

Say **"puebla el directorio con la productora de ejemplo"** or **"seed the demo production company"**: a fully fictional production company ([demo/](demo/README.md)), in Spanish or in English to match your directory, with eight freelancer cards whose certifications cross every expiry tier, the rules of a team that staffs shoots by priority, one closed request and one shoot waiting to be staffed. Running the bridge case shows the whole mechanism in five minutes, with nothing real exposed. Delete the folder when done.

## Languages

Spanish and English. The setup asks the language first and creates the directory in it (templates, demo and operating guide exist in both under `templates/`, `demo/` and `docs/`). Each freelancer's card also records that person's language, and the messages come out in it.

## Requirements

None on the computer: the directory is Markdown, one JSON state file, connectors and a scheduled task. Connectors: Google Drive (required; Drive for desktop on the machines that consult locally, the Drive connector for cloud sessions and for the routine), Google Calendar (optional, read-only: the shoot's date and clashes with what is already scheduled). Cloud sessions need nothing installed.

## What it does NOT do

It does not write to the freelancers: there is no WhatsApp or Messenger connector, and the messages are drafts a person pastes and sends. It does not book, hire or pay crews; the calendar invite is sent by a person with the text the agent leaves. It does not rate a person without the team's criteria: it writes the dated facts the team states, and the judgment stays with the team.
