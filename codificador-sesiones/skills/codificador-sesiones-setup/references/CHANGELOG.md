# codificador-sesiones-setup CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the research folder contract this skill reads or writes,
  or to what it may change without a person asking.
- **MINOR (x.Y.0):** a new rule, mode or output section, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.1.0 | 2026-09-28 | minor | Installation trial: new demo mode that runs Phases 2 to 7 on sample material in real formats (xlsx, docx, txt) shipped in the plugin, with a previous study deliberately not anonymized so the anonymization check is shown, and one session held out for the fidelity test. Phase 3 now names the formats a team hands over and keeps originals while writing the folder's CSV and Markdown from them. |
| 1.0.0 | 2026-09-28 | initial | Initial version. Phase 0 recognizes an installed folder by its marker; creates the folder in Drive and opens it as the project; interviews people, roles (at least one lead) and the Fathom rule; stores the team's formats untouched and derives the output format from them with each rule's origin; checks a previous study is anonymized before storing it as the calibration example, reconstructing its codebook from the hand matrix when needed; interviews the quality criteria; loads the current study and its codebook from the team's spreadsheet; writes the root CLAUDE.md with marker and vocabulary block; checks Fathom or explains the inbox; codes a first session as heartbeat and offers the fidelity test; closes with an inventory, gaps in memory and the Drive permissions list. Demo mode copies a fictional study next to the real folder. Spanish in this version. |
