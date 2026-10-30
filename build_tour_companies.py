#!/usr/bin/env python3
"""Build the Luxury Guide Top 500 Specialty Tour Companies Worldwide page as a
server-rendered list page in the LIKE DnA / Diplomatic Corps pattern: entries
rendered in HTML, ItemList JSON-LD (TravelAgency), source credits.

Usage: python3 build_tour_companies.py   (run from the repo root)
Idempotent: re-running regenerates the same page.
"""
import json
import re
import html as htmlmod
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "luxury"
SECTIONS = ROOT / "sections"
SITE = "https://likeleaders.com"
PAGE_FILE = "luxury-tour-companies.html"
JSON_FILE = "tour-companies.json"

SUBNAV = [
    ("luxury-guide.html", "Overview"),
    ("luxury-hotels.html", "Hotels"),
    ("luxury-dining.html", "Dining"),
    ("luxury-shopping.html", "Shopping"),
    ("luxury-airlines.html", "Airlines"),
    ("luxury-wineries.html", "Wineries"),
    ("luxury-trains.html", "Trains"),
    ("luxury-aviation.html", "Aviation"),
    ("luxury-watchmakers.html", "Watchmakers"),
    ("luxury-jewelers.html", "Jewelers"),
    ("luxury-fashion-brands.html", "Fashion Brands"),
    ("luxury-casinos.html", "Casinos"),
    ("luxury-ski-resorts.html", "Ski Resorts"),
    ("luxury-beach-clubs.html", "Beach Clubs"),
    ("luxury-apparel-ski.html", "Ski Apparel"),
    ("luxury-apparel-beach.html", "Beach Apparel"),
    ("luxury-apparel-golf.html", "Golf Apparel"),
    ("luxury-apparel-equestrian.html", "Equestrian Apparel"),
    ("luxury-tour-companies.html", "Tour Companies"),
]

TOUR_CSS = """
<style>
.lg-tour-category{margin:2.2rem 0 .8rem;font-size:1.35rem;letter-spacing:.02em}
.lg-tour-category .lg-count{font-size:.85rem;color:#8a7a5c;margin-left:.5rem}
.lg-tour{border:1px solid #e4dccb;border-radius:6px;padding:1rem 1.2rem;margin:0 0 1rem;background:#fffdf8}
.lg-tour h3{margin:0 0 .15rem;font-size:1.12rem}
.lg-tour-loc{margin:0 0 .6rem;color:#6b6252;font-size:.92rem}
.lg-tour dl{margin:0;display:grid;grid-template-columns:11rem 1fr;gap:.3rem .8rem;font-size:.93rem}
.lg-tour dt{font-weight:600;color:#4a4438}
.lg-tour dd{margin:0}
.lg-tour dd ul{margin:.1rem 0 .1rem 1.1rem;padding:0}
@media (max-width:640px){.lg-tour dl{grid-template-columns:1fr}}
</style>
"""

TOUR_HERO = """<article class="lg-hero">
    <img class="lg-hero-media" src="/images/luxury-guide/luxury-guide-hero.jpg" alt="Luxury expedition travel" width="1600" height="900" loading="lazy"/>
    <div class="lg-hero-body">
      <p class="lg-eyebrow">LIKE\u00ae Magazine \u00b7 Luxury Guide</p>
      <h1 class="lg-title">Top 500 Specialty Tour Companies Worldwide</h1>
      <hr class="lg-gold-rule"/>
      <p class="lg-lede">{lede}</p>
      <p class="lg-credit">Curated for LIKE\u00ae Magazine Luxury Guide \u00b7 likeleaders.com</p>
    </div>
  </article>"""


def esc(v):
    if v is None:
        return ""
    return htmlmod.escape(str(v), quote=True)


def person_str(p):
    parts = [p.get("name", "")]
    if p.get("title"):
        parts.append(p["title"])
    bits = []
    if p.get("email"):
        bits.append(p["email"])
    if p.get("phone"):
        bits.append(p["phone"])
    s = ", ".join(x for x in parts if x)
    if bits:
        s += " (" + "; ".join(bits) + ")"
    return s


def contact_html(it):
    bits = []
    if it.get("address"):
        bits.append(f'<span itemprop="address">{esc(it["address"])}</span>')
    phone = it.get("phone", "")
    if phone:
        bits.append(f'<a href="tel:{esc(re.sub(r"[^+\\d]", "", phone))}">{esc(phone)}</a>')
    email = it.get("email", "")
    if email:
        bits.append(f'<a href="mailto:{esc(email)}">{esc(email)}</a>')
    site = it.get("website", "")
    if site:
        url = site if site.startswith("http") else "https://" + site
        bits.append(f'<a href="{esc(url)}" rel="nofollow" itemprop="url">{esc(site)}</a>')
    return "<br>".join(bits)


