# <Agent name>

<Two or three sentences: what the agent does, for whom, on top of what storage.>

## What it does

- **<Activity>** (`<skill>`): <one line>.
- **Recurring order** (`<agent>-audit`): weekly routine that restores order and polices the agent / context separation.
- **Zero-friction install** (`<agent>-setup`): "quiero instalarlo" mounts everything; the user never runs a command.

## The three layers

| Layer | Where it lives | Shared |
|---|---|---|
| The engine (skills, templates, routine) | this plugin | yes, 100 percent agnostic |
| The organization's context (`CLAUDE.md`, `_config/`, `memory.md`) | the organization's own Drive folder | no |
| The organization's records | the same folder | no |

## Installation

Paste this in a chat of Claude Code or the Claude desktop app (the folder open as the project), approve the permission prompts, and when it answers "listo" say **"quiero instalarlo"**:

> "Instala <agent name in the user's words>. Viene del marketplace AlgortimoTD/molt-agents, plugin <agent-slug>. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos."

claude.ai (web and mobile): Customize, Plugins, Add marketplace, Add from a repository, `AlgortimoTD/molt-agents`, Sync automatically, Add.

## Try it with the demo organization

Say **"puebla <agent> con la empresa de ejemplo"**: a fully fictional organization ([demo/](demo/README.md)) with enough state to run every use case, plus an inbox whose ingestion shows the before and after. Delete the folder when done.

## Requirements

None on the computer. Connectors: <list>. Cloud sessions (claude.ai, mobile) need nothing installed.

## What it does NOT do

<The agent's "does not" lines, as sold.>
