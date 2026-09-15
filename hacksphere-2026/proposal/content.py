# -*- coding: utf-8 -*-
"""
TANDATANI — HACKSPHERE 2026 Phase 1 proposal content (Team ROOT ACCESS).
Rendered into the official template by fill_docx.py. All facts cited; see REFS.
"""
from fill_docx import (P, SUBHEAD, BULLETS, TABLE, IMG, CAPTION, SPACER,
                       PAGEBREAK, STATBAND, CALLOUT, REFERENCES_BLOCK, REFS,
                       DXA_BODY)
import os
SCRATCH = os.path.dirname(os.path.abspath(__file__))

OUT_NAME = "ROOT ACCESS-TANDATANI-INTL"

# =============================================================== references
REFS.define("eudr",       "Regulation (EU) 2023/1115 on deforestation-free products (EUDR) — EUR-Lex", "https://eur-lex.europa.eu/eli/reg/2023/1115/oj")
REFS.define("eudr_delay", "European Commission, Access2Markets: “Delay until December 2026 … implementation of the EUDR” (amended by Regulation (EU) 2025/2650)", "https://trade.ec.europa.eu/access-to-markets/en/news/delay-until-december-2026-and-other-developments-implementation-eudr-regulation")
REFS.define("benchmark",  "Preferred by Nature: “European Commission publishes first list of Country Benchmarks under the EUDR” (May 2025) — Indonesia: standard risk", "https://www.preferredbynature.org/news/european-commission-publishes-first-list-country-benchmarks-under-eu-deforestation-regulation")
REFS.define("traces",     "European Commission / EUDR geolocation rules — GeoJSON specification for TRACES (point ≤ 4 ha, polygon > 4 ha, WGS-84, 6-decimal precision)", "https://green-business.ec.europa.eu/deforestation-regulation-implementation_en")
REFS.define("cips",       "Fauzi (CIPS) & Mugume, Southern Voice: “Potential Impacts of EU Deforestation Regulation on Smallholder Coffee Farmers: Evidence from Indonesia and Uganda” (May 2025)", "http://southernvoice.org/wp-content/uploads/2025/05/Smallholders-Farm-EUDRC-Article-YTT-GSP-Fauzi-Mugume-2025.pdf")
REFS.define("fftc",       "FFTC Agricultural Policy Platform (Ditjenbun 2022 data): 1,250,452 ha; 1,634,914 coffee households; 98.14% smallholder area", "https://ap.fftc.org.tw/article/3465")
REFS.define("usda",       "USDA FAS GAIN, Coffee Annual — Jakarta ID2026-0021 (May 2026): 98% smallholder area; EU-bound shipments +72% to 2.4M bags on EUDR preparedness", "https://www.fas.usda.gov/data/gain-report/2026/05/Coffee%20Annual_Jakarta_Indonesia_ID2026-0021.pdf")
REFS.define("bps_coffee", "Indonesia Investments (BPS data): coffee production 813,345 t (2024); world No. 4 producer", "https://www.indonesia-investments.com/business/commodities/coffee/item186")
REFS.define("estdb",      "S. Afra (Satya Bumi), The Jakarta Post: “Addressing gaps in Indonesia’s national commodity dashboard and EUDR” (Sept 2024) — e-STDB coverage: palm 1.07%, rubber 0.03%, coffee 0.03%, cocoa 0.00%", "https://www.thejakartapost.com/opinion/2024/09/03/addressing-gaps-in-indonesias-national-commodity-dashboard-and-eudr.html")
REFS.define("terpercaya", "EFI Terpercaya brief: “Smallholder registration (STDB) — challenges and strategies for acceleration” (2023) — 15,054 e-STDB issued vs ≈2.4M oil-palm households", "https://jaresourcehub.org/publications/smallholder-registration-std-b-challenges-and-strategies-for-acceleration/")
REFS.define("koltiva_gap","KOLTIVA / AgNavigator: “Only 1% certified: tackling barriers to EUDR compliance for Indonesian smallholders” (Aug 2025)", "https://www.agnavigator.com/Article/2025/08/11/tackling-barriers-to-eudr-compliance-for-indonesian-smallholders/")
REFS.define("gapki_ispo", "GAPKI: “RI’s Palm Oil Becoming More Sustainable Through ISPO” (Oct 2025) — independent smallholders: 81 ISPO certificates since 2011", "https://gapki.id/en/news/2025/10/28/ris-palm-oil-becoming-more-sustainable-through-ispo/")
REFS.define("palm_share", "Databoks/Katadata: smallholder palm plantations = 40.6% of Indonesia’s total", "https://databoks.katadata.co.id/en/agroindustry/statistics/5327e23d2c4834f/smallholder-palm-oil-plantations-account-for-406-of-indonesias-total-palm-oil-plantations")
REFS.define("cocoa",      "Indonesia Investments: Cocoa — 99.8% smallholder production; 617,112 t (2024)", "https://www.indonesia-investments.com/business/commodities/cocoa/item241")
REFS.define("rubber",     "Statista / FAO: Indonesian rubber — ≈85% of planted area, ≈91% of production from ≈2.1M smallholder households", "https://www.statista.com/statistics/1241006/indonesia-rubber-planted-area-by-type-of-ownership/")
REFS.define("pwc7b",      "PwC Indonesia (CMEA estimate): EUDR can affect up to US$7B of Indonesian exports (CPO-to-EU ≈US$3.5B/yr, rubber ≈US$1B, furniture ≈US$0.6B)", "https://www.pwc.com/id/en/pwc-publications/industries-publications/consumer-and-industrial-products-and-services/plantation-highlights/july-2023/eu-deforestation-free-regulation-can-hinder-indonesias-exports.html")
REFS.define("havas",      "Mongabay: “Indonesia raises concerns over EU deforestation law’s impact on smallholders” (Apr 2025) — Deputy FM Arief Havas Oegroseno", "https://news.mongabay.com/2025/04/indonesia-raises-concerns-over-eu-deforestation-laws-impact-on-smallholders/")
REFS.define("bps_census", "ANTARA (BPS Agricultural Census 2023): 28.19M farmers; 46.84% use modern/digital technology", "https://www.antaranews.com/berita/3854265/bps-4684-persen-petani-pakai-alsintan-modern-dan-teknologi-digital")
REFS.define("rspo_cost",  "Hidayat et al., IFAMR 21(6): RSPO certification of independent smallholders — €86/ha upfront; −8% net income in year 1; IOP ERL (2024): €191–751 per farmer", "https://iopscience.iop.org/article/10.1088/1748-9326/ad8367")
REFS.define("premium",    "Việt Nam News: EUDR-compliant robusta commands ≈ +US$50/tonne; only 35–40% of Vietnam’s coffee area compliant (2026)", "https://vietnamnews.vn/economy/1797956/deep-processing-eu-deforestation-regulation-compliance-to-drive-viet-nam-coffee-exports-in-h2.html")
REFS.define("mongabay25", "Thomsen & Nepstad, Mongabay commentary (Feb 2026): EUDR physical segregation adds up to +25% transport/storage; two-tier market dynamics", "https://news.mongabay.com/2026/02/the-cost-of-compliance-with-the-eudr-will-limit-its-impact-on-reducing-deforestation-commentary/")
REFS.define("parak",      "Nofialdi (Andalas Univ.), ANTARA Sumbar: “Kopi Parak dan Koordinat Yang Hilang” (Aug 2026) — West Sumatran parak agroforestry coffee: “no polygons, not recorded in any database”", "https://sumbar.antaranews.com/berita/776192/kopi-parak-dan-koordinat-yang-hilang")
REFS.define("gayolues",   "Gemarnews: Koperasi Kopi Gayo Lues Bersinar verifying and mapping every member plot by hand for EU rules (Aug 2026)", "https://www.gemarnews.com/2026/08/ekspor-ke-uni-eropa-makin-ketat.html")
REFS.define("ketiara",    "Atlas Coffee Importers: Kopepi Ketiara — women-led Gayo cooperative, 2,000+ members; Fairtrade geolocation deadline Jan 2027", "https://www.atlascoffee.com/coffees/ketiara-cooperative/")
REFS.define("fairtrade",  "Fairtrade International: geolocation-data deadline for certified co-ops extended to January 2027", "https://www.fairtrade.net/en/fairtrade-extends-timeline-for-cooperatives-to-complete-geolocation-data-collection.html")
REFS.define("dashboard",  "Mongabay: Indonesia’s National Dashboard of Sustainable Commodities (CMEA-led, blockchain-based) as verification & integration layer (Apr 2025)", "https://news.mongabay.com/2025/04/indonesia-strengthens-forest-monitoring-with-new-tool-to-meet-eu-deforestation-law/")
REFS.define("tempo_stdb", "Tempo English: Ditjenbun opens e-STDB mapping/data collection to third parties to accelerate issuance (Aug 2026)", "https://en.tempo.co/read/2116908/how-indonesian-coffee-farmers-and-exporters-face-eudr-rules")
REFS.define("cepa",       "Euronews: EU and Indonesia conclude CEPA free-trade agreement (Sept 23, 2025); EU–Indonesia trade €28.9B (2025)", "https://www.euronews.com/business/2025/09/23/european-commission-concludes-free-trade-deal-with-indonesia")
REFS.define("consult",    "TracePlot: “EUDR compliance costs for SMEs” — consultants €800–1,500/day; enterprise platforms €10k–50k+/yr plus €5k–90k setup; SME first year ≈ €4–5k", "https://www.traceplot.com/blog/eudr-compliance-costs-sme")
REFS.define("mkt",        "Future Market Insights: EUDR commodity due-diligence software market ≈ US$1.1B (2026) → US$1.8B (2036)", "https://www.futuremarketinsights.com/reports/eudr-commodity-due-diligence-software-market")
REFS.define("koltiva",    "Koltiva — KoltiTrace EUDR suite (enterprise agritech, 1.9M producers registered)", "https://www.koltiva.com/")
REFS.define("dimitra",    "Dimitra × PT Surveyor Indonesia: blockchain + satellite EUDR services, fees tied to the DMTR token (2025–26)", "https://blockchain.news/flashnews/dimitra-dmtr-and-surveyor-indonesia-aim-to-onboard-3m-farmers-for-eudr-compliance-using-blockchain-and-satellite-tech")
REFS.define("fairfood",   "Fairfood “Trace” — open-source, Hedera-anchored transparency platform (premium storytelling focus)", "https://fairfood.org/solutions-for-a-fair-supply-chain/blockchain-tool-trace/")
REFS.define("whisp",      "FAO / Forest Data Partnership: Whisp (“what is in that plot”) — free, open-source convergence-of-evidence deforestation-risk API", "https://www.fao.org/in-action/forest-data-partnership/news-and-events/news/news-detail/supporting-eudr-compliance-with-whisp/en")
REFS.define("gfw",        "Global Forest Watch (Global Nature Watch) Data API — free key; GLAD/RADD alerts, JRC Global Forest Cover 2020", "https://data-api.globalforestwatch.org/")
REFS.define("vc20",       "W3C Verifiable Credentials Data Model 2.0 — W3C Recommendation, 15 May 2025", "https://www.w3.org/TR/vc-data-model-2.0/")
REFS.define("polygon_gas","Polygonscan gas tracker: a 32-byte root anchor ≈ 45k gas ≈ US$0.001 — batches of thousands of plots per anchor", "https://polygonscan.com/gastracker")
REFS.define("gps",        "GPS.gov: smartphone GPS accuracy ≤ 4.9 m under open sky", "https://www.gps.gov/systems/gps/performance/accuracy/")
REFS.define("gemini",     "Google AI for Developers: Gemini API free tier — 2.5 Flash 250 req/day, Flash-Lite 1,000 req/day; Indonesian officially supported", "https://ai.google.dev/gemini-api/docs/pricing")
REFS.define("supabase",   "Supabase free plan: 500 MB Postgres (PostGIS available), Auth, 1 GB storage", "https://supabase.com/pricing")

