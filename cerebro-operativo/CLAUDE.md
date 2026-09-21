# Cerebro operativo · operating brain for an organization

Agent that keeps **how an organization does things, why, and what happened the previous times**, in a folder on Google Drive that the team can open, read and correct. It answers "how do we handle this" with the organization's values, negotiables and documented cases; converts every recorded meeting into playbook updates and a decision log, without anyone transcribing; and writes with the organization's voice. It is a folder with memory, not a chat with memory: if something is not written there, the agent says so instead of inventing it.

**Agent / context separation (the golden rule):** the **agent** (these skills, the templates, the routine prompt) is agnostic and replicable: no names, roles, phones, time zones, meeting schedules or rules of any organization embedded. Everything personal lives in the **context files** of the organization's own folder (`CLAUDE.md`, `_config/*`, `memory.md`). The `cerebro-audit` skill polices this separation on every run.

## Bootstrap contract (how a session finds the organization's folder)

Every skill does this before working, in order:

1. The working folder has a `CLAUDE.md` whose first line is `<!-- cerebro-operativo -->`: that is the brain. Cowork and Claude Code with the project open.
2. Otherwise, read the platform memory entry `cerebro-operativo: <folder name or Drive path>`. Mobile and claude.ai through the Drive connector.
3. Otherwise, ask once ("¿cómo se llama la carpeta de tu cerebro en Drive?") and save it to memory.

`cerebro-setup` writes the marker as the first line of the organization's `CLAUDE.md`; it is also how Phase 0 recognizes an existing brain instead of creating a second one.

## How an instance is organized (the organization's folder)

```
<Cerebro de la organización>/
  CLAUDE.md                     orchestrator from templates/CLAUDE.root.template.md; marker on line 1
  memory.md                     loose agreements and things to remember, one dated line each
  _config/
    empresa.md                  who they are, fronts, team by role, key clients
    valores-y-negociables.md    values, negotiables, non-negotiables, when a client is let go
    voz.md                      the organization's voice guide (output of brand-voice-style-guide)
    fuentes.md                  which meetings enter, time zone, working language, who approves what,
                                routine account and time
  playbooks/<proceso>.md        one per process, each with its "## Historial"
  decisiones/bitacora.md        append-only: date, decision, reason, source meeting and minute, playbook touched, state
  casos/<caso>.md               past cases: what happened, what was done, what was learned, which value applied
  reuniones/AAAA-MM-DD-<titulo>.md   ingested transcripts with their summary and extracted decisions
  reuniones/entrada/            where a transcript is dropped by hand when there is no Fathom
  salidas/ingesta-AAAA-MM-DD.md summary of each routine run; salidas/auditorias/ for the audit reports
  _estado/ultima-ingesta.json   watermark: id and date of the last processed transcript
```

Context hierarchy: the root `CLAUDE.md` is the only source of the hard rules and the file map. `_config/` holds what is specific to the organization. Skills read both; general rules are never duplicated into `_config/`.

## Use-case map

| The user says / happens | What runs |
|---|---|
| "quiero instalarlo" / new organization | `cerebro-setup`: Drive folder, root context from the templates through the interview, plugin check, daily routine, first heartbeat |
| "puebla el cerebro con la empresa de ejemplo" / learning or demoing | `cerebro-setup` (demo mode): copies the fictional organization from [demo/](demo/README.md) next to the real folder, never inside it |
| A recorded meeting is published, or "procesa este transcript" / a file lands in `reuniones/entrada/` | `transcript-to-playbook-updater`: meeting file, decision log lines, playbook sections rewritten with history, ingest summary; the watermark advances |
| "¿cómo manejamos esto?" / an escalation described in the chat | `escalation-playbook-responder`: values that apply, negotiable and non-negotiable, closest documented case, source of every claim; drafts only on request and marked for review |
| "¿qué decidimos sobre X?" | the decision log and the playbook histories, answered with date and source meeting |
| "escribe esto con nuestra voz" / first install / the site changed | `brand-voice-style-guide`: generates or regenerates `_config/voz.md`; drafts follow it |
| Weekly (scheduled) or "organiza la carpeta" | `cerebro-audit`: archive order, watermark and log coherence, stale "por confirmar", agent / context separation |

## Rules the whole agent obeys (defined in the root template, enforced everywhere)

1. **Only the routine writes `playbooks/` and `decisiones/`.** People ask for changes in the chat and the agent writes them. One writer per file avoids Drive sync conflicts and keeps the log in step with the playbooks.
2. **Nothing is deleted.** When a playbook section changes, the previous text moves to its `## Historial` with the date. It is what lets a bad extraction be undone.
3. **Only explicit decisions enter.** What someone said firmly ("de ahora en adelante", "quedamos en", "dejemos de") is written; the rest stays "por confirmar" and touches no playbook.
4. **Changes to values and negotiables wait for the approver** named in `_config/fuentes.md`. The routine proposes them in the ingest summary and waits.
5. **The agent never writes outward.** Its only writes are files in the folder. No emails, no posts, no replies to clients. A requested message is a draft marked "para revisar antes de enviar" that a person sends.
6. **Every claim carries its source**, file and date. What is not written is declared and offered for recording.
7. **The agent does not record meetings.** Fathom or a pasted transcript feeds it.

## Language

The organization fixes the working language of playbooks, log, cases and answers in its `CLAUDE.md` and `_config/fuentes.md`. Every skill reads it there. The templates default to Spanish; the setup skill produces them in the language the organization chooses.

## Dependencies

None on the machine. Google Drive (folder synced with Drive for desktop, plus the Drive connector for cloud sessions), Fathom (optional, read-only) and one scheduled task in one account.
