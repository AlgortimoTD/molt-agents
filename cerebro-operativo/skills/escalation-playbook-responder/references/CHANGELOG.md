# escalation-playbook-responder CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the answer contract (the order of authority, the
  citation requirement, or the no-send rule).
- **MINOR (x.Y.0):** a new section, source or rule, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.1.0 | 2026-09-22 | *(this commit)* | Resolves every name from the brain's vocabulary block and writes the answer headings in the brain's language. The unanswered-question memory line and the draft marker come from the vocabulary. The values file changes only when the brain owner named in the roles table asks for it or approves it. Drafts use the language the brain sets for clients. |
| 1.0.0 | 2026-09-18 | *(this commit)* | Initial version. Answers a "how do we handle this" question or a client escalation from a brain folder, reading values and negotiables, the decision log, the playbooks with their Historial, the past cases and the company profile, in that order of authority. Every claim carries its file and date; where the folder is silent the answer says so, proposes the rule in one sentence and logs the gap as one dated line in memory.md. A decision newer than a playbook wins and the contradiction is stated out loud. A requested draft uses the voice from _config/voz.md, keeps non-negotiables intact and opens with a review marker; the skill sends nothing. |
