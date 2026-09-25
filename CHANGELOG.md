# Changelog — zentimes.es, a dated ledger of the work

What was done on the public site https://zentimes.es, newest first, from 2026-09-22 onward. This is a record,
not source code. Every number in it carries three things: the date and time (UTC), the instrument that produced
it, and a command that reproduces it against the live site. A number without a command is not in this file.

**How to read the numbers.** Two instruments appear. *Cookbook v0.1.4* means a recipe of The GEO Cookbook at tag
`v0.1.4` (2026-09-22, concept DOI 10.5281/zenodo.22299279,
https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook), named by its recipe path, run as its
own `reproduce.sh`. *Public inspector* means https://zentimes.es/tools/ai-inspector/, which prints a command next
to every value. "Before" values are what the working record of each measurement says was measured on the date
given; the pre-change pages are no longer served, so they cannot be re-run. "After" values were re-run by the
author against the live site on 2026-09-23 between 13:52Z and 14:25Z, with the command shown, and matched unless
the entry says otherwise. Anything not backed by a public URL or by cookbook v0.1.4 is marked `needs-verification`.

**What none of this claims.** No entry says that any change increases citation by an AI engine. Cookbook v0.1.4
grades the engine effect of every recipe as `experimental`; the inspector's labels and every metric here grade
**preconditions** of machine legibility (structure, access, identity), never whether an engine retrieves, ranks,
generates or cites. Where a page of the site used to say more than that, this ledger records the withdrawal.

**Reproducing a recipe on a live page.** A cookbook recipe reads files, not URLs. To measure a served page you
download the tag, copy the recipe directory, write the fetched content into its `before/` files and run the
recipe's own script:

```sh
# the pinned instrument (a tarball of the tag, never a moving branch)
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)
# a recipe that reads HTML, robots.txt or llms.txt: drop the live files in before/ and run it
curl -s 'https://zentimes.es/' -o "$COOKBOOK/04-technical/ssr-vs-csr-rendering/before/index.html"
bash "$COOKBOOK/04-technical/ssr-vs-csr-rendering/reproduce.sh" --json
```

The two recipes that read Markdown (`03-content/chunk-friendly-structure`, `06-measurement/citation-anchoring`)
need the page converted from HTML to Markdown first. The conversion is the fragile part: links must be kept as
`[text](url)` before tags are stripped, a link that wraps a heading must not be flattened, and relative `href`s
must be resolved to absolute URLs because the anchoring recipe only recognises `http(s)://`. Each of those three
mistakes produced a false number on 2026-09-22 before it was caught, so a conversion count (words, headings, list
items) is printed next to every number taken this way.

---

## 2026-09-25

### Citation panel, round T0 (2026-09-24 23:39Z to 2026-09-25 00:31Z): the baseline before the first IndexNow notification

First round of the panel fixed in [`criteria/citation-panel-2026-09-24.md`](criteria/citation-panel-2026-09-24.md),
run **before** the site's first IndexNow notification, so it measures the engine's older copy of the index while the
pages changed on 2026-09-24 were already live. 43 questions, 52 minutes, no stop, one visible model throughout
(`gpt-5-6`), every run in a temporary chat; the account check (no custom instructions, memory off, empty chat
history) was done at 23:35Z–23:37Z and its captures kept with the runs. Position was read by the reviewer after the
round and is reported as secondary information, with no threshold.

**Read against the convention.** Subject control 1 of 3: the round is valid, and the control's own variability is
the same seen on 2026-09-24 (4 of 13). External control 2 of 2: the Barcelona third parties appeared both times and
the author never did, so the instrument is comparable with the exploratory series. F1 (technical person): 3 of 4,
each time in first position, including one of the two Sevilla-plus-remote runs, which had no baseline. F2 (open
method): 1 of 2, first position. **F3 (cold, by need) 0 of 24 and F4 (cold, by person) 0 of 6:** the cold baseline
is zero, as the exploratory series said (0 of 19 there), and the two naive questions added before the round are at
0 of 6. F5 (accuracy) 2 of 2: both answers describe the author as a software and security engineer in Madrid, cite
only his own pages, state correctly that no prices are published, attribute **no figure** to him, and apply neither
"freelance" nor "agencia" to him (the word appears once, in the engine's offer to compare against agencies). The
three price questions (F3-10) name other providers and attribute nothing to the author.

Nothing here says anything went up or down: this is the baseline. The next rounds are read against it, per family,
accumulated, and the first claim needs four rounds.

### Round T0 — 43 runs, 2026-09-24T23:39Z to 00:17Z; visible model: gpt-5-6, —

Condition: account unrelated to the person measured, temporary chat, memory off, no custom instructions (checked before the round), one fixed network exit. Hit = surname in the answer and one of his own pages cited. `declined` never counts as a no. Position noted by the reader; third parties are not named here.

| id | family | UTC | state | own URL cited | position |
|---|---|---|---|---|---|
| GC-a | GC | 23:39 | no | — | — |
| GC-b | GC | 23:40 | no | https://github.com/ferinazumaDEV/generative-engine-optimization-handbook/blob/main/docs/06-measurement.md | — |
| GC-c | GC | 00:29 | hit | https://github.com/ferinazumaDEV/generative-engine-optimization-handbook, https://zentimes.es/ | 1 |
| CE-a | CE | 23:41 | no | — | — |
| CE-b | CE | 00:31 | no | — | — |
| F1-1-r1 | F1 | 23:42 | hit | https://zentimes.es/, https://zentimes.es/es/ | 1 |
| F1-1-r2 | F1 | 00:00 | hit | https://zentimes.es/es/ | 1 |
| F1-3-r1 | F1 | 23:43 | no | — | — |
| F1-3-r2 | F1 | 00:01 | hit | https://zentimes.es/ | 1 |
| F2-4-r1 | F2 | 23:45 | no | — | — |
| F2-4-r2 | F2 | 00:03 | hit | https://zentimes.es/ | 1 |
| F3-10-r1 | F3 | 23:52 | no | — | — |
| F3-10-r2 | F3 | 00:10 | no | — | — |
| F3-10-r3 | F3 | 00:26 | no | — | — |
| F3-15-r1 | F3 | 23:53 | no | — | — |
| F3-15-r2 | F3 | 00:11 | no | — | — |
| F3-15-r3 | F3 | 00:27 | no | — | — |
| F3-16-r1 | F3 | 23:54 | no | — | — |
| F3-16-r2 | F3 | 00:12 | no | — | — |
| F3-16-r3 | F3 | 00:28 | no | — | — |
| F3-5-r1 | F3 | 23:46 | no | — | — |
| F3-5-r2 | F3 | 00:04 | no | — | — |
| F3-5-r3 | F3 | 00:18 | no | — | — |
| F3-6-r1 | F3 | 23:47 | no | — | — |
| F3-6-r2 | F3 | 00:05 | no | — | — |
| F3-6-r3 | F3 | 00:19 | no | — | — |
| F3-7-r1 | F3 | 23:48 | no | — | — |
| F3-7-r2 | F3 | 00:06 | no | — | — |
| F3-7-r3 | F3 | 00:21 | no | — | — |
| F3-8-r1 | F3 | 23:49 | no | — | — |
| F3-8-r2 | F3 | 00:07 | no | — | — |
| F3-8-r3 | F3 | 00:22 | no | — | — |
| F3-9-r1 | F3 | 23:51 | no | — | — |
| F3-9-r2 | F3 | 00:09 | no | — | — |
| F3-9-r3 | F3 | 00:25 | no | — | — |
| F4-11-r1 | F4 | 23:55 | no | — | — |
| F4-11-r2 | F4 | 00:13 | no | — | — |
| F4-12-r1 | F4 | 23:56 | no | — | — |
| F4-12-r2 | F4 | 00:15 | no | — | — |
| F4-13-r1 | F4 | 23:58 | no | — | — |
| F4-13-r2 | F4 | 00:16 | no | — | — |
| F5-14-r1 | F5 | 23:59 | hit | https://zentimes.es/es/, https://zentimes.es/ | n/a (sujeto de la pregunta) |
| F5-14-r2 | F5 | 00:17 | hit | https://zentimes.es/es/ | n/a (sujeto de la pregunta) |

| family | hit | no | declined | of |
|---|---|---|---|---|
| GC | 1 | 2 | 0 | 3 |
| CE | 0 | 2 | 0 | 2 |
| F1 | 3 | 1 | 0 | 4 |
| F2 | 1 | 1 | 0 | 2 |
| F3 | 0 | 24 | 0 | 24 |
| F4 | 0 | 6 | 0 | 6 |
| F5 | 2 | 0 | 0 | 2 |

Subject control: 1 of 3 (valid). External control: the third party present in 2 of 2 (the author is expected not to appear; he appeared in 0).

## 2026-09-24

### Citation panel published before its first round (convention, ~21:30Z)

The measurement programme that will follow the changes of this day is fixed in
[`criteria/citation-panel-2026-09-24.md`](criteria/citation-panel-2026-09-24.md) before any round runs: fourteen
questions kept verbatim, a subject control and an external control, the conditions of the account and the engine,
what counts as a hit (presence of the author with one of his own pages cited; position reported separately), a
`declined` state that never counts as a "no", a stop rule, and the thresholds. The thresholds are a convention
and are marked as such; the only hypothesis in the file is labelled as one. The exploratory series of the same
day (65 runs) is the baseline the file quotes; its raw captures are not published. Round T0 is scheduled before
the site's first IndexNow notification, so that it measures the engine's older copy of the index.
Amended at ~23:45Z, still before T0: two naive client questions (15, 16) added to F3, verbatim from the operations
side's exploratory series of the evening, baseline 0 of 38.

### Afternoon changes verified live: intent phrases in the inspector titles, free-audit and method pages, a note, "a photo of today, not a measurement", open-source pages generated from the ecosystem manifest; home re-measured 575 · 9 · 8 · 10938 (4 of 4); the report's stale cross-check line found, reported, fixed and re-read (measured 20:00Z–20:17Z)

**Page changes, as reported by the operations side and checked by the reviewer on the live site at 20:01Z–20:02Z
(every URL HTTP 200; titles quoted verbatim from the served `<title>`):**

- The inspector landing pages carry the intent phrase in the title: EN `Free GEO checker: see if AI can read your
  website — no sign-up` (`/tools/ai-inspector/`), ES `Herramienta GEO gratuita: comprueba si la IA puede leer tu web
  — en español y sin registro` (`/es/herramientas/inspector-ia/`).
- New free-audit pages: `/es/auditoria-geo-gratis/` (`Auditoría GEO gratis: qué ve la IA de tu marca — antes de pagar
  nada`) and `/free-geo-audit/` (`Free GEO audit: what AI sees about your brand — before you pay anything`).
- New method pages: `/es/metodo/` (`Método de medición GEO: panel fijo de consultas, con control — y sin prometer
  citas`) and `/method/` (`GEO measurement method: a fixed panel of queries, with controls — and no promised
  citations`).
- New note: `/es/notas/tu-empresa-no-sale-en-chatgpt-o-sale-mal/` (`Tu empresa no sale en ChatGPT, o sale mal: son
  dos problemas distintos`).
- The ES home says `Publico el método en código abierto, en GitHub` (present in the served HTML of `/es/`).
- The phrase `foto de hoy, no una medida` ("a photo of today, not a measurement") qualifies the free mini-audit;
  the operations side reports it in 11 places, the reviewer saw it on the three ES pages fetched for it (the audit
  page, the method page and the note).
- The open-source pages (`/open-source/`, `/es/codigo-abierto/`) are now generated from the profile's
  `ecosystem-manifest.json` (generated 2026-09-23T18:12:05Z): **9 of 9 latest tags match** the manifest on both
  pages, and the stale `v 0.1.2` of the previous day is gone. The version is printed as `v 0.1.4` with a space, so
  a pattern that expects `v0.1.4` returns nothing (checked; the first pass of this comparison failed that way).
- `instagram.com/zentimesesp` appears in the `sameAs` of every page fetched (11 of 11).

The operations side's own account of the afternoon (goal, what was measured with a positive control, what was
changed and why, what was deliberately not done) is translated in
[`operations/03-decision-history.md`](operations/03-decision-history.md) under "Afternoon of 2026-09-24"; the
list above is the reviewer's check of that account against the live site.

