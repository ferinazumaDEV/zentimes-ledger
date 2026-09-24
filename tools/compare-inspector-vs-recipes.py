#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Two readings of the same URL: the public inspector on zentimes.es and the cookbook recipes.

If two instruments claim to measure the same thing and disagree, one of them is wrong. The
recipes are NOT re-implemented: each recipe directory is copied to a temporary folder, the live
files are written into its before/ and after/, and its own `reproduce.sh --json` runs. The
inspector side is read from the `data-metric` / `data-value` attributes its report exposes.

Python 3 stdlib only (the recipes themselves need bash, perl and python3).

Usage:
  python3 compare-inspector-vs-recipes.py <path-to-cookbook-checkout> [URL]
e.g.
  curl -sL https://api.github.com/repos/ferinazumaDEV/generative-engine-optimization-cookbook/tarball/v0.1.4 | tar -xz
  python3 compare-inspector-vs-recipes.py ferinazumaDEV-generative-engine-optimization-cookbook-*/ https://zentimes.es/
"""
import gzip
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

INSPECTOR = "https://zentimes.es/tools/ai-inspector/"
UA = {"User-Agent": "Mozilla/5.0 (compatible; public-audit/1.0)", "Accept-Encoding": "gzip"}
METRICS = {
    "04-technical/ssr-vs-csr-rendering": ["words_visible_no_js"],
    "04-technical/structured-data-jsonld": ["typed_entities", "typed_facts"],
    "04-technical/ai-crawler-access": ["ai_user_agents_allowed", "llms_txt_bytes"],
}


def fetch(url, timeout=60):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            d = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                d = gzip.GzipFile(fileobj=io.BytesIO(d)).read()
            return d.decode("utf-8", "replace"), r.status
    except urllib.error.HTTPError as e:
        return "", e.code


def run_recipe(cookbook, name, files):
    with tempfile.TemporaryDirectory() as tmp:
        dst = Path(tmp) / "r"
        shutil.copytree(Path(cookbook) / name, dst)
        for variant in ("before", "after"):
            for rel, content in files.items():
                (dst / variant / rel).write_text(content, encoding="utf-8")
        r = subprocess.run(["bash", str(dst / "reproduce.sh"), "--json"],
                           capture_output=True, text=True, timeout=180)
        if r.returncode != 0:
            return {"error": r.stderr.strip()[:200]}
        return {m["id"]: m["before_value"] for m in json.loads(r.stdout)["measurements"]}


def inspector(url):
    report, code = fetch(f"{INSPECTOR}?{urllib.parse.urlencode({'url': url})}", timeout=90)
    # Since criteria v2026-09-24 the report is streamed: the raw HTML carries every card twice, a provisional
    # copy marked data-provisional="true" and the final one. Only the final copy counts. The inspector also
    # allows one inspection per origin every 10 minutes; when it serves the "inspected too recently" notice
    # there is no report, and the values are left empty rather than read from a stale page.
    out, provisional = {}, {}
    for m in re.finditer(r'(?is)<[^>]*\bdata-metric=["\']([^"\']+)["\'][^>]*>', report):
        tag = m.group(0)
        v = re.search(r'\bdata-value=["\']([^"\']*)["\']', tag)
        if not v:
            continue
        val = int(v.group(1)) if v.group(1).isdigit() else v.group(1)
        (provisional if re.search(r"\bdata-provisional\b", tag) else out)[m.group(1)] = val
    for mid, val in provisional.items():
        out.setdefault(mid, f"{val} (provisional)")
    if re.search(r"(?i)hace muy poco|inspected .{0,30}recently", report):
        print("   notice: the inspector served its rate-limit notice (one inspection per origin every 10 minutes); no report")
    prose = re.sub(r"\s+", " ", re.sub(r"(?s)<[^>]+>", " ", re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", report)))
    stamp = re.search(r"cross-checked\s+(\d{4}-\d{2}-\d{2}\s*\(\d{2}:\d{2}Z\))\s+against\s+cookbook\s+(v[\d.]+)", prose)
    crit = re.search(r"Criteria\s+(v\d{4}[.\-]\d{2}[.\-\d]*)", prose)
    return out, code, (stamp.group(1) + " " + stamp.group(2)) if stamp else None, crit.group(1) if crit else None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cookbook = sys.argv[1]
    base = (sys.argv[2] if len(sys.argv) > 2 else "https://zentimes.es/").rstrip("/") + "/"
    page, c1 = fetch(base)
    robots, c2 = fetch(base + "robots.txt")
    llms, c3 = fetch(base + "llms.txt")
    print(f"== {base}   html={c1} robots={c2} llms={c3}")
    recipes = {}
    recipes.update(run_recipe(cookbook, "04-technical/ssr-vs-csr-rendering", {"index.html": page}))
    recipes.update(run_recipe(cookbook, "04-technical/structured-data-jsonld", {"index.html": page}))
    recipes.update(run_recipe(cookbook, "04-technical/ai-crawler-access", {"robots.txt": robots, "llms.txt": llms}))
    insp, code, stamp, crit = inspector(base)
    print(f"   inspector report: HTTP {code}; its own statement: cross-checked {stamp}; criteria {crit}")
    print(f"   {'metric':24} {'recipe':>8} {'inspector':>10}   verdict")
    for mid in [m for ms in METRICS.values() for m in ms]:
        a, b = recipes.get(mid), insp.get(mid)
        v = "not shown by the inspector" if b is None else ("EQUAL" if a == b else "DIFFERENT")
        print(f"   {mid:24} {str(a):>8} {str(b):>10}   {v}")


if __name__ == "__main__":
    main()
