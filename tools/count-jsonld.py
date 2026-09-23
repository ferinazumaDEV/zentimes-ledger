#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Count typed entities, typed facts and @id occurrences in a page's JSON-LD. Python 3 stdlib only.

Same definitions as cookbook v0.1.4, recipe 04-technical/structured-data-jsonld:
  typed entity = an object carrying @type (a list of types is still one entity)
  typed fact   = a key on a typed object other than @context and @type
plus the raw count of the string "@id": (declarations and references together).

The authoritative instrument is the recipe's own reproduce.sh; this file restates its walk so
that a stranger can run it against a live URL without the recipe's before/after layout.

Usage: python3 count-jsonld.py https://zentimes.es/
"""
import gzip
import io
import json
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; public-audit/1.0)", "Accept-Encoding": "gzip"}


def get(url):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40)
    d = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        d = gzip.GzipFile(fileobj=io.BytesIO(d)).read()
    return d.decode("utf-8", "replace")


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://zentimes.es/"
    page = re.sub(r"<!--.*?-->", "", get(url), flags=re.DOTALL)
    blocks = re.findall(r'<script[^>]*type\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>',
                        page, re.IGNORECASE | re.DOTALL)
    entities, facts, types = 0, 0, set()

    def walk(node):
        nonlocal entities, facts
        if isinstance(node, dict):
            if "@type" in node:
                entities += 1
                facts += sum(1 for k in node if k not in ("@context", "@type"))
                t = node["@type"]
                types.update(t if isinstance(t, list) else [t])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    for raw in blocks:
        try:
            walk(json.loads(raw))
        except ValueError:
            continue
    id_refs = len(re.findall(r'"@id"\s*:', " ".join(blocks)))
    print(f"{url}")
    print(f"jsonld_blocks={len(blocks)} typed_entities={entities} typed_facts={facts} id_occurrences={id_refs}")
    print(f"types={', '.join(sorted(types))}")


if __name__ == "__main__":
    main()
