# How to operate the directory

<!-- FICTIONAL DOCUMENT: invented production company for the demo of the directorio-freelancers plugin. -->

Six things you will need to do and nobody should have to ask about. They are in order of
frequency: the first happens every time there is a shoot, the last almost never. The roles
(production coordinator, approver, viewer) are the ones in the roles table of
`_config/company.md` in this folder.

The rule that runs through all six: **the cards are yours, and the directory re-reads before
it writes**. You can correct a card in the chat or open it in Drive and edit it by hand; the
directory reads it again before touching it, and the text it replaces goes to the card's
`## History` with the date. Nothing is deleted. The only thing it asks is that, when you edit
by hand, you tell it in the chat ("I corrected Ariel's card"), so it archives the previous
version and nothing is left without a trail.

---

## 1. Staffing a shoot

From the moment the request comes in until a person is confirmed.

### Opening the request

Tell the directory, in the project chat, what you would tell a colleague:

> "I need a photographer tomorrow at 7:00 for the beams of the new bridge on the north road,
> a valid safety course is required."

If something is missing (the end time, how many people, the place), it asks before building
anything. With that it writes a new file in `requests/` with the date and the name of the
shoot, and shows you:

- **Requirements**: date and time, place, job, role, the job type of your rules that
  applies, the required certification and the mode (sequential or simultaneous) with its
  wait window.