IND = 720

def NUMLIST(items, start=1, size=21, indent=1080):
    out = []
    for i, it in enumerate(items, start):
        out.append(P(f"**{i}.**  {it}", size=size, indent=indent, after=46))
    return "".join(out)

# ====================================================== 1 EXECUTIVE SUMMARY
SEC1 = [
    P("**TANDATANI** (from Bahasa Indonesia *tanda* “mark” + *tani* “farmer” — an echo of *tanda "
      "tangan*, a signature) gives every smallholder plot a **cryptographically verifiable Plot "
      "Passport that the farmer owns**, so Indonesia’s 1.6 million coffee-farming "
      "families{r:fftc} — and after them the palm, cocoa and rubber smallholders behind up to "
      "**US$7 billion** of exports{r:pwc7b} — are not locked out of Europe when the EU "
      "Deforestation Regulation takes effect on **30 December 2026**.{r:eudr,eudr_delay} The "
      "registration that doubles as a farmer’s geolocation record, e-STDB, covers just **0.03% "
      "of coffee farmers** today;{r:estdb} TandaTani closes that gap at the price of a WhatsApp "
      "message.", after=110),
    P("A cooperative officer maps a plot in minutes on a **Bahasa-first, offline-capable app**; "
      "an **AI engine** cross-examines it against official satellite forest data (FAO Whisp, "
      "JRC-2020 baseline, GLAD/RADD alerts){r:whisp,gfw} and explains its verdict in plain "
      "Bahasa; the cooperative then signs a **W3C Verifiable Credential**{r:vc20} the farmer "
      "keeps and can carry to *any* buyer, its evidence hash **anchored on the Polygon public "
      "chain** (≈ $0.001 per thousand plots{r:polygon_gas}). Exporters click once for an "
      "**EU-ready due-diligence dossier** (TRACES GeoJSON){r:traces} — and **anyone, including "
      "the judges reading this, can scan a QR and verify the entire chain of proof with no "
      "account, no permission, and no trust in us.**", after=110),
    P("Farmers pay nothing; exporters pay per shipment — less than 6% of a single consultant-day at today’s "
      "€800–1,500 rates{r:consult} — for compliance that carries a documented "
      "**+US$50/tonne premium** (Vietnamese-robusta benchmark).{r:premium} Hybrid Web2 + Web3 + "
      "AI, every component free-tier, and every feature scoped to run **live, end-to-end, "
      "within the 24-hour final**.", after=160),
]