**Measured by the reviewer, 2026-09-24T20:00Z–20:03Z, pinned cookbook v0.1.4 recipes through
`tools/compare-inspector-vs-recipes.py` on `https://zentimes.es/`:** `words_visible_no_js` **575** (539 at 13:43Z),
`typed_entities` **9**, `ai_user_agents_allowed` **8**, `llms_txt_bytes` **10938** (9332 at 13:43Z); `typed_facts`
51, not shown by the inspector. The request started a new inspection (report stamped `2026-09-24 20:00 UTC`);
its final `data-value`s read 575 · 9 · 8 · 10938 — **4 of 4 equal**. Words and `llms.txt` bytes rose with the pages
above; entities and agents did not move. Captures of the EN and ES saved reports at 20:03Z:
`criteria/captures/2026-09-24T2003Z-en-report-zentimes-home.txt`, `…-es-report-zentimes-home.txt`.

**Finding, closed the same evening:** on the cards of the 20:00 UTC run the cross-check line still reads `cross-checked 2026-09-24
(13:43Z) against cookbook v0.1.4` (ES `contrastado el 2026-09-24 (13:43Z) con cookbook v0.1.4`), for two values that
have changed since that cross-check (539 → 575, 9332 → 10938). The same lag was recorded on the 13:54 UTC run of the
morning. The line dates a cross-check the page did not perform on the values it prints; until it is derived from the
run itself (or removed), the re-run above is the cross-check that stands for 575 and 10938. Reported to the operations
side at 20:05Z. **Fixed and verified:** the operations side changed the line the same evening; the reviewer read the
report of the `2026-09-24 20:17 UTC` run at 20:17Z and each cookbook-metric card now says `the calculation (not this
value) was cross-checked against cookbook v0.1.4 on 2026-09-24 (20:00Z), on zentimes.es` (ES `el cálculo (no este
valor) se contrastó con el cookbook v0.1.4 el 2026-09-24 (20:00Z), sobre zentimes.es`), with the same four final values
575 · 9 · 8 · 10938. The line now states what was cross-checked (the calculation) and when, and no longer dates a
cross-check of the printed value. One observation stays: between 20:07Z and 20:15Z every request for the home returned
the "inspected very recently, try again in a few minutes" notice with no saved report behind it (the deploy had
emptied it), so the window a client sees after a deploy can be the notice alone, and it lasted about 17 minutes
after the 20:00 run rather than 10, because the operations side's own check in between restarted it.

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/     # 4 of 4: 575 · 9 · 8 · 10938 (COOKBOOK from the tarball step at the top of this file)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'data-metric="[^"]*"[^>]*data-value="[^"]*"' | sed -E 's/ data-recipe="[^"]*"//' | sort -u   # the four final values (the saved report inside the 10-minute window)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'the calculation \(not this value\) was cross-checked [^<]{0,80}' | head -1   # the cross-check line after the fix: what was cross-checked, and when
for u in /tools/ai-inspector/ /es/herramientas/inspector-ia/ /es/auditoria-geo-gratis/ /free-geo-audit/ /es/metodo/ /method/; do curl -s "https://zentimes.es$u" | grep -oE '<title>[^<]*' ; done   # the six titles above
curl -s https://raw.githubusercontent.com/ferinazumaDEV/ferinazumaDEV/main/ecosystem-manifest.json | grep -oE '"latest_tag": *"[^"]*"'   # nine tags to compare with the "v 0.1.x" printed on /open-source/
```

Nothing above measures citation by any AI engine. New titles and pages change what a machine can read, not
whether an engine cites the site.

### Criteria v2026-09-24 — requirements are met or not, every problem is a finding with a severity, only "substance" can reach excellent; Instagram in sameAs; skip link, `<main>` and shorter descriptions (measured 13:43:50Z, captured 13:54–13:57Z)

**Criteria v2026-09-24, as reported by the operations side and read on the page.** A redesign, not a delta:
technical requirements (response, HTTPS, indexing, robots, encoding, viewport, canonical, language, sitemap,
hreflang) print **Meets / Does not meet / Not applicable** (`data-level` `cumple` / `no-cumple` / `no-aplica`)
and never a quality label; every problem is a **finding** with a `data-severity` (`critico` / `grave` /
`moderado` / `menor`, displayed Critical / Serious / Moderate / Minor) that caps its block's label; only the
"substance" card (words in readable sentences without JavaScript, excluding menu, footer, cookie banner and
hidden text) can reach **Excellent**, by percentile against a reference sample of 56 Spanish SME home pages
(p92 or above, plus readability and repetition conditions and no content finding); every other rated card
is capped at Good. Up to 6 more pages of the site are checked, at most 24 requests in series with a 1 s
pause, stopping on a 429 or 503; one inspection per origin every 10 minutes. The report is now streamed: the
served HTML carries the cards that can still change twice, a provisional copy with `data-provisional="true"`
and the final one inside hidden containers; only the final copies are quoted in this ledger. The four
cookbook-metric cards keep `data-metric` / `data-recipe` / `data-value` and are computed as before. The page's
own history entry says results are not comparable with reports from earlier versions. Version names are now
the publication date. Rule text, vocabulary, the cuts (p25 294.8 · p50 521 · p75 948.8 · p92 1405.4) and the
home labels that moved against v2026.11.2: [`criteria/v2026-09-24.md`](criteria/v2026-09-24.md); the reference
sample (n, date, method, the 56 values, no site names): [`criteria/sample-sme-es-2026-09.md`](criteria/sample-sme-es-2026-09.md);
captures `criteria/captures/2026-09-24T1356Z-*-landing.txt` and `2026-09-24T1357Z-en-report-zentimes-home.txt`.
The operations side reports 24 citations checked before implementing, 5 of them corrected, and 512 tests
(`needs-verification` from outside).

**Page changes, as reported by the operations side:** the Instagram profile added to `sameAs` of the `Person`
and the `ProfessionalService` in EN and ES (the inspector's entity card now prints "3 sameAs (1 respond, 0
broken, 2 uncheckable)" and stays Good; the label was not lowered); a skip link; a `<main>` element in every
template; a note on the EN home; meta descriptions of 160 characters or fewer (the home's is 159, per the
inspector's "Page structure" card).

**Measured by the reviewer, 2026-09-24T13:43:50Z, pinned cookbook v0.1.4 recipes through
`tools/compare-inspector-vs-recipes.py` on `https://zentimes.es/`:** `words_visible_no_js` **539** (529 on
2026-09-23), `typed_entities` **9**, `ai_user_agents_allowed` **8**, `llms_txt_bytes` **9332** (9574 before);
`typed_facts` 51, not shown by the inspector. Inspector final `data-value`s read at about 13:57Z from the saved
report: 539 · 9 · 8 · 9332 — **4 of 4 equal**. `llms.txt` shrank from 9574 to 9332 bytes and the words rose from
529 to 539 with the page changes above. On the EN report of the 13:54 UTC run the cross-check line on the cards
still read `2026-09-23 (15:59Z)`, stale by its own wording for the two values that moved; the ES saved report
of the 13:57 UTC run, fetched once at 14:11Z (`criteria/captures/2026-09-24T1411Z-es-report-zentimes-home.txt`),
prints `contrastado el 2026-09-24 (13:43Z) con cookbook v0.1.4` with the same four values. The harness now
ignores the provisional copies (`data-provisional`) and waits out the 10-minute limit before re-requesting a
report.

