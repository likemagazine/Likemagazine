#!/usr/bin/env python3
"""Rebuild the 9 Luxury Guide section pages as server-rendered list pages
(+ build the new fashion-brands page) in the LIKE DnA / Diplomatic Corps
pattern: entries rendered in HTML, ItemList JSON-LD, source credits.

Preserves each page's existing <head> SEO metadata, masthead, nav, hero,
and footer. Replaces the JS-rendered #lg-app div with a full table.

Usage: python3 build_luxury_pages.py   (run from the repo root)
Idempotent: re-running regenerates the same pages.
"""
import json
import re
import html as htmlmod
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "luxury"
SECTIONS = ROOT / "sections"
SITE = "https://likeleaders.com"

SOURCE_LABELS = {
    "Forbes": "Forbes Five-Star",
    "AAA": "AAA Five Diamond",
    "LHW": "Leading Hotels of the World",
}

# slug -> (json file, section page, item type, name key, columns[(key,label)])
LISTS = {
    "hotels": ("hotels.json", "luxury-hotels.html", "Hotel", "hotel", [
        ("hotel", "Hotel"), ("sources", "Recognized by"), ("continent", "Continent"),
        ("region", "Region"), ("country", "Country"), ("city", "City")]),
    "dining": ("dining.json", "luxury-dining.html", "Restaurant", "restaurant", [
        ("restaurant", "Restaurant"), ("stars", "Stars"), ("city", "City"),
        ("country", "Country"), ("guideRegion", "Guide region")]),
    "airlines": ("airlines.json", "luxury-airlines.html", "Airline", "airline", [
        ("rank", "#"), ("airline", "Airline"), ("hubAirport", "Hub airport"),
        ("hubCity", "Hub city"), ("hubCountry", "Country"), ("region", "Region"),
        ("alliance", "Alliance"), ("iata", "IATA"), ("icao", "ICAO")]),
    "aviation": ("aviation.json", "luxury-aviation.html", "Organization", "name", None),
    "jewelers": ("jewelers.json", "luxury-jewelers.html", "Store", "maison", None),
    "shopping": ("shopping.json", "luxury-shopping.html", "Place", "street", [
        ("street", "Street / District"), ("district", "District"), ("city", "City"),
        ("country", "Country"), ("region", "Region"), ("anchors", "Notable anchors")]),
    "trains": ("trains.json", "luxury-trains.html", "TouristAttraction", "name", None),
    "watchmakers": ("watchmakers.json", "luxury-watchmakers.html", "Organization", "name", None),
    "wineries": ("wineries.json", "luxury-wineries.html", "Winery", "name", None),
    "fashion-brands": ("fashion-brands.json", "luxury-fashion-brands.html", "Organization", "brand", None),
}

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
]

NAME_KEYS = {"name", "airline", "street", "maison", "boutique", "hotel", "restaurant", "brand"}


def esc(v):
    if v is None:
        return ""
    return htmlmod.escape(str(v), quote=True)


def fmt_value(slug, key, item):
    v = item.get(key)
    if v is None:
        return ""
    if isinstance(v, list):
        if key == "sources":
            return ", ".join(SOURCE_LABELS.get(x, x) for x in v)
        if key == "anchors":
            return ", ".join(a.get("name", "") for a in v if a.get("name"))
        return ", ".join(str(x) for x in v)
    if key == "stars" and isinstance(v, int):
        return "\u2605" * v
    if key == "region" and isinstance(v, str) and isinstance(item.get("continent"), str):
        if v.lower() == item["continent"].lower():
            return "\u2014"
        # fall through to normal render
    return str(v)


def cell_html(slug, key, item, label):
    v = item.get(key)
    itemprop = ""
    if key in NAME_KEYS:
        itemprop = ' itemprop="name"'
    elif key == "city":
        itemprop = ' itemprop="addressLocality"'
    elif key == "country":
        itemprop = ' itemprop="addressCountry"'
    cls = ' class="lg-rank"' if key == "rank" else ""
    if key == "website" and v:
        url = str(v)
        if not url.startswith("http"):
            url = "https://" + url
        return f'<td{cls}{itemprop}><a href="{esc(url)}" rel="nofollow">{esc(str(v))}</a></td>'
    return f'<td{cls}{itemprop}>{esc(fmt_value(slug, key, item))}</td>'


