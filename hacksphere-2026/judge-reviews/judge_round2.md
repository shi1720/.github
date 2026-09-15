# HACKSPHERE 2026 — Phase 1 Judging, ROUND 2 (Verification Score)
## Proposal: TANDATANI — A Verifiable Plot Passport for Every Smallholder (Team ROOT ACCESS)

Panel re-convened: (J1) Indonesian CS lecturer — architecture & 24h feasibility. (J2) Startup mentor/VC — market realism. (J3) Web3 practitioner. Same harsh standard as Round 1 (scored 78.8/100). Every claimed fix was checked against the revised text and against pages 1, 2, 7, 8, 10 and 11 of the typeset PDF; Figure 1 was audited at native resolution (5220×3237 px source) and at simulated print scale (300 DPI, 161 mm placed width).

**Standing assumption, per instruction:** the page-1 identity placeholders will be filled correctly before submission and are scored as if filled. Noted for the record: there are **seven** placeholder fields, not six — the ‹member 2/3 …› sets **plus the team leader's own Institution** ("‹institution — fill before export›"), which the team's own fix list did not mention. Also: the section headed "Member 1 Personal Information" holds the ‹member 2 …› placeholders (and "Member 2" holds ‹member 3 …›) — an off-by-one template labeling to map carefully when filling, and Builders 2/3 in the §4 table should receive initials at the same time.

---

## 1. Fix-by-fix verification (17 claimed fixes)

