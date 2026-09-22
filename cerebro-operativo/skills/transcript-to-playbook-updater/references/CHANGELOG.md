# transcript-to-playbook-updater CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the folder contract this skill writes into, or to what
  it is allowed to write without approval.
- **MINOR (x.Y.0):** a new rule, marker or output section, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.1.1 | 2026-09-22 | *(this commit)* | Fixes from a simulated install: new confirmed state for a kickoff confirmation that changes no text; a no-longer with a replacement is a change; the original transcript is kept whole in the meeting file before the inbox file is removed; tentative talk about values is discarded, and a value change from a meeting is a proposal even when the owner says it; last_processed_at is the newest meeting's time; the playbook state line moves from seed to current once reviewed. |
| 1.1.0 | 2026-09-22 | *(this commit)* | Resolves every folder, file, heading, marker and state from the brain's vocabulary block, so an English brain gets English names end to end, and stops instead of guessing when the block is missing. The decision log gains the requested-by column (meeting, for a transcript). Value changes wait for the brain owner named in the roles table. Handles a kickoff meeting that walks the playbooks one by one. |
| 1.0.0 | 2026-09-18 | *(this commit)* | Initial version. Reads one meeting transcript against a brain folder and writes the meeting file, the decision-log lines and the playbook sections those decisions changed, keeping the replaced text under Historial. Extraction is filtered by explicit commitment markers in Spanish and English; an inference lands in the log as "por confirmar" and touches no playbook; a change to values is proposed in the run report and never applied without the named approver. Nothing is deleted, the working language comes from the folder's CLAUDE.md, writes never leave the folder, and the watermark advances last so a failed run retries and a second run over the same transcript changes nothing. |
