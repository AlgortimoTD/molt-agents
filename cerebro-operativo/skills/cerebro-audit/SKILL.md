---
name: cerebro-audit
description: >-
  v1.1.1 · Weekly audit of an organization's operating brain folder and of the agent itself. On the
  folder: loose files, unprocessed transcripts and documents, a watermark that disagrees with the
  meetings, log lines without their playbook change and the reverse, stale pending items and
  installation gaps, a missing brain owner, names from another language, unfilled placeholders,
  cases without their lesson. On the agent: any name, phone, email or rule of the organization that
  slipped into a skill or template, reported. Fixes the mechanical, never deletes, and leaves a
  dated report in the brain's language. Use it when someone asks to organize, review, clean or audit
  the brain, when the weekly routine runs it, or after an ingestion left items pending. Triggers:
  "organiza la carpeta", "revisa el cerebro", "corre la auditoría del cerebro", "qué está pendiente
  en el cerebro", "organize the folder", "audit the brain", "tidy up the brain". [v1.1.1]
---

# cerebro-audit

## Version 1.1.1

A brain folder drifts. Transcripts land in the inbox and nobody processes them, a decision gets
logged and its playbook never changes, an inference stays pending for two months, a placeholder
from the installation is still `<Nombre>`. None of this is anyone's fault; it is what happens
to any shared folder that several people and one routine write to. This skill is the routine
that restores order without waiting to be asked, fixes what is mechanical, and leaves a trail
of what it cannot decide alone.

It also does something the archive audit of a normal folder does not: it audits **the agent**.
The brain is a product installed by many organizations, and it stays a product only while the
skills and templates carry nothing of any single organization. Every urgent fix is a chance
for a customer's name to slip into a skill. This skill is the mechanism that reverts that, one
extraction at a time.

## Where you work

