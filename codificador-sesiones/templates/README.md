# templates/

What `codificador-sesiones-setup` fills to create a team's research folder. Everything here lands in
the team's folder. Version 0.1 ships one set, `es/`. No template carries data of any team: every
placeholder is `<like this>` and the installation fills it from the interview and from the team's
own files. The name of every folder, file, heading and state, by key, is in
[vocabulary.md](vocabulary.md).

| Template | Becomes (vocabulary key) | Filled by |
|---|---|---|
| `es/CLAUDE.root.template.md` | `CLAUDE.md` of the folder (marker on line 1, vocabulary block at the end) | the interview: team and roles |
| `es/config/equipo.template.md` | `team` | the interview: people, roles, Fathom rule, permissions |
| `es/config/formato-de-salida.template.md` | `output-format` | the team's own spreadsheet in `templates`, then the interview |
| `es/config/criterios-de-calidad.template.md` | `quality-criteria` | the interview with the example study open |
| `es/memoria.template.md` | `memory` | as is, plus the gap inventory |
| `es/ejemplos-README.template.md` | `README.md` inside `examples` | what the team uploaded and what was anonymized |
| `es/estudio.template.md` | `study` | the interview: objectives, hypotheses, groups |
| `es/libro-de-codigos.template.md` | `codebook` | the team's codebook spreadsheet |
| `es/matriz-codificada.template.csv` | `matrix` (header only) | the columns of `output-format` |
| `es/propuestas-de-categoria.template.md` | `proposals` | as is |
| `es/sesion.template.md` | one file per session under `sessions` | `qualitative-session-coder` |
| `es/cruce.template.md` | one file per cross under `crosses` | `cross-variable-analyzer` |
| `es/sesiones-entrada-README.template.md` | `README.md` inside `sessions-inbox` | as is |
| `es/ultima-sesion.template.json` | `state` | as is |

The setup skill also copies `docs/es/como-operar-el-codificador.md` to the root of the folder so it
travels with it.