def entry_html(it):
    name = it.get("name", "")
    city = it.get("city", "")
    country = it.get("country", "")
    rows = []
    if it.get("specialty"):
        rows.append(("Specialty", esc(it["specialty"])))
    if it.get("ownership"):
        rows.append(("Ownership", esc(it["ownership"])))
    ch = contact_html(it)
    if ch:
        rows.append(("Contact", ch))
    if it.get("destinations"):
        rows.append(("Destinations", esc("; ".join(it["destinations"]))))
    if it.get("fleet"):
        rows.append(("Fleet", esc("; ".join(it["fleet"]))))
    if it.get("trip_types"):
        rows.append(("Trip types", esc("; ".join(it["trip_types"]))))
    if it.get("price_positioning"):
        rows.append(("Positioning", esc(it["price_positioning"])))
    loy = it.get("loyalty_programs") or []
    if loy:
        rows.append(("Loyalty programs",
                     esc("; ".join(f'{l.get("name","")}'
                                   + (f' \u2014 {l.get("offers","")}' if l.get("offers") else '')
                                   for l in loy if l.get("name")))))
    for key, label in [("pr_contacts", "Public relations"),
                       ("marketing_contacts", "In-house marketing")]:
        people = [person_str(p) for p in (it.get(key) or []) if p.get("name")]
        if people:
            rows.append((label, esc("; ".join(people))))
    if not rows:
        return ""
    dl = '<dl class="lg-tour-facts">' + "".join(
        f"<div><dt>{esc(label)}</dt><dd>{val}</dd></div>" for label, val in rows) + "</dl>"
    loc = ", ".join(x for x in [city, country] if x)
    loc_html = ""
    if loc:
        loc_html = (f'  <p class="lg-tour-loc"><span itemprop="addressLocality">{esc(city)}</span>, '
                    f'<span itemprop="addressCountry">{esc(country)}</span></p>\n')
    return (f'<article class="lg-tour" itemscope itemtype="https://schema.org/TravelAgency">\n'
            f'  <h3 itemprop="name">{esc(name)}</h3>\n'
            + loc_html
            + f"  {dl}\n</article>")


def itemlist_jsonld(page_url, list_name, items):
    elements = []
    for i, it in enumerate(items, 1):
        entry = {"@type": "ListItem", "position": i,
                 "item": {"@type": "TravelAgency", "name": it.get("name", "")}}
        addr = {}
        if it.get("city"):
            addr["addressLocality"] = it["city"]
        if it.get("country"):
            addr["addressCountry"] = it["country"]
        if addr:
            addr["@type"] = "PostalAddress"
            entry["item"]["address"] = addr
        site = it.get("website", "")
        if site:
            entry["item"]["url"] = site if site.startswith("http") else "https://" + site
        elements.append(entry)
    doc = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Luxury Guide",
                 "item": SITE + "/sections/luxury-guide.html"},
                {"@type": "ListItem", "position": 3, "name": list_name, "item": page_url},
            ]},
            {"@type": "ItemList", "name": list_name + " \u2014 LIKE Magazine",
             "url": page_url, "numberOfItems": len(items),
             "itemListElement": elements},
        ],
    }
    return ('<!-- LUXURY-ITEMLIST-START -->\n<script type="application/ld+json">\n'
            + json.dumps(doc, ensure_ascii=False)
            + '\n</script>\n<!-- LUXURY-ITEMLIST-END -->')


def strip_injected_schema(head):
    head = re.sub(r'<!-- LUXURY-ITEMLIST-START -->.*?<!-- LUXURY-ITEMLIST-END -->\n?',
                  '', head, flags=re.S)
    head = re.sub(r'\n[ \t]*<script type="application/ld\+json">(?:(?!</script>)[\s\S])*?"ItemList"[\s\S]*?</script>[ \t]*\n?',
                  '\n', head)
    head = re.sub(r'\n{3,}', '\n\n', head)
    return head


def build_subnav(active_page):
    links = []
    for page, label in SUBNAV:
        cls = ' class="is-active"' if page == active_page else ""
        links.append(f'  <a href="/sections/{page}"{cls}>{esc(label)}</a>')
    return '<nav class="lg-subnav" aria-label="Luxury Guide">\n' + "\n".join(links) + "\n</nav>"


