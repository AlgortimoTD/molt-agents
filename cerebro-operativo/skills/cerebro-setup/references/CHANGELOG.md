# cerebro-setup CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the folder contract this skill creates (file map,
  marker, canonical tokens) or to the interview's outputs.
- **MINOR (x.Y.0):** a new phase, block, language or check, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.2.0 | 2026-09-23 | *(this commit)* | Demo mode seeds the fictional organization in the language of the brain: a full English copy (demo/en/brain, copied as Brain (demo), with the English vocabulary: decisions/log.md, meetings/inbox/, ## History, pending confirmation) next to the Spanish one (demo/es/cerebro, Cerebro (demo)). Without a brain the demo asks the language without fixing a future brain; Phase 0 ignores both demo folder names. Replaces the old warning that the demo only existed in Spanish. |
| 1.1.1 | 2026-09-22 | *(this commit)* | Fixes from a simulated install in Spanish and English: the clients' language is always asked right after the working language and not again in the interview; the interview asks who executes approved changes and the Fathom team's name; a process named but not described becomes a gap, not an empty playbook; the kickoff script has its own vocabulary name. |
| 1.1.0 | 2026-09-22 | *(this commit)* | Language asked first as a mandatory, final question, and every file, folder, heading and state written in it through the vocabulary block of the brain's CLAUDE.md (no more Spanish canonical tokens in an English brain). New Phase 2a turns the documents the organization already has into the first playbooks, cited and never modernized. The interview fills three generic roles (brain owner, editor, viewer) instead of naming people in rules. Phase 5 becomes the kickoff meeting that corrects the documents, and new Phase 6 closes with the inventory of what the brain knows and what it does not, plus the Drive permissions that match the roles. |
| 1.0.0 | 2026-09-21 | *(this commit)* | Initial version. Zero-command onboarding of the operating brain: detects the language of the first message and confirms it explicitly before creating anything, then Drive folder, guided interview that fills the plugin templates of the chosen language (es or en), voice guide, plugin check, daily routine with the literal prompt, and a first transcript processed end to end. Idempotent Phase 0 recognizes an existing brain by the marker on line 1 of its CLAUDE.md and never creates a second one. Demo mode seeds the fictional organization next to the real brain and never saves it to memory, so a later real install is not mistaken for a second brain. Nothing is installed on the machine. Canonical tokens (file names, Historial, Vigente desde, decision states) never translate. |
