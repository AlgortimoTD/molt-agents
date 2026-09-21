# Sources: what enters the brain, who approves what and how the routine runs

## Meetings that enter

- **Yes:** the internal meetings of the Fathom team <team name in Fathom>. In particular
  <the main recurring meeting, day and time>, which is the main source of decisions.
- **No:** meetings with clients, unless <who approves values> marks one "for the brain".
- Owner of the Fathom team: **<Name>**. The routine runs in **<Name>**'s account, reading the
  recordings shared with the team. Without Fathom, transcripts are dropped in
  `reuniones/entrada/` and do the same job.

## Time zone

<IANA zone, for example America/New_York>. Dates in the decision log and the file names under
`reuniones/` and `salidas/` use <Organization>'s local time, not UTC.

## Language

<Language> for playbooks, decision log, cases and answers. See `CLAUDE.md`. <If clients speak
another language: drafts for clients go in that language.>

## Who approves what

| What | Who | Note |
|---|---|---|
| Changes to `_config/valores-y-negociables.md` | **<Name>** | The routine proposes them and waits. That person also edits the file directly |
| Executing an approved change | **<Name>** | |
| Changes to `playbooks/` that come from an explicit decision | The routine applies them alone | The trail stays in the log and in the playbook's `## Historial` |
| Marking a client meeting "for the brain" | **<Name>** | |
| Adding a case to `casos/` | Anyone on the team, through the chat | |

## The daily ingestion routine

It is the only piece of the system that consults an external service, and the only thing it
does with it is fetch transcripts. It writes only inside this folder.

- **Account:** **<Name>**'s Claude account. One account, so there is no double ingestion.
- **Where:** in the cloud. It does not depend on a computer being on.
- **When:** <days>, <time> <zone> time. <Margin after the main meeting.>

The literal prompt of the scheduled task. It is not paraphrased when configuring it:

> Run the brain ingestion: read the watermark, ask Fathom for the new internal meetings,
> process each transcript with the playbook updater, update the decision log and the
> playbooks in the Drive folder, leave the summary in salidas/.

Every run leaves a file `salidas/ingesta-YYYY-MM-DD.md`. If it is missing, either there was
nothing to ingest or the routine did not run: see "What to do if the routine did not run" in
`salidas/how-to-operate-the-brain.md`.

## What NEVER enters

- Direct messaging with clients (WhatsApp, Messenger or others). The brain connects to none.
- Anything that means writing outside this folder.
