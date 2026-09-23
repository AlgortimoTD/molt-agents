> **FICTIONAL DOCUMENT.** Configuration of an invented agency, written to demonstrate the agent.

# Sources: what enters the brain, who holds which role and how the routine runs

## Meetings that enter

- **They enter:** the internal meetings of the Fathom team "Faro". In particular the weekly
  meeting on Mondays at 9 in the morning, which is the main source of decisions.
- **They do not enter:** meetings with clients, unless Marina marks one "for the brain".
- Owner of the Fathom team: **Tomás**. The routine runs in **Marina**'s account, reading the
  recordings shared with the team. Without Fathom, transcripts are dropped in
  `meetings/inbox/`.

## Time zone

America/Bogota. Log dates and file names use local time.

## Language

English, fixed at installation, for everything written in this folder, including drafts for
clients.

## Roles

| Person | Role | Since | Source |
|---|---|---|---|
| **Marina** | brain owner | 2026-09-01 | interview 2026-09-01 |
| Tomás | editor | 2026-09-01 | interview 2026-09-01 |
| Julia | editor | 2026-09-01 | interview 2026-09-01 |

## Who approves what

| What | Who | Note |
|---|---|---|
| Any change, in any file | Marina, with nobody's approval | Through the chat, or by hand telling the brain so it leaves the trail |
| Changes to `playbooks/` and `cases/` asked for in the chat | Tomás, Julia or Marina | They stay in the log with who asked for them |
| Changes to `_config/values-and-negotiables.md` not asked for by Marina | Marina approves them | The routine, Tomás or Julia propose them and they wait |
| Changes to `playbooks/` that come from an explicit decision in a meeting | The routine applies them on its own | The trail stays in the log and in the History |
| That the processes are written and up to date | Marina | Reviews what the brain proposes and calls the kickoff meeting when a process changes at its core |
| Executing an approved change | **Tomás** | |
| Marking a client meeting "for the brain" | Marina | |

## Permissions on the Drive folder

- Marina, Tomás and Julia: **editor**.
- The routine's account (Marina's): **editor**.

## The daily ingestion routine

- **Account:** **Marina**'s Claude account.
- **Where:** in the cloud. It does not depend on a computer being on.
- **When:** Monday to Friday, 13:00 Bogotá time. The weekly meeting is at 9, so by 1 the
  transcript is already published with margin.

The literal prompt of the scheduled task:

> Run the brain's ingestion: read the watermark, ask Fathom for the new internal meetings,
> process each transcript with the playbook updater, update the log and the playbooks in the
> Drive folder, leave the summary in outputs/.

## What never enters

- Direct messaging with clients. The brain connects to none.
- Anything that implies writing outside this folder.
