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

- **v2026.11.1 and the site held to its own yardstick.** Criteria change: the main entity is now the one the graph itself declares as publisher of the WebSite; only if it declares none, the first root entity. Before, it depended on the order of the JSON-LD. It carries two new tests (72 in total) and was seen red by breaking it.

  **Fixes on the site after running the inspector over the 27 URLs of the sitemap.** Before there were 4 "low" ratings, all of them figures without a source:
  - on experiments, numbered footnote calls leading to their source: the GEO paper for the "+40 %", checked against its abstract on arXiv, and the work of Schulte et al. for the "±15.8";
  - on the case study, the "−83.3 %" card links to the measured page;
  - the business declares a logo;
  - the articles carry an image, and as headline the title visible on the page;
  - the visible dates carry their label;
  - the home illustration has a description: the first version exceeded the 125 characters of our own rule and the inspector caught it;
  - lastmod on the home and on the notes index.

  **Result measured live:** 27 of 27 pages rated strong or excellent. The four cross-check metrics did not move.
- **v2026.11.2: the h1 rule was unfair to titles that start with the brand.** Before, the h1 had to reflect the whole title. Now any of its segments split by `|`, `–` or `—` also counts, because "Brand — topic" is a legitimate convention, not an inconsistency. The test was seen red before the fix; there are 74 tests in total.

  **More changes on the site:**
  - titles aligned with their h1 on the home, the inspector, the services, the contact and the FAQ pages;
  - a table of contents with anchors on the case, the experiments, the notes, "about", the FAQ and the glossary;
  - a FAQ item opens on its own when reached through its link;
  - HSTS with `includeSubDomains`.

  **Honest consequence:** the `<title>` counts as text visible without JavaScript, so the home metrics moved: 529 words (526 before) and 9,574 bytes of `llms.txt` (9,484 before). The cross-check with the cookbook of 23-09 at 13:32Z no longer matched the live site. The reviewer redid it at 15:59Z with the pinned v0.1.4 recipes: 4 of 4 equal (529, 9, 8 and 9,574). The inspector now shows that time.

  **Result measured live:** 27 of 27 pages rated strong or excellent (519 excellent, 36 strong). The remaining "strong" labels are deliberate: the sitemap `lastmod` without a time where the time is not known, because nothing is invented.

## 2026-09-24

- **v2026-09-24: the criteria now start from defects.** The site owner ran the inspector over a prospect's site, a generic WordPress install whose home page has no text: 0 words in sentences without JavaScript and a content that was, in its entirety, one image. It still got 13 "excellent", which is the median of 58 real small businesses. The yardstick did not separate an empty site from a worked one.

  **Why it failed:**
  - Half the cards measured hygiene that any SEO plugin ships by default and called it "excellent".
  - What really separates one site from another, how much text there is to cite, came out "not rated".
  - The inspector looked at one page only, so it saw nothing of what was broken on the rest of the site.

  **What changed** (the site owner's decisions, with a specification produced by 9 agents and an adversarial critique that corrected 22 points):
  - Technical requirements become "Met / Not met" and never yield a quality label.
  - Every problem is a finding with a severity (critical, serious, moderate or minor) and caps the label of its block.
  - Only "substance" can reach "excellent": the words in readable sentences without JavaScript, compared against a published sample of 56 home pages of Spanish small businesses. "Excellent" is only the top 8 %, the same point Lighthouse uses for its green. It is a **convention** and is declared as one: the sample, the exact metric and the command that reproduces it are public; the names of the businesses are not.
  - What is required depends on the page type: a contact page is not measured in words.
  - Besides the requested page, 6 more pages of the site are checked, with a maximum of 24 requests in series, a 1 s pause between them, a stop on a 429 or a 503, and at most one inspection per site every 10 minutes.
  - From this version on, the name is the publication date: "v2026.10" read as October.

  **Tests:** 512, every new rule seen red before green, plus a fuzz of 80 hostile patterns that forced regular expressions of quadratic cost to be rewritten as linear.

  **Result measured live:**
  - the prospect's site goes from 13 "excellent" to 0: 2 serious (the home page with no content, and lorem ipsum on a page-builder demo page), 8 moderate and 4 minor over 7 pages checked.
  - zentimes.es/es/ is left with 0 findings, but its content comes out "low, on the edge": 290 words against a p25 of 294.8. The rule is not adjusted to our own figure: if we want more, the home page is expanded.

  **Many sites will drop without having changed: what changed is the criteria.**

  **A process failure, stated plainly:** this version was deployed without first going through the reviewer, as had been agreed. Its review is done after the fact, and whatever it breaks with evidence will come out as v2026-09-24.2.

- **Afternoon of 2026-09-24: the site answers a client's questions, not only a technician's.** The site owner set the goal: a business looking for help to show up in AI answers should find him by asking the AI. For two hours, client-style questions were asked in Gemini and ChatGPT and the site was changed according to what was measured.

  **What was measured** (anecdotal series; the detail is in the GEO reviewer's notebook, §76):
  - **A positive control was added:** a question whose answer is already known, at the start of every round.
  - **Gemini:** the control failed in every controlled condition: with the work account in a temporary conversation (0 of 5) and with no session in an isolated context (0 of 2). That day's Gemini hits happened inside the owner's personal account, with history, so they may be personalisation.
  - **ChatGPT** (temporary chat): the control passed in part of the rounds. When the business question mentioned "open source" or "GitHub", or asked for "an independent engineer who does the technical part himself", it named the owner first, citing zentimes.es and the Handbook. Without those words, it did not.
  - **Rule that stays:** a hit inside the account of the person being measured does not count, and every round starts with a control.

  **What was changed on the site, following the measured patterns:**
  - In purchase questions, the engines cite pages whose title says the intent phrase literally. In response:
    - the inspector is now titled "Herramienta GEO gratuita: comprueba si la IA puede leer tu web — en español y sin registro" (free GEO tool: check whether AI can read your site, in Spanish and with no sign-up);
    - new page "Auditoría GEO gratis: qué ve la IA de tu marca — antes de pagar nada" (free GEO audit: what AI sees about your brand, before you pay anything);
    - new page "Método de medición GEO: panel fijo de consultas, con control — y sin prometer citas" (GEO measurement method: a fixed panel of queries, with a control, and no promised citations).
  - **New note:** "Tu empresa no sale en ChatGPT, o sale mal: son dos problemas distintos" (your business does not show up in ChatGPT, or shows up wrong: two different problems).
  - **Person, repository and service in one text:** the open-source page opens by saying who the owner is and that this is the method of his consulting practice; "About me" is titled "independent GEO consultant in Madrid"; the home says "I publish the method as open source, on GitHub".
  - **The mini-audit** is presented across the site as "a photo of today, not a measurement".
  - **The eight versions** on the open-source page (all of them were stale) now come from the ecosystem manifest, and the deployment stops if they drift again.
  - **Hand-written test counts** are replaced by links to the tests that run on GitHub.
  - **The inspector card** that said "cross-checked on …" next to a figure now says that what was cross-checked was the calculation, not that value. It was a finding of the public ledger.

  **What was deliberately not done:**
  - **Prices:** not published; the owner decides them.
  - **The word "freelance"** is not used, because of a possible company with a partner.
  - **Mentions:** the texts for CreceRank, Alvargonzález and Pillitteri are prepared but have not been sent without his approval.

  **The honest part:** as of 2026-09-24, in a client's condition, the owner does not appear in Gemini. In ChatGPT he appears only with the words that describe his method. Everything changed today has to be measured again in a few weeks, from outside his account.
