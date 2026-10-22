# The World's Healthcare Providers — LIKE® Magazine Health Guide

**40 major hospital groups and health systems worldwide, 16 columns, as of October 22, 2026.**
The flagship guide of LIKE® Magazine's Health department.

## Roster by region (as grouped in the guide)

- North America: 13
- Europe: 5
- Africa, Europe and the Middle East: 1
- Africa: 2
- Oceania, Europe and Asia: 1
- Oceania: 1
- Asia: 11
- Asia and the Middle East: 1
- Europe and Asia (Türkiye): 1
- South America: 2
- Middle East: 1
- Asia, Africa and Central Asia: 1

## Files

- `healthcare_providers.csv` — the master list (40 rows × 17 columns, UTF-8)
- `entries.py` / `entries2.py` — the source data (single source of truth for all builds)
- `build_all.py` — builds the CSV, this README's companions, the PDF, the DOCX, the staged article page, the staged Health department page and the homepage snippet
- Deliverables in `~/workspace/your_files/`: `The World's Healthcare Providers - LIKE Health Guide.pdf` and `.docx`
- Staged web pages in `~/workspace/likeleaders-site/`: `articles/like-worlds-healthcare-providers.html`, `sections/health.html`, `snippet-health-card.html` — STAGED ONLY, not published or pushed

## Field set (the depth standard — applied to every entry, in CSV, PDF/DOCX and web alike)

1. `rank` — position in the guide (editorial order: anchor academic systems first, then by region; not a quality ranking)
2. `name` — provider name as it publishes it
3. `region` — guide grouping
4. `hq` — headquarters city
5. `country`
6. `founded`
7. `type` — private / nonprofit / public system, with legal form where published
8. `ownership_parent` — owner or parent, including listing venue for traded groups
9. `leadership` — full executive leadership with exact published titles: CEO/president, chair where applicable, CFO, COO, chief medical officer and equivalents where published. Where a title is not published or could not be verified from official sources, the cell says so plainly.
10. `facilities_scale` — hospitals, beds, staff and patients, dated and sourced from official publications
11. `specialties` — specialties of note, in full
12. `patient_categories` — patient/client categories where published, else "not disclosed"-style wording in the cell
13. `contact` — official contact route; published emails and phones only where the provider itself publishes them — never guessed
14. `website` — official site
15. `sources` — per-row source attribution
16. `notes` — dated transitions, overlaps and honest caveats

## Methodology and rules

- Official published sources first: provider sites, annual reports, regulatory and exchange filings, and established trade press reporting of official statements. Verification currency: October 2026.
- **Unverifiable beats guessed.** Every field that could not be verified says so in the cell; the column stays in the schema for every entry.
- Leadership transitions announced for 2026–2027 are recorded with their dates (Mayo Clinic, Netcare, Ascension, King's College Hospital).
- Related-party overlaps are stated, never hidden: IHH Healthcare (30) is the parent of Fortis Healthcare (26) and Acibadem (32); all three are listed because each publishes its own leadership, brand and patient base. UPMC's October 2026 acquisition of Ohio's Trinity Health System is a different organization from Trinity Health of Michigan (10), and both entries say so.
- Public systems' flagship operators are in scope where they are genuine providers (AP-HP, Charité, Karolinska, SingHealth, NUHS, UHN, Sheba, King's).

## Named gaps (honest limitations)

1. **CFO/COO/CMO depth varies by disclosure culture.** U.S. listed and large nonprofit systems publish full C-suites; several European public hospitals, Korean flagship hospitals and Singapore clusters publish full management mainly in their home language or not as a single list. Those cells name the CEO/chair verified and flag the rest rather than reconstructing titles.
2. **King's College Hospital chief executive succession:** Professor Clive Kay announced retirement for summer 2026 (Nov. 6, 2025); no successor was verified in official sources at publication.
3. **Mediclinic** has published thinner group data since its 2023 delisting; its scale figures are dated 2024.
4. **Consolidated bed/staff totals are not published as single figures** for SingHealth, Einstein Hospital Israelita and the AKDN health system; the cells say so instead of assembling totals from mixed years.
5. **General contact emails are rarely published** by hospital groups; most entries therefore give the official contact route and only list an email or phone where the provider itself publishes one (published examples: Medanta, Samsung Medical Center, Bumrungrad, Fortis investor/secretarial contacts).
6. **China and Japan** have no entry: no mainland Chinese or Japanese hospital group met the verification standard in English-language official sources within this build; the gap is named rather than padded.
7. Ramsay Health Care's proposed separation of Ramsay Santé (late 2026, subject to a November 2026 shareholder vote) may change its European footprint in the next edition.