# ====================================================== 2 PROBLEM STATEMENT
SEC2 = [
    P("**The problem in one sentence:** from 30 December 2026, every kilogram of coffee, palm "
      "oil, cocoa or rubber entering the EU must carry plot-level geolocation proof that it grew "
      "on land that was not deforested after 2020 — and the Indonesian smallholders who grow "
      "almost all of it have effectively none of the required records.", after=100),

    SUBHEAD("2.1  A regulatory wall, eleven weeks after this hackathon’s final"),
    P("Regulation (EU) 2023/1115 (EUDR) obliges any operator placing seven commodities on the EU "
      "market to file a due-diligence statement containing the **geolocation of every plot of "
      "origin** — a GPS point for plots up to 4 ha, a full polygon above that — plus evidence of "
      "**no deforestation after 31 Dec 2020** and of **legality** under Indonesian "
      "law.{r:eudr,traces} After two postponements, enforcement begins **30 December 2026** for "
      "large and medium operators (30 June 2027 for micro/small);{r:eudr_delay} the runway has "
      "been consumed, and the simplifications that came with the delay did not remove the "
      "plot-level data requirement. Non-compliance risks fines whose ceiling is no lower than **4% of a company’s EU-wide "
      "turnover**, plus confiscation and exclusion from public procurement.{r:eudr} Indonesia is "
      "benchmarked **“standard risk”** — 3% of operators face ex-post audits, but a valid DDS "
      "reference is a customs precondition for *every* shipment, and buyers facing the fines "
      "push the data burden upstream regardless.{r:benchmark}", after=100),

    SUBHEAD("2.2  The people on the wrong side of the wall"),
    STATBAND([
        ("99.3%", "of Indonesian coffee production comes from smallholders on 0.5–2 ha plots{r:cips,fftc}"),
        ("0.03%", "of coffee farmers hold e-STDB — the registration that doubles as their geolocation record (MoA, 2024){r:estdb}"),
        ("US$7 B", "of Indonesian exports exposed to EUDR requirements (CMEA estimate){r:pwc7b}"),
    ]),
    P("Indonesia is the world’s 4th-largest coffee producer (813,345 t in 2024){r:bps_coffee}, "
      "and its coffee is a smallholder crop to a degree few realize: **1.63 million farming "
      "households** work 98.1% of the coffee area.{r:fftc} The pattern repeats across the EUDR "
      "basket: smallholders hold **40.6% of the 16.8 M ha of oil palm** (≈2.4 M "
      "households),{r:palm_share,terpercaya} grow **99.8% of cocoa**{r:cocoa} and **≈91% of "
      "natural rubber**.{r:rubber} Yet the state instrument that would prove their plots’ "
      "location and legality — the e-STDB cultivation registration — has reached **1.07% of palm "
      "farmers, 0.03% of rubber and coffee farmers, and 0.00% of cocoa farmers** (Ministry of "
      "Agriculture data, July 2024 — the latest published breakdown).{r:estdb} By December 2023 exactly **15,054** e-STDB certificates "
      "existed against ≈2.4 million oil-palm households alone.{r:terpercaya} Koltiva — the "
      "largest traceability provider in the country — itself estimates that **only ≈1% of "
      "Indonesian smallholders meet EUDR traceability and legality requirements**.{r:koltiva_gap}", after=100),

    CALLOUT("In Pasaman, West Sumatra, Minangkabau families grow coffee inside ancestral *parak* "
            "agroforests — shade trees, areca, sugar-palm and coffee layered “like a tidied "
            "forest.” It is the most forest-friendly coffee agriculture imaginable. But the plots "
            "“have no polygons and are not recorded in any database” — so, come 30 December, *the "
            "most forest-friendly coffee has the highest chance of being refused at Europe’s "
            "door.*{r:parak} Meanwhile in Gayo Lues, cooperative staff are walking member plots "
            "one by one, mapping by hand against protected-area boundaries.{r:gayolues}",
            title="Field reality, August 2026"),

    SUBHEAD("2.3  Why the gap persists — it is not a mapping problem"),
    P("A GPS point takes thirty seconds to capture. The real bottlenecks, documented across "
      "government and field studies, are structural:", after=60),
    BULLETS([
        "**Cost asymmetry.** Traditional certification routes cost **€86/ha upfront and €191–751 "
        "per farmer**, and can push a smallholder’s first-year net income **negative "
        "(−8%)**{r:rspo_cost} — against typical plots of under 2 ha. Consultants bill "
        "**€800–1,500/day**.{r:consult} These unit economics can never reach a 1-hectare farm.",
        "**Institutional throughput.** e-STDB issuance runs through district offices with limited "
        "capacity; the Agriculture Ministry has now opened data collection to third parties "
        "precisely because the state cannot map millions of plots alone.{r:tempo_stdb}",
        "**A trust and custody gap.** Records collected by enterprise platforms belong to the "
        "paying client, not the farmer; Deputy Foreign Minister Havas Oegroseno put the farmer’s "
        "side bluntly — asked whether smallholders can perform EUDR’s screening duties: **“Can "
        "farmers do it? Of course not.”**{r:havas}",
        "**The digital divide is real but navigable.** Only **46.8%** of Indonesia’s 28.2 M "
        "farmers use modern machinery or digital technology;{r:bps_census} any workable solution must run "
        "offline, in Bahasa, on cheap Android phones — or through a literate cooperative officer.",
        "**Chain-of-custody fraud.** Collection points mix compliant and non-compliant lots; "
        "without tamper-evident records, one launderer can contaminate — legally and reputationally "
        "— an entire container.{r:mongabay25}",
    ]),

    SUBHEAD("2.4  The cost of doing nothing"),
    P("The market is already pricing the wall in. EU-bound Indonesian coffee shipments jumped "
      "**+72% to 2.4 million bags** in 2025/26 as buyers front-load stock ahead of "
      "enforcement{r:usda} — stockpiling, not confidence. Compliant robusta already earns a "
      "**+US$50/tonne premium** in Vietnam, where 35–40% of area is EUDR-ready; non-compliant "
      "beans are not discounted into Europe — they are **excluded**, because mixing contaminates "
      "the lot.{r:premium,mongabay25} Physical segregation adds up to **+25%** logistics "
      "cost.{r:mongabay25} At stake for Indonesia: up to **US$7 B of exports** by the "
      "government’s own estimate,{r:pwc7b} at the very moment the newly concluded EU–Indonesia "
      "CEPA (Sept 2025) finally opens the €28.9 B trade corridor wider.{r:cepa} The door to "
      "Europe is being unlocked and walled up in the same year — and whether a farming family "
      "stays inside is decided by data they do not have.", after=80),
    P("**Synthesis.** Indonesia does not have a deforestation-evidence problem so much as a "
      "**proof-distribution** problem: the forests were standing in 2020, the satellites saw "
      "them, the farmers were there — but no instrument turns that truth into a portable, "
      "trusted, affordable record in a smallholder’s hand. That is precisely an infrastructure "
      "gap — and infrastructure is what we build.", after=100),
]

