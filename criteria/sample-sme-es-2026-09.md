# Reference sample for "substance" · pymes-es-2026-09

This is the convention that decides the labels of the `sustancia` card of the zentimes.es AI inspector since
version **v2026-09-24**. It is published so that anyone can discuss it and measure it again. Following the
site owner's decision D4, **the URLs and the names of the small businesses are not published**: they are third
parties.

Translated from the operations side's published file (Spanish, 2026-09-24); numbers, identifiers and commands
are verbatim.

| Field | Value |
|---|---|
| id | `pymes-es-2026-09` |
| n | 56 (58 home pages of Spanish small businesses; 2 returned 403 and are excluded) |
| Kind of sample | convenience: the home pages of a commercial prospecting run, not a random sample |
| Capture | 2026-09-23, a single GET per home page, without JavaScript |
| Metric | `palabrasEnFrases` (words in sentences), measured with the **production reader** (TypeScript), not with the prototype |
| Fingerprint of the versioned lists (`huellaLecturas`) | `8a8aed070fbeaa0b` |
| Hash of the reader (`inspector-lecturas.ts`, sha256, first 16) | `62c1a05b804cb745` |
| Hash of the calibrator (`tools/calibra-sustancia.ts`, sha256, first 16) | `d52bbb425b3d066b` |

## Exact definition of `palabrasEnFrases`

1. **Visible text without JavaScript.** Removed:
   - `script`, `style`, `noscript`, `template`, `svg`, `iframe` and comments;
   - `[hidden]`, `aria-hidden="true"`, and inline `display:none` or `visibility:hidden`;
   - the classes in `OCULTAS_V1` (with the responsive exception);
   - the containers in `CONSENTIMIENTO_V1` (cookie banners), matched on the full class or id.
2. **Content root.** `main` or `[role=main]`; failing that, a single `article`; failing that, `body`. Inside
   the root, removed:
   - `nav` and `aside`;
   - the roles navigation, banner, contentinfo and complementary;
   - `header` and `footer`, unless inside an article, section or main;
   - form controls (but not the `<form>` itself).
3. **Template leftovers** (shortcodes and the like): extracted before counting.
4. **Segmentation.** Every block element is a boundary; `br` is not.
5. **Word.** A token with at least one Unicode letter or digit.
6. **Result.** The sum of the words of the segments of **10 words or more** (Kohlschütter et al., WSDM 2010).

## The 56 values, sorted

`0 54 74 75 76 151 173 173 183 188 190 197 289 294 295 304 331 353 386 391 397 410 414 415 444 496 501 505 537 537 573 626 647 682 743 765 769 775 819 876 901 946 957 1047 1099 1114 1232 1274 1294 1308 1346 1445 1464 1828 1964 3504`

## Control points

Computed by **linear interpolation**: position `(n−1)·p/100` over the sorted values.

| Point | Value | Recomputed here |
|---|---|---|
| p25 | 294.8 | 294.8 |
| p50 | 521 | 521.0 |
| p75 | 948.8 | 948.8 |
| p92 | 1405.4 | 1405.4 |

## The card's cuts (the site owner's decision D1)

| Label | Condition |
|---|---|
| none | under 250 characters in sentences (absolute threshold) |
| low | below p25 |
| good | p25 to p75 |
| strong | p75 to p92 |
| excellent | p92 or above, **and** readable (Readability 140/20), **and** under 15 % repeated blocks, **and** no content finding |

- **Why p92:** it is Lighthouse's green, which puts its 50 at HTTP Archive's p25 and its 90 at its p8. There
  less is better; with words more is, so their p25 and p8 are our p75 and p92.
- **Scope:** Spanish home pages only. Within 5 % of a cut the card says "on the edge" and the label does not
  change.
- **Declared limit:** Google, "there's no magical word count target". This compares against real small
  businesses and promises nothing.

## How to reproduce it

```
node --experimental-strip-types tools/calibra-sustancia.ts --comprueba <carpeta-con-los-html>
```

The calibrator measures each saved HTML file with the same reader the inspector uses. With the original folder
it reproduces the 56 values exactly; checked on 2026-09-24: "coincide: 56 valores" (matches: 56 values). With
your own sample you get your own curve. The folder of saved HTML files is not published (it holds the third
parties' pages), so from outside only the interpolation over the 56 values above can be re-run.

## What does NOT count

`curva-sustancia-2026-09.json`, from the `mide.py` prototype, is the curve **contaminated** by cookie banners
(p25 316 · median 536 · p75 962). It is marked as superseded and is not the deployed one.

## Next recalibration

Every 90 days, keeping the previous sample. Changing the control points requires a new version.
