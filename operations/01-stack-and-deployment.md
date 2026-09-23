# Stack and deployment of zentimes.es

> Contribution from the server side. Described without machine names, addresses, paths or users: what matters is **how** it is built and published, not **where**.

## What the site is

- **Next.js with React** (major versions deliberately not noted: they are a fingerprint), compiled in *standalone* mode (a self-contained Node server) and with plain CSS, no styling framework.
- **Two languages with separate routes**: English at the root (`/`) and Spanish under `/es/`. Every page exists in both, and they declare each other with `hreflang`, plus `x-default`.
- **Content lives in TypeScript files**, not in a database or a CMS. Every text, every service and every note is typed, and the compiler fails if a translation is missing.
- **A single page registry** from which the `sitemap.xml`, the `llms.txt`, the canonicals and the `hreflang` are DERIVED. Nobody writes them by hand. There are type assertions that fail at compile time if a route in the registry has no page or if a page is not in the registry.
- **JSON-LD structured data** with stable `@id` identifiers, scoped to the site (hanging off the origin) or to the page (hanging off the canonical). A published `@id` is never renamed.

## How it is published

A single command runs the whole path, and every step can stop it:

1. **Type check** of the entire project.
2. **Production build**.
3. **Local start of the compiled result** and execution of the invariant suite (see `02-guards.md`) **against that local server**, not against the published site. If anything fails, nothing is published.
4. **Packaging** and transfer to the machine that serves the site, over an encrypted channel.
5. **Package check** at the destination before touching anything.
6. **Reversible swap**: the new version is extracted next to the current one, it is checked that it has the essentials (server, static assets, public files) and they are swapped. The previous one is kept.
7. **Wait for a real 200** on `/`, `/sitemap.xml` and `/llms.txt`. It is not enough for the process to start.
8. **One-step rollback** if needed: the same command with `--rollback` restores the previous version.

There is also a **rehearsal mode** (`--dry-run`) that runs steps 1 to 3 without touching the published site.

## Why this way

- **Derive instead of writing by hand** because in a single day (2026-09-22) four cases of "fact corrected in one place and forgotten in another" showed up: the headline corrected and the meta description not, a count fixed and its list of types not… A fact does not live where it is written; it lives in the page, in the meta description, in `og:`, in the JSON-LD, in the `llms.txt` and in the command that reproduces it.
- **Verify against the local build and not against production** because a "0 FAIL" read without looking at the target ended up validating the old site instead of the new one.