# ==================================== 3 PROPOSED SOLUTION & VALUE PROPOSITION
SEC3 = [
    P("Indonesia’s harvest is real, the land is clean, but the evidence lives in paper folders, "
      "WhatsApp photos and enterprise databases the farmer will never control. TandaTani’s "
      "answer: give the proof itself to the person who created it. Every ingredient we use "
      "exists; the **combination** — a compliance credential the *farmer* owns, priced *per "
      "shipment*, verifiable by *anyone* without an account — exists nowhere in production, and "
      "§3.5 shows why incumbents cannot copy it without breaking their own business model.", after=100),

    SUBHEAD("3.1  The core concept — a Plot Passport, owned by the farmer"),
    P("For every plot we assemble one **evidence bundle**: geolocation (a GPS point for plots "
      "≤ 4 ha, a walked polygon above — exactly the EU specification{r:traces}), the satellite "
      "deforestation verdict, legality documents, geotagged field photos and the review trail. "
      "After human review, the cooperative signs this bundle as a **W3C Verifiable Credential "
      "2.0**{r:vc20} — the *Plot Passport*. Three properties make it more than a database row:", after=60),
    BULLETS([
        "**Portable.** The passport downloads as a self-contained signed file — the credential, "
        "its evidence hashes and its Merkle proof, plus a printable QR card — **held by the "
        "farmer** on their own device, with cooperative custody as the fallback, never locked "
        "in our database. Verifying it needs only that file and the public chain: if the "
        "farmer changes buyer or platform, or if TandaTani itself disappears, the proof still "
        "verifies. None of the major incumbents offers this; their records live in the paying "
        "client’s silo.{r:koltiva}",
        "**Independently verifiable.** Each bundle’s SHA-256 hash is batched into a Merkle tree "
        "whose root is anchored on the Polygon public chain.{r:polygon_gas} Any importer or "
        "auditor can re-compute the hash in a browser and confirm the record existed, unaltered, "
        "at issuance — without asking us, or trusting us.",
        "**Private by design.** The chain carries only salted hashes — never coordinates, never "
        "names. Geolocation is disclosed solely inside the exporter’s due-diligence submission, "
        "as the regulation requires.{r:eudr}",
    ]),

    P("**Scope honesty — the legality pillar.** EUDR demands two proofs: deforestation-free "
      "*and* legal production. TandaTani verifies the first from satellites; for the second it "
      "structures and hash-seals the farmer’s legality evidence (e-STDB, land letters, "
      "cooperative membership), checks it for presence and internal consistency, and records "
      "who attested it — while authenticity verification remains with the issuing authorities. "
      "The dossier is evidence the exporter files under its own due-diligence responsibility; "
      "we do not replace that duty — we make it affordable to discharge.", after=120),
    SUBHEAD("3.2  How it works — one journey"),
    P("Ibu Sari, a field officer of a Gayo cooperative, visits member farms with a mid-range "
      "Android. At Pak Karim’s plot she opens **Ladang**, our farmer app: one tap for the GPS "
      "point, two photos, a harvest estimate — all offline; it syncs at the next signal. "
      "Overnight, the **AI engine** interrogates FAO Whisp and Global Forest Watch: was this "
      "forest on 31 Dec 2020? Any loss alerts since?{r:whisp,gfw} PostGIS checks no other member "
      "has claimed an overlapping polygon. The verdict returns in Bahasa: *“Lahan ini aman — "
      "tidak ada deforestasi terdeteksi setelah 2020,”* with every evidence layer attached. The "
      "cooperative chair reviews her queue, taps **Terbitkan** (“issue”), and the cooperative’s "
      "key signs Pak Karim’s Plot Passport. When an exporter builds its next container for "
      "Hamburg, it selects verified passports and TandaTani emits the TRACES-format GeoJSON "
      "dossier{r:traces} plus a QR-coded evidence certificate. The importer scans the QR: hash "
      "matches, signature valid, root on-chain — due diligence the importer can re-verify, "
      "byte for byte, five years from now.", after=100),

    SUBHEAD("3.3  Why Web3 — an honest answer, not a buzzword"),
    BULLETS([
        "**The trust gap is structural.** An EU importer must rely on evidence from a smallholder "
        "they will never meet, passed through 3–5 intermediaries — some of whom profit from "
        "laundering non-compliant volume into compliant lots.{r:mongabay25} A vendor’s private "
        "database asks the importer to trust the vendor and every editor; a public anchor makes "
        "tampering *detectable by anyone* — a signature proves *who* wrote a record, the "
        "anchor proves *when*, so no issuer can quietly backdate a passport after a "
        "deforestation alert lands.",
        "**Records must outlive companies.** EUDR requires operators to keep due-diligence "
        "records for **five years**.{r:eudr} Startups die; anchored hashes on a public chain do "
        "not.",
        "**Portability breaks lock-in.** Verifiable Credentials give farmers *exit rights* over "
        "their own compliance history — the structural opposite of enterprise traceability, and "
        "the reason a farmer-first platform can win cooperatives’ participation.",
        "**Decentralized authentication where it belongs.** Exporters sign in with their wallets "
        "(SIWE); cooperatives hold signing keys (DIDs); farmers never touch crypto — a relayer "
        "pays the sub-cent gas. Web3 machinery, zero Web3 friction.",
    ]),

    SUBHEAD("3.4  Why AI — verification at a price a smallholder can afford"),
    P("Manual verification costs €800–1,500 per consultant-day;{r:consult} corporate mapping "
      "programs have burned millions. TandaTani’s engine performs the equivalent "
      "convergence-of-evidence analysis in seconds for ≈ **$0.002 per plot**: deterministic "
      "geospatial scoring over official datasets (JRC forest baseline 2020, GLAD/RADD alerts, "
      "commodity maps via Whisp, with Global Forest Watch as an independent backup "
      "track){r:whisp,gfw} plus PostGIS geometry-anomaly detection against duplicate or "
      "overlapping claims — then **Gemini** (official Bahasa support{r:gemini}) renders the "
      "verdict as three plain sentences a farmer can act on, and powers **Tanya Tani**, a "
      "field-question copilot. The design principle is auditable honesty: **AI narrates; "
      "evidence decides.** Every verdict links its raw sources.", after=100),

    SUBHEAD("3.5  The landscape — and the wedge it leaves open"),
    TABLE(
        [
            ["Today’s options", "Who pays, roughly", "The gap TandaTani exploits"],
            ["Enterprise traceability — Koltiva, osapiens, Sourcemap, Agridence{r:koltiva}",
             "Exporters/brands: €10k–50k+/yr + €5k–90k setup{r:consult}",
             "Top-down; the farmer is a data row; records sit in the client’s silo"],
            ["Web3 agri-platforms — Dimitra × PT Surveyor Indonesia{r:dimitra}",
             "Enterprise deals; fees tied to the DMTR token",
             "Token volatility as a compliance dependency; credentials not farmer-owned"],
            ["NGO transparency — Fairfood Trace (Hedera){r:fairfood}",
             "Donor-funded pilots",
             "Premium storytelling, not EUDR dossier automation; no AI verification"],
            ["Consultants & certifiers{r:consult,rspo_cost}",
             "€800–1,500/day; €191–751 per certified farmer",
             "Unit economics that can never reach a 2-ha farm"],
            ["Free public tools — Whisp, GFW, TRACES, Fairtrade Plot Insights{r:whisp,fairtrade}",
             "Free",
             "Analysis and filing exist — identity, attestations, volume-bounded dossiers, offline Bahasa capture and portable credentials do not"],
        ],
        [2760, 2500, 3049], size=18,
    ),
    P("**Unique selling proposition.** TandaTani is the only design in this landscape where the "
      "*farmer* ends up owning a portable, publicly verifiable compliance credential — free — "
      "while the exporter pays per shipment instead of per year. Incumbents cannot copy this "
      "without dismantling their enterprise pricing and data custody; that structural conflict, "
      "not secrecy, is our moat. And we are deliberately **complementary to the state**: "
      "Indonesia’s blockchain-based National Dashboard and the e-STDB drive need exactly the "
      "verified, plot-level smallholder data we produce — the Agriculture Ministry now invites "
      "third parties to collect it.{r:dashboard,tempo_stdb} TandaTani is the missing last mile "
      "between a farmer’s field and every rail built above it.", after=100),
]

