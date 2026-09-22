# Sources: what enters the brain, who holds which role and how the routine runs

## Meetings that enter

- **Yes:** the internal meetings of the Fathom team <team name in Fathom>. In particular
  <the main recurring meeting, day and time>, which is the main source of decisions.
- **No:** meetings with clients, unless the brain owner marks one "for the brain".
- Owner of the Fathom team: **<Name>**. The routine runs in **<Name>**'s account, reading the
  recordings shared with the team. Without Fathom, transcripts are dropped in
  `meetings/inbox/` and do the same job.

## Time zone

<IANA zone, for example America/New_York>. Dates in the decision log and the file names under
`meetings/` and `outputs/` use <Organization>'s local time, not UTC.

## Language

English, fixed at installation, for everything written in this folder: folder and file
names, playbooks, decision log, cases and answers. See `CLAUDE.md`. <If clients speak another
language: drafts for clients go in that language.>

## Roles

They come from the installation interview and are changed by asking the brain in the chat
(the brain owner changes them). There is exactly one brain owner; editor and viewer may stay
empty.

| Person | Role | Since | Source |
|---|---|---|---|
| **<Name>** | brain owner | <YYYY-MM-DD> | <interview YYYY-MM-DD> |
| <Name> | <editor or viewer> | <YYYY-MM-DD> | <interview YYYY-MM-DD> |

## Who approves what

| What | Who | Note |
|---|---|---|
| Any change, in any file | The brain owner, with nobody's approval | Through the chat, or by hand telling the brain so it leaves the trail |
| Changes to `playbooks/` and `cases/` asked in the chat | Editor or owner | They stay in the log with who asked for them |
| Changes to `_config/values-and-negotiables.md` not asked by the owner | The owner approves them | The routine, an editor or a viewer proposes them and they wait |
| Changes to `playbooks/` that come from an explicit decision in a meeting | The routine applies them alone | The trail stays in the log and in the playbook's `## History` |
| The processes being written and up to date | The brain owner | Reviews what the brain proposes and calls the kickoff meeting when a process changes at its core |
| Executing an approved change | **<Name>** | |
| Marking a client meeting "for the brain" | The brain owner | |

## Folder permissions in Drive

The brain does not know who is writing to it; what protects the folder is its permissions.
They must match the roles:

- Brain owner and editors: **editor** on the Drive folder.
- Viewers: **viewer** on the Drive folder.
- The account the routine runs in: **editor**.

## The daily ingestion routine

It is the only piece of the system that consults an external service, and the only thing it
does with it is fetch transcripts. It writes only inside this folder.

- **Account:** **<Name>**'s Claude account. One account, so there is no double ingestion.
- **Where:** in the cloud. It does not depend on a computer being on.
- **When:** <days>, <time> <zone> time. <Margin after the main meeting.>

The literal prompt of the scheduled task. It is not paraphrased when configuring it:

> Run the brain ingestion: read the watermark, ask Fathom for the new internal meetings,
> process each transcript with the playbook updater, update the decision log and the
> playbooks in the Drive folder, leave the summary in outputs/.

Every run leaves a file `outputs/ingestion-YYYY-MM-DD.md`. If it is missing, either there was
nothing to ingest or the routine did not run: see "What to do if the routine did not run" in
`outputs/how-to-operate-the-brain.md`.

## What NEVER enters

- Direct messaging with clients (WhatsApp, Messenger or others). The brain connects to none.
- Anything that means writing outside this folder.