def split_page(page_html):
    head_m = re.search(r"(?s)^.*?</head>", page_html)
    head = head_m.group(0)
    body = page_html[head_m.end():]
    mast_start = body.find('<header class="mast">')
    nav_start = body.find('<nav class="nav"')
    nav_end = body.find("</nav>", nav_start) + len("</nav>")
    hero_start = body.find('<article class="lg-hero">')
    hero_end = body.find("</article>", hero_start) + len("</article>")
    foot_start = body.find('<footer class="footer">')
    foot_end = body.find("</footer>", foot_start) + len("</footer>")
    tail = body[foot_end:]
    tail = re.sub(r'(?s)<script>\s*window\.LIKE_LUXURY_GUIDE.*?</script>', '', tail)
    tail = re.sub(r'<script src="/js/luxury-(seo|guide)\.js" defer></script>', '', tail)
    return {"head": head, "masthead_nav": body[mast_start:nav_end],
            "hero": body[hero_start:hero_end],
            "footer": body[foot_start:foot_end], "tail": tail}


def build_tour_head(template_head, meta):
    seo = meta["seo"]
    head = template_head
    head = re.sub(r'(?s)<script type="application/ld\+json">(?:(?!</script>).)*?"ItemList".*?</script>', '', head)
    subs = [
        ("Major Fashion Brands Worldwide \u00b7 LIKE\u00ae Magazine Luxury Guide", seo["title"]),
        ("87 major fashion houses and brands organized by group \u2014 curated for LIKE\u00ae Magazine Luxury Guide on likeleaders.com.", seo["description"]),
        ("LIKE Magazine, luxury fashion brands, fashion houses, designer brands, luxury brands, likeleaders", ", ".join(seo["keywords"])),
        ("https://likeleaders.com/sections/luxury-fashion-brands.html", seo["canonical"]),
    ]
    for old, new in subs:
        head = head.replace(old, new)
    head = head.replace("</head>", TOUR_CSS + "\n</head>")
    return head


def build_page():
    doc = json.loads((DATA / JSON_FILE).read_text(encoding="utf-8"))
    meta, items = doc["meta"], doc["items"]
    count = len(items)
    page_url = f"{SITE}/sections/{PAGE_FILE}"
    list_name = meta["title"]

    template = (SECTIONS / "luxury-fashion-brands.html").read_text(encoding="utf-8")
    parts = split_page(template)
    parts["hero"] = TOUR_HERO.format(lede=esc(meta["seo"]["description"]))

    schema = itemlist_jsonld(page_url, list_name, items)
    head = build_tour_head(strip_injected_schema(parts["head"]), meta)
    head = head.replace("</head>", schema + "\n</head>")

    groups = {}
    for it in items:
        cat = it.get("category", "Specialty Tour Companies")
        groups.setdefault(cat, []).append(it)
    order = ["Expedition & Polar Cruises", "Luxury Ocean Cruises", "River Cruises",
             "Luxury Escorted Tours", "Adventure Travel", "Safaris & Private Travel"]
    ordered = sorted(groups.items(),
                     key=lambda kv: (order.index(kv[0]) if kv[0] in order else 99, kv[0]))

    body_parts = []
    for cat, gitems in ordered:
        cards = [entry_html(it) for it in gitems]
        cards = [c for c in cards if c]
        body_parts.append(
            f'<h2 class="lg-tour-category">{esc(cat)}<span class="lg-count">{len(cards)} compan{"y" if len(cards)==1 else "ies"}</span></h2>\n'
            + "\n".join(cards))

    sources = "; ".join(meta.get("sources", [])[:12])
    compiled = meta.get("compiled", "")
    ordering = meta.get("ordering", "")
    meta_bar = (f'<div class="lg-meta-bar"><span><strong>{count:,}</strong> '
                f'compan{"y" if count == 1 else "ies"}</span>'
                + (f"<span>Compiled {esc(compiled)}</span>" if compiled else "") + "</div>")
    source_note = (f'<p class="lg-credit">Sources: {esc(sources)}. '
                   f'{count:,} entries compiled {esc(compiled)}. {esc(ordering)} '
                   f'Verified facts only; a blank field means the detail is not publicly documented.</p>')

    main = ("<main class=\"lg-wrap\">\n" + parts["hero"] + "\n"
            + build_subnav(PAGE_FILE) + "\n" + meta_bar + "\n"
            + source_note + "\n" + "\n".join(body_parts) + "\n</main>")

    page = head + "\n<body>\n" + parts["masthead_nav"] + "\n" + main + "\n" + parts["footer"] + parts["tail"]
    (SECTIONS / PAGE_FILE).write_text(page, encoding="utf-8")
    return count


