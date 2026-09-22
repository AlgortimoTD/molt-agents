# Methodology: sold agents packaged as plugins

How Molt builds, packages, ships and maintains the agents it sells through Orbital. Adapted from the `Ntobon/agents` methodology (three-layer architecture, plugin tied to the repository, zero-command onboarding) and from the review of its `health` plugin, whose two execution gaps this document closes by design.

## 1. What an agent is here

An agent is **a folder that is both a plugin and a product**: a `CLAUDE.md` that orchestrates, one skill per activity under `skills/`, templates that produce the customer's context files, fictional demo data, the operating guide and the team onboarding session, and the plugin manifest that installs and updates it from this repository.

An agent is sold as a row of Orbital's agent catalog (`orbital.agt_agents`, curated, usually cross-industry). This repository is how that row reaches a customer's machines.

## 2. Three layers (the golden rule)

| Layer | What it is | Where it lives | Shared |
|---|---|---|---|
| The engine | skills, templates, docs, demo, the routine prompt | this repository | yes, 100 percent agnostic |
| The instance | the customer's filled `CLAUDE.md`, `_config/*`, execution state, the memory file | the customer's own folder (Google Drive) | never |
| The data | the customer's records (playbooks, logs, cases, meetings, outputs) | the same folder | never |

**Nothing personal outside the customer's folder.** If a skill needs a customer fact (who approves what, which language, which meetings count), it reads it from `_config/` of the folder it runs in. It never carries it written. There is no `local/` layer on the machine: everything that is instance lives in the customer's folder, so the phone and the desktop see the same thing.

Repository language: everything committed here is English. What lands in the customer's folder (templates, operating guide, demo data) and every user-facing trigger phrase stays in the users' language, because it is data.

## 3. Repository layout

```
molt-agents/
├── .claude-plugin/marketplace.json     one entry per plugin
├── README.md · METHODOLOGY.md          catalog and this document
├── template/                           the starting point of every new agent
├── scripts/release.sh · check.sh       stamp skills from the registry; run the gates
└── <agent>/
    ├── .claude-plugin/plugin.json
    ├── CLAUDE.md                       what it is, bootstrap contract, use-case map, rules
    ├── README.md                       what it does, three layers, bootstrap message, requirements
    ├── skills/<slug>/                  stamped copies, never hand-edited (section 7)
    ├── templates/                      what the setup skill fills for the customer
    ├── demo/                           the fictional organization (section 8)
    └── docs/                           operating guide and onboarding session
```

## 4. Distribution: plugin tied to the repository

The plugin is associated with this public repository with automatic sync: every release updates every installation. Per surface:

| Surface | Install | Update |
|---|---|---|
| Claude Code and the Claude desktop app (Cowork reads the same install) | paste the agent's bootstrap message, or `claude plugin marketplace add AlgortimoTD/molt-agents` + `claude plugin install <agent>@molt-agents` | `claude plugin update <agent>` |
| claude.ai (web and mobile) | Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add | automatic |

The repository is public, so no customer has to grant the Claude GitHub App. Releases stay small because a push reaches every customer at once.

## 5. Zero-command onboarding: the `<agent>-setup` skill

Installation is designed for a person who may know nothing about computers. The user does not run commands, create folders or edit files. Claude executes everything executable and asks only for the clicks that depend on the person's identity (accounts, sign-ins, connector authorizations). Claude never asks for or types passwords, and never names a language, package, repository or error code to the person.

Structure: Phase 0 silent diagnosis (idempotent, skips what exists); storage backbone; environment (nothing to install by default, see section 11); root context from the templates through a guided interview; plugin verification; scheduled routine; a live first heartbeat that proves the system works end to end. Plus a demo mode that seeds the fictional organization.

**The bootstrap message.** The setup skill lives inside the plugin, which does not exist yet on a fresh machine. The way in is one sentence the person pastes in a clean session, written as copy: it names the marketplace and the plugin (exact identity), authorizes whatever the agent needs to work, and fixes the output contract ("do not explain the technical details"). A plain session honors it, installs the plugin and answers "listo" plus what to say next. Every agent's README carries its bootstrap message.

## 6. The bootstrap contract (finding the customer's folder)

Every skill resolves the customer's folder the same way before working, in this order:

