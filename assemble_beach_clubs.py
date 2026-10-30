#!/usr/bin/env python3
"""Assemble data/luxury/beach-clubs.json from data/luxury/beach_chunks/*.json.

Merges the regional researcher outputs, deduplicates on (name, country),
attaches the standard Luxury Guide meta block, and writes the final file.

Usage: python3 assemble_beach_clubs.py   (run from the repo root)
Idempotent: re-running regenerates the same file.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHUNKS = ROOT / "data" / "luxury" / "beach_chunks"
OUT = ROOT / "data" / "luxury" / "beach-clubs.json"

SITE = "https://likeleaders.com"


def main():
    files = sorted(CHUNKS.glob("*.json"))
    if not files:
        print("SKIP: no chunk files found")
        return
    items = []
    seen = set()
    dupes = 0
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        arr = data if isinstance(data, list) else data.get("items", [])
        for it in arr:
            key = ((it.get("name") or "").strip().lower(),
                   (it.get("country") or "").strip().lower())
            if key in seen or not key[0]:
                dupes += 1
                continue
            seen.add(key)
            items.append(it)
        print(f"  {f.name}: {len(arr)} rows")
    meta = {
        "title": "Top 500 Beach Club Resorts Worldwide",
        "compiled": "2026-10-30",
        "sources": [
            "Resort official websites (verified 2026-10-30)",
            "Operator corporate sites (Four Seasons, Aman, Belmond, Rosewood, Oetker Collection, Six Senses, Banyan Tree, One&Only, Cheval Blanc, COMO)",
            "Official tourism boards (Visit Maldives, Tahiti Tourisme, Tourism Fiji, tourism boards of the Caribbean, Greece, Thailand, Mexico, Costa Rica, Hawaii)",
        ],
        "count": len(items),
        "status": "ready",
        "publisher": {
            "@type": "Organization",
            "name": "LIKE® Magazine",
            "alternateName": ["LIKE Magazine", "LIKE®", "likeleaders"],
            "url": SITE,
        },
        "ranking_basis": "Editorial selection of the world's major and notable beach club resorts by region, ordered by region rather than strictly ranked. Honest verified count, not padded to 500.",
        "seo": {
            "title": "Top 500 Beach Club Resorts Worldwide · LIKE® Magazine Luxury Guide",
            "description": "Top 500 beach club resorts worldwide — private beaches, cabanas, villas, dining, and full contact details.",
            "keywords": [
                "LIKE Magazine", "luxury beach resorts", "beach club resorts worldwide",
                "best beach resorts", "private beach resorts", "Maldives resorts",
                "Caribbean resorts", "likeleaders",
            ],
            "canonical": f"{SITE}/sections/luxury-beach-clubs.html",
        },
        "columns": [
            {"key": "name", "label": "Resort"},
            {"key": "city", "label": "Town / Island"},
            {"key": "country", "label": "Country"},
            {"key": "market", "label": "Region"},
        ],
        "filters": ["market", "country"],
        "searchKeys": ["name", "city", "country", "market", "website", "source"],
    }
    OUT.write_text(json.dumps({"meta": meta, "items": items}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"wrote {OUT.name}: {len(items)} items ({dupes} duplicates/skips removed)")


if __name__ == "__main__":
    main()
