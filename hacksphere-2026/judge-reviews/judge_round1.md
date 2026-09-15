# HACKSPHERE 2026 — Phase 1 Judging, Round 1
## Proposal: TANDATANI — A Verifiable Plot Passport for Every Smallholder (Team ROOT ACCESS)

Panel: (J1) Indonesian CS lecturer — architecture & 24h feasibility. (J2) Startup mentor/VC — market realism & differentiation. (J3) Web3 practitioner — allergic to gratuitous blockchain. Scores merged. Graded against the official Phase 1 rubric, after ~40 proposals today. No curve for effort; only for what is on the page.

---

## 1. Per-criterion scores

### Technical Architecture & Feasibility — 80/100 (weight 30% → 24.0)
The three-plane hybrid (Web2 core / Web3 trust / AI verification) is coherent, the stack table justifies every choice, and the hour-by-hour 3-builder plan plus §6.4 failure-mode list is more engineering honesty than 95% of proposals show — J1 notes the on/off-chain boundary (32-byte Merkle roots only, salted hashes, relayer-paid gas) is textbook-correct. But the scope is at the outer edge of 24h sanity: four user-facing surfaces (farmer PWA, Cooperative Console, Exporter DDS Studio, public verify page) plus two external EO APIs, an LLM layer, a smart contract, VC issuance, Merkle batching, TRACES GeoJSON and a PDF generator — with only a 3-hour integration pass — and the plan's "3 builders" are undermined by a roster where two of the three are literally unnamed. §6.1's own numbering breaks causality (the cooperative reviews an "AI-annotated queue" at step 4, but the AI engine only appears at step 6, after VC issuance at step 5), and the "records outlive companies" claim is not architecturally closed: the on-chain root proves existence, but the evidence bundles it points to live in Supabase, so if TandaTani dies the hash survives and the evidence does not.

**Single change that would raise this score most:** close the survivability hole and the ordering error together — renumber §6.1 into true temporal order (capture → sync → integrity gate → AI evidence → review → VC issuance → anchor → dossier → verify) and add one sentence making the passport self-contained: "The passport is exported as a single signed file (VC + evidence hashes + Merkle proof) the farmer can download, print as QR, or hand to any buyer — verifiable against the chain even if TandaTani no longer exists."

### Innovation & Value Proposition — 76/100 (weight 25% → 19.0)
J3's gut reaction to "blockchain agri-traceability" is a 2018 eye-roll, and the proposal's own landscape table concedes Dimitra and Fairfood already do blockchain agri-trace — every individual component (Whisp, GFW, VC 2.0, Merkle anchoring, SIWE) is off-the-shelf, so the innovation is composition and business-model inversion, not new technology. That said, the inversion is genuinely sharp: farmer-owned portable credentials + per-shipment pricing + zero-trust in-browser QR verification is a real structural wedge the incumbents cannot copy without breaking their enterprise-custody revenue, and §3.3 is the best "why Web3, honestly" argument this panel has read today — restrained, specific, no token. The USP paragraph, however, buries its most novel element (anyone verifies the full proof chain with no account, no API, no trust in the platform) under the ownership argument, and absolutes like "No incumbent offers this" invite a rebuttal from Fairfood's open-source Trace.

**Single change that would raise this score most:** lead the USP with the zero-trust verification as the headline invention — one sentence of the form: "TandaTani is, to our knowledge, the first EUDR tool where the proof can be verified by anyone, in a browser, against a public chain, with the platform itself removed from the trust equation — the farmer owns the credential, and nobody has to believe us."