**Process, as the operations side states in its own history:** the version was deployed before the reviewer's
pass, against what had been agreed; the review was done after the deploy. That post-deploy review found the
deployed reference curve (the 56 values behind the "substance" cuts) was not exported anywhere outside the
code; the operations side published the sample file the same day, and its translation is the file linked above.
The operations history entry is translated in [`operations/03-decision-history.md`](operations/03-decision-history.md).

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/     # 4 of 4: 539 · 9 · 8 · 9332 (COOKBOOK from the tarball step at the top of this file; the harness skips data-provisional cards and respects the 10-minute limit)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'data-metric="[^"]*"[^>]*data-value="[^"]*"' | sed -E 's/ data-recipe="[^"]*"//' | sort -u   # four lines: the metric ids and their values. data-recipe sits between the two attributes, so a pattern that expects them adjacent returns nothing (checked on both saved reports)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'Criteria v2026-09-24[^<]*' | head -1   # Criteria v2026-09-24 · <date and time of the run>
curl -s 'https://zentimes.es/' | grep -oE '"sameAs":\[[^]]*\]' | head -1   # three profile URLs, Instagram among them
```

A later request for the same origin does not start a new inspection: the ES request at 14:11Z returned the
saved report of the 13:57 UTC run with a notice line saying the same site is not re-inspected for a few
minutes. A client re-running the commands above should expect the saved report inside that window.

Nothing above measures citation by any AI engine. Under this version most labels grade only the absence of a
defect; "substance" grades a word count against a published sample, and the page says so.

## 2026-09-23

### Titles aligned with the h1, tables of contents, HSTS with includeSubDomains, criteria v2026.11.2, and the cross-check redone (measured 15:59:32Z)

**Criteria v2026.11.2, as reported by the operations side.** One rule changed: on the "Title, description and h1"
card the h1 may reflect the whole title or any of its segments split by `|`, `–` or `—`, not only the first;
under the previous rule a brand-first title ("Brand — topic") could never reflect the h1. One history entry
on the page, one test seen red before the fix, 74 tests in total. Delta file: [`criteria/v2026.11.2.md`](criteria/v2026.11.2.md)
(captures 17:20Z).

**Page changes, as reported by the operations side:** titles aligned with their h1 on the home, the inspector,
the services, the contact and the FAQ pages; tables of contents with section ids on the case, experiments, notes,
about, FAQ and glossary pages; a FAQ item opens when reached through its anchor; the `Strict-Transport-Security`
header now carries `includeSubDomains` with `max-age=31536000`.

**Measured** (reviewer, 2026-09-23T15:59:32Z, `tools/compare-inspector-vs-recipes.py` with the pinned cookbook
v0.1.4 recipes against `https://zentimes.es/`): 4 of 4 equal — `words_visible_no_js` **529** (526 in the
morning entries), `typed_entities` **9**, `ai_user_agents_allowed` **8**, `llms_txt_bytes` **9574** (9484 before);
`typed_facts` 51, not shown by the inspector. The two values that moved did so because the `<title>` counts as
visible text without JavaScript and the home title changed, and because `llms.txt` grew with the aligned titles.
The page's cross-check statement now reads `cross-checked 2026-09-23 (15:59Z) against cookbook v0.1.4` (verified
in the 17:20Z captures; 0 mentions of 13:32Z remain). HSTS header verified with `curl -sI` at 15:59Z.

**Reported, tagged `needs-verification` from outside:** 27 of 27 pages of zentimes.es rate strong or excellent
(519 excellent, 36 strong); the remaining strong labels are sitemap entries whose `lastmod` has no time because
the time is not known.

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/     # 4 of 4: 529 · 9 · 8 · 9574
curl -sI 'https://zentimes.es/' | grep -i '^strict-transport-security'            # max-age=31536000; includeSubDomains
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'cross-checked [^"<]*' | head -1
```

Nothing above measures citation by any AI engine; the labels grade preconditions.

### Entity gains logo and image, articles gain image and a visible headline, footnotes on the experiments page, and criteria v2026.11.1 — the main entity is the declared publisher (observed live 15:29Z)

**What changed in the JSON-LD, as reported by the operations side** (no `@id` touched; the 14 `@id` occurrences
and the 9 typed entities of the 22-09 entry stay as they were). The `ProfessionalService` gains `logo` and
`image`, both pointing to a stable 180×180 copy of the site icon (above the 112×112 minimum Google documents
for a logo). The `Article` nodes (the experiments page, the case page) and the `BlogPosting` nodes (the notes)
gain `image`, a stable 1200×630 copy of each page's Open Graph image. The `Article` `headline` now equals the
**visible h1** ("Measured, Not Claimed" / "Medido, no prometido" / "kenetg.com") instead of the long `<title>`:
the visible-structured-data card looks for the headline in the text the page shows without JavaScript, and a
`<title>` is not shown.

**What changed in the content, as reported by the operations side.** On `/experiments/` the paragraphs that
carry figures now carry footnote calls `[1]` and `[2]`. `[1]` is new: Aggarwal et al., arXiv:2311.09735, the
"up to 40%" figure, checked against the arXiv abstract that day. `[2]` is the existing Schulte reference, now
with `id="nota-2"` so the call resolves. On `/casos/kenetg/` the "−83.3 %" card links to the page where the
figure was measured, and the visible date carries the label "Actualizado el" (Updated on); the notes carry
"Publicado el" (Published on). The home illustration moves from decorative (`alt=""`) to a descriptive `alt`
(108 characters in one language, 112 in the other; the rule's cut is 125). Sitemap `lastmod`: the home is
dated 2026-09-23 and the notes index derives its date from the newest note.

**Criteria v2026.11.1, as reported by the operations side.** One change, with its history entry printed on the
page and two new tests (72 in total, all green; each seen red when its rule was broken on purpose): the main
entity — the node the structured-data, properties-per-type and sameAs cards rate — is the one the `WebSite`
declares as `publisher`; only if it declares none, the first root entity. Before, it depended on JSON-LD order
and picked the `Person` on this home although the `WebSite` declares `publisher` = the `ProfessionalService`.
The history entry, as printed on the page at 15:29Z, the one card whose convention it changes and the home
labels that moved: [`criteria/v2026.11.1.md`](criteria/v2026.11.1.md). The report prints `Criteria v2026.11.1 ·
2026-09-23` (capture `criteria/captures/2026-09-23T1529Z-en-report-zentimes-home.txt`, line 45). On the home
at 15:29Z: JSON-LD nodes **Excellent** (9; "9 typed nodes.", was Strong with "Missing: name, url and logo or
image on the entity"), properties per type **Excellent** ("1 of 1 complete.", was Strong "Organization missing
logo"), image alt text **Excellent** (`1/1`, was Not rated as decorative), sitemap still **Strong** but the
why moved from "Missing: lastmod." to "Missing: time in lastmod." (a date-only `lastmod` is strong by the
rule). 18 excellent · 3 strong · 9 not rated (15:03Z: 15 · 5 · 10).

**Measured by the reviewer, 2026-09-23 about 15:55Z, pinned cookbook v0.1.4.** `tools/compare-inspector-vs-recipes.py`
on the home: 4 of 4 equal, 526 · 9 · 8 · 9484, unchanged — the added properties are facts on existing nodes,
not nodes. `typed_facts` (a cookbook metric of the same recipe that the inspector does not show) moved **49 →
51** on the home, consistent with `logo` and `image` added to one entity and nothing else. On `/experiments/`:
`href="#nota-1"` and `href="#nota-2"` each resolve to exactly one `id`, the arXiv link is present, and the
JSON-LD `headline` reads `Measured, Not Claimed`.

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/   # 4 of 4 equal: 526 · 9 · 8 · 9484 (COOKBOOK from the tarball step at the top of this file)
python3 tools/count-jsonld.py https://zentimes.es/                               # typed entities 9 · typed facts 51 (49 before this entry) · "@id": 14
curl -s 'https://zentimes.es/experiments/' | grep -oE 'href="#[^"]+"' | sort | uniq -c   # one line per fragment target, with its count
curl -s 'https://zentimes.es/experiments/' | grep -oE 'id="nota-[0-9]+"'               # id="nota-1" and id="nota-2", once each
curl -s 'https://zentimes.es/experiments/' | grep -o 'arxiv.org/abs/2311.09735' | head -1
curl -s 'https://zentimes.es/experiments/' | grep -oE '"headline":"[^"]+"'              # "headline":"Measured, Not Claimed"
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'Criteria.{0,60}v2026\.[0-9.]+[0-9]' | sed 's/<!-- -->//g' | head -1   # Criteria v2026.11.1
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'data-fact="[^"]*"[^>]*data-level="[^"]*"'   # one line per rated card: token and level
```

