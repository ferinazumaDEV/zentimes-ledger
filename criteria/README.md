# Criteria — what the public inspector prints, captured as printed

The AI citability inspector on zentimes.es rates one page at a time. Every check is printed with a label, the
rule that decides the label, the discipline the check belongs to, whether the rule is stable or still changing,
the criteria version it was rated under, and the shell command that reproduces the value. This folder captures
those published criteria so that any report someone kept can be read against the rule set that produced it.

Nothing here is the inspector's source code. It is a record of what the public pages say, quoted verbatim, with
the date and the command used to capture them.

| | |
|---|---|
| Public pages | https://zentimes.es/tools/ai-inspector/ (EN) · https://zentimes.es/es/herramientas/inspector-ia/ (ES) |
| Report run used | `?url=https://zentimes.es/` on both pages |
| Captured | 2026-09-23 13:40Z (v2026.09.2) and 2026-09-23 14:44Z (v2026.10), `curl -sL <page>` — visible text saved under [`captures/`](captures/), one file per page and timestamp |
| Version captured | **v2026.10** · 2026-09-23, current on the page at 14:44Z: full rule text in [`v2026.10.md`](v2026.10.md), captures `2026-09-23T1444Z-*`. Earlier the same day the page served **v2026.09.2** (captured 13:40Z, [`v2026.09.2.md`](v2026.09.2.md)); v2026.10 was first observed 13:52Z with seven new cards (see [`CHANGELOG.md`](../CHANGELOG.md)). |
| Versions with their own file | [`v2026.10.md`](v2026.10.md) (full rule text, 24 cards) · [`v2026.09.2.md`](v2026.09.2.md) (full rule text, 17 cards) · [`v2026.09.1.md`](v2026.09.1.md) · [`v2026.09.md`](v2026.09.md) (history entries only; earlier rule text was not captured before it changed) |
| Reference cookbook | The GEO Cookbook **v0.1.4** (tag 2026-09-22), https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook |

## The promise text (verbatim)

Printed above the form on both pages and repeated on every report:

> No overall score and no prediction. Each check gets a label with the exact rule behind it and the command to
> verify it. These are properties of your page, not a promise: no check measures whether an AI cites you, which
> is the engine's decision and nobody outside it controls.

> Sin nota global y sin predicción. Cada comprobación lleva una etiqueta con la regla exacta que la decide y el
> comando para comprobarla. Son propiedades de tu página, no una promesa: ninguna comprobación mide si una IA te
> cita, y eso es decisión del motor, que no controla nadie de fuera.

This matches the grading in the cookbook the inspector cross-checks against: cookbook v0.1.4 `CLAIMS.md` grades
the *engine effect* of every recipe as `experimental` ("no recipe measures retrieval, reranking, generation or
citation by any engine"), and its `dataset/SCHEMA.md` says no `evidence_class` "in any row, measures retrieval,
reranking, generation or citation". The labels below grade **preconditions** of legibility, never citation.

## Label vocabulary

Six states. The page's HTML carries the Spanish token in `data-level`; the English page translates it for display.

| `data-level` (HTML) | ES display | EN display | meaning as the page uses it |
|---|---|---|---|
| `excelente` | Excelente | Excellent | since v2026.09.1: "nothing verifiable is left to improve in that area" |
| `notable` | Notable | Strong | the top rule holds except for one named detail |
| `buena` | Buena | Good | the basic property holds; a convention is missed |
| `baja` | Baja | Low | the property is present but defective |
| `nula` | Nula | None | the property is absent or the page does not respond |
| `sin-evaluar` | Sin valorar | Not rated | a number is printed with no label, on purpose |

Three cards carry no `data-level` at all (informational: distinct Schema.org types, the eight-token robots.txt
card, `/llms.txt`). Several rules also define a "not applicable" outcome (no hreflang, no images, no `#id` links)
that is printed as text, not as a label. Since v2026.10, two of the new cards (article authorship, figures with a
source) print their "not applicable" outcome as the `sin-evaluar` label instead, with `—` as the value.

## Fields printed on every card

Read from the report HTML (class names as served on 2026-09-23; counts are for **v2026.10**, the version
captured at 14:44Z; the v2026.09.2 counts are in [`v2026.09.2.md`](v2026.09.2.md)):

| field | where | values seen |
|---|---|---|
| title of the check | `dt > span` | 24 cards (17 in v2026.09.2) |
| label | `span.insp-nivel.n-<level>` | see vocabulary |
| measured value | `p.insp-valor` | e.g. `200 · 22 ms`, `526`, `9`, `—` |
| why | `p.insp-porque` | one sentence, e.g. "200 direct." |
| how to improve it | `div.insp-mejora` | only when the label is below excellent |
| rhythm + reason | `span.insp-ritmo.r-estable` / `.r-cambiante` | **Stable** (12 cards) or **Changing** (9 cards), followed by the reason, e.g. "RFC 6797", "depends on whether AI crawlers run JavaScript" |
| the rule | second `span` in `p.insp-regla` | verbatim in [`v2026.10.md`](v2026.10.md) |
| evidence class + version | `span.insp-regla-v` | `technical-seo` (12) · `geo-precondition` (6) · `aeo` (2) · `security` (1), each followed by `v2026.10` |
| caveat | `p.insp-matiz` | e.g. "Counting nodes is not validating them."; on the completeness card it is the full list of minimums per type |
| cookbook link | `data-metric`, `data-recipe`, `data-value` on the card, and a line `<metric id> · <recipe path> · cross-checked <date> (<time>Z) against cookbook v0.1.4` | 4 cards |
| reproduce it | `details.insp-cmd > pre > code` | one shell command per card |

The version/date line at the top of a report reads `Criteria v2026.10 · 2026-09-23`. On the landing page it
reads `Criteria v2026.10` without the date. The v2026.10 history entry says the criteria "now carry a review
date"; no such date is printed anywhere on the page or present in its HTML, only that sentence.

### Rhythm is not evidence class

The two axes are deliberately separate. `evidence_class` is the cookbook's field (`dataset/SCHEMA.md`, schema
version 2): whether the number "already finishes" its own discipline (`technical-seo`, `aeo`) or is "a step
before" an outcome nobody has observed (`geo-precondition`). It says nothing about how often the rule changes.
The `Stable / Changing` field says that, with its reason. The landing page explains it this way:

