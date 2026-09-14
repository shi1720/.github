# AKAR — Technical Due-Diligence Research Report

**Project:** AKAR — offline-first plot-mapping PWA (Bahasa Indonesia) → AI satellite deforestation verification → W3C Verifiable Credentials → Polygon anchoring → EUDR due-diligence report generator.
**Purpose:** verify every load-bearing technical claim for a 24-hour, 3-student, free-tier-only hackathon MVP.
**Research date: all sources accessed 2026-09-14** (access date applies to every citation below unless noted). Citations: [n] = numbered source in the Source List at the end.

**Overall verdict: BUILDABLE in 24h** with the mitigations in §11. No claim in the concept is fabricated; two services rebranded recently (Global Forest Watch → Global Nature Watch; web3.storage/Storacha free tier is gone) and two free tiers shrank (Gemini, OpenRouter) — details below.

---

## 1. FAO Open Foris "Whisp" — VERIFIED, real and EUDR-aligned

**What it is.** Whisp ("**Wh**at **is** in that **p**lot") is FAO Open Foris' free, open-source (MIT) plot-level land-use / deforestation-risk analysis service, built with the Forest Data Partnership and running on Google Earth Engine [1][2]. It implements a **"Convergence of Evidence"** approach — combining many open EO datasets so no single dataset's bias decides the result — explicitly framed around the **EUDR cut-off date of 31 Dec 2020** [1][5]. FAO's own news page is titled "Supporting EUDR compliance with Whisp" [5], and the European Forest Institute lists Whisp among tools available to comply with EUDR [6]. This is exactly the "EUDR-aligned" citation the proposal needs.

**Inputs.** GeoJSON, WKT, or AgStack GeoIDs; points and polygons [1][2][4]. Web app, HTTP API, QGIS plugin, and integrations (Open Foris Ground, TechnoServe Terra Trac, Trace) [1].

