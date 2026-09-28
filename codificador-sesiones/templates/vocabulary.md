# Vocabulary of a research folder

A research folder works in one language, fixed at installation. **Everything the agent writes
into the folder is in that language**: folder and file names, headings, markers, states and
prose. The skills are written in English and never carry a literal name of the folder; they
refer to each thing by its **key**, and the folder's own `CLAUDE.md` says what that key is
called in this folder.

Version 0.1 ships the Spanish column only (`templates/es/`). The keys are what make a second
language a matter of adding a column and a template set, without touching a skill.

## How a skill resolves a name

The root `CLAUDE.md` of every research folder ends with a machine block, an HTML comment that
does not render, with one `key: name` line per row of the table below:

```
<!-- codificador-sesiones:vocabulary
lang: es
codebook: libro-de-codigos.md
...
-->
```

Every skill reads that block before touching the folder and uses the names it gives. Names
under a study (`codebook`, `sessions`, `matrix`, ...) are relative to that study's folder,
`{studies}<slug-del-estudio>/`. `codificador-sesiones-setup` writes the block; nobody edits it
by hand.

Two things are identical in every language, because they are identifiers and not text a
person reads: the marker `<!-- codificador-sesiones -->` on line 1 (a session has to find the
folder before it knows its language) and the keys of `{state}` and the role keys of the
`{matrix}` columns (declared in `{output-format}`), which only the skills read.

## The dictionary

| Key | es | What it is |
|---|---|---|
| `memory` | `memoria.md` | loose agreements, gaps and pending items, one dated line each |
| `team` | `_config/equipo.md` | people, roles, working language, Drive permissions, Fathom account |
| `output-format` | `_config/formato-de-salida.md` | the team's format: matrix columns, how a quote and a category are written |
| `quality-criteria` | `_config/criterios-de-calidad.md` | what the team considers well coded and what not, with examples |
| `templates` | `_config/plantillas/` | the files the team uploaded as they are; never edited |
| `examples` | `_ejemplos/` | calibration: previous studies coded by hand, anonymized |
| `studies` | `estudios/` | one subfolder per study |
| `study` | `estudio.md` | the study: objectives, client hypotheses, target groups, dates |
| `codebook` | `libro-de-codigos.md` | variables and their categories, with state and history |
| `guides` | `guias/` | the moderator guides of the study (optional) |
| `sessions` | `sesiones/` | one coded file per session |
| `sessions-inbox` | `sesiones/entrada/` | transcripts dropped by hand, waiting to be coded |
| `matrix` | `matriz/matriz-codificada.csv` | one row per participant, variable and code; regenerated from the session files |
| `proposals` | `matriz/propuestas-de-categoria.md` | emergent categories proposed with evidence, waiting for a decision |
| `crosses` | `cruces/` | one file per cross of variables, with its steps and pauses |
| `outputs` | `salidas/` | run summaries and fidelity reports |
| `run-summary` | `salidas/resumen-AAAA-MM-DD.md` | what one coding run took in and produced |
| `fidelity-report` | `salidas/fidelidad-AAAA-MM-DD.md` | agent coding against the team's hand coding; relative to the example study folder, `{examples}<study>/` |
| `guide` | `como-operar-el-codificador.md` | the operating guide, at the root of the folder |
| `state` | `_estado/ultima-sesion.json` | the watermark: sessions already coded |
| `history` | `## Historial` | heading that keeps every change of the codebook, dated, with its reason |
| `summary` | `## Resumen` | section of a session file |
| `participants` | `## Participantes` | section of a session file |
| `coding` | `## Codificación` | section of a session file: one row per code |
| `uncategorized` | `## Sin categoría` | section of a session file: relevant passages that fit no category |
| `session-proposals` | `## Propuestas de categoría` | section of a session file: what this session proposed |
| `transcript` | `## Transcripción` | last section of a session file: the original transcript, whole |
| `pause` | `## Pausa: esperando tu revisión` | heading that closes each step of a cross |
| `decision-at-pause` | `Lo que decidiste:` | line under a pause, filled with the researcher's answer |
| `unidentified` | `participante no identificado` | participant label when the transcript does not attribute a turn |
| `doubtful-quote` | `cita dudosa` | note on a quote whose transcript is unclear |
| `fixed` | `fija` | category state: defined by the study design |
| `emergent-proposed` | `emergente propuesta` | category state: proposed by the agent, not in use |
| `emergent-accepted` | `emergente aceptada` | category state: accepted by a researcher, in use |
| `retired` | `retirada` | category state: out of use, kept with date and reason |
| `coded` | `codificada` | row state: coded against an active category |
| `to-recode` | `por recodificar` | row state: its category changed or was retired after coding |
| `proposal-pending` | `pendiente` | proposal state |
| `proposal-accepted` | `aceptada` | proposal state |
| `proposal-rejected` | `rechazada` | proposal state |
| `role-lead` | `líder de investigación` | role: changes anything, decides the codebook, owns the study |
| `role-researcher` | `persona investigadora` | role: codes, crosses, accepts or rejects proposals, edits the codebook |
| `role-viewer` | `consulta` | role: asks; a change it requests waits for the lead |
| `gap` | `Hueco:` | prefix of a memory line the installation inventory writes |
