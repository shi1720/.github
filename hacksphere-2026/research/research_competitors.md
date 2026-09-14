# AKAR — Competitive Intelligence Report
**EUDR compliance platforms, free tools, Web3 landscape, naming, pricing & market size**
Prepared for the AKAR hackathon team · Research date: 14 September 2026 · All URLs accessed 2026-09-14.

**Regulatory context (for framing):** EUDR (Regulation (EU) 2023/1115) requires plot-level geolocation, deforestation-free verification against the 31 Dec 2020 cutoff, and a Due Diligence Statement (DDS) filed in TRACES NT before goods enter the EU; non-compliant product is blocked and fines reach 4% of EU turnover [50][51]. Application has been phased across 2025–2026, with the EU "simplification" package cutting projected industry-wide compliance costs ~75% (from €2.5–3.5B to €600–900M/yr) [70]. The FMI analyst report treats December 2026 as the enforcement pivot forcing adoption [76].

---

## 1. COMPETITOR PROFILES

### 1.1 Koltiva (Jakarta, Indonesia) — **the key incumbent competitor**
- **What it is:** Agritech/traceability company founded 2013, HQ South Jakarta; "beyond traceability" platform spanning agritech + fintech + climate, with paid field teams ("boots on the ground") [1][5].
- **Products:** KoltiTrace (SaaS web+mobile traceability MIS: polygon mapping, deforestation/LUC checks vs JRC & Hansen data, legality verification, automated DDS generation), KoltiSkills (extension/coaching services), Data Verification (desktop verification with high-res imagery), KoltiPay (fintech), FarmCloud producer app [2][3][7].
- **Scale claims:** >1.9M producers mapped across 65 countries, >542,000 in Indonesia; ~1.4M registered producers + business users; >8,000 business clients in 61 countries [4][1]. Series A led by AC Ventures (Sept 2023, undisclosed 7-figure), plus an oversubscribed follow-on [5].
- **Pricing:** **Not public.** Sold enterprise-style (SaaS + field services) to exporters, brands, and programs; no per-farmer/per-DDS rate card found [7][19-analogy]. Honest gap: pricing opacity is itself a finding.
- **Farmer data ownership/portability:** **No public statement found** that farmers own or can port their data; FarmCloud gives farmers *access* to their profile, but the platform is client-funded and data sits in Koltiva's system serving the paying supply-chain client [7]. No documented export of farmer credentials to competing platforms.
- **Blockchain:** No blockchain found on current KoltiTrace product pages [7].
- **Gap vs smallholders:** Top-down, B2B-funded model; farmer is data subject, not data owner; heavy service component (mapping crews) that scales with cost. Even Koltiva's own ecosystem coverage: only ~1% of Indonesian smallholders currently certified EUDR-ready (their SHINES program targets 5,000 farmers/12 months in Kutai — small vs ~millions needed) [6].

### 1.2 Dimitra (US/global, token: DMTR) — **closest Web3 competitor, active in Indonesia**
- **What it is:** "Connected Farmer" ag-platform combining AI, satellite, IoT and blockchain; ERC-20 token DMTR; Environmental Compliance Protocol live on Solana (July 2025), also operates across Polygon/Ethereum [8][11][82].
- **EUDR:** Deforestation-analysis reports for EUDR; claims first "EUDR-compliant coffee shipment" using AI+blockchain; **partnership with PT Surveyor Indonesia aiming to onboard 3M Indonesian coffee/cocoa farmers for EUDR** [9][89].
- **Pricing:** Each deforestation report is paid in DMTR (fiat converted to DMTR by treasury; 50% of revenue used for token buyback). **No public $ per-plot price found** [10].
- **Scale claims:** Operates in 60–65 countries; "18–20M farms under contract" via cooperative partnerships (2021–22 claims; verify skeptically — these are contracted co-op memberships, not active users) [12].
- **Gap:** Token-centric model (report fees ride DMTR volatility; crypto exposure is a procurement red flag for EU importers); corporate/co-op top-down onboarding; no W3C Verifiable Credential "farmer-owned passport" model found — chain use is for payments/anchoring inside Dimitra's own platform, not portable farmer identity.

### 1.3 Agridence (Singapore; ex-HeveaConnect, acquired farmer connect)
- Rubber-born (2018) digital marketplace, renamed Agridence 2022; now multi-commodity (coffee, cocoa, rubber, palm) traceability + compliance: first-mile capture, deforestation risk, EUDR DDS and PPWR filings in one platform [13].
- **Acquired farmer connect (Geneva, founded 2019) in Aug 2025** — farmer connect built blockchain-backed coffee/cocoa traceability and the consumer "Thank My Farmer" app; deal gives Agridence EU presence [14][15].
- **Pricing:** Not public. Targets importers, brands, industry schemes — enterprise sales [13].
- **Gap:** Trader/importer-first design; farmers are suppliers being onboarded, not credential owners; blockchain heritage (farmer connect) is corporate-permissioned, not public-verifiable.