Find the brain folder the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- cerebro-operativo -->`; otherwise the platform memory entry
`cerebro-operativo: <folder>`; otherwise ask once and save it. Read the folder's `CLAUDE.md`
first. It gives you the organization's name, the working language (the report is written in
it), the roles and the time zone, and it outranks this skill wherever they differ.

**Every name comes from the brain.** `CLAUDE.md` ends with a vocabulary block
(`<!-- cerebro-operativo:vocabulary ... -->`) with one `key: name` line per folder, file,
heading, marker, state and role, in the brain's language. This skill refers to them by key in
braces (`{log}`, `{history}`, `{role-owner}`); read the block before anything else and use the
names it gives. Check 1 below is about that block itself.

You are member-agnostic. You take every name of a person from `{company}` and `{sources}` and
every rule from `CLAUDE.md`; nothing here assumes a particular organization.

## Scope of a run

Walk the folder in this order: `CLAUDE.md`, `{sources}` and the rest of `_config/`,
`{playbooks}`, `{log}`, `{cases}`, `{documents}`, `{meetings}` and `{meetings-inbox}`,
`{outputs}`, `{state}`, `{memory}`, and finally the loose items at the root. In each place you
compare **what the context files say against what actually exists**.

## The checks on the folder

1. **Vocabulary and language.** The vocabulary block is present, declares `lang`, and has
   every key the plugin's dictionary lists (`templates/vocabulary.md`, when reachable). Then
   look for names from another language: a folder or file named with the other column of the
   dictionary (`decisions/` in a Spanish brain, `reuniones/` in an English one), a `{history}`
   heading or a decision state written in the other language. Report each with its path; do
   not rename a folder yourself, because other surfaces may be holding it open. A missing or
   incomplete block is the first line of the report: every other skill depends on it.
2. **Roles.** The roles table of `{sources}` has exactly one person with `{role-owner}`. None,
   or two, is a finding for the team, in plain words ("el cerebro no tiene responsable" / "the
   brain has no owner"). Also report a rule in `CLAUDE.md` that names a person where it should
   name a role.
3. **Loose files.** Anything at the root or inside a pattern folder that is not part of the
   pattern (a PDF dropped at the root, a transcript outside `{meetings}`, a copy of a skill).
   If the destination is obvious (a document at the root goes to `{documents}`), move it and
   record the move; if it is doubtful, do not touch it, put it in the report with a proposal.
4. **Transcripts waiting.** Files in `{meetings-inbox}` other than its README are work the
   routine has not done. Do not process them yourself (that is `transcript-to-playbook-
   updater`'s job and it runs from the watermark); list them in the report with their dates
   and say, in one line, how to trigger it.
5. **Documents not processed.** Every file in `{documents}` other than its README should be
   cited as origin by at least one playbook section, value or case. A document nobody cites is
   knowledge the brain does not have yet; list it with its name and date, and propose the one
   line that processes it ("procesa el documento que dejé en documentos" / "process the
   document I left in documents").
6. **Watermark against reality.** Every meeting in `{meetings}` should be in the `processed`
   list of `{state}`, and every processed id should have its file. A meeting file with no
   `{ingestion-report}` on or after its date is a run that did not leave its report. Record the
   mismatch; do not rewrite the watermark, because the next run depends on it and a wrong
   "fix" here makes the routine skip or repeat work.
7. **Log against playbooks, both ways.** Every `{applied}` line in `{log}` names a playbook;
   that playbook must have a section marked `{current-since}` on that date or a `{history}`
   entry for it (a `{confirmed}` line needs neither: it changed no text). And every
   `{history}` entry must have its line in the log. A change without a
   line, or a line without a change, is the exact drift the single-writer rule exists to
   prevent; report both kinds with the file and date. A section whose text changed with no
   history entry and no log line is most likely a hand edit: ask the brain owner to confirm it
   so the trail can be written, and do not revert it.
8. **Stale pending items.** `{to-confirm}` lines older than 30 days and `{proposed}` lines older
   than 14 days (a proposed change to values waiting for the brain owner). List them with the
   question that would close each one, so the person can answer in one line.
9. **Installation gaps.** `{memory}` lines starting with `{gap}` or `{pending-kickoff}` that are
   still open. List each with its age; a kickoff meeting still pending after two weeks goes at
   the top of the summary, because until it happens the playbooks say what the old documents
   said.
10. **Placeholders still unfilled.** Any `<...>` left from the templates in `CLAUDE.md`,
    `_config/`, `{memory}` or a playbook. The installation interview leaves gaps on purpose;
    the audit is what keeps asking about them.
11. **Cases without their lesson.** A case in `{cases}` with an empty `{case-lesson}` or
    `{case-value}` section is an anecdote, and the responder does not cite anecdotes. Report it
    as a question for the person who told the case.
12. **Duplicates and sync clashes.** Files with `(1)`, `(2)` suffixes are Drive name clashes.
    Keep the newest under the canonical name only when the older one is byte-identical or
    strictly contained in it; otherwise report both and let a person choose. Never lose text.
13. **Memory to promote.** Lines in `{memory}` that record a gap (`{unanswered}` or `{gap}`) for
    which a playbook, case or value now exists. Mark them resolved with a new dated line; do
    not delete the old one.

## The checks on the agent (once per run)

14. **Agent / context separation.** Build the list of the organization's proper names from
    `{company}` and `{sources}` (the organization, the people, the clients) plus the patterns of
    a phone number and an email address. Search for them in the agent's own files: the
    plugin's `skills/`, `templates/` and `docs/` when they are reachable from where you run
    (Claude Code, the desktop app), and any skill or template copy that ended up inside the
    brain folder. If a name, phone, email or organization-specific rule appears there, do
    three things: confirm the fact lives in the right file under `_config/` (add it only if it
    is missing; the folder outranks the agent file when they disagree); replace it in the local
    agent file with the generic reference ("the brain owner named in the roles table") when
    that file is writable, knowing the next plugin release overwrites the local copy; and write
    the finding in the report with the exact file, line and one-line correction, marked **for
    the engine's maintainers**, because the durable fix is upstream in the plugin repository
    and this report is how it reaches them. If the file is not writable or the plugin files are
    not reachable (a cloud session), say so in the report instead of claiming the separation was
    restored. It is progressive work; one run does not have to finish it.
15. **One copy of each skill.** A skill that exists twice with content (for example a copy of
    `SKILL.md` inside the brain folder next to the installed plugin) drifts. Report it and
    propose keeping the installed one; do not delete the copy yourself.

## Intervention rules

- **The mechanical gets fixed**: moving a loose file to its obvious place, renaming a `(1)`
  duplicate that is identical, marking a resolved memory line, extracting a personal datum from
  an agent file. Every fix cites what it saw.
- **The doubtful is not touched**: it goes in the report with a proposal. Never delete
  content; never rewrite a log line; never change the watermark; never edit a playbook's
  current text; never rename a folder.
- **No fix invents anything** or takes a position on a decision. The audit orders the folder;
  it does not opine on the case, and it never processes a transcript or a document.
- **You never write outside the folder**, except the extraction of check 14 into the agent's
  own files, which removes information rather than adding it.

## Output

1. **A dated report** at the `{audit-report}` path, in the brain's working language, creating
   its folder if missing. Structure: a summary (what was fixed, what is pending, one line
   each), then findings per check with file and date, then the agent-level findings. A run
   with nothing to report leaves a one-line report saying all is in order: the record that it
   ran is information too.
2. **Questions for the team**, one dated line each in `{memory}`, only for what needs a person:
   a stale inference to confirm, a proposal waiting for the brain owner, a case missing its
   lesson, a placeholder nobody filled, a brain with no owner.
3. Nothing else changes. The report is the deliverable; the folder is the same folder, in
   order.

## Done means

- Every check ran, or the report says which one could not and why.
- Every fix is listed with what it saw and what it did; every doubt is listed with a proposal.
- No line of the log, no current playbook text, no watermark value and no folder name changed.
- The report exists, dated, at the `{audit-report}` path, in the brain's language.

## The failure to watch for

Helpfulness again. The audit finds a transcript waiting and the obvious move is to process it;
it finds a stale inference and the obvious move is to apply it; it finds a wrong watermark and
the obvious move is to correct it; it finds a folder named in the other language and the
obvious move is to rename it. Each of those is another skill's job or a person's decision, and
doing it from the audit breaks the one property that makes the folder trustworthy: that every
change to its records came through the front door, with its source and date.