**Datasets analyzed (from the repo's `layers_description.md`)** [3] — all four the prompt asked about are in, plus more:
- **EUFO_2020** — EC **JRC Global Forest Cover 2020** binary forest mask (the map JRC built for the EUDR benchmark date; 10 m, ~91% accuracy) [3][7]
- **GFC_TC_2020** — Hansen/UMD Global Forest Change tree cover 2020 [3]
- **ESA_TC_2020** — **ESA WorldCover** tree + mangrove classes 2020 [3]
- **JRC TMF** — Tropical Moist Forest undisturbed / degradation / deforestation masks split before/after 2020 [3]
- **Disturbance alerts split before/after 2020: RADD** (radar, confirmed), **GLAD-L** (Landsat), **GLAD-S2** (Sentinel-2) [3]
- Fires (MODIS, ESA FireCCI), primary/intact forest (GLAD Primary, IFL 2020, Global Forest Types), planted/plantation layers [3]
- **Commodity maps**: oil palm (Descals + FDaP model), cocoa (ETH Zurich, BNETD, FDaP), coffee (FDaP), rubber (RBGE 2020, FDaP), soy (Song) [3] — directly relevant to Indonesian palm/rubber/cocoa/coffee plots.

**API access — free, registration required, no published hard rate limits.**
- Live app + API: **https://whisp.openforis.org/** with API docs at `/api/docs` [2][4].
- Auth flow: sign in via Keycloak SSO (email registration), then **generate an API key in the app account page**; keys are UUIDs sent as an **`X-API-KEY` header**, valid 365 days, one active key per user [4].
- Endpoints: `POST /api/submit/geojson` (also `/submit/wkt`, `/submit/geo-ids`), then poll `GET /api/status/{token}` (SSE stream variant available), download via `/generate-geojson/{token}` or `/download-csv/{token}` [4]. **Jobs are asynchronous** — submit → poll → fetch.
- Capacity: **up to 5,000 geometries per job** [2]; per-key rate limits and geometry caps are runtime-configured and exposed via `GET /api/config` (not published as fixed numbers) [4].
- Cost: free and open source [1]; the whole stack (Next.js 16 + FastAPI + Celery + GEE) is on GitHub (`forestdatapartnership/whisp-app`, 787 commits) [4].

**Output.** CSV or GeoJSON of per-plot statistics for every layer, plus aggregate indicators and an **EUDR-style risk classification: "Low" / "High" / "More Info Needed"** [1][2].

**Repo status.** `forestdatapartnership/whisp`: MIT, ~593 commits, 38 stars, active development, Python package **`openforis-whisp` on PyPI** (the pip package itself needs a Google Earth Engine account + cloud project — use the hosted API instead for the hackathon) [2][8]. A support-forum thread shows occasional users struggling with API access [9] — **register accounts + generate keys BEFORE the hackathon** (see §11).

## 2. Global Forest Watch Data API — VERIFIED free; note the rebrand

**Rebrand:** Global Forest Watch is becoming **Global Nature Watch** (WRI); the rename was announced July 2026 and help pages 301-redirect from globalforestwatch.org to globalnaturewatch.org [10]. The **Data API itself still lives at `https://data-api.globalforestwatch.org`** [11]. Mention the new name in the proposal to show currency.

**Access:** free; register at globalforestwatch.org/my-gfw (don't use social login) or `POST /auth/sign-up`; get a bearer token via `POST /auth/token`; create an API key via `POST /auth/apikey` (alias, email, organization, optional domain allowlist); use it as an **`x-api-key` header** [12]. **Keys expire after 1 year; with no domain allowlist you get the lowest rate-limit tier** (exact numbers unpublished; quota raises via gfw@wri.org) [12][13].

**Datasets:** tree cover loss (Hansen/UMD, 30 m, queryable via SQL-ish endpoint e.g. `GET /dataset/umd_tree_cover_loss/v1.9/query/json?sql=SELECT SUM(area__ha) ...`), tree cover gain, **GLAD-L** (30 m Landsat), **GLAD-S2** (10 m Sentinel-2), **RADD** (10 m radar, tropics), and the **Integrated Deforestation Alerts** layer that now combines GLAD-L + GLAD-S2 + RADD + the newer **DIST-ALERT** (UMD/NASA, global, all vegetation) [12][14][15]. JRC Global Forest Cover 2020 is publicly available on GEE / JRC's own portal [7][16] (and is already inside Whisp's answer [3]), so AKAR doesn't need to host it.

**Hackathon role:** backup/secondary evidence to Whisp (e.g., pull GLAD/integrated alert counts for the drawn polygon), not the primary engine.

## 3. Sentinel-2 imagery & satellite basemap tiles — VERIFIED

**Copernicus Data Space Ecosystem (CDSE)** — free registration; generous free tier (all functionality free for "General users"): **12 TB/month download transfer** (rolling 30 days; throttled to 1 MB/s after), **Sentinel Hub APIs: 10,000 processing units + 10,000 requests/month, 300 PU-or-requests/minute**, **openEO: 10,000 credits/month** [17][18]. APIs: STAC, S3, openEO, Sentinel Hub (Processing API can return true-color Sentinel-2 PNG for a bbox — feasible for one-off "show the evidence" imagery) [18][19].

**Verdict for a 24h web app:** CDSE is plenty free but is an extra OAuth + processing integration. For the map background, use a tile service instead:
- **Esri World Imagery via ArcGIS Location Platform — recommended.** Free tier: **2M basemap tiles/month** (then $0.15/1k), free API key, satellite style included; attribution required [20][21]. Works in MapLibre/Leaflet directly.
- **Mapbox**: free **50,000 map loads/month** for GL JS (a load = map init, unlimited tiles for 12 h), then $5/1k [22]. Also fine; needs card on file historically — Esri or plain raster tiles are lower-friction.
- Note: Esri's legacy "World Imagery for OSM tracing without a key" allowance exists but is scoped to OSM editing [23] — use the Location Platform key route to be clean.
- Sentinel-2 cloud-free basemap alternative: EOX S2 Cloudless is another known free-with-attribution option (not load-bearing; not further verified here).

## 4. Polygon PoS in 2026 — VERIFIED, fees are fractions of a cent

- **Mainnet fee level:** Polygon PoS average fee ≈ **$0.009–$0.021 per transaction across 2026** (Jan avg $0.0208, Mar avg $0.0094; averages include heavy DeFi calls) [24]. Gas price snapshots ~250–380 gwei with **POL ≈ $0.08** (PolygonScan gas tracker / trackers, Aug 2026 snapshots) [25].
- **Cost of anchoring one 32-byte Merkle root:** SSTORE of a new (zero→non-zero, cold) slot costs **22,100 gas** post-Berlin (EIP-2929) [26][27]; + 21,000 base tx + ~2k for an event ≈ **~45,000 gas** → at 280 gwei × POL $0.08 ≈ **0.0126 POL ≈ $0.001 (≈ one-tenth of a US cent)**; even at a 500-gwei spike ≈ $0.002 [25][26]. The "fractions of a cent" claim is TRUE for a simple anchor call (batch many plots under one Merkle root and it amortizes to ~zero per plot).
- **Amoy testnet:** active, **chain ID 80002**, POL gas token, Sepolia-anchored, ~2 s blocks, explorer amoy.polygonscan.com [28][29]. **Free faucets:** QuickNode (1 drip/12 h) [30], **Alchemy (0.1 POL/24 h, no account)** [31], Chainlink, GetBlock, ETHGlobal [32]; Polygon's docs list faucets [33] (one 2026 guide reports the official polygon faucet itself now defers to third-party faucets [34] — rely on Alchemy/QuickNode).
- **Deploy time:** with Foundry, `forge init` → `forge create --rpc-url https://rpc-amoy.polygon.technology --private-key ...` is a standard minutes-long flow (standard tutorials: Cyfrin Updraft, chain docs) [35][36]. A 20-line `AkarAnchor` contract (`mapping(bytes32=>uint256) anchoredAt; function anchor(bytes32 root)`) deploys in **well under 30 minutes including faucet drip**. Hardhat equivalent equally standard.
- **Alternatives worth naming:** **Base** (Coinbase OP-stack L2; median fee ≈ $0.02, simple transfers as low as ~$0.0007 [37]) and **Lisk** (OP-Superchain L2 with an explicit **Indonesia strategy** — MoU with Indonesia's Ministry of Communications & Informatics / 1000 Startup Digital program, and an L2 grant program up to ~$16k [38][39]) — Lisk is a great judge-facing mention for an Indonesian project. **Recommendation: Polygon PoS (Amoy for the demo)** — best faucet/tooling ubiquity, fees ~$0.001, and Polygon's strong Indonesian ecosystem presence; name Base and Lisk as portable alternatives (EVM bytecode identical).

## 5. W3C Verifiable Credentials — VERIFIED

- **Status:** **VC Data Model 2.0 became a W3C Recommendation on 15 May 2025**, published together with the securing specs (Data Integrity, VC-JOSE-COSE, controller documents, Bitstring Status List) — seven Recommendations total [40][41][42].
- **Recommended Node.js stack (simplest robust for 24 h):** **`@digitalbazaar/vc`** (v7.2.0, actively maintained by Digital Bazaar, the principal editor-company of the spec) + **`@digitalbazaar/ed25519-signature-2020`** + **`@digitalbazaar/ed25519-verification-key-2020`**, with a **`did:key`** identifier (README documents exactly this did:key + Ed25519 flow) [43][44][45]. ~30 lines to issue a signed VC. For VC 2.0-native proofs the Data Integrity `eddsa-rdfc-2022` cryptosuite packages from the same org slot into the same `vc.issue()` call [40][43].
- **Alternatives:** **Veramo** — modular DID/VC framework, now maintained under the Decentralized Identity Foundation, actively developed; heavier setup (agent + plugins), better if you also want did:ethr/KMS [46]. **DIDKit (SpruceID) — AVOID: repo archived 10 July 2025, read-only** (Spruce points to its Rust `ssi` library instead) [47].
- **Selective disclosure (one line for the proposal):** later, swap/augment the proof with **IETF SD-JWT VC** (draft-ietf-oauth-sd-jwt-vc, standards-track, in IESG processing 2026, already adopted in EU Digital Identity Wallet implementing acts) or the **W3C Data Integrity BBS cryptosuite** (Candidate Recommendation) for unlinkable, field-level disclosure of farmer data [48][49].

## 6. Offline-first PWA geolocation ("walk the boundary") — VERIFIED, one flag

- **GPS capture:** `navigator.geolocation.watchPosition()` with `enableHighAccuracy: true` streams fixes (lat/lon + `coords.accuracy` in meters) in all mobile browsers; requires HTTPS + user permission [50]. **Accuracy: GPS-enabled smartphones are typically ≤ 4.9 m radius under open sky (GPS.gov)** [51]; peer-reviewed urban testing shows ~7–13 m typical under obstruction [52]. So quote **"~5 m open-sky, 5–10 m typical field accuracy"** — fine for EUDR (points suffice for plots ≤ 4 ha; see §9) and for smallholder polygons; log `coords.accuracy` per vertex as metadata (nice judge detail).
- **Map/drawing library:** **MapLibre GL JS** (open-source Mapbox GL fork, WebGL, v6.x, supports `RasterTileSource` for satellite tiles) [53] **or Leaflet** (stable 1.9.x, 42 KB, mobile-first; 2.0 still alpha since Aug 2025) [54]. **Recommendation: MapLibre GL JS + Esri imagery tiles + Terra Draw (or mapbox-gl-draw fork) for polygon editing**; Leaflet + leaflet-geoman is the equally safe conservative choice. Either is hackathon-standard; walk-mode just pushes each watchPosition fix into the polygon ring.
- **Offline queue:** IndexedDB write queue + Service Worker **Background Sync API**. **FLAG: Background Sync is Chromium-only — Chrome/Edge/Samsung/Chrome-for-Android yes; Safari (incl. all iOS) and Firefox NO** (~78% global coverage) [55]. Mitigation (standard): queue in IndexedDB and also flush on `online` event / app foreground — works everywhere; Background Sync becomes a progressive enhancement. Demo on an Android phone (Chrome), which is also the realistic Indonesian smallholder device.
- **PWA install on Android:** standard — HTTPS + manifest (name, icons, display, start_url) + service worker ⇒ Chrome install prompt [56][57]. No blockers.

## 7. AI/LLM free tiers (as of Sept 2026) — VERIFIED, with a December-2025 caveat

- **Google Gemini API** — free tier exists, **no credit card**, but Google **cut free quotas on 7 Dec 2025** and now points to the AI Studio dashboard for authoritative per-model limits [58][59]. Current commonly-reported free limits: **Gemini 2.5 Flash: 10 RPM / 250 RPD; Gemini 2.5 Flash-Lite: 15 RPM / 1,000 RPD; 2.5 Pro: 5 RPM / 100 RPD** (250k TPM each) [59]. **Gemini officially supports Indonesian (id)** input/output [60].
- **Groq** — free tier, no card, org-level limits: **Llama 3.1 8B Instant: 30 RPM / 14,400 RPD; Llama 3.3 70B Versatile: 30 RPM / 1,000 RPD** (TPM caps 6k/12k) [61][62]. Blazing fast; **but Llama 3.3's officially supported languages are 8 (En, De, Fr, It, Pt, Hi, Es, Th) — Indonesian is NOT officially supported** (works in practice, unwarranted quality) [63].
- **Anthropic Claude API** — no standing free tier; **new users receive only a small amount of free trial credits**; **Claude Haiku 4.5: $1 / MTok input, $5 / MTok output** ($0.50/$2.50 batch) [64]. Excellent Indonesian, but paid — position as the production upgrade path, not the hackathon engine.
- **OpenRouter** — ~20–28 `:free` models; **20 RPM always; 50 requests/day with no credits, 1,000/day once you've ever bought $10 of credits** [65]. Useful as a second fallback only.
- **Recommendation:** **(a) Bahasa Indonesia explanation generation: Gemini 2.5 Flash-Lite (1,000 RPD) with Flash for the few longer reports** — official Indonesian support + biggest no-card free quota. **(b) Farmer Q&A copilot: same Gemini key; wire Groq Llama-3.3-70B as automatic fallback** (open-source fallback story + 1k RPD headroom; note the unofficial-Indonesian caveat in the appendix). Total demo-day load (≈ tens of requests) fits either provider alone.

## 8. Storage / hosting free tiers — VERIFIED

- **Supabase Free plan:** **500 MB Postgres (shared CPU, 500 MB RAM), 1 GB file storage, 50,000 MAUs, 500k Edge Function invocations, 5 GB egress, 2 active projects; free projects pause after 1 week of inactivity** [66]. **PostGIS is available as a dashboard-enable extension (`create extension postgis`)** — works on the free tier [67]. Auth (email/OTP) included. Perfect fit.
- **Vercel Hobby (free):** 100 GB bandwidth/mo; functions ≈ 1M invocations, 4 h active CPU, 60 s max duration; non-commercial single dev (Feb 2026 restructure to Active CPU metering) [68]. Fine for the Next.js PWA + API routes.
- **IPFS pinning — CHANGED LANDSCAPE:** classic **web3.storage free tier is gone**; Storacha's paid Medium tier is ~$10/mo/100 GB [69], and **storacha.network now redirects to fil.one** (pay-as-you-go $4.99/TB/mo, 30-day trial) — observed directly on 2026-09-14 [70]. **Pinata Free: 1 GB storage, 500 files, 1 gateway, 10 GB bandwidth, 10k requests** — still the workable free option [71]. **Recommendation:** make IPFS optional: store the report PDF in Supabase Storage, put its **SHA-256 hash** in the VC + Merkle tree (integrity without pinning), and pin to Pinata free only if time remains.

## 9. PostGIS duplicate-plot fraud check + EU DDS GeoJSON — VERIFIED

- **`ST_Intersects(geom_a, geom_b)`** returns true when geometries share any point, **automatically uses the spatial (GiST) index** via its built-in bbox pre-filter [72]. Duplicate/overlap fraud check is literally one indexed query: `SELECT id FROM plots WHERE ST_Intersects(geom, :new_geom) AND id != :self;` (use ST_Intersects rather than ST_Overlaps — ST_Overlaps is false for containment cases; also cute demo metric: `ST_Area(ST_Intersection(...)::geography)` for overlap m²). Trivial — hours, not days.
- **EU DDS geolocation format:** the EU **TRACES / EUDR Information System accepts GeoJSON** import for production-place geolocation; the Commission's "EUDR GeoJSON File Description" (v1.0 May 2024; **v1.5 dated 5 May 2025**) specifies: RFC 7946 GeoJSON, **WGS 84 (EPSG:4326), coordinates with at least 6 decimal places, Point allowed for plots ≤ 4 ha, Polygon required > 4 ha**, optional per-feature properties `ProducerName`, `ProducerCountry` (ISO2), `ProductionPlace`, `Area`, file ≤ 25 MB [73][74][75]. AKAR's export = PostGIS `ST_AsGeoJSON` + those properties → judge-checkable "TRACES-ready file" claim.

## 10. QR verification page — VERIFIED (standard)

Standard pattern, ~50 lines client-side: QR encodes credential URL + plot hash; the page recomputes `keccak256` of the canonical plot record, verifies the VC's Ed25519 proof in-browser, and checks Merkle inclusion against the on-chain root via a read-only RPC call using **ethers.js or viem** with an **OpenZeppelin-style Merkle proof** (`@openzeppelin/merkle-tree` JS to build/prove, `MerkleProof.verify` semantics on/off-chain) [76][77]. Read calls on Amoy RPC are free.

## 11. Red flags & mitigations for the 24-hour build

1. **Whisp is async and GEE-backed** (submit → poll; job latency not guaranteed) and needs a registered account + in-app API key [4][9]. → **Register 2–3 accounts and mint keys BEFORE the event; cache one real response as demo fixture; degrade to GFW Data API alert counts [12] if Whisp is slow live.**
2. **Gemini free tier shrank Dec 2025** (Flash 250 RPD) [58][59]. → Use **Flash-Lite (1,000 RPD)** + Groq fallback; demo load is tiny.
3. **Background Sync ≠ iOS Safari** [55]. → IndexedDB queue + `online`-event flush everywhere; Background Sync as enhancement; demo on Android.
4. **Free IPFS pinning is nearly dead** (web3.storage gone; storacha.network → fil.one) [69][70]. → SHA-256 hash on-chain + Supabase Storage; Pinata 1 GB free [71] only if time allows.
5. **Mainnet POL acquisition needs an exchange/KYC** (fee itself ≈ $0.001 [24][25][26]). → **Demo on Amoy** (free faucets [30][31]); one slide: "mainnet cost per anchored batch ≈ $0.001."
6. **GFW rebrand** (→ Global Nature Watch, July 2026) [10] — cite the new name; API endpoints unchanged [11].
7. **Don't ship the Whisp Python package** in-app (needs each user's Google Earth Engine cloud project [2]) — use the hosted API.
8. **Llama/Groq not officially Indonesian** [63] — keep Gemini primary for Bahasa output.
9. Supabase free project pauses after 7 idle days [66] — irrelevant during the event; unpause before judging if built early.
10. **Scope guard:** skip CDSE Sentinel-2 processing in the MVP (basemap tiles + Whisp evidence are enough); it's the #1 time sink temptation.

## 12. Recommended concrete stack (free-tier, 24 h, 3 people)

| Layer | Choice | Free-tier proof |
|---|---|---|
| PWA frontend | Next.js (PWA manifest + SW) on **Vercel Hobby**, Bahasa Indonesia UI | [68] |
| Map | **MapLibre GL JS v6** + **Esri World Imagery** (ArcGIS Location Platform key, 2M tiles/mo) + Terra Draw; GPS via `watchPosition` (~5 m open-sky [51]) | [20][21][53] |
| Offline | IndexedDB queue (Dexie) + `online` flush + Background Sync where available | [55] |
| DB/Auth/Storage | **Supabase Free** + **PostGIS** (`ST_Intersects` dupe check) | [66][67][72] |
| Deforestation verification | **Whisp API** (`POST /api/submit/geojson`, `X-API-KEY`) → Low/High/More-Info + per-dataset table (JRC EUFO 2020, TMF, GLAD, RADD, WorldCover, palm/cocoa/rubber maps); GFW Data API as backup evidence | [1]–[5][12] |
| Credentials | **`@digitalbazaar/vc` 7.2.0 + Ed25519 suite + did:key** in a Vercel/Supabase function | [43][44][45] |
| Chain | **Polygon Amoy** (80002), Foundry, 20-line Merkle-root anchor contract; Alchemy faucet; verify page reads root via **viem** | [28][31][35][76] |
| LLM | **Gemini 2.5 Flash-Lite/Flash free tier** (Bahasa explanations + farmer copilot), **Groq Llama-3.3-70B** fallback | [59][60][61] |
| EUDR output | GeoJSON per Commission spec v1.5 (WGS84, 6 decimals, point ≤ 4 ha) + PDF report, SHA-256 in VC & Merkle leaf | [73][74] |

**Suggested 24 h split (3 people):** (A) PWA + map + offline queue; (B) Supabase/PostGIS + Whisp integration + EUDR GeoJSON/PDF; (C) VC issuance + Amoy contract + QR verify page + LLM copilot. Pre-event: accounts/keys (Whisp, GFW, ArcGIS, Gemini, Groq, Supabase, Vercel, Alchemy faucet), repo scaffold.

---

## Source List (all accessed 2026-09-14)

[1] Whisp – Open Foris. https://www.openforis.org/whisp/
[2] GitHub — forestdatapartnership/whisp (README: datasets, 5,000 geometries/job, GEE requirement, MIT, PyPI). https://github.com/forestdatapartnership/whisp
[3] Whisp layers description (full dataset list incl. EUFO_2020/JRC, ESA WorldCover, GLAD-L/S2, RADD, TMF, commodity maps). https://github.com/forestdatapartnership/whisp/blob/main/layers_description.md
[4] GitHub — forestdatapartnership/whisp-app (endpoints, Keycloak sign-in, X-API-KEY, 365-day UUID keys, GET /config limits, stack). https://github.com/forestdatapartnership/whisp-app
[5] FAO Forest Data Partnership: "Supporting EUDR compliance with Whisp" (convergence of evidence; 31 Dec 2020 cut-off). https://www.fao.org/in-action/forest-data-partnership/news-and-events/news/news-detail/supporting-eudr-compliance-with-whisp/en
[6] EFI: "What tools are available to comply with the EUDR?" https://efi.int/publication/what-tools-are-available-comply-eudr
[7] JRC Global Forest Cover 2020 v1 data access (10 m, EUDR context). https://forobs.jrc.ec.europa.eu/GFC/v1
[8] openforis-whisp on PyPI. https://pypi.org/project/openforis-whisp/
[9] Open Foris Support: "Can't access WHISP API". https://openforis.support/questions/4467/cant-access-whisp-api
[10] GFW blog: "Global Forest Watch is Becoming Global Nature Watch" (July 2026). https://www.globalforestwatch.org/blog/data-and-tools/gfw-now-global-nature-watch/
[11] GFW Data API (ReDoc root). https://data-api.globalforestwatch.org/
[12] OpenEPI how-to: "Getting started using Global Forest Watch Data API" (sign-up, /auth/token, /auth/apikey, x-api-key, domain-tiered rate limits, umd_tree_cover_loss query). https://developer.openepi.io/how-tos/getting-started-using-global-forest-watch-data-api
[13] GFW Help Center — create and use an API key (redirects to globalnaturewatch.org; 1-year key expiry, quota contact gfw@wri.org). https://globalnaturewatch.org/help/developers/guides/create-and-use-an-api-key/
[14] GFW blog: Integrated Deforestation Alerts (GLAD-L, GLAD-S2, RADD, DIST-ALERT). https://www.globalforestwatch.org/blog/data-and-tools/integrated-deforestation-alerts/
[15] GFW blog: DIST-ALERT global vegetation disturbance alerts. https://www.globalforestwatch.org/blog/data-and-tools/global-vegetation-disturbance-deforestation-alerts/
[16] Google Earth Engine catalog — EC JRC global forest cover/types 2020. https://developers.google.com/earth-engine/datasets/catalog/JRC_GFC2020_subtypes_V1
[17] CDSE Quotas & Limitations (12 TB/mo transfer; SH 10,000 PU/mo, 300/min; openEO 10,000 credits/mo). https://documentation.dataspace.copernicus.eu/Quotas.html
[18] CDSE APIs overview (STAC, S3, openEO, Sentinel Hub). https://documentation.dataspace.copernicus.eu/APIs.html
[19] CDSE FAQ (free-of-charge with predefined quotas). https://documentation.dataspace.copernicus.eu/FAQ.html
[20] ArcGIS Location Platform pricing (2M basemap tiles/mo free; $0.15/1k after). https://location.arcgis.com/pricing/
[21] Esri blog: Basemap sessions for ArcGIS Location Platform (1,000 free sessions alternative). https://www.esri.com/arcgis-blog/products/platform/announcements/basemap-sessions
[22] Mapbox pricing breakdown 2026 (50k map loads/mo free; $5/1k). https://storerocket.io/learn/mapbox-pricing
[23] OSM wiki: Esri imagery permission for OSM tracing. https://wiki.openstreetmap.org/wiki/Esri
[24] "Polygon POS Transaction Fees 2026" ($0.015 avg; Jan $0.0208 / Mar $0.0094; base fee ~477–571 gwei months). https://polygonposvspolygon.com/polygon-pos-transaction-fees.html
[25] PolygonScan gas tracker (~280 gwei; POL ≈ $0.08, Aug 2026 snapshot). https://polygonscan.com/gastracker
[26] EIP-2929 (cold SSTORE 22,100 gas). https://eips.ethereum.org/EIPS/eip-2929
[27] "Understanding gas costs after Berlin" (22,100/20,000 zero→non-zero). https://hackmd.io/@fvictorio/gas-costs-after-berlin
[28] Polygon blog: Introducing the Amoy testnet (chain 80002, Sepolia-anchored, POL gas). https://polygon.technology/blog/introducing-the-amoy-testnet-for-polygon-pos
[29] Amoy PolygonScan explorer. https://amoy.polygonscan.com/
[30] QuickNode Amoy faucet (1 drip/12 h). https://faucet.quicknode.com/polygon/amoy
[31] Alchemy Amoy faucet (0.1 POL/24 h, no account). https://www.alchemy.com/faucets/polygon-amoy
[32] ETHGlobal Amoy faucet. https://ethglobal.com/faucet/polygon-amoy-80002
[33] Polygon docs: test token faucets. https://docs.polygon.technology/tools/gas/matic-faucet
[34] Spydra guide 2026 (official faucet defers to third-party). https://www.spydra.app/blog/how-to-move-test-matic-and-usdc-tokens-to-your-wallet-on-polygon-amoy-step-by-step-guide
[35] Cyfrin Updraft: deploying a contract to a testnet with Foundry. https://updraft.cyfrin.io/courses/foundry/foundry-simple-storage/deploying-smart-contract-testnet-sepolia
[36] "How to deploy smart contracts using Foundry" (forge create flow). https://awesamarth.hashnode.dev/how-to-deploy-smart-contracts-using-foundry
[37] Base docs: network fees (+ The Block L2 fee data; Base median ≈ $0.02, transfers ~$0.0007). https://docs.base.org/base-chain/network-information/network-fees ; https://www.theblock.co/data/scaling-solutions/scaling-overview/layer-2-average-transaction-cost-in-usd-daily-7dma
[38] Lisk L2 Grant Program (up to $16k builder grants). https://lisk.com/blog/posts/say-hello-to-the-new-Lisk-L2-grant-program/
[39] Decrypt: Lisk × Indonesian Ministry of Communications partnership. https://decrypt.co/219203/lisk-announces-strategic-partnership-with-the-indonesian-ministry-of-communications-and-informatics-to-support-local-web3-startups
[40] W3C News (15 May 2025): "The Verifiable Credentials 2.0 family of specifications is now a W3C Recommendation." https://www.w3.org/news/2025/the-verifiable-credentials-2-0-family-of-specifications-is-now-a-w3c-recommendation/
[41] W3C press release: Verifiable Credentials 2.0. https://www.w3.org/press-releases/2025/verifiable-credentials-2-0/
[42] VC Data Model v2.0 (W3C Recommendation). https://www.w3.org/TR/vc-data-model-2.0/
[43] @digitalbazaar/vc on npm (v7.2.0). https://www.npmjs.com/package/@digitalbazaar/vc
[44] digitalbazaar/vc README (did:key + Ed25519Signature2020 issuance example). https://github.com/digitalbazaar/vc
[45] @digitalbazaar/ed25519-signature-2020 on npm. https://www.npmjs.com/package/@digitalbazaar/ed25519-signature-2020
[46] Veramo (Decentralized Identity Foundation, active). https://github.com/decentralized-identity/veramo
[47] spruceid/didkit — archived 10 Jul 2025, read-only. https://github.com/spruceid/didkit
[48] IETF draft-ietf-oauth-sd-jwt-vc (standards track; draft-19; IESG 2026; in EUDI wallet acts). https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/
[49] W3C Data Integrity BBS Cryptosuites v1.0 (Candidate Recommendation; selective disclosure). https://www.w3.org/TR/vc-di-bbs/
[50] MDN: Using the Geolocation API (watchPosition, enableHighAccuracy, coords.accuracy, HTTPS+permission). https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API/Using_the_Geolocation_API
[51] GPS.gov — GPS Accuracy ("GPS-enabled smartphones are typically accurate to within a 4.9 m radius under open sky"). https://www.gps.gov/gps-accuracy
[52] Merry & Bettinger, smartphone GPS accuracy study (urban ~7–13 m). https://pmc.ncbi.nlm.nih.gov/articles/PMC6638960/
[53] MapLibre GL JS docs (WebGL, v6.x, RasterTileSource). https://maplibre.org/maplibre-gl-js/docs/
[54] Leaflet homepage (42 KB, mobile-friendly; 2.0.0-alpha Aug 2025). https://leafletjs.com/
[55] caniuse — Background Sync API (Chromium yes incl. Chrome Android; Safari/iOS no; Firefox no; ~78%). https://caniuse.com/background-sync
[56] web.dev: What does it take to be installable? https://web.dev/articles/install-criteria
[57] MDN: Making PWAs installable. https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable
[58] Google — Gemini API rate limits doc (limits now shown per-account in AI Studio). https://ai.google.dev/gemini-api/docs/rate-limits
[59] AI Free API: Gemini free-tier rate limits guide (Jan 2026 update; Dec 7 2025 quota cuts; Flash 10 RPM/250 RPD, Flash-Lite 15 RPM/1,000 RPD, Pro 5 RPM/100 RPD). https://www.aifreeapi.com/en/posts/gemini-api-free-tier-rate-limits
[60] Firebase AI Logic — supported Gemini models & languages (Indonesian "id" supported). https://firebase.google.com/docs/ai-logic/models
[61] TokenMix: Groq free tier limits 2026 (30 RPM / 14,400 RPD Llama 3.1 8B; 1,000 RPD Llama 3.3 70B; org-level; no card). https://tokenmix.ai/blog/groq-free-tier-limits-2026
[62] Klymentiev: Groq API pricing & free tier 2026. https://klymentiev.com/blog/groq-pricing
[63] Meta Llama 3.3 70B model card (8 official languages; Indonesian absent). https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
[64] Anthropic pricing docs (Haiku 4.5 $1/$5 per MTok; $0.50/$2.50 batch; "new users receive a small amount of free credits"). https://platform.claude.com/docs/en/about-claude/pricing
[65] PricePerToken: OpenRouter free tier 2026 (20 RPM; 50 RPD unfunded / 1,000 RPD after $10 credits). https://pricepertoken.com/endpoints/openrouter/free
[66] Supabase pricing (Free: 500 MB DB, 1 GB storage, 50k MAU, 500k edge invocations, 2 active projects, 1-week pause). https://supabase.com/pricing
[67] Supabase docs: PostGIS extension. https://supabase.com/docs/guides/database/extensions/postgis
[68] DeployWise: Vercel free tier limits 2026 (100 GB bandwidth; 1M invocations; 4 h active CPU; 60 s timeout; Feb 2026 restructure). https://deploywise.dev/blog/vercel-free-tier-limits-2026
[69] CryptoAdventure: Web3.Storage/Storacha review 2026 (free tier discontinued; $10/100 GB). https://cryptoadventure.com/web3-storage-review-2026-storacha-ucan-spaces-and-ipfs-plus-filecoin-storage/
[70] fil.one/pricing (storacha.network 301-redirects here; $4.99/TB/mo PAYG, 30-day trial) — redirect observed directly 2026-09-14. https://fil.one/pricing
[71] Pinata pricing (Free: 1 GB, 500 files, 1 gateway, 10 GB bandwidth, 10k requests). https://pinata.cloud/pricing
[72] PostGIS docs: ST_Intersects (any-point-in-common; automatic index-assisted bbox comparison). https://postgis.net/docs/ST_Intersects.html
[73] EU Commission "EUDR GeoJSON File Description" v1.5 (5 May 2025) — WGS84/EPSG:4326, ≥6 decimals, Point ≤4 ha / Polygon >4 ha, properties, 25 MB. https://nli.gov.cz/wp-content/uploads/EUDR-EUDR-GEOJSON-FILE-DESCRIPTION-1.5_.pdf
[74] EUDR GeoJSON File Description v1.0 (8 May 2024, ATIBT mirror). https://www.atibt.org/files/upload/newsletter/1_EUDR_-_Gelocation_file_description_1-0.pdf
[75] LiveEO: EUDR geolocation guide (TRACES GeoJSON requirements overview). https://www.live-eo.com/blog/eudr-geolocation-guide
[76] OpenZeppelin merkle-tree JS library (build trees/proofs; pairs with MerkleProof.verify). https://github.com/OpenZeppelin/merkle-tree
[77] OpenZeppelin Contracts 5.x utilities — MerkleProof. https://docs.openzeppelin.com/contracts/5.x/utilities
