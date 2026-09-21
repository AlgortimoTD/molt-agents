# templates/

What `cerebro-setup` fills to create an organization's brain. Everything here lands in the customer's folder, so it is written in the customer's language (Spanish by default; the setup skill produces it in the language the organization fixes) and carries no data of any organization: every placeholder is `<así>` and the setup interview fills it.

| Template | Becomes | Filled by |
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

The setup skill also copies `docs/como-operar-el-cerebro.md` into `salidas/` so the operating guide travels with the brain.
