# Vocabulary of a directory

A directory works in one language, chosen by the organization in the first question of the
installation and fixed from then on. **Everything the agent writes into the folder is in that
language**: folder and file names, headings, data fields, request states, expiry tiers, role
names and prose. The skills are written in English and never carry a literal name of the
folder; they refer to each thing by its **key**, and the directory's own `CLAUDE.md` says what
that key is called in this directory.

The one thing written in a second language is a message to a freelancer: it goes out in the
language recorded on that person's card (`field-language`), because the message is for them and
not for the folder.

## How a skill resolves a name

The root `CLAUDE.md` of every directory ends with a machine block, an HTML comment that does not
render, with one `key: name` line per row of the table below, in the directory's language:

```
<!-- directorio-freelancers:vocabulary
lang: es
freelancers: freelancers/
index: salidas/directorio.md
history: ## Historial
...
-->
```

Every skill reads that block before touching the folder and uses the names it gives. The block
travels with the directory, so a cloud session that cannot reach the plugin files still resolves
every name. `directorio-freelancers-setup` writes it from the column of the chosen language;
nobody edits it by hand, and `directorio-freelancers-audit` checks that it is present and
complete.

Only two things are identical in every language, because they are identifiers and not text a
person reads: the marker `<!-- directorio-freelancers -->` on line 1 (a session has to find the
directory before it knows its language) and the keys of `{state}`, which is JSON read only by
the skills.

## The dictionary

This table is the single source. The `CLAUDE.root.template.md` of `es/` and of `en/` carry
their column as the block above, and every template uses the names of its own column.

