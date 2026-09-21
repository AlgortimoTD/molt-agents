# templates/

What `cerebro-setup` fills to create an organization's brain. Everything here lands in the customer's folder, so it exists in the two languages the agent supports, `es/` and `en/`, with identical structure. The setup skill detects the language of the person's first interaction, confirms it with an explicit question, and picks one set; that language is then written in the brain's `CLAUDE.md` and `_config/fuentes.md`, where every skill reads it. No template carries data of any organization: every placeholder is `<like this>` and the interview fills it.

**Canonical tokens, identical in both languages.** The skills navigate the folder by names, so these never change with the language: folder and file names (`_config/empresa.md`, `_config/valores-y-negociables.md`, `_config/voz.md`, `_config/fuentes.md`, `playbooks/`, `decisiones/bitacora.md`, `casos/`, `reuniones/`, `reuniones/entrada/`, `salidas/`, `_estado/ultima-ingesta.json`, `memory.md`), the `## Historial` heading of a playbook, the `<!-- Vigente desde AAAA-MM-DD -->` marker, and the decision states `aplicada`, `por confirmar`, `propuesta`, `abierta`, `revertida`. The English templates keep them and explain them once. Everything else is prose in the organization's language.

| Template (same name under `es/` and `en/`) | Becomes | Filled by |
|---|---|---|
| `CLAUDE.root.template.md` | `CLAUDE.md` of the brain (line 1 is the marker `<!-- cerebro-operativo -->`) | interview: organization, roles, language |
| `config/empresa.template.md` | `_config/empresa.md` | interview and the public site |
| `config/valores-y-negociables.template.md` | `_config/valores-y-negociables.md` | interview (the four blocks) |
| `config/fuentes.template.md` | `_config/fuentes.md` | interview: meetings, time zone, language, approvals, routine account and time |
| `config/voz.template.md` | `_config/voz.md` | `brand-voice-style-guide` |
| `bitacora.template.md` | `decisiones/bitacora.md` | as is, with the approver's role |
| `playbook.template.md` | `playbooks/<proceso>.md`, one per process the organization names | interview, then the routine |
| `caso.template.md` | `casos/<AAAA>-<cliente>.md` | the chat, when a case is told |
| `memory.template.md` | `memory.md` | as is |
| `ultima-ingesta.template.json` | `_estado/ultima-ingesta.json` | time zone from the interview |
| `reuniones-entrada-README.template.md` | `reuniones/entrada/README.md` | as is |
| `salidas-README.template.md` | `salidas/README.md` | as is |

The setup skill also copies the operating guide of the chosen language (`docs/es/como-operar-el-cerebro.md` or `docs/en/how-to-operate-the-brain.md`) into `salidas/` so it travels with the brain.
