# Codificador de sesiones de investigación

Agent that codes a research team's qualitative sessions (interviews and focus groups) the way that team already codes by hand: per participant and variable, the category and the verbatim quote with its minute, in a matrix the team opens in its own spreadsheet. It proposes emergent categories with evidence instead of applying them, changes the codebook only when a person asks, and crosses variables in steps that stop for the researcher. It lives in a research folder on Google Drive that every researcher opens as a project.

**Agent / context separation (the golden rule):** the **agent** (these skills, the templates, the demo) is agnostic and replicable: no names, clients, studies, categories or rules of any team embedded. Everything specific lives in the **context files** of the team's own folder (`CLAUDE.md`, `_config/`, `_ejemplos/`, the studies). Calibration comes from the team's own hand-coded example, never from anything written in a skill.

## Bootstrap contract (how a session finds the research folder)

Every skill does this before working, in order:

1. The working folder has a `CLAUDE.md` whose first line is `<!-- codificador-sesiones -->`: that is the folder. Cowork and Claude Code with the project open.
2. Otherwise, read the platform memory entry `codificador-sesiones: <folder name or Drive path>`.
3. Otherwise, ask once ("¿cómo se llama la carpeta de investigación en tu Drive?") and save it to memory.

Then it reads the vocabulary block at the end of that `CLAUDE.md` and resolves every name from it ([templates/vocabulary.md](templates/vocabulary.md)).

## How an instance is organized (the team's folder)

Shown by vocabulary key; the Spanish names are in the vocabulary.

```
<the team's research folder>/
  CLAUDE.md            orchestrator from templates/es/CLAUDE.root.template.md; marker on line 1,
                       vocabulary block at the end
  {memory}             loose agreements, gaps and pending items
  {team}               people, roles, language, Fathom rule, Drive permissions
  {output-format}      the team's format: matrix columns with their role keys, quotes, names
  {quality-criteria}   what the team considers well coded, with examples; minimums for crosses
  {templates}          the team's own files, untouched
  {examples}<study>/   previous studies coded by hand, anonymized: calibration and fidelity test
  {studies}<study>/
    {study}            objectives, client hypotheses, target groups
    {codebook}         variables and categories with state and a dated history
    {guides}           moderator guides (optional)
    {sessions}         one coded file per session; {sessions-inbox} for pasted transcripts
    {matrix}           one row per code, regenerated from the session files
    {proposals}        emergent categories waiting for a decision
    {crosses}          one file per cross, with its steps and pauses
    {outputs}          run summaries
    {state}            the watermark
```

## Use-case map

| The user says / happens | What runs |
|---|---|
| "instala el codificador" / "quiero instalarlo" | `codificador-sesiones-setup` |
| "puebla el codificador con el estudio de ejemplo" | `codificador-sesiones-setup` (demo mode) |
| "codifica la sesión de hoy del grupo 3" / a transcript lands in `{sessions-inbox}` | `qualitative-session-coder` (code a session) |
| "acepta recreación como categoría" / "retira la categoría X" / "renombra X" | `qualitative-session-coder` (change the codebook) |
| "¿qué dijo la gente del grupo 2 sobre X?" | `qualitative-session-coder` (answer from the coded sessions) |
| "corre la prueba de fidelidad" | `qualitative-session-coder` (fidelity test) |
| "cruza deporte con alimentación por grupo" | `cross-variable-analyzer` |

## Rules the whole agent obeys

1. **Every code carries its quote, participant and minute.** No quote, no code.
2. **Only the codebook's active categories code a row.** A new idea is a proposal with evidence from two or more participants; it enters the codebook when a researcher accepts it.
3. **The codebook changes only when a person asks**, and every change goes to its history with date, reason and who asked. Nothing is deleted: a retired category keeps its state and its rows become "por recodificar".
4. **The matrix is regenerated from the session files.** Each session is its own file, so several researchers code at the same time without overwriting each other.
5. **Crosses go in steps and stop for the researcher.** Counts are of participants with their n; relations carry three quotes; nothing is stated as a cause.
6. **The agent neither writes the report nor decides which findings matter**, and never moderates. Those are the team's.
7. **Participants are codes, never names**, outside the transcript section of a session file.
8. **The agent writes only inside the folder.** No email, no message, no document for the client.

## Language

Version 0.1 works in Spanish (`templates/es/`, `demo/es/`, `docs/es/`). The skills are written in English and resolve every name by key, so adding a language is a new column in the vocabulary plus a template set.

## Dependencies

None on the machine beyond Google Drive for desktop (the folder opened as a project) and the plugin. Connectors: Google Drive, Fathom (optional, read only).