| Key | es | en | What it is |
|---|---|---|---|
| `memory` | `memoria.md` | `memory.md` | gaps and loose agreements, one dated line each |
| `company` | `_config/empresa.md` | `_config/company.md` | who they are, team and roles, time zone |
| `rules` | `_config/reglas-de-asignacion.md` | `_config/assignment-rules.md` | job types, principals and preferred, mode and window, certification per job type |
| `certifications` | `_config/certificaciones.md` | `_config/certifications.md` | the certifications the organization recognizes and the notice tiers |
| `message-templates` | `_config/plantillas-de-mensaje.md` | `_config/message-templates.md` | tone per channel and language, what a message always carries |
| `sources` | `_config/fuentes.md` | `_config/sources.md` | routine account, time and literal prompt; calendar read; Drive permissions per role |
| `freelancers` | `freelancers/` | `freelancers/` | one card per person |
| `supports` | `freelancers/soportes/` | `freelancers/documents/` | photos or PDFs of certificates, when they exist |
| `requests` | `solicitudes/` | `requests/` | one file per shoot |
| `request-file` | `solicitudes/AAAA-MM-DD-<produccion>.md` | `requests/YYYY-MM-DD-<shoot>.md` | the name pattern of a request |
| `outputs` | `salidas/` | `outputs/` | the index, the sweep reports, the audits, the operating guide |
| `index` | `salidas/directorio.md` | `outputs/directory.md` | the regenerated index of the whole pool |
| `expiry-report` | `salidas/vencimientos-AAAA-MM-DD.md` | `outputs/expiries-YYYY-MM-DD.md` | the report of one sweep |
| `audit-report` | `salidas/auditorias/AAAA-MM-DD-auditoria.md` | `outputs/audits/YYYY-MM-DD-audit.md` | the report of one audit |
| `guide` | `salidas/como-operar-el-directorio.md` | `outputs/how-to-operate-the-directory.md` | the operating guide |
| `state` | `_estado/ultimo-barrido.json` | `_state/last-sweep.json` | the watermark |
| `history` | `## Historial` | `## History` | heading that keeps replaced text in a card or a config file |
| `current-since` | `Vigente desde AAAA-MM-DD (origen: ...)` | `Current since YYYY-MM-DD (origin: ...)` | marker above the current text of a section, always inside an HTML comment |
| `card-data` | `## Datos` | `## Data` | first section of a card: the data block, one `field: value` line each |
| `card-specialties` | `## Especialidades` | `## Specialties` | what the person does and at what level, one line each |
| `card-limits` | `## Límites de asignación` | `## Assignment limits` | what not to ask of the person, as constraints |
| `card-certifications` | `## Certificaciones` | `## Certifications` | table: certification, issuer, expires, supporting document |
| `card-reliability` | `## Confiabilidad (hechos)` | `## Reliability (facts)` | dated facts the team stated, one line each |
| `card-shoots` | `## Producciones` | `## Shoots` | the requests this person was shortlisted for, answered or got |
| `card-notes` | `## Notas del equipo` | `## Team notes` | anything else the team wants to remember, dated |
| `field-name` | `nombre` | `name` | data block field |
| `field-channel` | `canal` | `channel` | data block field: where the person actually answers (WhatsApp, Messenger, other) |
| `field-contact` | `contacto` | `contact` | data block field: the handle or group the coordinator uses in that channel |
| `field-language` | `idioma` | `language` | data block field: the language the person writes in |
| `field-status` | `estado` | `status` | data block field: one of the three statuses below |
| `status-active` | `activo` | `active` | status: can be shortlisted |
| `status-paused` | `en pausa` | `paused` | status: not shortlisted for now, with the dated reason in the card |
| `status-do-not-call` | `no volver a llamar` | `do not call` | status: decided by the approver, with the dated reason in the card |
| `request-requirements` | `## Requisitos` | `## Requirements` | section of a request |
| `request-shortlist` | `## Lista corta` | `## Shortlist` | section of a request: ordered, with a reason per name |
| `request-excluded` | `## Excluidos y por qué` | `## Excluded and why` | section of a request |
| `request-messages` | `## Mensajes` | `## Messages` | section of a request: one draft per person |
| `request-answers` | `## Respuestas` | `## Answers` | section of a request: time, person, answer |
| `request-assigned` | `## Quién quedó` | `## Who got it` | section of a request |
| `request-invite` | `## Texto de la invitación` | `## Invite text` | section of a request: for a person to send |
| `request-closure` | `## Cierre` | `## Closure` | section of a request: how each person delivered, as facts |
| `mode-sequential` | `secuencial` | `sequential` | request mode: the preferred person first, then the next after the wait window |
| `mode-simultaneous` | `simultáneo` | `simultaneous` | request mode: all principals at once, the first to answer gets it |
| `state-open` | `abierta` | `open` | request state: messages drafted, waiting for answers |
| `state-assigned` | `asignada` | `assigned` | request state: someone got it |
| `state-closed` | `cerrada` | `closed` | request state: the shoot happened and the facts went to the cards |
| `state-unfilled` | `sin cubrir` | `unfilled` | request state: nobody could, and the team was told |
| `tier-expired` | `vencida` | `expired` | expiry tier |
| `tier-7` | `vence en 7 días` | `expires within 7 days` | expiry tier |
| `tier-30` | `vence en 30 días` | `expires within 30 days` | expiry tier |
| `tier-60` | `vence en 60 días` | `expires within 60 days` | expiry tier |
| `tier-undated` | `sin fecha` | `undated` | expiry tier: never counts as valid |
| `tier-unsupported` | `sin soporte` | `no supporting document` | expiry tier: has a date but no document in `{supports}` |
| `draft-marker` | `> BORRADOR: para pegar y enviar desde tu teléfono. Este agente no envía nada.` | `> DRAFT: paste and send from your phone. This agent sends nothing.` | first line of every message and of the invite text |
| `rephrased` | `Reformulado como restricción de asignación el AAAA-MM-DD` | `Rephrased as an assignment constraint on YYYY-MM-DD` | note next to a limit that arrived as a personal condition |
| `gap` | `Hueco:` | `Gap:` | prefix of a memory line the installation inventory or a skill writes |
| `role-coordinator` | `coordinación de producción` | `production coordinator` | role: operates daily, creates and edits cards, opens and closes requests |
| `role-approver` | `aprueba altas y bajas` | `approver` | role: reviews the cards the coordinator created (the audit lists them) and alone marks `status-do-not-call` or takes a person out of the pool |
| `role-viewer` | `consulta` | `viewer` | role: asks; any change it requests is a proposal for the coordinator |

## Adding a language or a key

A new key is a new row here, a new line in the block of both root templates, and the skills
that need it referring to it by key. A new language is a new column, a new template set under
`templates/<lang>/`, a new operating guide under `docs/<lang>/`, a new demo copy under
`demo/<lang>/`, and the language question of `directorio-freelancers-setup` gaining the option.
No skill text changes for a new language: that is the point of the keys.