def itemlist_jsonld(slug, page_url, list_name, item_type, name_key, items):
    elements = []
    for i, it in enumerate(items, 1):
        name = it.get(name_key) or ""
        entry = {"@type": "ListItem", "position": i,
                 "item": {"@type": item_type, "name": name}}
        # a little geography where available, no invented data
        addr = {}
        if it.get("city"):
            addr["addressLocality"] = it["city"]
        if it.get("country"):
            addr["addressCountry"] = it["country"]
        if addr:
            addr["@type"] = "PostalAddress"
            entry["item"]["address"] = addr
        elements.append(entry)
    doc = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home",
                 "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Luxury Guide",
                 "item": SITE + "/sections/luxury-guide.html"},
                {"@type": "ListItem", "position": 3, "name": list_name,
                 "item": page_url},
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
    """Remove previously injected list-schema blocks (marked or legacy)."""
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


def add_fashion_to_dropdown(nav_html):
    """Insert the Fashion Brands link into the Luxury Guide dropdown (idempotent)."""
    if "luxury-fashion-brands.html" in nav_html:
        return nav_html
    anchor = '<a href="/sections/luxury-jewelers.html">Jewelers</a>'
    addition = anchor + '\n      <a href="/sections/luxury-fashion-brands.html">Fashion Brands</a>'
    if anchor in nav_html:
        return nav_html.replace(anchor, addition)
    return nav_html


def split_page(page_html):
    """Return dict of page parts."""
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
    # drop the JS app bootstrap + scripts (content is now server-rendered)
    tail = re.sub(r'(?s)<script>\s*window\.LIKE_LUXURY_GUIDE.*?</script>', '', tail)
    tail = re.sub(r'<script src="/js/luxury-(seo|guide)\.js" defer></script>', '', tail)
    return {
        "head": head,
        "masthead_nav": body[mast_start:nav_end],
        "hero": body[hero_start:hero_end],
        "footer": body[foot_start:foot_end],
        "tail": tail,
    }


FASHION_HERO = """<article class="lg-hero">
    <img class="lg-hero-media" src="/images/luxury-guide/luxury-guide-hero.jpg" alt="The Peninsula Hotel, Kowloon, Hong Kong" width="1600" height="900" loading="lazy"/>
    <div class="lg-hero-body">
      <p class="lg-eyebrow">LIKE\u00ae Magazine \u00b7 Luxury Guide</p>
      <h1 class="lg-title">Fashion Brands</h1>
      <hr class="lg-gold-rule"/>
      <p class="lg-lede">{lede}</p>
      <p class="lg-credit">Photo: UggBoy\u2665UggGirl / Wikimedia Commons (CC BY 2.0)</p>
      <p class="lg-credit">Curated for LIKE\u00ae Magazine Luxury Guide \u00b7 likeleaders.com</p>
    </div>
  </article>"""


def build_fashion_head(template_head, meta):
    """Derive the fashion page head from the hotels page head via substitution."""
    seo = meta["seo"]
    head = template_head
    # the template may already carry its own ItemList (rebuilt page) — strip
    # any ItemList/BreadcrumbList script blocks; the publisher graph stays
    head = re.sub(r'(?s)<script type="application/ld\+json">(?:(?!</script>).)*?"ItemList".*?</script>',
                  '', head)
    subs = [
        ("Luxury Hotels Worldwide \u00b7 LIKE\u00ae Magazine Luxury Guide", seo["title"]),
        ("Editorial index of luxury hotels worldwide recognized by Forbes Travel Guide Five-Star, AAA Five Diamond, and Leading Hotels of the World \u2014 published as the LIKE\u00ae Magazine Luxury Guide on likeleaders.com.", seo["description"]),
        ("LIKE Magazine, LIKE\u00ae, likeleaders, luxury guide, luxury hotels, Forbes Five-Star, AAA Five Diamond, Leading Hotels of the World, five-star hotels", ", ".join(seo["keywords"])),
        ("Luxury Hotels Worldwide (Forbes Five-Star, AAA Five Diamond, Leading Hotels of the World) \u00b7 LIKE\u00ae Magazine Luxury Guide", seo["title"]),
        ("https://likeleaders.com/sections/luxury-hotels.html", seo["canonical"]),
        ("/images/luxury-guide/hotels-hero.jpg", "/images/luxury-guide/luxury-guide-hero.jpg"),
    ]
    for old, new in subs:
        head = head.replace(old, new)
    return head


