# Cerebro operativo

The **operating brain of an organization**, run by Claude on top of a Google Drive folder: how the organization does things, why, and what happened the previous times, kept current from its own recorded meetings and answered with sources, in the organization's voice. Usable from the computer (Cowork, Claude Code), the web and the phone against the same folder.

## What it does

- **Answers "how do we handle this"** (`escalation-playbook-responder`): the values that apply, what is negotiable and what is not, the closest documented case, and the source of every claim (file and date). When something is not documented it says so and offers to record it. Drafts only on request, marked for human review.
- **Turns every recorded meeting into playbook updates and a decision log** (`transcript-to-playbook-updater`): one file per meeting with its summary and extracted decisions; new lines in the append-only log with date, reason, source meeting and minute; playbook sections rewritten with the previous text kept in their history. Only explicit decisions enter; the rest stays "por confirmar".
- **Runs a daily routine** (scheduled task in one account, in the cloud): reads the watermark, fetches the new internal meetings from Fathom, processes each transcript, leaves an ingest summary. Idempotent: running it twice changes nothing.
- **Writes with the organization's voice** (`brand-voice-style-guide`): a voice guide generated from the public site and channels, kept in the folder and followed by every draft.
- **Keeps itself in order** (`cerebro-audit`): weekly routine that re-files strays, checks the watermark against the meetings, the log against the playbooks, flags stale "por confirmar" items, and polices the agent / context separation.
- **Installs itself** (`cerebro-setup`): "quiero instalarlo" mounts the folder, interviews the organization for its context, schedules the routine and runs a first heartbeat. The user never runs a command or creates a folder.

## The three layers

| Layer | Where it lives | Shared |
|---|---|---|
| The engine (skills, templates, routine prompt, demo) | this plugin | yes, 100 percent agnostic |
| The organization's context (`CLAUDE.md`, `_config/`, the memory file, the watermark) | the organization's own Drive folder | no |
| The organization's records (playbooks, decisions, cases, meetings, outputs) | the same folder | no |

## Installation

In Claude Code or the Claude desktop app, with the future brain folder open as the project, paste this and approve the permission prompts (or switch the app to automatic permissions):

> "Instala el cerebro operativo de mi empresa. Viene del marketplace AlgortimoTD/molt-agents, plugin cerebro-operativo. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos."

When it answers "listo", say **"quiero instalarlo"**. `cerebro-setup` takes over: Google Drive (desktop app, offline folder, Drive connector), the root `CLAUDE.md` and `_config/` from the templates through a guided interview, the voice guide, the daily routine, and a first transcript processed end to end.

claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add. The repository is public: no GitHub App grant is needed. CLI users: `claude plugin marketplace add AlgortimoTD/molt-agents` and `claude plugin install cerebro-operativo@molt-agents`.

## User guide

For the people who use the brain: [docs/user-guide.html](docs/user-guide.html), in Spanish and English, with two views. The quick guide: one card per feature with the exact phrase to say. The complete guide: eight chapters that take a reader from installing the brain (Claude desktop app, Code section, the message above) to testing every feature on the demo organization, each step with what to do, what appears and how to check it. Its source is [docs/user-guide.json](docs/user-guide.json), built with the `orb-agent-user-guide` skill; regenerate it with that skill, never by hand.

## Try it with the demo organization

Say **"puebla el cerebro con la empresa de ejemplo"**: a fully fictional agency ([demo/](demo/README.md)) with two playbooks, a decision log, a closed case and one meeting transcript not yet processed. Processing it adds a decision, rewrites a playbook section with history and leaves one inference "por confirmar": the whole mechanism in five minutes, with nothing real exposed. Delete the folder when done.

## Languages

Spanish and English. The setup detects the language of your first message, asks you to confirm it, and creates the brain in that language (templates and operating guide exist in both under `templates/` and `docs/`). Folder and file names stay the same in both languages because the skills navigate by them.

## Requirements

None on the computer: the brain is Markdown, one JSON state file, connectors and a scheduled task. Connectors: Google Drive (required; Drive for desktop on the machines that consult locally, the Drive connector for cloud sessions and for the routine), Fathom (optional, read-only; a pasted transcript does the same job). Cloud sessions need nothing installed.

## What it does NOT do

It does not make decisions with clients or send anything to a client on its own; it does not record meetings (Fathom or a pasted transcript feeds it); it does not connect to WhatsApp or Messenger; it does not invent a policy: what is not written is declared, not filled in.