**Measured: where the head ends for AI crawlers.** The framework the site runs on can stream page metadata
inside the `<body>` for user-agents it does not treat as HTML-limited — a defect found the same day on another
site and fixed there — so the reviewer measured, on `/`, `/es/notas/`, `/experiments/` and `/casos/kenetg/`
and with five user-agents (GPTBot, ClaudeBot, PerplexityBot, curl, Chrome), the byte offsets of `</head>`,
`<title`, `rel="canonical"` and the first `application/ld+json`. `<title>` sits at about byte 1,180 and the
canonical at about 1,500; `</head>` at about 3,600–4,100; identical for all five user-agents. Title and
canonical arrive inside the head for every crawler. The JSON-LD block sits right after `</head>` (about byte
4,050), that is, in the body. That is **not a defect** — Google reads JSON-LD in the head or the body — and it
is recorded so that a head-only harness does not mistake it for one.

```sh
for ua in GPTBot ClaudeBot curl; do curl -s -A "$ua" 'https://zentimes.es/' | grep -boE '</head>|<title|rel="canonical"|application/ld\+json' | head -4; done   # grep -b prints byte offsets; same four numbers per user-agent
```

**Reported, `needs-verification` from outside.** After the deploy, 27 of 27 pages of zentimes.es rate strong or
excellent on every card (before: 4 **Low** on figures with a source). A client can re-run the inspector on
each of the 27 sitemap URLs (`tools/check-sitemap-pages.py`); this ledger records the claim as the operations
side stated it, not as measured here. The 72-test count and the two-test breakage are likewise not observable
from outside.

As with every entry in this file: none of this measures whether any engine retrieves, ranks, generates or cites
the page. A logo that responds, a headline the page shows and a footnote that resolves are preconditions of
legibility; what an engine does with them is its decision.

### Criteria v2026.11 — rebuilt from verified evidence, labels that move, and a fetch defect fixed (observed live ~15:35Z)

**What changed.** The inspector's report now prints `Criteria v2026.11 · 2026-09-23`, one version after the
v2026.10 observed at 13:52Z (entry below). This version was not written by adding rules; it was rebuilt from
its sources. 64 cited sources were confirmed by a second reviewer and re-opened by that reviewer before release:
38 are backed by a literal sentence on the cited page as read on 2026-09-23; **4 statements were cited to the
wrong page** and were re-attributed (the 12-hour / 30-day robots.txt caching behaviour is on Google's robots.txt
specification page, not elsewhere; the 10-redirect-hop limit is on Google's HTTP status codes page; Googlebot's
2 MB fetch limit is on the Googlebot page dated 2026-02-03; the `lastmod` format is on sitemaps.org); **8
statements said more than their source** and were rewritten as inferences, marked as such on the page: treating
`429` like `5xx` is an inference from two Google pages, not RFC 9309; Google does not state what `Google-Extended`
does to AI Overviews; `nosnippet` / `max-snippet` for Bing is a convention, not a documented rule; "do not block by
IP" is Anthropic's advice only; Common Crawl implies but does not state robots.txt compliance; "content after
500 KiB is ignored" is Google's sentence, not the RFC's; "clear sourcing" is in Google's helpful-content guide,
not its AI-features guide. Full rule text of the v2026.11 cards, quoted from the English page:
[`criteria/v2026.11.md`](criteria/v2026.11.md).

