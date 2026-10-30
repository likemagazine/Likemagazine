#!/usr/bin/env python3
"""Build the 4 Luxury Guide apparel-brand companion pages as server-rendered
list pages in the LIKE DnA / Diplomatic Corps pattern: entries rendered in
HTML, ItemList JSON-LD, source credits.

Each apparel list companions a lifestyle list:
  apparel-ski        -> Top 500 Ski Resorts (live)
  apparel-beach      -> Top 500 Beach Club Resorts (building; hub fallback)
  apparel-golf       -> Top 500 Golf Clubs (upcoming; hub fallback)
  apparel-equestrian -> Horse Shows & Clubs (upcoming; hub fallback)

Brands are listed for reference as future shoppable inventory. NO affiliate
IDs, tags, or tracking parameters anywhere — official brand sites only.

Usage: python3 build_apparel_pages.py   (run from the repo root)
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

# slug -> (json file, page file, short label, hub blurb, companion page or None)
LISTS = {
    "apparel-ski": (
        "apparel-ski.json", "luxury-apparel-ski.html", "Ski Apparel",
        "Ski and apr\u00e8s-ski apparel brands \u2014 technical skiwear to luxury alpine style.",
        "luxury-ski-resorts.html", "Top 500 Ski Resorts",
    ),
    "apparel-beach": (
        "apparel-beach.json", "luxury-apparel-beach.html", "Beach Apparel",
        "Beach and resort swimwear brands \u2014 luxury maisons to cult swim labels.",
        "luxury-beach-clubs.html", "Top 500 Beach Club Resorts",
    ),
    "apparel-golf": (
        "apparel-golf.json", "luxury-apparel-golf.html", "Golf Apparel",
        "Golf apparel brands \u2014 heritage clubhouse labels to modern golf fashion.",
        None, "Top 500 Golf Clubs",
    ),
    "apparel-equestrian": (
        "apparel-equestrian.json", "luxury-apparel-equestrian.html", "Equestrian Apparel",
        "Equestrian apparel brands \u2014 riding houses, boots, helmets, and saddlery.",
        None, "Horse Shows & Clubs",
    ),
}

APPAREL_SUBNAV = [
    ("luxury-guide.html", "Overview"),
    ("luxury-apparel-ski.html", "Ski Apparel"),
    ("luxury-apparel-beach.html", "Beach Apparel"),
    ("luxury-apparel-golf.html", "Golf Apparel"),
    ("luxury-apparel-equestrian.html", "Equestrian Apparel"),
]

NAME_KEYS = {"brand"}


def esc(v):
    if v is None:
        return ""
    return htmlmod.escape(str(v), quote=True)


def cell_html(key, item):
    v = item.get(key)
    itemprop = ' itemprop="name"' if key in NAME_KEYS else ""
    if key == "country":
        itemprop = ' itemprop="addressCountry"'
    if key == "website" and v:
        url = str(v)
        if not url.startswith("http"):
            url = "https://" + url
        return f'<td{itemprop}><a href="{esc(url)}" rel="nofollow">{esc(str(v))}</a></td>'
    return f'<td{itemprop}>{esc("" if v is None else str(v))}</td>'


def itemlist_jsonld(page_url, list_name, items):
    elements = []
    for i, it in enumerate(items, 1):
        entry = {"@type": "ListItem", "position": i,
                 "item": {"@type": "Organization", "name": it.get("brand") or ""}}
        if it.get("country"):
            entry["item"]["address"] = {"@type": "PostalAddress",
                                        "addressCountry": it["country"]}
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
    head = re.sub(r'<!-- LUXURY-ITEMLIST-START -->.*?<!-- LUXURY-ITEMLIST-END -->\n?',
                  '', head, flags=re.S)
    head = re.sub(r'\n[ \t]*<script type="application/ld\+json">(?:(?!</script>)[\s\S])*?"ItemList"[\s\S]*?</script>[ \t]*\n?',
                  '\n', head)
    head = re.sub(r'\n{3,}', '\n\n', head)
    return head


def build_subnav(active_page):
    links = []
    for page, label in APPAREL_SUBNAV:
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
    return {
        "head": head,
        "masthead_nav": body[mast_start:nav_end],
        "hero": body[hero_start:hero_end],
        "footer": body[foot_start:foot_end],
        "tail": tail,
    }


HERO_TMPL = """<article class="lg-hero">
    <img class="lg-hero-media" src="/images/luxury-guide/luxury-guide-hero.jpg" alt="Luxury Guide" width="1600" height="900" loading="lazy"/>
    <div class="lg-hero-body">
      <p class="lg-eyebrow">LIKE\\u00ae Magazine \\u00b7 Luxury Guide</p>
      <h1 class="lg-title">{title}</h1>
      <hr class="lg-gold-rule"/>
      <p class="lg-lede">{lede}</p>
      <p class="lg-credit">{companion}</p>
      <p class="lg-credit">These brands are listed as future shoppable inventory; no affiliate links are live on this page.</p>
      <p class="lg-credit">Photo: UggBoy\\u2665UggGirl / Wikimedia Commons (CC BY 2.0)</p>
      <p class="lg-credit">Curated for LIKE\\u00ae Magazine Luxury Guide \\u00b7 likeleaders.com</p>
    </div>
  </article>"""


def build_head(template_head, meta):
    seo = meta["seo"]
    head = template_head
    head = re.sub(r'(?s)<script type="application/ld\+json">(?:(?!</script>).)*?"ItemList".*?</script>',
                  '', head)
    subs = [
        ("Luxury Hotels Worldwide \\u00b7 LIKE\\u00ae Magazine Luxury Guide", seo["title"]),
        ("Editorial index of luxury hotels worldwide recognized by Forbes Travel Guide Five-Star, AAA Five Diamond, and Leading Hotels of the World \\u2014 published as the LIKE\\u00ae Magazine Luxury Guide on likeleaders.com.", seo["description"]),
        ("LIKE Magazine, LIKE\\u00ae, likeleaders, luxury guide, luxury hotels, Forbes Five-Star, AAA Five Diamond, Leading Hotels of the World, five-star hotels", ", ".join(seo["keywords"])),
        ("Luxury Hotels Worldwide (Forbes Five-Star, AAA Five Diamond, Leading Hotels of the World) \\u00b7 LIKE\\u00ae Magazine Luxury Guide", seo["title"]),
        ("https://likeleaders.com/sections/luxury-hotels.html", seo["canonical"]),
        ("/images/luxury-guide/hotels-hero.jpg", "/images/luxury-guide/luxury-guide-hero.jpg"),
    ]
    for old, new in subs:
        head = head.replace(old, new)
    return head


def companion_note(companion_page, companion_name):
    if companion_page and (SECTIONS / companion_page).exists():
        return (f'Companion to the <a href="/sections/{companion_page}">'
                f'{esc(companion_name)}</a> list.')
    return (f'Companion to the {esc(companion_name)} list, coming to the '
            f'<a href="/sections/luxury-guide.html">Luxury Guide</a>.')


def build_page(slug):
    json_file, page_file, label, blurb, companion_page, companion_name = LISTS[slug]
    doc = json.loads((DATA / json_file).read_text(encoding="utf-8"))
    meta, items = doc["meta"], doc["items"]
    columns = [(c["key"], c.get("label") or c["key"]) for c in meta["columns"]]
    count = len(items)
    page_url = f"{SITE}/sections/{page_file}"
    list_name = meta["title"]

    template = (SECTIONS / "luxury-hotels.html").read_text(encoding="utf-8")
    parts = split_page(template)
    parts["head"] = build_head(parts["head"], meta)
    parts["hero"] = HERO_TMPL.format(
        title=esc(list_name),
        lede=esc(meta["seo"]["description"]),
        companion=companion_note(companion_page, companion_name),
    )

    head = strip_injected_schema(parts["head"])
    head = head.replace("</head>", itemlist_jsonld(page_url, list_name, items) + "\n</head>")

    nav = parts["masthead_nav"]
    nav = add_apparel_to_dropdown(nav)

    thead = "<thead><tr>" + "".join(
        f'<th scope="col">{esc(lbl)}</th>' for _, lbl in columns) + "</tr></thead>"
    rows = []
    for it in items:
        tds = "".join(cell_html(key, it) for key, _ in columns)
        rows.append(
            f'<tr itemscope itemtype="https://schema.org/Organization">{tds}</tr>')
    table = ('<div class="lg-table-wrap"><table class="lg-table">'
             + thead + "\n<tbody>\n" + "\n".join(rows) + "\n</tbody></table></div>")
    sources = "; ".join(meta.get("sources", []))
    compiled = meta.get("compiled", "")
    meta_bar = (f'<div class="lg-meta-bar"><span><strong>{count:,}</strong> '
                f'brand{"s" if count != 1 else ""}</span>'
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


def add_apparel_to_dropdown(nav_html):
    """Insert the 4 apparel links into the Luxury Guide dropdown (idempotent)."""
    if "luxury-apparel-ski.html" in nav_html:
        return nav_html
    anchor = '<a href="/sections/luxury-ski-resorts.html">Ski Resorts</a>'
    addition = (anchor
                + '\n      <a href="/sections/luxury-apparel-ski.html">Ski Apparel</a>'
                + '\n      <a href="/sections/luxury-apparel-beach.html">Beach Apparel</a>'
                + '\n      <a href="/sections/luxury-apparel-golf.html">Golf Apparel</a>'
                + '\n      <a href="/sections/luxury-apparel-equestrian.html">Equestrian Apparel</a>')
    if anchor in nav_html:
        return nav_html.replace(anchor, addition)
    return nav_html


def patch_hub_cards(counts):
    p = SECTIONS / "luxury-guide.html"
    html = p.read_text(encoding="utf-8")
    added = 0
    for slug in LISTS:
        _, page_file, label, blurb, _, _ = LISTS[slug]
        if page_file in html:
            continue
        card = (f'    <a class="lg-hub-card" href="/sections/{page_file}">\n'
                f'      <p class="label">{counts[slug]:,} brands</p>\n'
                f'      <strong>{esc(label)}</strong>\n'
                f'      <p>{esc(blurb)}</p>\n'
                f'    </a>\n')
        anchor = '    <a class="lg-hub-card" href="/sections/ai-source.html">'
        if anchor in html:
            html = html.replace(anchor, card + anchor)
            added += 1
    if added:
        p.write_text(html, encoding="utf-8")
    return added


def patch_dropdowns():
    anchor = '<a href="/sections/luxury-ski-resorts.html">Ski Resorts</a>'
    n = 0
    for f in list(ROOT.rglob("*.html")):
        if ".git" in str(f):
            continue
        html = f.read_text(encoding="utf-8")
        if "luxury-apparel-ski.html" in html or anchor not in html:
            continue
        f.write_text(html.replace(anchor, add_apparel_to_dropdown(anchor)),
                     encoding="utf-8")
        n += 1
    return n


def patch_sitemap():
    p = ROOT / "sitemap.xml"
    xml = p.read_text(encoding="utf-8")
    added = 0
    for slug in LISTS:
        _, page_file, _, _, _, _ = LISTS[slug]
        if page_file in xml:
            continue
        entry = (f'  <url>\n    <loc>{SITE}/sections/{page_file}</loc>\n'
                 f'    <lastmod>2026-10-30</lastmod>\n    <changefreq>weekly</changefreq>\n'
                 f'    <priority>0.8</priority>\n  </url>\n')
        xml = xml.replace("</urlset>", entry + "</urlset>")
        added += 1
    if added:
        p.write_text(xml, encoding="utf-8")
    return added


def patch_search_index():
    p = ROOT / "data" / "search-index.json"
    idx = json.loads(p.read_text(encoding="utf-8"))
    added = 0
    for slug in LISTS:
        json_file, page_file, _, _, _, _ = LISTS[slug]
        url = f"/sections/{page_file}"
        if any(e.get("url") == url for e in idx):
            continue
        meta = json.loads((DATA / json_file).read_text(encoding="utf-8"))["meta"]
        idx.append({"url": url,
                    "title": meta["seo"]["title"].replace(" \u00b7 LIKE\u00ae Magazine Luxury Guide", " \u00b7 LIKE Magazine"),
                    "description": meta["seo"]["description"], "kicker": "Luxury Guide"})
        added += 1
    if added:
        p.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    return added


def patch_ai_index():
    p = DATA / "ai-index.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    ds = d.get("dataset", [])
    added = 0
    for slug in LISTS:
        json_file, page_file, _, _, _, _ = LISTS[slug]
        if any(json_file in (x.get("distribution", {}) or {}).get("contentUrl", "") for x in ds):
            continue
        meta = json.loads((DATA / json_file).read_text(encoding="utf-8"))["meta"]
        ds.append({
            "@type": "Dataset",
            "name": meta["title"],
            "description": meta["seo"]["description"],
            "url": f"{SITE}/sections/{page_file}",
            "creator": {"@id": "https://likeleaders.com/#organization"},
            "isPartOf": {"@type": "CreativeWork", "name": "LIKE\u00ae Magazine Luxury Guide",
                         "url": f"{SITE}/sections/luxury-guide.html"},
            "distribution": {"@type": "DataDownload", "encodingFormat": "application/json",
                             "contentUrl": f"{SITE}/data/luxury/{json_file}"},
            "variableMeasured": "listing",
            "count": len(json.loads((DATA / json_file).read_text(encoding="utf-8"))["items"]),
        })
        added += 1
    if added:
        d["dataset"] = ds
        d["dateModified"] = "2026-10-30"
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return added


def main():
    counts = {}
    for slug in LISTS:
        json_file = LISTS[slug][0]
        if not (DATA / json_file).exists():
            print(f"SKIP {slug}: {json_file} not found")
            continue
        page_file, count = build_page(slug)
        counts[slug] = count
        print(f"built sections/{page_file}: {count:,} brands")
    if counts:
        print("hub cards added:", patch_hub_cards(counts))
        print("dropdowns patched:", patch_dropdowns())
        print("sitemap entries added:", patch_sitemap())
        print("search index entries added:", patch_search_index())
        print("ai-index datasets added:", patch_ai_index())


if __name__ == "__main__":
    main()