# ========================================= 4 MVP & KEY FEATURES (24-HOUR)
SEC4 = [
    P("Everything below will be **built and running end-to-end during the 24-hour final** — live "
      "backend, live satellite queries, live chain writes, on a public URL. Nothing hardcoded, "
      "nothing mocked. Scope discipline is the strategy: five features, each independently "
      "demoable, composing one continuous story.", after=100),

    SUBHEAD("Feature 1 — Ladang: offline-first plot capture (Bahasa)"),
    P("A PWA for low-end Android. One-tap GPS point for plots ≤ 4 ha (per the EU geolocation "
      "spec;{r:traces} smartphone GPS reaches ≤ 4.9 m in open sky{r:gps}, and under shade "
      "canopy Ladang shows live accuracy, accepting a point only below a 10 m threshold with "
      "tap-on-imagery fallback) or walk-the-boundary polygon capture above 4 ha, over Esri satellite imagery (MapLibre GL). "
      "Farmer profile, plot photos, harvest estimate. Captures queue in IndexedDB and sync when "
      "signal returns — demonstrated live in airplane mode.", after=80),

    SUBHEAD("Feature 2 — AI verification engine"),
    P("On sync, the backend submits each geometry to **FAO Whisp**{r:whisp} (convergence of "
      "evidence across JRC forest-cover 2020, tropical-moist-forest, GLAD-L/S2 and RADD alerts, "
      "ESA WorldCover, commodity maps) with the **Global Forest Watch API** as an independent "
      "second track.{r:gfw} PostGIS runs ST_Intersects duplicate/overlap detection against every "
      "existing plot. Results fuse into a deterministic risk score; **Gemini 2.5 Flash**{r:gemini} "
      "renders the verdict as three plain-Bahasa sentences with evidence links. The demo shows a "
      "clean plot passing and a test polygon drawn over post-2020 forest loss failing — live.", after=80),

    SUBHEAD("Feature 3 — Plot Passport issuance (Cooperative Console)"),
    P("A review queue for the cooperative: map, AI verdict, photos and anomaly flags side by "
      "side; approve or reject in one tap. On approval the platform issues a **W3C Verifiable "
      "Credential 2.0**, Ed25519-signed by the cooperative’s did:key.{r:vc20} The passport — with "
      "its QR — appears instantly in the farmer’s app.", after=80),

    SUBHEAD("Feature 4 — Public anchoring & one-scan verification"),
    P("Evidence hashes batch into a Merkle tree; the root is anchored by **TandaRegistry.sol** on "
      "Polygon (Amoy testnet in the demo; the identical call costs ≈ $0.001 on "
      "mainnet{r:polygon_gas}). The public verify page re-computes the bundle hash in-browser and "
      "checks the VC signature plus the Merkle proof against the on-chain root — no login, no API "
      "key, no trust in TandaTani. **Judges can scan the QR from their own phones during the "
      "pitch.**", after=80),

    SUBHEAD("Feature 5 — Exporter DDS Studio"),
    P("Wallet sign-in (SIWE); pick verified passports into a batch; export a due-diligence "
      "dossier — **TRACES-conformant GeoJSON** (WGS-84, six-decimal precision, point-or-polygon "
      "by plot size{r:traces}) plus a QR-stamped evidence-summary PDF. A **volume-plausibility "
      "gate** blocks any dossier whose tonnage exceeds the summed harvest estimates of its "
      "passports — the launderer’s math stops working — and an append-only audit log shows "
      "every state change behind it.", after=100),

    SUBHEAD("The 24-hour execution plan (3 builders × 24 h)"),
    TABLE(
        [
            ["Window (WIB)", "Builder 1 (S. Gupta) — Web3 / Infra", "Builder 2 — Frontend / PWA", "Builder 3 — Backend / AI"],
            ["10:00–14:00", "Repo/CI; Vercel + Supabase; deploy TandaRegistry.sol to Amoy", "App shell; map capture; offline queue", "Supabase schema + PostGIS; API skeleton"],
            ["14:00–19:00", "VC issuance service (did:key, Ed25519)", "Farmer flows; verification result UI", "Whisp + GFW integration; risk scorer"],
            ["19:00–00:00", "Merkle batcher + anchoring worker", "Cooperative Console", "Gemini Bahasa verdicts; Tanya Tani"],
            ["00:00–05:00", "Public verify page (hash + proof in browser)", "Exporter DDS Studio", "TRACES GeoJSON + PDF dossier generator"],
            ["05:00–08:00", ("Integration pass, all hands — seeded Gayo demo dataset, airplane-mode drill, cross-device tests", {"span": 3, "align": "left"})],
            ["08:00–10:00", ("Hardening, deploy freeze, pitch rehearsal ×3, Q&A drill", {"span": 3, "align": "left"})],
        ],
        [1400, 2280, 2340, 2289], size=17,
    ),
    P("Feasibility rests on rehearsed pieces, not hope. Every external service (Whisp, GFW, "
      "Gemini, Amoy faucet, Supabase, Vercel) is free-tier, with accounts and API keys "
      "provisioned before the clock starts. Fallbacks are pre-planned: GFW if Whisp queues "
      "slowly; Groq/Llama behind the same interface if Gemini rate-limits; a cached verification "
      "fixture exists *only* as an offline-resilience aid and would be labeled as such on screen, "
      "never presented as live output. **Cut-not-fake rule: if a feature slips, we cut it — we "
      "never simulate it.** Declared cut order if time slips: the Tanya Tani copilot goes first, "
      "the PDF dossier second (the TRACES GeoJSON remains), Exporter Studio polish third — the "
      "capture → verify → issue → publicly-verify loop (Features 1–4) is the non-negotiable "
      "demo core.", after=80),
    P("**Deliberately out of the 24-hour scope** — native mobile builds, payments, marketplace, "
      "mainnet deployment, SD-JWT selective disclosure, voice interface. They appear in §5 as "
      "roadmap and are promised nowhere as demo.", after=100),
]

