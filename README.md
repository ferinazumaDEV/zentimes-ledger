# zentimes.es — public ledger of the work

**English** · [Español](README.es.md)

**Author:** Fernando Aporta Franco ([ferinazumaDEV](https://github.com/ferinazumaDEV) / [Zentimes](https://zentimes.es))
**Started:** 2026-09-23 · **Instruments:** The GEO Cookbook v0.1.4 ([tag](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook/releases/tag/v0.1.4), DOI [10.5281/zenodo.22890558](https://doi.org/10.5281/zenodo.22890558)) and the site's public inspector

## What this repository is

A **public, dated, reproducible record** of the work done on <https://zentimes.es>: what was measured on the
public pages, with which instrument, on which date (UTC), and the command that returns the same number; the
rule sets the site's public inspector has printed, captured verbatim with their version; and the operations
side's description of how the site is built, deployed and guarded, plus the decisions taken with their
before/after numbers. Mistakes are recorded with the same detail as fixes: a ledger that only shows what went
right is not a ledger.

Every number here has three companions: its **date and time**, its **instrument** (a recipe path in cookbook
v0.1.4, the inspector with its criteria version, or a standard-library script in `tools/`), and the **command**
that reproduces it against the public URL. A number without a command is not written down. How this works
in detail, and what each measurement does and does not mean: [METHOD.md](METHOD.md).

## What this repository is not

- **Not the site's source code.** Nothing here builds or runs zentimes.es. There are no machine names,
  addresses, paths, accounts, keys or deployment scripts, and there will not be.
- **Not a promise of AI citation.** No number or label in this repository measures whether any AI engine
  retrieves, uses or cites a page, and none predicts it. The cookbook grades the *engine effect* of every one
  of its six techniques as `experimental`; its schema states that no evidence class measures retrieval,
  reranking, generation or citation; the inspector prints the same on every report. What is measured are
  **preconditions** of legibility — words present without JavaScript, typed facts a parser extracts, declared
  crawler access, chunks that stand alone, claims that carry a source — never the outcome.
- **Not a live view.** Each document is a snapshot dated in its header. The site changes; the record does not.

## Scope

- **Whose site.** zentimes.es is the author's own brand site; the work recorded here is work on the author's own
  pages, not on a client's.
- **In scope.** Everything <https://zentimes.es> serves publicly: every URL in its `sitemap.xml`, `robots.txt`,
  `llms.txt`, the public inspector and its reports.
- **Out of scope.** Any other site. Where another site appears (the client site the public case study links to
  is measured once in the CHANGELOG), it is a one-off comparison, not a subject of this ledger.
- **When it starts.** The ledger was started on 2026-09-23, mid-work, and reaches back to 2026-09-22. The
  "before" values of the pre-2026-09-22 baseline come from internal notes and cannot be verified independently:
  the earlier pages are not served any more, so those figures carry `needs-verification` by construction.

## How to read it

| Path | What it holds |
|---|---|
| [`METHOD.md`](METHOD.md) | The instruments, what each of the six recipes measures and its evidence class, why labels grade preconditions, the cross-check discipline, the controls, and what is not measured. |
| [`CHANGELOG.md`](CHANGELOG.md) | The dated ledger, newest first, from 2026-09-22: what changed on the public site, why, how it was measured and the command that reproduces it. Mistakes and withdrawals are entries like any other. |
| [`audits/`](audits/) | Dated audits of the public surface. Each number in the summary table links to the reproduction command in its appendix. |
| [`criteria/`](criteria/) | The inspector's rule sets as printed on the public page, one file per criteria version, with the raw captures under `captures/`. A report someone kept can be read against the rules that produced it. |
| [`operations/`](operations/) | Stack, deployment steps, the invariants that block a deploy, the decision history and what a client can verify from outside. Written by the operations side, in Spanish; no machines, paths, users or providers. |
| [`verification/`](verification/) | Independent re-runs of the published commands: who ran what, when, and whether the number matched. One file per re-run; first entry: [`2026-09-23-critic-rerun.md`](verification/2026-09-23-critic-rerun.md). |
| [`tools/`](tools/) | Python 3 standard-library scripts used by the audits. The two that touch a cookbook recipe run the recipe's own `reproduce.sh` unmodified; the two that restate a definition say so in their docstring. |
| [`CITATION.cff`](CITATION.cff) · [`LICENSE`](LICENSE) · [`LICENSES/`](LICENSES/) | How to cite this record (a dataset, version `2026.09.23`) and the full licence texts. |

Where a fact could not be verified against a public URL or the pinned cookbook, it is marked
`needs-verification` instead of asserted. Where two instruments disagree, the recipe published with a DOI
decides, and the disagreement is written down with both values.

## How to reproduce a number

Every command runs against the public URL with `curl`, `perl` and Python 3, no account anywhere. Recipes are
fetched from the **tag**, never from a moving branch:

```sh
curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
COOKBOOK=$(ls -d ferinazumaDEV-generative-engine-optimization-cookbook-*/)

# words a crawler that does not execute JavaScript can read on the home page — recipe as shipped
curl -s 'https://zentimes.es/' -o "$COOKBOOK/04-technical/ssr-vs-csr-rendering/before/index.html"
bash "$COOKBOOK/04-technical/ssr-vs-csr-rendering/reproduce.sh" --json | grep before_value
# 526 on 2026-09-23 13:41:52Z (audits/2026-09-23-public-surface.md, A7). The page may have changed since.
```

Then find the number in the audit, read the appendix entry it links to, and run that command. If your result
differs from the recorded one, the first question is the date: the site moves and the record does not. The
second is the instrument: the same name on a different version, or a helper that "does the same thing", is a
different instrument (see [METHOD.md §1](METHOD.md#1-the-instruments) for a two-word gap that came from
exactly that). If date and instrument match and the numbers still differ, the record is wrong: open an issue
with your command and output.

**Two kinds of change.** Changes to the *site* are recorded in [`CHANGELOG.md`](CHANGELOG.md); changes to *this
ledger* are recorded by the repository's own git history once it is published, and nowhere else.

## Licences

Prose and data (every `.md` file and every capture): **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)**,
full text in [`LICENSE`](LICENSE). Scripts under `tools/`: **MIT**, full text in [`LICENSES/MIT.txt`](LICENSES/MIT.txt).
The GEO Cookbook the measurements rely on has its own licence (CC BY 4.0 prose, MIT code) in its own repository.

## Next

Planned, not done:

1. A machine-readable data file (one row per number: UTC timestamp, URL, metric id or name, value, instrument,
   command reference), so a re-run can be diffed against this ledger mechanically.
2. A stable identifier per CHANGELOG entry and a table of contents at its top, so an entry can be cited.
3. A SHA-256 fingerprint, beside each number, of the *extracted* artefact it was measured on (the no-JS text,
   the JSON-LD block, `robots.txt`, `llms.txt`) — not of the raw HTML, whose size varies per request — so a
   reader can tell whether the page they fetch is the one that was measured.

---

Fernando Aporta Franco · ferinazumaDEV / Zentimes · <https://zentimes.es>
