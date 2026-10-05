# certification-expiry-tracker CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to what the sweep reads or writes (the card table it
  parses, the report structure, the state keys, the tier precedence).
- **MINOR (x.Y.0):** a new tier, question, language or check, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.0.0 | 2026-10-05 | *(this commit)* | Initial version. Replaces the seed fixture row of the same slug in the skill registry, which had no package and no operating content. Weekly sweep of a production freelancer directory (the directorio-freelancers plugin): reads every card's certifications table, puts each certification in exactly one tier counted from the sweep day (expired, within 7, 30 or 60 days, undated, no supporting document), writes the dated expiry report, regenerates the index and advances the watermark; idempotent within a day. Answers who holds a valid certification on a given date (valid means it expires after the shoot's date; undated never counts). Records a renewal the team states, with history, and asks for the document. Never sends anything and never invents a date. |