# ================================== 5 TARGET MARKET & IMPACT VIABILITY
SEC5 = [
    SUBHEAD("5.1  Exactly who uses TandaTani", before=40),
    BULLETS([
        "**Primary — cooperative field officers and managers** in Indonesia’s Arabica belt: "
        "specifically the Gayo highlands (Aceh Tengah, Bener Meriah, Gayo Lues), home to "
        "Southeast Asia’s largest Arabica area, a protected Geographical Indication origin since 2010, and "
        "cooperatives like women-led **Kopepi Ketiara (2,000+ members across 19 villages)** — "
        "which face a **January 2027** Fairtrade geolocation deadline on top of "
        "EUDR.{r:ketiara,fairtrade} These are digitally literate professionals mapping member "
        "plots *by hand* today.{r:gayolues}",
        "**Primary — compliance managers at Indonesian coffee exporters** shipping green beans "
        "to Belgium and Germany (the top two EU destinations{r:usda}), who currently face "
        "consultant day-rates or enterprise SaaS to produce every due-diligence "
        "statement.{r:consult}",
        "**Secondary (year 1–2)** — cocoa and rubber cooperatives (0.00% and 0.03% e-STDB "
        "coverage{r:estdb}), then independent palm smallholder associations; **EU importers** "
        "who verify passports (free) and later pay for API access.",
        "**Validation, honestly stated:** we have not yet interviewed a customer. Between this "
        "submission and the final we will hold structured calls with Gayo cooperative officers "
        "(intro path: the WRI Sustainable Gayo Coffee network and Fairtrade producer support) "
        "to test willingness-to-pay — and we will report what we hear, including bad news, on "
        "stage.",
    ]),

    SUBHEAD("5.2  Market size, from the bottom up"),
    TABLE(
        [
            ["Scope", "Basis", "Size"],
            ["TAM — EUDR due-diligence software, global",
             "Analyst estimate, 2026 → 2036{r:mkt}", "US$1.1 B →\u00a01.8 B"],
            ["SAM — Indonesian smallholder EUDR corridor",
             "≈7.5 M smallholder households across coffee (1.63 M), palm (2.4 M), cocoa (1.4 M), "
             "rubber (2.1 M); exports at stake up to US$7 B{r:pwc7b}",
             "≈7.5 M farms · US$7 B trade"],
            ["SOM — 12-month beachhead: Gayo coffee",
             "(8,000 members × €1.40 × 2 seasons) + (200 dossiers × €45) ≈ €31k, across 3 co-ops and 2 exporters",
             "≈US$33k ARR"],
        ],
        [2280, 4300, 1729], size=18,
    ),

    SUBHEAD("5.3  Business model — commercial from day one"),
    BULLETS([
        "**Farmers: free, forever.** Their participation is the network; charging them kills it.",
        "**Exporters: Rp 800k (≈ €45) per due-diligence dossier**, or a flat coop-season "
        "license. Context: consultants run €800–1,500/day, enterprise SaaS €10k–50k/yr;{r:consult} "
        "one compliant 19-tonne container carries ≈ US$950 of premium at "
        "+US$50/tonne.{r:premium} We price at ≈5% of the value we unlock.",
        "**Cooperatives: Rp 25k (≈ €1.40) per member per season** for the credential registry "
        "and Fairtrade/e-STDB exports — less than 1% of a certification’s per-farmer "
        "cost;{r:rspo_cost} a member visit takes minutes, and one visit now serves EUDR, "
        "Fairtrade and e-STDB at once.",
        "**Later: verification API** for EU importers and (per Ditjenbun’s invitation to third "
        "parties{r:tempo_stdb}) **paid e-STDB data-collection partnerships** feeding the "
        "National Dashboard.{r:dashboard}",
    ]),
    P("**Unit economics.** Marginal cost per verified plot ≈ $0.002 LLM + anchoring amortized to ≈$0.000001 in "
      "1,000-plot batches + fractions of a cent of storage{r:polygon_gas,gemini} — under **$0.01 all-in** against "
      "€45-per-dossier revenue: software margins on infrastructure that incumbents deliver with "
      "field armies. Free tiers carry the pilot; the first paying exporter carries the "
      "company.", after=80),

    SUBHEAD("5.4  Scalability — one engine, many walls"),
    P("The pipeline — *map → verify → credential → anchor → dossier* — is commodity-agnostic and "
      "regulation-agnostic. The same engine serves cocoa, rubber and palm; the same passports "
      "satisfy Fairtrade’s 2027 geodata mandate,{r:fairtrade} feed e-STDB and the National "
      "Dashboard,{r:dashboard} and are ready for whatever follows EUDR (the UK and US have "
      "parallel bills in motion). Geographically, Vietnam alone has 60–65% of its coffee area "
      "still non-compliant;{r:premium} the architecture ports with a language file. Because "
      "passports are portable open credentials, every new buyer that accepts them makes every "
      "existing passport more valuable — adoption compounds.", after=80),

    SUBHEAD("5.5  Impact, measured"),
    BULLETS([
        "**Economic:** keeping smallholders inside a corridor worth up to US$7 B{r:pwc7b} and "
        "capturing the +US$50/t compliance premium{r:premium} at the farm gate rather than the "
        "trader’s margin.",
        "**Institutional:** every passport is e-STDB-ready data — accelerating the registration "
        "drive the government itself says it cannot staff.{r:tempo_stdb}",
        "**Environmental:** EUDR’s promise only works if compliance is achievable; TandaTani "
        "makes deforestation-free farming *provable*, so the market can reward it (SDGs 1, 8, "
        "12, 13, 15).",
        "**Social:** the first bankable, portable proof-of-practice a smallholder has ever "
        "owned — with women-led cooperatives like Ketiara{r:ketiara} as first protagonists.",
    ]),

    SUBHEAD("5.6  Risks, named — and answered"),
    TABLE(
        [
            ["Risk", "Reality check", "Mitigation built into the design"],
            ["Farmer digital literacy (46.8% modern-tech adoption{r:bps_census})",
             "Real, generational", "Cooperative-officer-assisted capture; offline PWA; Bahasa-first; voice roadmap"],
            ["EUDR slips a third time", "Possible — it slipped twice{r:eudr_delay}",
             "The 2024 delay itself triggered +72% buyer front-loading — buyers, not Brussels, now enforce;{r:usda} passports also serve Fairtrade Jan-2027, e-STDB and ISPO{r:fairtrade,tempo_stdb}"],
            ["GPS spoofing / claim fraud", "Attempted everywhere",
             "Satellite cross-check, PostGIS overlap detection, geotagged photos, cooperative attestation — convergence, not trust"],
            ["Cooperative key loss", "Operational hazard",
             "Credential-status registry + re-issuance under a successor DID (did:key is single-keypair by design; roadmap: did:web for true rotation)"],
            ["Incumbent copies the model", "Koltiva has 1.9 M producers{r:koltiva}",
             "Copying farmer-owned portability breaks their enterprise custody model — our wedge is their conflict"],
        ],
        [2620, 2140, 3549], size=17,
    ),
]