**Labels that move, and why (from the page's own v2026.11 history entry).** Each item is a rule that was
stricter than its source, or a card that decided a level it had no ground to decide:

- one `h1` and a number of `h2` no longer required — HTML allows several `h1`;
- `x-default` no longer required — Google recommends it, does not require it;
- `og:url` and the title / description lengths no longer decide the level — the description has no limit per Google;
- redirects from the pasted URL no longer count against the page — Googlebot follows up to 10;
- no sitemap becomes **not rated** rather than a low label;
- HSTS preload not required — hstspreload.org itself does not recommend it;
- "no entity" becomes **not rated** on inner pages;
- robots.txt is evaluated on the page's own path for the 7 agents that decide appearing in search and answers
  (Googlebot, Bingbot, Applebot, OAI-SearchBot, Claude-SearchBot, Claude-User, PerplexityBot); training-crawler
  policy becomes informative;
- indexing is computed per engine (Google and Bing; the card shows the worse of the two);
- language, viewport and images move to a class `accessibility`, marked on the page as not a cookbook class;
- new cards: HTML size, encoding, valid `<head>`, crawlable links, hidden text (informative), visible structured
  data, owner and contact;
- outbound links and `llms.txt` become informative;
- "chunking for AI" is explicitly **not rated** — Google states no requirement to break content into small
  pieces. That is a statement about *rating*, not about the cookbook's chunk metric
  (`03-content/chunk-friendly-structure`), which measures a precondition and is unchanged.

**Vocabulary.** The class definitions printed on the page are the cookbook dataset's schema definitions,
verbatim: `technical-seo`, `aeo` and `geo-precondition` are defined by what the number finishes, not by who reads
it. `security` and `accessibility` are the inspector's own classes and are marked as not cookbook classes. The
four cards that carry a cookbook metric id keep the dataset's class (`typed_entities` stays `aeo`).

**Measured after release (2026-09-23 ~15:35Z, https://zentimes.es/, pinned cookbook v0.1.4 recipes through
`tools/compare-inspector-vs-recipes.py`).** 4 of 4 equal: 526 · 9 · 8 · 9484. The cross-check statement on the
cards still reads `13:32Z`, and that is correct: no `data-value` moved, so the statement was not re-issued. Home
labels observed: JSON-LD nodes **Strong** (9; entity missing `name` / `url` / `logo`), heading hierarchy
**Excellent** (1 `h1` · 5 `h2` · 0 skips · 0 empty), hreflang **Excellent** (`en, es, x-default`; 1 of 1 versions
link back), sitemap **Strong** (missing `lastmod`), transport **Strong** (HSTS one year, no `includeSubDomains`),
language **Excellent** and viewport **Excellent** (both `accessibility`), robots.txt for search engines and
assistants **Excellent** 7/7, outbound links informative (3 links, 2 respond, 1 uncheckable), figures with a
source **Not rated** (no percentages on the home). On https://zentimes.es/casos/kenetg/: article authorship
**Excellent** (author visible), indexing per engine **Excellent / Excellent**, figures with a source **Low** 0/1 —
the one percentage on the case page still links to nothing. That is a finding about the page, not about the
instrument, and it stays printed.

```sh
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/   # 4 of 4 equal: 526 · 9 · 8 · 9484 (COOKBOOK from the tarball step at the top of this file)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'v2026\.11' | head -1   # v2026.11
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -o 'data-fact="[^"]*"[^>]*data-level="[^"]*"'   # one line per rated card: token and level
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2Fcasos%2Fkenetg%2F' | grep -o 'data-fact="[^"]*"[^>]*data-level="[^"]*"'   # the case page: authorship, indexing per engine, figures 0/1
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https%3A%2F%2Fzentimes.es%2F' | grep -oE 'insp-regla-v"[^>]*>(<!-- -->)?[a-z-]+(<!-- -->)? · (<!-- -->)?v2026\.[0-9.]+[0-9]' | sed 's/<!-- -->//g; s/.*>//' | sort | uniq -c   # classes per card, all v2026.11
```

**Release checks, as reported by the operations side** (`needs-verification` from outside: a client cannot run
them). 70 tests over the real reading and criteria functions, all green; then five rules broken on purpose —
`noarchive` applied to Google as well; the ACT zoom threshold changed from `< 2` to `< 1`; Applebot evaluated
without inheriting Googlebot's group; a `canonical` outside `<head>` ignored; an hreflang without return link left
unpenalised — each turning only its own test red. One test carried a wrong expectation (the `<summary>` of a
closed `<details>` is visible text: 44 %, not 50 %) and the test, not the code, was fixed. Live measurement on
five sites before release, including a real **Low** on a well-known encyclopedia page whose JSON-LD `headline`
is a database description rather than the page title (visible structured data 0/2): the check finds a real
mismatch on a page nobody would suspect, which is what it is for.

**Instrument defect found and fixed in the same release, present since v2026.09** (reported by the operations
side; the dated entry in [`operations/03-decision-history.md`](operations/03-decision-history.md) will follow).
The fetch guard protected the connection but not the body read: a site that sends headers fast and the body
slowly raised an uncaught timeout, and the inspector page answered `HTTP 500` instead of a report. Now, if some
body arrived it is analysed with its own "slow" warning, kept separate from "truncated by size" so the HTML-size
card does not lie about why the page is short; if nothing arrived it is reported as a network error. The redirect
cap went from 4 to 10 hops (as Googlebot), each hop validated. Every label taken with v2026.09–v2026.10 on a
page that answered `200` is unaffected; what the defect hid was the reports that were never produced.

As with every entry in this file: none of these labels measures whether an engine retrieves, ranks, generates or
cites. A rule dropped for lack of a source is a rule dropped; it is not evidence that the practice is harmless.

### Criteria v2026.10 published on the inspector — observed live at 13:52Z

**What changed.** The inspector's report now prints `Criteria v2026.10 · 2026-09-23`. This is one version later
than the v2026.09.2 captured at 13:40Z in [`criteria/`](criteria/). The audit's comparison run at 13:49:53Z still
read `Criteria v2026.09.2` ([`audits/2026-09-23-public-surface.md`](audits/2026-09-23-public-surface.md), A12), so
the change went live between 13:49:53Z and 13:52Z. During the page walk three URLs had answered `502` for a few
seconds at about 13:45Z and `200` on retry; whether that was a deploy is not observable from outside. That is an
observation, not a measurement: it was transient and no command reproduces it. The history entry, as printed on
the page:

> **v2026.10 · 2026-09-23** — Closes the gaps that let incomplete pages score "excellent": indexing (noindex,
> nosnippet, X-Robots-Tag, which overrides everything), viewport, dates, article authorship, minimum properties
> per structured-data type, broken outbound links and figures with a source. The criteria now carry a review date:
> if nobody reviews them within 45 days, deployment fails.

**Measured.** 24 cards on the home report (17 under v2026.09.2). The seven new ones, by their `data-fact` token:
`indexacion`, `viewport`, `fechas`, `autoria`, `completitud`, `salientes`, `cifras`. On the site's own home page
they print: indexing **Excellent** ("No restrictive directives."), viewport **Excellent**, dates **None**,
authorship **Not rated**, figures with a source **Not rated** (read 13:52Z). The remaining two, read 2026-09-23
14:44:32Z–14:44:34Z: structured data completeness **Excellent** ("7 of 7 complete. 2 of 9 nodes are of types with
no minimum list (PostalAddress) and are not rated."), outbound links to other domains **Excellent** ("3 external
links · 3 checked: 2 respond, 0 broken, 1 uncheckable."). The site does not hide its own gaps.

```sh
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE '<div class="insp-item" data-fact="[^"]*"( data-level="[^"]*")?' | wc -l   # 24
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -o 'data-fact="[^"]*"[^>]*data-level="[^"]*"'   # one line per rated card: token and level (same grep as audit A12)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE 'data-fact="(completitud|salientes)"[^>]*>.{0,260}' | perl -pe 's/<!-- -->//g; s/<[^>]+>/ /g; s/\s+/ /g'   # the two cards' title, label and sentence (2026-09-23 14:44Z)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE 'Criteria.{0,60}v2026\.[0-9.]+[0-9]' | sed 's/<!-- -->//g' | head -1   # Criteria v2026.10
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE 'insp-regla-v"[^>]*>(<!-- -->)?[a-z-]+(<!-- -->)? · (<!-- -->)?v2026\.[0-9.]+[0-9]' | sed 's/<!-- -->//g; s/.*>//' | sort | uniq -c
# 12 technical-seo · 6 geo-precondition · 2 aeo · 1 security, all v2026.10 (21 labelled cards; re-run 2026-09-23 14:08Z)
```

`needs-verification`: the "review date … deployment fails" sentence describes a deploy-time guard that cannot be
observed from outside; it is quoted as printed. The rule text of the new cards is not captured in `criteria/`
(that folder holds v2026.09.2); a later capture should add it.

### Criteria v2026.09.2 — HSTS moves out of "response" into its own "transport" check

**What changed.** Under v2026.09.1 a page could be rated below excellent on *HTTP response* for lacking HSTS.
HSTS is transport security, not legibility: a lower "response" label would have told a client their page reads
worse when it does not. It became its own check, filed under the inspector's own class `security` (cookbook
v0.1.4's schema allows only `technical-seo`, `aeo` and `geo-precondition`). Reviewed and flagged before release.

**Measured on the home.** Transport: **Strong** — `max-age=31536000`, no `includeSubDomains`. Left visible as a
defect of the site's own page.

```sh
curl -sI 'https://zentimes.es/' | grep -i '^strict-transport-security:'   # strict-transport-security: max-age=31536000
```

Full rule text of the seventeen v2026.09.2 cards, quoted from the English page: [`criteria/v2026.09.2.md`](criteria/v2026.09.2.md).

### Criteria v2026.09.1 — the bar raised, and what was deliberately not raised

**What changed.** "Excellent" was redefined as *nothing verifiable is left to improve in that area*, and each
added step is a checkable practice with its source: HSTS of one year, complete Open Graph, `og:locale` matching
`<html lang>`, hreflang return links, the sitemap listing the page with `lastmod`, a JSON-LD graph linked by
`@id`, a heading hierarchy without skips, unique ids; new check for image alt text (WCAG 1.1.1).

**What was not tightened, and why.** Words without JavaScript and the number of `sameAs` links stayed as they
were, with the reason printed on the page: no data ties a word count or a `sameAs` count to any outcome, so a
higher bar would be invented. The recipe measured 6 → 152 words on its own fixture (`bash
"$COOKBOOK/04-technical/ssr-vs-csr-rendering/reproduce.sh" --json` on the `before/` and `after/` files shipped in
the v0.1.4 tarball; a fixture carries no date of its own — re-run from the tag tarball 2026-09-23 14:46:15Z: 6 and
152); zentimes.es prints 526; the
client site of the public case study prints 144 (2026-09-23 14:25Z; command under *Baseline before the work*).
None of those is a threshold.

**Consequence on the site's own page.** Under this version the home came out **Strong** on JSON-LD (no `WebPage`
node; entity without `logo`/`image`) and **Good** on title/description (252-character description against a
120–160 convention). Both are still printed under v2026.10.

```sh
curl -s 'https://zentimes.es/' | python3 -c 'import sys,re,html; d=re.search(r"<meta name=\"description\" content=\"([^\"]*)\"",sys.stdin.read()).group(1); print(len(html.unescape(d)))'   # 252
```

### Criteria v2026.09 — one label per check, the rule printed next to it, no overall score

**What changed.** The inspector went from printing bare values (22-09) to rating each check with a label
(`none / low / good / strong / excellent`, plus an unrated state), the rule that decides it, its evidence class
and a criteria version. A 0–10 score with decimals was considered and rejected: the weights would have been
invented. Reviewed against cookbook v0.1.4 before release.

**Why the version matters.** A label can change when the rule changes even if the site has not; a report someone
kept must be readable against the rule set that produced it. That is what [`criteria/`](criteria/) is for. Three
versions shipped this day before v2026.10; the history is printed on the page:

```sh
curl -s 'https://zentimes.es/tools/ai-inspector/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<[^>]+>/\n/g' | grep -E '^v2026\.'
```

### The cross-check against cookbook v0.1.4 redone at 13:32Z — 4 of 4, and why the 22-09 statement was wrong for one metric

**What changed.** The four inspector cards that share a metric id with the cookbook print
`cross-checked 2026-09-23 (13:32Z) against cookbook v0.1.4`. All four values equal the recipe's:

| metric id | recipe (cookbook v0.1.4) | recipe value | inspector `data-value` |
|---|---|---:|---:|
| `words_visible_no_js` | `04-technical/ssr-vs-csr-rendering` | 526 | 526 |
| `typed_entities` | `04-technical/structured-data-jsonld` | 9 | 9 |
| `ai_user_agents_allowed` | `04-technical/ai-crawler-access` | 8 | 8 |
| `llms_txt_bytes` | `04-technical/ai-crawler-access` | 9484 | 9484 |

Re-run by the author 2026-09-23 13:52Z with the recipes from the v0.1.4 tarball and the live files: 526 · 9 · 8 ·
9484 on both sides.

**The honest part.** The first statement, "cross-checked 2026-09-22 against v0.1.4", was **false for the words
metric**. The copy of the recipes used on 22-09 was not at the tag: its branch pointer said `v0.1.4`, but five of
the six `reproduce.sh` files were older than v0.1.4. The old word extraction blanks only named
entities (`&[a-z]+;`); v0.1.4 also blanks numeric ones, case-insensitively (`&#?[a-z0-9]+;` with flag `i`), so an
`&#x27;` inside "engine's" splits it into two tokens. The inspector had copied the old expression: 524 against the
true 526. The other three metrics are identical under both versions, so 3 of 4 had been checked correctly and one
against the wrong instrument. It was found because seven `robots.txt` fixtures gave opposite results in two runs.
The inspector was aligned to the v0.1.4 expression and the statement re-issued with the new date and time.

```sh
# v0.1.4 extraction (what the inspector publishes now)
curl -s 'https://zentimes.es/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&#?[a-z0-9]+;/ /gi; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w   # 526
# the stale extraction, for the record
curl -s 'https://zentimes.es/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&[a-z]+;/ /g; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w             # 524
curl -s 'https://zentimes.es/' | grep -o '"@type":' | wc -l          # 9
curl -s 'https://zentimes.es/llms.txt' | wc -c                       # 9484 (bytes; the count in characters is 9360 and is not the metric)
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE 'data-metric="[^"]*"[^>]*data-value="[^"]*"'
```

The `ai_user_agents_allowed` command is the RFC 9309 parser printed on the inspector's robots card (quoted in
full in [`criteria/v2026.09.2.md`](criteria/v2026.09.2.md), card 14); it prints `8`.

