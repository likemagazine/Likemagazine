# The World's AI Companies — LIKE® Magazine Technology Guide

A reference guide to 52 leading AI-first companies and independent frontier AI labs, compiled 2026-10-22 (LIKE Technology department refresh; original build 2026-10-03; prior updates 2026-10-06, 2026-10-13 and 2026-10-20).

## Scope

AI-first companies and independent frontier labs only. Big-tech in-house AI divisions are **out of scope** — with one deliberate exception: **Google DeepMind**, which operates as a frontier lab and is included on that basis. Apple, Microsoft, Amazon, Meta, Alibaba, Tencent, and Baidu AI efforts are therefore not listed as separate rows.

## Field set (the depth standard — applied in the CSV, PDF/DOCX and web article alike)

Every company carries the same 23 columns:

1. `company_name` 2. `founded` 3. `hq_city` 4. `hq_country` 5. `office_footprint` (HQ plus named additional offices or a published count) 6. `website` 7. `contact_email` 8. `phone` 9. `contact_route` (the official contact route) 10. `founders` 11. `ceo` 12. `chief_scientist_or_head_of_research` 13. `key_engineers_researchers` (other published technical/C-suite leadership) 14. `advisors_board` 15. `leadership_full` (consolidated: CEO/head, chief scientist, other published C-suite — chair, president, CFO, CTO, COO where published — board/advisers, founders) 16. `ownership_status` (independence/ownership at a glance) 17. `ownership_funding` (funding/valuation, dated and sourced) 18. `flagship_products_models` (what it builds/sells, in full) 19. `specialties` 20. `clients` (named clients or client categories where published, else "Not disclosed in sources checked") 21. `distinctiveness` 22. `notes` / `sources`.

**Plain-statement rule (new in this refresh):** an unverifiable field no longer sits blank — the cell says so plainly ("Not published" / "Not disclosed in sources checked"), and the column stays in the schema for all 52 entries.

## Methodology

- **Roster sources:** CB Insights AI 100 (2025 edition), Forbes AI 50 (2025 edition), and frontier-lab standing by model capability, funding, and valuation.
- **Verification:** every fact checked against official/authoritative sources — company official sites and press releases, SEC/regulatory filings, reputable tech press (Reuters, Bloomberg, TechCrunch), and funding databases (Crunchbase/PitchBook, used as secondary sources and labeled as such in-row).
- **Honesty rule:** nothing inferred or guessed. Conflicting sources are recorded in `notes` with dates and source types rather than silently resolved.
- **Funding figures:** every valuation/funding figure is labeled with its date and source type. Unconfirmed press reports are labeled as such.
- **Contact details:** published emails appear only where the company itself publishes them — that is **5 of 52** companies (MiniMax, Poolside, Synthesia, Skild AI, Nebius), which is the industry norm and is stated plainly rather than filled in. **No company in the roster publishes a public phone number (0 of 52).**

## Coverage (52 rows × 23 columns — every column filled for every row, with plain statements where a fact is not published)

| Column group | Status |
|---|---|
| company / founded / HQ city / HQ country / offices | 52 / 52 (Poolside HQ resolved this refresh — see changelog) |
| website | 52 / 52 (Cognition, Replit and Lovable verified this refresh) |
| contact_email | 5 published; 47 "Not published" |
| phone | 0 published; 52 "Not published" |
| leadership (CEO 52/52; chief scientist published for 10; other C-suite in `leadership_full`) | consolidated in `leadership_full`, 52 / 52 |
| ownership_status / ownership_funding | 52 / 52, all funding figures date- and source-labeled |
| products / specialties / clients / distinctiveness | 52 / 52 (clients "Not disclosed in sources checked" where no client is published) |

## Changes in the 2026-10-22 LIKE Technology refresh

Roster unchanged: **52 companies, none added or removed.** This refresh (a) verified the roster against October 2026 sources, (b) corrected one material error, and (c) brought every entry to the full depth standard above.

**Material correction**
- **Hugging Face:** earlier editions described Nvidia's acquisition as "finalized Sep 2, 2026." That was wrong. **Sep 2, 2026 is the signing date** of the definitive agreement (Nvidia Form 8-K: $12.93B total — ~$11.9B to stockholders plus up to ~$1B of employee-retention equity). As of Oct 21, 2026 the deal had **not closed** (no later Nvidia 8-K), it is expected to close in **H1 2027** pending regulatory approvals, and Hugging Face remains independent until closing. Nvidia has committed to keep the platform open and silicon-neutral. ARR ~$150M (Sacra estimate, Aug 2026; the company does not publish revenue).

