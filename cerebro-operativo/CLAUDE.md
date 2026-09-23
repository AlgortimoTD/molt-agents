# Cerebro operativo · operating brain for an organization

Agent that keeps **how an organization does things, why, and what happened the previous times**, in a folder on Google Drive that the team can open, read and correct. It answers "how do we handle this" with the organization's values, negotiables and documented cases; converts every recorded meeting into playbook updates and a decision log, without anyone transcribing; and writes with the organization's voice. It is a folder with memory, not a chat with memory: if something is not written there, the agent says so instead of inventing it.

**Agent / context separation (the golden rule):** the **agent** (these skills, the templates, the routine prompt) is agnostic and replicable: no names, roles held by a person, phones, time zones, meeting schedules or rules of any organization embedded. Everything personal lives in the **context files** of the organization's own folder (`CLAUDE.md`, `_config/*`, the memory file). The `cerebro-audit` skill polices this separation on every run.

## Bootstrap contract (how a session finds the organization's folder)

Every skill does this before working, in order:

1. The working folder has a `CLAUDE.md` whose first line is `<!-- cerebro-operativo -->`: that is the brain. Cowork and Claude Code with the project open.
2. Otherwise, read the platform memory entry `cerebro-operativo: <folder name or Drive path>`. Mobile and claude.ai through the Drive connector.
3. Otherwise, ask once, in the person's language ("¿cómo se llama la carpeta de tu cerebro en Drive?" / "what is your brain's folder called in Drive?"), and save it to memory.

Then it reads the vocabulary block at the end of that `CLAUDE.md` and resolves every name from it (see Language).

`cerebro-setup` writes the marker as the first line of the organization's `CLAUDE.md`; it is also how Phase 0 recognizes an existing brain instead of creating a second one.

## How an instance is organized (the organization's folder)

Shown by vocabulary key; the literal name of each depends on the brain's language (see [templates/vocabulary.md](templates/vocabulary.md)).

```
<the organization's brain>/
  CLAUDE.md            orchestrator from templates/<lang>/CLAUDE.root.template.md; marker on line 1,
                       vocabulary block at the end
  {memory}             loose agreements, gaps and things to remember, one dated line each
  {company}            who they are, fronts, team, key clients
  {values}             values, negotiables, non-negotiables, when a client is let go
  {voice}              the organization's voice guide (output of brand-voice-style-guide)
  {sources}            which meetings enter, time zone, working language, roles, Drive permissions,
                       routine account and time
  {playbooks}          one file per process, each with its {history}
  {log}                append-only: date, decision, reason, meeting and minute, playbook, requested by, state
  {cases}              past cases: what happened, what was done, what was learned, which value applied
  {documents}          documents the organization already had; the originals are never edited
  {meetings}           ingested transcripts with their summary and extracted decisions
  {meetings-inbox}     where a transcript is dropped by hand when there is no Fathom
  {outputs}            {ingestion-report} per routine run, {audit-report} per audit, the {guide}
  {state}              watermark: id and date of the last processed transcript
```

Context hierarchy: the root `CLAUDE.md` is the only source of the hard rules, the file map and the vocabulary. `_config/` holds what is specific to the organization. Skills read both; general rules are never duplicated into `_config/`.

## Use-case map

| The user says / happens | What runs |
|---|---|
| "quiero instalarlo" / new organization | `cerebro-setup`: language first, Drive folder, the documents they already have, the interview (people and roles), plugin check, daily routine, kickoff meeting, gap inventory and Drive permissions |
| "puebla el cerebro con la empresa de ejemplo" / "seed the demo organization" / learning or demoing | `cerebro-setup` (demo mode): copies the fictional organization from [demo/](demo/README.md), in the brain's language (`demo/es/cerebro/` as `Cerebro (demo)`, `demo/en/brain/` as `Brain (demo)`), next to the real folder, never inside it |
| A recorded meeting is published, or "procesa este transcript" / a file lands in `{meetings-inbox}` | `transcript-to-playbook-updater`: meeting file, decision log lines, playbook sections rewritten with history, ingest summary; the watermark advances |
| "¿cómo manejamos esto?" / an escalation described in the chat | `escalation-playbook-responder`: values that apply, negotiable and non-negotiable, closest documented case, source of every claim; drafts only on request and marked for review |
| "¿qué decidimos sobre X?" | the decision log and the playbook histories, answered with date and source meeting |
| "escribe esto con nuestra voz" / first install / the site changed | `brand-voice-style-guide`: generates or regenerates `{voice}`; drafts follow it |
| Weekly (scheduled) or "organiza la carpeta" | `cerebro-audit`: vocabulary and language, roles, archive order, unprocessed documents and transcripts, watermark and log coherence, stale pending items and installation gaps, agent / context separation |

## Rules the whole agent obeys (defined in the root template, enforced everywhere)

1. **The agent is the one writer of `{playbooks}` and `{log}`.** People ask for changes in the chat and the agent writes them with their trail. One writer avoids Drive sync conflicts and keeps the log in step with the playbooks. The brain owner may also edit any file by hand and tells the agent, which archives the previous version and logs it.
2. **Nothing is deleted.** When a playbook section changes, the previous text moves to its `{history}` with the date. It is what lets a bad extraction be undone.
3. **Only explicit decisions enter.** What someone said firmly ("de ahora en adelante", "from now on", "quedamos en", "we agreed") is written; the rest stays `{to-confirm}` and touches no playbook.
4. **Roles come from the installation, never from the agent.** Three generic roles (brain owner, editor, viewer) filled by the interview in the roles table of `{sources}`. The brain owner changes anything, values included, with nobody's approval; a change to values from anyone else, or from the routine, waits for the owner. No skill or template names a person; the rules name the role. The agent cannot tell who is writing to it, so the folder's Drive permissions are the real control, and the installation hands over the list that matches the roles.
5. **The agent never writes outward.** Its only writes are files in the folder. No emails, no posts, no replies to clients. A requested message is a draft opening with `{draft-marker}` that a person sends.
6. **Every claim carries its source**, file and date. What is not written is declared and offered for recording.
7. **The agent does not record meetings.** Fathom or a pasted transcript feeds it.

## Language

The agent works in Spanish and in English. The skills are written in English; **everything they write into a brain is in the brain's language, with no exception a person can see**. `cerebro-setup` asks the language as its first, mandatory question, before creating anything, says the answer is final, picks the matching template set (`templates/es/` or `templates/en/`) and writes the choice in the brain's `CLAUDE.md` and `{sources}`. The language does not change after installation.

**Names by key.** Folder and file names, headings, markers, decision states and role names all exist in both languages in [templates/vocabulary.md](templates/vocabulary.md). The brain's `CLAUDE.md` ends with a vocabulary block (an HTML comment, one `key: name` line each) in its language, and every skill resolves every name from that block by key. That is why a Spanish brain has `decisiones/bitacora.md` and `## Historial`, an English one has `decisions/log.md` and `## History`, and no skill text changes between them. The only language-neutral pieces are identifiers nobody reads as text: the marker `<!-- cerebro-operativo -->` on line 1 and the JSON keys of `{state}`.

## Dependencies

None on the machine. Google Drive (folder synced with Drive for desktop, plus the Drive connector for cloud sessions), Fathom (optional, read-only) and one scheduled task in one account.
