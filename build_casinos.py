#!/usr/bin/env python3
"""Build the Top 500 Casinos Worldwide Luxury Guide list page.

Reads data/luxury/casinos.json (meta + items), renders
sections/luxury-casinos.html as a server-rendered, market-grouped directory
in the LIKE Luxury Guide pattern: entries in HTML, ItemList + BreadcrumbList
JSON-LD, source credits, canonical masthead/nav/hero/footer.

Also wires the page in (idempotently):
  - sections/luxury-guide.html hub (11th card)
  - the Luxury Guide dropdown nav on every site page
  - sitemap.xml, data/search-index.json, data/luxury/ai-index.json

Usage: python3 build_casinos.py   (run from the repo root)
Idempotent: re-running regenerates the same page and wiring.
"""
import json
import re
import html as htmlmod
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "luxury"
SECTIONS = ROOT / "sections"
SITE = "https://likeleaders.com"
PAGE_FILE = "luxury-casinos.html"
JSON_FILE = "casinos.json"

# broad region grouping for the directory (matched case-insensitively against
# each item's "market" value, first match wins; unmatched fall back to country)
REGION_RULES = [
    ("tribal", "Tribal Gaming"),
    ("macau", "Macau"), ("macao", "Macau"),
    ("las vegas", "Las Vegas"), ("henderson", "Las Vegas"),
    ("summerlin", "Las Vegas"), ("north las vegas", "Las Vegas"),
    ("singapore", "Singapore"),
    ("atlantic city", "Atlantic City"),
    ("philippines", "Philippines"), ("manila", "Philippines"),
    ("cebu", "Philippines"), ("clark", "Philippines"),
    ("south korea", "South Korea"), ("korea", "South Korea"),
    ("malaysia", "Rest of Asia"), ("genting", "Rest of Asia"),
    ("cambodia", "Rest of Asia"), ("naga", "Rest of Asia"),
    ("vietnam", "Rest of Asia"), ("phu quoc", "Rest of Asia"),
    ("hoi an", "Rest of Asia"), ("hoiana", "Rest of Asia"),
    ("ho tram", "Rest of Asia"), ("sri lanka", "Rest of Asia"),
    ("india", "Rest of Asia"), ("goa", "Rest of Asia"),
    ("pennsylvania", "Pennsylvania"), ("pittsburgh", "Pennsylvania"),
    ("philadelphia", "Pennsylvania"), ("bethlehem", "Pennsylvania"),
    ("pocono", "Pennsylvania"),
    ("new york", "New York"), ("finger lakes", "New York"),
    ("capital district", "New York"), ("new york city", "New York"),
    ("niagara", "New York"),
    ("massachusetts", "Massachusetts"), ("boston", "Massachusetts"),
    ("springfield", "Massachusetts"),
    ("connecticut", "Connecticut"),
    ("ohio", "Ohio"), ("columbus", "Ohio"), ("cleveland", "Ohio"),
    ("cincinnati", "Ohio"), ("toledo", "Ohio"), ("northfield", "Ohio"),
    ("michigan", "Michigan"), ("detroit", "Michigan"),
    ("illinois", "Illinois"), ("chicago", "Illinois"),
    ("aurora", "Illinois"), ("joliet", "Illinois"), ("elgin", "Illinois"),
    ("indiana", "Indiana"), ("hammond", "Indiana"),
    ("mississippi", "Mississippi"), ("vicksburg", "Mississippi"),
    ("tunica", "Mississippi"), ("gulf coast", "Mississippi"),
    ("biloxi", "Mississippi"),
    ("louisiana", "Louisiana"), ("shreveport", "Louisiana"),
    ("bossier", "Louisiana"), ("new orleans", "Louisiana"),
    ("lake charles", "Louisiana"), ("baton rouge", "Louisiana"),
    ("bayou", "Louisiana"), ("cajun", "Louisiana"),
    ("arkansas", "Arkansas"), ("hot springs", "Arkansas"),
    ("west memphis", "Arkansas"),
    ("reno", "Nevada"), ("laughlin", "Nevada"), ("tahoe", "Nevada"),
    ("sparks", "Nevada"),
    ("black hawk", "Colorado"), ("central city", "Colorado"),
    ("cripple creek", "Colorado"),
    ("council bluffs", "Iowa"), ("dubuque", "Iowa"),
    ("iowa city", "Iowa"), ("northwood", "Iowa"),
    ("waterloo", "Iowa"),
    ("st. louis", "Missouri"), ("st louis", "Missouri"),
    ("kansas city", "Missouri"), ("cape girardeau", "Missouri"),
    ("caruthersville", "Missouri"), ("boonville", "Missouri"),
    ("dodge city", "Kansas"), ("kansas crossing", "Kansas"),
    ("mulvane", "Kansas"),
    ("new mexico", "New Mexico"), ("albuquerque", "New Mexico"),
    ("farmington", "New Mexico"), ("hobbs", "New Mexico"),
    ("ruidoso", "New Mexico"), ("sunland", "New Mexico"),
    ("arizona", "Arizona"),
    ("canada", "Canada"), ("ontario", "Canada"), ("windsor", "Canada"),
    ("québec", "Canada"), ("quebec", "Canada"), ("montréal", "Canada"),
    ("montreal", "Canada"), ("british columbia", "Canada"),
    ("monte carlo", "Monte Carlo"), ("monaco", "Monte Carlo"),
    ("london", "London"), ("mayfair", "London"),
    ("france", "France"), ("cannes", "France"), ("deauville", "France"),
    ("paris", "France"), ("lille", "France"), ("évian", "France"),
    ("evian", "France"), ("enghien", "France"),
    ("germany", "Germany"), ("baden-baden", "Germany"),
    ("dortmund", "Germany"), ("hohensyburg", "Germany"),
    ("wiesbaden", "Germany"), ("stuttgart", "Germany"),
    ("hamburg", "Germany"),
    ("spain", "Spain"), ("madrid", "Spain"), ("barcelona", "Spain"),
    ("marbella", "Spain"), ("costa del sol", "Spain"),
    ("torrelodones", "Spain"),
    ("portugal", "Portugal"), ("póvoa", "Portugal"),
    ("povoa", "Portugal"), ("figueira", "Portugal"),
    ("estoril", "Portugal"), ("cascais", "Portugal"),
    ("lisbon", "Portugal"), ("lisboa", "Portugal"),
    ("italy", "Italy"), ("aosta", "Italy"), ("sanremo", "Italy"),
    ("venice", "Italy"), ("venezia", "Italy"),
    ("campione", "Italy"),
    ("belgium", "Belgium"), ("knokke", "Belgium"),
    ("brussels", "Belgium"),
    ("netherlands", "Netherlands"), ("amsterdam", "Netherlands"),
    ("holland", "Netherlands"), ("scheveningen", "Netherlands"),
    ("austria", "Austria"), ("graz", "Austria"), ("innsbruck", "Austria"),
    ("linz", "Austria"), ("salzburg", "Austria"), ("vienna", "Austria"),
    ("wien", "Austria"), ("bregenz", "Austria"),
    ("switzerland", "Switzerland"), ("baden-baden", "Germany"),
    ("montreux", "Switzerland"), ("geneva", "Switzerland"),
    ("zurich", "Switzerland"), ("zürich", "Switzerland"),
    ("baden", "Switzerland"), ("basel", "Switzerland"),
    ("bern", "Switzerland"), ("lugano", "Switzerland"),
    ("lucerne", "Switzerland"), ("luzern", "Switzerland"),
    ("st. gallen", "Switzerland"), ("st gallen", "Switzerland"),
    ("greece", "Greece"), ("athens", "Greece"),
    ("thessaloniki", "Greece"),
    ("cyprus", "Cyprus"), ("limassol", "Cyprus"),
    ("malta", "Malta"), ("st julian", "Malta"),
    ("czechia", "Czechia"), ("czech", "Czechia"), ("rozvadov", "Czechia"),
    ("slovenia", "Slovenia"),
    ("poland", "Poland"), ("warsaw", "Poland"),
    ("serbia", "Serbia"), ("belgrade", "Serbia"),
    ("australia", "Australia & New Zealand"),
    ("sydney", "Australia & New Zealand"),
    ("melbourne", "Australia & New Zealand"),
    ("perth", "Australia & New Zealand"),
    ("canberra", "Australia & New Zealand"),
    ("launceston", "Australia & New Zealand"),
    ("hobart", "Australia & New Zealand"),
    ("townsville", "Australia & New Zealand"),
    ("cairns", "Australia & New Zealand"),
    ("darwin", "Australia & New Zealand"),
    ("alice springs", "Australia & New Zealand"),
    ("brisbane", "Australia & New Zealand"),
    ("gold coast", "Australia & New Zealand"),
    ("new zealand", "Australia & New Zealand"),
    ("auckland", "Australia & New Zealand"),
    ("queenstown", "Australia & New Zealand"),
    ("christchurch", "Australia & New Zealand"),
    ("dunedin", "Australia & New Zealand"),
    ("hamilton", "Australia & New Zealand"),
    ("south africa", "South Africa"), ("gauteng", "South Africa"),
    ("johannesburg", "South Africa"), ("ormonde", "South Africa"),
    ("gqeberha", "South Africa"), ("menlyn", "South Africa"),
    ("mauritius", "Africa – Other"), ("kenya", "Africa – Other"),
    ("nairobi", "Africa – Other"), ("egypt", "Africa – Other"),
    ("cairo", "Africa – Other"), ("morocco", "Africa – Other"),
    ("marrakech", "Africa – Other"),
    ("argentina", "Argentina"), ("buenos aires", "Argentina"),
    ("rosario", "Argentina"), ("tigre", "Argentina"),
    ("chile", "Chile"), ("santiago", "Chile"), ("viña", "Chile"),
    ("vina", "Chile"), ("pucón", "Chile"), ("pucon", "Chile"),
    ("coquimbo", "Chile"), ("la serena", "Chile"),
    ("monticello", "Chile"),
    ("uruguay", "Uruguay"), ("punta del este", "Uruguay"),
    ("peru", "Peru"), ("lima", "Peru"),
    ("mexico", "Mexico"), ("tijuana", "Mexico"),
    ("costa rica", "Costa Rica"), ("san josé", "Costa Rica"),
    ("san jose", "Costa Rica"),
    ("bahamas", "Bahamas"), ("nassau", "Bahamas"),
    ("paradise island", "Bahamas"), ("cable beach", "Bahamas"),
    ("bimini", "Bahamas"),
    ("puerto rico", "Puerto Rico"), ("san juan", "Puerto Rico"),
    ("condado", "Puerto Rico"),
    ("aruba", "Caribbean – Other"), ("curaçao", "Caribbean – Other"),
    ("curacao", "Caribbean – Other"), ("st. maarten", "Caribbean – Other"),
    ("st maarten", "Caribbean – Other"), ("caribbean", "Caribbean – Other"),
    ("punta cana", "Caribbean – Other"),
    ("dominican", "Caribbean – Other"),
    # city/metro-level fallbacks (checked after the broader rules above)
    ("harrisburg", "Pennsylvania"), ("york", "New York"),
    ("laurel highlands", "Pennsylvania"), ("erie", "Pennsylvania"),
    ("pittsburg", "Kansas"),
    ("dayton", "Ohio"), ("youngstown", "Ohio"),
    ("long island", "New York"), ("southern tier", "New York"),
    ("tioga", "New York"),
    ("wichita", "Kansas"), ("mulvane", "Kansas"),
    ("natchez", "Mississippi"),
    ("la grange", "Missouri"), ("st. joseph", "Missouri"),
    ("st joseph", "Missouri"),
    ("peoria", "Illinois"),
    ("des moines", "Iowa"), ("altoona", "Iowa"), ("davenport", "Iowa"),
    ("sioux falls", "Iowa"), ("larchwood", "Iowa"),
    ("el paso", "New Mexico"),
    ("adelaide", "Australia & New Zealand"),
    ("panama", "Panama"),
]

