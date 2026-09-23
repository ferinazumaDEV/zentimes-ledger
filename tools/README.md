# tools/ — the scripts the audits run

Four Python 3 scripts, standard library only, no account anywhere. Two of them run a cookbook recipe
**unmodified** (they copy the recipe directory, write the live files into its `before/` and run the recipe's
own `reproduce.sh --json`); the other two restate a definition so that a stranger can run it against a live
URL, and say so in their docstring. Only the recipe's own output carries a cookbook metric id.

| script | what it does | recipe |
|---|---|---|
| `measure-live-page-with-recipe.py <URL> <cookbook>` | converts the page to Markdown (conversion counts printed, result written to `./last-conversion.md`) and runs two recipes on it | `03-content/chunk-friendly-structure` · `06-measurement/citation-anchoring` |
| `compare-inspector-vs-recipes.py <cookbook> [URL]` | runs three recipes on the live files and compares each value with the inspector's `data-metric` / `data-value` | `04-technical/ssr-vs-csr-rendering` · `04-technical/structured-data-jsonld` · `04-technical/ai-crawler-access` |
| `count-jsonld.py [URL]` | typed entities, typed facts and `"@id":` occurrences on one page, with the recipe's definitions restated | (restates `04-technical/structured-data-jsonld`) |
| `check-sitemap-pages.py [sitemap URL]` | per sitemap URL: HTTP status, canonical == `<loc>`, hreflang set, description length, `@id` census | (no recipe) |

The cookbook argument is the directory of the **tag tarball**, never a moving branch:

```sh
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)
python3 tools/compare-inspector-vs-recipes.py "$COOKBOOK" https://zentimes.es/
```

The recipes themselves need `bash`, `perl` and `python3`, which is what the cookbook ships with. Requests are
sequential with a pause and retry with backoff: the site runs on a small server.

**Licence.** These scripts are released under the **MIT License** (`LICENSES/MIT.txt` at the repository root), following the cluster-wide policy that embeddable code is MIT and prose is CC BY-SA 4.0. Each script carries an `SPDX-License-Identifier: MIT` line. The prose of this README stays under the repository `LICENSE` (CC BY-SA 4.0).
