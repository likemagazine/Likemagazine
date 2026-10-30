#!/usr/bin/env python3
"""Assemble data/luxury/tour-companies.json from the six researcher chunk files.

Usage: python3 assemble_tour_companies.py   (run from the repo root)
Idempotent: re-running regenerates the same JSON (researcher chunks are inputs).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHUNKS = ROOT / "data" / "luxury" / "tour_chunks"
OUT = ROOT / "data" / "luxury" / "tour-companies.json"

CATEGORY_ORDER = [
    ("chunk_expedition.json", "Expedition & Polar Cruises"),
    ("chunk_ocean_cruise.json", "Luxury Ocean Cruises"),
    ("chunk_river_cruise.json", "River Cruises"),
    ("chunk_escorted_tours.json", "Luxury Escorted Tours"),
    ("chunk_adventure.json", "Adventure Travel"),
    ("chunk_safari_jet.json", "Safaris & Private Travel"),
]

# Companies researched in multiple chunks get their PRIMARY category here
# (display names; normalized at runtime). Everything else: first chunk wins.
PRIMARY_CATEGORY = {
    # Expedition-first
    "Lindblad Expeditions": "Expedition & Polar Cruises",
    "Quark Expeditions": "Expedition & Polar Cruises",
    "HX (Hurtigruten Expeditions)": "Expedition & Polar Cruises",
    "Oceanwide Expeditions": "Expedition & Polar Cruises",
    "Poseidon Expeditions": "Expedition & Polar Cruises",
    "Adventure Canada": "Expedition & Polar Cruises",
    "Chimu Adventures": "Expedition & Polar Cruises",
    "Churchill Wild": "Expedition & Polar Cruises",
    "Frontiers North Adventures": "Expedition & Polar Cruises",
    "Cheesemans' Ecology Safaris": "Expedition & Polar Cruises",
    "Zegrahm Expeditions": "Expedition & Polar Cruises",
    "Hapag-Lloyd Cruises": "Expedition & Polar Cruises",
    "Coral Expeditions": "Expedition & Polar Cruises",
    "Noble Caledonia": "Expedition & Polar Cruises",
    "Atlas Ocean Voyages": "Expedition & Polar Cruises",
    "Aranui Cruises": "Expedition & Polar Cruises",
    "Aqua Expeditions": "Expedition & Polar Cruises",
    "UnCruise Adventures": "Expedition & Polar Cruises",
    "Ponant": "Expedition & Polar Cruises",
    # Ocean-first
    "American Cruise Lines": "Luxury Ocean Cruises",
    "Emerald Cruises": "Luxury Ocean Cruises",
    "Pearl Seas Cruises": "Luxury Ocean Cruises",
    "Phoenix Reisen": "Luxury Ocean Cruises",
    "Plantours Kreuzfahrten": "Luxury Ocean Cruises",
    "Ritz-Carlton Yacht Collection": "Luxury Ocean Cruises",
    "SeaDream Yacht Club": "Luxury Ocean Cruises",
    "Windstar Cruises": "Luxury Ocean Cruises",
    # River-first
    "nicko cruises": "River Cruises",
    # Escorted-first
    "Abercrombie & Kent": "Luxury Escorted Tours",
    "Tauck": "Luxury Escorted Tours",
    "Kensington Tours": "Luxury Escorted Tours",
    "Cox & Kings": "Luxury Escorted Tours",
    "Ker & Downey": "Luxury Escorted Tours",
    "Smithsonian Journeys": "Luxury Escorted Tours",
    "Riviera Travel": "Luxury Escorted Tours",
    "Titan Travel": "Luxury Escorted Tours",
    "Rocky Mountaineer": "Luxury Escorted Tours",
    "Rovos Rail": "Luxury Escorted Tours",
    "APT": "Luxury Escorted Tours",
    "Extraordinary Journeys": "Luxury Escorted Tours",
    # Adventure-first
    "Backroads": "Adventure Travel",
    "Butterfield & Robinson": "Adventure Travel",
    "Austin Adventures": "Adventure Travel",
    "Classic Journeys": "Adventure Travel",
    "Country Walkers": "Adventure Travel",
    "Trek Travel": "Adventure Travel",
    "DuVine Cycling + Adventure Co.": "Adventure Travel",
    "G Adventures": "Adventure Travel",
    "Intrepid Travel": "Adventure Travel",
    "Explore!": "Adventure Travel",
    "Orbridge": "Adventure Travel",
    "Natural Habitat Adventures": "Adventure Travel",
    "Wilderness Travel": "Adventure Travel",
    "Geographic Expeditions": "Adventure Travel",
    "Geographic Expeditions (GeoEx)": "Adventure Travel",
    "50 Degrees North": "Adventure Travel",
    "Nordic Visitor": "Adventure Travel",
    "InsideJapan Tours": "Adventure Travel",
    "Artisans of Leisure": "Adventure Travel",
    "National Geographic Expeditions": "Adventure Travel",
    "Steppes Travel": "Adventure Travel",
    # Safari & private-first
    "&Beyond": "Safaris & Private Travel",
    "Micato Safaris": "Safaris & Private Travel",
    "Wilderness": "Safaris & Private Travel",
    "Singita": "Safaris & Private Travel",
    "Asilia Africa": "Safaris & Private Travel",
    "Nomad Tanzania": "Safaris & Private Travel",
    "Great Plains Conservation": "Safaris & Private Travel",
    "Aardvark Safaris": "Safaris & Private Travel",
    "Captain's Choice": "Safaris & Private Travel",
    "TCS World Travel": "Safaris & Private Travel",
    "Sanctuary Retreats": "Safaris & Private Travel",
    "Expert Africa": "Safaris & Private Travel",
    "Scott Dunn": "Safaris & Private Travel",
    "Pelorus": "Safaris & Private Travel",
    "Cookson Adventures": "Safaris & Private Travel",
    "Black Tomato": "Safaris & Private Travel",
    "Original Travel": "Safaris & Private Travel",
}
PRIMARY_NORM = None  # computed in main() after norm_name is defined


def norm_name(n):
    n = (n or "").lower()
    n = re.sub(r"[^a-z0-9 ]", "", n)
    n = re.sub(r"\s+", " ", n).strip()
    # drop common legal suffixes for dedupe
    n = re.sub(r"\b(inc|llc|ltd|limited|co|company|corp|corporation|gmbh|sa|pty)\b", "", n)
    return re.sub(r"\s+", " ", n).strip()


def clean_str(v):
    if v is None:
        return ""
    return str(v).strip()


def clean_list(v):
    if not v:
        return []
    if isinstance(v, str):
        return [v] if v.strip() else []
    return [str(x).strip() for x in v if str(x).strip()]


def normalize(item, category):
    it = dict(item)
    it["name"] = clean_str(it.get("name"))
    it["specialty"] = clean_str(it.get("specialty"))
    it["city"] = clean_str(it.get("city"))
    it["country"] = clean_str(it.get("country"))
    it["ownership"] = clean_str(it.get("ownership"))
    it["address"] = clean_str(it.get("address"))
    it["phone"] = clean_str(it.get("phone"))
    it["email"] = clean_str(it.get("email"))
    it["website"] = clean_str(it.get("website"))
    it["destinations"] = clean_list(it.get("destinations"))
    it["fleet"] = clean_list(it.get("fleet"))
    it["trip_types"] = clean_list(it.get("trip_types"))
    it["price_positioning"] = clean_str(it.get("price_positioning"))
    lp = it.get("loyalty_programs") or []
    it["loyalty_programs"] = [
        {"name": clean_str(p.get("name")), "offers": clean_str(p.get("offers"))}
        for p in lp if isinstance(p, dict) and clean_str(p.get("name"))
    ]
    for k in ("pr_contacts", "marketing_contacts"):
        cs = it.get(k) or []
        it[k] = [
            {"name": clean_str(c.get("name")), "title": clean_str(c.get("title")),
             "email": clean_str(c.get("email")), "phone": clean_str(c.get("phone"))}
            for c in cs if isinstance(c, dict) and clean_str(c.get("name"))
        ]
    it["source"] = clean_str(it.get("source"))
    it["category"] = category
    return it


def main():
    global PRIMARY_NORM
    PRIMARY_NORM = {norm_name(k): v for k, v in PRIMARY_CATEGORY.items()}
    items, seen, dupes = [], set(), 0
    sources = []
    for fname, category in CATEGORY_ORDER:
        p = CHUNKS / fname
        if not p.exists():
            print(f"MISSING {fname}")
            continue
        doc = json.loads(p.read_text(encoding="utf-8"))
        chunk_items = doc.get("items", [])
        print(f"{fname}: {len(chunk_items)} raw")
        for raw in chunk_items:
            key = norm_name(raw.get("name", ""))
            if not key:
                continue
            if key in seen:
                dupes += 1
                continue
            seen.add(key)
            # primary-category override beats first-chunk-wins
            cat = PRIMARY_NORM.get(key, category)
            it = normalize(raw, cat)
            if not it["name"]:
                continue
            items.append(it)
        # collect distinct source domains for meta
        for it in chunk_items:
            s = clean_str(it.get("source"))
            if s:
                sources.append(s)

    order = {c: i for i, (_, c) in enumerate(CATEGORY_ORDER)}
    items.sort(key=lambda it: (order.get(it["category"], 99), it["name"].lower()))
    n = len(items)

    meta = {
        "title": "Top 500 Specialty Tour Companies Worldwide",
        "compiled": "2026-10-30",
        "sources": [
            "Company official websites (contact, fleet, loyalty programs)",
            "Parent-company corporate sites and investor disclosures",
            "Official press releases",
        ],
        "count": n,
        "status": "ready",
        "publisher": {
            "@type": "Organization",
            "name": "LIKE® Magazine",
            "alternateName": ["LIKE Magazine", "LIKE®", "likeleaders"],
            "url": "https://likeleaders.com",
        },
        "ordering": ("Grouped by specialty — expedition & polar cruises, luxury ocean cruises, "
                     "river cruises, luxury escorted tours, adventure travel, safaris & private travel — "
                     "alphabetical within each group. Not a strict 1–500 ranking: most companies do not publish revenue."),
        "seo": {
            "title": "Top 500 Specialty Tour Companies Worldwide · LIKE® Magazine Luxury Guide",
            "description": (f"{n} specialty tour companies worldwide — expedition cruises, luxury ocean and river "
                            "lines, escorted tours, adventure travel, safaris and private-jet journeys — ownership, "
                            "fleets, loyalty programs and full contact details — curated for LIKE® Magazine Luxury Guide on likeleaders.com."),
            "keywords": ["LIKE Magazine", "top tour companies worldwide", "luxury tour operators",
                         "expedition cruises", "luxury safaris", "adventure travel companies", "likeleaders"],
            "canonical": "https://likeleaders.com/sections/luxury-tour-companies.html",
            "robots": "index,follow",
        },
    }
    OUT.write_text(json.dumps({"meta": meta, "items": items}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"wrote {OUT}: {n} companies ({dupes} duplicates dropped)")


if __name__ == "__main__":
    main()