# ======================================= 6 TECH STACK & SYSTEM ARCHITECTURE
SEC6 = [
    P("One hybrid system, three planes: a **Web2 core** for speed and cost, a **Web3 trust "
      "plane** for proof and portability, an **AI plane** for verification at smallholder "
      "prices. Every component is free-tier; the whole demo runs on public URLs.", after=100),
    SUBHEAD("6.1  Data flow (the numbered steps match the chips in Figure 1, next page)"),
    NUMLIST([
        "Field capture, fully offline: GPS point/polygon, photos, farmer identity → IndexedDB queue.",
        "Sync to the API (Next.js route handlers, Zod-validated); plots land in Postgres/PostGIS,{r:supabase} where the ST_Intersects gate blocks exact-duplicate claims outright and flags partial overlaps into the risk score.",
        "AI engine gathers satellite evidence (Whisp primary; GFW independent track){r:whisp,gfw} and Gemini writes the Bahasa verdict.{r:gemini}",
        "Cooperative reviews the AI-annotated queue in its Console.",
        "Approved bundle → W3C Verifiable Credential 2.0, signed with the cooperative’s did:key (Ed25519).{r:vc20}",
        "Bundle hashes batch into a Merkle tree — thousands of plots, one 32-byte root.",
        "The root is anchored by TandaRegistry.sol on Polygon; the event is public forever.{r:polygon_gas}",
        "Exporter composes verified passports → TRACES GeoJSON + evidence-PDF dossier.{r:traces}",
        "Anyone scans the QR: the browser re-computes the hash and checks VC signature + Merkle proof against the chain.",
    ]),
    PAGEBREAK(),
    IMG(os.path.join(SCRATCH, "diagram_arch_rot.png"), width_dxa=7430, indent=800),
    CAPTION("Figure 1 — TandaTani system architecture and data flow (rotate to read). Numbered chips on the arrows match the data-flow steps in §6.1."),
    SPACER(40),

    SUBHEAD("6.2  Technology choices — and why each earns its place"),
    TABLE(
        [
            ["Layer", "Technology", "Why this, for this build"],
            ["Frontend", "Next.js 15 PWA · TypeScript · Tailwind · MapLibre GL + Esri World Imagery · Dexie (IndexedDB)",
             "One codebase, four roles; installable on low-end Android; offline by architecture, not afterthought"],
            ["Backend", "Next.js route handlers on Vercel · Supabase: Postgres + PostGIS, Auth, Storage{r:supabase}",
             "Zero-ops free tiers; geometry fraud checks are one SQL clause"],
            ["AI / EO", "FAO Whisp API · Global Forest Watch Data API · Gemini 2.5 Flash, Groq/Llama fallback{r:whisp,gfw,gemini}",
             "Official, free, EUDR-aligned convergence of evidence; Bahasa officially supported"],
            ["Web3", "Solidity (Foundry) on Polygon PoS/Amoy · viem · @digitalbazaar/vc + did:key (Ed25519) · SIWE · OpenZeppelin Merkle{r:vc20,polygon_gas}",
             "Sub-cent anchoring; W3C-standard credentials (Recommendation, May 2025); wallets only where users are companies"],
            ["Delivery", "GitHub Actions CI · Vercel previews · public demo URL + Amoy explorer links",
             "Live public deployment for the pitch — judged explicitly above localhost"],
        ],
        [1150, 3700, 3459], size=17,
    ),

    SUBHEAD("6.3  The on-chain / off-chain boundary (privacy by architecture)"),
    BULLETS([
        "**On-chain:** 32-byte Merkle roots and batch URIs — nothing else. ≈ $0.001 per thousand "
        "plots{r:polygon_gas}: the whole Gayo highlands could be anchored for the price of one "
        "cup of its own coffee.",
        "**Off-chain:** coordinates, identities, photos — Postgres under row-level security, "
        "disclosed only inside the exporter’s DDS as EUDR requires.{r:eudr} Salted hashing "
        "defeats rainbow-matching of known plots.",
        "**Keys:** cooperatives hold did:key signing keys; exporters authenticate by wallet "
        "(SIWE); a relayer pays gas so farmers never see crypto.",
        "**Privacy law, named.** Indonesia’s PDP Law (UU 27/2022) and the GDPR shape the "
        "design: consent captured at enrollment (the cooperative as data controller, TandaTani "
        "as processor), coordinates under row-level security and disclosed only inside the "
        "DDS, credential copies on the farmer’s device and printable QR card — and, because "
        "the chain holds only salted hashes, destroying a record’s salt is a clean erasure "
        "path. The public QR page shows a verdict, never coordinates or identities.",
    ]),

    SUBHEAD("6.4  Engineering honesty — failure modes we designed for"),
    BULLETS([
        "Whisp jobs are asynchronous (Earth-Engine-backed): we submit early, poll, and keep GFW "
        "as an independent evidence track — either alone yields a verdict.{r:whisp,gfw}",
        "Background Sync API is Chromium-only, so the offline queue flushes on the browser’s "
        "online event — works everywhere modern; demoed on Android Chrome.",
        "Free-tier LLM limits (Gemini: 250 requests/day{r:gemini}) comfortably exceed "
        "rehearsal-measured demo load; Groq is wired behind the same interface.",
        "If venue Wi-Fi dies mid-pitch, the offline-first design *is* the contingency: capture "
        "continues, and we sync over any hotspot.",
    ]),
]