def patch_hub_card(count):
    p = SECTIONS / "luxury-guide.html"
    html = p.read_text(encoding="utf-8")
    if PAGE_FILE in html:
        return False
    card = (f'    <a class="lg-hub-card" href="/sections/{PAGE_FILE}">\n'
            f'      <p class="label">{count:,} companies</p>\n'
            f'      <strong>Tour Companies</strong>\n'
            f'      <p>Top 500 specialty tour companies worldwide \u2014 expedition cruises, luxury lines, escorted tours, safaris and private journeys.</p>\n'
            f'    </a>\n')
    anchor = '    <a class="lg-hub-card" href="/sections/ai-source.html">'
    if anchor in html:
        html = html.replace(anchor, card + anchor)
        p.write_text(html, encoding="utf-8")
        return True
    return False


def patch_dropdowns():
    anchor = '<a href="/sections/luxury-apparel-equestrian.html">Equestrian Apparel</a>'
    addition = anchor + '\n      <a href="/sections/luxury-tour-companies.html">Tour Companies</a>'
    n = 0
    for f in list(ROOT.rglob("*.html")):
        if ".git" in str(f):
            continue
        html = f.read_text(encoding="utf-8")
        if PAGE_FILE in html or anchor not in html:
            continue
        f.write_text(html.replace(anchor, addition), encoding="utf-8")
        n += 1
    return n


def patch_sitemap():
    p = ROOT / "sitemap.xml"
    xml = p.read_text(encoding="utf-8")
    if PAGE_FILE in xml:
        return False
    entry = (f'  <url>\n    <loc>{SITE}/sections/{PAGE_FILE}</loc>\n'
             f'    <lastmod>2026-10-30</lastmod>\n    <changefreq>weekly</changefreq>\n'
             f'    <priority>0.8</priority>\n  </url>\n')
    xml = xml.replace("</urlset>", entry + "</urlset>")
    p.write_text(xml, encoding="utf-8")
    return True


def patch_search_index(meta, count):
    p = ROOT / "data" / "search-index.json"
    idx = json.loads(p.read_text(encoding="utf-8"))
    url = f"/sections/{PAGE_FILE}"
    if any(e.get("url") == url for e in idx):
        return False
    idx.append({"url": url,
                "title": meta["seo"]["title"].replace(" \u00b7 LIKE\u00ae Magazine Luxury Guide", " \u00b7 LIKE Magazine"),
                "description": meta["seo"]["description"], "kicker": "Luxury Guide"})
    p.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    return True


def patch_ai_index(meta, count):
    p = DATA / "ai-index.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    ds = d.get("dataset", [])
    if any(JSON_FILE in (x.get("distribution", {}) or {}).get("contentUrl", "") for x in ds):
        return False
    ds.append({
        "@type": "Dataset",
        "name": meta["title"],
        "description": meta["seo"]["description"],
        "url": f"{SITE}/sections/{PAGE_FILE}",
        "creator": {"@id": "https://likeleaders.com/#organization"},
        "isPartOf": {"@type": "CreativeWork", "name": "LIKE\u00ae Magazine Luxury Guide",
                     "url": f"{SITE}/sections/luxury-guide.html"},
        "distribution": {"@type": "DataDownload", "encodingFormat": "application/json",
                         "contentUrl": f"{SITE}/data/luxury/{JSON_FILE}"},
        "variableMeasured": "listing",
        "count": count,
    })
    d["dataset"] = ds
    d["dateModified"] = "2026-10-30"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return True


def main():
    count = build_page()
    print(f"built sections/{PAGE_FILE}: {count:,} entries")
    doc = json.loads((DATA / JSON_FILE).read_text(encoding="utf-8"))
    meta = doc["meta"]
    print("hub card:", "added" if patch_hub_card(count) else "already present")
    print("dropdowns patched:", patch_dropdowns())
    print("sitemap:", "added" if patch_sitemap() else "already present")
    print("search index:", "added" if patch_search_index(meta, count) else "already present")
    print("ai-index:", "added" if patch_ai_index(meta, count) else "already present")


if __name__ == "__main__":
    main()
