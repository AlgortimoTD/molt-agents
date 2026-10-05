# Directorio de freelancers · production freelancer directory

Agent that keeps **who a production team can call, for what, with which certifications and how they have delivered**, in a folder on Google Drive that the team can open, read and correct. When a shoot comes in it builds the shortlist in the team's priority order, filtered by the certification the job requires on that date, and leaves one message per person ready to paste into the channel that person actually answers; it logs who answered and who got the job when the team tells it; and every week it lists the certifications that are expired or about to expire. It is a folder with memory, not a chat with memory: if a person or a rule is not written there, the agent says so instead of inventing it.

**Agent / context separation (the golden rule):** the **agent** (these skills, the templates, the routine prompt) is agnostic and replicable: no names, phones, channels, job types, certifications or rules of any organization embedded. Everything personal lives in the **context files** of the organization's own folder (`CLAUDE.md`, `_config/*`, the cards under the freelancers folder, the memory file). The `directorio-freelancers-audit` skill polices this separation on every run.

## Bootstrap contract (how a session finds the organization's folder)

Every skill does this before working, in order:

1. The working folder has a `CLAUDE.md` whose first line is `<!-- directorio-freelancers -->`: that is the directory. Cowork and Claude Code with the project open.
2. Otherwise, read the platform memory entry `directorio-freelancers: <folder name or Drive path>`. Mobile and claude.ai through the Drive connector.
3. Otherwise, ask once, in the person's language ("¿cómo se llama la carpeta de tu directorio en Drive?" / "what is your directory's folder called in Drive?"), and save it to memory.

Then it reads the vocabulary block at the end of that `CLAUDE.md` and resolves every name from it (see Language).

`directorio-freelancers-setup` writes the marker as the first line of the organization's `CLAUDE.md`; it is also how Phase 0 recognizes an existing directory instead of creating a second one.

## How an instance is organized (the organization's folder)

Shown by vocabulary key; the literal name of each depends on the directory's language (see [templates/vocabulary.md](templates/vocabulary.md)).

```
<the organization's directory>/
  CLAUDE.md             orchestrator from templates/<lang>/CLAUDE.root.template.md; marker on line 1,
                        vocabulary block at the end
  {memory}              gaps and loose agreements, one dated line each
  {company}             who they are, who coordinates production, who approves additions and removals, time zone
  {rules}               job types; principals and preferred person per type; request mode and wait window;
                        certification each job type requires; what to do when nobody answers
  {certifications}      catalog of certifications the organization recognizes, typical validity, notice tiers
  {message-templates}   tone per channel and language, what a message always carries
  {sources}             routine account and time with its literal prompt, calendar read, Drive permissions per role
  {freelancers}         one card per person, each with a data block and sections; {supports} holds their certificates
  {requests}            one file per shoot: requirements, shortlist with reasons, exclusions, messages, answers, closure
  {outputs}             {index} (regenerated), {expiry-report} per sweep, {audit-report} per audit, the {guide}
  {state}               watermark: when the last sweep and the last index regeneration ran
```

Context hierarchy: the root `CLAUDE.md` is the only source of the hard rules, the file map and the vocabulary. `_config/` holds what is specific to the organization. Skills read both; general rules are never duplicated into `_config/`.

## Use-case map

