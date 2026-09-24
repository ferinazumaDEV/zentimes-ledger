# Criteria — what the public inspector prints, captured as printed

The AI citability inspector on zentimes.es rates one page at a time. Every check is printed with a label, the
rule that decides the label, the discipline the check belongs to, whether the rule is stable or still changing,
the criteria version it was rated under, and the shell command that reproduces the value. This folder captures
those published criteria so that any report someone kept can be read against the rule set that produced it.

Nothing here is the inspector's source code. It is a record of what the public pages say, quoted verbatim, with
the date and the command used to capture them. The Spanish page's wording is preserved verbatim in the `-es-`
capture files; the rule files quote the English page only.

| | |
|---|---|
| Public pages | https://zentimes.es/tools/ai-inspector/ (EN) · https://zentimes.es/es/herramientas/inspector-ia/ (ES) |
| Report run used | `?url=https://zentimes.es/` on both pages |
| Captured | 2026-09-24 13:56Z (v2026-09-24, both landing pages), 13:57Z (v2026-09-24, EN report page, saved as raw HTML and converted; the report prints 13:54 UTC as its run time) and 14:11Z (v2026-09-24, ES report page, returned as the saved report of a 13:57 UTC run). 2026-09-23 13:40Z (v2026.09.2), 14:44Z (v2026.10), 15:03Z (v2026.11) , 15:29Z (v2026.11.1, report pages only) and 17:20Z (v2026.11.2, report pages only), `curl -sL <page>` — visible text saved under [`captures/`](captures/), one file per page and timestamp |
| Version captured | **v2026-09-24** · 2026-09-24, current on the page at 13:54–13:57Z: a redesign, described in [`v2026-09-24.md`](v2026-09-24.md) (requirements met or not, findings with a severity, "substance" by percentile, site-wide checks, a streamed report; rule text of every card, the vocabulary of `data-class`, `data-level` and `data-severity`, and the home labels that moved against v2026.11.2). The reference sample behind the "substance" cuts: [`sample-sme-es-2026-09.md`](sample-sme-es-2026-09.md). Before it, **v2026.11.2** · 2026-09-23, current on the page at 17:20Z: delta in [`v2026.11.2.md`](v2026.11.2.md) (one history entry, one rule changed on the title/h1 card, HSTS and the cross-check line moved); before it v2026.11.1: delta in [`v2026.11.1.md`](v2026.11.1.md) (one history entry, one convention changed, rule text otherwise identical to v2026.11), captures `2026-09-23T1529Z-*-report-*`. Before it, **v2026.11** (captured 15:03Z, full rule text in [`v2026.11.md`](v2026.11.md), captures `2026-09-23T1503Z-*`), **v2026.10** (captured 14:44Z, [`v2026.10.md`](v2026.10.md)) and **v2026.09.2** (captured 13:40Z, [`v2026.09.2.md`](v2026.09.2.md)); v2026.10 was first observed 13:52Z with seven new cards (see [`CHANGELOG.md`](../CHANGELOG.md)). v2026.11 was already live at 15:03Z and v2026.11.1 at 15:29Z; the minutes they went live (between 14:44Z and 15:03Z, and between 15:03Z and 15:29Z) were not observed, nor was the minute v2026-09-24 went live (between 17:20Z on 2026-09-23 and 13:54Z on 2026-09-24). Since v2026-09-24 the version name is the publication date; the page says results are not comparable across that change. |
| Versions with their own file | [`v2026-09-24.md`](v2026-09-24.md) (full rule text, 36 cards: 12 requirements, 12 rule cards, 2 percentile cards, 10 informative; plus [`sample-sme-es-2026-09.md`](sample-sme-es-2026-09.md)) · [`v2026.11.2.md`](v2026.11.2.md) (delta) · [`v2026.11.1.md`](v2026.11.1.md) (delta: the one changed convention, home labels that moved) · [`v2026.11.md`](v2026.11.md) (full rule text, 31 cards) · [`v2026.10.md`](v2026.10.md) (full rule text, 24 cards) · [`v2026.09.2.md`](v2026.09.2.md) (full rule text, 17 cards) · [`v2026.09.1.md`](v2026.09.1.md) · [`v2026.09.md`](v2026.09.md) (history entries only; earlier rule text was not captured before it changed) |
| Reference cookbook | The GEO Cookbook **v0.1.4** (tag 2026-09-22), https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook |

