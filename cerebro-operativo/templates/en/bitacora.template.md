# Decision log

Append only. One line per decision, the newest at the end. No existing line is rewritten: if
a decision is reverted or corrected, a new line says so, and the playbook goes back with its
`## Historial`. The day someone asks "why did this change?", the answer has to be here.

**States** (canonical tokens, the same in every language):

- `aplicada`: it changed a playbook, and the previous text stayed in its `## Historial`.
- `por confirmar`: inferred from the conversation, nobody said it firmly. **It touched no
  playbook** until someone confirms it.
- `propuesta`: it touches `_config/valores-y-negociables.md` and waits for <who approves
  values>'s approval.
- `abierta`: an owned action that has not been executed yet.
- `revertida`: undone by a later line; the playbook went back to its previous text.

| Date | Decision | Reason | Meeting and minute | Playbook | State |
|---|---|---|---|---|---|

Empty. The first ingestion fills it.
