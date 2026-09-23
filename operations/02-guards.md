# The guards: what is checked before publishing

> Every deploy of zentimes.es goes through a suite of invariants that runs **against the local build** before anything is uploaded. If any one fails, nothing is published. Here is what each one checks and **what breaks it**, because a guard that has never been seen failing is worth nothing.

## The page list is not written by hand

The suite **carries no page list**. It takes it from the `sitemap.xml` itself, which in turn comes from the page registry. It used to have the list written by hand: a new page was left out without anyone noticing, and a default branch waved it through. Now any route that does not match is a FAIL.

## The nine invariants

| # | What it checks | What breaks it |
|---|---|---|
| 1 | `/llms.txt` is alive and contains **all** the sitemap URLs | a new page that never reaches the `llms.txt` |
| 2 | **Entity** JSON-LD on both homes: Person, ProfessionalService, WebSite and PostalAddress, with `@id` and `sameAs` | losing a node or an identifier in one of the two languages |
| 3 | `robots.txt` **explicitly** allows the AI agents on the list | a block, or an agent no longer being named |
| 4 | the sitemap declares what it has to declare | missing pages, or extra ones |
| 5 | canonical and `hreflang` of every page, checked against the sitemap | a canonical that does not match its `<loc>`, or a language without its pair |
| 6 | the word "agencia" ("agency") does not appear | Zentimes is a personal brand, and the suite enforces it |
| 7 | the root is English, Spanish lives under `/es/` and the public URLs do not break; the expected titles **are derived** from the content, not written by hand | moving a published route, or changing a title without changing what is expected of it |
| 8 | `og:image` on every page: present, absolute and **actually being served** (200) | an image that is declared but does not exist |
| 9 | every important page is **reachable** from its home | an orphan page (it happened: it was detected and linked from the footer) |

## Two extra guards

- **Parity of service identifiers in English and Spanish.** The `@id` of the services have to be identical in both languages. If one language renames one, it fails.
- **Expiry of the equivalence with the cookbook.** The site's inspector states that its metrics match the cookbook recipes, **with a date and a version**. If that date ages past 120 days, the suite fails: an equivalence claim nobody revalidates becomes false without anyone touching a line.

## What we learned from the guards, with dates

- **2026-09-22 — a guard that was not running.** The EN/ES parity guard was written in the morning and tested by breaking it at that moment. Hours later it had ended up **behind an `exit 0`**, so it never ran, and from outside it looked exactly like one that always passes. It was moved, and tested again by breaking it **in the place where it lives**.
- **2026-09-22 — a comparison that passed by chance.** The title check compared against a literal. The Spanish title matched; the English one did not, because of `&` versus `&amp;`. The Spanish one passed only because it carried no `&`. Now the expected titles are derived from the content and unescaped before comparing.
- **The rule that comes out of this:** a check is accepted only after it has been seen failing, already integrated in its place.