- **Shortlist**: the people who can, in the order of your rules, and the reason for each
  position ("preferred for the type", "second principal", "does the job according to their
  card, not a principal").
- **Excluded and why**: who does that job but stays out, with the written reason (course
  expired on such date, undated course, paused status, an assignment limit). Nobody leaves
  the list without a reason, and the reason always cites the card.
- **Messages**: one draft per person on the list, in the channel and language of their
  card, with what your templates say a message always carries.
- **Answers**, empty, waiting.

The certification is checked against the date of the shoot, not against today. Someone whose
course expires on the 10th enters a shoot on the 7th and does not enter one on the 15th.

### Sending the messages

The directory sends nothing. Every message opens with the line "DRAFT: paste and send from
your phone" and you copy it and paste it into WhatsApp or Messenger, to the person or the
group named on their card. If the mode is sequential, you send position 1 first and wait the
window; if it is simultaneous, you send them all.

### Logging who answered

Tell it however it comes:

> "Ariel cannot. Bel said yes at 3:40."

The directory writes time, person and answer under **Answers**, writes the name under **Who
got it**, adds a dated fact to each card (answered, did not answer, how fast) and leaves the
**Invite text** ready: title, date, time, place and who is going. You send the calendar
invite from your own account; the directory invites nobody.

If nobody answered within the window, say **"nobody answered"** and it proposes the next
step of the list according to your rules (widening to whoever has the specialty even if not
a principal, or whatever you wrote under "When nobody answers").

### Closing the shoot

Once the job has happened:

> "Close the bridge shoot. Bel delivered the material on Thursday, on time."

The directory marks the request closed, writes the **Closure** with how each person
delivered, and passes that fact, with the date and your name, to the **Reliability (facts)**
section of the card. That is what the next shortlist will take into account.

---

## 2. Adding or correcting a freelancer

### A new person

One sentence is enough:

> "Add Nora Beltrán, event camera operator, WhatsApp in the production group, writes in
> Spanish, safety course expires March 2027."

The directory creates her card in `freelancers/` with the **Data** block (name, channel,
contact, language, status), her **Specialties**, her **Certifications** and the rest empty.
What you did not say becomes a gap in `memory.md` ("no exact expiry date") instead of an
invention. If you have a list (a sheet, a note, a pinned chat), paste the whole thing and the
directory turns it into cards and tells you what each one is missing.

Who enters the pool is decided by the **approver**. If the coordinator asks for it, it stays
a proposal until that person confirms it in the chat.

### Correcting something

In the chat ("change Dani's channel to Messenger", "Greta no longer does construction
photography") or by hand in Drive, and then you tell it. Either way the previous text stays
in the card's `## History` with the date.

### Limits are written as constraints

An assignment limit says what not to ask of a person: "no short-deadline editing", "no
shifts longer than eight hours in a row". If you dictate it as a personal or medical
condition, the directory writes it as the constraint it implies, marks it "Rephrased as an
assignment constraint" with the date, and tells you. It is not distrust: the cards describe
people who are not in the conversation, and what production needs to know is which job not
to assign them, not why.

### Facts, not ratings

The directory rates nobody. If you tell it "Dani is unreliable", it will ask for the fact:
"Dani delivered the video a day late on August 22". That is what it writes, with the date and
who said it. The judgment about whether to call him stays yours; what the directory does is
make sure that judgment is made with the facts in view.

### The three statuses

- **active**: enters shortlists.
- **paused**: does not enter for now; the card says until when and why, with a date ("out
  of the country until November 15"). The coordinator sets it.
- **do not call**: does not enter anymore; the card says why, with a date. The approver
  decides it, and if anyone else asks for it, it stays a proposal.

---

## 3. Certifications and the Monday sweep

Every Monday at the time written in `_config/sources.md`, with no computer switched on, the
directory reads the certifications of every card and leaves a new report in
`outputs/expiries-YYYY-MM-DD.md`. Every certification falls into exactly one of six tiers,
counted from that Monday:

| Tier | What it means | What you do |
|---|---|---|
| expired | the date has passed | that person does not enter shoots that require the course until they renew |
| expires within 7 days | it expires this week | tell them; they still enter shoots this week before the date |
| expires within 30 days | it expires this month | a good moment to ask for the renewal |
| expires within 60 days | it expires in two months | just so you have it on the radar |
| undated | the card names the course but not when it expires | it never counts as valid; ask for the card and tell the directory the date |
| no supporting document | it has a date but there is no document in `freelancers/documents/` | ask for the document; meanwhile the date does count for shortlists |

What expires after 60 days does not appear in the report; it stays on the card.

### Saving a certificate

Drop the photo or the PDF in `freelancers/documents/` and tell the directory whose it is:

> "I left Fausto's heights card in documents, it expires December 1, 2026."

The directory writes the date and the file name in the **Certifications** table of his card,
and the certification leaves the "undated" or "no supporting document" tier at the next
sweep.

### A renewal

> "Dani renewed his safety course, it expires September 28, 2027."

The old date goes to History, the new one stays in the table, and Dani enters shortlists
again from that moment.

### Asking without waiting for Monday

> "Who holds a valid safety course on October 15?"

It answers with the people and each one's expiry date, read from the cards. If you want the
full sweep today, say **"run the sweep"**; running it twice on the same day changes nothing.

---

## 4. Reading the directory from the phone

The file `outputs/directory.md` is the index of the whole pool: one row per person with
their specialties, channel and language, status, certifications valid as of the last sweep,
and last shoot. It regenerates on its own at every sweep and whenever a card changes; it is
not edited by hand.

Open it from the Drive app on your phone, or ask the directory from the Claude app on your
phone ("who does construction photography?"): it reads the same folder, with your computer
off.

---

## 5. What the directory never does, and why

- **It does not message the freelancers.** It leaves the messages written and you send them.
  On purpose: you are the one who signs the message, and the freelancers answer in the
  channel where they already know you.
- **It does not book, hire, pay or invite to the calendar.** It leaves the invite text and you
  send it. Confirming someone is your commitment to that person.
- **It rates nobody.** It writes the dated facts, with their author, that you tell it. The
  judgment belongs to the team.
- **It does not invent.** If a person, a rule or a certification is not written in the
  folder, it says so and offers to record it.

---

## 6. When something looks wrong

### Tidying the folder

Once a week a review runs on its own, and you can ask for it any time: **"tidy up the
folder"**. It leaves a report in `outputs/audits/` with what it found and what it fixed:
cards whose data block was broken by a hand edit, undated or undocumented certifications,
requests whose date has passed without a closure, an outdated index or watermark, and the
gaps in `memory.md` that are still open. It fixes the mechanical and tells you; what needs a
decision it leaves as a one-line question.

### A card lost its structure

It happens when a card is edited by hand and a heading or a line of the data block is
deleted. Say **"repair Greta's card"**: the directory rebuilds it with its sections, shows you
what went where and keeps the previous version in History. It loses no text; at worst it
leaves a line under "Team notes" with what it could not place.

### A request was left open

If the shoot's date has passed and the request is still open or assigned without a closure,
the weekly review asks you about it. Close it with one sentence (section 1) or say **"that
shoot did not happen"** and it is marked unfilled, with the reason.

### The Monday sweep did not run

**How you notice:** there is no new `expiries-YYYY-MM-DD.md` in `outputs/` dated this
Monday.

1. **Ask for it in the chat:** "run the sweep". It does exactly what the scheduled task does,
   and running it twice changes nothing. With that you already have the week's report.
2. **Check the scheduled task** in the account where it runs (it is written in
   `_config/sources.md`): that it is still on, with the day and time you agreed. If it is
   off, switch it back on.
3. **Check the Drive connection** in that same account: in the Claude app, under
   connections, Google Drive should show as authorized. If it asks to authorize again, do it
   with your own session; the directory never asks you for a password.

With those three checks the sweep runs again on its own the following Monday.

---

## Changing who holds which role

The approver asks for it in the chat: **"from today Nora coordinates production"**. The
directory updates the roles table of `_config/company.md` with the date and keeps the
previous one in History. Then the folder's permissions in Drive have to be adjusted to match:
a person does that, because it is what really decides who can change the folder.
