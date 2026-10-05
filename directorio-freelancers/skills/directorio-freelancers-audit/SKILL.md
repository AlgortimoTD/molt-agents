---
name: directorio-freelancers-audit
description: >-
  v1.0.0 · Weekly audit of a production team's freelancer directory folder and of the agent
  itself. On the folder: cards with a broken data block or edited by hand without a dated history
  entry, certifications without date or document, names outside the catalog, requests past their
  shoot date without closure, index or watermark drift, stale gaps, missing roles, sync
  duplicates. On the agent: any name, phone or rule of the organization or a freelancer that
  slipped into a skill or template, reported for the maintainers. Fixes the mechanical, never
  deletes, never reverts a card, leaves a dated report in the directory's language. Use it when
  someone asks to organize, review or audit the directory, when the weekly routine runs it, or
  after a sweep left gaps. Triggers: "organiza la carpeta del directorio", "revisa el
  directorio", "corre la auditoría del directorio", "qué está pendiente en el directorio", "audit
  the freelancer directory", "tidy up the directory". [v1.0.0]
---

# directorio-freelancers-audit

## Version 1.0.0

A directory folder drifts. The coordinator fixes a card by hand on the phone and the history
never hears of it, a shoot happens and its request stays open, a certification keeps saying
"sin fecha" for two months, a placeholder from the installation is still `<Nombre>`. None of
this is anyone's fault; it is what happens to any shared folder that several people and one
routine write to, and in this folder people are supposed to write, because editing the cards
is the product. This skill is the routine that restores order without waiting to be asked,
fixes what is mechanical, and leaves a trail of what it cannot decide alone.

It also does something the archive audit of a normal folder does not: it audits **the agent**.
The directory is a product installed by many organizations, and it stays a product only while
the skills and templates carry nothing of any single organization or of any freelancer. Every
urgent fix is a chance for a person's name to slip into a skill. This skill is the mechanism
that reverts that, one extraction at a time.

## Where you work

Find the directory folder the way every skill of this agent does: the working folder whose
`CLAUDE.md` starts with `<!-- directorio-freelancers -->`; otherwise the platform memory entry
`directorio-freelancers: <folder>`; otherwise ask once and save it. Read the folder's
`CLAUDE.md` first. It gives you the organization's name, the working language (the report is
written in it), the roles and the time zone, and it outranks this skill wherever they differ.

**Every name comes from the directory.** `CLAUDE.md` ends with a vocabulary block
(`<!-- directorio-freelancers:vocabulary ... -->`) with one `key: name` line per folder, file,
heading, data field, state, tier and role, in the directory's language. This skill refers to
them by key in braces (`{freelancers}`, `{card-data}`, `{role-approver}`); read the block
before anything else and use the names it gives. Check 1 below is about that block itself.

You are member-agnostic. You take every name of a person from `{company}` and from the cards
under `{freelancers}`, and every rule from `CLAUDE.md`, `{rules}` and `{certifications}`;
nothing here assumes a particular organization.

## Scope of a run

Walk the folder in this order: `CLAUDE.md`, `{company}` and the rest of `_config/`,
`{freelancers}` and `{supports}`, `{requests}`, `{outputs}` (the `{index}`, the latest
`{expiry-report}`), `{state}`, `{memory}`, and finally the loose items at the root. In each
place you compare **what the context files say against what actually exists**.

## The checks on the folder

1. **Vocabulary and language.** The vocabulary block is present, declares `lang`, and has
   every key the plugin's dictionary lists (`templates/vocabulary.md`, when reachable). Then
   look for names from another language: a folder or file named with the other column of the
   dictionary (`requests/` in a Spanish directory, `solicitudes/` in an English one), a
   `{history}` heading, a data field or a tier written in the other language. Report each with
   its path; do not rename a folder yourself, because other surfaces may be holding it open. A
   missing or incomplete block is the first line of the report: every other skill depends on
   it.
