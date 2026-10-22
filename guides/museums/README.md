# The World's Great Museums

**A LIKE® Museums Guide** — the worldwide guide of the Museums department of LIKE® Magazine (likeleaders.com).
Compiled October 2026.

## Scope

The world's great public museums of art, antiquities and national collections — encyclopedic and national-calibre
institutions only — in three sections:

1. **Europe's Great Houses of Art** — 22 museums.
2. **The Americas** — 9 museums (all, in this edition, in the United States; see Named gaps).
3. **Asia, the Middle East & Oceania** — 9 museums.

Per museum the CSV records: name; category; city and country; founding year; the director, verified current in
October 2026 (with president/chair where the governance splits); collection scale — object counts **only** where
the museum itself publishes them; signature works; visitor numbers from officially published figures **with the
year always stated**; an architecture note; the official website and a published contact route; notes; and
sources per row.

## Method

- Official sources first — museum websites, official annual reports and press releases — reputable press second
  (Associated Press, Reuters, The Art Newspaper, Artnet News, Le Monde, Korea JoongAng Daily).
- **Directors are the guide's signature risk and were verified one by one.** A large share of the roster changed
  hands in 2024–26. The guide prints, among others: Christophe Leribault at the Louvre (Laurence des Cars resigned
  in February 2026, after the October 2025 crown-jewels theft); Annick Lemoine at the Musée d'Orsay and de
  l'Orangerie (the brief's starting name, Sylvie Patry, was a former senior curator who left in 2022; the
  presidency has since passed through Christophe Leribault and Sylvain Amic, who died in office in August 2025);
  Tate's layered position (Maria Balshaw stepped down in December 2025; Karin Hindsbo is interim director;
  Jessica Morgan takes office on 1 January 2027); the Met's consolidated leadership (Max Hollein is director
  **and** CEO; the separate presidency ended in 2023); Miren Arzalluz at Guggenheim Bilbao; Jonathan Fine in
  Vienna; Souraya Noujaim at Louvre Abu Dhabi (announced 10 October 2026); Olga Galaktionova at the Tretyakov;
  Pierre Terjanian in Boston; Daniel H. Weiss in Philadelphia; and Marion Ackermann as president of the
  foundation that governs Berlin's state museums.
- **Visitor numbers are never blended.** Museums report on different bases (calendar year, financial year,
  main building only, whole complex). Each figure carries its year and basis in the entry; where two bases exist
  for one museum (the British Museum, the Met), both are printed, labelled.
- Collection counts appear **only** where the museum itself publishes them (British Museum: eight million
  objects; National Museum of China: more than 1.4 million items; Mauritshuis: 854 objects). Where no count is
  published in that form, the entry describes the collection without a number.
- Where a field could not be verified to standard, the entry says so in words — no figure, name or date in this
  guide is a guess.

## Counts (October 2026)

- **40 museums** in the guide.
- Museums in **19 countries** and **28 cities**: Australia, Austria, China, Egypt, France, Germany, Greece, Italy, Japan, Netherlands, Qatar, Russia, South Korea, Spain, Taiwan, United Arab Emirates, United Kingdom, United States, Vatican City.
- Sections: Europe 22 · The Americas 9 · Asia, the Middle East & Oceania 9.

## Director fields that could not be printed as a verified current name

- **National Museum of Korea — VACANT.** You Hong-june, appointed 20 July 2025, announced his resignation on
  Wednesday 21 October 2026 (accepted by President Lee Jae Myung the same day) over a calligraphy scroll from his
  own collection, misattributed to independence activist Park Won-geun, that had been exhibited at the museum.
  No successor had been announced when this guide closed (22 October 2026).
- **Leeum Museum of Art — NO DIRECTOR SINCE 2017.** Hong Ra-hee resigned as director in 2017 and returned on
  2 April 2025 as Honorary Director (Samsung Foundation of Culture announcement); Kim Sung-won is Deputy
  Director. The guide names no director.
- **National Museum of China — CONFLICTING SOURCES, RESOLVED TO THE MUSEUM'S OWN SITE.** Wikipedia and older
  sources name Wang Chunfa; 2024–25 reports name Gao Zheng and Li Qun in director-level roles. The museum's own
  English site (en.chnmuseum.cn) named Luo Wenli as Director in its reports of 17 and 22 June 2026; the guide
  prints Luo Wenli and records the conflict in the entry.

## Named gaps — stated honestly

Latin America has no entry in this roster, and it is the guide's largest gap: Mexico City's Museo Nacional de Antropología received 5,048,893 visitors in 2025 (The Art Newspaper's survey) — among the ten most visited art and antiquities museums in the world — and is the recommended first build of the department's next edition. Sub-Saharan Africa likewise has no entry (the Grand Egyptian Museum represents North Africa); no institution there was verified to this guide's standard in this pass. South Asia has no entry. Canada was considered — the Art Gallery of Ontario is the strongest candidate — and cut at the roster's cap of 40, which is also why the Americas section is, in this edition, a United States section; that is stated plainly rather than disguised. Two institutions in The Art Newspaper's 2025 top ten are not in the roster: the State Russian Museum, St Petersburg (5,087,276 visitors in 2025), and Shanghai Museum East (4,593,216 in 2025). Excluded by design: science and natural-history museums (the Natural History Museum, London, drew 7.1 million visitors in 2025 and belongs to a future guide of its own), single-artist houses as a class — with two deliberate exceptions, the Van Gogh Museum and the Musée de l'Orangerie, both national museums of the first rank named in the commissioning brief — and private house-museums. The Leeum Museum of Art is a private foundation museum, included as a brief-listed peer and labelled as such in its entry. Director fields that could not be printed as a verified current name: the National Museum of Korea (vacant since 21 October 2026, no successor announced at press time) and the Leeum Museum of Art (no director since 2017; an honorary director and a deputy director only).

## Files

- `museums.csv` — the master data file (this folder).
- `entries.py` — the working source data used to generate all outputs.
- `build_outputs.py` / `build_web.py` — the build scripts (adapted from the LIKE® Weddings build).
- Library copies (PDF + DOCX): `~/workspace/your_files/The World's Great Museums - LIKE Museums Guide.pdf` / `.docx`.
- Web package (staged, not published): `~/workspace/likeleaders-site/sections/museums.html`,
  `~/workspace/likeleaders-site/articles/like-worlds-great-museums.html` (the full guide) and
  `~/workspace/likeleaders-site/articles/like-museums-directors-cultural-statesmen.html` (supporting editorial);
  homepage card snippet at `~/workspace/likeleaders-site/snippet-museums-card.html`.
