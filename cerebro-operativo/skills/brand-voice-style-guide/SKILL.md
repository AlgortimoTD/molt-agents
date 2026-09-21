---
name: brand-voice-style-guide
description: >-
  v1.1.0 · Reverse-engineer a company's voice from the copy it already published and write it
  down as a one-page guide anything else can follow. Reads the site, the blog and the public
  social posts (plus any text the team hands over), and produces voz.md: tone axes with a
  position and evidence, do and do-not pairs taken from real sentences, banned phrases,
  vocabulary, and rewrite samples. Built for a brain folder, so the output is a file other
  skills consume, not a one-off answer. Use it when setting up a company brain, when copy
  sounds off-brand, or before letting anything write on a company's behalf. Triggers:
  "extract our brand voice", "build a voice and style guide", "make this sound like us",
  "why does this copy sound off", "extrae nuestra voz de marca", "arma la guía de estilo y
  voz", "haz que esto suene a nosotros", "esto no suena a nuestra marca". [v1.1.0]
---

# brand-voice-style-guide

## Version 1.1.0

Every company already has a voice; almost none has written it down. It lives in the way the
founder ends an email and in the words the team refuses to use, and it survives only as long
as the people who hold it. The moment something else writes on the company's behalf, that
voice either gets captured or gets replaced by the flat, agreeable register of generic
marketing copy.

This skill captures it from evidence. Not from asking the team to describe themselves, which
produces the voice they wish they had, but from reading what they actually published.

## The output is a file

You produce **one file**, normally `_config/voz.md` inside a brain folder. That matters more
than it sounds: the guide is consumed by other skills and by people drafting under time
pressure, so it has to be short enough to be read whole and specific enough to settle an
argument. A four-page essay on brand personality settles nothing.

When the destination folder has a `CLAUDE.md`, read it first for the company and the working
language. It outranks this skill on both.

## Language

The customer sets it, and there are three real cases. Ask if it is not already written in
`CLAUDE.md` or `_config/fuentes.md`:

- **One language.** The whole guide in it.
- **Two languages, same voice.** One guide, with the axes and rules once, and the examples in
  both. The rules generalize; the sentences do not.
- **Two languages, different registers.** This is common and easy to miss: a company whose
  site is in English and whose team works in Spanish often sounds more formal in one than the
  other. When the evidence shows it, say so explicitly and give each language its own axis
  positions. Flattening them into one average voice produces copy that is wrong in both.

Never default to your own language, and never assume the language of the site is the language
of the guide.

## How to build it

### 1. Gather evidence, and say where it came from

Read the home page and two or three interior pages, three to five of the most recent blog
posts, and ten to twenty recent social posts across the networks they actually use. Add
whatever the team hands over: proposals, client emails, decks. Their own text is the best
evidence there is, because a site is often written by somebody else.

Prefer recent material. A voice drifts, and a guide built on a 2019 site describes a company
that no longer exists.

If you cannot reach a source, write the guide from what you did reach and **name the gap** in
the file. A guide that hides its own thin spots gets trusted more than it deserves.

### 2. Read for patterns, not for adjectives

You are looking for things you can point at:

- Sentence length and rhythm. Short and declarative, or long and qualified?
- Person. "We" or the company's own name? Does it address the reader as "tú", "usted", "you"?
- Concreteness. Numbers, names and specifics, or abstractions and benefits?
- Warmth. Where does it sit between formal and familiar, and is it steady across channels?
- Humor, and of what kind, if any.
- Recurring words and constructions. Every company has a handful it reaches for.
- What it never does. Absences are evidence too: no exclamation marks, no hype adjectives, no
  emoji, no jargon.

"Professional and approachable" describes ninety percent of companies and helps nobody. "Opens
with the client's problem in the client's words, never with the company's credentials" is a
rule somebody can follow and check.

### 3. Write the guide

Use this structure. It is deliberately short.

```markdown
# Voz de <Company>

Fuentes: <urls and files read>, leídas el <YYYY-MM-DD>.
Faltó: <what could not be read, or "nada">.

## En una línea

<The voice in one sentence somebody could hold in their head while writing.>

## Ejes de tono

| Eje | Dónde está <Company> | Evidencia |
|---|---|---|
| Formal ... Cercano | Cercano, sin ser informal | "<real sentence from the site>" |
| Sobrio ... Entusiasta | Sobrio | "<real sentence>" |
| Abstracto ... Concreto | Concreto, siempre con un ejemplo | "<real sentence>" |

<Three to six axes. Each one carries a real sentence as evidence. An axis without
evidence is an opinion, and opinions are what this file exists to replace.>

## Sí y no

| Así sí | Así no | Por qué |
|---|---|---|
| "<real or close-to-real sentence>" | "<the same idea in the wrong voice>" | <one line> |

<Four to eight pairs. The "no" column is the one people learn from, so make it the
plausible wrong version, not a strawman.>

## Frases prohibidas

- <phrase> - <why: it is a cliché, it overpromises, it is not how they talk>

## Vocabulario

- Dicen: <their words for their own work>
- No dicen: <the industry words they avoid>

## Reescrituras de muestra

### Antes
<a generic paragraph>

### Después
<the same content in their voice>

### Qué cambió
<two or three lines: which axis moved and why. This is what teaches the rule.>
```

### 4. Check it against something it did not see

Take a piece of copy you did not use as evidence, rewrite it with the guide, and read both.
If the rewrite is merely shorter or merely friendlier, the guide is still describing generic
good writing and not this company. Go back for the specifics: the words they repeat, the
constructions they avoid, the thing they always put first.

## Done means

- Every tone axis carries a real quoted sentence as evidence.
- The banned phrases and the vocabulary come from what the company avoids and uses, not from
  general taste.
- At least one full before and after rewrite, with the reasoning.
- The sources and the gaps are named at the top, with the date they were read.
- The whole thing fits on one page a person will actually read.
- A person from the company reads a rewrite and recognizes it as theirs. That is the only test
  that matters, and it is worth asking for explicitly.

## What makes these guides fail

They describe a voice instead of constraining one. The tell is a guide you could hand to a
different company in the same industry without changing a word. If that is true of yours,
it has no evidence in it yet.