### 1.4 TraceX Technologies (Bangalore, India)
- Blockchain + satellite + AI EUDR suite: polygon mapping & geometry validation vs JRC/Hansen datasets, doc parsing, risk alerts, direct TRACES DDS submission; separate products for enterprises and producers/FPOs [16][17].
- **Pricing:** Not public (free-trial funnel). Positioned notably cheaper than EU enterprise platforms; sells to agribusiness exporters and producer organizations [16].
- **Gap:** Blockchain is a private trust layer ("tamper-proof records"), not farmer-owned credentials; India-first; smallholder is onboarded under the paying exporter's tenant.

### 1.5 osapiens (Mannheim, Germany) — enterprise ESG heavyweight
- osapiens HUB for EUDR: automated due-diligence workflows, claims up to 90% risk-analysis time reduction, 900+ companies on the EUDR product, 1,300+ customers overall; $120M Series B led by Goldman Sachs (Jul 2024), ~$246M raised total [18][20].
- **Pricing:** Not public; OMR notes provider does not publish prices; PEFC members get negotiated "special rates" [19][21]. Third-party benchmark for this class: €10k–50k+/yr licenses, €5k–90k setup [68].
- **Gap:** Pure enterprise compliance software for EU operators; zero farmer-side presence, no farmer data ownership concept, no offline first-mile capture; smallholder data must arrive from someone else's system.

### 1.6 Satelligence (Utrecht, Netherlands)
- Geospatial monitoring (founded 2016): radar+optical (Sentinel-1/2, Landsat) near-real-time deforestation alerts, risk assessment, API-friendly web app; results "within 2 minutes"; flat-rate pricing model (amounts not public) [22][23].
- **Gap:** Monitoring layer only — no farmer identity, no first-mile capture, no DDS ownership by farmers; sells to corporates (e.g., rubber producer RLU) [22].

### 1.7 Orbify (Poland/UK)
- Satellite-data platform with EUDR compliance app: plot risk analysis, traceability, audit-ready outputs; "start free, scale by usage" pricing tailored by users/supplier base/orders; special deals for startups <$50k revenue, NGOs, universities [24][25].
- **Gap:** Geospatial developer platform first; no farmer-facing app, no Bahasa UX, no credential model.

### 1.8 Meridia (Netherlands/Ghana) — Meridia Verify
- Verify (launched Oct 2024, after 10 yrs field mapping): assesses field data quality, deforestation, legality, traceability for cocoa/coffee/palm/soy/rubber; specifically engineered to pass TRACES' "evolving, often undocumented" geometry checks [26][92].
- Rabo Foundation partnership subsidizes verification for 19 co-ops/traders in Africa & LatAm [27]. Pricing not public (per-plot data-verification service sold to buyers/traders).
- **Gap:** Verification-as-a-service for buyers; farmers don't hold the resulting verified asset; donor subsidy (not product economics) is the current smallholder bridge.

### 1.9 Global Traceability (Germany/UK) — RADIX Tree
- Cloud, SAP-integrated end-to-end traceability; expert analysts do risk evaluation; strong in timber (Fordaq partnership for wood industry EUDR) [28][29]. Pricing not public.
- **Gap:** ERP-adjacent enterprise tooling; nothing farmer-owned; timber/EU-operator heritage.

### 1.10 Farmforce (Oslo, Norway; spun out of Syngenta Foundation 2012→Norwegian ownership 2017)
- First-mile SaaS for smallholder sourcing: farmer database, GPS/polygon mapping, harvest & purchase records, deforestation monitoring, EUDR support [30][31]. (Note: we could not verify any "EPI" ownership link — investors listed include Edaphon, NorgesGruppen, EIT Food, Investinor, Mp Pensjon [31]; treat "EPI/farmforce" as unconfirmed.)
- **Pricing signal (third-party directory, low confidence):** flat NOK 330/yr (~$30) with implementation NOK 55,000–220,000 (~$5k–20k) [32].
- **Gap:** Sold to the agribusiness/off-taker, who owns the tenant and the data; farmers don't port records between buyers; no public verifiability.

