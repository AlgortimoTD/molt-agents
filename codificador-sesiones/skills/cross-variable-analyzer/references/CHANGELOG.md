# cross-variable-analyzer CHANGELOG

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
| 1.0.0 | 2026-09-28 | initial | Initial version. Reads the coded matrix of a research folder through the role keys of its output format, the codebook, the study's hypotheses and the team's minimums (3 participants by default), warns about to-recode rows and a stale matrix, and writes one cross file in three steps, each closed by a pause that waits for the researcher and records their decision in their words: participant counts by group with n and small samples marked, candidate relations with count, base and three quotes from three participants plus the threads under the minimum and the relations not found, and a summary tied to the study's hypotheses. Refuses to do it all at once, never states a cause, never ranks or drafts findings, never edits the codebook or the matrix. |