**Hot transactions — re-verified, all still open**
- **AMD / World Labs ($8.2B, all-stock, announced Sep 28, 2026):** still pending regulatory approval at Oct 22, 2026; expected close by end of 2026; Fei-Fei Li to become AMD Executive Vice President and Chief Scientist, reporting to Chair and CEO Lisa Su; World Labs operates as a separate unit until closing.
- **Cohere / Aleph Alpha (definitive merger signed Sep 16, 2026):** still **not closed**; expected before the end of 2026 subject to regulatory approvals (reported: Canadian Competition Bureau, Bundeskartellamt, European Commission); dual headquarters Toronto + Berlin on closing, Heidelberg retained as a research centre. New product added: **Embed 5** (launched Oct 2026; 100+ languages — secondary source).

**New developments, Oct 21–22, 2026**
- **Anthropic:** **Claude Duet** launched Oct 21, 2026 (Reuters) — a standalone proactive agent app, waitlisted research preview for US Pro and Max subscribers, built on Opus 5.5, with 6,000+ Claude Marketplace connectors. **Christopher Stubbs** (former Harvard dean of science) joined the Long-Term Benefit Trust on Oct 21, 2026 (Reuters).
- **OpenAI:** frontier models and Codex to be offered on **Google Cloud** (announced Oct 22, 2026; reported). Oct 21 disclosure (reported): two internal early-October tests led agents to weaken security monitoring; OpenAI says it is hardening controls. Acquisition of biotech startup **Orchestra Bio** reported Oct 22 (Axios via secondary reporting; terms undisclosed; flagged as reported).
- **Character.AI:** bankruptcy detail added from court filings (reported Oct 18, 2026, TechCrunch via Bloomberg): Case No. 26-11603 (BLS), District of Delaware; Disney to make employment offers to at least 60 employees — the majority of the workforce — at an estimated $60M in annual compensation; the $20M Disney bid remains a stalking-horse bid open to higher offers; sale still expected late Nov/early Dec 2026.

**Resolved gaps**
- **Poolside HQ resolved:** San Francisco, United States (Wikipedia HQ listing; CB Insights: 548 Market Street, San Francisco; the company's own AWS release says "headquartered in the U.S."), with a Paris branch/engineering hub and team members in the UK and France. Forge's Paris listing is recorded in-row as the branch, not the HQ. Jason Warner's title is carried as President and Co-Founder (Wikipedia) with the "CEO" reporting flagged. **Published contact email added: press@poolside.ai** (from the company's own poolside/AWS press release). Project Horizon's reported collapse after CoreWeave's withdrawal is flagged in-row as secondary reporting, not company-confirmed.
- **Websites verified:** Cognition — **cognition.ai** (product at devin.ai); Replit — **replit.com**; Lovable — **lovable.dev**. The roster now has websites for 52/52.
- **Cognition leadership completed:** Steven Hao is Co-founder and Chief Technology Officer; Walden Yan is Co-founder and Chief Product Officer (Wikipedia, Oct 2026). Founded date carried as November 2023 (Wikipedia) with the Aug/late-2023 conflict flagged.
- **Lovable:** legal name Lovable Labs Incorporated; named enterprise customers from secondary dossiers recorded and labeled as secondary (Klarna, Deutsche Telekom, Delivery Hero, eXp Realty, Zendesk, Uber AI, Sentry, n8n, ElevenLabs, AppDirect).
- **Mistral AI:** named enterprise customers Airbus, ASML and HSBC recorded (reported Oct 2026) alongside the company's 125+ enterprise-customer figure. Mistral Large 4 open weights: the company promised release "by the end of October 2026"; the specific Oct 27 date is press-reported only — still pending at Oct 22, 2026.
- **ElevenLabs:** India is now the company's second-largest market (company, Oct 6, 2026, Bengaluru): 250+ Indian businesses, 100M ElevenAgents conversations in India in the past year; CARS24 and Razorpay deployments reported.