### 1.11 Sourcemap (New York, USA)
- Enterprise supply-chain mapping since 2011; EUDR: maps every shipment to farm, satellite screening, auto-DDS to TRACES; SAP/Databricks/Salesforce integrations; ISO 27001/SOC 2; supplier outreach team in 8 languages [33][34]. Positioned "best for enterprises with complex supply chains" [35]. Pricing not public.
- **Gap:** Priced and architected for multinationals; smallholders enter as rows in a supplier campaign.

### 1.12 Fairfood (Amsterdam, NGO) — **the closest philosophical neighbor, uses blockchain**
- Trace: blockchain-based farm-to-fork traceability with farmer-visible transactions and premium verification; NFC cards for low-tech farmer interaction; **open-sourced module by module (AGPLv3 dual license) on GitHub** (Trace-Server, Connect-Mobile) [36][37][38].
- Blockchain: uses **Hedera** for tokenization/ledger; Hedera Guardian "Premium Paid Token" proves premiums reached farmers [39].
- **Business model:** nonprofit; grant-funded interventions + a "basic" SME subscription for Trace (price not published) [40]. Reference deployments: Pure Africa coffee (519 Uganda farmers), Social Vanilla, etc. [40].
- **Gap:** Living-income/premium-transparency focus, not EUDR DDS automation; no AI deforestation verification pipeline; NGO capacity limits scale; farmer sees data but the W3C-VC "portable credential owned by farmer" is not the design.