| # | Claimed fix | Status | Evidence |
|---|---|---|---|
| 1 | SOM arithmetic, visible math ≈US$33k | **LANDED** | §5.2 SOM row now shows the whole computation: "3 co-ops · 8,000 members × €1.40 × 2 harvest seasons + 2 exporters · 200 dossiers × €45 ≈ €31k → ≈US$33k ARR". It reconciles: 8,000×1.40×2 = €22,400; 200×45 = €9,000; sum €31,400 ≈ €31k ≈ US$33k at ~1.06. The claim was honestly **lowered** from US$60–90k rather than back-filled — the right call. Nit: the "·" separator ("3 co-ops · 8,000 members") could be misread as ×3 → 24,000 members; "8,000 members across 3 co-ops" would be unambiguous. |
| 2 | §6.1 reordered to true temporal order | **LANDED (text); diagram chips renumbered but two arrows mis-wired — see New Defects A** | §6.1 now runs ① capture ② sync + ST_Intersects gate ③ AI evidence + Gemini verdict ④ cooperative review ⑤ VC issuance ⑥ Merkle batch ⑦ anchor ⑧ dossier ⑨ public verify. AI now precedes review precedes issuance — the Round-1 causality break is gone. Chips 1–9 in Figure 1 follow the same sequence. |
| 3 | Executive summary in 3 paragraphs | **LANDED** | Page 2 shows three clean paragraphs: problem+deadline+gap / mechanism / economics+scope-honesty — exactly the Round-1 prescription. The zero-trust verification claim now closes paragraph 2 in bold ("…no account, no permission, and no trust in us"), surfacing the buried wow. |
| 4 | Self-contained downloadable/printable passport guarantee | **LANDED — but the strongest wording is in the diagram, not the body** | Figure 1's Plot Passport box: "**Held by the farmer, not the platform** — portable to any buyer, forever / **Downloads as a signed file + QR — verifies even if TandaTani is gone**." §6.3: "credential copies on the farmer's device and printable QR card." §3.1: "if TandaTani itself disappears, the proof stays valid and verifiable." Residual gap: no body sentence states the exported file **contains the Merkle proof + evidence hashes** (the mechanism that makes 'verifies even if we are gone' architecturally true), and no mirroring of batch bundles to public storage. The survivability hole is 90% closed; the closing sentence lives on the wrong page. |
| 5 | Legality-pillar scope statement | **LANDED, excellently** | §3.1 "Scope honesty — the legality pillar": satellites verify deforestation-free; legality evidence is structured, hash-sealed, checked for presence/consistency, attester recorded, "while authenticity verification remains with the issuing authorities… we do not replace that duty — we make it affordable to discharge." Bonus: this same sentence quietly answers Round-1's unasked "why would compliance counsel accept an unaccredited student dossier" — the exporter files under its own responsibility; TandaTani is evidence assembly, not certification. |
| 6 | Declared 24h cut order | **LANDED** | §4: "Declared cut order if time slips: Tanya Tani copilot first, PDF dossier second (TRACES GeoJSON remains), Exporter Studio polish third — Features 1–4 … the non-negotiable demo core." Verbatim the Round-1 ask. |
| 7 | did:key rotation contradiction | **LANDED** | §5.6 now reads: "Credential-status registry + re-issuance under a successor DID (did:key is single-keypair by design; roadmap: did:web for true rotation)." Grep confirms no stray "rotation" claim survives anywhere else. J3 withdraws the Q&A ambush. |
| 8 | Builder 1 named | **LANDED** | §4 table: "Builder 1 (S. Gupta) — Web3 / Infra" (page 7 confirms in print). Builders 2/3 remain role-only pending the roster. |
| 9 | Honest "no customer interviews yet" | **LANDED** | §5.1 "Validation, honestly stated: we have not yet interviewed a customer" + concrete pre-final plan (structured calls, named intro paths: WRI Sustainable Gayo Coffee network, Fairtrade producer support) + "we will report what we hear, including bad news, on stage." Second-best to an actual interview; first-class as honesty. |
| 10 | Volume-plausibility gate (chain-of-custody honesty) | **LANDED** | Feature 5: gate "blocks any dossier whose tonnage exceeds the summed harvest estimates of its passports — the launderer's math stops working" + append-only audit log. Directly answers the §2.3 fraud bullet. |
| 11 | PDP Law UU 27/2022 + GDPR bullet | **LANDED** | §6.3 "Privacy law, named": controller/processor roles assigned, consent at enrollment, RLS, salt-destruction as erasure path, QR page shows verdict never coordinates/identities. More than asked. |
| 12 | Magnitude precision "less than 6% of a single consultant-day" | **LANDED** | Exec summary: €45/€800 = 5.6% — true at the *low* end of the cited €800–1,500 range, so the claim is conservative and unimpeachable. |
| 13 | Production-vs-area labeling | **LANDED** | Callout: "99.3% of Indonesian coffee **production**"; body: "1.63 M households work 98.1% of the coffee **area**" (ref gives 98.14% area). Cocoa labeled production (99.8%), rubber labeled production ≈91% with area ≈85% in the reference, palm labeled area (40.6%). Consistent. |
| 14 | e-STDB data vintage (MoA July 2024) | **LANDED** | Callout: "(MoA, 2024)"; body: "(Ministry of Agriculture data, July 2024 — the latest published breakdown)". |
| 15 | GPS canopy accuracy honesty | **LANDED** | Feature 1: ≤4.9 m cited for **open sky**, live accuracy display under canopy, 10 m acceptance threshold, tap-on-imagery fallback. Exactly the honest formulation. |
| 16 | Anchoring-cost harmonization | **LANDED** | All five statements now mutually consistent: ~$0.001 per anchor transaction (45k gas, ref 9) = "≈$0.001 per thousand plots" (exec, §6.3) = "amortized ≈$0.000001/plot in 1,000-plot batches" (§5.3) = diagram batcher "≈$0.001 per batch"; the diagram Polygon box's "<$0.01 per anchor" is a consistent conservative bound. |
| 17 | Larger diagram fonts | **PARTIAL** | Figure 1 is dramatically better: near-black-on-white box text, white-on-navy headers, legible chips, readable at any screen zoom. But at placed print width (161 mm), box body text measures **≈4.5 pt equivalent** (cap height ≈1.1 mm at 300 DPI) — below the ≥7 pt Round-1 bar — and the figure still shares page 10 rather than taking a full page or landscape. Legible with effort on paper; fine on screen. |

**Tally: 15 landed clean, 2 partial (fixes 4 and 17), 0 failed, 0 fixes reverted anything.**

