#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run two cookbook recipes on a LIVE page without re-implementing them. Python 3 stdlib only.

How it works: the recipe directory is copied to a temporary folder, the page's content is written
to its `before/article.md`, and the recipe's OWN `reproduce.sh --json` is executed. The `before`
value is the live page. The `after` value is the recipe's own fixture and is ignored here.

Recipes used (GEO Cookbook, pin the version by tag, never `main`):
  03-content/chunk-friendly-structure   -> self_contained_chunks / chunks_produced
  06-measurement/citation-anchoring     -> claim_source_pairs / claims

The fragile part is the HTML -> markdown conversion, so its counts (words, headings, list items)
are printed next to the numbers and the converted markdown is written to ./last-conversion.md.
If the conversion lies, the number lies: audit it by eye.

Known limits of the conversion (each one produced a false number once before it was fixed):
  - links are converted to [text](url) BEFORE tags are stripped, otherwise anchoring counts 0;
  - a link that WRAPS a heading is left intact, otherwise the heading (a unit boundary) vanishes;
  - relative hrefs are resolved to absolute, because the anchoring recipe only matches http(s)://.
The citation-anchoring recipe counts EVERY markdown list item as a claim when the page carries no
<!-- claims:start --> marker; on a live page that is a coincidence, not a design.

Usage:
  python3 measure-live-page-with-recipe.py <URL> <path-to-cookbook-checkout>
e.g.
  curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
  python3 measure-live-page-with-recipe.py https://zentimes.es/ ferinazumaDEV-generative-engine-optimization-cookbook-*/
"""
import gzip
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

UA = {"User-Agent": "Mozilla/5.0 (compatible; public-audit/1.0)", "Accept-Encoding": "gzip"}
BASE = ["https://zentimes.es/"]


def fetch(url):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40)
    d = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        d = gzip.GzipFile(fileobj=io.BytesIO(d)).read()
    return d.decode("utf-8", "replace")


def to_markdown(page):
    h = re.sub(r"(?is)<(script|style|noscript|svg|head)\b.*?</\1>", " ", page)
    h = re.sub(r"(?is)<(nav|header|footer)\b.*?</\1>", " ", h)
    h = re.sub(r"(?is)<!--.*?-->", " ", h)

    def link(m):
        href, inner = m.group(1), m.group(2)
        if re.search(r"(?i)<h[1-6]\b", inner):
            return inner
        text = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", inner)).strip()
        if not text or href.startswith(("#", "javascript:", "mailto:")):
            return text
        absolute = urljoin(BASE[0], href)
        if not absolute.startswith(("http://", "https://")):
            return text
        return f"[{text}]({absolute})"

    h = re.sub(r'(?is)<a\b[^>]*\bhref=["\']([^"\']+)["\'][^>]*>(.*?)</a>', link, h)
    pieces = []
    for m in re.compile(r"(?is)<(h[1-6]|p|li)\b[^>]*>(.*?)</\1>").finditer(h):
        tag = m.group(1).lower()
        text = re.sub(r"(?s)<[^>]+>", " ", m.group(2))
        text = re.sub(r"&nbsp;", " ", text)
        text = re.sub(r"&amp;", "&", text)
        text = re.sub(r"&[a-z]+;|&#\d+;", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            pieces.append((tag, text))
    lines = []
    for tag, text in pieces:
        if tag.startswith("h"):
            lines.append("\n" + "#" * int(tag[1]) + " " + text + "\n")
        elif tag == "li":
            lines.append("- " + text)
        else:
            lines.append(text + "\n")
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip() + "\n"


def run_recipe(cookbook, recipe, content):
    with tempfile.TemporaryDirectory() as tmp:
        dst = Path(tmp) / "recipe"
        shutil.copytree(Path(cookbook) / recipe, dst)
        (dst / "before" / "article.md").write_text(content, encoding="utf-8")
        r = subprocess.run(["bash", str(dst / "reproduce.sh"), "--json"],
                           capture_output=True, text=True, timeout=180)
        if r.returncode != 0:
            return {"error": r.stderr.strip()[:300]}
        return json.loads(r.stdout)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    url, cookbook = sys.argv[1], sys.argv[2]
    BASE[0] = url
    md = to_markdown(fetch(url))
    print(f"== {url}")
    print(f"   converted content: {len(md.split())} words, "
          f"{len([l for l in md.splitlines() if l.startswith('#')])} headings, "
          f"{len([l for l in md.splitlines() if l.startswith('- ')])} list items")
    for recipe in ("03-content/chunk-friendly-structure", "06-measurement/citation-anchoring"):
        print(f"-- {recipe}")
        res = run_recipe(cookbook, recipe, md)
        if "error" in res:
            print(f"   ERROR: {res['error']}")
            continue
        for m in res.get("measurements", []):
            print(f"   {m.get('id', '?'):24} {m.get('role', ''):11} page={m.get('before_value')}")
    Path("last-conversion.md").write_text(md, encoding="utf-8")
    print("conversion written to ./last-conversion.md — audit it by eye before trusting the numbers")


if __name__ == "__main__":
    main()
