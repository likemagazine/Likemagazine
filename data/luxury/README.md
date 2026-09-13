# Luxury guide data (likeleaders.com)

Parsed from PDF text extracts compiled 2026-09-12. Original PDFs live in `source-pdfs/`.

**hotels.json** — 680 luxury hotels worldwide tagged with Forbes Five-Star, AAA Five Diamond, and/or Leading Hotels of the World (`sources` array). Fields: `hotel`, `sources`, `continent`, `region`, `country`, `city` (nearest city).

**shopping.json** — 179 shopping streets/districts **grouped** from 637 flat anchor rows (by street+city+country). Each item has `anchors: [{name, address}]` plus district, country, region, and a representative top-level `address`.

**dining.json** — 3606 Michelin-starred restaurants (1★=2934, 2★=509, 3★=163). Fields: `restaurant`, `stars` (1|2|3), `city`, `country`, `guideRegion`.

**airlines.json** — 100 Skytrax Top 100 (2025) airlines by primary hub. Fields: `rank`, `airline`, `hubAirport`, `hubCity`, `hubCountry`, `region`, `icao`, `iata`, `otherHubs[]`, `classes[]`, `callsign`, `alliance`.