REGION_ORDER = [
    "Macau", "Las Vegas", "Singapore", "Tribal Gaming", "Atlantic City",
    "Philippines", "South Korea", "Rest of Asia",
    "Pennsylvania", "New York", "Massachusetts", "Connecticut",
    "Ohio", "Michigan", "Illinois", "Indiana",
    "Mississippi", "Louisiana", "Arkansas",
    "Nevada", "Colorado", "Iowa", "Missouri", "Kansas", "New Mexico", "Arizona",
    "Canada",
    "Monte Carlo", "London", "France", "Germany", "Spain", "Portugal",
    "Italy", "Belgium", "Netherlands", "Austria", "Switzerland",
    "Greece", "Cyprus", "Malta", "Czechia", "Slovenia", "Serbia", "Poland",
    "Australia & New Zealand", "South Africa", "Africa – Other",
    "Argentina", "Chile", "Uruguay", "Peru", "Mexico", "Costa Rica",
    "Bahamas", "Puerto Rico", "Caribbean – Other", "Panama",
]


def region_for(it):
    m = (it.get("market") or "").lower()
    for sub, display in REGION_RULES:
        if sub in m:
            return display
    c = (it.get("country") or "").strip()
    return c if c else "Other destinations"


def region_rank(region):
    try:
        return REGION_ORDER.index(region)
    except ValueError:
        return len(REGION_ORDER)

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
]

