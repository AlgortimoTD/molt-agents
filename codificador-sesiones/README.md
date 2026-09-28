# Codificador de sesiones de investigación

A **qualitative session coder** for a research team, run by Claude on top of a Google Drive folder: every interview or focus group becomes a coded session (per participant and variable, the category and the verbatim quote with its minute), the matrix grows in the team's own format, and variables are crossed step by step with a pause for the researcher at each step. Calibrated on a study the team already coded by hand, so the result looks like their work.

## What it does

- **Codes each session** (`qualitative-session-coder`): reads the transcript from Fathom or from the study's inbox, the codebook, the team's format and criteria and a hand-coded example, and writes the session file and the matrix rows, every code with its quote and minute. Emergent categories are proposed with evidence and wait for a researcher.
- **Keeps the codebook in the team's hands** (same skill): accept, reject, add, rename or retire a category by asking in the chat; every change is dated in the codebook's history, nothing is deleted.
- **Runs the fidelity test** (same skill): codes a session of the example study and compares it with the team's hand coding, difference by difference.
- **Crosses variables in steps** (`cross-variable-analyzer`): frequencies by group with their n, candidate relations with three quotes each, a summary tied to the study's hypotheses; it stops after each step and records what the researcher decided.
- **Installs itself** (`codificador-sesiones-setup`): creates the folder, interviews the team, takes their formats and an example study, loads the current study, checks Fathom and codes a first session. The user never runs a command.

## The three layers

| Layer | Where it lives | Shared |
|---|---|---|
| The engine (skills, templates, demo) | this plugin | yes, 100 percent agnostic |
| The team's context (`CLAUDE.md`, `_config/`, `_ejemplos/`) | the team's own Drive folder | no |
| The studies (codebooks, sessions, matrix, crosses) | the same folder | no |

## Working at the same time

The folder lives in a shared Drive; Google Drive for desktop makes it a local folder on each researcher's machine, and Cowork or Claude Code open it as a project. Each coded session is its own file and the matrix is regenerated from them, so several researchers can code different sessions at once without overwriting each other. Changes to the codebook are made through the chat, one at a time, each with its date.

## Installation

In Claude Code or the Claude desktop app (Cowork), with the future research folder open as the project, paste this and approve the permission prompts:

> "Instala el codificador de sesiones de investigación. Viene del marketplace AlgortimoTD/molt-agents, plugin codificador-sesiones. Deja listo todo lo que necesite para funcionar y avísame cuando esté, sin explicarme los detalles técnicos."

When it answers "listo", say **"instala el codificador"**. CLI users: `claude plugin marketplace add AlgortimoTD/molt-agents` and `claude plugin install codificador-sesiones@molt-agents`.

Each researcher installs the plugin on their own machine with the same message; the folder is shared once.

## Try it with the demo study

Say **"puebla el codificador con el estudio de ejemplo"**: a fully fictional team and study ([demo/](demo/README.md)) with an example coded by hand, one coded focus group and one waiting in the inbox. Coding it adds rows with their quotes, raises one category proposal and shows an unattributed turn handled honestly. Delete the folder when done.

## Operating guide

[docs/es/como-operar-el-codificador.md](docs/es/como-operar-el-codificador.md): coding a session, pasting a transcript, changing the codebook, crossing variables, running the fidelity test.

## Requirements

Google Drive for desktop on each researcher's machine. Connectors: Google Drive; Fathom (optional, read only; its free plan is enough).

## What it does NOT do

- It does not write the final report or decide which findings matter to the client.
- It does not moderate sessions or replace the researcher's judgment.