---

## 2. Round-2 scores (same harsh standard)

### Technical Architecture & Feasibility — 86/100 (was 80; weight 30% → 25.8)
Two of Round 1's three architecture objections are retired outright: §6.1 now states the pipeline in true causal order (and the exec summary's own narrative matches it), and the "records outlive companies" claim is now backed by a stated artifact — a downloadable signed file + printable QR that "verifies even if TandaTani is gone." The third objection — 24h over-commitment — is mitigated rather than removed: the declared cut order converts a hope into a plan, and S. Gupta is now accountable for the Web3/infra track, but four surfaces + two EO APIs + LLM + contract with two still-unnamed builders remains the outer edge of sanity. Held below 88 by the new finds: two Figure-1 arrows whose endpoints contradict their own chip semantics (Defect A) and the unreconciled reject-vs-score behavior of the overlap check (Defect B).

### Innovation & Value Proposition — 78/100 (was 76; weight 25% → 19.5)
The underlying innovation is unchanged — composition and business-model inversion, not new technology — so this cannot move much. What moved: the zero-trust verification is no longer buried; it now closes exec paragraph 2 in bold ("anyone, including the judges reading this, can scan a QR… no trust in us") and gets its own outcome box in the diagram ("Anyone can audit, forever"). The §3.5 USP paragraph, however, still leads with ownership rather than the zero-trust headline Round 1 recommended, and the absolute "No incumbent offers this" (§3.1) survives as Fairfood-shaped Q&A bait.

### Problem Relevance & Solution Fit — 92/100 (was 90; weight 20% → 18.4)
Already the best problem statement of the cycle; the revision fixed its one substantive gap. The legality-pillar scope statement is exactly what was asked and better written than the panel's own suggested text — it converts the largest silent gap into a stated design decision, and as a side effect partially defuses the adoption/accreditation objection (the exporter files under its own duty; TandaTani assembles evidence). The stat apparatus is now internally precise (production vs area, data vintages). What keeps it from 95: the exporter-counsel acceptance question is answered only implicitly, never head-on.

### Market & Impact Viability — 84/100 (was 80; weight 15% → 12.6)
The SOM now survives the napkin — the math is printed, closes to the euro, and the claim was lowered to ≈US$33k rather than defended: an integrity trade the panel rewards, because one reconciling number restores trust in the other thirty-eight citations. The customer-validation hole is now honestly declared with a dated, named plan and a report-bad-news-on-stage pledge — second-best to a single actual conversation, which is still absent. National-Dashboard subsumption risk remains framed as pure complementarity. Nit: "we price under 5% of the value we unlock" computes to ≈5.0% (€45 ≈ US$47.7 vs US$950/container) — say "≈5%".

### Document Clarity & Structure — 80/100 (was 58; weight 10% → 8.0)
**Conditional on the placeholder assumption.** The exec summary is three clean paragraphs; the SOM table, risk matrix and 24h plan print cleanly; Figure 1 went from illegible to high-contrast and screen-legible with correctly sequenced chips. Deductions: figure body text ≈4.5 pt at print size on a shared page; the two mis-wired chip arrows are also a layout defect; "held for the farmer" vs the diagram's "Held by the farmer" (Defect C). **If the seven ‹…› fields are NOT filled, this criterion reverts to ≈60 and the Round-1 administrative-DQ risk returns in full — the assumption is doing 2.0 weighted points of work in the total below.**

### Weighted total

| Criterion | Weight | R1 | R2 | Weighted |
|---|---|---|---|---|
| Technical Architecture & Feasibility | 30% | 80 | **86** | 25.8 |
| Innovation & Value Proposition | 25% | 76 | **78** | 19.5 |
| Problem Relevance & Solution Fit | 20% | 90 | **92** | 18.4 |
| Market & Impact Viability | 15% | 80 | **84** | 12.6 |
| Document Clarity & Structure | 10% | 58 | **80** | 8.0 |
| **TOTAL** | | **78.8** | | **84.3 / 100** |

