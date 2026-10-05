# Team onboarding session: install the freelancer directory, seed it, demo it

A two-hour hands-on session for a team that will install the **directorio-freelancers** agent on their own computers, populate it with the fictional demo production company, run the use cases, and leave able to demo it to a prospect. Facilitator: whoever built the agent. Attendees: 3 to 8 people, each with their own laptop.

## Before the session (the day before)

Each item is the attendee's own click; Claude cannot do it for them:

1. A Claude account with **Claude Code** access, signed in on the **Claude desktop app** (the Code tab visible next to Chat). Nobody opens a terminal at any point.
2. **Google account + Google Drive for Desktop** installed and syncing (the drive letter or `~/Google Drive` visible).
3. Nothing else. The directory has no local dependencies. The repository `AlgortimoTD/molt-agents` is public, so no GitHub account either.

## Agenda (120 minutes)

| Block | Minutes | Outcome |
|---|---|---|
| 1. What it is | 10 | Facilitator demo on the demo company: one shoot staffed from the request to the invite text, one expiry report read. The three layers explained. |
| 2. Install | 20 | Every laptop has the plugin, a directory folder in Drive, and has run "quiero instalarlo" to the first sweep. |
| 3. Seed the demo company | 10 | "puebla el directorio con la productora de ejemplo": eight cards whose certifications cross every tier, the assignment rules, one closed request, and the bridge shoot waiting to be staffed. |
| 4. Use cases | 45 | Each attendee runs at least four of the six use cases below on their own machine. |
| 5. Surfaces and the routine | 15 | Facilitator shows the same folder from the phone (Drive connector) and the scheduled Monday sweep. |
| 6. Sales script | 20 | The five-minute pitch, the objections, and who will run the first prospect demo. |

## Block 2: install (zero commands, everything from the Code tab)

