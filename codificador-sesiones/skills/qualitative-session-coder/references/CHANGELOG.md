# qualitative-session-coder CHANGELOG

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
| 1.0.0 | 2026-09-28 | initial | Initial version. Codes one session (Fathom connector or a transcript in the study's inbox) against the study's codebook after calibrating on the team's output format, quality criteria and a hand-coded example study: one row per code with participant code, category, verbatim quote and minute; the moderator is never coded; unattributed turns stay unidentified; unclear quotes are kept as written and flagged. Only fixed and accepted-emergent categories code a row; a new idea from two or more participants becomes a pending proposal with evidence, a single mention stays uncategorized. The codebook changes only when a person asks (accept, reject, add, rename, retire), each change dated in its history, retired categories turn their rows to-recode. The matrix CSV is regenerated from every session file so several researchers can code at once. Answers questions from the coded sessions with quotes, and runs the fidelity test against the team's hand coding with a classified list of differences. Writes only inside the folder; a second run over the same session changes nothing. |