84.3 sits inside the 84–86 band Round 1 predicted for exactly these fixes — the revision earned its points; nothing here is inflation.

---

## 3. New defects introduced (or exposed) by the edits

- **A. Figure 1 chips 6 and 8 ride the wrong arrows.** The renumbering was applied to the old arrow topology. The chip-⑧ arrow descends from Exporter DDS Studio and its arrowhead terminates on the **AI Verification Service** box (they share a column), so the diagram literally draws "Exporter Studio → AI engine" for the step defined as "Exporter composes passports → TRACES dossier"; the chip-⑥ arrow then emerges from the **AI box's bottom edge** into the Evidence Merkle Batcher, drawing "AI engine → Merkle batching" for "bundle hashes batch into a tree" (the true Passport → Batcher horizontal edge sits right there, unlabeled). The caption explicitly invites judges to match chips to §6.1 — a lecturer tracing arrows re-discovers the very "doesn't know its own pipeline" reading the team just paid to erase.
- **B. Reject vs score.** §6.1 step 2 and the diagram's Supabase box say the ST_Intersects gate "**rejects** duplicate and overlapping claims on arrival"; Feature 2 and §3.4 fold PostGIS overlap detection into the **fused risk score**. Hard gate or soft signal? Both may be true (exact duplicates rejected, partial overlaps scored) but no sentence says so.
- **C. Custody preposition wobble.** §3.1: "a signed credential held **for** the farmer"; diagram: "Held **by** the farmer, not the platform." In a proposal whose entire thesis is custody, the preposition is load-bearing — J3 will ask which it is.
- **D. Diagram overclaim on the 5-year duty.** TandaRegistry box: anchor "satisfies the EUDR 5-year record-keeping duty." §3.3 words it correctly (anchors persist; operators keep records); the anchor proves integrity/existence — it does not satisfy a record-keeping duty by itself.
- **E. Borderline arithmetic flourish.** "Under 5% of the value we unlock" ≈ 5.0% at current FX (see criterion 4).
- **F. Minor.** SOM "·" separator ambiguity (fix #1 nit); page 1 has **seven** placeholders including the leader's own Institution, with off-by-one section labels ("Member 1" section ↔ ‹member 2› placeholders); Builders 2/3 still initial-less in the §4 table; "ARR" applied to per-season + per-dossier revenue is loose usage.

---

## 4. The one remaining highest-leverage improvement (doable tonight, by editing the document)

**Regenerate Figure 1 with the chips on the correct edges — and take the free font win while the asset is open.** Concretely: route the chip-⑧ arrow from Exporter DDS Studio to the **API** box (or the platform band edge), not the AI Verification Service; move chip ⑥ onto the existing **Plot Passport → Evidence Merkle Batcher** horizontal arrow and delete the AI-box→Batcher vertical; while editing, bump box body text ~2 pt and consider giving the figure the full page. One asset, ~30 minutes, and it protects the single largest score gain of this revision: the §6.1 fix is currently contradicted by its own illustration on the one page every technical judge studies. (Runner-up, one sentence in §3.1: "Each passport exports as a single signed file — VC + evidence hashes + Merkle proof — the farmer can download or print as a QR card, verifiable against the chain even if TandaTani no longer exists." The diagram already says it; the body should too.)

---

## 5. Final verdict

- **Top 30 of ~120: YES — solidly, and no longer on content alone but on hygiene too, with the single condition that the seven page-1 placeholder fields are actually filled before submission, since that unfixed block remains the only thing that could bounce the strongest problem statement in the field before a rubric point is awarded.**
- **Top 3 potential: YES — now genuinely in contention on paper at 84.3, because the two "mechanical" blockers Round 1 named are resolved or scheduled and the honesty upgrades (lowered SOM, declared cut order, no-interviews confession, legality scoping) read Grand-Prize-grade; what decides it from here is not this document but whether the capture→verify→issue→public-QR-verify loop runs live on a judge's phone — and whether one real Gayo cooperative conversation happens before the final, as promised on page 8.**