### 1.13 Others found focused on EUDR (brief)
- **Enveritas (US nonprofit):** free sustainability + EUDR verification for smallholder coffee (geospatial + field observation; jurisdictional pilots with JDE Peet's). Free for producers — but farmers receive no portable credential; roaster-funded model [41][42].
- **BanQu (US):** non-crypto blockchain traceability incl. EUDR; enterprise contracts [35].
- **iov42 / Interu (UK/Austria):** permissioned-DLT due-diligence platform (ex-Timber Chain) for EUDR/UK Environment Act/US FOREST Act — timber-centric, enterprise [43][90].
- **LiveEO, IntegrityNext, Source Intelligence, EAS Project, Coolset, TracePlot (€59/mo SME tool), Trusty (per-risk-assessment pricing, free data collection)** — EU-operator-side compliance software [51][52][68][69][35].
- **"Beluga":** **no EUDR-focused company by this name found** in multiple searches; likely a misremembered name — nothing to profile [search null result].

**Cross-cutting smallholder gap (all of the above):** every commercial player is paid by, and architected around, the exporter/importer/brand. Farmer data lives in the vendor's silo; if the co-op switches exporters (or the exporter switches vendors), the farmer's mapping and compliance history typically does not travel with them. None issues farmers a self-owned, publicly verifiable credential.

---

## 2. FREE / PUBLIC TOOLS (and what they don't solve)

### 2.1 FAO Open Foris **Whisp** — CONFIRMED, exists and is free
- "What is in that plot?" — open-source geospatial **API**: submit plot geometry (GeoJSON), get a **convergence-of-evidence** analysis across multiple public datasets (forest cover, disturbance, commodity maps) relative to the 31 Dec 2020 EUDR cutoff; outputs per-plot indicator table + risk flag (pre-2020 disturbance = low risk; post-2020 = high risk) [44][85].
- **Run by:** FAO with the Forest Data Partnership (WRI, Google, NASA, USAID et al.) and the AIM4Forests programme [44].
- **Access/cost:** free & open source — Whisp API, Whisp on Earth Map (whisp.earthmap.org), `openforis-whisp` Python package on PyPI, Open Foris Ground mobile; all code on GitHub [44][45][46]. **AKAR can legally build its AI-verification layer on Whisp — and should say so.**
### 2.2 EU Forest Observatory (JRC)
- Free global forest cover 2020 map (GFC2020, 10m, v2 improved for coffee/cocoa/rubber/palm confusion) + forest-type map (natural/primary/planted) at forobs.jrc.ec.europa.eu; explicitly **non-mandatory, non-binding** reference for EUDR [47][48][86].
### 2.3 Global Forest Watch (WRI)
- Free near-real-time deforestation alerts (integrated GLAD/RADD), 20+ yrs tree-cover-loss data, GFW Pro for supply-chain portfolios; suitable for EUDR monitoring per WRI [49][50].
### 2.4 TRACES NT (European Commission)
- The official — and free — portal where operators register and submit the DDS, returning reference numbers (EU-EUDR-XX-…); geolocation upload built in; shipments without a DDS number are blocked at customs. System reopened 30 June 2026 after technical updates [51][52][53].

### What the free stack does NOT solve (= AKAR's build space)
1. **Farmer identity & land-claim linkage** — Whisp scores a polygon; it cannot say *whose* polygon it is, or bind it to an ID/cooperative membership (Indonesia's e-STDB registration reached only **0.03% of coffee farmers** as of mid-2024 [60][61]).
2. **Credential portability** — a Whisp output is a one-off report, not a reusable, signed attestation the farmer owns and can present to any buyer.
3. **Chain of custody & mass-balance fraud** — none of these tools track bags/lots from plot to container, so compliant polygons can "launder" non-compliant volume; EUDR requires segregation, and mixing renders the whole lot non-compliant [83].
4. **Offline first-mile capture** — Whisp/GFW assume you already have clean polygons; collecting them in low-connectivity Sumatra/Sulawesi is the unsolved mile.
5. **Bahasa Indonesia UX / low-literacy design** — all are English/geospatial-expert oriented.
6. **DDS packaging workflow** — TRACES accepts filings but doesn't assemble evidence; someone must aggregate polygons+risk+legality into an exporter-ready package.

---

## 3. WEB3 ANGLE CHECK — how novel is AKAR's combination?

**Existing blockchain/VC × agri × EUDR projects found:**
- **Dimitra** — blockchain (Solana/Ethereum/Polygon) + AI for EUDR reports, token-gated economics, 3M-farmer Indonesia ambition with PT Surveyor Indonesia [9][89]. *Not* W3C VCs; farmer doesn't hold a portable credential; utility-token dependency.
- **Fairfood Trace** — Hedera-anchored open-source traceability with farmer-visible premiums/NFC cards; nonprofit; not an EUDR DDS engine, no AI verification, no farmer-held VC wallet [36][39].
- **farmer connect** (now Agridence) — blockchain coffee traceability, consumer QR ("Thank My Farmer"); enterprise-permissioned, acquired Aug 2025 [14][15].
- **BanQu, iov42/Interu** — permissioned DLT for enterprise due diligence (incl. EUDR) [35][43].
- **EMURGO (Cardano)** — announced blockchain coffee-traceability solution *for Indonesia* (enterprise pilot; no evidence of EUDR DDS output or farmer-owned VCs) [57].
- **HARA (Indonesia)** — blockchain agri-data exchange (farmer data monetization; pre-EUDR era, not compliance-focused) [58].
- **Indonesia's own National Commodity Dashboard** — the government platform is described as **blockchain-based** and tied to e-STDB smallholder registration [59][60]. AKAR should integrate/align, not compete, with this.
- **W3C Verifiable Credentials specifically:** only fringe/early artifacts found — Voice Ledger (a Chainlink-hackathon project using DID:key + VCs for EUDR-style coffee provenance) [54], academic AgriTrust framework (VCs for coffee certification) [55], and CIMMYT pilots giving farmers VC data wallets [56]. **No production platform found that issues smallholders W3C VC "plot passports" anchored on a public chain and wired into EUDR DDS generation.**

**Honest novelty verdict:** Every individual ingredient of AKAR exists — offline plot mapping (Koltiva, Farmforce), AI satellite verification (Satelligence, Whisp, Meridia), blockchain anchoring (Dimitra, Fairfood, TraceX), QR consumer verification (farmer connect), DDS automation (osapiens, Sourcemap, TraceX). **The novel combination is real but narrow: (a) farmer-owned, portable W3C Verifiable Credentials as the unit of compliance, (b) anchored on a public chain with public QR verifiability, (c) free at farmer level with per-shipment exporter monetization, (d) Bahasa-first offline capture, (e) built atop free public rails (Whisp/JRC/TRACES) instead of proprietary geospatial stacks.** Nobody found does that stack together, and incumbents are structurally disincentivized to make farmer data portable (their moat is the silo). Dimitra × Surveyor Indonesia is the direct threat to watch — same geography, same commodities, blockchain story, government-adjacent partner — but its token economics and top-down onboarding leave the farmer-ownership lane open. Expect judges to ask "why blockchain at all?": the defensible answer is *portability across buyers + public verifiability without trusting any single vendor* — precisely the two things every incumbent withholds.

---

## 4. NAME COLLISION CHECK

- **"Akar" — significant collisions in Indonesia:**
  - **AKAR Farm** — Indonesian agritech (vertical/indoor farming + agri supply-chain, since 2022, Indotech Group portfolio). Same sector, same country. **Direct collision** [62].
  - **akar.id is TAKEN** — currently a 3D design/VFX studio portfolio site [67].
  - **AKAR Indonesia** — adolescent-health NGO association (asosiasikesehatanremaja.or.id) [87]; **Akar NFYR** — Bandung sustainable-products brand [88]; AKR Corporindo (akr.co.id) — major listed logistics/chemicals firm with phonetically identical ticker-style name.
  - Verdict: "Akar" (root) is a beautiful but crowded Indonesian word-mark; agritech collision (AKAR Farm) + taken .id domain mean **rebrand or qualify** (e.g., "AkarTani", "AkarTrace", "Akar Lestari" — recheck before use).
- **"Jejak"**: **Jejakin exists** — funded Indonesian climate-tech (carbon management, $2.7M round May 2024; clients Gojek, BCA, Telkomsel) [63][64]. Any "Jejak-" name will be read as related. Avoid "Jejakin"-adjacent forms; plain "Jejak" + modifier may still be feasible but risky in the sustainability space.
- **"Saksi"**: dominated by Indonesian **election-witness apps** (Saksi Partai Perindo, SI Saksi/PDIP, Aplikasi Saksi PPP, iCount Saksi) and the Philippine GMA news program "Saksi" [65][66]. Political connotation in Indonesia — poor fit for a farmer brand.
- **Recommendation:** pick a compound/coined mark, verify PDKI (Indonesian trademark) + .id/.com availability. Candidates worth checking: *AkarTani, TandaTani, BuktiTani, Panenpasti, Terang, AkarChain*.

---

## 5. PRICING BENCHMARKS (what EUDR compliance costs today)

**Software (EU-operator side):**
- SME tools from **€59/month** (TracePlot, after €49 deposit); enterprise platforms **€10,000–50,000+/yr licenses** with **€5,000–90,000 setup** [68].
- Consultants: **€800–1,500/day**, typical small-importer engagement 2–5 days; first DDS legal review €200–400; realistic SME first-year all-in ≈ **€4,000–5,000** [68].
- Trusty prices per *risk assessment* (data collection free) rather than per DDS [69]. Farmforce directory listing: flat NOK 330/yr + NOK 55k–220k implementation (low confidence) [32]. osapiens/Koltiva/Sourcemap/Satelligence/Meridia/Agridence: **no public prices** (all quote-based enterprise sales) [19][7][33].

**Field mapping & verification (producer side):**
- Polygon mapping is cheap in marginal cost (20–30 min walk of a 2-ha farm with a smartphone; EC calls it a "one-off cost") but expensive at scale: **Barry Callebaut spent >CHF 2M just GPS-mapping cocoa farmers** [73][74]; a Peruvian cacao co-op reported **$60k–100k** total EUDR adaptation [75].
- EC estimates post-simplification total EU compliance burden **€600–900M/yr** (from €2.5–3.5B); per-company: **€450 per €1M revenue (large) vs €2,389 per €1M (SMEs)** — SMEs pay ~5x more relatively [70]. A large EU coffee company's EUDR cost: **0.03–0.07% of revenue** (ClientEarth via Mongabay) [72-mongabay].

**Certification comparators (per-farmer costs that co-ops already know):**
- RSPO independent smallholders: **€191–751 per farmer** (group-size dependent); ~€86/ha upfront; first-year net income effect can be negative (~-8%/ha) [70b][71].
- Rainforest Alliance: farmer/group pays audit (varies, not regulated); cocoa carries a mandated **$70/MT Sustainability Differential** [72].

**Market price signal for compliant beans:**
- Vietnam robusta: EUDR-compliant lots command ≈ **+$50/tonne** compliance differential; ~35–40% of Vietnam's supply is EUDR-ready; vendor-side claims of 40–60% price moves for "EUDR-ready" suppliers are marketing, treat with caution [77][78][84]. Non-compliant beans aren't "discounted" into the EU — they're **excluded** (segregation required; mixing contaminates the lot) [83]. Indonesia baseline: only ~1% of smallholders EUDR-certified-ready; e-STDB coffee uptake 0.03% — i.e., the compliant-supply scarcity premium should persist [6][61].

**Implication for AKAR pricing:** an exporter paying €50–100 per shipment DDS package + a few cents/plot for verification is 1–2 orders of magnitude below both enterprise SaaS (€10k–50k/yr) and the +$50/tonne value it unlocks; free-for-farmer is genuinely differentiated since even nonprofit Enveritas monetizes roaster-side [41][68][77].

---

## 6. MARKET SIZE (analyst estimates, 2026–2030s)

- **EUDR commodity due-diligence software (most specific):** **USD 1.1B (2026) → 1.8B (2036), 5.2% CAGR** — Future Market Insights; includes licensing + onboarding/verification/monitoring services [76].
- Supply-chain **traceability** software: **USD 5.61B (2026) → 12.4B (2035), 9.3% CAGR** (Business Research Insights) [80]; alternative: USD 10.5B (2025) → 30B (2033), 18.5% CAGR (FutureDataStats) [81]; a third house says USD 21.7B (2026) at 4.36% CAGR — definitions vary wildly, cite ranges [79-note].
- Supply-chain **visibility** software: USD 3.5B (2026) → 11.9B (2036), 13% CAGR (FMI) [80b].
- Sanity anchor: osapiens alone raised $246M and serves 1,300+ customers on regulation-driven demand [20].

---

## 7. DIFFERENTIATION MATRIX

| Dimension | **AKAR (proposed)** | **Koltiva** | **Fairfood Trace** | **Dimitra** | **Free stack (Whisp + GFW/JRC + TRACES)** |
|---|---|---|---|---|---|
| **Farmer cost** | Free (exporter/co-op pays per shipment) | Free to farmer but client-funded program decides who gets mapped; no public pricing [7] | Free to farmer (grant/SME-subscription funded) [40] | Free-to-farmer claims, but service fees flow in DMTR token [10] | Free, but farmer must self-serve GIS + TRACES (unrealistic) [44][51] |
| **Offline capture (Bahasa, low-literacy)** | Core design: offline-first app in Bahasa Indonesia | Yes — KoltiTrace MIS + field agents; Bahasa (Indonesian company) [1][7] | Partial — Connect mobile app + NFC cards; not EUDR-geometry-first [36][37] | Mobile app, 60+ countries; Indonesia via Surveyor partnership [9][12] | No — Whisp assumes polygons already exist [44] |
| **Farmer-owned portable credentials (W3C VC)** | **Yes — the core novelty**: VC "plot passport" held by farmer/co-op, reusable across buyers | No public data-ownership/portability commitment [7] | Farmer sees transactions; no portable VC wallet [36] | No — data & proofs live inside Dimitra platform [8] | No identity layer at all [44] |
| **Public verifiability (QR → public chain)** | Yes — hash anchored on Polygon, public QR check | No — closed B2B silo [7] | Partial — Hedera-anchored claims, brand-facing QR [39] | Partial — chain-anchored inside proprietary app [8] | No (JRC/GFW maps are public data, not per-lot proofs) |
| **AI satellite deforestation verification** | Yes — convergence-of-evidence on public data (Whisp/JRC/GFW) + AI layer | Yes — ML deforestation checks + desktop verification [2][3] | No in-house EO pipeline | Yes — AI + satellite reports [8][9] | Yes (Whisp/GFW risk flags) but generic, unattested [44][49] |
| **EUDR DDS output (TRACES-ready)** | Yes — exporter dashboard builds due-diligence package | Yes — automated DDS generation [2] | No (transparency/premium focus) [36] | Partial — compliance reports; DDS packaging unclear [9] | TRACES itself accepts DDS but assembles nothing [51] |
| **Price for exporter** | Per-shipment fee (target: 1–2 orders below enterprise SaaS) | Undisclosed enterprise SaaS + services [7] | NGO/SME subscription, undisclosed [40] | Per-report in DMTR (volatile), undisclosed $ [10] | $0 + significant internal labor (€40–80/hr staff time) [68] |

---

## Key honest caveats
1. Almost all commercial pricing is private; figures above from third-party directories/blogs are low-to-medium confidence and dated 2024–2026.
2. Dimitra's and Koltiva's farmer counts are self-reported marketing numbers (contracted co-op members ≠ active mapped farmers).
3. "Farmers don't own their data" at Koltiva/Farmforce/Agridence is an inference from absence of any public portability commitment — no vendor states farmers *can't* export data; none states they can.
4. Market-size figures diverge 4x across research houses; use the FMI EUDR-specific $1.1B (2026) number as primary.
5. No "Beluga" EUDR company found; "EPI/farmforce" link unverified.

---

## CITATIONS (all accessed 2026-09-14)
[1] https://www.koltiva.com/
[2] https://asiafoodjournal.com/koltiva-launches-state-of-the-art-eudr-solutions/
[3] https://www.koltiva.com/global-eudr-compliance-tools-for-upstream-and-downstream-businesses
[4] https://www.comunicaffe.com/koltiva-empowers-digital-traceability-for-sustainable-coffee-over-25000-coffee-farmers-across-the-americas-digitally-validated/
[5] https://technode.global/2023/09/19/indonesian-sustainable-farming-and-supply-chain-traceability-startup-koltiva-raises-series-a-financing-led-by-ac-ventures/
[6] https://www.agnavigator.com/Article/2025/08/11/tackling-barriers-to-eudr-compliance-for-indonesian-smallholders/
[7] https://www.koltiva.com/koltitrace
[8] https://dimitra.io/
[9] https://blockchain.news/flashnews/dimitra-dmtr-and-surveyor-indonesia-aim-to-onboard-3m-farmers-for-eudr-compliance-using-blockchain-and-satellite-tech
[10] https://dimitratech.medium.com/dmtr-utility-in-the-real-world-7a55bd027655
[11] https://cointelegraph.com/news/how-blockchain-and-ai-can-reshape-agriculture-interview-with-dimitra
[12] https://www.agnavigator.com/Article/2025/04/15/dimitra-aims-to-shift-farmers-worldwide-from-analogue-to-digtial-services/
[13] https://agridence.com/about
[14] https://www.media-outreach.com/news/singapore/2025/08/19/400528/agridence-acquires-farmer-connect-to-deliver-unified-compliance-and-traceability-solutions-for-global-agriculture-supply-chains/
[15] https://ggba.swiss/en/agridence-acquires-genevas-traceability-platform-farmer-connect/
[16] https://tracextech.com/eudr-compliance/
[17] https://tracextech.com/blockchain-for-eudr-solution-for-supply-chain-transparency/
[18] https://osapiens.com/solutions/eudr/
[19] https://omr.com/en/reviews/product/osapiens-hub-for-due-diligence/pricing
[20] https://www.businesswire.com/news/home/20240729535470/en/osapiens-raises-%24120-million-funding-round-led-by-Growth-Equity-at-Goldman-Sachs-Alternatives
[21] https://pefc.org/news/pefc-and-osapiens-partner-to-advance-sustainable-forestry-and-eudr-compliance
[22] https://satelligence.com/home/eudr-due-diligence-solutions/
[23] https://www.digitalcoffeefuture.com/magazineen/seven-deforestation-monitoring-tools-that-can-support-compliance-with-the-eudr
[24] https://orbify.com/
[25] https://www.getapp.com/business-intelligence-analytics-software/a/orbify/
[26] https://www.prnewswire.com/news-releases/meridia-launches-verify-the-most-comprehensive-solution-for-eudr-risk-assessment-302276868.html
[27] https://www.rabobank.nl/en/about-us/rabofoundation/project/011461151/meridia-and-rabo-foundation-join-forces-to-support-smallholder-farmers-prepare-for-eudr-compliance
[28] https://www.global-traceability.com/en/radix-tree/
[29] https://www.fordaq.com/news/Fordaq_GlobalTraceability_RadixTree_EUDR_90224.html
[30] https://farmforce.com/
[31] https://farmforce.com/articles/from-the-syngenta-foundation-to-the-world-the-story-of-farmforce/ ; investors via https://pitchbook.com/profiles/company/399689-83
[32] https://softwarefinder.com/facility-management-software/farmforce
[33] https://www.sourcemap.com/solutions/eudr
[34] https://www.sourcemap.com/blog/eudr-milestone-sourcemap-goes-live-with-eu-traces-and-sap-integrations
[35] https://www.coolset.com/academy/best-6-eudr-compliance-tools-for-2026-supply-chain-due-diligence
[36] https://fairfood.org/solutions-for-a-fair-supply-chain/blockchain-tool-trace/
[37] https://github.com/Fairfood/Trace-Server ; https://github.com/Fairfood/Connect-Mobile
[38] https://fairfood.org/resources/giving-back-5-reasons-for-open-sourcing-trace/
[39] https://hedera.foundation/blog/fair-payments-for-carbon-markets-with-hedera-guardian
[40] https://fairfood.org/annual-report-2022-chapter-3/ ; https://fairfood.org/annual-report-2021-chapter-2-our-work/
[41] https://www.enveritas.org/eudr/
[42] https://knowledge4policy.ec.europa.eu/projects-activities/enveritas_en
[43] https://iov42.com/eudr-importer-exporter-due-diligence/
[44] https://www.fao.org/in-action/forest-data-partnership/news-and-events/news/news-detail/supporting-eudr-compliance-with-whisp/en
[45] https://whisp.earthmap.org/
[46] https://pypi.org/project/openforis-whisp/
[47] https://forobs.jrc.ec.europa.eu/GFC
[48] https://essd.copernicus.org/articles/18/1331/2026/
[49] https://www.globalforestwatch.org/
[50] https://pro-news.globalforestwatch.org/news-events/busting-3-myths-about-deforestation-monitoring-for-the-eudr
[51] https://osapiens.com/traces-nt/
[52] https://www.live-eo.com/blog/traces-for-eudr-guide
[53] https://www.foodnavigator.com/Article/2025/10/21/eudr-inside-the-it-system/
[54] https://github.com/The-Voice-Ledger/Voice-Ledger ; https://chain.link/hack-26/projects/the-voice-ledger
[55] https://www.mdpi.com/2673-4052/7/2/57
[56] https://repository.cimmyt.org/server/api/core/bitstreams/03616776-e40d-4fcc-9804-c91b1ba3d07c/content
[57] https://cryptoslate.com/global-blockchain-solutions-company-and-cardano-commercial-arm-emurgo-is-building-a-blockchain-traceability-solution-for-coffee-in-indonesia-interview/
[58] https://www.compasslist.com/insights/indonesia-agritech-startup-hara-goes-on-the-blockchain
[59] https://www.thejakartapost.com/opinion/2024/09/03/addressing-gaps-in-indonesias-national-commodity-dashboard-and-eudr.html
[60] https://zerodeforestationhub.eu/summary-report-support-to-indonesias-eudr-preparedness-through-electronic-smallholder-registration-e-stdb-acceleration/
[61] https://en.tempo.co/read/2116908/how-indonesian-coffee-farmers-and-exporters-face-eudr-rules
[62] https://indotech.group/portfolio_type/akar-farm-2/
[63] https://www.jejakin.com/en/about
[64] https://technode.global/2024/05/13/indonesian-carbon-management-provider-jejakin-secures-new-funding-of-2-7m/
[65] https://play.google.com/store/apps/details?id=com.saksipartaiperindo.app (also SI Saksi, Aplikasi Saksi PPP, iCount Saksi on Google Play)
[66] https://en.wikipedia.org/wiki/Saksi_(disambiguation)
[67] https://akar.id
[68] https://www.traceplot.com/blog/eudr-compliance-costs-sme
[69] https://trusty.report/the-eudr-compliance-dds-is-the-easy-part/
[70] https://www.foodexpoconnect.com/en/blog/eudr-deforestation-regulation-compliance-guide-food-exporters-2026
[70b] https://iopscience.iop.org/article/10.1088/1748-9326/ad8367
[71] http://www.sensorproject.net/wp-content/uploads/2017/04/Costs-and-benefits-of-RSPO-certification-for-independent-smallholders-FINAL.pdf
[72] https://www.rainforest-alliance.org/business/certification/how-much-does-rainforest-alliance-certification-cost/ ; 0.03–0.07% revenue: https://news.mongabay.com/2025/02/coffee-companies-are-readier-for-the-eudr-than-they-claim-commentary/
[73] https://fairtrade-advocacy.org/posts/247-what-latin-american-coffee-and-cocoa-farmers-are-telling-us-about-one-size-fits-all-eu-regulations
[74] https://farmforce.com/articles/the-real-cost-of-eudr-compliance-what-agri-commodities-companies-need-to-know/
[75] see [73]
[76] https://www.futuremarketinsights.com/reports/eudr-commodity-due-diligence-software-market
[77] https://haliocoffee.com/the-eu-vietnam-coffee-trade-a-strategic-analysis-of-the-vietnam-green-coffee-prices-eu-import-trend/
[78] https://www.stonex.com/en/insights/eudr-is-reshaping-the-global-coffee-trade-which-origins-are-best-positioned-to-meet-europe-s-new-requirements/
[79-note] https://www.360researchreports.com/market-reports/supply-chain-traceability-software-market-205665
[80] https://www.businessresearchinsights.com/market-reports/supply-chain-traceability-software-market-103736
[80b] https://www.futuremarketinsights.com/reports/supply-chain-visibility-software-market
[81] https://www.futuredatastats.com/supply-chain-traceability-market
[82] https://coinmarketcap.com/currencies/dimitra/
[83] https://www.cbi.eu/market-information/coffee/tips-become-eudr-compliant
[84] https://tracextech.com/eudr-coffee-compliance/ (vendor claim, low confidence)
[85] https://www.openforis.org/unlocking-forest-monitoring-through-open-source-innovation-explore-open-foris/
[86] https://forobs.jrc.ec.europa.eu/GFT
[87] https://asosiasikesehatanremaja.or.id/
[88] https://www.karyakreatifindonesia.co.id/en/umkm/akar-nfyr
[89] https://blockchain.news/flashnews/eudr-deadline-nears-dimitra-and-pt-surveyor-indonesia-deploy-ai-and-blockchain-to-onboard-3-million-indonesian-coffee-and-cocoa-farmers
[90] https://www.interu.io/eudr-compliance
[92] https://coffeegeography.com/2024/10/17/meridia-launches-verify-data-solution-for-eudr-to-assess-the-origin-of-green-coffee-and-comply-with-the-regulation/
