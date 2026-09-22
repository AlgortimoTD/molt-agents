# Decision log

Append only. One line per decision, the newest at the end. No existing line is rewritten: if
a decision is reverted or corrected, a new line says so, and the playbook goes back with its
History. The day someone asks "why did this change?", the answer has to be here.

**States:**

- `applied`: it changed a playbook, and the previous text stayed in its History.
- `confirmed`: someone said a written section still holds; no text changed.
- `pending confirmation`: inferred from the conversation, nobody said it firmly. **It touched
  no playbook** until someone confirms it.
- `proposed`: it touches `_config/values-and-negotiables.md`, the brain owner did not ask for
  it, and it waits for their approval.
- `open`: an owned action that has not been executed yet.
- `reverted`: undone by a later line; the playbook went back to its previous text.

It starts empty; the first ingestion adds the first line at the end of the table.

"Requested by" is the person who asked for the change in the chat, with their role, or
"meeting" when it came from a transcript.

| Date | Decision | Reason | Meeting and minute | Playbook | Requested by | State |
|---|---|---|---|---|---|---|