1. Create the directory folder in Drive (for example `Directorio de producción <empresa>\`) and mark it available offline.
2. Open the Claude desktop app, **Code** tab, *Open project*, pick that folder.
3. Paste this message in the chat and approve the permission prompt(s):

   > Instala el directorio de freelancers de producción de mi empresa. Viene del marketplace AlgortimoTD/molt-agents, plugin directorio-freelancers. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos.

   Click alternative: `/plugin`, Marketplaces, Add, `AlgortimoTD/molt-agents`, Discover, directorio-freelancers, Install.
4. In the same chat say **"quiero instalarlo"**. `directorio-freelancers-setup` takes over: the language first (final, and every folder and file ends up named in it), Drive integration, root `CLAUDE.md` and `_config/` through the interview (who coordinates production, who approves additions and removals, the job types with their principals and preferred person, the request mode and wait window per type, the certification each job type requires and the notice tiers, the tone per channel), the first cards from the interview or a pasted list, the Drive and Calendar connectors, the weekly sweep scheduled with its literal prompt, and a first sweep run end to end. For claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add, plus the Google Drive connector.

After a release, ask in the chat: *actualiza el plugin directorio-freelancers* (claude.ai syncs on its own).

## Block 3: the demo company

"puebla el directorio con la productora de ejemplo" copies Faro Norte Producciones (fully fictional, every file marked DOCUMENTO FICTICIO) next to the real folder, never inside it. Its "today" is Monday 2026-10-06; the last sweep ran on 2026-09-29. The eight cards are built so that the bridge case exercises every rule: a preferred person with two valid certifications, a second principal who writes in English and whose course expires within the week, a third principal whose course expired, a non-principal who does the job, one undated course, one course with no document, one paused person. Details in `demo/README.md`.

## Block 4: the six use cases (phrase, then what appears)

| # | Say | What appears |
|---|---|---|
| 1 | "necesito un fotógrafo mañana a las 7:00 para las vigas del puente nuevo en la vía norte, exige curso de seguridad en obra" | a new file in `solicitudes/` with the shortlist Ariel (1), Bel (2), Greta (3) and the reason for each position; Dani excluded (course expired 2026-09-28) and Fausto excluded (undated course); three drafts, two in Spanish for Messenger and WhatsApp and one in English; an empty answers table |
| 2 | "Ariel no puede; Bel dijo que sí a las 3:40" | both answers logged with the time, Bel under "Quién quedó", the invite text drafted for a person to send, one dated fact on each of the two cards |
| 3 | "¿quién edita con detalle?" then "¿quién hace gráficas con texto?" | Emma Loiza with her card and the date as source; then Ariel excluded by his constraint, cited without repeating how it was first said |
| 4 | "corre el barrido" | `salidas/vencimientos-2026-10-06.md`: Dani expired, Bel within 7 days, Ariel's safety course and Fausto's heights course within 60 days, Fausto's safety course undated, Greta's safety course with no document; the index regenerated; the watermark advanced. Run it again: nothing changes |
| 5 | "Dani renovó su curso de seguridad en obra, vence el 2027-09-28" | the card updated with the old date under `## Historial`; a new bridge request now shortlists Dani again |
| 6 | "organiza la carpeta" (or run the scheduled audit) | the audit report in `salidas/auditorias/`: the two open gaps of `memoria.md`, the closed request checked, nothing deleted |

Optional: edit a card by hand in Drive (delete a heading), tell the agent, and watch the audit flag it and the repair keep every line.

## Block 5: surfaces and the routine

Google Drive is the backbone. Local sessions (Cowork, Claude Code) read the synced, offline-enabled folder; claude.ai web and the mobile app read and write the same folder through the Drive connector; the Monday sweep runs in the cloud from one account, reads every card and the certifications catalog, writes the expiry report, regenerates the index and advances the watermark, and writes only inside the folder. Google Calendar enters read-only: the shoot's date and clashes with what is already scheduled; the invite is sent by a person. Contract: people edit the cards and the agent re-reads before it writes; nothing is deleted; reliability is dated facts, never a score; limits are assignment constraints, never diagnoses; nothing leaves the agent toward the freelancers.

## Block 6: the five-minute pitch

1. The problem: whom to call for which job, who holds a valid safety course and who delivers on time lives in two heads; staffing a shoot is messaging everyone and waiting; when one of those two people is out, the pool is out with them.
2. Demo 1 (1 min): "a photographer tomorrow at 7, safety course required" becomes a shortlist in the team's order with the reasons, the exclusions with theirs, and one message per person in their channel and language.
3. Demo 2 (1 min): "Bel said yes at 3:40" becomes the log, who got it, the invite text and a dated fact on her card.
4. Demo 3 (1 min): the Monday report of certifications about to expire, and the same index on the phone with no computer on.
5. The three layers: the engine is shared and agnostic; the organization's rules, cards and requests never leave its own Drive.

Objections that come up, with the one-line answer grounded in the agent's rules:

- **"It does not send the messages, so what is the value?"** The value is the list: who can, in your order, filtered by the certification the job requires on that date, with the message already written in each person's language. Sending is one paste; deciding whom to ask was the hour.
- **"Our people are on WhatsApp groups."** Exactly where the drafts go: each card records the group or profile the coordinator uses, and the message comes out ready for that channel. The agent reads no group; the team pastes.
- **"We do not have certificates on file."** Then the first sweep shows it: every course without a date is "sin fecha" and never counts as valid, every course without a document is "sin soporte". The directory is how the file gets built, one card at a time.
- **"What if the coordinator leaves?"** The criteria that lived in their head are in the cards and the rules, with dates and authors; the next coordinator reads the folder, and the Monday sweep keeps running from whichever account the team assigns.
- **Privacy.** Nothing of the organization in the engine; the cards describe third parties, so limits are written as assignment constraints and reliability as facts, never diagnoses or scores; the folder's Drive permissions decide who can read and edit.
