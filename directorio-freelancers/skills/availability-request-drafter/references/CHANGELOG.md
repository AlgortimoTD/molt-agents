# availability-request-drafter CHANGELOG

Version metadata is maintained by `skills-sync` (`version:bump` re-stamps the `SKILL.md`
description + `## Version` heading and inserts the row below).

Semver:
- **MAJOR (X.0.0):** breaking change to the request file contract (sections, states, the
  draft marker) or to what the skill writes on a card.
- **MINOR (x.Y.0):** a new moment, rule, mode or check, no contract break.
- **PATCH (x.y.Z):** typo, link, cosmetic copy.

## History

| Version | Date | Commits | What changed |
|---------|------|---------|--------------|
| 1.0.0 | 2026-10-05 | *(this commit)* | Initial version. Opens a request from a shoot described in the chat: picks the job type from the directory's assignment rules, builds the candidate set (principals plus anyone whose card names the job), keeps only active cards whose required certification expires after the date of the shoot (undated never valid) and whose limits do not clash, orders by the team's priority, writes the request file with shortlist, exclusions with reasons, one draft message per person in their channel and language opening with the draft marker, and an empty answers table; reads Google Calendar when available and goes on when it is not. Logs answers as rows with time and author, marks who got it, drafts the invite text, proposes the next person when the wait window expires, and closes the shoot with a closure table; every answer and delivery becomes a dated fact on the person's card. Never sends, books or pays; never writes outside the folder. |
