# Citation panel — the fixed questions, the controls and the conventions (published 2026-09-24, before the first round)

This file fixes, before any round is run, what the measurement programme of zentimes.es asks an AI engine, under
which conditions, what counts as a hit, and which thresholds will be read against the results. It is published
first so that the thresholds cannot move with the data. Rounds are recorded in the ledger as dated tables; the
raw captures (full answer text, links, screenshots) stay in the working directory and are not published.

**What this measures and does not.** A round measures whether an engine, asked a fixed question, names the
author and cites one of his own pages as a source. It does not measure ranking, traffic, or business outcome, and
no single round says anything went up or down. Everything here is a convention, declared as such, in the same way
the inspector's "substance" percentile is a convention.

## Conditions of every round

- **Engine:** ChatGPT, web search on (the engine searched the web in 65 of 65 runs of the exploratory series of
  2026-09-24, every cited link carrying `utm_source=chatgpt.com`). Gemini is excluded until a positive control
  passes in a client's condition (0 of 5 with a work account in a temporary conversation, 0 of 2 with no session,
  2026-09-24).
- **Account:** an account unrelated to the person being measured, **temporary chat**, memory and chat-history
  reference switched off, no custom instructions. The account is not named. The absence of custom instructions
  and memory is checked **in every round**, before the first question, and written into the round's table.
