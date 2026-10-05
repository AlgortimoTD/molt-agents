# directorio-freelancers-audit CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** a check that changes what the audit is allowed to write, or a change to
  the report's path or structure.
- **MINOR (x.Y.0):** a new check or a new intervention rule, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.0.0 | 2026-10-05 | *(this commit)* | Initial version. Weekly audit of the freelancer directory folder with fourteen checks (vocabulary and language, roles with at least one coordinator and exactly one approver, loose files, broken card data blocks, hand edits reported and never reverted, certifications without date or document cross-checked with the latest sweep report, certification names outside the catalog, requests past their shoot date without closure, index against the cards, watermark against the reports, stale gaps, placeholders, sync duplicates, memory lines to promote) and two checks on the agent (agent / context separation over the organization's and the freelancers' names, phones and emails, reported for the engine's maintainers; one copy of each skill). Fixes the mechanical, never deletes, never rewrites a card's current text, the watermark or the index, never closes a request or runs a sweep. Dated report in the directory's language plus one memory line per question for the team. |
