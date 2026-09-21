# <Agent name>

Agent that <what it does for an organization, one sentence>. It manages <the real situations it handles end to end>, not just outputs.

**Agent / context separation (the golden rule):** the **agent** (these skills, the templates, the routine) is agnostic and replicable: no names, phones, emails, contracts or customer rules embedded. Everything personal lives in the **context files** of the customer's own folder (`CLAUDE.md`, `_config/`, `memory.md`). The `<agent>-audit` skill polices this separation on every run.

## Bootstrap contract (how a session finds the customer's folder)

1. The working folder has a `CLAUDE.md` whose first line is `<!-- <agent-slug> -->`: that is the folder.
2. Otherwise, read the platform memory entry `<agent-slug>: <folder>`.
3. Otherwise, ask once ("¿cómo se llama la carpeta de <agent> en tu Drive?") and save it to memory.

## How an instance is organized (the customer's folder)

```
<Folder>/
  CLAUDE.md          orchestrator filled from templates/CLAUDE.root.template.md; first line is the marker
  memory.md          durable facts, one dated line each
  _config/           who they are, rules, sources, who approves what
  <data folders>     the customer's records; the engine only ships their format
  _estado/           execution state (watermarks); the engine ships it empty
```

## Use-case map

| The user says / happens | What runs |
|---|---|
| "quiero instalarlo" / new organization | `<agent>-setup` |
| "puebla <agent> con la empresa de ejemplo" | `<agent>-setup` (demo mode) |
| <trigger phrase> | `<skill>` |
| Weekly (scheduled) or "organiza la carpeta" | `<agent>-audit` |

## Rules the whole agent obeys

- Every claim carries its source (file and date); what is not written is said, not invented.
- Only the routine writes the record folders; people ask for changes in the chat.
- Nothing is deleted: superseded content moves to a dated history.
- The agent writes only inside the customer's folder; drafts for the outside are marked for human review.
- The working language is the one the customer fixed in `CLAUDE.md`; every skill reads it there.

## Dependencies

None on the customer's machine. Connectors and a scheduled task only.
