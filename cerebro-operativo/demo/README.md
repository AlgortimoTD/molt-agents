# Demo organization (100 percent fictional data)

A ready-made brain to learn, test and demo the agent **without touching any real organization**. Every person, company, client, date and quote here is invented; every file carries a fictional-document notice ("DOCUMENTO FICTICIO" in Spanish, "FICTIONAL DOCUMENT" in English). A privacy grep of this folder must return no real person, company or client.

## One organization, two languages

The same organization exists twice, once per language the brain works in. Both copies tell the same story, file for file, and each one follows the vocabulary of its language ([templates/vocabulary.md](../templates/vocabulary.md)): folder and file names, headings, markers, decision states and roles.

| Language | Folder | Copied to Drive as | Example names |
|---|---|---|---|
| Spanish | `es/cerebro/` | `Cerebro (demo)` | `decisiones/bitacora.md`, `reuniones/entrada/`, `## Historial`, `por confirmar` |
| English | `en/brain/` | `Brain (demo)` | `decisions/log.md`, `meetings/inbox/`, `## History`, `pending confirmation` |

`cerebro-setup` copies the one that matches the language of the person's brain, or the language they choose when they have no brain yet. The two copies never mix, and a change to the story is made in both.

## What is inside

Both copies hold the brain of **Faro Estudio**, a fictional five-person digital design agency: `CLAUDE.md` with the marker and the vocabulary block of its language, the four configuration files (company, values with two non-negotiables, voice, sources with the roles table: Marina is the brain owner, Tomás and Julia editors), the memory file with two open gaps, an old manual in the documents folder (2023) from which two sections of the escalations playbook were written, one of them still pending confirmation because nobody has said whether it holds, two playbooks (proposals, escalations) with one history entry, a decision log with **three lines** (two applied, one pending confirmation), one closed case (`2025-nebula.md`), one meeting already ingested (2026-09-08) with its ingestion summary, and the watermark pointing at it.

**One transcript is not yet processed**, waiting in the inbox (`es/cerebro/reuniones/entrada/2026-09-15-reunion-semanal.md`, `en/brain/meetings/inbox/2026-09-15-weekly-meeting.md`). It contains one explicit decision (no proposal without a discovery call), one inference that must stay pending confirmation (asking new clients for references), one open action item, and noise. Processing it rewrites the discovery call section of the proposals playbook with history, adds lines to the log, advances the watermark and leaves the ingestion report of 2026-09-15. That is the demo's before and after.

The story is deliberately small: an agency that decided last week to put schedules in every proposal, that has one hard lesson about protecting its team from a difficult client, and that this week decides to stop sending proposals blind.

## How to use it

Ask the agent: **"puebla el cerebro con la empresa de ejemplo"** or **"seed the demo organization"**. `cerebro-setup` copies the demo of your language into your Drive, next to your real brain if you have one, never inside it. Then run the use cases (Spanish phrase / English phrase):

1. "procesa el transcript que está en entrada" / "process the transcript in the inbox": meeting file, three new log lines (one applied, one pending confirmation, one open), the discovery call section rewritten with its history, the ingestion report of 2026-09-15.
2. "¿cómo manejamos un cliente que maltrata al equipo?" / "how do we handle a client who mistreats the team?": the non-negotiable, the Nébula case, the escalations playbook, every claim with file and date.
3. "¿qué decidimos sobre las propuestas?" / "what did we decide about proposals?": the log lines of 2026-09-08 and 2026-09-15 with their meetings and minutes.
4. "escribe este correo con nuestra voz" / "write this email in our voice": a draft following the voice guide, marked for review.
5. "esa decisión quedó mal, corrígela" / "that decision was wrong, correct it": a correcting line, the playbook restored from history, the wrong text kept.
6. "organiza la carpeta" / "organize the folder": the audit report in the audits folder.

Run use case 1 twice: the second run changes nothing (the watermark).

Delete the demo folder whenever you are done; nothing else references it.
