---
name: cerebro-audit
description: >-
  v1.0.0 · Weekly audit of an organization's operating brain (cerebro operativo) folder and of
  the agent itself. On the folder: loose files, transcripts waiting in reuniones/entrada/, a
  watermark that disagrees with reuniones/, decision-log lines without their playbook change
  and the reverse, stale "por confirmar" and "propuesta" items, unfilled placeholders, cases
  without their lesson. On the agent: any name, phone, email or rule of the organization that
  slipped into a skill or template, moved back to _config/ and reported. Fixes the mechanical,
  never deletes, and leaves a dated report in salidas/auditorias/ in the folder's language. Use
  it when someone asks to organize, review, clean or audit the brain, when the weekly routine
  runs it, or after an ingestion left items pending. Triggers: "organiza la carpeta", "revisa
  el cerebro", "corre la auditoría del cerebro", "qué está pendiente en el cerebro", "organize
  the folder", "audit the brain", "tidy up the brain". [v1.0.0]
---

# cerebro-audit

## Version 1.0.0

A brain folder drifts. Transcripts land in `reuniones/entrada/` and nobody processes them, a
decision gets logged and its playbook never changes, an inference stays "por confirmar" for
two months, a placeholder from the installation is still `<Nombre>`. None of this is anyone's
fault; it is what happens to any shared folder that several people and one routine write to.
This skill is the routine that restores order without waiting to be asked, fixes what is
mechanical, and leaves a trail of what it cannot decide alone.

It also does something the archive audit of a normal folder does not: it audits **the agent**.
The brain is a product installed by many organizations, and it stays a product only while the
skills and templates carry nothing of any single organization. Every urgent fix is a chance
for a customer's name to slip into a skill. This skill is the mechanism that reverts that, one
extraction at a time.

## Where you work

Find the brain folder the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- cerebro-operativo -->`; otherwise the platform memory entry
`cerebro-operativo: <folder>`; otherwise ask once and save it. Read the folder's `CLAUDE.md`
and `_config/fuentes.md` first: they give you the organization's name, the working language
(the report is written in it), the roles (who approves values, who executes) and the time
zone. The folder outranks this skill wherever they differ.

You are member-agnostic. You take every name from `_config/empresa.md` and every rule from
`CLAUDE.md`; nothing here assumes a particular organization.

## Scope of a run

Walk the folder in this order: `_config/`, `playbooks/`, `decisiones/bitacora.md`, `casos/`,
`reuniones/` and `reuniones/entrada/`, `salidas/`, `_estado/`, `memory.md`, and finally the
loose items at the root. In each place you compare **what the context files say against what
actually exists**.

## The checks on the folder

1. **Loose files.** Anything at the root or inside a pattern folder that is not part of the
   pattern (a PDF dropped at the root, a transcript outside `reuniones/`, a copy of a skill).
   If the destination is obvious, move it and record the move; if it is doubtful, do not
   touch it, put it in the report with a proposal.
2. **Transcripts waiting.** Files in `reuniones/entrada/` other than its README are work the
   routine has not done. Do not process them yourself (that is `transcript-to-playbook-
   updater`'s job and it runs from the watermark); list them in the report with their dates
   and say, in one line, how to trigger it ("procesa el transcript que dejé en entrada").
3. **Watermark against reality.** Every meeting in `reuniones/` should be in the `processed`
   list of `_estado/ultima-ingesta.json`, and every processed id should have its file. A
   meeting file with no `salidas/ingesta-<fecha>.md` on or after its date is a run that did not
   leave its report. Record the mismatch; do not rewrite the watermark, because the next run
   depends on it and a wrong "fix" here makes the routine skip or repeat work.
4. **Log against playbooks, both ways.** Every `aplicada` line in `decisiones/bitacora.md`
   names a playbook; that playbook must have a section marked `<!-- Vigente desde <fecha> -->`
   on that date or a `## Historial` entry for it. And every `## Historial` entry must have its
   line in the log. A change without a line, or a line without a change, is the exact drift
   the single-writer rule exists to prevent; report both kinds with the file and date.
5. **Stale pending items.** `por confirmar` lines older than 30 days and `propuesta` lines
   older than 14 days (a proposed change to values waiting for the approver). List them with
   the question that would close each one, so the person can answer in one line.