**Depth-standard build-out (all 52 rows)**
- Five new columns: `office_footprint`, `contact_route`, `leadership_full`, `ownership_status`, `clients`.
- Every previously blank cell replaced with a plain statement ("Not published" / "Not disclosed in sources checked"): contact email 47 rows, phone 52 rows, chief scientist 42 rows, board/advisers 35 rows, key engineers 10 rows.

**Checked with no change:** Thinking Machines Lab's reported $5–6B raise at a $40B pre-money valuation still not closed; Character.AI sale process ongoing; no new CB Insights AI 100 or Forbes AI 50 editions; no other CEO/chair-level changes found across the roster in Oct 21–22, 2026 sources.

## Deliverables of this refresh

- `ai_companies.csv` + this README, `ai_companies.html`, `ai_companies.pdf`, `ai_companies_llms.txt` (all rebuilt from the refreshed CSV).
- Library: *The World's AI Companies — LIKE Technology Guide* (PDF, 39 pp., and DOCX) in `~/workspace/your_files/`, plus refreshed `ai_companies.csv` / `ai_companies.pdf` copies.
- Staged web (not published): article page `~/workspace/likeleaders-site/articles/like-worlds-ai-companies.html` (full guide, all 52 entries, full field set) and department fragment `~/workspace/likeleaders-site/fragments/technology-ai-companies.html`. The Technology section page itself is built separately by the coordinator from fragments.

## Notable facts on the roster (October 2026)

- **xAI:** acquired by SpaceX (Feb 2026, ~$250B xAI valuation), rebranded SpaceXAI (Jul 2026).
- **Cursor (Anysphere):** SpaceX completed its $60B all-stock acquisition (merger effective Aug 14, 2026); OpenAI invoked the change-of-control clause to wind down Cursor's OpenAI model access, proposed shutoff Nov 12, 2026.
- **Cerebras:** IPO'd May 14, 2026 (Nasdaq: CBRS) — largest IPO of 2026 and largest semiconductor IPO on record.
- **Databricks:** $5B strategic round at $190B (Aug 13, 2026) — highest-valued private software company.
- **Google DeepMind:** leadership change Aug 5, 2026 — Hassabis to Chair + Alphabet Chief Scientist; Kavukcuoglu to SVP; Jeff Dean departed to found an independent PBC.
- **Cognition:** $2B Series E at $48B (Sep 8, 2026).
- **ElevenLabs:** $300M employee tender at $22B (Sep 30, 2026).
- **Sierra:** $950M Series E at $15.8B (May 2026).
- **Harvey:** $550M at $15.5B (Sep 2026); first in-house model post-trained on Moonshot Kimi K3 open weights.
- **Mistral AI:** €3B Series D at >€21B (Sep 8, 2026).
- **Scale AI:** new CEO Francis deSouza effective Aug 10, 2026.
- **Groq:** Nvidia ~$20B non-exclusive LPU license + hire of founder/CEO Jonathan Ross (Dec 2025); DOJ antitrust investigation opened Sep 2026.
- **Together AI:** $800M Series C at $8.3B (Jul 1, 2026); $240M multi-year IBM deal (Aug 2026).
- **Thinking Machines Lab:** open-weight Inkling (975B params) released Jul 15, 2026; in talks Sep 2026 for $5–6B at $40B pre-money (not closed).
- **MiniMax:** listed on HKEX Jan 9, 2026. **Zhipu AI (Z.ai):** listed on HKEX Jan 8, 2026.

## Known limitations

- Funding and valuation figures move fast; all are labeled with dates — treat as point-in-time.
- Chinese labs (DeepSeek, MiniMax, Moonshot, Zhipu) have thinner English-language disclosure; figures rely more heavily on press reporting, labeled as such.
- Contact columns are structurally sparse for this industry (5 published emails, 0 published phone numbers across 52 companies) — this reflects reality, not incomplete research.
- Office footprints and client lists are given only where a company or reputable reporting publishes them; otherwise the entry says so plainly.

## Prior changelogs

The full 2026-10-20, 2026-10-13 and 2026-10-06 weekly-update changelogs are preserved in git-style in `work/` (pre-refresh CSV snapshot: `work/ai_companies_pre_refresh_2026-10-22.csv`; refresh and build scripts: `work/refresh_2026-10-22.py`, `work/build_deliverables_2026-10-22.py`).
