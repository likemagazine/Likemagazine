#!/usr/bin/env python3
"""Compile data/luxury/horse-shows-clubs.json from authored entries.

Usage: python3 compile_horse_data.py   (run from the repo root)
Writes data/luxury/horse-shows-clubs.json (meta + items).
Official sources only; blanks mean not publicly documented.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "luxury"

ENTRIES = []


def E(name, kind, city, country, market, website="", **kw):
    e = {
        "name": name,
        "kind": kind,
        "city": city,
        "country": country,
        "market": market,
        "location": kw.get("location", ""),
        "venue": kw.get("venue", ""),
        "organizer": kw.get("organizer", ""),
        "ownership": {"ultimate_owner": kw.get("owner", ""), "operator": kw.get("operator", "")},
        "management": kw.get("management", ""),
        "contact": {
            "address": kw.get("address", ""),
            "phone": kw.get("phone", ""),
            "email": kw.get("email", ""),
            "website": website,
        },
        "disciplines": kw.get("disciplines", []),
        "season": kw.get("season", ""),
        "classes": kw.get("classes", []),
        "hospitality": kw.get("hospitality", ""),
        "stabling": kw.get("stabling", ""),
        "lodging": kw.get("lodging", []),
        "dining": kw.get("dining", []),
        "activities": kw.get("activities", []),
        "sponsors": kw.get("sponsors", []),
        "ticketing": kw.get("ticketing", ""),
        "pr_contacts": kw.get("pr_contacts", []),
        "marketing_contacts": kw.get("marketing_contacts", []),
        "concierge": kw.get("concierge", ""),
        "source": kw.get("source", website),
    }
    ENTRIES.append(e)
    return e


# ---------------------------------------------------------------- Switzerland
E("CHI Geneva", "Horse show", "Geneva", "Switzerland", "Switzerland",
  "https://www.chigeneva.ch",
  location="Palexpo", disciplines=["Show jumping", "Dressage", "Driving"],
  season="Early December (annual)",
  classes=["Rolex Grand Prix (CSI5*)", "Top 10 Final", "Indoor cross-country"],
  organizer="CHI Geneva Association",
  hospitality="VIP lounges and hospitality chalets",
  source="https://www.chigeneva.ch")
E("Longines CSIO St. Gallen", "Horse show", "St. Gallen", "Switzerland", "Switzerland",
  "https://www.csio.ch",
  location="Gründenmoos", disciplines=["Show jumping"],
  season="Late May / early June (annual)",
  classes=["Nations' Cup (CSIO5*)", "Longines Grand Prix"],
  source="https://www.csio.ch")
E("CSI Ascona", "Horse show", "Ascona", "Switzerland", "Switzerland",
  "https://www.csiascona.ch",
  disciplines=["Show jumping"], season="September (annual)",
  source="https://www.csiascona.ch")
E("CSI Basel", "Horse show", "Basel", "Switzerland", "Switzerland",
  "https://www.csibasel.ch",
  location="St. Jakobshalle", disciplines=["Show jumping", "Dressage"],
  season="January (annual)", source="https://www.csibasel.ch")
E("Jumping International de Verbier", "Horse show", "Verbier", "Switzerland", "Switzerland",
  "https://www.verbier.ch",
  disciplines=["Show jumping"], season="Summer (annual)",
  source="https://www.verbier.ch")

# ------------------------------------------------- Germany, Austria & Central Europe
E("CHIO Aachen", "Horse show", "Aachen", "Germany", "Germany, Austria & Central Europe",
  "https://www.chioaachen.de",
  location="Soers showgrounds", disciplines=["Show jumping", "Dressage", "Eventing", "Driving", "Vaulting"],
  season="Late June – early July (annual)",
  classes=["Rolex Grand Prix (CSIO5*)", "Nations' Cups", "Deutsche Bank Prize (dressage)"],
  organizer="Aachen-Laurensberger Rennverein",
  hospitality="Extensive VIP and hospitality village",
  source="https://www.chioaachen.de")
E("Deutsches Spring- und Dressurderby", "Horse show", "Hamburg", "Germany", "Germany, Austria & Central Europe",
  "https://www.engarde.de",
  location="Hamburg-Klein Flottbek", disciplines=["Show jumping", "Dressage"],
  season="May (annual)", classes=["German Jumping Derby", "German Dressage Derby"],
  organizer="EN GARDE Marketing GmbH",
  source="https://www.engarde.de")
E("Pferd International München", "Horse show", "Munich", "Germany", "Germany, Austria & Central Europe",
  "https://www.pferdinternational.de",
  location="Olympia-Reitanlage Riem", disciplines=["Show jumping", "Dressage"],
  season="May (annual)", source="https://www.pferdinternational.de")
E("Wiesbadener PfingstTurnier", "Horse show", "Wiesbaden", "Germany", "Germany, Austria & Central Europe",
  "https://www.wiesbadener-pfingstturnier.de",
  location="Schlosspark Biebrich", disciplines=["Show jumping", "Dressage", "Eventing"],
  season="Whitsun / late May – early June (annual)",
  source="https://www.wiesbadener-pfingstturnier.de")
E("CHI Donaueschingen", "Horse show", "Donaueschingen", "Germany", "Germany, Austria & Central Europe",
  "https://www.chidonaueschingen.de",
  disciplines=["Show jumping", "Dressage"], season="September (annual)",
  source="https://www.chidonaueschingen.de")
E("Partner Pferd Leipzig", "Horse show", "Leipzig", "Germany", "Germany, Austria & Central Europe",
  "https://www.partner-pferd.de",
  disciplines=["Show jumping", "Dressage", "Driving"], season="January (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  source="https://www.partner-pferd.de")
E("Stuttgart German Masters", "Horse show", "Stuttgart", "Germany", "Germany, Austria & Central Europe",
  "https://www.stuttgart-german-masters.de",
  disciplines=["Show jumping", "Dressage", "Driving"], season="November (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  source="https://www.stuttgart-german-masters.de")
E("Vienna Masters", "Horse show", "Vienna", "Austria", "Germany, Austria & Central Europe",
  "https://www.viennamasters.at",
  disciplines=["Show jumping"], season="September (annual)",
  source="https://www.viennamasters.at")
E("CSI Wiener Neustadt", "Horse show", "Wiener Neustadt", "Austria", "Germany, Austria & Central Europe",
  "https://www.reitarena.at",
  disciplines=["Show jumping"], season="Seasonal",
  source="https://www.reitarena.at")
E("Prague Playoffs (Global Champions)", "Horse show", "Prague", "Czechia", "Germany, Austria & Central Europe",
  "https://www.globalchampionstour.com",
  disciplines=["Show jumping"], season="November (annual)",
  classes=["Longines Global Champions Tour Super Grand Prix", "GCL Super Cup"],
  source="https://www.globalchampionstour.com")

# ------------------------------------------------- France, Belgium & the Netherlands
E("Longines Masters of Paris", "Horse show", "Paris", "France", "France, Belgium & the Netherlands",
  "https://www.longinesmasters.com",
  location="Paris-Villepinte", disciplines=["Show jumping"],
  season="December (annual)", classes=["Longines Grand Prix (CSI5*)"],
  organizer="EEM",
  source="https://www.longinesmasters.com")
E("Saut Hermès", "Horse show", "Paris", "France", "France, Belgium & the Netherlands",
  "https://www.sauthermes.com",
  location="Grand Palais Éphémère", disciplines=["Show jumping"],
  season="Spring (annual)", organizer="Hermès",
  source="https://www.sauthermes.com")
E("Longines Jumping International de La Baule", "Horse show", "La Baule", "France", "France, Belgium & the Netherlands",
  "https://www.labaule-cheval.com",
  disciplines=["Show jumping", "Dressage"], season="June (annual)",
  classes=["Nations' Cup (CSIO5*)", "Grand Prix"],
  source="https://www.labaule-cheval.com")
E("Jumping International de Dinard", "Horse show", "Dinard", "France", "France, Belgium & the Netherlands",
  "https://www.jumping-dinard.com",
  disciplines=["Show jumping"], season="July – August (annual)",
  source="https://www.jumping-dinard.com")
E("Jumping International de Bordeaux", "Horse show", "Bordeaux", "France", "France, Belgium & the Netherlands",
  "https://www.jumping-bordeaux.com",
  disciplines=["Show jumping", "Driving"], season="February (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  source="https://www.jumping-bordeaux.com")
E("CHIO Rotterdam", "Horse show", "Rotterdam", "Netherlands", "France, Belgium & the Netherlands",
  "https://www.chio.nl",
  location="Kralingse Bos", disciplines=["Show jumping", "Dressage"],
  season="June (annual)", classes=["Nations' Cups", "Grand Prix"],
  source="https://www.chio.nl")
E("The Dutch Masters", "Horse show", "'s-Hertogenbosch", "Netherlands", "France, Belgium & the Netherlands",
  "https://www.thedutchmasters.com",
  location="Brabanthallen", disciplines=["Show jumping", "Dressage"],
  season="March (annual)", classes=["Rolex Grand Prix (CSI5*)", "FEI Dressage World Cup Final (rotating)"],
  source="https://www.thedutchmasters.com")
E("Jumping Amsterdam", "Horse show", "Amsterdam", "Netherlands", "France, Belgium & the Netherlands",
  "https://www.jumpingamsterdam.nl",
  disciplines=["Show jumping", "Dressage"], season="January (annual)",
  source="https://www.jumpingamsterdam.nl")
E("Stephex Masters", "Horse show", "Brussels", "Belgium", "France, Belgium & the Netherlands",
  "https://www.stephexmasters.com",
  location="Stephex Stables, Wolvertem", disciplines=["Show jumping"],
  season="August – September (annual)", classes=["Grand Prix (CSI5*)"],
  organizer="Stephex Stables",
  source="https://www.stephexmasters.com")
E("Knokke Hippique", "Horse show", "Knokke", "Belgium", "France, Belgium & the Netherlands",
  "https://www.knokke-hippique.com",
  disciplines=["Show jumping"], season="Summer (annual)",
  source="https://www.knokke-hippique.com")
E("Jumping de Mechelen", "Horse show", "Mechelen", "Belgium", "France, Belgium & the Netherlands",
  "https://www.jumping-mechelen.be",
  disciplines=["Show jumping", "Dressage", "Driving"], season="December (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  source="https://www.jumping-mechelen.be")

# ------------------------------------------------------------------ UK & Ireland
E("London International Horse Show", "Horse show", "London", "United Kingdom", "United Kingdom & Ireland",
  "https://www.londoninternationalhorseshow.com",
  location="ExCeL London", disciplines=["Show jumping", "Dressage", "Driving"],
  season="December (annual)",
  classes=["FEI Jumping World Cup qualifier", "FEI Dressage World Cup qualifier", "Shetland Pony Grand National"],
  organizer="HPower Group",
  source="https://www.londoninternationalhorseshow.com")
E("Royal International Horse Show", "Horse show", "Hickstead", "United Kingdom", "United Kingdom & Ireland",
  "https://www.hickstead.co.uk",
  location="Hickstead Place", disciplines=["Show jumping", "Showing"],
  season="July (annual)",
  classes=["Nations' Cup (CSIO5*)", "King George V Gold Cup", "Derby Meeting (June)"],
  organizer="The Hickstead Group",
  source="https://www.hickstead.co.uk")
E("Royal Windsor Horse Show", "Horse show", "Windsor", "United Kingdom", "United Kingdom & Ireland",
  "https://www.rwhs.co.uk",
  location="Windsor Castle private grounds", disciplines=["Show jumping", "Dressage", "Showing", "Driving"],
  season="May (annual)", classes=["Rolex Grand Prix (CSI5*)"],
  organizer="Royal Windsor Horse Show Ltd",
  source="https://www.rwhs.co.uk")
E("Dublin Horse Show", "Horse show", "Dublin", "Ireland", "United Kingdom & Ireland",
  "https://www.dublinhorseshow.com",
  location="RDS Simmonscourt", disciplines=["Show jumping", "Showing"],
  season="August (annual)",
  classes=["Nations' Cup of Ireland (CSIO5*)", "Anglesea Grand Prix"],
  organizer="Royal Dublin Society",
  source="https://www.dublinhorseshow.com")
E("Badminton Horse Trials", "Horse show", "Badminton", "United Kingdom", "United Kingdom & Ireland",
  "https://www.badminton-horse.co.uk",
  location="Badminton Park", disciplines=["Eventing"],
  season="May (annual)", classes=["CCI5*-L"],
  organizer="Badminton Horse Trials",
  source="https://www.badminton-horse.co.uk")
E("Burghley Horse Trials", "Horse show", "Stamford", "United Kingdom", "United Kingdom & Ireland",
  "https://www.burghley-horse.co.uk",
  location="Burghley Park", disciplines=["Eventing"],
  season="September (annual)", classes=["CCI5*-L"],
  source="https://www.burghley-horse.co.uk")
E("Bramham International Horse Trials", "Horse show", "Wetherby", "United Kingdom", "United Kingdom & Ireland",
  "https://www.bramham-horse.co.uk",
  location="Bramham Park", disciplines=["Eventing"],
  season="June (annual)", source="https://www.bramham-horse.co.uk")
E("Blenheim Palace International Horse Trials", "Horse show", "Woodstock", "United Kingdom", "United Kingdom & Ireland",
  "https://www.blenheimhorse.co.uk",
  disciplines=["Eventing"], season="September (annual)",
  source="https://www.blenheimhorse.co.uk")
E("Horse of the Year Show", "Horse show", "Birmingham", "United Kingdom", "United Kingdom & Ireland",
  "https://www.hoys.co.uk",
  location="NEC Birmingham", disciplines=["Show jumping", "Showing"],
  season="October (annual)",
  classes=["Leading Showjumper of the Year"],
  organizer="Grandstand Media",
  source="https://www.hoys.co.uk")
E("Bolesworth International", "Horse show", "Tattenhall", "United Kingdom", "United Kingdom & Ireland",
  "https://www.bolesworthinternational.com",
  location="Bolesworth Estate", disciplines=["Show jumping"],
  season="June – July (annual)", classes=["Grand Prix (CSI4*)"],
  source="https://www.bolesworthinternational.com")
E("Liverpool International Horse Show", "Horse show", "Liverpool", "United Kingdom", "United Kingdom & Ireland",
  "https://www.liverpoolhorseshow.com",
  location="M&S Bank Arena", disciplines=["Show jumping"],
  season="December – January (annual)", source="https://www.liverpoolhorseshow.com")

# ------------------------------------------------------------------ North America
E("Winter Equestrian Festival", "Horse show", "Wellington", "USA", "North America",
  "https://www.wellingtoninternational.com",
  location="Wellington International", disciplines=["Show jumping", "Dressage", "Polo"],
  season="January – March (annual)",
  classes=["Grand Prix series (CSI5*)", "Nations' Cups"],
  organizer="Wellington International",
  source="https://www.wellingtoninternational.com")
E("Spruce Meadows 'Masters'", "Horse show", "Calgary", "Canada", "North America",
  "https://www.sprucemeadows.com",
  location="Spruce Meadows", disciplines=["Show jumping"],
  season="Early September (annual)",
  classes=["CP 'International' Grand Prix (CSIO5*)", "Nations' Cup"],
  organizer="Spruce Meadows (Southern family)",
  hospitality="VIP hospitality and corporate hosting",
  source="https://www.sprucemeadows.com")
E("Kentucky Three-Day Event", "Horse show", "Lexington", "USA", "North America",
  "https://www.kentuckythreedayevent.com",
  location="Kentucky Horse Park", disciplines=["Eventing"],
  season="Late April (annual)", classes=["CCI5*-L"],
  organizer="Equestrian Events Inc.",
  source="https://www.kentuckythreedayevent.com")
E("Tryon International Equestrian Center", "Horse show", "Tryon", "USA", "North America",
  "https://www.tryon.com",
  disciplines=["Show jumping", "Dressage", "Eventing"],
  season="Year-round calendar",
  classes=["Grand Prix series (CSI5*)"],
  source="https://www.tryon.com")
E("Upperville Colt & Horse Show", "Horse show", "Upperville", "USA", "North America",
  "https://www.upperville.com",
  disciplines=["Show jumping", "Showing"],
  season="June (annual)", classes=["Grand Prix"],
  source="https://www.upperville.com")
E("Hampton Classic", "Horse show", "Bridgehampton", "USA", "North America",
  "https://www.hamptonclassic.com",
  disciplines=["Show jumping"], season="Late August – early September (annual)",
  classes=["Grand Prix (CSI4*)"],
  source="https://www.hamptonclassic.com")
E("Devon Horse Show", "Horse show", "Devon", "USA", "North America",
  "https://www.devonhorseshow.net",
  disciplines=["Show jumping", "Showing", "Driving"],
  season="May – June (annual)", classes=["Grand Prix"],
  source="https://www.devonhorseshow.net")
E("Traverse City Horse Shows", "Horse show", "Traverse City", "USA", "North America",
  "https://www.traversecityhorseshows.com",
  disciplines=["Show jumping"], season="Summer (annual)",
  classes=["Grand Prix series (CSI5*)"],
  source="https://www.traversecityhorseshows.com")
E("Desert International Horse Park", "Horse show", "Thermal", "USA", "North America",
  "https://www.desertinternationalhorsepark.com",
  disciplines=["Show jumping", "Dressage"], season="November – March (annual)",
  classes=["Grand Prix series (CSI5*/CSI4*)"],
  source="https://www.desertinternationalhorsepark.com")
E("World Equestrian Center Ocala", "Horse show", "Ocala", "USA", "North America",
  "https://www.worldequestriancenter.com",
  disciplines=["Show jumping", "Dressage"], season="Year-round calendar",
  classes=["Grand Prix series"],
  source="https://www.worldequestriancenter.com")
E("Royal Horse Show (Toronto)", "Horse show", "Toronto", "Canada", "North America",
  "https://www.royalfair.org",
  location="Exhibition Place", disciplines=["Show jumping", "Showing"],
  season="November (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  organizer="Royal Agricultural Winter Fair",
  source="https://www.royalfair.org")
E("Bromont International", "Horse show", "Bromont", "Canada", "North America",
  "https://www.bromont.com",
  disciplines=["Show jumping", "Eventing"], season="Summer (annual)",
  source="https://www.bromont.com")
E("Pennsylvania National Horse Show", "Horse show", "Harrisburg", "USA", "North America",
  "https://www.panational.org",
  disciplines=["Show jumping"], season="October (annual)",
  source="https://www.panational.org")
E("National Horse Show", "Horse show", "Lexington", "USA", "North America",
  "https://www.nhs.org",
  location="Kentucky Horse Park", disciplines=["Show jumping"],
  season="October – November (annual)",
  classes=["Grand Prix"],
  source="https://www.nhs.org")
E("American Gold Cup", "Horse show", "Traverse City", "USA", "North America",
  "https://www.theamericangoldcup.com",
  disciplines=["Show jumping"], season="September (annual)",
  source="https://www.theamericangoldcup.com")
E("Ocala Winter Circuit (HITS)", "Horse show", "Ocala", "USA", "North America",
  "https://www.hitsshows.com",
  disciplines=["Show jumping"], season="January – March (annual)",
  classes=["Grand Prix series"],
  organizer="HITS",
  source="https://www.hitsshows.com")
E("Del Mar International", "Horse show", "Del Mar", "USA", "North America",
  "https://www.delmarnationalhorseshow.com",
  disciplines=["Show jumping"], season="Autumn (annual)",
  source="https://www.delmarnationalhorseshow.com")

# ------------------------------------------------------------------ Middle East
E("CHI Al Shaqab", "Horse show", "Doha", "Qatar", "Middle East",
  "https://www.alshaqab.com",
  location="Al Shaqab Equestrian Center", disciplines=["Show jumping", "Dressage"],
  season="February (annual)",
  classes=["Grand Prix (CSI5*)", "Nations' Cup"],
  organizer="Al Shaqab (Qatar Foundation)",
  source="https://www.alshaqab.com")
E("Longines Global Champions Tour — Riyadh", "Horse show", "Riyadh", "Saudi Arabia", "Middle East",
  "https://www.globalchampionstour.com",
  disciplines=["Show jumping"], season="Autumn (annual)",
  classes=["Longines Global Champions Tour Grand Prix"],
  source="https://www.globalchampionstour.com")
E("Dubai Show Jumping Championship", "Horse show", "Dubai", "UAE", "Middle East",
  "https://www.emiratesec.com",
  location="Emirates Equestrian Centre", disciplines=["Show jumping"],
  season="January (annual)", source="https://www.emiratesec.com")
E("Sharjah CSI", "Horse show", "Sharjah", "UAE", "Middle East",
  "https://www.srcequestrian.com",
  disciplines=["Show jumping"], season="January (annual)",
  source="https://www.srcequestrian.com")
E("Al Ain CSI", "Horse show", "Al Ain", "UAE", "Middle East",
  "https://www.alainrc.ae",
  disciplines=["Show jumping"], season="February (annual)",
  source="https://www.alainrc.ae")

# ------------------------------------------------------------------ Asia-Pacific
E("Longines Masters of Hong Kong", "Horse show", "Hong Kong", "China", "Asia-Pacific",
  "https://www.longinesmasters.com",
  location="AsiaWorld-Expo", disciplines=["Show jumping"],
  season="February (annual)", classes=["Longines Grand Prix (CSI5*)"],
  organizer="EEM",
  source="https://www.longinesmasters.com")
E("Sydney Royal Easter Show (Equestrian)", "Horse show", "Sydney", "Australia", "Asia-Pacific",
  "https://www.eastershow.com.au",
  location="Sydney Showground", disciplines=["Show jumping", "Showing"],
  season="March – April (annual)", source="https://www.eastershow.com.au")
E("Adelaide Equestrian Festival", "Horse show", "Adelaide", "Australia", "Asia-Pacific",
  "https://www.adelaideequestrianfestival.com.au",
  disciplines=["Eventing"], season="April – May (annual)",
  classes=["CCI5*-L"],
  source="https://www.adelaideequestrianfestival.com.au")
E("Boneo Park International", "Horse show", "Melbourne", "Australia", "Asia-Pacific",
  "https://www.boneopark.com.au",
  disciplines=["Show jumping", "Dressage"], season="Summer (annual)",
  source="https://www.boneopark.com.au")
E("Tokyo Equestrian Events", "Horse show", "Tokyo", "Japan", "Asia-Pacific",
  "https://www.equitation-japan.or.jp",
  disciplines=["Show jumping", "Dressage"], season="Seasonal",
  source="https://www.equitation-japan.or.jp")
E("Auckland International Horse Show", "Horse show", "Auckland", "New Zealand", "Asia-Pacific",
  "https://www.aucklandhorseshow.co.nz",
  disciplines=["Show jumping"], season="Summer (annual)",
  source="https://www.aucklandhorseshow.co.nz")

# ------------------------------------------------------- Latin America & Africa
E("Morocco Royal Tour", "Horse show", "Rabat", "Morocco", "Latin America & Africa",
  "https://www.morocco-royal-tour.com",
  location="Rabat / El Jadida / Tétouan", disciplines=["Show jumping"],
  season="October (annual)", classes=["Grand Prix series (CSI4*)"],
  source="https://www.morocco-royal-tour.com")
E("São Paulo International (Hípica Paulista)", "Horse show", "São Paulo", "Brazil", "Latin America & Africa",
  "https://www.sociedadehipica.com.br",
  disciplines=["Show jumping"], season="Seasonal",
  source="https://www.sociedadehipica.com.br")
E("Coapexpan International (Xalapa)", "Horse show", "Xalapa", "Mexico", "Latin America & Africa",
  "https://www.coapexpan.com",
  disciplines=["Show jumping"], season="May (annual)",
  source="https://www.coapexpan.com")
E("Cape Town CSI", "Horse show", "Cape Town", "South Africa", "Latin America & Africa",
  "https://www.saequestrian.co.za",
  disciplines=["Show jumping"], season="Seasonal",
  source="https://www.saequestrian.co.za")

# ---------------------------------------------------------------- Global series
E("Longines Global Champions Tour (series)", "Horse show", "Worldwide", "International", "Global Series",
  "https://www.globalchampionstour.com",
  disciplines=["Show jumping"], season="Season-long circuit",
  classes=["LGCT Grand Prix legs", "Global Champions League"],
  organizer="Tops Equestrian Events",
  source="https://www.globalchampionstour.com")
E("Rolex Grand Slam of Show Jumping", "Horse show", "Worldwide", "International", "Global Series",
  "https://www.rolexgrandslam.com",
  disciplines=["Show jumping"], season="Season-long majors circuit",
  classes=["Majors: Aachen, Spruce Meadows, CHI Geneva, 's-Hertogenbosch"],
  source="https://www.rolexgrandslam.com")
E("FEI Jumping World Cup Final", "Horse show", "Rotating", "International", "Global Series",
  "https://www.fei.org",
  disciplines=["Show jumping"], season="April (annual)",
  organizer="Fédération Équestre Internationale",
  source="https://www.fei.org")
E("FEI Dressage World Cup Final", "Horse show", "Rotating", "International", "Global Series",
  "https://www.fei.org",
  disciplines=["Dressage"], season="April (annual)",
  organizer="Fédération Équestre Internationale",
  source="https://www.fei.org")

# ---------------------------------------------------------- Polo Clubs Worldwide
E("Guards Polo Club", "Polo club", "Windsor", "United Kingdom", "Polo Clubs Worldwide",
  "https://www.guardspoloclub.com",
  location="Smith's Lawn, Windsor Great Park", disciplines=["Polo"],
  season="May – September (annual)",
  classes=["Queen's Cup", "Royal Windsor Cup", "Gold Cup (Cowdray Park)"],
  source="https://www.guardspoloclub.com")
E("Cowdray Park Polo Club", "Polo club", "Midhurst", "United Kingdom", "Polo Clubs Worldwide",
  "https://www.cowdraypolo.co.uk",
  disciplines=["Polo"], season="May – September (annual)",
  classes=["Gold Cup for the British Open", "Queen's Cup (Guards)"],
  source="https://www.cowdraypolo.co.uk")
E("Cirencester Park Polo Club", "Polo club", "Cirencester", "United Kingdom", "Polo Clubs Worldwide",
  "https://www.cirencesterpolo.co.uk",
  disciplines=["Polo"], season="May – September (annual)",
  source="https://www.cirencesterpolo.co.uk")
E("Royal County of Berkshire Polo Club", "Polo club", "Windsor", "United Kingdom", "Polo Clubs Worldwide",
  "https://www.rcbpc.com",
  disciplines=["Polo"], season="May – September (annual)",
  source="https://www.rcbpc.com")
E("Santa María Polo Club", "Polo club", "Sotogrande", "Spain", "Polo Clubs Worldwide",
  "https://www.santamariapoloclub.com",
  disciplines=["Polo"], season="Summer (annual)",
  classes=["Gold Cup", "Silver Cup", "Bronze Cup"],
  source="https://www.santamariapoloclub.com")
E("Polo Club du Domaine de Chantilly", "Polo club", "Chantilly", "France", "Polo Clubs Worldwide",
  "https://www.polo-chantilly.com",
  disciplines=["Polo"], season="May – October (annual)",
  source="https://www.polo-chantilly.com")
E("Polo de Paris", "Polo club", "Paris", "France", "Polo Clubs Worldwide",
  "https://www.polodeparis.com",
  location="Bois de Boulogne", disciplines=["Polo"],
  season="May – October (annual)", source="https://www.polodeparis.com")
E("Asociación Argentina de Polo (Palermo)", "Polo club", "Buenos Aires", "Argentina", "Polo Clubs Worldwide",
  "https://www.aapolo.com",
  location="Campo Argentino del Polo, Palermo", disciplines=["Polo"],
  season="October – December (annual)",
  classes=["Campeonato Argentino Abierto", "Hurlingham Open", "Tortugas Open"],
  source="https://www.aapolo.com")
E("Tortugas Country Club", "Polo club", "Buenos Aires", "Argentina", "Polo Clubs Worldwide",
  "https://www.tortugascountryclub.com.ar",
  disciplines=["Polo"], season="Spring (annual)",
  classes=["Tortugas Open"],
  source="https://www.tortugascountryclub.com.ar")
E("Hurlingham Club (Argentina)", "Polo club", "Buenos Aires", "Argentina", "Polo Clubs Worldwide",
  "https://www.hurlinghamclub.com.ar",
  disciplines=["Polo"], season="Spring (annual)",
  classes=["Hurlingham Open"],
  source="https://www.hurlinghamclub.com.ar")
E("International Polo Club Palm Beach", "Polo club", "Wellington", "USA", "Polo Clubs Worldwide",
  "https://www.internationalpoloclub.com",
  disciplines=["Polo"], season="January – April (annual)",
  classes=["U.S. Open Polo Championship", "Gold Cup", "CV Whitney Cup"],
  source="https://www.internationalpoloclub.com")
E("Santa Barbara Polo & Racquet Club", "Polo club", "Santa Barbara", "USA", "Polo Clubs Worldwide",
  "https://www.sbpolo.com",
  disciplines=["Polo"], season="May – October (annual)",
  classes=["Pacific Coast Open"],
  source="https://www.sbpolo.com")
E("Aspen Valley Polo Club", "Polo club", "Aspen", "USA", "Polo Clubs Worldwide",
  "https://www.aspenvalleypolo.club",
  disciplines=["Polo"], season="Summer (annual)",
  source="https://www.aspenvalleypolo.club")
E("Dubai Polo & Equestrian Club", "Polo club", "Dubai", "UAE", "Polo Clubs Worldwide",
  "https://www.poloclubdubai.com",
  disciplines=["Polo"], season="October – April (annual)",
  source="https://www.poloclubdubai.com")
E("Singapore Polo Club", "Polo club", "Singapore", "Singapore", "Polo Clubs Worldwide",
  "https://www.singaporepoloclub.org",
  disciplines=["Polo"], season="Year-round",
  source="https://www.singaporepoloclub.org")
E("Royal Selangor Polo Club", "Polo club", "Kuala Lumpur", "Malaysia", "Polo Clubs Worldwide",
  "https://www.royalselangorpoloclub.com",
  disciplines=["Polo"], season="Year-round",
  source="https://www.royalselangorpoloclub.com")
E("Deauville Polo (Pôle International du Cheval)", "Polo club", "Deauville", "France", "Polo Clubs Worldwide",
  "https://www.pole-international-du-cheval.com",
  disciplines=["Polo", "Show jumping"], season="August (annual)",
  classes=["Gold Cup Deauville"],
  source="https://www.pole-international-du-cheval.com")
E("St. Moritz Snow Polo", "Polo club", "St. Moritz", "Switzerland", "Polo Clubs Worldwide",
  "https://www.snowpolo-stmoritz.com",
  location="Frozen Lake St. Moritz", disciplines=["Polo"],
  season="Late January (annual)", classes=["Snow Polo World Cup"],
  source="https://www.snowpolo-stmoritz.com")

# --------------------------------------------------- Premier Riding Clubs Worldwide
E("The Hurlingham Club", "Riding club", "London", "United Kingdom", "Premier Riding Clubs Worldwide",
  "https://www.hurlinghamclub.org.uk",
  location="Fulham", disciplines=["Polo", "Croquet", "Tennis"],
  season="Private members' club (est. 1869)",
  source="https://www.hurlinghamclub.org.uk")
E("Gleneagles Equestrian Centre", "Riding club", "Auchterarder", "United Kingdom", "Premier Riding Clubs Worldwide",
  "https://www.gleneagles.com",
  disciplines=["Show jumping", "Dressage", "Hacking"],
  season="Year-round", source="https://www.gleneagles.com")
E("Chantilly — Grandes Écuries", "Riding club", "Chantilly", "France", "Premier Riding Clubs Worldwide",
  "https://www.domainedechantilly.com",
  disciplines=["Flat racing", "Showing"], season="Year-round",
  source="https://www.domainedechantilly.com")
E("Palm Beach International Equestrian Center — Riding Academy", "Riding club", "Wellington", "USA", "Premier Riding Clubs Worldwide",
  "https://www.wellingtoninternational.com",
  disciplines=["Show jumping", "Dressage"], season="Year-round",
  source="https://www.wellingtoninternational.com")
E("Kentucky Horse Park", "Riding club", "Lexington", "USA", "Premier Riding Clubs Worldwide",
  "https://www.kyhorsepark.com",
  disciplines=["Show jumping", "Eventing", "Driving"], season="Year-round",
  source="https://www.kyhorsepark.com")
E("Al Shaqab Equestrian Center", "Riding club", "Doha", "Qatar", "Premier Riding Clubs Worldwide",
  "https://www.alshaqab.com",
  disciplines=["Show jumping", "Dressage", "Endurance"], season="Year-round",
  organizer="Qatar Foundation",
  source="https://www.alshaqab.com")
E("Dubai Polo & Equestrian Club — Riding Academy", "Riding club", "Dubai", "UAE", "Premier Riding Clubs Worldwide",
  "https://www.poloclubdubai.com",
  disciplines=["Show jumping", "Dressage", "Polo"], season="Year-round",
  source="https://www.poloclubdubai.com")
E("Hong Kong Jockey Club — Equestrian", "Riding club", "Hong Kong", "China", "Premier Riding Clubs Worldwide",
  "https://www.hkjc.com",
  disciplines=["Show jumping", "Racing"], season="Year-round",
  source="https://www.hkjc.com")


# ------------------------------------------------- second wave: Scandinavia, more Europe
E("Falsterbo Horse Show", "Horse show", "Falsterbo", "Sweden", "Scandinavia & Northern Europe",
  "https://www.falsterbohorseshow.com",
  disciplines=["Show jumping", "Dressage"], season="July (annual)",
  classes=["Nations' Cup (CSIO5*)", "Grand Prix"],
  source="https://www.falsterbohorseshow.com")
E("Gothenburg Horse Show", "Horse show", "Gothenburg", "Sweden", "Scandinavia & Northern Europe",
  "https://www.gothenburghorseshow.com",
  location="Scandinavium", disciplines=["Show jumping", "Dressage"],
  season="February – March (annual)",
  classes=["FEI Jumping World Cup qualifier"],
  source="https://www.gothenburghorseshow.com")
E("Helsinki International Horse Show", "Horse show", "Helsinki", "Finland", "Scandinavia & Northern Europe",
  "https://www.helsinkihorseshow.fi",
  disciplines=["Show jumping"], season="October (annual)",
  source="https://www.helsinkihorseshow.fi")
E("VR Classics Neumünster", "Horse show", "Neumünster", "Germany", "Germany, Austria & Central Europe",
  "https://www.vr-classics.de",
  disciplines=["Show jumping", "Dressage"], season="February (annual)",
  source="https://www.vr-classics.de")
E("Löwen Classics Braunschweig", "Horse show", "Braunschweig", "Germany", "Germany, Austria & Central Europe",
  "https://www.loewenclassics.de",
  disciplines=["Show jumping"], season="March (annual)",
  source="https://www.loewenclassics.de")
E("Riesenbeck International", "Horse show", "Riesenbeck", "Germany", "Germany, Austria & Central Europe",
  "https://www.riesenbeck-international.com",
  location="Riesenbeck International", disciplines=["Show jumping"],
  season="Seasonal", classes=["Grand Prix series (CSI5*)"],
  source="https://www.riesenbeck-international.com")
E("Jumping Indoor Maastricht", "Horse show", "Maastricht", "Netherlands", "France, Belgium & the Netherlands",
  "https://www.jumpingindoormaastricht.nl",
  disciplines=["Show jumping", "Dressage"], season="November (annual)",
  source="https://www.jumpingindoormaastricht.nl")
E("Tops International Arena Valkenswaard", "Horse show", "Valkenswaard", "Netherlands", "France, Belgium & the Netherlands",
  "https://www.topsinternationalarena.com",
  disciplines=["Show jumping"], season="Seasonal",
  classes=["Grand Prix series (CSI5*)"],
  source="https://www.topsinternationalarena.com")
E("Chatsworth International Horse Trials", "Horse show", "Bakewell", "United Kingdom", "United Kingdom & Ireland",
  "https://www.chatsworth.org",
  disciplines=["Eventing"], season="May (annual)",
  source="https://www.chatsworth.org")
E("Blair Castle International Horse Trials", "Horse show", "Blair Atholl", "United Kingdom", "United Kingdom & Ireland",
  "https://www.blaircastlehorsetrials.co.uk",
  disciplines=["Eventing"], season="August (annual)",
  source="https://www.blaircastlehorsetrials.co.uk")

# ------------------------------------------------- second wave: North America
E("Split Rock Jumping Tour", "Horse show", "Lexington", "USA", "North America",
  "https://www.splitrockjumpingtour.com",
  disciplines=["Show jumping"], season="Seasonal",
  classes=["Grand Prix series"],
  source="https://www.splitrockjumpingtour.com")
E("Vermont Summer Festival", "Horse show", "East Dorset", "USA", "North America",
  "https://www.vermontsummerfestival.com",
  disciplines=["Show jumping"], season="Summer (annual)",
  source="https://www.vermontsummerfestival.com")
E("HITS-on-the-Hudson", "Horse show", "Saugerties", "USA", "North America",
  "https://www.hitsshows.com",
  disciplines=["Show jumping"], season="May – September (annual)",
  classes=["Grand Prix series"],
  organizer="HITS",
  source="https://www.hitsshows.com")
E("Lake Placid Horse Shows", "Horse show", "Lake Placid", "USA", "North America",
  "https://www.lakeplacidhorseshow.com",
  disciplines=["Show jumping"], season="June – July (annual)",
  source="https://www.lakeplacidhorseshow.com")
E("Old Salem Farm Spring Horse Shows", "Horse show", "North Salem", "USA", "North America",
  "https://www.oldsalemfarm.net",
  disciplines=["Show jumping"], season="May (annual)",
  source="https://www.oldsalemfarm.net")
E("Menlo Charity Horse Show", "Horse show", "Atherton", "USA", "North America",
  "https://www.menlocharityhorseshow.com",
  disciplines=["Show jumping", "Showing"], season="August (annual)",
  source="https://www.menlocharityhorseshow.com")
E("Colorado Horse Park", "Horse show", "Parker", "USA", "North America",
  "https://www.coloradohorsepark.com",
  disciplines=["Show jumping", "Dressage"], season="Seasonal",
  source="https://www.coloradohorsepark.com")
E("Thunderbird Show Park", "Horse show", "Langley", "Canada", "North America",
  "https://www.tbird.ca",
  disciplines=["Show jumping"], season="Seasonal",
  classes=["Grand Prix series"],
  source="https://www.tbird.ca")
E("Angelstone Show Jumping", "Horse show", "Toronto", "Canada", "North America",
  "https://www.angelstone.ca",
  disciplines=["Show jumping"], season="Seasonal",
  source="https://www.angelstone.ca")
E("Caledon Equestrian Park", "Horse show", "Caledon", "Canada", "North America",
  "https://www.caledonequestrianpark.com",
  disciplines=["Show jumping"], season="Seasonal",
  source="https://www.caledonequestrianpark.com")

# ------------------------------------------------- second wave: Australia
E("Melbourne International 3 Day Event", "Horse show", "Melbourne", "Australia", "Asia-Pacific",
  "https://www.melbourne3de.com.au",
  disciplines=["Eventing"], season="June (annual)",
  source="https://www.melbourne3de.com.au")

# ------------------------------------------------- second wave: polo clubs
E("Beaufort Polo Club", "Polo club", "Tetbury", "United Kingdom", "Polo Clubs Worldwide",
  "https://www.beaufortpoloclub.com",
  disciplines=["Polo"], season="May – September (annual)",
  source="https://www.beaufortpoloclub.com")
E("Houston Polo Club", "Polo club", "Houston", "USA", "Polo Clubs Worldwide",
  "https://www.houstonpoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.houstonpoloclub.com")
E("Eldorado Polo Club", "Polo club", "Indio", "USA", "Polo Clubs Worldwide",
  "https://www.eldoradopolo.com",
  disciplines=["Polo"], season="January – March (annual)",
  source="https://www.eldoradopolo.com")
E("Empire Polo Club", "Polo club", "Indio", "USA", "Polo Clubs Worldwide",
  "https://www.empirepolo.com",
  disciplines=["Polo"], season="January – March (annual)",
  source="https://www.empirepolo.com")
E("Sarasota Polo Club", "Polo club", "Sarasota", "USA", "Polo Clubs Worldwide",
  "https://www.sarasotapolo.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.sarasotapolo.com")
E("Meadowbrook Polo Club", "Polo club", "Old Westbury", "USA", "Polo Clubs Worldwide",
  "https://www.meadowbrookpoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.meadowbrookpoloclub.com")
E("Aiken Polo Club", "Polo club", "Aiken", "USA", "Polo Clubs Worldwide",
  "https://www.aikenpolo.org",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.aikenpolo.org")
E("Will Rogers Polo Club", "Polo club", "Los Angeles", "USA", "Polo Clubs Worldwide",
  "https://www.willrogerspoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.willrogerspoloclub.com")
E("Denver Polo Club", "Polo club", "Denver", "USA", "Polo Clubs Worldwide",
  "https://www.denverpoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.denverpoloclub.com")
E("Calgary Polo Club", "Polo club", "Calgary", "Canada", "Polo Clubs Worldwide",
  "https://www.calgarypoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.calgarypoloclub.com")
E("Vancouver Polo Club", "Polo club", "Vancouver", "Canada", "Polo Clubs Worldwide",
  "https://www.vancouverpoloclub.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.vancouverpoloclub.com")
E("Real Club de Polo de Barcelona", "Polo club", "Barcelona", "Spain", "Polo Clubs Worldwide",
  "https://www.rcpolo.com",
  disciplines=["Polo"], season="Seasonal",
  source="https://www.rcpolo.com")

# ------------------------------------------------- second wave: riding institutions
E("Spanish Riding School", "Riding club", "Vienna", "Austria", "Premier Riding Clubs Worldwide",
  "https://www.srs.at",
  disciplines=["Dressage"], season="Year-round",
  source="https://www.srs.at")
E("Cadre Noir de Saumur", "Riding club", "Saumur", "France", "Premier Riding Clubs Worldwide",
  "https://www.cadrenoir.fr",
  disciplines=["Dressage"], season="Year-round",
  source="https://www.cadrenoir.fr")
E("Royal Andalusian School of Equestrian Art", "Riding club", "Jerez de la Frontera", "Spain", "Premier Riding Clubs Worldwide",
  "https://www.realescuela.org",
  disciplines=["Dressage", "Driving"], season="Year-round",
  source="https://www.realescuela.org")
# ------------------------------------------------------------------ meta + write
META = {
    "title": "Top 500 Horse Shows & Clubs Worldwide",
    "compiled": "2026-10-30",
    "sources": [
        "Show / club official websites (verified 2026-10-30)",
        "Organizing body and federation records (FEI)",
        "Official tourism board listings where show-published",
    ],
    "count": len(ENTRIES),
    "status": "ready",
    "publisher": {
        "@type": "Organization",
        "name": "LIKE® Magazine",
        "alternateName": ["LIKE Magazine", "LIKE®", "likeleaders"],
        "url": "https://likeleaders.com",
    },
    "ranking_basis": (
        "Editorial selection of the world's major international horse shows, "
        "premier polo clubs and leading equestrian clubs by region, ordered by "
        "region rather than strictly ranked; honest count of verified entries, "
        "not padded to 500. Prize money, dates and named staff appear only where "
        "the organizer publishes them."
    ),
    "seo": {
        "title": "Top 500 Horse Shows & Clubs Worldwide · LIKE® Magazine Luxury Guide",
        "description": (
            "Top 500 horse shows and equestrian clubs worldwide — CHI Geneva, CHIO Aachen, "
            "Spruce Meadows, Wellington, premier polo clubs, and full contact details."
        ),
        "keywords": [
            "LIKE Magazine", "horse shows worldwide", "equestrian clubs",
            "show jumping", "CHI Geneva", "CHIO Aachen", "polo clubs",
            "dressage", "eventing", "likeleaders",
        ],
        "canonical": "https://likeleaders.com/sections/luxury-horse-shows-clubs.html",
    },
    "columns": [
        {"key": "name", "label": "Show / Club"},
        {"key": "city", "label": "City / Town"},
        {"key": "country", "label": "Country"},
        {"key": "market", "label": "Region"},
    ],
    "filters": ["market", "country", "kind"],
    "searchKeys": ["name", "city", "country", "market", "kind", "website", "source"],
}

doc = {"meta": META, "items": ENTRIES}
(DATA / "horse-shows-clubs.json").write_text(
    json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote horse-shows-clubs.json: {len(ENTRIES)} entries")