6. **Placeholders still unfilled.** Any `<...>` left from the templates in `CLAUDE.md`,
   `_config/*`, `memory.md` or a playbook. The installation interview leaves gaps on purpose;
   the audit is what keeps asking about them.
7. **Cases without their lesson.** A case in `casos/` with an empty "Qué se aprendió" or "Qué
   valor se aplicó" section is an anecdote, and the responder does not cite anecdotes. Report
   it as a question for the person who told the case.
8. **Duplicates and sync clashes.** Files with `(1)`, `(2)` suffixes are Drive name clashes.
   Keep the newest under the canonical name only when the older one is byte-identical or
   strictly contained in it; otherwise report both and let a person choose. Never lose text.
9. **Memory to promote.** Lines in `memory.md` that record a gap ("pregunta sin respuesta
   escrita") for which a playbook, case or value now exists. Mark them resolved with a new
   dated line; do not delete the old one.

## The checks on the agent (once per run)

10. **Agent / context separation.** Build the list of the organization's proper names from
    `_config/empresa.md` (the organization, the people, the clients) plus the patterns of a
    phone number and an email address. Search for them in the agent's own files: the plugin's
    `skills/`, `templates/` and `docs/` when they are reachable from where you run (Claude
    Code, the desktop app), and any skill or template copy that ended up inside the brain
    folder. If a name, phone, email or organization-specific rule appears there, do three
    things: confirm the fact lives in the right file under `_config/` (add it only if it is
    missing; the folder outranks the agent file when they disagree); replace it in the local
    agent file with the generic reference ("the approver named in `_config/fuentes.md`") when
    that file is writable, knowing the next plugin release overwrites the local copy; and
    write the finding in the report with the exact file, line and one-line correction, marked
    **for the engine's maintainers**, because the durable fix is upstream in the plugin
    repository and this report is how it reaches them. If the file is not writable or the
    plugin files are not reachable (a cloud session), say so in the report instead of
    claiming the separation was restored. It is progressive work; one run does not have to
    finish it.
11. **One copy of each skill.** A skill that exists twice with content (for example a copy of
    `SKILL.md` inside the brain folder next to the installed plugin) drifts. Report it and
    propose keeping the installed one; do not delete the copy yourself.

## Intervention rules

- **The mechanical gets fixed**: moving a loose file to its obvious place, renaming a `(1)`
  duplicate that is identical, marking a resolved memory line, extracting a personal datum from
  an agent file. Every fix cites what it saw.
- **The doubtful is not touched**: it goes in the report with a proposal. Never delete
  content; never rewrite a log line; never change the watermark; never edit a playbook's
  current text.
- **No fix invents anything** or takes a position on a decision. The audit orders the folder;
  it does not opine on the case, and it never processes a transcript.
- **You never write outside the folder**, except the extraction of check 10 into the agent's
  own files, which removes information rather than adding it.

## Output

1. **A dated report**: `salidas/auditorias/<AAAA-MM-DD>-auditoria.md`, in the folder's working
   language, created together with `salidas/auditorias/` if missing. Structure: a summary (what
   was fixed, what is pending, one line each), then findings per check with file and date,
   then the agent-level findings. A run with nothing to report leaves a one-line report ("todo
   en orden" / "all in order"): the record that it ran is information too.
2. **Questions for the team**, one dated line each in `memory.md`, only for what needs a
   person: a stale inference to confirm, a proposal waiting for the approver, a case missing
   its lesson, a placeholder nobody filled.
3. Nothing else changes. The report is the deliverable; the folder is the same folder, in
   order.

## Done means

- Every check ran, or the report says which one could not and why.
- Every fix is listed with what it saw and what it did; every doubt is listed with a proposal.
- No line of the log, no current playbook text and no watermark value changed.
- The report exists, dated, in the folder's language.

## The failure to watch for

Helpfulness again. The audit finds a transcript waiting and the obvious move is to process it;
it finds a stale inference and the obvious move is to apply it; it finds a wrong watermark and
the obvious move is to correct it. Each of those is another skill's job or a person's decision,
and doing it from the audit breaks the one property that makes the folder trustworthy: that
every change to its records came through the front door, with its source and date.
