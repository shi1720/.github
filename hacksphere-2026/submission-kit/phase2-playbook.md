# Phase 2 Playbook — the 24-hour build (Oct 10–11, 2026)

Everything to prepare **before** the clock starts, so the marathon is execution, not discovery.
(Rules allow pre-provisioned accounts/keys; all *code* must be written inside the 24 h.)

## 1. Accounts & API keys — create these the week before (all free)

| Service | What for | How to get it | Owner |
|---|---|---|---|
| FAO Whisp | Deforestation evidence API | Register at whisp.openforis.org (Keycloak sign-up) → create API key. Test with one GeoJSON POST; jobs are async, so practice the submit→poll flow | Member B |
| Global Forest Watch Data API | Backup evidence track | data-api.globalforestwatch.org → request free API key (x-api-key) | Member B |
| ArcGIS Location Platform | Esri World Imagery basemap tiles (2M tiles/mo free) | location.arcgis.com free account → API key | Member A |
| Google AI Studio (Gemini) | Bahasa verdicts + Tanya Tani copilot (Flash-Lite: 1,000 req/day free) | aistudio.google.com → Get API key (no card) | Member B |
| Groq | LLM fallback (Llama 3.3 70B free tier) | console.groq.com → API key | Member B |
| Supabase | Postgres + PostGIS + Auth + Storage | supabase.com free project; enable PostGIS extension; note the 7-day pause rule — create fresh project that week | Member C |
| Vercel | Hosting + CI previews | vercel.com hobby account, connect the GitHub org/repo | Member C |
| Polygon Amoy | Testnet for TandaRegistry.sol | Wallets (fresh, throwaway) + POL from Alchemy/QuickNode faucets — drip over several days, faucets are stingy | Member C |
| WalletConnect/SIWE test wallet | Exporter sign-in demo | Any browser wallet with an Amoy account | Member C |

Also pre-install locally: Node 22, pnpm, Foundry, Supabase CLI. Cache `create-next-app` and
node_modules once at home (venue bandwidth is not for gigabytes — guidebook says so).

## 2. Pre-event rehearsals (not code — skills)

- Each member walks once through their stack's "hello world" (fresh Next.js app; a PostGIS
  `ST_Intersects` query; deploy a Foundry contract to Amoy; issue one VC with
  `@digitalbazaar/vc`) so nothing is *first-ever* during the marathon.
- Capture a real GPS point + polygon with a phone browser (`watchPosition`) outdoors.
- Prepare the **seed scenario** on paper only: Gayo coordinates for 6 demo plots (5 clean, 1
  drawn over a 2021 GLAD alert area — find one via the GFW map), farmer names, coop name.
- Rehearse the airplane-mode demo choreography once.

## 3. The 24-hour plan (as committed in the proposal — §4)

| Window (WIB) | Member A — Frontend/PWA | Member B — Backend/AI | Member C — Web3/Infra |
|---|---|---|---|
| 10:00–14:00 | App shell; map capture; offline queue | Supabase schema + PostGIS; API skeleton | Repo/CI; Vercel + Supabase; deploy TandaRegistry.sol to Amoy |
| 14:00–19:00 | Farmer flows; verification result UI | Whisp + GFW integration; risk scorer | VC issuance service (did:key, Ed25519) |
| 19:00–00:00 | Cooperative Console | Gemini Bahasa verdicts; Tanya Tani | Merkle batcher + anchoring worker |
| 00:00–05:00 | Exporter DDS Studio | TRACES GeoJSON + PDF dossier generator | Public verify page (hash + proof in browser) |
| 05:00–08:00 | Integration pass, all hands — seed data, airplane-mode drill, cross-device tests | | |
| 08:00–10:00 | Hardening, deploy freeze, pitch rehearsal ×3, Q&A drill | | |

**Cut-not-fake rule** (also written in the proposal): if a feature slips its window, cut it and
say so on stage. Never simulate. The no-mockup rule carries drastic penalties — and integrity
is part of our brand.

Cut order if needed (last → first): Tanya Tani copilot → exporter PDF (keep GeoJSON) →
polygon walk mode (keep GPS point) → coop photo review (keep verdict-only review).

## 4. Demo choreography (10-minute slot, "dirty stopwatch")

- Laptop pre-booted, HDMI/USB-C dongle tested, demo tabs pre-opened, phone mirrored or camera'd.
- One rehearsed reset script that re-seeds the database in <30 s between rehearsals.
- QR of the verify page printed LARGE on paper — judges scan from their seats.
- Amoy explorer tab open showing the anchor transaction.
- If Wi-Fi dies: phone hotspot is pre-paired with the laptop; offline capture continues live.

## 5. Submission artifacts (before 10:00 WIB code freeze)

- Public GitHub repo (created ON Oct 10, first commit after 10:00) with honest commit history,
  README with architecture diagram + live URL + contract address.
- Live deployment URL (Vercel) + Amoy contract on the explorer — public network deployment is
  explicitly weighted above localhost.
- Slide deck PDF (≤ 50 MB) — build from the proposal's figures + pitch script section B.
