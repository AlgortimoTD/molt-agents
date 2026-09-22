# templates/

What `cerebro-setup` fills to create an organization's brain. Everything here lands in the customer's folder, so it exists in the two languages the agent supports, `es/` and `en/`, with identical structure. The setup skill asks the language as its first, mandatory question, before creating anything, and picks one set; the choice is fixed from then on. No template carries data of any organization: every placeholder is `<like this>` and the interview fills it.

**One language, everywhere.** A brain born in English is English all the way down: folder and file names, headings, markers, decision states, role names and prose. The skills never carry a literal name; they resolve each one by key from the vocabulary block at the end of the brain's `CLAUDE.md`. The dictionary of keys, with the name of each in every language, is [vocabulary.md](vocabulary.md). The only language-neutral pieces are the marker `<!-- cerebro-operativo -->` on line 1 and the JSON keys of the state file.

Template file names are the same under `es/` and `en/` (they are maintainer-side names); what each becomes in the brain is the vocabulary key, whose name depends on the language.

| Template (same name under `es/` and `en/`) | Becomes (vocabulary key) | Filled by |
|---|---|---|
| `CLAUDE.root.template.md` | `CLAUDE.md` of the brain (line 1 is the marker; the vocabulary block closes it) | interview: organization, people and roles, clients' language |
| `config/empresa.template.md` | `company` | interview and the public site |
| `config/valores-y-negociables.template.md` | `values` | interview (the four blocks) and the documents |
| `config/fuentes.template.md` | `sources` | interview: meetings, time zone, roles, Drive permissions, routine account and time |
| `config/voz.template.md` | `voice` | `brand-voice-style-guide` |
| `bitacora.template.md` | `log` | as is |
| `playbook.template.md` | one file per process under `playbooks` | the documents first, then the interview, then the routine |
| `caso.template.md` | one file per case under `cases` | the chat, when a case is told |
| `memory.template.md` | `memory` | as is, plus the gap inventory at the end of the installation |
| `ultima-ingesta.template.json` | `state` | time zone from the interview |
| `reuniones-entrada-README.template.md` | `README.md` inside `meetings-inbox` | as is |
| `documentos-README.template.md` | `README.md` inside `documents` | as is |
| `salidas-README.template.md` | `README.md` inside `outputs` | as is |

The setup skill also copies the operating guide of the chosen language (`docs/es/como-operar-el-cerebro.md` or `docs/en/how-to-operate-the-brain.md`) to the `guide` path so it travels with the brain.