CASINO_CSS = """
<style>
.lg-casino-market{margin:2.2rem 0 .8rem;font-size:1.35rem;letter-spacing:.02em}
.lg-casino-market .lg-count{font-size:.85rem;color:#8a7a5c;margin-left:.5rem}
.lg-casino{border:1px solid #e4dccb;border-radius:6px;padding:1rem 1.2rem;margin:0 0 1rem;background:#fffdf8}
.lg-casino h3{margin:0 0 .15rem;font-size:1.12rem}
.lg-casino-loc{margin:0 0 .6rem;color:#6b6252;font-size:.92rem}
.lg-casino dl{margin:0;display:grid;grid-template-columns:11rem 1fr;gap:.3rem .8rem;font-size:.93rem}
.lg-casino dt{font-weight:600;color:#4a4438}
.lg-casino dd{margin:0}
.lg-casino dd ul{margin:.1rem 0 .1rem 1.1rem;padding:0}
@media (max-width:640px){.lg-casino dl{grid-template-columns:1fr}}
</style>
"""

CASINO_HERO = """<article class="lg-hero">
    <img class="lg-hero-media" src="/images/luxury-guide/luxury-guide-hero.jpg" alt="Luxury resort at night" width="1600" height="900" loading="lazy"/>
    <div class="lg-hero-body">
      <p class="lg-eyebrow">LIKE\u00ae Magazine \u00b7 Luxury Guide</p>
      <h1 class="lg-title">Top 500 Casinos Worldwide</h1>
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


def contact_html(contact):
    bits = []
    addr = contact.get("address", "")
    if addr:
        bits.append(f'<span itemprop="address">{esc(addr)}</span>')
    phone = contact.get("phone", "")
    if phone:
        bits.append(f'<a href="tel:{esc(re.sub(r"[^+\d]", "", phone))}">{esc(phone)}</a>')
    email = contact.get("email", "")
    if email:
        bits.append(f'<a href="mailto:{esc(email)}">{esc(email)}</a>')
    site = contact.get("website", "")
    if site:
        url = site if site.startswith("http") else "https://" + site
        bits.append(f'<a href="{esc(url)}" rel="nofollow" itemprop="url">{esc(site)}</a>')
    return "<br>".join(bits)


def entry_html(it):
    name = it.get("name", "")
    city = it.get("city", "")
    country = it.get("country", "")
    rows = []
    own = it.get("ownership", {}) or {}
    owner, operator = own.get("ultimate_owner", ""), own.get("operator", "")
    if owner or operator:
        v = esc(owner)
        if operator and operator != owner:
            v += f' \u00b7 Operator: {esc(operator)}'
        rows.append(("Ownership", v))
    mgmt = it.get("management", "")
    if mgmt and mgmt != operator:
        rows.append(("Management", esc(mgmt)))
    contact = it.get("contact", {}) or {}
    ch = contact_html(contact)
    if ch:
        rows.append(("Contact", ch))
    for key, label in [("amenities", "Amenities"), ("vip_clubs", "High-roller / VIP clubs"),
                       ("perks", "Perks"), ("activities", "Activities"),
                       ("nightclubs", "Nightclubs"), ("venues", "Venues"),
                       ("banquet_spaces", "Banquet & meeting spaces")]:
        vals = [x for x in (it.get(key) or []) if x]
        if vals:
            rows.append((label, esc(", ".join(vals))))
    loy = it.get("loyalty_programs") or []
    if loy:
        rows.append(("Loyalty programs",
                     esc("; ".join(f'{l.get("name","")}'
                                   + (f' \u2014 {l.get("offers","")}' if l.get("offers") else '')
                                   for l in loy if l.get("name")))))
    for key, label in [("pr_contacts", "Public relations"),
                       ("marketing_contacts", "In-house marketing"),
                       ("fb_managers", "Food & beverage")]:
        people = [person_str(p) for p in (it.get(key) or []) if p.get("name")]
        if people:
            rows.append((label, esc("; ".join(people))))
    conc = it.get("concierge", "")
    if conc:
        rows.append(("Concierge", esc(conc)))
    if not rows:
        return ""
    dl = '<dl class="lg-casino-facts">' + "".join(
        f"<div><dt>{esc(label)}</dt><dd>{val}</dd></div>" for label, val in rows) + "</dl>"
    loc = ", ".join(x for x in [city, country] if x)
    market = it.get("market", "")
    loc_html = ""
    if loc:
        loc_html = (f'  <p class="lg-casino-loc"><span itemprop="addressLocality">{esc(city)}</span>, '
                    f'<span itemprop="addressCountry">{esc(country)}</span>'
                    + (f' · {esc(market)}' if market else "") + '</p>\n')
    return (f'<article class="lg-casino" itemscope itemtype="https://schema.org/Casino">\n'
            f'  <h3 itemprop="name">{esc(name)}</h3>\n'
            + loc_html
            + f"  {dl}\n</article>")


def itemlist_jsonld(page_url, list_name, items):
    elements = []
    for i, it in enumerate(items, 1):
        entry = {"@type": "ListItem", "position": i,
                 "item": {"@type": "Casino", "name": it.get("name", "")}}
        addr = {}
        if it.get("city"):
            addr["addressLocality"] = it["city"]
        if it.get("country"):
            addr["addressCountry"] = it["country"]
        if addr:
            addr["@type"] = "PostalAddress"
            entry["item"]["address"] = addr
        site = (it.get("contact") or {}).get("website", "")
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


def build_casino_head(template_head, meta):
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
    # page-specific directory styles
    head = head.replace("</head>", CASINO_CSS + "\n</head>")
    return head


def build_page():
    doc = json.loads((DATA / JSON_FILE).read_text(encoding="utf-8"))
    meta, items = doc["meta"], doc["items"]
    count = len(items)
    page_url = f"{SITE}/sections/{PAGE_FILE}"
    list_name = meta["title"]

    template = (SECTIONS / "luxury-fashion-brands.html").read_text(encoding="utf-8")
    parts = split_page(template)
    parts["hero"] = CASINO_HERO.format(lede=esc(meta["seo"]["description"]))

    schema = itemlist_jsonld(page_url, list_name, items)
    head = build_casino_head(strip_injected_schema(parts["head"]), meta)
    head = head.replace("</head>", schema + "\n</head>")

    # group items by broad region
    groups = {}
    for it in items:
        region = region_for(it)
        groups.setdefault(region, []).append(it)
    ordered = sorted(groups.items(), key=lambda kv: (region_rank(kv[0]), kv[0]))

    body_parts = []
    for region, gitems in ordered:
        cards = [entry_html(it) for it in gitems]
        cards = [c for c in cards if c]
        body_parts.append(
            f'<h2 class="lg-casino-market">{esc(region)}<span class="lg-count">{len(cards)} propert{"y" if len(cards)==1 else "ies"}</span></h2>\n'
            + "\n".join(cards))

    sources = "; ".join(meta.get("sources", [])[:12])
    compiled = meta.get("compiled", "")
    basis = meta.get("ranking_basis", "")
    meta_bar = (f'<div class="lg-meta-bar"><span><strong>{count:,}</strong> '
                f'propert{"y" if count == 1 else "ies"}</span>'
                + (f"<span>Compiled {esc(compiled)}</span>" if compiled else "") + "</div>")
    source_note = (f'<p class="lg-credit">Sources: {esc(sources)}. '
                   f'{count:,} entries compiled {esc(compiled)}. {esc(basis)} '
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
            f'      <p class="label">{count:,} listings</p>\n'
            f'      <strong>Casinos</strong>\n'
            f'      <p>Top 500 casinos worldwide \u2014 ownership, VIP clubs, loyalty programs, and full contact details.</p>\n'
            f'    </a>\n')
    anchor = '    <a class="lg-hub-card" href="/sections/ai-source.html">'
    if anchor in html:
        html = html.replace(anchor, card + anchor)
        p.write_text(html, encoding="utf-8")
        return True
    return False


def patch_dropdowns():
    anchor = '<a href="/sections/luxury-fashion-brands.html">Fashion Brands</a>'
    addition = anchor + '\n      <a href="/sections/luxury-casinos.html">Casinos</a>'
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
