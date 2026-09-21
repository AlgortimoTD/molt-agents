# brand-voice-style-guide CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the structure of the produced `voz.md`.
- **MINOR (x.Y.0):** a new section, axis or rule, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.1.0 | 2026-09-18 | *(this commit)* | First real skill behind this slug. The registry carried a demo fixture at 1.0.0 (seed_fixture, no package, metadata instead of a skill) that resolved as "registry" for a generated agent and would have shipped a customer an empty capability. This version reverse-engineers a company's voice from published copy and writes voz.md: tone axes each carrying a real quoted sentence, do and do-not pairs, banned phrases, vocabulary, and at least one before/after rewrite with its reasoning. It names its sources and its gaps with the date read, takes the output language from the brain folder rather than from the site, and treats a company with two languages in two registers as two sets of axis positions instead of one average. Published as 1.1.0 because the registry already holds 1.0.0: a same-version push with different content is rejected, and reusing the number would silently redefine it. |
