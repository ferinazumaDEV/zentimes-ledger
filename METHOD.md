# Method — how this ledger measures

**Author:** Fernando Aporta Franco (ferinazumaDEV / Zentimes) · **Written:** 2026-09-23 · **Instrument version:** The GEO Cookbook v0.1.4

This file states what produces every number in this repository, what each number means, what it does not
mean, and which checks a number has to survive before it is written down. It is the contract the
[audits](audits/), the [criteria captures](criteria/) and the [operations records](operations/) follow. If a
document in this repository disagrees with this file, the document is wrong and gets corrected.

## 1. The instruments

Every metric that carries a metric id comes from **one of the six recipes of The GEO Cookbook, pinned at tag
`v0.1.4`**, and from nothing else:

| | |
|---|---|
| Tag | <https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/releases/tag/v0.1.4> (released 2026-09-22) |
| Version DOI | [10.5281/zenodo.22890558](https://doi.org/10.5281/zenodo.22890558) — this exact state of the six recipes |
| Concept DOI | [10.5281/zenodo.22299279](https://doi.org/10.5281/zenodo.22299279) — always the latest release; **not** what this ledger measures with |
| Licence of the cookbook | CC BY 4.0 prose, MIT code samples (its own `LICENSE` and `LICENSES/MIT.txt`) |

The recipes are executed **unmodified**. A recipe reads files, not URLs, so measuring a live page means:
copy the recipe directory, write the public file (`curl` of the page, of `robots.txt`, of `llms.txt`, or the
page converted to markdown) into its `before/`, run the recipe's **own** `reproduce.sh --json`, and read
`before_value`. Nothing in a recipe is re-implemented for a number that carries that recipe's metric id. The
two helper scripts in [`tools/`](tools/) that touch a recipe do exactly this and nothing more; the two that
restate a definition (`count-jsonld.py`, `check-sitemap-pages.py`) say so in their docstring and are not the
source of any number that carries a cookbook id.

**The copy is the tag tarball, never a working checkout.** On 2026-09-23 a working copy of the repository whose
branch pointer said `v0.1.4` had a working tree that was older than its own HEAD: five of the six `reproduce.sh`
predated the audit fixes of 2026-09-12/13, and it reported 524 words for the zentimes.es home page where
v0.1.4 reports 526 (the old filter left numeric character references such as `&#x27;` in place; v0.1.4 turns
every entity, named or numeric, into a space). The reproduction commands in every audit therefore start with
the tag tarball, and a copy is trusted only after `diff -q` of each `reproduce.sh` against that tarball:

```sh
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)
```

Numbers that no recipe defines (sitemap URL count, `hreflang` presence, `@id` census, HTTP status, HSTS
header, meta description length, anchor existence) are produced by `curl`, `grep`, `perl` and Python 3's
standard library, with the command printed beside the number. They carry **no cookbook metric id**, so
nobody can mistake them for a recipe's measurement.

## 2. The six recipes: what each one measures, and its evidence class

Read from each recipe's `meta.yml` at v0.1.4. All six have `method: deterministic-offline`,
`requires_llm: false`, `requires_network: false`: the number is re-derived with no model and no network from
the files placed in `before/`.

| Recipe (path in v0.1.4) | Metric id(s) in `--json` | What the number counts | `evidence_class` | `limitations` (verbatim from `meta.yml`) |
|---|---|---|---|---|
| `04-technical/ssr-vs-csr-rendering` | `words_visible_no_js` | whitespace-separated words left in the HTML source after removing `<script>`, `<style>`, comments, every tag and every character entity; `<noscript>` content is kept | `technical-seo` | "Measures the mechanical visibility of the text to a fetch-only crawler, not whether any answer engine cites the page." |
| `04-technical/structured-data-jsonld` | `typed_facts` · `typed_entities` | objects carrying `@type` in the page's `application/ld+json` blocks (nested included; a list of types is one entity), and keys other than `@context`/`@type` on those objects | `aeo` | "Measures the extractability of typed statements from the page source, not whether any answer engine cites the page." |
| `04-technical/ai-crawler-access` | `ai_user_agents_allowed` (of 8) · `llms_txt_bytes` | of eight AI-related `robots.txt` tokens, how many may fetch `/` under RFC 9309 (wildcards, `$`, longest match, `Allow` wins ties); and the size in UTF-8 **bytes** of `llms.txt` | `technical-seo` | "Measures a precondition (declared access and an extractable feed), not whether any answer engine retrieves, indexes or cites the page. The eight tokens are not eight HTTP crawlers […]" |
| `03-content/chunk-friendly-structure` | `self_contained_chunks` / `chunks_produced` | chunks from a recursive character splitter (`chunk_size = 800`, no overlap) that start clean (heading, list or quote mark, capital or digit) and end clean (`.` `!` `?` `:` or a heading line) | `geo-precondition` | "Measures a machine-legibility proxy (whether a chunk stands alone after fixed-size splitting), not whether any answer engine cites the page." |
| `05-authority/entity-clarity-sameas` | `entities_resolved` / `entities` | named entities in the page's `about` list whose `@id` or `sameAs` holds exactly one Wikidata `Q<n>` URL (host and path checked; `P…` ids and lookalikes do not count) | `geo-precondition` | "Measures the mechanical resolvability of each name to one canonical identifier, not whether any answer engine cites the page." |
| `06-measurement/citation-anchoring` | `claim_source_pairs` / `claims` | markdown list items inside `<!-- claims:start -->…<!-- claims:end -->` (the whole document if the markers are absent) that carry at least one inline `[text](http…)` link; code spans, fences, images, bare and relative URLs do not count | `geo-precondition` | "Measures how many claim-to-source pairs a parser can lift from the document, not whether any answer engine cites the page." |

`evidence_class` is defined in the cookbook's `dataset/SCHEMA.md` (schema version 2). It is **not** a
confidence rating and does not grade how well anything was measured. It separates whether the measured
property **is the deliverable** or is **one step short** of an outcome nobody has observed:

- `technical-seo` — the property is itself the outcome of technical SEO; anyone reproduces it with `curl`
  and the job is done (a fetch-only crawler reads *n* words: that *is* readability).
- `aeo` — the same for answer surfaces: the property is what an answer engine consumes (a schema.org
  parser extracts *n* typed facts).
- `geo-precondition` — measured just as directly, but it shows the artifact is *ready* to be retrieved,
  resolved or cited, not that it is.

And the sentence of that schema that travels with every class: **"No row, in any class, measures retrieval,
reranking, generation or citation by an answer engine."**

The cookbook's `INSTRUMENTS.md` records that two of these instruments were wrong for weeks while reproducing
their published numbers perfectly (the robots matcher treated `*` and `$` as literal text; the Wikidata matcher
accepted any string that *contained* a Q-id). Reproducing a number proves the instrument is deterministic, not
that it measures what its name says. That is why this ledger pins the tag that carries the fixes and why the
controls in §5 exist.

## 3. Why labels grade preconditions and never citation

The public inspector on zentimes.es (<https://zentimes.es/tools/ai-inspector/>) prints one label per check —
`excellent / strong / good / low / none`, plus an unrated state — with the rule that decides it, the
discipline it belongs to, a criteria version and the command that reproduces the value. The captured rule
sets are in [`criteria/`](criteria/). Three things fix what a label may say:

1. **The cookbook grades every engine effect as `experimental`.** `CLAIMS.md` of v0.1.4: the measured
   property of each recipe is `established` (deterministic, re-runnable by anyone), the engine effect is
   `experimental` for all six — "no recipe measures retrieval, reranking, generation or citation by any
   engine". A grade moves only with a dated measurement of an engine, with the named model, N and seed, and
   the noise floor acknowledged (repeated identical queries cite different sources within a day,
   [arXiv:2604.07585](https://arxiv.org/abs/2604.07585), the primary source the cookbook cites for why a small
   live test cannot settle the effect).
2. **The schema forbids the claim structurally.** `evidence_class` is a closed vocabulary of three values,
   enforced by the cookbook's `build.sh` and `validate.py`; none of the three means "cited". The inspector's
   fourth class, `security`, is its own and is filed as such in the captures.
3. **The inspector says it on the page**, above the form and on every report: *"no check measures whether an
   AI cites you, which is the engine's decision and nobody outside it controls."*

So a label grades a **precondition of legibility** — the page arrives with its words, its facts are typed,
its crawler policy is declared, its chunks stand alone, its claims carry a source — and the rule behind the
label is published so that the label can be re-derived by hand. Two further rules keep labels honest:

- **Merit thresholds on proxies are not defended; pathologies are.** No data ties a word count to an
  outcome, so words without JavaScript flag only the clear case (under 50 words on a page that looks full)
  and are otherwise printed unrated. The same for the number of `sameAs` links. When a bar is not raised,
  the reason is printed in the rule.
- **One identifier, one definition.** A card that reuses a cookbook metric id (`words_visible_no_js`,
  `typed_entities`, `ai_user_agents_allowed`, `llms_txt_bytes`) uses the recipe's files, agent list and unit.
  A card that needs a different grouping (the four assistants that *search to answer*, rather than the
  recipe's eight tokens) gets its own name, so one id never carries two meanings. Rules that share a
  discipline but not a metric say so ("same class as the cookbook's chunking recipe, not its metric").

## 4. The cross-check discipline

An inspector that claims to match the cookbook is claiming something measurable. The claim is tested, not
read, and the test has four parts:

1. **Same URL, same instant.** The recipes and the inspector run on `https://zentimes.es/` within the same
   window; the recipe side is the recipe's own `reproduce.sh --json` on the live files.
2. **Tagged values, never prose.** The inspector exposes each shared metric as `data-metric` / `data-value`
   attributes; the comparison reads those. A number that has to be pulled out of prose with a regular
   expression is a number someone will pull out wrong (the first parser swallowed the `04` of
   `04-technical/` and reported three fours).
3. **A dated statement that names the version.** The result is written as *"cross-checked 2026-09-23
   (13:32Z) against cookbook v0.1.4, 4 of 4 equal"* — with the values (526 · 9 · 8 · 9 484). The date and
   the version are what make the word "matches" honest.
4. **Redone on every cookbook release.** A new tag makes the statement stale by its own wording, even when
   the new version moves none of the four values: the sentence names a version, so it is re-run and re-dated.
   The site's deploy guard fails when the statement is older than 120 days, so a cross-check nobody
   revalidates cannot silently stay on the page.

When the two sides disagree, **the recipe decides**: it is the instrument published with a DOI and the one
that names the metric. The inspector is adjusted to it. If a definition ever needs to change, it changes in
the cookbook first, under a **new** metric id, and the inspector follows; a published number is never moved
under its old id. That is a correction, not an improvement, and a correction is announced.

## 5. Controls

Two rules, applied before any number or check in this ledger is trusted.

**A check is broken on purpose before it is trusted.** A check that has only been seen passing has not been
tested; it may be passing because the hard case was not in the sample, or because it never runs. Three cases
from the days this ledger covers, all recorded in [`operations/02-guards.md`](operations/02-guards.md) and
[`operations/03-decision-history.md`](operations/03-decision-history.md):

- a guard for EN/ES `@id` parity was written and proven by breaking it in the morning; by the afternoon it
  sat behind an unconditional `exit 0` and never ran, with the same face as a guard that always passes. It
  was moved and broken again *in the place where it lives*;
- a title comparison passed for Spanish only because the Spanish title contains no `&` (the HTML serves
  `&amp;`); expected values are now derived from the content source and unescaped before comparing;
- the inspector's `robots.txt` parser reported "8 of 8 allowed" for a file that blocks everyone with
  `Disallow: /*`; it now follows RFC 9309 like the recipe, proven on seven cases with the opposite outcomes
  (`Disallow: /*` → 0, `Allow: /$` → 8), all seven equal to v0.1.4.

**A published reproduction command is run and must return the number beside it.** A command printed next to
a value is a claim and is measured like any other. On 2026-09-22 three published commands did not: the word
count returned 0 (a greedy `sed` pattern consumed the whole single-line document — the recipe uses
`perl -0777` with non-greedy `.*?`); a JSON-LD card displayed 4 types while its command returned 5; the
`llms.txt` card printed characters and called them bytes (8 312 against 8 405 that day). Since then every
command on the inspector is executed and has to return its printed value, and every command in an audit of
this repository was run on the date beside it.

Two further habits that belong with the controls:

- **The conversion is printed with the number.** Measuring a live HTML page with the chunking or anchoring
  recipe requires converting it to markdown, and three conversion defects each produced a false number
  silently before they were caught (flattening tags destroyed links → anchoring 0; flattening a link that
  wraps a heading removed a chunk boundary → 6 chunks became 5; the anchoring recipe only matches `http(s)://`
  so relative `href`s must be resolved → 0 of 5). Every such measurement therefore prints the conversion's
  word, heading and list-item counts, and writes the converted markdown to a file to be read by eye.
- **Absence is verified, not assumed.** A regular expression that fails to find something that should be
  there is followed by reading the prose (a "not a prediction" disclaimer was once reported missing because
  the search looked for the word *predict*). A 404 or 403 on one query proves that query found nothing, not
  that the thing does not exist. Where a fact could not be verified against a public URL or the pinned
  cookbook, it is written as `needs-verification`, never asserted.

## 6. What is NOT measured

- **No engine citation.** Nothing here measures whether ChatGPT, Perplexity, Google AI Overviews, Copilot,
  Gemini or any other engine retrieves, reranks, uses or cites a page of zentimes.es. No number in this
  repository should be read as an effect on citation, and no label predicts one.
- **No rankings.** No position in any search engine, for any query, is recorded.
- **No traffic.** No visits, sessions, impressions, referrals or crawler hits are recorded; "allowed in
  `robots.txt`" is a statement of declared policy, not evidence that any crawler fetched the page.
- **No timing as a rating.** Time to first byte is printed as one measurement from one place and never
  rated.
- **No HTML size.** Two fetches of the same page within minutes returned different byte counts (different
  request headers); size is not stable enough to be a measurement.
- **No truth of the figures the pages link to.** Anchoring a claim to a source moves the burden of proof to
  the linked method; the recipe checks that the link exists, and this ledger separately checks that the
  target anchor exists. Neither says the figure is true.
- **No server, code or deployment facts.** The ledger records only what a stranger can fetch from
  `https://zentimes.es` without an account, plus the operations side's description of *how* the site is
  built and guarded, without machines, addresses, paths, users or providers.

## 7. Every number, three companions

A number appears in this repository only with: the **date and time (UTC)** it was measured, the
**instrument** (a recipe path in cookbook v0.1.4, the public inspector with its criteria version, or a named
standard-library script in `tools/`), and the **command** that reproduces it against the public URL. A number
without a command is not written down.

Two terms appear where a "before" value is cited. **The working record** is the author's own dated notes of each
measurement taken while the work was done; **the operations record** is the operations side's dated notes of
each change and deployment. Both are internal notes that a reader of this repository cannot open. Every figure
taken from either of them is tagged `needs-verification` where it is cited, because the pre-change pages are no
longer served and the figure cannot be re-run; the tag is by construction, not a doubt about the note.