# ===================================================================== DOC
CONTENT = {
    "cells": [
        ("[Enter Project Title]",
         "TANDATANI — A Verifiable Plot Passport for Every Smallholder", {"bold": True, "size": 26}),
        ("[Enter Team Name]", "ROOT ACCESS", {"bold": True}),
        ("[e.g., National / International (All Mem) / International (Mix)]",
         "International (All Members)", {}),
        # Leader
        ("[Enter Name]", "Shivam Gupta", {}),
        ("[e.g., High School Student / College Student]", "College Student", {}),
        ("[name@email.com]", "shivam1720406@gmail.com", {}),
        ("[e.g., Indonesia / Other Country]", "India", {}),
        ("[Enter Institution Name]", "‹leader: institution›", {}),
        # Member 1
        ("[Enter Name]", "‹Member 1: full name›", {}),
        ("[e.g., High School Student / College Student]", "College Student", {}),
        ("[name@email.com]", "‹Member 1: email›", {}),
        ("[e.g., Indonesia / Other Country]", "‹Member 1: country›", {}),
        ("[Enter Institution Name]", "‹Member 1: institution›", {}),
        # Member 2
        ("[Enter Name]", "‹Member 2: full name›", {}),
        ("[e.g., High School Student / College Student]", "College Student", {}),
        ("[name@email.com]", "‹Member 2: email›", {}),
        ("[e.g., Indonesia / Other Country]", "‹Member 2: country›", {}),
        ("[Enter Institution Name]", "‹Member 2: institution›", {}),
    ],
    "sections": [
        ("Executive Summary", SEC1),
        ("Problem Statement", SEC2),
        ("Proposed Solution", SEC3),
        ("Minimum Viable Product", SEC4),
        ("Target Market", SEC5),
        ("Tech Stack", SEC6),
    ],
    "appendix": [REFERENCES_BLOCK()],
}