1. The working folder has a `CLAUDE.md` whose first line is the agent's marker (for example `<!-- cerebro-operativo -->`). Cowork and Claude Code with the project open.
2. Otherwise, the platform memory holds `<agent>: <folder name or path in Drive>`. Mobile and claude.ai through the Drive connector.
3. Otherwise, ask once ("what is your folder called in Drive?") and save it to memory.

The setup skill writes the marker as the first line of the customer's `CLAUDE.md`. The marker is also what lets Phase 0 recognize an existing installation instead of recreating it.

## 7. Skills: one source of truth, two packages

The source of truth of every skill is the Molt skill registry, vendored in the platform monorepo at `catalogs/global/<slug>/skill/`. It is written with `skill-creator`, reviewed (area and security) and published there. Orbital grants skills to customers through entitlements from that registry.

This repository holds **stamped copies** of the same folders, produced by `scripts/release.sh`, which copies `catalogs/global/<slug>/skill/` into `<agent>/skills/<slug>/` and bumps the plugin version. Nobody edits `skills/` here by hand; a hand edit is overwritten by the next release. A skill never exists in two editable places.

## 8. Demo data

Every agent ships a fully fictional organization under `demo/`, marked "DOCUMENTO FICTICIO" in every file: enough state to run every use case, plus an inbox whose ingestion produces a visible before and after in minutes. Demo data is seeded next to a real installation, never inside it, and deleted when done. A privacy grep of `demo/` returns no real person, company or client.

## 9. The onboarding session

`docs/onboarding-session.md` is a two-hour team session: install from the bootstrap message, seed the demo, run the use cases as exact phrase and visible result, see the same folder from the phone, close with the five-minute pitch and its objections. It is sales enablement material, versioned next to the code.

## 10. The audit skill: the engine defends itself

Every agent has a recurring audit skill with two blocks. On the customer's archive: loose files, stale state, inconsistencies between records. On the engine itself: if a name, phone, email or customer rule appears inside a skill or template, it is moved to the `_config/` of the folder where it runs, the generic reference stays, and the extraction is recorded. Productization erodes one urgent edit at a time; this is the mechanism that reverts it.

## 11. Dependencies: none by default

Agents here are Markdown, JSON state, connectors and scheduled tasks. No Python, Node or converters on the customer's machine. If a skill ever needs a script, it declares its dependencies in a manifest versioned in the engine and installs them outside the plugin's version folder (the installed plugin lives at a path that includes its version, so anything installed inside it disappears at the first update). The setup skill then gains an invocable self-check instead of a prose promise.

## 12. Fit with the Orbital catalog

- The agent exists as a **curated** row of `orbital.agt_agents` (`origin = curated`, `visibility = listed`, usually `is_cross_industry = true`), promoted through the curator with its `does`, `does_not`, bundled skills, business area and pricing tier.
- The row's `metadata` records the marketplace and plugin that deliver it and the bootstrap message, so the engagement's `agent_install` task has something to show.
- A customer who buys it gets `build_state = ready` and an `agent_install` task. The installation is the bootstrap message plus the setup skill. Molt accompanies the configuration interview in the first three instances of each agent.
- A generated agent that a deal produced (`origin = deal_generated`) can become the seed of a catalog agent by splitting it into layers (section 2) and following the checklist below; the deal's instance then adopts the engine through the setup skill's Phase 0.

## 13. Checklist: a new agent

- [ ] Copy `template/` to `<agent>/` and fill the manifest.
- [ ] Audit the seed installation: separate engine, instance and data; pull everything personal into templates with placeholders.
- [ ] Write the skills with `skill-creator` in the monorepo (`catalogs/global/<slug>/skill/`), review and publish them; never a hand-written `SKILL.md` here.
- [ ] Write the `<agent>-setup` skill with the phases of section 5 and a demo mode, and the audit skill of section 10.
- [ ] Write the `CLAUDE.md` with the bootstrap contract (section 6), the use-case map and the hard rules.
- [ ] Write the README with the bootstrap message; write `docs/` and `demo/`.
- [ ] Run `scripts/release.sh <agent>` and `scripts/check.sh`; register the plugin in `marketplace.json`.
- [ ] Create the catalog row and promote it (section 12).
- [ ] Install it on a teammate's machine from the bootstrap message alone; fix what they had to ask; repeat once.

## 14. Gates before every push

LF endings, no em dash (U+2014) or en dash (U+2013), no secrets, no personal data, valid manifests, and every `skills/<slug>` matching a published registry version. `scripts/check.sh` runs them; CI runs it on every push and pull request.
