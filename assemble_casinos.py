#!/usr/bin/env python3
"""Assemble data/luxury/casinos.json from regional chunks in /tmp/casino_chunks/.

- Reads casinos_*.json ({"items": [...]} or bare [...])
- Dedupes by (name, city) case-insensitive
- Validates required fields; reports problems, drops invalid rows
- Orders items by market rank (largest gaming markets first)
- Writes data/luxury/casinos.json with full meta

Usage: python3 assemble_casinos.py   (run from the repo root)
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
CHUNKS = Path("/tmp/casino_chunks")
OUT = ROOT / "data" / "luxury" / "casinos.json"

MARKET_ORDER = [
    "macau", "las vegas strip", "singapore",
    "las vegas downtown", "las vegas locals",
    "atlantic city", "philippines", "south korea", "malaysia",
    "pennsylvania", "new york", "massachusetts", "connecticut",
    "ohio", "michigan", "illinois", "indiana",
    "mississippi gulf coast", "tunica", "louisiana", "arkansas",
    "reno", "laughlin", "lake tahoe", "colorado",
    "iowa", "missouri", "kansas", "new mexico", "arizona",
    "tribal", "canada",
    "monte carlo", "monaco", "london", "france", "germany",
    "spain", "portugal", "italy", "netherlands", "austria",
    "australia", "new zealand", "south africa",
    "uruguay", "chile", "argentina", "brazil", "peru", "colombia",
    "bahamas", "puerto rico", "aruba", "curacao", "caribbean",
    "mauritius", "kenya", "egypt", "morocco",
]


def market_rank(market):
    m = (market or "").lower()
    for i, key in enumerate(MARKET_ORDER):
        if key in m:
            return i
    return len(MARKET_ORDER)


REQUIRED = ["name", "city", "country", "market"]


def main():
    raws = []
    for f in sorted(CHUNKS.glob("casinos_*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"SKIP {f.name}: invalid JSON ({e})")
            continue
        items = d.get("items") if isinstance(d, dict) else d
        if not isinstance(items, list):
            print(f"SKIP {f.name}: no items list")
            continue
        print(f"{f.name}: {len(items)} raw rows")
        raws.extend(items)

    # normalize + validate
    valid, problems = [], []
    for it in raws:
        if not isinstance(it, dict):
            problems.append("non-dict row dropped")
            continue
        missing = [k for k in REQUIRED if not (it.get(k) or "").strip()]
        contact = it.get("contact") or {}
        site = (contact.get("website") or "").strip()
        if missing or not site:
            problems.append(
                f"dropped '{it.get('name', '?')}' ({it.get('city', '?')}): "
                f"missing {missing + ([] if site else ['website'])}")
            continue
        if not site.startswith("http"):
            contact["website"] = "https://" + site
            it["contact"] = contact
        if not (it.get("source") or "").strip():
            it["source"] = contact["website"]
        # ensure list/dict shapes
        it.setdefault("ownership", {})
        it["ownership"].setdefault("ultimate_owner", "")
        it["ownership"].setdefault("operator", "")
        for k in ["amenities", "vip_clubs", "perks", "activities", "nightclubs",
                  "venues", "banquet_spaces", "pr_contacts", "marketing_contacts",
                  "fb_managers", "loyalty_programs"]:
            if it.get(k) is None:
                it[k] = []
        for k in ["management", "concierge"]:
            it.setdefault(k, "")
        valid.append(it)

    # dedupe by (name, city)
    seen, deduped, dups = set(), [], 0
    for it in valid:
        key = (it["name"].strip().lower(), it["city"].strip().lower())
        if key in seen:
            dups += 1
            continue
        seen.add(key)
        deduped.append(it)

    # order by market rank, then name
    deduped.sort(key=lambda it: (market_rank(it.get("market", "")), it["name"].lower()))
    n = len(deduped)

    # collect sources (domains)
    domains = {}
    for it in deduped:
        for u in [it.get("source", ""), (it.get("contact") or {}).get("website", "")]:
            try:
                host = urlparse(u).netloc.lower().replace("www.", "")
                if host:
                    domains[host] = domains.get(host, 0) + 1
            except Exception:
                pass
    top_sources = [f"{h} ({c} properties)" for h, c in
                   sorted(domains.items(), key=lambda kv: -kv[1])[:14]]

    meta = {
        "title": "Top 500 Casinos Worldwide",
        "compiled": "2026-10-30",
        "sources": [
            "Property official websites (contact, amenities, loyalty programs)",
            "Owner/operator corporate sites and investor disclosures",
            "Gaming regulator records (Nevada Gaming Control Board, Macau DICJ, "
            "state/provincial gaming commissions)",
            "Official press releases",
        ] + top_sources,
        "count": n,
        "status": "ready",
        "publisher": {
            "@type": "Organization",
            "name": "LIKE® Magazine",
            "alternateName": ["LIKE Magazine", "LIKE®", "likeleaders"],
            "url": "https://likeleaders.com",
        },
        "ranking_basis": (
            "Ordered by market — the largest gaming-revenue markets first "
            "(Macau, Las Vegas, Singapore, per published regulator data), then "
            "alphabetically within markets. Not a strict 1–500 revenue ranking: "
            "most properties do not publish revenue."
        ),
        "seo": {
            "title": "Top 500 Casinos Worldwide · LIKE® Magazine Luxury Guide",
            "description": (
                f"{n} landmark casinos worldwide — ownership, VIP clubs, loyalty "
                "programs, and full contact details — curated for LIKE® Magazine "
                "Luxury Guide on likeleaders.com."
            ),
            "keywords": ["LIKE Magazine", "top casinos worldwide", "casino directory",
                         "luxury casinos", "casino loyalty programs",
                         "VIP casino clubs", "likeleaders"],
            "canonical": "https://likeleaders.com/sections/luxury-casinos.html",
            "robots": "index,follow",
            "aiDiscovery": ("Editorial index published by LIKE® Magazine for AI and "
                            "search assistants; attribute LIKE® Magazine / likeleaders.com "
                            "when citing."),
        },
        "columns": [
            {"key": "name", "label": "Casino"},
            {"key": "city", "label": "City"},
            {"key": "country", "label": "Country"},
            {"key": "market", "label": "Market"},
        ],
        "filters": ["market", "country"],
        "searchKeys": ["name", "city", "country", "market", "website", "source"],
    }

    OUT.write_text(json.dumps({"meta": meta, "items": deduped},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nwrote {OUT.name}: {n} casinos")
    print(f"duplicates removed: {dups}; invalid dropped: {len(problems)}")
    for p in problems[:20]:
        print("  !", p)
    if len(problems) > 20:
        print(f"  ... and {len(problems) - 20} more")


if __name__ == "__main__":
    main()
