# Devpost Submission Kit — TANDATANI (Team ROOT ACCESS)

Everything to copy-paste into the Devpost form, plus the compliance checklist.
Deadline: **September 18, 2026, 23:59 WIB (GMT+7)** — the portal locks automatically.

---

## 1. Project name

```
TandaTani
```

## 2. Elevator pitch (short tagline — shown in the public gallery and used for Public Favorite voting)

```
The farmer's signature, verified from space. TandaTani gives Indonesia's 1.6M coffee-farming
families a free, farmer-owned "Plot Passport" — AI-verified against satellite forest data and
sealed on a public chain — so the EU's deforestation law (live Dec 30, 2026) doesn't lock them
out of a US$7B export market.
```

(If Devpost enforces a shorter limit, use: `A verifiable Plot Passport for every smallholder —
AI-verified, farmer-owned, sealed on-chain, EUDR-ready.`)

## 3. "About the project" (long description — visible to public voters)

```
🌱 THE WALL
On December 30, 2026, the EU Deforestation Regulation (EUDR) starts refusing coffee, palm oil,
cocoa and rubber that cannot prove — with plot-level GPS data — that it grew on land not
deforested after 2020. Indonesia's coffee is 99% smallholder-grown, yet only 0.03% of coffee
farmers hold e-STDB, the registration that doubles as their geolocation record. Up to US$7B of
exports are exposed. The farmers who never cut a tree are about to be treated as if they had.

✍️ THE SIGNATURE
TandaTani (tanda = mark, tani = farmer — an echo of "tanda tangan", a signature) turns any plot
into a cryptographically verifiable Plot Passport:

1. MAP — A cooperative officer maps a plot in minutes on a Bahasa-first PWA that works fully
   offline on low-end Android. One GPS tap for plots ≤ 4 ha (exactly what EU rules accept).
2. VERIFY — Our AI engine cross-examines the plot against official satellite evidence (FAO
   Whisp, JRC 2020 forest baseline, GLAD/RADD alerts) plus PostGIS overlap-fraud checks, then
   explains the verdict in plain Bahasa. AI narrates; evidence decides.
3. SIGN — The cooperative reviews and signs a W3C Verifiable Credential 2.0 the farmer owns
   forever — portable to any buyer, any platform. Not locked in anyone's silo, including ours.
4. SEAL — Evidence hashes are Merkle-batched and anchored on Polygon (≈ $0.001 per thousand
   plots). On-chain: salted hashes only. Never coordinates, never names.
5. SHIP — Exporters click once for an EU-ready due-diligence dossier (TRACES GeoJSON v1.5 +
   evidence pack). Anyone on Earth can scan the QR and verify the whole chain of proof —
   no account, no permission, no trust in us required.

💡 WHY IT WINS
Enterprise traceability platforms charge €10k–50k/year and keep farmer data in the client's
silo. Consultants bill €800/day. TandaTani is free for farmers, ≈ €45 per shipment for
exporters, and the farmer walks away owning the proof. Incumbents can't copy that without
dismantling their own business model.

🔧 HYBRID BY DESIGN
Web2 core (Next.js + Supabase/PostGIS) for speed and cost. Web3 trust plane (VC 2.0, did:key,
Polygon anchoring, SIWE) for proof and portability. AI plane (satellite convergence-of-evidence
+ Gemini in Bahasa) for verification at smallholder prices. Every component free-tier; every
feature scoped to run live, end-to-end, in the 24-hour final.

Made with respect for the people who grow our mornings. ☕
```

## 4. "Built with" tags

```
next.js, typescript, supabase, postgis, polygon, solidity, foundry, maplibre-gl,
verifiable-credentials, did, gemini, fao-whisp, global-forest-watch, vercel, tailwindcss, viem
```

## 5. Additional info section

- **Upload:** `ROOT ACCESS-TANDATANI-INTL.pdf` (verify the filename is EXACTLY this — naming
  convention `[TEAM NAME]-[PROJECT NAME]-INTL.pdf` for a Full International team).
- **Twibbon link field:** paste the Instagram post URL of a team member's Twibbon post
  (see checklist below).

---

## ✅ Compliance checklist (from the official guidebook — do all of these)

| # | Item | Status |
|---|------|--------|
| 1 | All 3 members have Devpost accounts and clicked **Join hackathon** | ☐ |
| 2 | Team = **exactly 3 members**, each registered in only 1 team, ages 15–25, active students | ☐ |
| 3 | Category check: all three reside **outside Indonesia** → INTL. If any member resides in Indonesia → rename the PDF to `ROOT ACCESS-TANDATANI-MIX.pdf` and set Team Category cell to "International (Mix)" (rebuild: edit `content.py`, run `python3 build.py`, re-export PDF) | ☐ |
| 4 | Every member joined the **Compsphere Discord** and renamed to `ROOT ACCESS - <Name>` (e.g., `ROOT ACCESS - Shivam Gupta`) | ☐ |
| 5 | Every member posted the official **Twibbon on Instagram**; copy one post's link for the submission | ☐ |
| 6 | Personal-info table in the PDF completed for all 3 members (names, emails, countries, institutions) — regenerate via `content.py` → `build.py` | ☐ |
| 7 | PDF < 10 MB (current build: ~0.8 MB ✓), opens correctly, hyperlinks work | ☐ |
| 8 | Project created on Devpost, all 3 members invited via **Manage Team** | ☐ |
| 9 | Elevator pitch + project details filled (they'll be public during Oct 1–10 voting) | ☐ |
| 10 | **Submit** before Sep 18, 23:59 WIB — the portal locks exactly then; aim for Sep 17 | ☐ |

> Phase 1 requires no video and no images on Devpost ("You are not required to fill it out").
> If you have 2 spare hours, a 60–90s video (script in `pitch-video-script.md`) strengthens the
> Public Favorite vote later — Top 30 project pages are shown publicly Oct 1–10.