- **Network exit:** one, fixed; its geolocation is noted once per programme, not per round.
- **Per run, saved:** date and time (UTC), the visible model name, the full answer text, every cited link, and
  the `posicion` field (the place of the author in the answer's list: 1, 2, 3… or "—"), noted by the person who
  reads the answer.
- **Spacing:** at least 45 s between questions. A round is 43 questions, about 55 minutes. If the account's
  usage limit cuts the round, the rest runs the next day with the controls repeated in that half.

## What counts

- **Hit:** the author's surname appears in the answer **and** at least one cited link is one of his own pages
  (zentimes.es, or a repository under his GitHub account). Presence, not position. `posicion` is reported next
  to it as secondary information, with no threshold for now.
- **No:** an answer with sources that does not meet the two conditions.
- **`declined`:** no usable answer: usage limit, technical refusal, or a compact render without the full text
  when the question needs the text (F5 and any question about prices). **Never counted as a "no".**
- **Stop rule:** three technical refusals in a row, or a change in the visible model during the round, stops the
  round; the round is recorded as incomplete and does not count towards any threshold.

## Controls

- **Subject control (GC), ×3 per round.** Verbatim: «¿Qué desarrolladores independientes en España publican su
  trabajo de GEO (Generative Engine Optimization) en código abierto, por ejemplo en GitHub?» A round with 0 hits
  in the panel only counts if GC gives at least 1 of 3; otherwise the round is recorded as "control failed" and
  its zeros are not read as absence.
- **External control (CE), ×2 per round.** A question that, in the exploratory series, stably brought a stable
  third party (a Barcelona agency) and never the author. Verbatim: «Tengo un hotel pequeño en Barcelona. Busco a un
  ingeniero de software independiente, no un marketero ni una agencia, que sepa de GEO (lo de que ChatGPT te
  recomiende) y que haga él mismo la parte técnica: código, schema, estructura de la web. ¿Conoces a alguien así
  en Barcelona?» The subject control depends on the same pages that are being changed, so it cannot tell "the
  instrument changed" from "the site changed"; the external control can. If the third party disappears from both
  CE runs, the round is recorded as "instrument changed" and is not compared with earlier rounds. The same two
  runs serve as F1 (2) below; they are counted once.

The control questions are exploratory texts of 2026-09-24 kept verbatim, including their wording about agencies;
they are questions a client typed, not text of the site.

## The fixed panel (verbatim; each ×2, F3 ×3; 16 questions since the amendment of 23:45Z)

**F1 — the technical-person question (watch for regression).**
1. «Tengo un hotel pequeño en Madrid. Busco a un ingeniero de software independiente, no un marketero ni una agencia, que sepa de GEO (lo de que ChatGPT te recomiende) y que haga él mismo la parte técnica: código, schema, estructura de la web. ¿Conoces a alguien así en Madrid?»
2. The same with Barcelona (= CE above).
3. «Tengo un hotel pequeño en Sevilla. Busco a un ingeniero de software independiente, no un marketero ni una agencia, que sepa de GEO (lo de que ChatGPT te recomiende) y que haga él mismo la parte técnica: código, schema, estructura de la web. No me importa que trabaje en remoto. ¿Conoces a alguien así?»

**F2 — the open-method question.**
4. «Soy directora de marketing de una empresa de servicios. Quiero contratar a alguien para lo de aparecer bien en ChatGPT (GEO, creo que se llama), pero solo me fío de quien publique su método y su trabajo en abierto, por ejemplo en GitHub, para poder revisarlo antes. ¿Conoces algún consultor independiente en España así?»

**F3 — cold, by need (×3).**
5. «Tengo una clínica dental en Madrid. Antes de contratar nada quiero una auditoría GEO gratis: que alguien mire mi web y me diga qué ve la IA de nosotros y qué falla. ¿Quién ofrece algo así?»
6. «Soy socio de un despacho de abogados pequeño. ¿Existe alguna herramienta gratuita, en español y sin tener que registrarme, que me diga si ChatGPT o Gemini pueden leer bien mi web y entender a qué nos dedicamos? Lo de GEO lo he oído pero no sé por dónde empezar.»
7. «Soy director de marketing en una empresa mediana. Nos están vendiendo servicios de 'aparecer en ChatGPT' y todos prometen resultados. Yo quiero a alguien que me explique cómo se mide esto de verdad, que tenga un método de medición publicado y abierto y que no prometa que nos van a citar. ¿Conoces algún profesional o consultor en España así?»
8. «Llevo el marketing de una empresa de software B2B (un ERP para talleres). Hemos visto que ChatGPT, cuando alguien le pregunta por nosotros, se inventa cosas: dice que tenemos app móvil (no la tenemos) y nos confunde con otra empresa con nombre parecido. ¿Quién en España sabe arreglar esto? He leído que lo llaman GEO o algo así. Busco nombres concretos.»
9. «Tengo una tienda online y antes de contratar a nadie quiero entender bien esto del GEO. ¿Hay alguna guía o manual gratuito y abierto, en español, escrito por algún profesional español que además se dedique a ello? Así veo si sabe de verdad.»
10. «¿Cuánto cuesta contratar GEO en España para una pyme? Quiero cifras de profesionales concretos.»
15. «Tengo una tienda pequeña de ropa en Madrid. En una charla oí algo de eso que llaman GEO o algo así, para salir en las respuestas de la inteligencia artificial. ¿Quién hace eso en Madrid?»
16. «Hola, tengo un hotel en Madrid y me han dicho que ahora la gente busca hoteles preguntando a ChatGPT y que hay que hacer algo para salir. ¿Quién me puede ayudar con eso?»

Questions 15 and 16 were added on 2026-09-24 at ~23:45Z, **before round T0 ran**, from the operations side's
exploratory series of naive client questions of the same evening (40 runs, no positive control, so it counts sources
and not hits): with no expert cue in the question, zentimes.es was cited 0 times in 38; the two texts are kept
verbatim from that series (Y07-1 and Y03-1). They are the coldest questions in the panel; their baseline is 0.

**F4 — cold, by person.**
11. «Tengo una tienda online pequeña de cosmética natural que vende en toda España. En Google vamos bien, pero cuando le pregunto a ChatGPT por marcas como la nuestra nunca salimos. Me han dicho que eso es GEO. ¿Conoces a alguien en España que se dedique a esto de verdad, un profesional independiente y no una agencia grande?»
12. «¿Quién hace GEO en Madrid? Tengo una pyme y quiero salir en las respuestas de ChatGPT.»
13. «Busco un consultor GEO en España para una empresa de servicios B2B. ¿A quién me recomiendas?»

**F5 — accuracy (full text required).**
14. «¿Quién es Fernando Aporta Franco y qué ofrece Zentimes? ¿Tiene precios publicados?» Read for: figures
attributed to him (recorded with the exact sentence, target 0 without a source), the words "freelance" or
"agencia" applied to him, the city, and the name of the tool.

## Thresholds (convention, fixed before the first round)

- **Attributable signal:** the engine cites a page that did not exist before the change (on 2026-09-24, 0 of 65).
- **Cold families (F3, F4), per family, accumulated across rounds:** improvement is claimed at **6 or more hits in
  15**; 1–2 hits are noise; a page indexed for six weeks and still at 0 has its title and intent reconsidered, and
  no new page is added for it. *That 6 of 15 separates signal from noise under the variability seen on 2026-09-24
  (subject control 4 of 13 in the same condition) is a hypothesis without a measurement; it is the convention.*
- **F1:** baseline 16 of 21 (presence, exploratory series, 2026-09-24). A change is rolled back if the accumulated
  rate after it falls **below 50 % over 20 questions**, or if question (1) gives 0 of 2 in two consecutive rounds.
- **Geography:** if Barcelona or Sevilla start producing hits, the text and the index are checked first; the
  cities in the questions are never changed.
- **Prices:** figures attributed to the author without a source; target 0.
- **No claim of "up" or "down" from a single round.** A claim needs 7–8 accumulated repetitions per engine and
  family, that is, four rounds at ×2. In public, only the dated table.

## Schedule

- **T0:** before the first IndexNow notification of the changes of 2026-09-24; it measures the engine's older copy
  of the index.
- **T1 precondition:** the engine's web index shows the new titles and the engine's crawler has fetched the URLs.
- Then weekly for four weeks, then monthly.

*Convention published 2026-09-24 by the reviewer, on the decisions of the operations side of the same day.*
