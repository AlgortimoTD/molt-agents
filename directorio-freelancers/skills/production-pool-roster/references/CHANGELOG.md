# production-pool-roster CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the card contract (sections, the five data fields, the
  history format) or to the index columns.
- **MINOR (x.Y.0):** a new job, rule, language or check, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.0.0 | 2026-10-05 | *(this commit)* | Initial version. Keeps the freelancer cards of a production directory: creates or updates one card per person from a sentence or a pasted list, answers "who can do X" from the cards with card and date as source or declares that nobody is documented, and regenerates the index after every change. Card contract with a five-field data block, seven sections and a dated history; people edit and the skill re-reads before writing and never deletes. Reliability as dated, attributed facts and never a score; limits as assignment constraints with the rephrased marker when they arrive as a personal condition; undated certifications written as the undated tier plus a gap line; unknown certification names reported, not renamed; the do-not-call status only on the approver's request. Every name resolved by key from the directory's vocabulary block, so the same skill serves Spanish and English directories. |