def build_page(slug):
    json_file, page_file, item_type, name_key, columns = LISTS[slug]
    doc = json.loads((DATA / json_file).read_text(encoding="utf-8"))
    meta, items = doc["meta"], doc["items"]
    if columns is None:
        columns = [(c["key"], c.get("label") or c["key"]) for c in meta["columns"]]
    count = len(items)
    page_url = f"{SITE}/sections/{page_file}"
    list_name = meta["title"]

    if slug == "fashion-brands":
        template = (SECTIONS / "luxury-hotels.html").read_text(encoding="utf-8")
        parts = split_page(template)
        parts["head"] = build_fashion_head(parts["head"], meta)
        parts["hero"] = FASHION_HERO.format(lede=esc(meta["seo"]["description"]))
    else:
        parts = split_page((SECTIONS / page_file).read_text(encoding="utf-8"))

    # 1. head + ItemList JSON-LD (strip any previously injected list schema first:
    #    the generator must be idempotent across re-runs)
    head = strip_injected_schema(parts["head"])
    schema = itemlist_jsonld(slug, page_url, list_name, item_type, name_key, items)
    head = head.replace("</head>", schema + "\n</head>")

    # 2. nav with fashion link
    nav = add_fashion_to_dropdown(parts["masthead_nav"])

    # 3. content
    thead = "<thead><tr>" + "".join(
        f'<th scope="col">{esc(label)}</th>' for _, label in columns) + "</tr></thead>"
    rows = []
    for it in items:
        tds = "".join(cell_html(slug, key, it, label) for key, label in columns)
        rows.append(
            f'<tr itemscope itemtype="https://schema.org/{esc(item_type)}">{tds}</tr>')
    table = ('<div class="lg-table-wrap"><table class="lg-table">'
             + thead + "<tbody>\n" + "\n".join(rows) + "\n</tbody></table></div>")
    sources = "; ".join(meta.get("sources", []))
    compiled = meta.get("compiled", "")
    meta_bar = (f'<div class="lg-meta-bar"><span><strong>{count:,}</strong> '
                f'listing{"s" if count != 1 else ""}</span>'
                + (f"<span>Compiled {esc(compiled)}</span>" if compiled else "") + "</div>")
    source_note = (f'<p class="lg-credit">Source: {esc(sources)}. '
                   f'{count:,} entries compiled {esc(compiled)}. Verified facts only; '
                   f'a blank field means the detail is not publicly documented.</p>')

    main = ("<main class=\"lg-wrap\">\n" + parts["hero"] + "\n"
            + build_subnav(page_file) + "\n" + meta_bar + "\n"
            + source_note + "\n" + table + "\n</main>")

    page = head + "\n<body>\n" + nav + "\n" + main + "\n" + parts["footer"] + parts["tail"]
    (SECTIONS / page_file).write_text(page, encoding="utf-8")
    return page_file, count


def main():
    results = {}
    for slug in LISTS:
        if not (DATA / LISTS[slug][0]).exists():
            print(f"SKIP {slug}: {(DATA / LISTS[slug][0]).name} not found")
            continue
        page_file, count = build_page(slug)
        results[slug] = (page_file, count)
        print(f"built {page_file}: {count:,} entries")
    print("done:", len(results), "pages")


if __name__ == "__main__":
    main()
