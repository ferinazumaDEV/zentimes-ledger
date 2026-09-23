#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Per-page checks over every URL in a site's sitemap.xml. Python 3 stdlib only.

For each <loc> in the sitemap it fetches the page and reports:
  - HTTP status
  - whether <link rel="canonical"> equals the sitemap <loc> exactly
  - the set of hreflang values declared with <link rel="alternate" hreflang="...">
  - the length in characters of <meta name="description"> (after HTML-unescaping)
  - the number of JSON-LD nodes carrying both @type and @id (a rough @id census)

Usage: python3 check-sitemap-pages.py [https://zentimes.es/sitemap.xml]

Requests are sequential with a short pause: this is a small server.
"""
import gzip
import html
import io
import json
import re
import sys
import time
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; public-audit/1.0)", "Accept-Encoding": "gzip"}


def get(url, tries=3):
    """Fetch once; on a network error wait and retry (a small server may drop a connection)."""
    for attempt in range(tries):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40)
            d = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                d = gzip.GzipFile(fileobj=io.BytesIO(d)).read()
            return d, r.status
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if attempt == tries - 1:
                raise
            print(f"   retry {attempt + 1} after {type(e).__name__} on {url}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))


def ids_in(page):
    blocks = re.findall(r'(?is)<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', page)
    out = []
    stack = []
    for b in blocks:
        try:
            stack.append(json.loads(b.strip()))
        except ValueError:
            continue
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            if "@type" in x and "@id" in x:
                out.append(str(x["@id"]))
            stack.extend(v for v in x.values() if isinstance(v, (dict, list)))
        elif isinstance(x, list):
            stack.extend(x)
    return out


def main():
    sitemap = sys.argv[1] if len(sys.argv) > 1 else "https://zentimes.es/sitemap.xml"
    sm, _ = get(sitemap)
    sm = sm.decode("utf-8", "replace")
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sm)
    lastmod = len(re.findall(r"<lastmod>", sm))
    print(f"sitemap URLs: {len(locs)}   <lastmod> tags: {lastmod}")
    mismatches, no_hreflang, all_ids = 0, 0, set()
    for u in locs:
        body, status = get(u)
        page = body.decode("utf-8", "replace")
        m = re.search(r'(?is)<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', page)
        canonical = m.group(1) if m else None
        hl = sorted(set(re.findall(r'(?is)<link[^>]*rel=["\']alternate["\'][^>]*hreflang=["\']([^"\']+)["\']', page)))
        md = re.search(r'(?is)<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', page)
        desc_len = len(html.unescape(md.group(1))) if md else None
        ids = ids_in(page)
        all_ids.update(ids)
        ok = canonical == u
        mismatches += 0 if ok else 1
        no_hreflang += 0 if hl else 1
        print(f"HTTP {status}  canonical={'OK' if ok else 'MISMATCH ' + str(canonical)}  "
              f"hreflang={','.join(hl) or '-'}  description_chars={desc_len}  ids={len(ids)}  {u}")
        time.sleep(1.0)
    site_scope = {i for i in all_ids if i.startswith("https://zentimes.es/#")}
    print(f"\ncanonical mismatches: {mismatches}")
    print(f"pages without hreflang: {no_hreflang}")
    print(f"distinct @id: {len(all_ids)}  site-scope (hang off the origin): {len(site_scope)}  "
          f"page-scope (hang off a page URL): {len(all_ids) - len(site_scope)}")
    malformed = [i for i in all_ids if i.count('#') > 1 or ' ' in i]
    print(f"malformed @id (more than one '#' or whitespace): {len(malformed)}")


if __name__ == "__main__":
    main()