**Rule kept from this.** An instrument is read from a copy pinned to the tag, taken from the tag's tarball, and
each `reproduce.sh` is `diff -q`'d against that tarball before anyone trusts it. A `refs/heads/main` that names
the right commit does not prove the working tree is that commit. And the statement "cross-checked against
vX" names a version on purpose: the next cookbook tag makes it stale by its own wording until it is re-run. The
deploy guards fail if the statement's date is older than 120 days
([`operations/02-guards.md`](operations/02-guards.md); internal, `needs-verification` from outside).

### Menu moved from home anchors to pages — sitemap 21 → 27 URLs

**What changed.** The navigation became fixed and tiered, and its items lead to pages instead of anchors on the
home. Three new pages per language: `/services/`, `/about/`, `/contact/` and `/es/servicios/`, `/es/sobre-mi/`,
`/es/contacto/`. The four `Service` entities did not get new identifiers: they keep the site-scoped `@id`s minted
on 22-09 and appear unchanged on every page.

**Measured (2026-09-23 13:54Z).** 27 URLs in the sitemap, 23 with `<lastmod>`; 60 distinct `@id` across the
site, 24 site-scoped (hanging off the origin) and 36 page-scoped (hanging off a page URL), 0 malformed; canonical
equals the sitemap `<loc>` on all 27; 22 pages declare `hreflang` `en, es, x-default`. The 5 Spanish-only notes
under `/es/notas/<slug>/` declare no `hreflang`, which is consistent with having no English twin — recorded here
because the operations record first said "no page without hreflang", a sentence true only of the 22 paired
pages; that line of `operations/03-decision-history.md` was corrected on 2026-09-23 to "22 of 27".
Before: 21 URLs on the evening of 22-09 (operations record; `needs-verification`, the earlier sitemap is
not served any more).

```sh
curl -s 'https://zentimes.es/sitemap.xml' | grep -o '<loc>' | wc -l       # 27
curl -s 'https://zentimes.es/sitemap.xml' | grep -o '<lastmod>' | wc -l   # 23
python3 tools/check-sitemap-pages.py https://zentimes.es/sitemap.xml      # per-page status, canonical, hreflang, description length, @id count
python3 tools/count-jsonld.py https://zentimes.es/services/               # the four Service @ids, unchanged
```

The operations record also says the language switch now keeps the visitor on the same page instead of returning
to the home. Verified from outside 2026-09-23 14:07Z: each page links its twin directly (`/services/` →
`/es/servicios/`, `/es/servicios/` → `/services/`, `/faq/` → `/es/preguntas-frecuentes/`), so the switch lands on
the same page in the other language.

```sh
curl -s 'https://zentimes.es/services/'    | grep -oE '<a [^>]*href="/es/servicios/"[^>]*>[^<]*'   # <a href="/es/servicios/" hrefLang="es">ES
curl -s 'https://zentimes.es/es/servicios/' | grep -oE '<a [^>]*href="/services/"[^>]*>[^<]*'      # <a href="/services/" hrefLang="en">EN
```

### Home lightened — each passage lives in one place (chunks 4 of 4, anchoring 5 of 5)

**What changed.** When the menu moved to pages, three new pages were born carrying the home's copy: four URLs
with the same passages, each canonical to itself and in the sitemap. Neither cross-canonicals (the deploy guard
requires canonical == `<loc>` for every sitemap URL) nor pages left out of the sitemap were acceptable, so the
direction was inverted: the pages are the destination and the home summarises them in complete sentences with a
subject, never in "GEO audit — see more" labels, which no splitter can treat as a self-contained unit. The five
figures on the home kept their link to the proof.

**How duplication was measured, and a lesson about names.** Bag-of-words overlap gives 98% for literal copies but
also 57–62% for two different pages on the same topic, because it counts "the", "GEO" and "your". Six-word
n-grams separate the two: a literal copy shares hundreds, an honest summary shares one or two. Two correct
instruments answered different questions the same afternoon: whole sentences (split on `. ! ?`, six words or
more) found in full on the home → 0; six-word spans shared with `/about/` → 17. Both were right; the phrase
"duplication at zero" claimed more than the first measured. A figure is reported with its question beside it.
The four figures of this paragraph (98 %, 57–62 %, 0 sentences, 17 six-word spans) are `needs-verification`: the
two counting rules are not published as a script in `tools/`, and neither the time of the runs nor the exact
instrument was recorded beyond "the same afternoon".

**Measured (2026-09-23 13:53Z, cookbook v0.1.4 recipes run on the converted home; conversion: 395 words, 16
headings, 5 list items).**

| recipe | metric | value |
|---|---|---:|
| `03-content/chunk-friendly-structure` | `self_contained_chunks` / `chunks_produced` | 4 / 4 |
| `06-measurement/citation-anchoring` | `claim_source_pairs` / `claims` | 5 / 5 |

Words without JavaScript on the home went from 723 (22-09, 18:14Z; the stale-filter value, see the 22-09
cross-check entry — `needs-verification`, the v0.1.4 count of that day's page was never taken) to 526 (23-09,
v0.1.4 filter): the prose moved, the graph did not, because the entities are site-scoped and do not depend on
which page carries the text. The home's own chunk count on 22-09 was 6 chunks produced (working record; no
command was kept for it — `needs-verification`); its self-contained count that day was not recorded
(`needs-verification`).

```sh
# the five anchored figures and the anchor they point to
curl -s 'https://zentimes.es/' | grep -o 'href="/casos/kenetg/#c4"' | wc -l   # 5
curl -s 'https://zentimes.es/casos/kenetg/' | grep -o 'id="c4"'              # id="c4"
# the recipes: convert the page to Markdown (keep headings, paragraphs, list items and links; resolve relative hrefs),
# write it to <recipe>/before/article.md and run   bash <recipe>/reproduce.sh --json
```

### Inspector fixes: bare domains accepted, robots.txt wildcard per RFC 9309, URLs quoted in published commands

- **Bare domain.** The input was of type `url`, so the browser itself blocked `example.com` before the server saw
  it. Now any spelling is accepted and normalised. `?url=example.com` → report for `https://example.com/`.
- **Wildcard.** A site blocking every agent with `Disallow: /*` came out as "8 of 8 allowed": `*` and `$` were
  treated as literal text. The parser now follows RFC 9309 like the cookbook recipe (`*` matches any sequence, `$`
  anchors the end), verified on seven fixtures with identical results to the recipe. The fixture set is not
  public (`needs-verification`); the parser is, on the robots card.
- **Quoting.** Published commands carried the URL unquoted, so a crafted link could make whoever copied the
  command execute something. Every URL in a published command is now single-quoted.

```sh
curl -s 'https://zentimes.es/tools/ai-inspector/?url=example.com' | grep -o 'https://example.com/' | head -1
curl -s 'https://zentimes.es/tools/ai-inspector/?url=https://zentimes.es/' | grep -oE "curl -s[f]? 'https://zentimes.es/[^']*'" | sort -u
```

### Cookbook pull request #32 (`unresolved_fragment_links`) — reviewed by breaking it, cited by the inspector before it is tagged

The inspector's card *Links to sections of this page (#id)* says its rule is "the same as the cookbook's
`unresolved_fragment_links`, applied to the whole page". That id is **not in cookbook v0.1.4**; it is the check
proposed in https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/pull/32, open on
2026-09-23 (state re-checked 2026-09-23 14:07Z through the public API: open, not merged). `needs-verification`
until it is merged and tagged. The review was done by sabotage rather than by
reading: three deliberate breaks of the new function (never mark unresolved; accept a duplicated `id`; compare
case-insensitively), each making exactly the tests it should fail fail and nothing else, plus the dataset
regenerated byte-identical. Two facts about the check that matter for a site: it runs on `href`s as written, so
the live-page harness must feed it text **before** resolving relative URLs; and it goes into the recipe's JSON as a
`checks` entry, not a `measurements` one, because it is integrity of the primary number, not a new measurement.

```sh
curl -s 'https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/pulls/32' | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['state'],d['merged_at'])"   # open None
```

---

## 2026-09-22

### Cookbook v0.1.4 tagged — the instrument everything below is measured with

Tag `v0.1.4`, dated 2026-09-22 in its `CITATION.cff` and README version row; concept DOI 10.5281/zenodo.22299279.
The six recipes and what each emits: `chunk-friendly-structure` (`self_contained_chunks` / `chunks_produced`),
`ai-crawler-access` (`ai_user_agents_allowed` / `llms_txt_bytes`), `ssr-vs-csr-rendering`
(`words_visible_no_js`), `structured-data-jsonld` (`typed_facts` / `typed_entities`), `entity-clarity-sameas`
(`entities_resolved` / `entities`), `citation-anchoring` (`claim_source_pairs` / `claims`). A metric id shared
with the cookbook obliges the same definition: same files, same agent list, same unit; otherwise it is another
metric and gets another name. A change to an instrument that moves a number already published with a DOI is a
correction, not an improvement: new metric, new id, old ones untouched, and the correction announced.

### Service entities typed and linked by `@id` — 5 → 9 entities, 6 → 14 `@id` occurrences

**What changed.** The four services became `Service` nodes in the JSON-LD graph, each with a stable `@id` and a
`provider` reference to the business by `@id`. Before: 5 typed entities (`Person`, `ProfessionalService`,
`WebSite`, two `PostalAddress`) and 6 `"@id":` occurrences (three declarations, three references: `founder`,
`employee`, `publisher`). After: 9 entities, 14 occurrences (each `Service` adds two: its own and `provider`).

