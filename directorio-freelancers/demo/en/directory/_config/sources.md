# Sources and routine

<!-- FICTIONAL DOCUMENT: invented production company for the directorio-freelancers plugin demo. No person, company or client is real. -->

<!-- Current since 2026-09-15 (origin: installation interview) -->

## Language

Folder language: **English** (fixed at installation; it does not change). Messages to each
freelancer go out in the language on their card.

## The weekly sweep

| What | Value |
|---|---|
| Account it runs in | Claude account of Lucía Arredondo (production coordinator) |
| Day and time | Monday 8:00, zone America/Chicago |
| Where it runs | in the cloud, with no computer switched on |
| What it touches | reads the cards and `_config/certifications.md`; writes `outputs/expiries-YYYY-MM-DD.md`, regenerates `outputs/directory.md` and advances `_state/last-sweep.json` |
| What it does not touch | no card, no request; it sends nothing |

Literal prompt of the scheduled task (never paraphrased):

> Run the directory sweep: check the certifications on every card, write the expiry report
> in outputs/, regenerate the index and advance the watermark.

## The calendar

| What | Value |
|---|---|
| Calendar read | "North Beacon Shoots" (shared calendar of Lucía's account) |
| For what | date, time and duration of the shoot; clashes with what is already scheduled |
| Writing | none. A person sends the invite with the text the request leaves |

## Drive permissions per role

| Role | Permission on the folder |
|---|---|
| production coordinator | editor |
| approver | editor |
| viewer | reader |
| routine account | editor |

Who can change this folder is decided by these permissions, not by the agent.

## History

No entries. This file is born on 2026-09-15 with the installation.
