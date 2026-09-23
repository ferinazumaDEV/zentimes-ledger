# Independent re-runs of the published commands

This folder is where anyone who re-runs a command from this ledger records the date, the command and what came
back, so the ledger is cross-attested and not only self-attested. To add an entry: copy the block below into a
new file named `YYYY-MM-DD-<who-or-what>.md`, keep the UTC window, list every command run and the result beside
the recorded value, and never edit a previous entry.

## 2026-09-23 · completeness review before publication

- **Window:** 2026-09-23 14:33:49Z–14:36:00Z
- **Run by:** an independent reviewer reading only this repository and the public URLs
- **Instrument:** cookbook v0.1.4 from the tag tarball; `curl`, `perl`, Python 3 standard library
- **Result:** 24 commands re-run verbatim (URL quoting and `$COOKBOOK` substitution only), 24 returned the
  recorded number. No command failed.

Line numbers refer to `CHANGELOG.md` as it stood at the time of the run; later edits shift them.

| CHANGELOG claim (line) | command run | recorded | observed 14:33–14:36Z | result |
|---|---|---|---|---|
| Sitemap 27 URLs (L188) | `curl … sitemap.xml \| grep -o '<loc>' \| wc -l` | 27 | 27 | pass |
| 23 `<lastmod>` (L189) | `… grep -o '<lastmod>' \| wc -l` | 23 | 23 | pass |
| Words without JS, v0.1.4 filter (L153) | `perl -0777 …&#?[a-z0-9]+;… \| wc -w` | 526 | 526 | pass |
| Stale filter, for the record (L155) | `perl -0777 …&[a-z]+;… \| wc -w` | 524 | 524 | pass |
| `llms.txt` bytes / chars (L157) | `wc -c` / `wc -m` | 9484 / 9360 | 9484 / 9360 | pass |
| `"@type":` / `"@id":` on `/` (L314–315) | `grep -o … \| wc -l` | 9 / 14 | 9 / 14 | pass |
| `"@id":` on `/es/` (L316) | same | 14 | 14 | pass |
| Four `Service` ids, one `#` each (L317) | `grep -o '"@id":"https://zentimes.es/#service-…' \| sort -u` | 4 lines | 4 lines, same ids | pass |
| Five `#c4` links EN / ES, anchor exists (L339–341) | `grep -o 'href="/casos/kenetg/#c4"' \| wc -l` etc. | 5 / 5 / `id="c4"` | 5 / 5 / `id="c4"` | pass |
| Glossary 16 `DefinedTerm`, 14 with `sameAs`, 2 without (L391, L394–399) | `grep` + the inline Python | 16 · 14 · GEO, llms.txt | 16 · 14 · same two | pass |
| FAQ 14 `Question`, 14 `<details>` / 0 open (L413–415) | as printed | 14 · 14/0 | 14 · 14/0 | pass |
| HSTS header (L86) | `curl -sI \| grep -i strict-transport-security` | `max-age=31536000` | identical | pass |
| Description length 252 (L109) | the inline Python | 252 | 252 | pass |
| 24 inspector cards, `Criteria v2026.10` (L65–66) | as printed | 24 · v2026.10 | 24 · v2026.10 | pass |
| Evidence-class tally under v2026.10 (L67–68) | as printed | 12 · 6 · 2 · 1 | 12 · 6 · 2 · 1 | pass |
| `data-metric`/`data-value` ×4 (L158) | as printed | 526 · 9 · 8 · 9484 | identical | pass |
| Cross-check statement on the page (L130) | grep `cross-checked` | 13:32Z v0.1.4 | 13:32Z v0.1.4 | pass |
| Inspector refuses `localhost` (L448) | as printed | "no public domain, so it is not fetched." | identical | pass |
| Form is `GET` (L447) | as printed | `method="GET"` | `method="GET"` | pass |
| Language switch link (L200) | as printed | `<a href="/es/servicios/" hrefLang="es">ES` | identical | pass |
| Withdrawn-promise wording (L364–367) | four greps | four strings | all four present | pass |
| `5 Python libraries` in `llms.txt` (L365) | as printed | 5 | 5 | pass |
| The 22-09 defect still reproduces (L450) | `sed` greedy | 0 | 0 | pass |
| PR #32 state (L271) | GitHub API | `open None` | `open None` | pass |

The three scripts in `tools/`, run with the v0.1.4 tarball, also matched the audit: `check-sitemap-pages.py` →
0 canonical mismatches · 5 pages without hreflang · 60 distinct `@id` (24/36) · 0 malformed (14:34:18–14:34:53Z);
`compare-inspector-vs-recipes.py` → 4 of 4 EQUAL, `typed_facts` 49 not shown (14:35:22–14:35:55Z);
`measure-live-page-with-recipe.py` → EN 395 w / 16 h / 5 li, 4/4 and 5/5; ES 419 w / 16 h / 5 li, 4/4 and 5/5.
Also confirmed: tag v0.1.4 published 2026-09-22T05:36:01Z (GitHub API); both DOIs resolve to zenodo.org (302);
whether the version DOI 22890558 is the record for v0.1.4 specifically was not opened → `needs-verification`.