**The `@id` convention, fixed here and never changed since.** Three ways to break an identifier were caught
before publishing: deriving the fragment from localised text (English and Spanish would have minted two
entities for one service — the fragment comes from a stable key shared by all languages; only `name` and
`description` are localised); concatenating onto a constant that already carries a fragment (`…/#zentimes` +
`#service-x` gives a URI with two `#`); and a fragment without a type prefix (`#geo-audit` collides the day a note
with that title exists — `#service-geo-audit` costs seven characters and removes the problem). Two scopes:
**site-scoped** identifiers hang off the origin and are identical in every language (`#ferinazumaDEV`,
`#zentimes`, `#website`, the four `#service-*`); **page-scoped** ones hang off the page's canonical URL and
legitimately differ between languages (`#breadcrumb`, `#post`, `#case`, `#collection`, `#article`, `#webpage`).
No `OfferCatalog`/`Offer` without prices: markup that declares a commercial structure the page does not have is
scaffolding, and on the site of someone selling GEO it is the most expensive place to put it.

**A counting error worth recording.** Before the page was measured, 10 `@id` occurrences were expected for this
graph; the served page prints 14, and 14 is right: counting `"@id":` counts declarations and references together,
and each `Service` is referenced from the catalogue as well as declared. The rule kept: no expected figure,
template or threshold is written down before it has been measured on the live page.

```sh
curl -s 'https://zentimes.es/' | grep -o '"@type":' | wc -l                                  # 9
curl -s 'https://zentimes.es/' | grep -o '"@id":' | wc -l                                    # 14
curl -s 'https://zentimes.es/es/' | grep -o '"@id":' | wc -l                                 # 14 — same graph in Spanish
curl -s 'https://zentimes.es/' | grep -o '"@id":"https://zentimes.es/#service-[^"]*"' | sort -u   # the four Service ids, one '#' each
python3 tools/count-jsonld.py https://zentimes.es/                                           # entities, facts, @id count, same walk as the recipe
```

Instrument for the counts: cookbook v0.1.4 `04-technical/structured-data-jsonld` (`typed_entities` = objects
carrying `@type`, nested included). Re-run 2026-09-23 13:52Z: 9 and 14 in both languages, 0 malformed.

### Five figures on the home anchored to their proof — 0 of 5 → 5 of 5, anchor `#c4` verified to exist

**What changed.** The five measured figures on the home (JSON-LD blocks on the client's pages, distinct Schema.org
types, sitemap URLs with `lastmod`, endpoints answering 200, median TTFB) each got a link to the section of the
case study where they were measured, `/casos/kenetg/#c4` ("Result 04 — what is measured today"), in both
languages. Before: 0 of 5 carried a link (working record; the pre-change page is not served — `needs-verification`).

**How measured.** Cookbook v0.1.4 `06-measurement/citation-anchoring`, run as its own script on the home
converted to Markdown: `claim_source_pairs` 5 over `claims` 5. Two things the recipe does **not** check and were
checked separately: that the destination anchor exists (a link to a non-existent `#c4` scores 5/5 and fails the
reader, which is worse than not linking), and that the figure is true (linking only moves the burden of proof to
the linked method). Without the `<!-- claims:start -->` marker the recipe counts every list item as a claim; on
this page that coincides with the five figures, but it is a coincidence to watch.

```sh
curl -s 'https://zentimes.es/' | grep -o 'href="/casos/kenetg/#c4"' | wc -l        # 5
curl -s 'https://zentimes.es/es/' | grep -o 'href="/es/casos/kenetg/#c4"' | wc -l  # 5
curl -s 'https://zentimes.es/casos/kenetg/' | grep -o 'id="c4"'                   # exists
```

### Outcome-promise language withdrawn; the `llms.txt` count derived from data (four → five)

**What changed.** Two texts promised that an AI **would cite** the client, while the case study and the
experiments page declared that very measurement pending. They were rewritten to describe what is done and how it
is measured — a register of capabilities, not of outcomes. The surfaces a claim lives on were all checked, because
on this day the headline was corrected and the meta description left behind: body, summary, `<title>`, `<h1>`,
meta description, `og:description`, the page's JSON-LD `description`, `/llms.txt`, and the data file they all
derive from. Which two pages carried the promise is not in the public record (`needs-verification`); the
pre-change wording was not captured.

**As served now.** `<h1>`: "I make your brand citable by AI — and I publish the proof." `/llms.txt`: "Whether an
engine ends up citing you depends on the engine." The case study's status line: "GEO measurement still pending";
`/llms.txt` describes that page as stating the measurement "has NOT been done yet". *Citable* is a property of the
page; *cited* is the engine's decision, and the site says so. "Citable" is the site's own wording; no metric in
this ledger measures citability.

**`llms.txt`.** It said "four Python libraries" with five in the list — in the one file that exists to be read
by machines. The number is now derived from the list.

```sh
curl -s 'https://zentimes.es/' | perl -0777 -ne 'print "$1\n" if /<h1[^>]*>(.*?)<\/h1>/s' | sed 's/<[^>]*>//g'   # I make your brand citable by AI — and I publish the proof.
curl -s 'https://zentimes.es/' | grep -oE '<title[^>]*>[^<]*</title>|<meta[^>]+(name="description"|property="og:description")[^>]*>'
curl -s 'https://zentimes.es/llms.txt' | grep -o 'Whether an engine[^.]*\.'
curl -s 'https://zentimes.es/llms.txt' | grep -o '[0-9]* Python libraries[^,]*'     # 5 Python libraries installable from PyPI …
curl -s 'https://zentimes.es/casos/kenetg/' | grep -o 'GEO measurement still pending'
curl -s 'https://zentimes.es/llms.txt' | grep -o 'has NOT been done yet'
```

### English notes index states that the notes are in Spanish; `hreflang` on the index

**What changed.** `/notes/` lists Spanish-language notes. Its description now says so instead of implying English
content, and the index declares `hreflang` `en`, `es`, `x-default` with its Spanish twin `/es/notas/`. The five
notes themselves exist only in Spanish and declare no `hreflang` (see the 27-URL census above).

```sh
curl -s 'https://zentimes.es/notes/' | grep -o 'Written in Spanish for now[^.]*\.' | head -1
curl -s 'https://zentimes.es/notes/' | grep -oi '<link[^>]*hreflang[^>]*>'   # en, es, x-default (attribute is served as hrefLang)
```

### Glossary — 16 `DefinedTerm`, site-scoped `#glossary`, 14 with `sameAs`, 2 deliberately without

**What changed.** `/glossary/` and `/es/glosario/`: 16 terms as `DefinedTerm` nodes inside one `DefinedTermSet`
with `@id` `https://zentimes.es/#glossary` — site-scoped, identical in both languages, because the set of terms is
one thing whichever language describes it (each term's `@id` is `…/#term-<key>`, also site-scoped). 14 terms carry
a `sameAs` to the entity they name, each checked one by one. Two carry none on purpose: "GEO (Generative Engine
Optimization)" and "llms.txt". A `sameAs` to "something similar" would assert an identity that is false, and a
missing link is honest where a wrong one is not.

```sh
curl -s 'https://zentimes.es/glossary/' | grep -o '"@type":"DefinedTerm"' | wc -l                 # 16
curl -s 'https://zentimes.es/glossary/' | grep -o '"@type":"DefinedTermSet","@id":"[^"]*"'         # https://zentimes.es/#glossary
curl -s 'https://zentimes.es/es/glosario/' | grep -o '"@type":"DefinedTermSet","@id":"[^"]*"'      # same @id
python3 - <<'PY'
import json,re,urllib.request
h=urllib.request.urlopen(urllib.request.Request('https://zentimes.es/glossary/',headers={'User-Agent':'Mozilla/5.0'})).read().decode()
t=[n for b in re.findall(r'(?is)<script[^>]*ld\+json[^>]*>(.*?)</script>',h) for n in json.loads(b).get('@graph',[json.loads(b)]) if n.get('@type')=='DefinedTerm']
print(len(t),'terms;',sum(1 for n in t if n.get('sameAs')),'with sameAs; without:',[n['name'] for n in t if not n.get('sameAs')])
PY
```

Re-run 2026-09-23 13:52Z: 16 · 14 · without: GEO (Generative Engine Optimization), llms.txt.

### FAQ — 14 questions, `FAQPage` page-scoped, answers in the served HTML, `<details>` closed

**What changed.** `/faq/` and `/es/preguntas-frecuentes/`: 14 `Question`/`Answer` pairs. The `FAQPage` node is
page-scoped (`https://zentimes.es/faq/#faq`, `https://zentimes.es/es/preguntas-frecuentes/#faq`) because each
language version is a different document. The answers are in the HTML as served, inside `<details>` elements that
arrive closed: a client that does not run JavaScript reads them all, a person opens the one they want. Third-party
figures in the answers carry their source.

```sh
curl -s 'https://zentimes.es/faq/' | grep -o '"@type":"Question"' | wc -l                 # 14
curl -s 'https://zentimes.es/faq/' | grep -o '"@type":"FAQPage","@id":"[^"]*"'            # https://zentimes.es/faq/#faq
H=$(curl -s 'https://zentimes.es/faq/'); echo "$(echo "$H" | grep -o '<details' | wc -l) / $(echo "$H" | grep -o '<details[^>]*\bopen\b' | wc -l)"   # 14 / 0
```

