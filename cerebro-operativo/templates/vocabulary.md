# Vocabulary of a brain

A brain works in one language, chosen by the organization in the first question of the
installation and fixed from then on. **Everything the agent writes into the folder is in that
language**: folder and file names, headings, markers, decision states, role names and prose.
The skills are written in English and never carry a literal name of the folder; they refer to
each thing by its **key**, and the brain's own `CLAUDE.md` says what that key is called in
this brain.

## How a skill resolves a name

The root `CLAUDE.md` of every brain ends with a machine block, an HTML comment that does not
render, with one `key: name` line per row of the table below, in the brain's language:

```
<!-- cerebro-operativo:vocabulary
lang: es
log: decisiones/bitacora.md
history: ## Historial
...
-->
```

Every skill reads that block before touching the folder and uses the names it gives. The block
travels with the brain, so a cloud session that cannot reach the plugin files still resolves
every name. `cerebro-setup` writes it from the column of the chosen language; nobody edits it by
hand, and `cerebro-audit` checks that it is present and complete.

Only two things are identical in every language, because they are identifiers and not text a
person reads: the marker `<!-- cerebro-operativo -->` on line 1 (a session has to find the
brain before it knows its language) and the keys of `{state}`, which is JSON read only by the
skills.

## The dictionary

This table is the single source. The `CLAUDE.root.template.md` of `es/` and of `en/` carry
their column as the block above, and every template uses the names of its own column.

| Key | es | en | What it is |
|---|---|---|---|
| `memory` | `memoria.md` | `memory.md` | loose agreements and gaps, one dated line each |
| `company` | `_config/empresa.md` | `_config/company.md` | who they are, team, fronts, clients, tools |
| `values` | `_config/valores-y-negociables.md` | `_config/values-and-negotiables.md` | values, negotiables, non-negotiables |
| `voice` | `_config/voz.md` | `_config/voice.md` | the voice guide |
| `sources` | `_config/fuentes.md` | `_config/sources.md` | meetings, time zone, language, roles, routine |
| `playbooks` | `playbooks/` | `playbooks/` | one file per process |
| `log` | `decisiones/bitacora.md` | `decisions/log.md` | append-only decision log |
| `cases` | `casos/` | `cases/` | past cases |
| `meetings` | `reuniones/` | `meetings/` | ingested transcripts |
| `meetings-inbox` | `reuniones/entrada/` | `meetings/inbox/` | transcripts dropped by hand |
| `documents` | `documentos/` | `documents/` | documents the organization already had, ingested at installation or later |
| `outputs` | `salidas/` | `outputs/` | run reports, audits, the operating guide |
| `ingestion-report` | `salidas/ingesta-AAAA-MM-DD.md` | `outputs/ingestion-YYYY-MM-DD.md` | the report of one routine run |
| `audit-report` | `salidas/auditorias/AAAA-MM-DD-auditoria.md` | `outputs/audits/YYYY-MM-DD-audit.md` | the report of one audit |
| `kickoff-script` | `salidas/guion-reunion-de-arranque.md` | `outputs/kickoff-meeting-script.md` | the script handed over before the kickoff meeting |
| `guide` | `salidas/como-operar-el-cerebro.md` | `outputs/how-to-operate-the-brain.md` | the operating guide |
| `state` | `_estado/ultima-ingesta.json` | `_state/last-ingestion.json` | the watermark |
| `history` | `## Historial` | `## History` | heading that keeps replaced text in a playbook or in the values file |
| `current-since` | `Vigente desde AAAA-MM-DD (origen: ...)` | `Current since YYYY-MM-DD (origin: ...)` | marker above the current text of a section, always written inside an HTML comment (`<!-- ... -->`); the block carries only the inner text, because a comment cannot nest |
| `case-lesson` | `## Qué se aprendió` | `## What was learned` | case section the audit checks |
| `case-value` | `## Qué valor se aplicó` | `## Which value applied` | case section the audit checks |
| `meeting-summary` | `## Resumen` | `## Summary` | section of a meeting file |
| `meeting-decisions` | `## Decisiones extraídas` | `## Extracted decisions` | section of a meeting file |
| `meeting-pending` | `## Por confirmar` | `## Pending confirmation` | section of a meeting file |
| `meeting-discarded` | `## Descartado` | `## Discarded` | section of a meeting file |
| `meeting-transcript` | `## Transcripción` | `## Transcript` | last section of a meeting file: the original transcript, kept whole |
| `value-proposals` | `## Cambios propuestos a valores, esperando aprobación` | `## Proposed changes to values, awaiting approval` | section of an ingestion report |
| `unanswered` | `Pregunta sin respuesta escrita:` | `Unanswered question:` | prefix of a memory line the responder writes |
| `gap` | `Hueco:` | `Gap:` | prefix of a memory line the installation inventory writes |
| `pending-kickoff` | `Reunión de arranque pendiente` | `Kickoff meeting pending` | memory line when the kickoff meeting could not happen at installation |
| `draft-marker` | `> BORRADOR: para revisar antes de enviar. Este agente no envía nada.` | `> DRAFT: review before sending. This agent sends nothing.` | first line of any draft |
| `applied` | `aplicada` | `applied` | state: changed a playbook |
| `confirmed` | `confirmada` | `confirmed` | state: someone said a written section still holds; touched no text |
| `to-confirm` | `por confirmar` | `pending confirmation` | state: inferred, touched nothing |
| `proposed` | `propuesta` | `proposed` | state: touches values, waits for the owner |
| `open` | `abierta` | `open` | state: an owned action not yet done |
| `reverted` | `revertida` | `reverted` | state: undone by a later line |
| `role-owner` | `responsable del cerebro` | `brain owner` | role: changes anything, approves values |
| `role-editor` | `editor` | `editor` | role: changes playbooks and cases, proposes the rest |
| `role-viewer` | `consulta` | `viewer` | role: asks; any change it requests is a proposal |

## Adding a language or a key

A new key is a new row here, a new line in the block of both root templates, and the skills
that need it referring to it by key. A new language is a new column, a new template set under
`templates/<lang>/`, a new operating guide under `docs/<lang>/`, and the language question of
`cerebro-setup` gaining the option. No skill text changes for a new language: that is the
point of the keys.
