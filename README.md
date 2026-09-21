# Molt agents

Catalog and distribution marketplace of the agents Molt sells through Orbital: one Claude plugin per agent, installable from Claude Code, the Claude desktop app (Cowork) and claude.ai, and kept up to date by syncing this repository.

## How this repository works

- Each agent is a plugin in its own folder, registered in `.claude-plugin/marketplace.json`.
- The engine of every agent (skills, templates, docs, demo data) lives here and contains nothing personal: no names, emails, phone numbers or rules of any customer. Everything specific to an installation lives in the customer's own folder, never in this repository.
- The source of truth for every skill is the Molt skill registry (`catalogs/global/<slug>/skill/` in the platform monorepo). The `skills/` folder of each plugin holds stamped copies produced by the release script; it is never edited by hand, and a hand edit is overwritten by the next release.
- Updates reach every installation through the marketplace sync, so releases stay small and deliberate.
- An agent with a backend of its own (schema, provisioning) lives in its own repository and is only cataloged here.

## Installing an agent

Claude Code and the Claude desktop app: paste the agent's bootstrap message in a chat (each plugin's README carries it), or run:

    claude plugin marketplace add AlgortimoTD/molt-agents
    claude plugin install <agent>@molt-agents

claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add. The repository is public, so no GitHub App grant is needed.

## Catalog

| Agent | What it does | Status |
|---|---|---|
| [`cerebro-operativo`](cerebro-operativo/) | Operating brain for an organization: playbooks and a decision log kept current from recorded meetings, answers to "how do we handle this" with sources, drafts in the company's voice | Engine scaffolded (templates, docs, demo); skills pending their first release |

## Conventions

- Files are LF (`.gitattributes`) and written in English; user-facing trigger phrases and messages stay in the users' language because they are data, not documentation.
- No em dashes, no secrets, no personal data. Every release passes those three gates before it is pushed.
