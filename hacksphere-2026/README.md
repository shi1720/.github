# 🌱 TandaTani — HACKSPHERE 2026 (Team ROOT ACCESS)

> **The farmer's signature, verified from space, sealed on-chain.**
> A verifiable Plot Passport for every Indonesian smallholder, so the EU Deforestation
> Regulation (live **Dec 30, 2026**) doesn't lock 1.6M coffee-farming families out of a
> US$7B export market.

This folder is the complete Phase 1 workspace: the submitted proposal, its reproducible build
pipeline, the research base behind every cited number, and the submission/Phase 2 kits.

## The idea in 30 seconds

EUDR requires plot-level GPS proof of deforestation-free origin for coffee, palm, cocoa and
rubber entering the EU. Indonesian coffee is 99% smallholder-grown, but the state registration
that records plot geolocation (e-STDB) covers **0.03%** of coffee farmers. TandaTani closes the
gap: a Bahasa-first offline mapping app → AI satellite verification (FAO Whisp + Global Forest
Watch) → a W3C Verifiable Credential **owned by the farmer** → Merkle-anchored on Polygon →
one-click EU TRACES dossiers for exporters → public QR verification for anyone. Free for
farmers; ≈ €45 per shipment for exporters (vs €800/day consultants); < $0.01 marginal cost per
verified plot.

## Repository map

```
hacksphere-2026/
├── proposal/
│   ├── ROOT ACCESS-TANDATANI-INTL.pdf   ← the Phase 1 submission (named per convention)
│   ├── ROOT ACCESS-TANDATANI-INTL.docx  ← same document, editable (official template, filled)
│   ├── content.py                       ← ALL proposal text + references (edit here)
│   ├── fill_docx.py                     ← template-filling engine (surgical OOXML edits)
│   ├── build.py                         ← runner: python3 build.py → rebuilds the .docx
│   ├── diagram_arch.html                ← architecture diagram source (SVG)
│   └── render_diagram.js                ← renders the diagram to PNG via Chromium
├── research/                            ← four sourced dossiers (≈240 cited URLs)
│   ├── research_indonesia.md            ← smallholder/commodity/EUDR-gap data
│   ├── research_competitors.md          ← Koltiva, Dimitra, Fairfood… + differentiation
│   └── research_tech.md                 ← every stack claim verified (free tiers, APIs, gas)
├── submission-kit/
│   ├── devpost.md                       ← copy-paste Devpost fields + compliance checklist
│   ├── pitch-video-script.md            ← verbatim 90-s video + 4½-min live-pitch scripts
│   └── phase2-playbook.md               ← pre-event keys/accounts, 24-h plan, demo choreography
└── judge-reviews/                       ← simulated judging rounds against the official rubric
```

## Rebuilding the proposal (e.g., after adding teammate names)

1. Edit the `CONTENT["cells"]` block in `proposal/content.py` (the `‹…›` placeholders:
   teammate names, emails, countries, institutions — and the leader's institution).
2. From `proposal/`: `python3 build.py` → regenerates the `.docx` in place.
3. Export the PDF: `soffice --headless --convert-to pdf "ROOT ACCESS-TANDATANI-INTL.docx"`
   (any Word/LibreOffice works — File → Export as PDF).
4. If the team has an Indonesia-resident member, the category is **MIX**: change the Team
   Category cell in `content.py`, set `OUT_NAME` to `ROOT ACCESS-TANDATANI-MIX`, rebuild.

Design notes: the pipeline edits the **official template's** XML directly, so all branding,
tables and the mandated 6-section anatomy are preserved; citations are auto-numbered
superscripts with a hyperlinked reference list generated from first use.

## Phase 1 rubric → where the proposal answers it

| Criterion (weight) | Where |
|---|---|
| Technical Architecture & Feasibility (30%) | §6 diagram + data flow + stack table; §4 hour-by-hour 24-h plan, fallbacks, cut-not-fake rule |
| Innovation & Value Proposition (25%) | §3 farmer-owned portable credentials, honest "why Web3", differentiation table, structural moat |
| Problem Relevance & Solution Fit (20%) | §2 fully data-driven (39 sources), field vignettes, cost-of-nothing analysis |
| Market & Impact Viability (15%) | §5 personas, bottom-up TAM/SAM/SOM, unit economics, risks table |
| Document Clarity & Structure (10%) | Official template, strict anatomy, references, typeset figures |

— Built by Team Root Access: Shivam Gupta and teammates, with heavy research, iteration and
judge-simulation passes to earn the win honestly.