2. **Roles.** The roles table of `{company}` has at least one person with `{role-coordinator}`
   and exactly one with `{role-approver}`. None, or two approvers, is a finding for the team,
   in plain words ("el directorio no tiene quien apruebe altas y bajas" / "nobody approves
   additions and removals"). Also report a rule in `CLAUDE.md` that names a person where it
   should name a role. Then list, for the approver, the cards created since the last audit
   (their `{current-since}` date is later than the previous `{audit-report}`): a new card starts
   active the moment the coordinator creates it, and this list is how the approver sees every
   addition without anyone having to remember to tell them.
3. **Loose files.** Anything at the root or inside a pattern folder that is not part of the
   pattern (a certificate PDF at the root, a request outside `{requests}`, a copy of a skill).
   If the destination is obvious (a certificate at the root goes to `{supports}`), move it and
   record the move; if it is doubtful, do not touch it, put it in the report with a proposal.
4. **Cards: the data block.** Every card under `{freelancers}` opens with `{card-data}` and a
   fenced block carrying the five fields (`{field-name}`, `{field-channel}`, `{field-contact}`,
   `{field-language}`, `{field-status}`), and the status is one of `{status-active}`,
   `{status-paused}`, `{status-do-not-call}`. A missing field, an extra field, or a status
   outside the three is a broken block: report it with the card, say which field, and propose
   the one-line repair ("falta `idioma:` en la ficha de Bel Casas; ¿español o inglés?"). Do not
   fill it yourself: the value is a fact about a person only the team knows.
5. **Cards: hand edits.** Compare each card's sections against its `{history}` and against
   the last dated line that cites it (a request closure, a roster change). A section whose
   text differs from what its last trail accounts for, with no dated `{history}` entry, is
   most likely a hand edit in Drive. That is allowed here, so do not revert it and do not treat
   it as an error; report it and ask the coordinator to confirm it in one line, so the trail
   can be written ("la ficha de Bel Casas tiene una especialidad nueva sin fecha ni autor;
   ¿la agregaste tú? dime cuándo y la dejo con su rastro").
6. **Certifications without date or without document.** Every row of every card's
   `{card-certifications}` table has a date or says `{tier-undated}`, and names a file in
   `{supports}` that exists or says `{tier-unsupported}`. Cross-check with the latest
   `{expiry-report}`: a row the report lists as undated or unsupported that the card now dates
   or documents is progress (check 13); a card row the report does not mention is a sweep that
   did not run over it. Report both.
7. **Certification names outside the catalog.** A certification named on a card that is not a
   row of `{certifications}` is either a new one the team should add or a different spelling
   of an existing one. Report it with the card and the closest catalog name; do not rename it
   on the card.
8. **Requests past their date without closure.** Every file in `{requests}` whose shoot date
   is before today and whose state line is not `{state-closed}` or `{state-unfilled}` is a
   shoot that happened without its facts reaching the cards. List them with the one line that
   closes each ("cierra la producción del puente del 2026-10-07"); do not close them yourself,
   because the closure needs what the team says about how each person delivered.
9. **Index against the cards.** `{index}` has one row per card and no row for a card that no
   longer exists; its regeneration date is on or after the newest card change. An index older
   than a card is stale: say so and name the card, so the next sweep or roster change
   regenerates it. Do not regenerate it from the audit.
10. **Watermark against the reports.** `{state}` names, as its last report, the newest
    `{expiry-report}` that exists in `{outputs}`, and its sweep date matches that report's.
    Record any mismatch; do not rewrite the watermark, because the next sweep depends on it.
11. **Stale gaps.** `{gap}` lines in `{memory}` older than 30 days with no later line closing
    them. List each with its age and the question that would close it, so the person can
    answer in one line.
12. **Placeholders still unfilled.** Any `<...>` left from the templates in `CLAUDE.md`,
    `_config/`, `{memory}` or a card. The installation interview leaves gaps on purpose; the
    audit is what keeps asking about them.
13. **Duplicates and sync clashes.** Files with `(1)`, `(2)` suffixes are Drive name clashes.
    Keep the newest under the canonical name only when the older one is byte-identical or
    strictly contained in it; otherwise report both and let a person choose. Never lose text.
14. **Memory to promote.** `{gap}` lines whose card now carries the date, the document or the
    channel they asked for. Mark them resolved with a new dated line; do not delete the old
    one.

## The checks on the agent (once per run)

15. **Agent / context separation.** Build the list of proper names from `{company}` (the
    organization, the people in the roles table) and from every card under `{freelancers}`
    (the freelancers), plus the patterns of a phone number and an email address. Search for
    them in the agent's own files: the plugin's `skills/`, `templates/` and `docs/` when they
    are reachable from where you run (Claude Code, the desktop app), and any skill or template
    copy that ended up inside the directory folder. If a name, phone, email or
    organization-specific rule appears there, do three things: confirm the fact lives in the
    right file under `_config/` or on the right card (add it only if it is missing; the folder
    outranks the agent file when they disagree); replace it in the local agent file with the
    generic reference ("the production coordinator named in the roles table", "a freelancer's
    card") when that file is writable, knowing the next plugin release overwrites the local
    copy; and write the finding in the report with the exact file, line and one-line
    correction, marked **for the engine's maintainers**, because the durable fix is upstream in
    the plugin repository and this report is how it reaches them. A phone number or a name that
    sits inside the folder's own `_config/` or cards is not an agent finding: it is where such
    data belongs, and at most a folder finding if it should not be there (a phone number in
    `{message-templates}`, for instance, which is a template of tone, not a contact list). If
    the plugin files are not reachable (a cloud session), say so in the report instead of
    claiming the separation was restored.
16. **One copy of each skill.** A skill that exists twice with content (for example a copy of
    `SKILL.md` inside the directory folder next to the installed plugin) drifts. Report it and
    propose keeping the installed one; do not delete the copy yourself.

## Intervention rules

- **The mechanical gets fixed**: moving a loose certificate to `{supports}`, renaming a `(1)`
  duplicate that is identical, marking a resolved memory line, extracting a personal datum from
  an agent file. Every fix cites what it saw.
- **The doubtful is not touched**: it goes in the report with a proposal. Never delete content;
  never rewrite a card's current text, not even a broken data block; never change the
  watermark; never regenerate the index; never close a request; never run a sweep; never rename
  a folder.
- **No fix invents anything** or takes a position on a person. The audit orders the folder; it
  does not opine on a freelancer, it does not fill a missing field, and it never drafts a
  message.
- **You never write outside the folder**, except the extraction of check 15 into the agent's
  own files, which removes information rather than adding it.

## Output

1. **A dated report** at the `{audit-report}` path, in the directory's working language,
   creating its folder if missing. Structure: a summary (what was fixed, what is pending, one
   line each), then findings per check with file and date, then the agent-level findings. A
   run with nothing to report leaves a one-line report saying all is in order: the record that
   it ran is information too.
2. **Questions for the team**, one dated line each in `{memory}`, only for what needs a person:
   a hand edit to confirm, a missing field to fill, a request to close, a certification to date
   or document, a placeholder nobody filled, a directory with no approver.
3. Nothing else changes. The report is the deliverable; the folder is the same folder, in
   order.

## Done means

- Every check ran, or the report says which one could not and why.
- Every fix is listed with what it saw and what it did; every doubt is listed with a proposal.
- No card's current text, no request, no watermark value, no index and no folder name changed.
- The report exists, dated, at the `{audit-report}` path, in the directory's language.

## The failure to watch for

Helpfulness again. The audit finds a card with no language and the obvious move is to guess
"español"; it finds an open request for a shoot that already happened and the obvious move is
to close it; it finds a stale index and the obvious move is to regenerate it; it finds a card
edited by hand and the obvious move is to put it back. Each of those is another skill's job or
a person's decision, and doing it from the audit breaks the one property that makes the folder
trustworthy: that every change to a person's card came through the front door, with its source
and date.
