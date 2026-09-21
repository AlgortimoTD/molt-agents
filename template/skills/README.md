# skills/

This folder holds **stamped copies** of skills published in the Molt skill registry, produced by `scripts/release.sh <agent>` from `catalogs/global/<slug>/skill/` in the platform monorepo. Do not create or edit a `SKILL.md` here.

Every agent needs at least:

- `<agent>-setup`: zero-command onboarding with Phase 0 diagnosis, the bootstrap contract, a guided interview that fills `templates/`, the scheduled routine, a first heartbeat and a demo mode (METHODOLOGY.md, sections 5 and 6).
- `<agent>-audit`: the recurring audit of the customer's archive and of the agent itself (METHODOLOGY.md, section 10).
- One skill per activity the agent sells.

Author them with `skill-creator` in the monorepo, publish them, then run the release script.