### Problem Relevance & Solution Fit — 90/100 (weight 20% → 18.0)
This is the strongest problem statement the panel has seen this cycle: a hard statutory deadline eleven weeks after the final, a quantified gap (0.03% e-STDB coverage vs 99.3% smallholder production, 15,054 certificates vs 2.4M households), US$7B of exposure, named field cases (Pasaman parak agroforests, Gayo Lues hand-mapping), and a government explicitly inviting third parties — all footnoted to 39 mostly-primary sources, several from August 2026. The solution maps onto the diagnosed bottlenecks (cost asymmetry, institutional throughput, custody, offline/Bahasa, chain-of-custody fraud) almost one-to-one, and the "proof-distribution problem" synthesis is a genuinely good framing. Two docked areas: EUDR has two evidentiary pillars — deforestation-free AND legality under Indonesian law — and the proposal verifies the first rigorously while "legality documents" merely ride along in the bundle unverified (which is precisely what e-STDB exists to establish); and the adoption chicken-and-egg (why does an exporter's compliance counsel accept a dossier from an unaccredited student platform?) is never confronted.

**Single change that would raise this score most:** add three sentences explicitly scoping the legality pillar — e.g., "Legality documents (SPPT, land letters) are captured, hashed and cooperative-attested in the bundle; TandaTani does not adjudicate land law — it packages the evidence the district office needs, which is exactly the third-party data-collection role Ditjenbun has opened. Full legality verification is the e-STDB partnership of §5.3, not a 24-hour claim."

### Market & Impact Viability — 80/100 (weight 15% → 12.0)
J2 credits real work here: bottom-up TAM/SAM/SOM, prices anchored to documented incumbent costs (€45/dossier vs €800–1,500/day consultants), sub-cent unit economics, a named beachhead (Gayo, Kopepi Ketiara, the Jan-2027 Fairtrade deadline as a second forcing function), a scalability argument with network effects, and a risk table that names its own kill conditions. But the SOM arithmetic does not survive a napkin: 200 containers × €45 ≈ €9k plus 8,000 members × €1.40 ≈ €11k comes to roughly US$22–25k, not the claimed "≈US$60–90k ARR" — at the stated prices the claim is ~3× the visible math, and an unreconciled revenue line poisons trust in every other number. There is also zero evidence of contact with any customer (no conversation, no LOI, not even "we emailed Ketiara"), and the state's own blockchain National Dashboard — framed as complementary — is equally plausibly the platform that subsumes this layer.

**Single change that would raise this score most:** show the SOM multiplication in one sentence and make it close — either lower the claim ("≈US$25–40k pilot-year revenue") or state the missing assumptions (dossiers per container > 1, two harvest seasons, coop-season licenses at Rp X) so the reader can reproduce US$60–90k.

### Document Clarity & Structure — 58/100 (weight 10% → 5.8)
The anatomy is exactly the mandated six sections, in order; the stat callouts, comparison tables, risk matrix and 39 references are the neatest apparatus in today's stack, and the writing is confident and largely jargon-free. Then page 1: "‹institution — fill before export›", "‹member 2 name›", "‹member 2 email›" — the identity block of the typeset, submitted PDF is an unfinished template, which is the most visible possible sloppiness, contradicts the "3 builders × 24h" plan and the "International (All Members)" category, and makes the eligibility of two-thirds of the team unverifiable. Beyond that fatal flaw: the Executive Summary is a single ~20-line wall of dense footnoted prose, and Figure 1's box labels are set so small and low-contrast that they are illegible at print size — the one figure judges will actually look at cannot be read.

**Single change that would raise this score most:** fill every ‹placeholder› field. Nothing else in this document — nothing — buys back more points per minute of effort.

---

## Weighted total

| Criterion | Weight | Score | Weighted |
|---|---|---|---|
| Technical Architecture & Feasibility | 30% | 80 | 24.0 |
| Innovation & Value Proposition | 25% | 76 | 19.0 |
| Problem Relevance & Solution Fit | 20% | 90 | 18.0 |
| Market & Impact Viability | 15% | 80 | 12.0 |
| Document Clarity & Structure | 10% | 58 | 5.8 |
| **TOTAL** | | | **78.8 / 100** |

With the placeholders filled and the SOM math fixed — two mechanical edits — this same content scores ≈ 84–86.

---

## 3. Top 8 weaknesses, ranked by (impact on total × ease of fix)

1. **Unfilled template placeholders in the team identity block (page 1).** Highest-impact, most trivially fixable defect in the document; it reads as "exported the draft by accident" and risks administrative rejection before scoring. **Fix:** fill all six ‹…› fields; if the team is genuinely still two people short, say so honestly and rewrite the execution plan for the real headcount — a 2-person plan that is true beats a 3-person plan that is fiction.

2. **SOM revenue math doesn't reconcile (~US$22–25k at stated prices vs claimed US$60–90k ARR).** One inconsistent number invites re-auditing of all 39 citations. **Fix:** add to §5.2: "SOM = 2 exporters × ~600 dossiers/yr (≈3 DDS per container across two harvests) × €45 + 3 coops × 8,000 members × €1.40 × 2 seasons ≈ US$76k" — or whatever the honest assumptions are; if they don't reach $60k, lower the claim.

3. **§6.1 data-flow numbering contradicts its own causality** (review of an "AI-annotated queue" at step 4; AI engine introduced at step 6, after VC issuance at step 5). A lecturer reads this as not understanding your own pipeline. **Fix:** renumber text and diagram chips to: ① capture ② sync ③ PostGIS gate ④ AI evidence + Gemini verdict ⑤ cooperative review ⑥ VC issuance ⑦ Merkle anchor ⑧ dossier ⑨ public verify.

4. **The "records outlive companies" claim is architecturally open.** On-chain roots prove existence, not availability; the bundles sit in Supabase. **Fix:** one sentence in §3.1 or §6.3: "Each passport exports as a self-contained signed file (VC + evidence hashes + Merkle proof) the farmer can download or print as QR — verifiable against the chain even if TandaTani disappears; batch bundles are mirrored to public storage."

5. **EUDR's legality pillar is hand-waved.** Deforestation-free is verified with rigor; "legality under Indonesian law" — the harder half, and the half e-STDB exists for — is a document upload. **Fix:** the three-sentence scope statement given under criterion 3 above; explicitly claiming the narrow role is stronger than silently implying the broad one.

6. **24h scope is over-committed with no declared cut order.** Five features, four surfaces, 3-hour integration buffer; the "cut-not-fake rule" exists but never says what gets cut first. **Fix:** add one line to §4: "Priority order if time slips: Tanya Tani copilot first, PDF dossier second (GeoJSON remains), Exporter Studio polish third; Features 1–4's capture→verify→issue→verify-publicly loop is the non-negotiable demo core."

7. **did:key cannot do the key rotation your own risk table promises.** §5.6 mitigates cooperative key loss with "key rotation + re-issuance," but did:key is derivationally bound to a single keypair — rotation means a new DID and mass re-issuance. J3 will ask this exact question in Q&A. **Fix:** either cite a credential-status registry + re-issuance under a successor DID as the actual mechanism (and drop the word "rotation"), or move cooperatives to did:web where rotation is real.

8. **Figure 1 is illegible and the Executive Summary is a wall.** The only diagram judges will study cannot be read at print size, and the opening paragraph asks a tired reader to hold 12 claims at once. **Fix:** give Figure 1 a full page (or landscape) with ≥7pt labels and ≥4.5:1 contrast; break the Executive Summary into three paragraphs — problem+deadline / mechanism / economics+scope-honesty.

---

## 4. Disqualification risks & red flags

- **Administrative/DQ — incomplete submission fields.** ‹institution — fill before export›, ‹member 2/3 name/email/country/institution› in the final PDF. If HACKSPHERE rules require complete team data in Phase 1 (they almost always do), this can be rejected unscored, and "Team Category: International (All Members)" cannot be verified for members who do not exist on paper. This is the single existential risk in the document.
- **Mocked-demo exposure.** The proposal's own §4 admits "a cached verification fixture exists" for offline resilience. The disclosure and labeling pledge ("would be labeled as such on screen, never presented as live output") is the right instinct and pre-empts the violation — but it is now on record: if any judge sees a cached verdict without the on-screen label during the final, the proposal's own text becomes the prosecution's exhibit. Keep the label large, and rehearse never showing the fixture unprompted.
- **Overclaiming watchlist (Q&A ammunition, not violations):** "defensible in an audit five years later" is a legal conclusion no prototype can promise; the +US$50/tonne premium is Vietnamese robusta data applied to an Indonesian Arabica beachhead (attributed, but a judge may poke); "No incumbent offers this" is an absolute that Fairfood's open-source Trace partially dents; "everything… live, nothing hardcoded" is a promise that converts any demo hiccup into a credibility event — the team has deliberately raised its own bar, which is admirable and dangerous.
- **Not a red flag (noted for the record):** Web3 use is justified, restrained, and token-free — this proposal would *pass* the gratuitous-blockchain screen that kills a third of this field. Anatomy order matches the mandate exactly.

---

## 5. Verdict

- **Top 30 of ~120: YES — comfortably, provided it is not administratively bounced.** On content this sits in the top 5–10 of the field: the problem statement is likely the single best-evidenced document the panel will read, the Web3 justification is the honest exception in a sea of buzzwords, and the feasibility section anticipates the exact objections judges raise. The placeholders are the only thing that could keep it out of the Top 30, and they would do it before a single rubric point is awarded.
- **Top 3: plausible but not yet.** What separates it from the Grand Prize, specifically: (1) document hygiene — a Grand Prize proposal does not ship template placeholders on page 1; (2) one number that doesn't reconcile (SOM) in an otherwise forensic document; (3) no evidence of a single customer conversation — one sentence of validation ("we spoke to a Gayo cooperative officer on …") would outweigh three citations; (4) execution risk the paper cannot retire — Phase 1 promises five live integrations in 24h with unnamed builders, and the prize will be decided by whether the capture→verify→issue→public-QR-verify loop actually runs on a judge's phone; (5) the wow is buried — the zero-trust QR verification is a Grand-Prize-grade demo moment currently hiding in Feature 4's third sentence.
- Net: **78.8/100 as submitted; ~84–86 with two mechanical fixes; Grand-Prize-competitive only if the final-day demo lands the full loop live.**

---

## 6. Smallest changes, biggest gains — punch list

1. **Fill every ‹placeholder›** in the identity block and reconcile the roster with the "3 builders × 24h" plan. (Removes the DQ risk; +5–8 weighted points of restored credibility.)
2. **Show the SOM arithmetic in one sentence** so 2 exporters + 3 coops visibly produce the claimed ARR — or lower the claim. (Restores trust in every other number.)
3. **Renumber §6.1 and the diagram chips into true temporal order** (AI verdict before cooperative review before VC issuance). (Five minutes; removes the lecturer's biggest architecture objection.)
4. **Add the one-sentence self-contained-passport guarantee** (downloadable/printable signed file, verifiable without TandaTani existing). (Closes the biggest Web3 logic hole and completes the "outlives us" claim.)
5. **Split the Executive Summary into three short paragraphs and give Figure 1 a full page with legible labels.** (The two things every judge actually reads become readable.)

*Bonus if there is appetite for a sixth edit: the three-sentence legality-pillar scope statement (weakness #5) — it converts the proposal's largest silent gap into a stated design decision.*