## The promise text (verbatim)

Printed above the form on both pages and repeated on every report (English page; the Spanish page's wording is in
the `-es-` capture files):

> No overall score and no prediction. Each check gets a label with the exact rule behind it and the command to
> verify it. These are properties of your page, not a promise: no check measures whether an AI cites you, which
> is the engine's decision and nobody outside it controls.

This matches the grading in the cookbook the inspector cross-checks against: cookbook v0.1.4 `CLAIMS.md` grades
the *engine effect* of every recipe as `experimental` ("no recipe measures retrieval, reranking, generation or
citation by any engine"), and its `dataset/SCHEMA.md` says no `evidence_class` "in any row, measures retrieval,
reranking, generation or citation". The labels below grade **preconditions** of legibility, never citation.

## Label vocabulary

**Since v2026-09-24 (2026-09-24)** the vocabulary has three layers, all carried as Spanish tokens in the HTML
and translated on the English page (details and the observed counts in [`v2026-09-24.md`](v2026-09-24.md)):

| attribute | tokens | EN display | where |
|---|---|---|---|
| `data-class` on `div.insp-item` | `requisito` · `regla` · `percentil` · `informativa` | printed as the token, e.g. `requisito · technical-seo · v2026-09-24` | every card |
| `data-level` on a `requisito` card | `cumple` · `no-cumple` · `no-aplica` (· `sin-evaluar` when it cannot be checked) | Meets · Does not meet · Not applicable (· Not rated) | 12 cards; only `cumple` and `sin-evaluar` observed on the home |
| `data-level` on a `regla` card | `nula` · `baja` · `buena` · `sin-evaluar` | None · Low · Good · Not rated | 12 cards, capped at Good by rule; only `buena` and `sin-evaluar` observed |
| `data-level` on a `percentil` card | `nula` · `baja` · `buena` · `notable` · `excelente` · `sin-evaluar` | None · Low · Good · Strong · Excellent · Not rated | 2 cards ("substance", site depth); only `sin-evaluar` observed (English home page; no inner-page sample) |
| `data-severity` on `li.insp-hallazgo` | `critico` · `grave` · `moderado` · `menor` | Critical · Serious · Moderate · Minor | one finding per problem, with `data-finding` and `data-block`; only `menor` observed |

The label of a card is the lower of what its rule gives and the cap of the worst open finding in its block
(Critical → None, Serious → Low, Moderate → Good on a percentile card and Low on a rule card, Minor → Strong
on a percentile card and Good on a rule card). Informative cards carry no `data-level`. The tokens marked
"not observed" are what the page's own tables and the operations side state; this record has not seen them
printed.

**Up to v2026.11.2 (2026-09-23):** six states. The page's HTML carries the Spanish token in `data-level`; the
English page translates it for display.

| `data-level` (HTML) | ES display | EN display | meaning as the page uses it |
|---|---|---|---|
| `excelente` | Excelente | Excellent | since v2026.09.1: "nothing verifiable is left to improve in that area" |
| `notable` | Notable | Strong | the top rule holds except for one named detail |
| `buena` | Buena | Good | the basic property holds; a convention is missed |
| `baja` | Baja | Low | the property is present but defective |
| `nula` | Nula | None | the property is absent or the page does not respond |
| `sin-evaluar` | Sin valorar | Not rated | a value is printed and, on purpose, not graded: informative cards, and since v2026.11 every "not applicable" outcome |

Under v2026.10, three cards carried no `data-level` at all (informational: distinct Schema.org types, the
eight-token robots.txt card, `/llms.txt`), several rules defined a "not applicable" outcome (no hreflang, no
images, no `#id` links) that was printed as text, not as a label, and two of the new cards (article authorship,
figures with a source) printed their "not applicable" outcome as the `sin-evaluar` label with `—` as the value.
Under v2026.11 only one card has no `data-level` (distinct Schema.org types); the robots.txt eight-token card and
`/llms.txt` carry `data-level="sin-evaluar"` with a rhythm line and an evidence class, every rule that defines a
"not applicable" outcome prints it as the `sin-evaluar` label, and three cards are informative by rule (hidden
text, outbound links, `/llms.txt`), so they are always `sin-evaluar`.

## Fields printed on every card

Read from the report HTML (class names as served on 2026-09-23; counts are for **v2026.11**, the version
captured at 15:03Z; the v2026.10 counts are in [`v2026.10.md`](v2026.10.md) and the v2026.09.2 counts in
[`v2026.09.2.md`](v2026.09.2.md)):

| field | where | values seen |
|---|---|---|
| title of the check | `dt > span` | 31 cards (24 in v2026.10, 17 in v2026.09.2) |
| label | `span.insp-nivel.n-<level>` | see vocabulary; 30 cards carry one |
| measured value | `p.insp-valor` | e.g. `200 · 25 ms`, `526`, `9`, `48 KB`, `—` |
| why | `p.insp-porque` | one or two sentences, e.g. "Returns 200 directly." |
| how to improve it | `div.insp-mejora` | only when the label is below excellent |
| rhythm + reason | `span.insp-ritmo.r-estable` / `.r-cambiante` | **Stable** (21 cards) or **Changing** (9 cards), followed by the reason, e.g. "RFC 6797 and the HSTS preload list requirements", "if AI crawlers start running JavaScript, the rule changes"; 30 cards carry one |
| the rule | second `span` in `p.insp-regla` | verbatim in [`v2026.11.md`](v2026.11.md); since v2026.11 most rules end with a "Source(s): … Convention(s): …" sentence |
| evidence class + version | `span.insp-regla-v` | `technical-seo` (20) · `geo-precondition` (4) · `aeo` (2) · `security` (1) · `accessibility` (3), each followed by `v2026.11`; `security` and `accessibility` are not cookbook classes |
| caveat | `p.insp-matiz` | 3 cards in v2026.11 (HTTP response, robots.txt eight tokens, structured data and entity), e.g. "Counting nodes is not validating them." |
| cookbook link | `data-metric`, `data-recipe`, `data-value` on the card, and a line `p.insp-metrica`: `<metric id> · <recipe path> · cross-checked <date> (<time>Z) against cookbook v0.1.4` | 4 cards |
| reproduce it | `details.insp-cmd > pre > code` | one shell command per card |

The version/date line at the top of a report reads `Criteria v2026.11.1 · 2026-09-23` since 15:29Z
(`Criteria v2026.11 · 2026-09-23` at 15:03Z). On the landing page it reads `Criteria v2026.11.1` without the
date. The v2026.11.1 counts per field are the same as v2026.11's: 31 cards, 30 labels, the same tallies of
rhythm and class. The v2026.10 history entry says the criteria "now carry a review
date"; no such date is printed anywhere on the page or present in its HTML under v2026.10 or v2026.11, only
that sentence.

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
Since v2026.11 there is a second such class, `accessibility` (declared language, viewport and zoom, image alt
text); the history entry names it as "not a cookbook class" itself.

## The cross-check statement

Four cards print, on 2026-09-23 (the same line under v2026.09.2, v2026.10, v2026.11 and v2026.11.1: the
statement was not re-run when the version changed):

> `<metric id>` · `<recipe path>` · cross-checked 2026-09-23 (13:32Z) against cookbook v0.1.4

| metric id | recipe path | inspector card (v2026.11 title) | `data-value` at 14:44Z, 15:03Z and 15:29Z |
|---|---|---|---|
| `words_visible_no_js` | `04-technical/ssr-vs-csr-rendering` | Words present without running JavaScript | 526 |
| `typed_entities` | `04-technical/structured-data-jsonld` | Structured data and entity (JSON-LD nodes with @type) | 9 |
| `ai_user_agents_allowed` | `04-technical/ai-crawler-access` | robots.txt — training and user agents (informative) | 8 |
| `llms_txt_bytes` | `04-technical/ai-crawler-access` | /llms.txt (informative) | 9484 |

Under v2026-09-24 (2026-09-24, read at 13:54–13:57Z) the four cards are informative (`data-class="informativa"`,
no `data-level`), keep `data-metric`, `data-recipe` and `data-value` on both the provisional and the final
copy. The EN report of the 13:54 UTC run still printed `cross-checked 2026-09-23 (15:59Z) against cookbook
v0.1.4`; the ES saved report of the 13:57 UTC run (fetched 14:11Z) prints `contrastado el 2026-09-24 (13:43Z)
con cookbook v0.1.4`. Their `data-value`s:
`words_visible_no_js` **539** · `typed_entities` **9** · `ai_user_agents_allowed` **8** · `llms_txt_bytes`
**9332** (529 · 9 · 8 · 9574 at 17:20Z on 2026-09-23; the two that moved did so with page changes, not with
the criteria). The reviewer re-ran the pinned v0.1.4 recipes at 2026-09-24T13:43:50Z: 539 · 9 · 8 · 9332, 4 of
4 equal to the inspector ([`CHANGELOG.md`](../CHANGELOG.md), 2026-09-24). The printed statement is stale by its
own wording for the two moved values until the page prints the new time. The titles changed: "Words present
without running JavaScript" (unchanged), "robots.txt — training and user agents (informative)" (unchanged),
"JSON-LD nodes with @type (informative)" (was "Structured data and entity (JSON-LD nodes with @type)"; the
entity rating moved to its own card without a metric id) and "/llms.txt (informative)" (unchanged).

All four ids exist in cookbook v0.1.4 (`<recipe>/reproduce.sh` and `dataset/geo-offline-measurements.csv`).
Across the v2026.10 → v2026.11 change the four cards kept their `data-metric`, `data-recipe` and `data-value`
(526 · 9 · 8 · 9484) and the cross-check statement still reads 13:32Z. Their evidence class also matches the
class the ledger's [`METHOD.md`](../METHOD.md) records for the three v0.1.4 recipes (`technical-seo`, `aeo`,
`technical-seo`): the words card and the structured-data card print the same class as before; the robots.txt
eight-token card and `/llms.txt` printed no class at all under v2026.10 and now print `technical-seo`.
The statement names a date, a time and a cookbook version on purpose: it is only true for that version, and a
new cookbook tag makes it stale by its own wording until it is re-run. (Earlier that week, a first "cross-checked
2026-09-22" statement had been made against a copy of the recipes that was not v0.1.4 for one of the four
metrics; the values were 3 of 4 equal and the words metric 2 apart, 524 against 526. The 13:32Z statement of
2026-09-23 is the one printed now. Source: [`operations/03-decision-history.md`](../operations/03-decision-history.md);
the page itself shows only the current statement. The 2-word gap reproduces on 2026-09-23 13:45Z by swapping
the entity expression: `curl -s 'https://zentimes.es/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&[a-z]+;/ /g; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w`
gives 524; the v0.1.4 expression `&#?[a-z0-9]+;` with flag `i` gives 526.)