> This is a snapshot of today. Checks marked Stable (crawling, robots.txt, canonical, structured data) have held
> for years. Checks marked Changing are the part the field is still working out: when we learn something new, the
> rule changes and this history says so, with the date and the reason. That is why a label can change even if
> your site has not.

`security` is the inspector's own class: cookbook v0.1.4's schema allows exactly three values and its
`validate.py` refuses a fourth, so the transport check could not have been filed under any cookbook class.

## The cross-check statement

Four cards print, on 2026-09-23 (the same line under v2026.09.2 and v2026.10: the statement was not re-run
when the version changed):

> `<metric id>` · `<recipe path>` · cross-checked 2026-09-23 (13:32Z) against cookbook v0.1.4

| metric id | recipe path | inspector card |
|---|---|---|
| `words_visible_no_js` | `04-technical/ssr-vs-csr-rendering` | Words present without running JavaScript |
| `typed_entities` | `04-technical/structured-data-jsonld` | JSON-LD nodes carrying an @type (nested included) |
| `ai_user_agents_allowed` | `04-technical/ai-crawler-access` | robots.txt — AI agents (eight tokens) |
| `llms_txt_bytes` | `04-technical/ai-crawler-access` | /llms.txt |

All four ids exist in cookbook v0.1.4 (`<recipe>/reproduce.sh` and `dataset/geo-offline-measurements.csv`).
The statement names a date, a time and a cookbook version on purpose: it is only true for that version, and a
new cookbook tag makes it stale by its own wording until it is re-run. (Earlier that week, a first "cross-checked
2026-09-22" statement had been made against a copy of the recipes that was not v0.1.4 for one of the four
metrics; the values were 3 of 4 equal and the words metric 2 apart, 524 against 526. The 13:32Z statement of
2026-09-23 is the one printed now. Source: [`operations/03-historial-de-decisiones.md`](../operations/03-historial-de-decisiones.md);
the page itself shows only the current statement. The 2-word gap reproduces on 2026-09-23 13:45Z by swapping
the entity expression: `curl -s 'https://zentimes.es/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&[a-z]+;/ /g; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w`
gives 524; the v0.1.4 expression `&#?[a-z0-9]+;` with flag `i` gives 526.)

## Same rule, not same metric

Which checks reuse a cookbook metric id and which use their own grouping:

| check | relation to the cookbook |
|---|---|
| Words without JavaScript | **same metric id** `words_visible_no_js`, same recipe command (`perl -0777`, entities `&#?[a-z0-9]+;` with flag `i`). |
| JSON-LD nodes with @type | **same metric id** `typed_entities`: counts nodes, nested included, as the recipe does. |
| robots.txt — AI agents | **same metric id** `ai_user_agents_allowed`: the recipe's eight tokens, printed but **not rated**. |
| /llms.txt | **same metric id** `llms_txt_bytes` (UTF-8 bytes, not characters), printed but **not rated**. |
| robots.txt — assistants that search to answer | **own grouping** (OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User). It decides a label; the cookbook's eight-token count is left intact for the cross-check. Two lists, two names, so one identifier never carries two meanings. |
| Heading structure | **same class, own rule.** The rule says: "A convention: same class as the cookbook's chunking recipe, not its metric." The cookbook metric is `self_contained_chunks` (`03-content/chunk-friendly-structure`); the inspector counts h1/h2 and skips. |
| Links to sections of this page (#id) | **same rule as `unresolved_fragment_links`, applied to the whole page** (the rule says so). That id is **not in cookbook v0.1.4**: it is the check proposed in cookbook pull request #32 (open on 2026-09-23, https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/pull/32). `needs-verification` until the PR is merged and tagged: the inspector cites a rule the pinned cookbook does not yet contain. |
| Your entity's identity links (sameAs) | **own rule.** Grades whether sameAs targets respond. The cookbook's `entities_resolved` (`05-authority/entity-clarity-sameas`) counts names resolved to one Wikidata Q-ID; the inspector does not use it. |
| Distinct Schema.org types | informational, no cookbook id. Note the printed reproduce command prints the **count** (`sort -u \| wc -l`), while the card displays the **names**. |
| Figures with a source (v2026.10) | **same idea, own rule.** The rule says it is "the cookbook's anchoring idea (the source next to the claim) applied to figures" and that any domain counts "as in the anchoring recipe"; it prints no metric id and no recipe path. Which recipe is meant: `needs-verification`. |
| Structured data completeness (v2026.10) | **own rule**, class `aeo`, no cookbook id: sixteen types with a minimum property list, printed in full on the card. |
| Publication and update dates, article authorship (v2026.10) | **own rules**, class `geo-precondition`, no cookbook id. |
| Indexing directives, mobile viewport, outbound links (v2026.10) | **own rules**, class `technical-seo`, sourced to a standard or a stated convention (robots meta / X-Robots-Tag, "HTML and WCAG 1.4.4", HTTP semantics). |
| status, transport, title/description, language, canonical, hreflang, images, sitemap | own rules, sourced to a standard or a stated convention (HTTP semantics, RFC 6797, RFC 6596, HTML Standard, WCAG 1.1.1, sitemaps.org 0.9, "a search convention for years"). |

## Criteria history as printed on the page

All four entries are dated the same day. Quoted verbatim from the English page as captured at 14:44Z; the
Spanish page carries the same four entries (the ES text of each is in the version files).

'GEO agent' is the page's own name for the reviewer role, quoted verbatim from the public criteria history.

> **v2026.10 · 2026-09-23** — Closes the gaps that let incomplete pages score "excellent": indexing (noindex,
> nosnippet, X-Robots-Tag, which overrides everything), viewport, dates, article authorship, minimum properties
> per structured-data type, broken outbound links and figures with a source. The criteria now carry a review
> date: if nobody reviews them within 45 days, deployment fails.

> **v2026.09.2 · 2026-09-23** — HSTS moves out of "response" into its own check, "transport". It is a security
> practice, not a legibility one: it could not lower the HTTP response label. Flagged by the GEO agent reviewing
> v2026.09.1.

> **v2026.09.1 · 2026-09-23** — Bar raised: "excellent" now means nothing verifiable is left to improve in that
> area (HSTS, Open Graph, og:locale, hreflang return links, sitemap listing this page with lastmod, linked JSON-LD
> graph, heading hierarchy without skips, unique ids). New check: image alt text. Words without JavaScript and
> sameAs count were not tightened: no data backs a higher bar.

> **v2026.09 · 2026-09-23** — First version: one label per check with its rule published, no overall score.
> Reviewed before release by the GEO agent against the cookbook.

## Reproducing this capture

The captures include the page's navigation and call-to-action text unedited (menu, footer, the mini-audit
line), because that is what the page prints around the cards; nothing was cut out of the visible text. The
14:44Z captures were fetched with `--compressed` and the User-Agent `Mozilla/5.0 (compatible;
ledger-capture/1.0)`, and had HTML entities unescaped and runs of whitespace collapsed; each file says so in its
header.

```sh
# the pages (visible text is what captures/ holds; tags, <script> and <style> stripped, nothing else edited)
curl -sL 'https://zentimes.es/tools/ai-inspector/'
curl -sL 'https://zentimes.es/es/herramientas/inspector-ia/'
curl -sL 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/'
curl -sL 'https://zentimes.es/es/herramientas/inspector-ia/?url=https://zentimes.es/'

# the rule set and the per-card attributes, from the served HTML
curl -sL 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' \
  | grep -oE '<div class="insp-item"[^>]*>'
curl -sL 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' \
  | grep -oE 'class="insp-ritmo [^"]*"|class="insp-regla-v">[^<]*' | sort | uniq -c

# the pinned cookbook the statement names
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)
```

The report is server-rendered: the `?url=` page arrives with all cards in the HTML, so `curl` is enough and no
browser is needed to read it.

## What this folder does not claim

- It does not claim any label predicts or increases citation by any engine. The page says so; the cookbook grades
  every engine effect as `experimental`; this record repeats it.
- It does not carry the rule text of v2026.09 or v2026.09.1: both were replaced the same day they were published
  and no capture of their rule text exists. Their files hold the history entry and what the operations history
  records about them, marked as such.
- Where the page cites a source this record could not open (the llms.txt study of 137,210 domains), the claim is
  quoted as printed and marked `needs-verification` in the version file.
- The v2026.10 home-page values were not re-run with the printed commands for this record; they are the
  report's own output at 14:44Z. The v2026.09.2 values were re-run at 13:42Z and matched.

Author: Fernando Aporta Franco · ferinazumaDEV / Zentimes. Captured 2026-09-23 (13:40Z and 14:44Z).
