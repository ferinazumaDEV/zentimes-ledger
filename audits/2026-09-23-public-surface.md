# Public-surface audit of zentimes.es — 2026-09-23

**Author:** Fernando Aporta Franco (ferinazumaDEV / Zentimes)
**Measured:** 2026-09-23, between 13:41Z and 13:50Z (each number carries its own timestamp)
**Instruments:** The GEO Cookbook **v0.1.4** (tag `v0.1.4`, released 2026-09-22; concept DOI
[10.5281/zenodo.22299279](https://doi.org/10.5281/zenodo.22299279); repository
[ferinazumaDEV/generative-engine-optimization-cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook)),
the site's public inspector at <https://zentimes.es/tools/ai-inspector/> (criteria v2026.09.2), and the
stdlib-only scripts in [`tools/`](../tools/) of this repository.
**Scope:** only what any stranger can fetch from `https://zentimes.es` without an account. Nothing here
comes from the server, the source code or the deployment.

## 0. What this audit is and is not

This is a dated record of **preconditions**: what a fetch-only crawler, a JSON-LD parser, a fixed-size
splitter and a link parser can extract from the public pages. Every number below has three things next
to it: the UTC timestamp of the measurement, the instrument (a cookbook recipe path or the inspector),
and a reproduction command in [Appendix A](#appendix-a--reproduction-commands) that runs with `curl`,
`perl` and Python 3's standard library against the public URL.

**No number here measures, and none should be read as, an effect on citation by any AI engine.** The
cookbook grades the engine effect of every one of its six techniques as `experimental` ("no recipe measures
retrieval, reranking, generation or citation by any engine", `CLAIMS.md` of v0.1.4), and its dataset schema
states that no `evidence_class` measures any of those either. The inspector says the same on its page:
"no check measures whether an AI cites you". Labels and metrics grade readiness, not outcome.

Where a value could not be verified against a public URL or the pinned cookbook it is marked
`needs-verification`.

## 1. Numbers at a glance

| # | Property | Value | UTC | Instrument | Command |
|---|---|---|---|---|---|
| 1 | URLs in `sitemap.xml` | **27** | 13:41:04 | sitemap fetch | [A1](#a1-sitemap-url-count) |
| 2 | Sitemap entries carrying `<lastmod>` | **23 of 27** | 13:44:09 | sitemap fetch | [A2](#a2-lastmod-per-sitemap-entry) |
| 3 | Pages whose `<link rel="canonical">` equals their sitemap `<loc>` | **27 of 27** | 13:44:09–13:45:41 | `tools/check-sitemap-pages.py` | [A3](#a3-canonical-hreflang-description-length-per-page) |
| 4 | Pages without any `hreflang` link | **5 of 27** (the five Spanish notes) | 13:44:09–13:45:41 | `tools/check-sitemap-pages.py` | [A3](#a3-canonical-hreflang-description-length-per-page) |
| 5 | Distinct JSON-LD `@id` across the sitemap | **60** (24 site-scope, 36 page-scope) | 13:41:04 | sitemap walk | [A4](#a4-id-census-over-the-sitemap) |
| 6 | Malformed `@id` (two `#`, or whitespace) | **0** | 13:41:04 | sitemap walk | [A4](#a4-id-census-over-the-sitemap) |
| 7 | Typed entities, EN home `/` | **9** | 13:41:52 | `04-technical/structured-data-jsonld` | [A5](#a5-typed-entities-and-typed-facts) |
| 8 | Typed facts, EN home `/` | **49** | 13:41:52 | `04-technical/structured-data-jsonld` | [A5](#a5-typed-entities-and-typed-facts) |
| 9 | Typed entities / typed facts / `"@id":` occurrences, ES home `/es/` | **9 / 49 / 14** | 13:47:07 | same definition (`tools/count-jsonld.py`) | [A5](#a5-typed-entities-and-typed-facts) |
| 10 | `Service` nodes with identical `@id` on EN and ES homes | **4 of 4**, all with `provider` → `https://zentimes.es/#zentimes` | 13:41:31 | JSON-LD walk of both homes | [A6](#a6-service-id-parity-en--es) |
| 11 | Words visible without JavaScript, EN home | **526** | 13:41:52 (recipe) · 13:46:35 (curl) | `04-technical/ssr-vs-csr-rendering` | [A7](#a7-words-visible-without-javascript) |
| 12 | Words visible without JavaScript, ES home | **555** | 13:46:35 | `04-technical/ssr-vs-csr-rendering` (same `extract`) | [A7](#a7-words-visible-without-javascript) |
| 13 | AI-related `robots.txt` tokens allowed for `/` | **8 of 8** | 13:41:52 | `04-technical/ai-crawler-access` | [A8](#a8-robotstxt-and-the-eight-tokens) |
| 14 | `llms.txt` size | **9 484 bytes** (9 360 characters, 70 lines, 31 links to `zentimes.es`) | 13:46:16 | `04-technical/ai-crawler-access` (`llms_txt_bytes`) | [A9](#a9-llmstxt-size) |
| 15 | Self-contained chunks, EN home | **4 of 4** | 13:41:48 | `03-content/chunk-friendly-structure` | [A10](#a10-chunk-self-containment-and-claimsource-pairs) |
| 16 | Self-contained chunks, ES home | **4 of 4** | 13:41:50 | `03-content/chunk-friendly-structure` | [A10](#a10-chunk-self-containment-and-claimsource-pairs) |
| 17 | Claim→source pairs, EN home | **5 of 5** | 13:41:48 | `06-measurement/citation-anchoring` | [A10](#a10-chunk-self-containment-and-claimsource-pairs) |
| 18 | Claim→source pairs, ES home | **5 of 5** | 13:41:50 | `06-measurement/citation-anchoring` | [A10](#a10-chunk-self-containment-and-claimsource-pairs) |
| 19 | Linked claims whose target anchor exists | **5 of 5** (EN) and **5 of 5** (ES), target `#c4` on the case-study page, HTTP 200 | 13:41:33 | anchor check (not a cookbook recipe) | [A11](#a11-anchor-existence) |
| 20 | Inspector vs recipes, four shared metric ids | **4 of 4 equal**: 526 · 9 · 8 · 9 484 | 13:41:53 (and again 13:49:53) | `tools/compare-inspector-vs-recipes.py` | [A12](#a12-inspector-versus-recipes) |
| 21 | `/en/` | **HTTP 404** (English lives at `/`, Spanish at `/es/`) | 13:41:07 | HTTP fetch | [A13](#a13-language-roots-and-hsts) |
| 22 | `Strict-Transport-Security` on `/` | `max-age=31536000`, no `includeSubDomains`, no `preload` | 13:47:07 | HTTP headers | [A13](#a13-language-roots-and-hsts) |

## 2. Sitemap, canonicals, hreflang

`https://zentimes.es/sitemap.xml` lists **27 URLs** (A1): 11 English pages under `/`, 11 Spanish pages under `/es/`,
and 5 Spanish notes under `/es/notas/<slug>/`. Every one of the 27 answered **HTTP 200** and every one declares a
`<link rel="canonical">` **equal to its own sitemap `<loc>`** (27 of 27, A3). The sitemap is also announced from
`robots.txt` (`Sitemap:` line, A8).

**`<lastmod>`:** 23 of 27 entries carry it. The four without are the two homes (`/`, `/es/`) and the two notes
listings (`/notes/`, `/es/notas/`) (A2).

**hreflang:** 22 of 27 pages declare `en`, `es` and `x-default` alternates. The **five Spanish notes declare no
hreflang at all** (A3):

- `/es/notas/lo-que-no-se-mide-no-cuenta/`
- `/es/notas/como-hacer-que-chatgpt-te-cite/`
- `/es/notas/geo-no-es-seo/`
- `/es/notas/que-es-geo/`
- `/es/notas/con-calma-y-con-tiempo/`

These five have no English counterpart in the sitemap, and the English listing `/notes/` links straight to the
`/es/notas/…` pages (A14). A page that exists in one language only has nothing to point `hreflang` at, so the
absence is consistent with the content; whether single-language notes are the intended design is a decision
of the site owner and is recorded here as `needs-verification`, not as a defect. The inspector's own
"hreflang: excellent" label for `/` is about the home page only and does not contradict this.

`/en/` returns **404** (A13): the English root is `/`, not `/en/`.

## 3. The entity graph (JSON-LD)

**Census (A4).** Walking every JSON-LD block on the 27 pages yields **60 distinct `@id`**, **0 malformed**
(none with more than one `#`, none with whitespace). They split into two scopes:

- **24 site-scope** identifiers, hanging off the origin `https://zentimes.es/#…`, identical on every page that
  emits them: `#ferinazumaDEV` (Person), `#zentimes` (ProfessionalService), `#website` (WebSite), four
  `#service-*` (Service: `geo-audit`, `geo-implementation`, `geo-monitoring`, `technical-seo`), `#glossary`
  (DefinedTermSet) and 16 `#term-*` (DefinedTerm). The seven non-glossary ones appear on all 27 pages; the
  glossary ones on the two glossary pages.
- **36 page-scope** identifiers, hanging off a page's canonical URL: `#breadcrumb` (BreadcrumbList) on 18
  pages, plus one content node per page (`#post` BlogPosting ×5, `#case` Article ×2, `#article` ×2,
  `#collection` CollectionPage ×4, `#faq` FAQPage ×2, `#webpage` WebPage ×4). Page-scope ids differ between
  languages because the canonical URL differs; site-scope ids never do.

**Both homes (A5, A6).** `/` and `/es/` each carry **one** JSON-LD block with **9 typed entities**, **49 typed
facts** and **14 occurrences of `"@id":`** (declarations and references together). Types present:
`Person`, `PostalAddress`, `ProfessionalService`, `Service` ×4, `WebSite`. The four `Service` nodes carry the
**same four `@id` on EN and ES** (only `name` is localised; `serviceType` is identical), and each one's
`provider` points by `@id` to `https://zentimes.es/#zentimes`. No `Offer`, `price`, `priceRange` or
`availability` key appears in the markup of either home (A6).

**What the homes do not carry.** The home pages emit no page-scope node: no `WebPage`, no `BreadcrumbList`
(7 ids on `/` and `/es/` against 9–26 on the other pages, A3/A4). The inspector labels the home's JSON-LD
"strong" rather than "excellent" for this reason and for entities lacking `logo`/`image` (A12).

## 4. Rendering without JavaScript

Applying the exact `extract` filter of recipe `04-technical/ssr-vs-csr-rendering` (v0.1.4) to the raw HTML
gives **526 words on `/`** and **555 words on `/es/`** (A7). The headings, the service summaries, the
case-study figures, the note titles and the "about" block are present in the served HTML; whether any copy is
added by JavaScript was not measured (the recipe counts words in the served HTML; it cannot show that *no* copy
is added client-side).

Definition note, because two instruments disagreed by 2 words during this audit: the recipe removes
`<script>`, `<style>`, comments, tags, and **every character entity, named or numeric, case-insensitive**
(`&#?[a-z0-9]+;`), and keeps `<noscript>`. A helper that also strips `<noscript>` and only removes
lower-case named entities and decimal references reports **524** for `/`. The recipe's number is the one
that carries the metric id `words_visible_no_js`; the other is a different instrument and is reported here
only so nobody mistakes the gap for a change on the site.

## 5. Crawler access

`robots.txt` (447 bytes, A8; `wc -c`) has 11 groups: `User-agent: *` plus ten named tokens (`GPTBot`,
`OAI-SearchBot`, `ChatGPT-User`, `ClaudeBot`, `anthropic-ai`, `PerplexityBot`, `Perplexity-User`,
`Google-Extended`, `Applebot-Extended`, `CCBot`), every one with `Allow: /`, then `Sitemap:` and `Llms:`
lines. Of the recipe's eight tokens, seven are named explicitly and the eighth (`Bytespider`) falls under
`*`: **8 of 8 allowed** by RFC 9309 evaluation (A8). The recipe's own caveat applies: the eight are a mix of
retrieval, training and usage-control tokens, and "allowed" is a statement of declared policy, not evidence
that any of them fetched or used the page.

`llms.txt` is **9 484 bytes** (A9) — the recipe measures bytes; a character count gives 9 360, which is why a
tool printing `len()` of the decoded text shows a smaller figure. It has 70 lines and 31 links to
`zentimes.es`, all 27 sitemap URLs among them. Four service links point to `https://zentimes.es/#servicios`;
that `id` exists on both homes (A9), so the links resolve, though the dedicated `/services/` and
`/es/servicios/` pages now exist and are also listed. The file states in its own words that "the before/after
measurement panel is not built yet and is not sold as delivered" and that "whether an engine ends up citing
you depends on the engine".

## 6. Content structure and claim anchoring on the homes

Both homes were converted to markdown (headings, paragraphs, list items; navigation, header and footer
dropped; links kept as `[text](absolute-url)`) and passed **unchanged** through the recipes' own
`reproduce.sh --json` (A10). The conversion counts are printed next to the numbers because a wrong
conversion produces a wrong number silently:

| Page | Converted content | `chunks_produced` | `self_contained_chunks` | `claims` | `claim_source_pairs` |
|---|---|---|---|---|---|
| `/` | 395 words · 16 headings · 5 list items | 4 | **4** | 5 | **5** |
| `/es/` | 419 words · 16 headings · 5 list items | 4 | **4** | 5 | **5** |

Two caveats that belong next to those numbers:

- The home carries no `<!-- claims:start -->` marker, so the anchoring recipe counts **every** list item as a
  claim. Today the only list items on the home are the five case-study figures, so the denominator is the
  intended one; if any other list is added, the denominator moves on its own.
- The recipe checks that a claim line carries an `http(s)` link. It does **not** check that the link's target
  anchor exists. That was checked separately (A11): all five claims on each home link to
  `/casos/kenetg/#c4` (EN) or `/es/casos/kenetg/#c4` (ES); both pages answer 200 and contain `id="c4"`.
  Neither check says the figures are true; linking moves the burden of proof to the linked method.

## 7. Inspector versus recipes

The site's public inspector exposes four metrics with the cookbook's own identifiers as `data-metric` /
`data-value` attributes. Running the corresponding recipes (v0.1.4) on the live files and reading those
attributes gives (A12, 13:41:53Z; repeated 13:49:53Z with the same result):

| metric id | recipe | inspector | verdict |
|---|---:|---:|---|
| `words_visible_no_js` | 526 | 526 | equal |
| `typed_entities` | 9 | 9 | equal |
| `ai_user_agents_allowed` | 8 | 8 | equal |
| `llms_txt_bytes` | 9 484 | 9 484 | equal |
| `typed_facts` | 49 | not shown | — |

The inspector's report for `https://zentimes.es/` states, next to each of the four, "cross-checked 2026-09-23
(13:32Z) against cookbook v0.1.4", and heads the report "Criteria v2026.09.2 · 2026-09-23". Its labels for the
home on that run: status excellent (200, direct, HTTPS), transport security strong (HSTS one year without
`includeSubDomains`), title and meta description good (description outside the 120–160 convention), language
excellent, words-without-JS not rated (reported as a number only), JSON-LD nodes strong, entity excellent,
canonical excellent, hreflang excellent, headings excellent, anchors excellent, images excellent,
search-robots excellent (4 of 4 answer-engine tokens), sitemap excellent. The inspector publishes the rule
behind each label and a command per number; those commands were not re-executed one by one here beyond the
four shared metrics.

## 8. Other public observations

- **Meta description lengths** (A3): home `/` 252 characters, `/es/` 217, case study 265 (EN) / 248 (ES), the
  five Spanish notes 180–312; the remaining pages 136–191. The 120–160 range is a display convention, not
  evidence, and the inspector says so; the numbers are recorded because they will change.
- **HSTS** (A13): `max-age=31536000` without `includeSubDomains` or `preload`. `X-Content-Type-Options:
  nosniff` is present. Transport security is a security property, not a legibility one, and is listed here
  as fact only.

## 9. Findings and open items

None of these is a defect against a published rule; each is a fact the owner may want to act on.

1. **Five Spanish notes without hreflang and without an English twin** (§2). Consistent with single-language
   content; whether that is intended is `needs-verification`.
2. **Four sitemap entries without `<lastmod>`**: the two homes and the two notes listings (§2).
3. **The homes emit no `WebPage` node** and the entities carry no `logo`/`image` (§3); the inspector rates its
   own home "strong" here.
4. **Meta descriptions above 160 characters** on the homes, the case study and four of the five notes (§8).
5. **HSTS without `includeSubDomains`** (§8).
6. **Instrument hygiene, for anyone re-measuring:** a helper that strips `<noscript>` or uses a narrower
   entity regex reports 524 instead of 526 words (§4); a helper that prints decoded characters reports 9 360
   instead of 9 484 for `llms.txt` (§5). Both are definition gaps, not site changes. Only the recipe's
   definition carries the metric id.

## 10. Method notes

- Requests were made sequentially with pauses; the server is small. One connection timed out during the
  page walk at 13:43Z and succeeded on retry; the script in `tools/` now retries with backoff.
- The cookbook copy used is the **tag `v0.1.4` tarball**, not a working checkout. A working checkout whose
  tree lags its own HEAD once produced a stale `extract` filter (524 instead of 526 for this very page); the
  reproduction commands below therefore fetch the tag.
- Recipes were executed **as shipped** (their own `reproduce.sh --json`), with the live files placed in
  `before/`. Nothing in a recipe was re-implemented for the numbers that carry a recipe's metric id.
- A repeated fetch of the same page returned a different HTML byte count within the window (49 234 vs
  49 382 for `/`, different request headers; `curl -s 'https://zentimes.es/' | wc -c`, whose result depends on
  the request headers and is not expected to reproduce). HTML size is therefore not reported as a measurement.

---

## Appendix A — reproduction commands

All commands run against the public URL with `curl`, `perl` and Python 3 standard library. `tools/*.py`
refers to the scripts in this repository; each one is stdlib-only and prints its definitions in its docstring.
Cookbook recipes are fetched from the tag:

```sh
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)
```

### A1. Sitemap URL count

```sh
curl -s 'https://zentimes.es/sitemap.xml' | grep -o '<loc>[^<]*</loc>' | wc -l          # 27
curl -s 'https://zentimes.es/sitemap.xml' | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g'
```

### A2. lastmod per sitemap entry

```sh
curl -s 'https://zentimes.es/sitemap.xml' | grep -o '<lastmod>' | wc -l                  # 23
curl -s 'https://zentimes.es/sitemap.xml' -o sitemap.xml
python3 -c "import re;s=open('sitemap.xml').read();[print(re.search(r'<loc>(.*?)</loc>',u).group(1),'lastmod' if '<lastmod>' in u else 'NO-lastmod') for u in re.findall(r'<url>(.*?)</url>',s,re.S)]"
```

### A3. Canonical, hreflang, description length per page

```sh
python3 tools/check-sitemap-pages.py https://zentimes.es/sitemap.xml
# prints one line per URL: HTTP status, canonical OK/MISMATCH, hreflang set, description length, ids;
# then: canonical mismatches 0 · pages without hreflang 5 · distinct @id 60 (24 site-scope, 36 page-scope) · malformed 0
```

Single page, no script:

```sh
curl -s 'https://zentimes.es/es/notas/que-es-geo/' | grep -o '<link[^>]*hreflang[^>]*>'          # (empty)
curl -s 'https://zentimes.es/es/notas/que-es-geo/' | grep -o '<link[^>]*canonical[^>]*>'
curl -s 'https://zentimes.es/' | grep -o '<link[^>]*hreflang="[^"]*"' | grep -o 'hreflang="[^"]*"'   # en, es, x-default
```

### A4. @id census over the sitemap

Same script as A3 (its last three lines). The scope split is by prefix: an `@id` starting with
`https://zentimes.es/#` is site-scope; any other is page-scope. Malformed = more than one `#` or whitespace.

### A5. Typed entities and typed facts

Recipe, as shipped (the number that carries the metric id):

```sh
curl -s 'https://zentimes.es/' -o "$COOKBOOK/04-technical/structured-data-jsonld/before/index.html"
bash "$COOKBOOK/04-technical/structured-data-jsonld/reproduce.sh" --json | python3 -c "import json,sys;[print(m['id'],m['before_value']) for m in json.load(sys.stdin)['measurements']]"
# typed_facts 49 · typed_entities 9
```

Same definition on any URL, plus the raw `"@id":` count:

```sh
python3 tools/count-jsonld.py https://zentimes.es/        # jsonld_blocks=1 typed_entities=9 typed_facts=49 id_occurrences=14
python3 tools/count-jsonld.py https://zentimes.es/es/     # jsonld_blocks=1 typed_entities=9 typed_facts=49 id_occurrences=14
curl -s 'https://zentimes.es/' | grep -o '"@id":' | wc -l  # 14
```

### A6. Service @id parity EN ↔ ES

```sh
for p in '' 'es/'; do curl -s "https://zentimes.es/$p" | grep -o '"@id":"https://zentimes.es/#service-[a-z-]*"' | sort; done
# the same four lines twice: #service-geo-audit, #service-geo-implementation, #service-geo-monitoring, #service-technical-seo
curl -s 'https://zentimes.es/' | grep -o '"provider":{"@id":"[^"]*"}' | sort | uniq -c   # 4 × https://zentimes.es/#zentimes
curl -s 'https://zentimes.es/' | grep -c '"Offer\|"price\|"availability'                 # 0
```

### A7. Words visible without JavaScript

The recipe's `extract` filter verbatim (v0.1.4). On single-line HTML `sed` with `.*` is greedy and returns
0; `perl -0777` with `.*?` is what the recipe uses.

```sh
curl -s 'https://zentimes.es/'    | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&#?[a-z0-9]+;/ /gi; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w   # 526
curl -s 'https://zentimes.es/es/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&#?[a-z0-9]+;/ /gi; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w   # 555
```

Or the recipe as shipped:

```sh
curl -s 'https://zentimes.es/' -o "$COOKBOOK/04-technical/ssr-vs-csr-rendering/before/index.html"
bash "$COOKBOOK/04-technical/ssr-vs-csr-rendering/reproduce.sh" --json | grep before_value   # 526
```

### A8. robots.txt and the eight tokens

```sh
curl -s 'https://zentimes.es/robots.txt'                          # 11 groups, all "Allow: /", Sitemap: and Llms: lines
curl -s 'https://zentimes.es/robots.txt' | wc -c                  # 447 bytes (re-run 2026-09-23 14:44:48Z: 447)
curl -s 'https://zentimes.es/robots.txt' | grep -c '^User-agent:'  # 11
curl -s 'https://zentimes.es/robots.txt' -o "$COOKBOOK/04-technical/ai-crawler-access/before/robots.txt"
curl -s 'https://zentimes.es/llms.txt'   -o "$COOKBOOK/04-technical/ai-crawler-access/before/llms.txt"
bash "$COOKBOOK/04-technical/ai-crawler-access/reproduce.sh" --json | python3 -c "import json,sys;d=json.load(sys.stdin);[print(m['id'],m['before_value']) for m in d['measurements']];print(d['user_agents_tested'])"
# ai_user_agents_allowed 8 · llms_txt_bytes 9484 · the eight tokens tested
```

### A9. llms.txt size

```sh
curl -s 'https://zentimes.es/llms.txt' | wc -c   # 9484 bytes  (the recipe's unit)
curl -s 'https://zentimes.es/llms.txt' | wc -m   # 9360 characters
curl -s 'https://zentimes.es/llms.txt' | wc -l   # 70 lines
curl -s 'https://zentimes.es/llms.txt' | grep -o 'https://zentimes.es[^) ]*' | wc -l   # 31
curl -s 'https://zentimes.es/' | grep -c 'id="servicios"'   # 1 — the anchor llms.txt links to exists
```

### A10. Chunk self-containment and claim→source pairs

```sh
python3 tools/measure-live-page-with-recipe.py https://zentimes.es/    "$COOKBOOK"
python3 tools/measure-live-page-with-recipe.py https://zentimes.es/es/ "$COOKBOOK"
# converted content 395 / 419 words, 16 headings, 5 list items
# self_contained_chunks 4 · chunks_produced 4 · claim_source_pairs 5 · claims 5   (both pages)
# the converted markdown is written to ./last-conversion.md: read it before trusting the numbers
```

### A11. Anchor existence

```sh
curl -s 'https://zentimes.es/' | grep -o '<li[^>]*><a [^>]*href="[^"]*"' | grep -o 'href="[^"]*"' | grep -c '/casos/kenetg/#c4'   # 5
curl -s 'https://zentimes.es/' | grep -o '<li[^>]*><a [^>]*href="[^"]*"' | grep -o 'href="[^"]*"' | sort | uniq -c   # all list-item links (17 on 2026-09-23; 5 of them to #c4)
curl -s -o /dev/null -w '%{http_code}\n' 'https://zentimes.es/casos/kenetg/'                             # 200
curl -s 'https://zentimes.es/casos/kenetg/'    | grep -c 'id="c4"'                                       # 1
curl -s 'https://zentimes.es/es/casos/kenetg/' | grep -c 'id="c4"'                                       # 1
```

### A12. Inspector versus recipes

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/
# words_visible_no_js 526/526 · typed_entities 9/9 · ai_user_agents_allowed 8/8 · llms_txt_bytes 9484/9484 — EQUAL
# and the inspector's own sentence: cross-checked 2026-09-23 (13:32Z) v0.1.4 · Criteria v2026.09.2
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'data-metric="[^"]*"[^>]*data-value="[^"]*"'
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'data-fact="[^"]*"[^>]*data-level="[^"]*"'
```

### A13. Language roots and HSTS

```sh
curl -s -o /dev/null -w '%{http_code}\n' 'https://zentimes.es/en/'   # 404
curl -s 'https://zentimes.es/'    | grep -o '<html[^>]*lang="[^"]*"'   # lang="en"
curl -s 'https://zentimes.es/es/' | grep -o '<html[^>]*lang="[^"]*"'   # lang="es"
curl -sI 'https://zentimes.es/' | grep -i '^strict-transport-security:'   # max-age=31536000
```

### A14. English notes listing

```sh
curl -s 'https://zentimes.es/notes/' | grep -o 'href="/es/notas/[^"]*"' | sort -u   # the five Spanish notes and /es/notas/
curl -s 'https://zentimes.es/sitemap.xml' | grep -c '<loc>https://zentimes.es/notes/[^<]'   # 0 English note URLs
```
