# Decision history (server and site side)

> What was changed, when and why, with what was measured before and after whenever it was measured. It includes what went wrong: a record that only shows successes is not a record.

## 2026-09-22

- **The contact did not work.** The "Escríbeme" button (Spanish page; "write to me") was a `mailto:` and, with no mail client configured, nothing happened on click. Now it opens the system mail, and if after 1.2 s the page still has focus, a panel with the usual providers appears. The choice is remembered for 90 days, with no visible text.
- **A false figure in the `llms.txt`.** It said "four Python libraries" with **five** on the list. Right in the file that exists so that machines read it. Now the number is derived from the list.
- **Outcome claims rewritten as capability.** Two texts promised that an AI **would cite** the client, while the case study and the experiments page declared that measurement pending. They were rewritten: what is done and how it is measured is described, not an outcome nobody controls.
- **New sections:** notes with sources linked next to each claim (three anchored claims), a glossary of 16 terms (14 with `sameAs` checked one by one; two without it, because a `sameAs` to "something similar" would assert a false identity), frequently asked questions (14) and a public inspector. **Sitemap: from 15 to 21 URLs.**
- **The inspector publishes a command next to every figure**, so that it can be checked without taking anything on trust. That day the command itself failed several times, and it was fixed:
  - the word-count one returned **0**: a greedy pattern swallowed the whole document, which arrives on a single line;
  - the JSON-LD node count published **4 types** and its command returned **5** (a nested node was missing);
  - the `llms.txt` one counted **characters** while calling them **bytes** (8,312 versus 8,405).
  Since then, **every published command is run and has to return the number printed next to it**.
- **The inspector protects itself against requests to internal networks.** It validates the target before connecting, rejects private and loopback ranges, validates again on every redirect, and cuts off at 8 s or 2 MB.
- **First cross-check of the inspector against the cookbook recipes: 4 of 4.** Later it turned out that, for the word count, that cross-check had been made against an **old** copy of the recipe (see 09-23).

## 2026-09-23

- **Fixed, tiered menu**, leading to pages and not to anchors on the home. New pages for services, about me and contact. **Sitemap: 27 URLs.** Measured by an independent reviewer: **60 `@id`, none malformed, no page without `hreflang`**.
- **Lighter home:** summaries linking to each page. Measured: 4 of 4 self-contained fragments and 5 of 5 anchored claims.
- **Language switch that keeps the page**, instead of sending back to the home.
- **The inspector accepts the domain written in any form.** The field was of type URL and the browser itself blocked "example.com" before it reached the server.
- **An inspector failure, corrected:** a site that blocked every agent with the wildcard rule came out as "8 of 8 allowed". Now it follows the RFC 9309 standard the same way the cookbook recipe does, tested on seven cases.
- **A risk in the published commands, corrected:** the URLs went unquoted, so a crafted link could make whoever copied the command execute something. Now they are always quoted.
- **The inspector now rates each check**, with a label, the rule that decides it and a criteria version. No overall score. A 0-to-10 score with decimals was deliberately discarded: the weights would have been invented.
  - **v2026.09:** first version, reviewed against the cookbook before publishing.
  - **v2026.09.1:** bar raised. "Excellent" now means that nothing verifiable is left to improve in that area. The word count and the number of `sameAs` were not tightened, because no data supports a higher bar.
  - **v2026.09.2:** transport security (HSTS) leaves "response" and becomes a check of its own. It is security, not readability.
- **The word cross-check was redone.** The copy of the recipe used on 09-22 was old: it did not turn numeric references such as `&#x27;` into a space. The inspector gave 524 and the real recipe 526. The counter was aligned with the real v0.1.4 recipe and the new cross-check, on **2026-09-23 at 13:32Z, gave 4 of 4** (526, 9, 8 and 9,484).
- **The inspector found defects on our own site**, which are left in plain sight:
  - home meta description of 252 characters (the convention is 120-160);
  - the home without a `WebPage` node, and the entities without `logo` or `image`;
  - HSTS without `includeSubDomains`.
- **v2026.10: a bar of 10, and with a review date.** The gaps that let incomplete pages score "excellent" are closed:
  - **indexing:** `noindex`, `nosnippet` and `X-Robots-Tag`. If the page asks not to be indexed, the report warns about it at the very top, because it overrides everything else;
  - **viewport**;
  - publication and update **dates**;
  - **authorship** of articles;
  - **minimum properties** of each structured data type;
  - broken **outbound links**;
  - **figures with a linkable source**, in the same paragraph or in a footnote.

  The criteria now carry a **review date**: if 45 days pass without anyone reviewing them against the state of the field, the deploy fails. It was tested by breaking it: with a date 84 days old, the invariant suite FAILS. And inside the full deployment rehearsal, with the date at **46 days** (one day over the cap), the deploy **stops** (exit 1: "46 days without review, cap 45"). With the date restored, it passes.

  Two defects of the instrument were caught before publishing:
  - an `alt` with no value was counted as absent;
  - footnotes did not count as a source: Wikipedia came out with "0 of 3", and the manual check gives 3 of 3.

  New findings on our own site: the home declares no dates, and the BlogPosting of one note carries no `image`.
- **v2026.11: criteria rebuilt from verified evidence.** A workflow of 16 agents searched for sources (official documentation of the engines, standards, academic work). Another agent opened every one of them: 64 were confirmed and 20 were discarded, 17 of them because the source did not say what was attributed to it. Then an independent reviewer reopened the 44 sources that support labels already shown and corrected citations attributed to the wrong page and claims stronger than their source. What was an inference is written as an inference.

  **Own rules withdrawn for lack of evidence:** "a single h1", "mandatory x-default", "og:url equal to the canonical", title and description lengths, counting redirects from the pasted URL, mandatory sitemap and HSTS preload.

  **What comes in, with an official source:** robots.txt evaluated on the page's path for the seven search and answer agents; indexing directives per search engine (Google and Bing); valid head; encoding; HTML size; crawlable links; structured data visible on the page; responsible party and contact.

  **Tests:** 70 tests on the real functions, and five rules broken on purpose, each one red only in its own test. The four cookbook metrics did not move (526, 9, 8 and 9,484).

- **A defect of the instrument that had existed since the first version.** The inspector only protected the connection, not the reading of the page. A site that sends the headers fast and the body slowly caused an uncaught error, and the inspector answered 500. A real site uncovered it during prospecting. Now whatever was received is analysed and flagged as slow, a warning distinct from "truncated by size"; if nothing arrives at all, it is a network error. The redirect cap rises from 4 to 10, like Googlebot, and every hop keeps being validated.

- **The 70 rule tests now gate the deploy.** Reported by the operations side. The tests live in the project as a test file outside the framework's type-check, and the deployment script runs them right after the type-check, so a broken rule no longer deploys. It was tested by breaking it on purpose in the real project file: applying `noarchive` to Google as well made the deployment dry run exit 1 with "the Googlebot noarchive index rule does not count"; restoring the file (byte-identical) made the clean dry run exit 0, with 70 of 70 passing.
