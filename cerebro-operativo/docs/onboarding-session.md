# Team onboarding session: install the operating brain, seed it, demo it

A two-hour hands-on session for a team that will install the **cerebro-operativo** agent on their own computers, populate it with the fictional demo organization, run the use cases, and leave able to demo it to a prospect. Facilitator: whoever built the agent. Attendees: 3 to 8 people, each with their own laptop.

## Before the session (the day before)

Each item is the attendee's own click; Claude cannot do it for them:

1. A Claude account with **Claude Code** access, signed in on the **Claude desktop app** (the Code tab visible next to Chat). Nobody opens a terminal at any point.
2. **Google account + Google Drive for Desktop** installed and syncing (the drive letter or `~/Google Drive` visible).
3. Nothing else. The brain has no local dependencies. The repository `AlgortimoTD/molt-agents` is public, so no GitHub account either.

## Agenda (120 minutes)

| Block | Minutes | Outcome |
|---|---|---|
| 1. What it is | 10 | Facilitator demo on the demo organization: one transcript processed, one "how do we handle this" answered with sources. The three layers explained. |
| 2. Install | 20 | Every laptop has the plugin, a brain folder in Drive, and has run "quiero instalarlo" to the first heartbeat. |
| 3. Seed the demo organization | 10 | "puebla el cerebro con la empresa de ejemplo": two playbooks, a decision log, a case, and one transcript not yet processed. |
| 4. Use cases | 45 | Each attendee runs at least four of the six use cases below on their own machine. |
| 5. Surfaces and the routine | 15 | Facilitator shows the same folder from the phone (Drive connector) and the scheduled daily routine. |
| 6. Sales script | 20 | The five-minute pitch, the objections, and who will run the first prospect demo. |

## Block 2: install (zero commands, everything from the Code tab)

1. Create the brain folder in Drive (for example `Cerebro <empresa>\`) and mark it available offline.
2. Open the Claude desktop app, **Code** tab, *Open project*, pick that folder.
3. Paste this message in the chat and approve the permission prompt(s):

   > Instala el cerebro operativo de mi empresa. Viene del marketplace AlgortimoTD/molt-agents, plugin cerebro-operativo. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos.

   Click alternative: `/plugin`, Marketplaces, Add, `AlgortimoTD/molt-agents`, Discover, cerebro-operativo, Install.
4. In the same chat say **"quiero instalarlo"**. `cerebro-setup` takes over: Drive integration, root `CLAUDE.md` and `_config/` through the interview, the voice guide, the daily routine, the first transcript processed end to end. For claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add, plus the Google Drive connector.

After a release, ask in the chat: *actualiza el plugin cerebro-operativo* (claude.ai syncs on its own).

## Block 4: the six use cases (phrase, then what appears)

| # | Say | What appears |
|---|---|---|
| 1 | "procesa el transcript que está en entrada" | a file in `reuniones/`, new lines in `decisiones/bitacora.md`, one playbook section rewritten with the previous text under `## Historial`, one inference left "por confirmar", and `salidas/ingesta-<fecha>.md` |
| 2 | "¿cómo manejamos un cliente que maltrata al equipo?" | the values that apply, what is negotiable and what is not, the closest documented case, and the source (file and date) of every claim |
| 3 | "¿qué decidimos sobre las propuestas?" | the decision log line with its date and source meeting, and the playbook section it changed |
| 4 | "escribe este correo con nuestra voz" | a draft following `_config/voz.md`, marked "para revisar antes de enviar" |
| 5 | "esa decisión quedó mal, corrígela" | a new correcting line in the log, the playbook restored from its history, the wrong text kept as record |
| 6 | "organiza la carpeta" (or run the scheduled audit) | the audit report in `salidas/auditorias/` |

Optional: run use case 1 a second time on the same transcript and show that nothing changes (the watermark).

## Block 5: surfaces and the routine

Google Drive is the backbone. Local sessions (Cowork, Claude Code) read the synced, offline-enabled folder; claude.ai web and the mobile app read and write the same folder through the Drive connector; the daily routine runs in the cloud from one account, reads the watermark, fetches the new internal meetings from Fathom (or finds nothing and says so), and writes only inside the folder. Contract: only the routine writes playbooks and the log; nothing is deleted; only explicit decisions enter.

## Block 6: the five-minute pitch

1. The problem: how a company does things lives in two founders' heads and in a daily call nobody records; when one of them is out, years of judgment are out with them.
2. Demo 1 (1 min): a meeting transcript becomes a decision with date, reason and the playbook it changed, without anyone writing anything.
3. Demo 2 (1 min): "how do we handle this" answered with the company's values, its negotiables, the closest past case and the source, in the company's voice.
4. Demo 3 (1 min): the same folder on the phone; the routine ran at lunchtime with no computer on.
5. The three layers: the engine is shared and agnostic; the organization's context and records never leave its own Drive.

Objections that come up: privacy (nothing personal in the engine; records stay in the organization's Drive with its own permissions; the agent never writes outward), "what if it invents a policy" (only explicit decisions enter, everything cites file and date, what is not written is declared), "we do not have Fathom" (a pasted transcript does the same job; Fathom is optional and the free plan is enough), cost (a Claude subscription and a Google account), "do I need a computer on" (no: the routine runs in the cloud, cloud surfaces work alone).
