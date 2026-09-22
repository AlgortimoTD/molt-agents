# Demo organization (100 percent fictional data)

A ready-made brain to learn, test and demo the agent **without touching any real organization**. Every person, company, client, date and quote here is invented; every file carries a "DOCUMENTO FICTICIO" notice. A privacy grep of this folder must return no real person, company or client.

## What is inside

| Path | What it is |
|---|---|
| `cerebro/` | The brain of **Faro Estudio**, a fictional five-person digital design agency, already following the pattern of a Spanish brain: `CLAUDE.md` with the marker and the Spanish vocabulary block, `_config/` (company, values with two non-negotiables, voice, sources with the roles table: Marina is the brain owner, Tomás and Julia editors), `memoria.md` with two open gaps, an old manual in `documentos/` (2023) from which two sections of `escalaciones` were written, one of them still pending confirmation because nobody has said whether it holds, two playbooks (`propuestas`, `escalaciones`) with one history entry, a decision log with **three lines** (two applied, one "por confirmar"), one closed case (`casos/2025-nebula.md`), one meeting already ingested (`reuniones/2026-09-08-reunion-semanal.md`) with its ingest summary, and the watermark pointing at it. |
| `cerebro/reuniones/entrada/2026-09-15-reunion-semanal.md` | **One transcript not yet processed.** It contains one explicit decision (no proposal without a discovery call), one inference that must stay "por confirmar" (asking new clients for references), one open action item, and noise. Processing it rewrites the "Llamada de descubrimiento" section of `playbooks/propuestas.md` with history, adds lines to the log, advances the watermark and leaves `salidas/ingesta-2026-09-15.md`. That is the demo's before and after. |

The story is deliberately small: an agency that decided last week to put schedules in every proposal, that has one hard lesson about protecting its team from a difficult client, and that this week decides to stop sending proposals blind.

## How to use it

Ask the agent: **"puebla el cerebro con la empresa de ejemplo"**. `cerebro-setup` copies `cerebro/` into your Drive as `Cerebro (demo)\`, next to your real brain if you have one, never inside it. Then run the use cases:

1. "procesa el transcript que está en entrada": meeting file, three new log lines (one `aplicada`, one `por confirmar`, one `abierta`), the "Llamada de descubrimiento" section rewritten with its history, `salidas/ingesta-2026-09-15.md`.
2. "¿cómo manejamos un cliente que maltrata al equipo?": the non-negotiable, the Nébula case, the escalation playbook, every claim with file and date.
3. "¿qué decidimos sobre las propuestas?": the log lines of 2026-09-08 and 2026-09-15 with their meetings and minutes.
4. "escribe este correo con nuestra voz": a draft following `_config/voz.md`, marked for review.
5. "esa decisión quedó mal, corrígela": a correcting line, the playbook restored from history, the wrong text kept.
6. "organiza la carpeta": the audit report in `salidas/auditorias/`.

Run use case 1 twice: the second run changes nothing (the watermark).

Delete `Cerebro (demo)\` whenever you are done; nothing else references it.