## Same rule, not same metric

Which checks reuse a cookbook metric id and which use their own grouping:

| check | relation to the cookbook |
|---|---|
| Words without JavaScript | **same metric id** `words_visible_no_js`, same recipe command (`perl -0777`, entities `&#?[a-z0-9]+;` with flag `i`). |
| Structured data and entity (JSON-LD nodes with @type) | **same metric id** `typed_entities`: counts nodes, nested included, as the recipe does. The label is decided by the inspector's own entity rule (v2026.11: entity with name, url and logo or image, plus a WebSite, on the home page; v2026.11.1: the entity checked is the one the WebSite declares as `publisher`, else the first root entity). |
| robots.txt — training and user agents (informative) | **same metric id** `ai_user_agents_allowed`: the recipe's eight tokens on the root path, printed but **not rated** (the caveat says so: "The data-value is the recipe's metric"). |
| /llms.txt (informative) | **same metric id** `llms_txt_bytes` (UTF-8 bytes, not characters), printed but **not rated**. |
| robots.txt — search engines and assistants | **own grouping.** v2026.11: seven agents (Googlebot, Bingbot, Applebot, OAI-SearchBot, Claude-SearchBot, Claude-User, PerplexityBot) on the page's path; v2026.10: four (OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User) on the root. It decides a label; the cookbook's eight-token count is left intact for the cross-check. Two lists, two names, so one identifier never carries two meanings. |
| Heading hierarchy (v2026.11; "Heading structure" until v2026.10) | **own rule.** Until v2026.10 the rule said "same class as the cookbook's chunking recipe, not its metric" (class `geo-precondition`; the cookbook metric is `self_contained_chunks`, `03-content/chunk-friendly-structure`). v2026.11 drops that sentence, moves the card to `technical-seo` and Stable, and sources it to the HTML Living Standard. |
| Links to sections of this page (#id) | **same rule as `unresolved_fragment_links`, applied to the whole page** (the rule says so, unchanged in v2026.11). That id is **not in cookbook v0.1.4**: it is the check proposed in cookbook pull request #32 (open on 2026-09-23, https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/pull/32). `needs-verification` until the PR is merged and tagged: the inspector cites a rule the pinned cookbook does not yet contain. |
| Your entity's identity links (sameAs) | **own rule.** Grades whether sameAs targets respond. The cookbook's `entities_resolved` (`05-authority/entity-clarity-sameas`) counts names resolved to one Wikidata Q-ID; the inspector does not use it (v2026.11 says so: "Wikidata and quantity are not rewarded"). |
| Distinct Schema.org types | informational, no cookbook id. Note the printed reproduce command prints the **count** (`sort -u \| wc -l`), while the card displays the **names**. |
| Figures with a source | **same idea, own rule.** The rule says a source counts "as in the cookbook's anchoring recipe" (v2026.11) / "the cookbook's anchoring idea … applied to figures" (v2026.10); it prints no metric id and no recipe path. Which recipe is meant: `needs-verification`. The ledger's [`METHOD.md`](../METHOD.md) lists `06-measurement/citation-anchoring` (`claim_source_pairs`, markdown list items with an inline link), which counts something else. |
| Properties per type (v2026.11; "Structured data completeness" in v2026.10) | **own rule**, class `aeo`, no cookbook id. v2026.10: sixteen types with a minimum list each, printed as a caveat. v2026.11: only types with properties documented by Google (Product, BreadcrumbList, ProfilePage required; Article, BlogPosting, NewsArticle, Organization recommended), inside the rule. |
| Article dates, article authorship | **own rules**, no cookbook id. v2026.10: every page, class `geo-precondition`, Changing. v2026.11: articles only, class `technical-seo`, Stable, sourced to Google's Article documentation. |
| Indexing directives (per engine), outbound links | **own rules**, class `technical-seo`. v2026.11 rates indexing per engine (Google and Bing, worse label wins) and makes outbound links informative (always not rated; "no source backs a scale for this"). |
| HTML size, character encoding, head readable by Google, crawlable links, structured data visible on the page, owner and contact (new in v2026.11) | **own rules**, class `technical-seo`, no cookbook id, each sourced to a named document (a Googlebot page dated 2026-02-03, the HTML Standard and W3C, Google's documentation on valid metadata, crawlable links, its general structured data policy, its quality guidelines) with the cuts declared as conventions. |
| Hidden text (informative, new in v2026.11) | **own rule**, class `geo-precondition`, no cookbook id, never rated ("there is no evidence-based threshold"). |
| Declared language, viewport and zoom, image alt text | **own rules**, class `accessibility` since v2026.11 (`technical-seo` until v2026.10), sourced to WCAG 3.1.1, WCAG 1.4.4 with W3C ACT rule b4f0c3, and WCAG 1.1.1. |
| status, transport, title/description/h1, canonical, hreflang, sitemap | own rules, class `technical-seo` (`security` for transport), sourced to a standard or a named document (HTTP semantics and Google's redirect documentation, RFC 6797 and hstspreload.org, Google's title-link, canonicalization and localized-versions documentation, sitemaps.org 0.9 with Google and Bing documentation). |

## Criteria history as printed on the page

All six entries are dated the same day. Quoted verbatim from the English page as captured at 15:29Z (the
first five were identical at 15:03Z); the Spanish page carries the same six entries (their Spanish text is in
the `-es-` capture files).

'GEO agent' and 'a second agent' are the page's own names for reviewer roles, quoted verbatim from the public
criteria history.

> **v2026.11.1 · 2026-09-23** — The main entity (rated by "structured data", "properties per type" and "sameAs")
> becomes the one the graph itself declares as the WebSite's publisher; only if it declares none, the first
> root entity. It used to depend on the JSON-LD order, not on what the site says about itself.

> **v2026.11 · 2026-09-23** — Rules rebuilt from verified evidence (64 sources confirmed by a second agent and
> reviewed by the GEO agent). Labels that move from v2026.10, and why: one h1 and a number of h2 are no longer
> required (HTML allows several h1); x-default is no longer required (Google recommends it, does not require
> it); og:url and title/description lengths no longer decide the level (Google does not ask for them; the
> description has no limit); redirects from the pasted URL no longer count (they depend on how it is pasted;
> Googlebot follows up to 10); having no sitemap becomes "not rated" (Google does not need one on small,
> well-linked sites); HSTS preload is not required (hstspreload.org does not recommend it); "no entity" becomes
> "not rated" on inner pages; robots.txt is evaluated on the page's path and for the 7 agents that decide
> appearing in search and answers, and training policy becomes informative; indexing is computed per engine
> (Google and Bing). Classes: language, viewport and images move to accessibility (not a cookbook class). New:
> HTML size, encoding, valid head, crawlable links, hidden text (informative), visible structured data, and
> owner and contact. Outbound links and llms.txt become informative.

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
14:44Z, 15:03Z and 15:29Z captures were fetched with `--compressed` and the User-Agent `Mozilla/5.0 (compatible;
ledger-capture/1.0)`, and had HTML entities unescaped and runs of whitespace collapsed; each file says so in its
header. In those captures every HTML tag starts a new line, so a history entry appears as two lines (the bold
version token, then the dated text) and a card's title and label are on separate lines.

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

Up to v2026.11.2 the report was server-rendered in one piece: the `?url=` page arrived with all cards in the
HTML, so `curl` was enough and no browser was needed to read it. Since v2026-09-24 the report is streamed:
`curl` still returns every card, but the cards that depend on the site-wide part appear twice, first as a
provisional copy (`data-provisional="true"`, label "Checking…" or a value that may still change) and then
final inside hidden containers. Read the final copies (`grep -v 'data-provisional'` on the `insp-item`
lines), and expect one inspection per origin every 10 minutes at most: a later request returns the saved
report of the last run, complete and without provisional copies, with a notice line saying so (the ES capture
of 14:11Z is one). The 2026-09-24 EN report capture was made from the raw HTML saved at 13:57Z, with comments
removed as well as tags, scripts and styles; the two 13:56Z landing captures and the 14:11Z ES report were
fetched with the same command and User-Agent as the 2026-09-23 ones.

## What this folder does not claim

- It does not claim any label predicts or increases citation by any engine. The page says so; the cookbook grades
  every engine effect as `experimental`; this record repeats it.
- It does not carry the rule text of v2026.09 or v2026.09.1: both were replaced the same day they were published
  and no capture of their rule text exists. Their files hold the history entry and what the operations history
  records about them, marked as such.
- Where the page cites a source this record could not open (the llms.txt study of 137,210 domains under
  v2026.09.2 and v2026.10; the "Vercel/MERJ study, Dec 2024" named in the v2026.11 words rule), the claim is
  quoted as printed and marked `needs-verification` in the version file. v2026.11 no longer prints the llms.txt
  study sentence.
- The v2026.10, v2026.11 and v2026.11.1 home-page values were not re-run with the printed commands for this
  record; they are the report's own output at 14:44Z, 15:03Z and 15:29Z. The v2026.09.2 values were re-run at 13:42Z and matched.
- The 64 sources the v2026.11 history entry says were confirmed are not listed on the page; this record cannot
  say which they are. The same holds for the 24 citations the operations side says it checked for v2026-09-24.
- Under v2026-09-24, the tokens `no-cumple`, `no-aplica`, `nula`, `baja`, `notable`, `excelente`, `critico`,
  `grave` and `moderado` were not observed on the site's own home page; they are recorded from the page's
  tables and the operations side's description, not from a printed card. The 56 values of the reference
  sample are as the page and the operations side publish them; the saved HTML files behind them are third
  parties' pages and are not published, so only the interpolation over the 56 values can be re-run from
  outside.

Author: Fernando Aporta Franco · ferinazumaDEV / Zentimes. Captured 2026-09-23 (13:40Z, 14:44Z, 15:03Z, 15:29Z and 17:20Z) and 2026-09-24 (13:56Z and 13:57Z).
