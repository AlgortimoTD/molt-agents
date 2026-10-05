# templates/

What `directorio-freelancers-setup` fills to create an organization's directory. Everything here lands in the customer's folder, so it exists in the two languages the agent supports, `es/` and `en/`, with identical structure. The setup skill asks the language as its first, mandatory question, before creating anything, and picks one set; the choice is fixed from then on. No template carries data of any organization: every placeholder is `<like this>` and the interview fills it.

**One language, everywhere.** A directory born in English is English all the way down: folder and file names, headings, data fields, request states, expiry tiers, role names and prose. The skills never carry a literal name; they resolve each one by key from the vocabulary block at the end of the directory's `CLAUDE.md`. The dictionary of keys, with the name of each in every language, is [vocabulary.md](vocabulary.md). The only language-neutral pieces are the marker `<!-- directorio-freelancers -->` on line 1 and the JSON keys of the state file.

Template file names are the same under `es/` and `en/` (they are maintainer-side names); what each becomes in the directory is the vocabulary key, whose name depends on the language.

| Template (same name under `es/` and `en/`) | Becomes (vocabulary key) | Filled by |
|---|---|---|
| `CLAUDE.root.template.md` | `CLAUDE.md` of the directory (line 1 is the marker; the vocabulary block closes it) | interview: organization, people and roles, language |
| `config/empresa.template.md` | `company` | interview: who they are, who coordinates production, who approves additions and removals, time zone |
| `config/reglas-de-asignacion.template.md` | `rules` | interview: job types, principals and preferred person per type, request mode and wait window, certification per job type, what to do when nobody answers |
| `config/certificaciones.template.md` | `certifications` | interview: the certifications the organization recognizes, typical validity, who requires each, notice tiers |
| `config/plantillas-de-mensaje.template.md` | `message-templates` | interview: tone per channel and language, what a message always carries |
| `config/fuentes.template.md` | `sources` | interview: routine account and time (the literal prompt is already there), calendar read, Drive permissions per role |
| `ficha.template.md` | one file per freelancer under `freelancers` | the interview and a pasted list first, then every request and shoot, then the coordinator |
| `solicitud.template.md` | one file per shoot under `requests` | `availability-request-drafter` |
| `memoria.template.md` | `memory` | as is, plus the gap inventory at the end of the installation |
| `ultimo-barrido.template.json` | `state` | time zone from the interview |
| `soportes-README.template.md` | `README.md` inside `supports` | as is |
| `salidas-README.template.md` | `README.md` inside `outputs` | as is |

The setup skill also copies the operating guide of the chosen language (`docs/es/como-operar-el-directorio.md` or `docs/en/how-to-operate-the-directory.md`) to the `guide` path so it travels with the directory. The `index` and the `expiry-report` have no template: the sweep writes them from the cards.