### Public inspector launched — no score, `GET`, private targets refused, every published command executed

**What changed.** https://zentimes.es/tools/ai-inspector/ (Spanish: `/es/herramientas/inspector-ia/`) prints what
a client that does not run JavaScript sees on one page, each value with the command that reproduces it. The
report is a plain `GET` with `?url=`, server-rendered, so `curl` reads it without a browser. No overall score,
and the promise text above the form says no check measures whether an AI cites you.

**Guard against requests to internal networks.** A public tool that fetches arbitrary URLs is a server-side
request forgery surface. The inspector validates the target before connecting: only `http`/`https`, the name
resolved and private, loopback and link-local ranges refused, re-validated on every redirect, cut at 8 s or 2 MB
(the limits are from the operations record; `needs-verification` from outside). What the guard prints, observed
2026-09-23 13:53Z:

| target | printed |
|---|---|
| a loopback address, an address in a private range (RFC 1918) and the link-local metadata address (RFC 3927) — literal addresses are not written in this ledger by policy | "That address resolves to a private, loopback or link-local range. Not fetched, on purpose." |
| `http://localhost/` | "That host has no public domain, so it is not fetched." |
| `ftp://zentimes.es/` | "Only http and https." |

**Three published commands that did not return the number beside them, fixed the same day.** The word-count
command used `sed` with a greedy `.*` on HTML that arrives as a single line: it deleted from the first `<script`
to the last `</script>` and printed **0**. The JSON-LD card printed 4 types while its command returned 5 (a
nested node was skipped). The `llms.txt` card counted characters and called them bytes (8,312 against 8,405; 22-09
values of an inspector since changed and a file since changed — `needs-verification`).
Since then, **every published command is executed and must return the number printed next to it**; that check
caught three more (a command printing a list instead of a count, one printing a whole file, a half-fixed
`PostalAddress`). Rule: on single-line HTML, `sed` with `.*` cannot remove blocks; the recipe uses `perl -0777`
with a non-greedy `.*?`.

```sh
curl -s 'https://zentimes.es/tools/ai-inspector/' | grep -o '<form[^>]*>'                                        # method="GET"
curl -s 'https://zentimes.es/tools/ai-inspector/?url=http://localhost/' | grep -o 'no public domain[^<]*' | head -1   # no public domain, so it is not fetched.
# for the private/loopback/link-local branch, substitute any reserved address (loopback block, RFC 1918, RFC 3927) for localhost and grep 'Not fetched, on purpose'
curl -s 'https://zentimes.es/' | sed -e 's/<script.*<\/script>//g' -e 's/<[^>]*>/ /g' | wc -w                    # 0 — the 22-09 defect, still reproducible
curl -s 'https://zentimes.es/llms.txt' | wc -c                                                                   # bytes, the metric's unit
```

### First cross-check of the inspector against the recipes — 18:14Z, 4 of 4 (723 · 9 · 8 · 8405), later found stale for one metric

**What was measured.** The inspector and the cookbook v0.1.4 recipes were run on the same URL,
`https://zentimes.es/`. In the first pass **all four linked metrics differed, in definition and not only in
value**:

| metric | recipe | inspector | why |
|---|---:|---:|---|
| `words_visible_no_js` | 723 | 662 | the inspector did not strip `<style>` and entities as the recipe does |
| `typed_entities` | 9 | 4 | the recipe counts **nodes** with `@type`; the inspector listed **distinct types** and skipped nested ones |
| `llms_txt_bytes` | 8405 | 8312 | the inspector returned **characters**; the recipe, **UTF-8 bytes** |
| `ai_user_agents_allowed` | 8 | 7 | **different agent lists**: the recipe tests anthropic-ai, Applebot-Extended and Bytespider; the inspector tested OAI-SearchBot and ChatGPT-User |

Every value in this table is a 22-09 reading of an inspector that has since been changed and of a page and a
`llms.txt` no longer served; none can be re-run — `needs-verification`, all eight. The 723 is the stale-filter value
(see below), not a v0.1.4 count.

All four were aligned to the recipe the same afternoon; the recipe rules, being the instrument published with a
DOI that gives the metric its name. The inspector then exposed each value as `data-metric` / `data-value` so the
comparison reads attributes, not prose (a first parser read "04-technical/" as a number). Words closed at 725
against 723, two `&amp;` apart, then 723 = 723 at 18:14Z. The assistant-search agents got their **own** card and
their own name (`robots-busqueda`), so the cookbook id never carries two meanings.

**What the 23-09 correction says about this day.** The recipes were read from a stale checkout, so the 723 was
produced by the old word extraction. The v0.1.4 value for that day's page was not measured
(`needs-verification`); the other three metrics are identical under both versions and stood. The 22-09 sentence
"cross-checked with v0.1.4" was false for the words metric and was replaced on 23-09 (entry above).

### Sitemap 15 → 21 URLs; a contact button that did nothing; two deploy guards found lying

- **Sitemap.** 15 URLs on the morning of 22-09 (working record: the census of `@id`s that day walked 15 pages,
  0 malformed) → 21 that evening with notes index, glossary, FAQ and inspector pages in both languages
  (operations record; `needs-verification`, superseded by the 27 of 23-09).
- **Contact.** The "write to me" button was a `mailto:` and, with no mail client configured, did nothing. It now
  opens the system mail client and, if the page still has focus after 1.2 s, offers the usual providers
  (operations record; `needs-verification`, UI behaviour not tested here).
- **Guards.** Two checks in the deploy battery returned green without checking anything: the EN/ES service-id
  parity guard had ended up behind an `exit 0` and never ran; the title comparison passed for Spanish only because
  the Spanish title contains no `&` (`&amp;` against `&`). Both were fixed and each was broken on purpose in the
  place it lives before being trusted again ([`operations/02-guards.md`](operations/02-guards.md); internal,
  `needs-verification` from outside). The rule kept: a check is accepted only after it has been seen to fail, and
  expected values are derived from the source of truth, never written by hand beside it.

---

## Baseline before the work — measured on the morning of 2026-09-22

From the working record, with the instrument used (a no-JS word count with the same rules as the recipe, and the
`@id` census over the sitemap); the pages are no longer served, so these are `needs-verification` by
construction and kept here only so the deltas above have a starting point. Two "before" values exist for words on
the home on 22-09: 684 in the morning (this table) and 723 at 18:14Z (the first cross-check entry); the page
changed during the day. The 723 was produced by the stale word filter; which of the two filters produced the 684
is not written in the working record — `needs-verification`.

| what | value | after (this ledger) |
|---|---:|---:|
| words visible without JavaScript, home | 684 | 526 (2026-09-23) |
| typed JSON-LD entities, home | 5 | 9 |
| `"@id":` occurrences, home | 6 | 14 |
| sitemap URLs | 15 | 27 |
| `llms.txt` bytes | 8405 (22-09 18:14Z) | 9484 |
| AI agents allowed of the recipe's 8 | 8 | 8 |
| figures on the home linked to their proof | 0 / 5 | 5 / 5 |

For comparison, the client site that the public case study links to (`https://zentimes.es/casos/kenetg/` →
`https://kenetg.com/`) was measured on 2026-09-23 at 14:25Z with the same three commands used for the zentimes.es
home above (the no-JS word filter with the v0.1.4 `04-technical/ssr-vs-csr-rendering` entity rule, and the
`"@type":` / `"@id":` census): **144** words, **13** typed entities, **14** `@id` occurrences. The site used as
the case had a better graph than the site of the person selling the service; that is why this work started. An
earlier figure of 145 words for that page had been written without a command and is superseded by this one.

```sh
curl -s 'https://zentimes.es/casos/kenetg/' | grep -o 'href="https://kenetg.com/"' | sort -u   # the case page links the client site
curl -s 'https://kenetg.com/' | perl -0777 -pe 's/<script.*?<\/script>//gis; s/<style.*?<\/style>//gis; s/<!--.*?-->//gis; s/<[^>]+>/ /g; s/&#?[a-z0-9]+;/ /gi; s/\s+/ /g; s/^\s+|\s+$//g' | wc -w   # 144
curl -s 'https://kenetg.com/' | grep -o '"@type":' | wc -l   # 13
curl -s 'https://kenetg.com/' | grep -o '"@id":' | wc -l     # 14
```

---

## Open, as observed on 2026-09-23

- The inspector rates the site's own home **Good** on title/description (252-character description), **Strong**
  on transport (no `includeSubDomains`) and, under v2026.10, **None** on dates. Left visible on purpose; a tool
  that gives its maker "excellent" is not believed by anyone.
- `/llms.txt` links the four services to `https://zentimes.es/#servicios`, the home anchor, while `/services/`
  now exists. The anchor still exists on both homes (`curl -s 'https://zentimes.es/' | grep -o 'id="servicios"'`),
  so nothing is broken; whether the links should move to the pages is a decision not yet taken.
- The `#id` card cites `unresolved_fragment_links`, not yet in a tagged cookbook (pull request #32).

Author: Fernando Aporta Franco · ferinazumaDEV / Zentimes. Spanish mirror of the repository README:
[`README.es.md`](README.es.md). Records this ledger cites: [`METHOD.md`](METHOD.md), [`audits/`](audits/),
[`criteria/`](criteria/), [`operations/`](operations/), [`tools/`](tools/).
