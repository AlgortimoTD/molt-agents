# How to operate the brain

Five things you will need to do and nobody should have to ask about. They are in order of
frequency: the first happens every week, the last almost never. The roles (brain owner,
editor, viewer) are the ones in the roles table of `_config/sources.md` in this folder.

The rule that runs through all five: **the brain writes, you tell it what**. Changes are
asked for in the chat and the brain writes them with their trail. It is not bureaucracy: if
two people edit the same file in Drive at the same time, one of the two versions is lost, and
if someone changes a playbook without going through the log, the record stops matching the
process and nobody knows which of the two is right anymore. The brain owner may also edit any
file by hand; when they do, they tell the brain in the chat ("I edited the proposals
playbook") so it archives the previous version and adds the line to the log.

---

## 1. Dropping a transcript by hand

When Fathom did not record the meeting (a phone call, a meeting nobody scheduled, a
conversation worth keeping).

1. Save the text in a file. Anything works: a `.md`, a `.txt`, whatever the tool exports.
2. Name it with the date first: `2026-09-22-call-with-client.md`.
3. Leave it in `meetings/inbox/`.
4. Wait for the routine's run (the time is in `_config/sources.md`), or ask in the project
   chat: **"process the transcript I left in the inbox"**.

The brain reads it, writes the meeting file in `meetings/`, adds the decisions to the log and
updates the playbooks that changed. The summary of what it did stays in `outputs/`.

**If the text has no minutes**, the brain says so and cites the meeting without a minute. It
is not a problem; it is only less traceable.

---

## 2. Adding a document you already had

A manual, a procedure, a template, an onboarding deck that shows up after the installation.

1. Leave it in `documents/`, or paste it in the chat. If it is a Drive link, paste the link.
2. Ask in the chat: **"process the document I left in documents"**.

The brain reads it, decides which process it belongs to and writes or completes that playbook
**from the document**, with the document's date and its name as the origin. It does not
modernize it: if something sounds old, it writes it as it is and marks it pending
confirmation, so the team corrects it in a meeting. The original is never touched.

If the document contradicts something already written, the brain does not choose on its own:
it shows you both versions with their dates and asks which one holds.

---

## 3. Correcting a badly extracted decision

It will happen. Informal meetings carry noise and the filter is not perfect.

Tell it in the chat, in plain language:

> "The September 18 decision about freelancers is wrong. We did not say the preferred one
> always gets it first, we said it depends on the type of work. Fix it."

The brain does three things and reports them to you:

1. **Adds a new line** to the log that corrects the previous one, with your name under
   "Requested by". It does not delete the old one. That is the whole rule: in this folder
   nothing is deleted, because the day someone asks "why did this change?", the answer has to
   be there.
2. **Returns the playbook to the correct text**, and the wrong text moves to `## History` the
   way the previous one did.
3. **Shows you how it turned out** before calling it done.

**If what you want is to undo it entirely**, say it like this: "that decision never existed,
you extracted it wrong". The brain leaves the line in the log marked as reverted, with the
date, and returns the playbook to the text it had before. The line stays because the log is
the record of what happened, including the mistake.

If the correction touches values or negotiables and the brain owner did not ask for it, it
stays as a proposal until the owner approves it.

---

## 4. Adding a case

A case is a story with a client, a decision and an ending. It is what the brain cites when
someone asks "how do we handle something like this?".

Tell it in the chat, spoken, without structure:

> "Add a case. Client so-and-so started emailing the team after hours with complaints. I
> stepped in, asked for a call with him and his boss, and we put in writing which channel is
> used to talk to the team. It lasted six more months and we did not renew."

The brain builds `cases/YYYY-client.md` with the five parts that make a case citable: what
happened, what was done, how it ended, **what was learned** and **which value applied**. The
last two are the ones that matter, and if you did not tell them it will ask. A case without
the lesson is an anecdote, and the brain does not cite anecdotes.

**Old cases count too**, and they count a lot: a case from three years ago that someone on
the team remembers is exactly the knowledge this folder exists not to lose.

---

## 5. What to do if the routine did not run

**How you notice:** there is no new `ingestion-YYYY-MM-DD.md` file in `outputs/`.

**First, and it is almost always this:** there was nothing to ingest. If there was no meeting
that day or Fathom published no new transcript, the routine ran, found nothing and wrote no
file. That is correct.

**If there was a recorded meeting**, in order:

1. **Wait for the next day's run.** The routine is cumulative: it reads how far it got last
   time and picks up everything pending. A lost day recovers by itself the next one, and
   nothing has to be done. This is the right answer most of the time.
2. **If you are in a hurry**, ask in the chat: **"run the ingestion now"**. It does the same
   as the routine. Running it twice breaks nothing: the watermark keeps a transcript from
   being processed twice.
3. **If two days in a row nothing appears** and there were recorded meetings, it is one of
   three, in this order of likelihood: the transcript was not shared with the Fathom team;
   the Fathom connection in the account where the routine runs expired and has to be
   authorized again; or the scheduled task was turned off. Write to Molt with the date of the
   missing meeting.

**What NOT to do:** start writing the playbooks by hand in the meantime. The transcript is not
lost, and when the routine runs again it picks them all up. Writing them by hand creates
exactly the conflict the single-writer rule avoids.

---

## Changing who holds which role

The brain owner asks for it in the chat: **"from today Ana is an editor"** or **"the new brain
owner is Ana"**. The brain updates the roles table of `_config/sources.md` with the date and
adds the line to the log. Then the folder's Drive permissions have to be adjusted to match:
a person does that, because it is what really decides who can change the folder.
