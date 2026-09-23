# Operations — how the site is built, deployed and guarded

Four records written by the operations side, in Spanish, describing the stack, the deployment procedure, the
invariants that block a deploy, the decision history with before/after numbers, and what a client can verify
from outside. They are kept in the language they were written in; the facts they carry are the same ones the
English documents in this repository cite.

| file | what it records |
|---|---|
| [`01-stack-y-despliegue.md`](01-stack-y-despliegue.md) | Stack (Next.js, English at the root and Spanish under `/es`, typed content files, one page registry from which the sitemap, `llms.txt`, canonicals and `hreflang` are derived) and the deployment in eight steps: types → build → invariants against the local build → package → check → reversible swap → real `200` → rollback. No machines, paths, users or providers. |
| [`02-guardas.md`](02-guardas.md) | The nine deploy-guard invariants plus two more (EN/ES id parity, 120-day expiry of the cross-check statement), each with what breaks it — and the two guard failures of 2026-09-22: one that never ran, and one that passed only because the Spanish title has no `&`. |
| [`03-historial-de-decisiones.md`](03-historial-de-decisiones.md) | The decisions of 22–23 September 2026 with before/after numbers, and three defects found on our own site by our own inspector. |
| [`04-que-puede-verificar-un-cliente.md`](04-que-puede-verificar-un-cliente.md) | Seven checks anyone can run from outside, without an account anywhere. |

These are snapshots dated 2026-09-23. The history up to that date stays true; the defects listed on our own
site may already be fixed when you read this. The [changelog](../CHANGELOG.md) is where that gets recorded.