| The user says / happens | What runs |
|---|---|
| "quiero instalarlo" / new organization | `directorio-freelancers-setup`: language first, Drive folder, the interview (who coordinates, job types and preferred people, request mode, certifications per job type, tone per channel), the first cards from the interview or a pasted list, connectors, weekly routine, a first sweep |
| "puebla el directorio con la productora de ejemplo" / "seed the demo production company" | `directorio-freelancers-setup` (demo mode): copies the fictional company from [demo/](demo/README.md), in the directory's language, next to the real folder, never inside it |
| "agrega a <persona>", "<persona> renovó su curso", "<persona> entregó tarde", a pasted list of people, "¿quién sabe hacer X?" | `production-pool-roster`: creates or updates a card with its history, writes reliability as dated facts, rephrases limits as assignment constraints, answers from the cards with the source, regenerates `{index}` |
| Monday (scheduled), "¿qué certificaciones vencen?", "¿quién tiene curso de alturas vigente el <fecha>?" | `certification-expiry-tracker`: the sweep by tier (expired, 7, 30, 60 days, undated, no supporting document), the `{expiry-report}`, the watermark, and dated answers |
| "necesito <perfil> para <fecha> en <lugar>, exige <certificación>", "<persona> dijo que sí", "nadie contestó", "cierra la producción" | `availability-request-drafter`: the request file with shortlist, exclusions with reasons, one message per person in their channel and language, the answers with time, who got it, the invite text, the closure that sends facts to the cards |
| Weekly (scheduled) or "organiza la carpeta" | `directorio-freelancers-audit`: vocabulary and language, roles, broken or hand-edited cards, undated certifications, requests past their date without closure, index and watermark coherence, agent / context separation |

## Rules the whole agent obeys (defined in the root template, enforced everywhere)

1. **People edit the cards, and the agent re-reads before it writes.** Unlike a single-writer archive, editing is the product here: the production coordinator corrects a card in the chat or by hand in Drive. Before writing a card the agent re-reads it, and the replaced text goes to the card's `{history}` with the date; nothing is deleted.
2. **Reliability is dated facts stated by the team, never a score.** "Delivered two days late on 2026-09-20, said by the coordinator" is written; a rating, a ranking or an adjective the team did not say is not. The agent lists and counts; the judgment stays with people.
3. **Limits are assignment constraints, never diagnoses.** A limit arrives as "do not assign text graphics" or "no short-deadline editing", and when it is dictated as a personal or medical condition the agent rephrases it as the constraint it implies, marks it `{rephrased}` with the date, and says so. The cards describe third parties who are not in the conversation.
4. **The agent never writes outward.** Its only writes are files in the folder. No messages to freelancers (even where a WhatsApp or Messenger piece exists on the platform), no calendar invites, no bookings, no payments. A message is a draft opening with `{draft-marker}` that a person pastes and sends.
5. **Only who meets the requirement on the date of the shoot enters the shortlist.** A certification is valid when its expiry is after the shoot's date, not after today; an undated certification never counts as valid; an exclusion always carries its written reason.
6. **Every claim carries its source**, card and date. What is not written is declared and offered for recording, never filled in.
7. **Roles come from the installation, never from the agent.** Three generic roles (production coordinator, approver of additions and removals, viewer) filled by the interview in the roles table of `{company}`; no skill or template names a person. A card the coordinator creates starts active at once and its addition is logged for the approver, who reviews new cards in the weekly audit and alone marks a person `{status-do-not-call}` or takes them out of the pool. The agent cannot tell who is writing to it, so the folder's Drive permissions are the real control.

## Language

The agent works in Spanish and in English. The skills are written in English; **everything they write into a directory is in the directory's language, with no exception a person can see**, and every message to a freelancer is additionally written in that freelancer's own language as recorded on their card. `directorio-freelancers-setup` asks the language as its first, mandatory question, says the answer is final, picks the matching template set (`templates/es/` or `templates/en/`) and writes the choice in the directory's `CLAUDE.md` and `{sources}`.

**Names by key.** Folder and file names, headings, data fields, request states, expiry tiers and role names all exist in both languages in [templates/vocabulary.md](templates/vocabulary.md). The directory's `CLAUDE.md` ends with a vocabulary block (an HTML comment, one `key: name` line each) in its language, and every skill resolves every name from that block by key. The only language-neutral pieces are identifiers nobody reads as text: the marker `<!-- directorio-freelancers -->` on line 1 and the JSON keys of `{state}`.

## Dependencies

None on the machine. Google Drive (folder synced with Drive for desktop, plus the Drive connector for cloud sessions), Google Calendar (read-only, optional: the shoot's date and clashes) and one scheduled task in one account.
