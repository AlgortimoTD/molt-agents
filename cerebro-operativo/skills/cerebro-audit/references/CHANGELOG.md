# cerebro-audit CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to what the audit is allowed to change in the folder or
  in the agent's files.
- **MINOR (x.Y.0):** a new check, threshold or report section, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.0.0 | 2026-09-21 | *(this commit)* | Initial version. Weekly audit of a brain folder and of the agent itself: loose files, transcripts waiting in reuniones/entrada/, watermark against reuniones/, decision log against playbook histories both ways, stale "por confirmar" (30 days) and "propuesta" (14 days) items, unfilled template placeholders, cases without their lesson, Drive duplicates, memory lines to promote; plus the agent / context separation check (names, phones, emails and rules of the organization found in skills or templates are moved back to _config/ and reported) and the one-copy-per-skill check. Fixes only the mechanical, never deletes, never touches the log, the current playbook text or the watermark, and leaves a dated report in salidas/auditorias/ in the folder's language. |
