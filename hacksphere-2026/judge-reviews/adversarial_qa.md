# TANDATANI — Hostile Due-Diligence Panel: Adversarial Q&A, Integrity Scan, and Pre-emptive Plants

Panel stance: we assume the judges include (i) a Web3 architect who despises decorative blockchain, (ii) an Indonesian agribusiness/policy person who knows EUDR and e-STDB cold, and (iii) an investor who does arithmetic during your pitch. Verdict up front: the proposal is unusually well-armored (it pre-plants "Why Web3", names its own risks, and cites almost everything), but it has **one arithmetic self-contradiction a judge can find in 30 seconds (the SOM/ARR row), one over-claim that contradicts its own MVP (chain of custody), one crypto-design contradiction (did:key "rotation"), and one uncovered legal flank (PDP/GDPR never named)**. Fix those four before submission.

---

## 1. The 12 Hardest Questions

### Q1 — "Why is this a blockchain product at all? A signed database with published keys does everything you showed."

**(a) The question as asked:** "The cooperative's Ed25519 signature already makes the passport verifiable offline, forever, with zero chain. Everything else is Postgres. What does the Polygon anchor add that a signature plus an RFC-3161 timestamp — or just publishing your Merkle roots on GitHub — doesn't? Be specific, or admit the chain is theater for the Web3 theme."

**(b) Proposal coverage — partial.** §3.3 pre-plants this well: *"A vendor's private database asks the importer to trust the vendor and every editor; a public anchor makes tampering detectable by anyone"* and *"Startups die; anchored hashes on a public chain do not."* But it never concedes that the signature does most of the verification work, and never names the one attack the anchor uniquely kills: **issuer backdating**. A sharp judge will force that concession and score whether the team makes it gracefully or flails.

**(c) Strongest answer (say it in this order):** "The signature proves *who* issued; the anchor proves *when*, against a clock nobody — including us and the cooperative — controls. Without it, an issuer could mint a passport *after* a RADD deforestation alert lands and slip it into history; an auditor five years out would have only our word. An RFC-3161 timestamp authority reintroduces exactly the trusted intermediary we're removing, and GitHub is a company that can rewrite history; a $0.001 Merkle anchor is 30 lines of Solidity, not the product — 95% of this system is deliberately boring Web2, which is the honest ratio."

**(d) Edit:** In §3.3 bullet 1, after *"…makes tampering detectable by anyone."* append: *"Concretely, it defeats backdating: a passport must exist before its anchor block, so evidence cannot be minted after a deforestation alert and inserted into history — the one guarantee no signature or private timestamp gives an auditor five years later."*

---

### Q2 — "Satellites verify pixels, not provenance. What stops the officer from mapping a clean plot while the coffee grows somewhere else?" (the oracle problem)

**(a):** "Ibu Sari can stand on any clean plot, tap the GPS button, and attach Pak Karim's name — while his actual trees are inside a protected forest two ridges away. Your satellite check will pass with flying colors because the *claimed* plot is genuinely clean. Where does ground truth ever enter your system?"

**(b) Proposal coverage — partial.** §5.6 GPS-spoofing row: *"Satellite cross-check, PostGIS overlap detection, geotagged photos, cooperative attestation — convergence, not trust."* Gap: this answers *spoofed coordinates*, not *truthful coordinates of the wrong plot*. The geotagged photos come from the same device that claims the location, so they are not independent. The proposal never admits that no remote system closes this gap, which is the concession the judge is fishing for.

**(c) Strongest answer:** "No remote system — not ours, not Koltiva's, not the EU's own checks — can prove which trees a bean grew on; EUDR itself relies on operator liability, not physics. What we do is make plot fraud *exclusive, bounded, and attributable*: PostGIS rejects overlaps so a clean plot can be claimed exactly once; harvest estimates cap the volume a plot can ever ship; and every attestation is signed by a named cooperative that stakes its own EU market access on it — when fraud surfaces, the audit trail shows who attested what, when, immutably. We convert an invisible lie into a signed, dated, prosecutable one."

**(d) Edit:** In §5.6, GPS row mitigation cell, append: *"; mock-location and EXIF cross-checks; every claim is exclusive (one plot, one passport) and signed — fraud is attributable to a named issuer, not anonymous."*

---

### Q3 — "Your passport proves the plot. Nothing proves the bag. Isn't your dossier a laundering machine with better paperwork?" (mass balance)

**(a):** "Your own §2.3 says 'one launderer can contaminate an entire container.' A coop with 500 verified passports can pour any neighbor's beans into the bags. Your Feature 5 lets the exporter 'pick verified passports into a batch' — pick! Nothing links physical coffee to those passports. You've automated the fig leaf."

**(b) Proposal coverage — GAP, and worse, an internal inconsistency.** The proposal *names* the problem (*"Chain-of-custody fraud. Collection points mix compliant and non-compliant lots… one launderer can contaminate — legally and reputationally — an entire container.27"*) and even *claims custody as differentiation* in the §3.5 table (*"identity, credentials, chain of custody, offline Bahasa UX do not"*) — but no MVP feature performs any custody function. A judge who reads both passages wins the exchange before you open your mouth.

**(c) Strongest answer:** "Plot-level evidence is the binding EUDR requirement and our v1 scope — but we do close the crudest laundering vector: the DDS Studio refuses any batch whose tonnage exceeds the summed harvest estimates of its passports, so over-claiming a plot becomes arithmetically visible instead of invisible, and every batch composition sits in an append-only log an auditor can replay. Full physical custody — weigh-slips at collection points, lot-level transfers — is season-two roadmap, and honestly no software vendor closes it without hardware at the weighbridge. We chose to be truthful about that line rather than sell it."

**(d) Edits (two, both required):**
1. §4 Feature 5, after *"pick verified passports into a batch;"* insert: *"a volume-plausibility gate blocks any dossier whose tonnage exceeds the summed harvest estimates of its passports — over-claiming a plot is arithmetically visible;"*
2. §3.5 table, last row, change *"identity, credentials, chain of custody, offline Bahasa UX do not"* → *"identity, attestation, credential lifecycle, volume-bounded dossiers, offline Bahasa UX do not"*. (Do not claim custody the MVP doesn't build — a judge will quote you to yourself.)

---

### Q4 — "You chose did:key — which cannot rotate — and your risk table promises 'key rotation.' Which is it? And walk me through the day a cooperative's laptop is stolen."

**(a):** "did:key IS the key; the spec has no rotation — a new key is a new identity, orphaning every issued credential. Your mitigation cell says 'Key rotation + re-issuance.' That's a contradiction. And compromise is worse than the 'loss' your table names: a thief mints perfectly valid passports for park-cleared land, signed by a trusted coop. What exactly happens on day one?"

**(b) Proposal coverage — partial and self-contradictory.** §5.6: *"Key rotation + re-issuance; credential status registry; custody handbook (roadmap: social recovery)"* vs. Feature 3 / §6.2: *"did:key (Ed25519)"*. A judge who knows DIDs sees the contradiction; the table also says "Cooperative key **loss**" and never says **compromise**.

**(c) Strongest answer:** "did:key is the right zero-infrastructure choice for a 24-hour build, and we accept its trade-off knowingly: 'rotation' for did:key means a fresh DID plus automated re-signing of affected credentials, and production issuers migrate to did:web where rotation is native. Compromise is contained by the anchors themselves — every legitimate passport was anchored before the reported-compromise block, so verifiers can automatically distrust anything anchored after it, and a Bitstring status list revokes the issuer's outstanding credentials in one write. The stolen key can forge nothing into the past; that is precisely what the chain is for."

**(d) Edit:** §5.6, replace the mitigation cell with: *"Compromise, not just loss: anchored timestamps partition pre-/post-compromise issuance; Bitstring status-list revocation; re-issuance under a fresh DID (did:key has no in-place rotation — production issuers move to did:web); custody handbook (roadmap: social recovery)."* Also change the risk label *"Cooperative key loss"* → *"Cooperative key loss or theft"*.

---

### Q5 — "Whisp is a free FAO service sitting on an Earth Engine batch queue. You have no SLA. What do the judges see if it's down at hour 23?"

**(a):** "What is Whisp's measured p95 round-trip? What's your GFW API quota? And if both are degraded during the pitch — a Tuesday afternoon for Google infrastructure — do we watch a spinner, or do you quietly swap in canned output and hope we don't ask?"

**(b) Proposal coverage — largely answered, best-prepared area.** §6.4: *"Whisp jobs are asynchronous (Earth-Engine-backed): we submit early, poll, and keep GFW as an independent evidence track — either alone yields a verdict."* §4: *"a cached verification fixture exists only as an offline-resilience aid and would be labeled as such on screen, never presented as live output."* Remaining gap: no measured latencies or quotas, and it never states the obvious pro move — pre-submitting the seeded demo plots at hour 0.

**(c) Strongest answer:** "Three rehearsed rungs: GFW's synchronous Data API feeds the identical deterministic scorer if Whisp queues; the seeded Gayo demo plots are submitted at hour zero, so their verdicts are in hand long before the pitch and only the judge's *new* test polygon rides live infrastructure; and if everything external dies on stage, the screen shows a fixture labeled CACHED in the UI — our cut-not-fake rule means we'd rather show you an honest cache than a fake live call. Rehearsal-measured round-trips go in the repo README before the clock starts."

**(d) Edit (small):** §6.4 first bullet, append: *"; demo-dataset verdicts are fetched at hour 0 so the pitch never depends on a live third-party queue, and rehearsal-measured round-trip times are pinned in the repo README."*

---

### Q6 — "A farmer's name plus a plot polygon is personal data. Where are Indonesia's PDP Law and GDPR in this document? Where is consent? Who is the controller?"

**(a):** "A smallholder's plot is his home address. You collect it, ship it to EU importers inside dossiers, and hash it onto a permanent public chain — and neither UU PDP 27/2022 nor GDPR appears once in your proposal. Also: you say 'private by design' and 'anyone can scan a QR' in the same document. Which is it?"

**(b) Proposal coverage — GAP.** The *architecture* is defensible (§3.1: *"The chain carries only salted hashes — never coordinates, never names"*; §6.3: *"Postgres under row-level security… Salted hashing defeats rainbow-matching"*) but neither statute is named, there is no consent capture, no controller/processor analysis, and the QR-vs-privacy tension is unaddressed. At an Indonesian university, expect the PDP question by name.

**(c) Strongest answer:** "On-chain we are erasure-compatible by construction: only salted hashes ever touch the chain, so deleting the off-chain record and its salt is cryptographic shredding — nothing personal persists. Off-chain, consent is captured in Bahasa at enrollment and stored inside the evidence bundle; the cooperative is the data controller of member data, we are the processor under UU PDP 27/2022, and coordinates leave the system only inside a due-diligence submission that EUDR legally requires — a lawful basis both regimes recognize. The QR verifies by holder presentation: it proves the integrity of what the holder chooses to show; it publishes nothing."

**(d) Edit:** §6.3, add a fourth bullet: *"▪ Lawful by design: informed consent captured at enrollment (Bahasa, recorded in the bundle); cooperative as data controller, TandaTani as processor under Indonesia's PDP Law (UU 27/2022) and GDPR; salted on-chain hashes make erasure requests satisfiable by deleting the off-chain record and salt (crypto-shredding). The public QR verifies holder-presented data — it publishes nothing."*

---

### Q7 — "Koltiva has 1.9 million producers and a decade of Indonesian field operations. You have zero users and, from this team sheet, zero Indonesians. Why does the second exporter pick you?"

**(a):** "Your moat is a licensing philosophy. Koltiva has boots, contracts, and government relationships. And your team page lists a leader from India and two literal placeholder members. Who on this team has spoken Bahasa to a single Gayo cooperative? Why would they trust you with their members' data?"

**(b) Proposal coverage — partial on competition, GAP on team credibility.** §5.6: *"Copying farmer-owned portability breaks their enterprise custody model — our wedge is their conflict"* and the §3.5 USP paragraph are good. But the team table contains *"‹member 2 name›"*, *"‹institution — fill before export›"* — and no Indonesia connection anywhere. At President University this is the most dangerous non-technical question in the room.

**(c) Strongest answer:** "Koltiva's own published number is our market map: after a decade of enterprise deployment they state only ~1% of Indonesian smallholders meet EUDR requirements — the per-farmer-paid-by-a-brand model structurally cannot reach the long tail, and we sell to the two actors it skips: cooperatives facing Fairtrade's January-2027 geodata deadline and mid-tier exporters, at €45 a shipment — a price that wouldn't cover a Koltiva onboarding call. Passports are also complementary, not substitutive: any Koltiva-served brand can verify our credentials for free, which grows our network instead of theirs. On the ground: [name the Indonesian teammate / advisor / the two cooperatives you will interview in week one — this sentence must be true, and it must exist]."

**(d) Edit:** (1) Fill every ‹placeholder› before export — submitting a template is a credibility wound no answer repairs; recruit at least one Bahasa-speaking member if at all possible. (2) If (and only if) true, append to §5.1 bullet 1: *"Validation plan, week one: structured interviews with two Gayo cooperatives and one exporter to pressure-test the officer workflow before the final."*

---

### Q8 — "EUDR has been postponed twice and Brussels keeps sanding it down. It slips to 2028 — what's left of this company?"

**(a):** "Your entire urgency narrative is '30 December 2026.' The EU has blinked twice; Parliament keeps trying to gut it. If in November they delay again or carve out smallholder origins, your deadline evaporates and your €45 dossier SKU with it. What survives?"

**(b) Proposal coverage — answered, adequately.** §5.6: *"Possible — it slipped twice4 | Passports also serve Fairtrade Jan-2027, e-STDB, ISPO and buyer programs — the wall has many bricks24,34."* Thin (one row) but correct. The stronger card is already in §2.4 and unplayed: the +72% front-loading.

**(c) Strongest answer:** "Three deadlines survive any Brussels delay: Fairtrade's January-2027 geodata mandate on certified coops — our actual beachhead users; the government's own e-STDB drive, which now invites third-party collectors; and buyer sourcing programs that already demand plot data contractually. The 2024 delay is our evidence, not our risk: buyers responded by front-loading EU-bound Indonesian coffee +72%, not by relaxing data demands — the market is now the enforcer. A slip costs us one SKU for two quarters; the registry and coop licenses don't move."

**(d) Edit:** §5.6 EUDR-slip mitigation cell, append: *"; the 2024 delay did not slow buyer data demands — EU-bound shipments +72% on preparedness28."*

---

### Q9 — "Standard risk means 3% of operators get checked. Rational actors ignore 1-in-33 audits. Is the pain even real?"

**(a):** "You proudly quote 'standard risk — 3% of operators checked.' That's a rounding-error enforcement probability. Why would an exporter pay you €45 per dossier to hedge a lottery ticket?"

**(b) Proposal coverage — partial.** §2.1: *"Indonesia is benchmarked 'standard risk' — meaning real checks on 3% of operators, not a waiver.13"* — names the number but never defuses it. The defusal exists implicitly in §2.1 (the DDS obligation) and §2.4 (exclusion, not discount) but is never connected.

**(c) Strongest answer:** "Three percent is the *ex-post audit* rate, not the compliance rate: 100% of shipments must carry a due-diligence-statement reference in the customs declaration or the goods do not enter the Union — a lot with no plot geolocation can't even be filed, audited or not. And the binding enforcement isn't Brussels, it's the buyer: importers facing fines floored at 4% of EU-wide turnover push the data requirement upstream contractually, which is why compliant robusta already clears +$50/t while non-compliant lots aren't discounted — they're excluded. It's a gate, not a lottery."

**(d) Edit:** §2.1, after *"not a waiver.13"* append: *"The 3% is an ex-post audit rate; the due-diligence statement itself — plot geolocation included — is a precondition of customs entry for 100% of shipments.3"*

---

### Q10 — "46.8% digital adoption, mountain villages, 2,000-member coops. Who physically walks 8,000 plots, and who pays for the walking?"

**(a):** "Ketiara: 2,000+ members, 19 villages. Call it 15 plots per officer-day — that's 130+ field-days per cooperative before one passport exists. Your Rp 25k per member doesn't buy a motorbike's petrol. Whose budget is the fieldwork?"

**(b) Proposal coverage — partial.** §5.6: *"Cooperative-officer-assisted capture; offline PWA; Bahasa-first; voice roadmap"*; §5.1: officers are *"digitally literate professionals mapping member plots by hand today.22"* The design answer (officer-mediated, not farmer-direct) is correct and present; the *throughput and cost* math is absent, and a judge who runs it will imply you haven't.

**(c) Strongest answer:** "The walking is already happening and already paid for — our cite 22 is a Gayo cooperative walking member plots by hand right now, and Fairtrade's 2027 mandate obliges every certified coop to do it with or without us. We don't create the fieldwork; we make each visit *terminal*: one capture yields EUDR, Fairtrade, and e-STDB evidence simultaneously instead of three separate campaigns, offline, so one officer clears a village without connectivity planning. Rp 25k prices the registry, not the labor — the labor is the coop's existing compliance cost, cut from three passes to one."

**(d) Edit:** §5.1 bullet 1, append: *"(≈130 officer-field-days for a 2,000-member coop at 15 plots/day — fieldwork these coops already perform manually for Fairtrade; TandaTani makes one visit serve EUDR, Fairtrade and e-STDB at once)."*

---

### Q11 — "Your own SOM math comes to ~US$22k. You wrote US$60–90k ARR. Which number is fiction?"

**(a):** "200 containers × Rp 800k ≈ US$9–10k. 8,000 members × Rp 25k ≈ US$11–12k. Total ≈ US$20–22k — against your printed '≈US$60–90k ARR.' Either your price is 3× higher than you told the farmers' coops, or your ARR is 3× lower than you told us. Which?"

**(b) Proposal coverage — INTERNAL CONTRADICTION.** §5.2: *"SOM — 12-month beachhead: Gayo coffee | 3 cooperatives · ≈8,000 member plots · 2 exporters · ≈200 EU-bound containers | ≈US$60–90k ARR"* is irreconcilable with §5.3's own prices (*"Rp 800k (≈ €45) per due-diligence dossier"*, *"Rp 25k (≈ €1.40) per member per season"*). This is the single most dangerous line in the document: it hands a hostile judge a calculator kill.

**(c) Strongest answer (if asked before you fix it):** "You're right — dossiers plus registry fees alone are ≈US$22k, and that's the floor we defend; the band assumed the two exporters on flat season licenses and per-plot e-STDB collection fees under Ditjenbun's third-party program, which we failed to itemize. We'd rather stand on a transparent $22k floor with sub-$1k infrastructure cost than an unexplained $80k. The point of the SOM is not the size — it's that the first paying exporter covers the entire cost base."

**(d) Edit — MUST FIX:** Replace the SOM size cell with: *"≈US$20–25k ARR floor (200 dossiers × €45 + 8,000 members × €1.40); ≈US$60–90k with exporter season licenses and per-plot e-STDB collection fees24 — arithmetic shown"* — and make sure the season-license and e-STDB fee assumptions are actually stated somewhere. Never print a revenue number the pricing on the same page can't reproduce.

---

### Q12 — "Strip the story: you're a UI on FAO's free Whisp API. A consultant with the GeoJSON template replicates you in an afternoon."

**(a):** "Whisp: free. GFW: free. The TRACES GeoJSON spec: public. Gemini: free tier. What in this stack is *yours*? What couldn't a competent intern rebuild in a week — and since Whisp does the only hard part, why do you deserve €45?"

**(b) Proposal coverage — partial.** §3.5 last table row: *"Free public tools — Whisp, GFW, TRACES, Fairtrade Plot Insights | Free | Analysis and filing exist — identity, credentials, chain of custody, offline Bahasa UX do not."* Right instinct, but it (i) over-claims custody (see Q3), and (ii) never confronts the wrapper accusation head-on.

**(c) Strongest answer:** "Whisp answers exactly one question — 'is this polygon risky?' — for someone who already has a correct polygon; our whole product lives upstream and downstream of that call: extracting a true polygon from an offline mountain village, binding it to an accountable human attestation, keeping the evidence portable across buyers and verifiable through a five-year audit, and compiling 8,000 of them into a dossier an importer accepts. The intern's afternoon of Whisp calls yields a spreadsheet the importer must take on faith and redo every season; a passport is verified once and reused by every later buyer — the asset is the attested registry, and it compounds. Treating the raster math as a commodity isn't our weakness; it's the design — FAO explicitly built Whisp for others to build the trust layer on."

**(d) Edit:** Apply the Q3 table-cell fix, and in §3.4 append one sentence: *"Whisp is deliberately our commodity layer: the defensible asset is the attested, portable registry of evidence — not the raster math, which we refuse to rebuild worse than FAO built it."*

---

## 2. Integrity Scan — claims a judge can fact-check or turn against you

Ordered by damage potential. Quotes are exact.

1. **[FATAL if unfixed — internal arithmetic]** *"≈US$60–90k ARR"* (§5.2 SOM row) vs. *"Rp 800k (≈ €45) per due-diligence dossier"* and *"Rp 25k (≈ €1.40) per member per season"* (§5.3). Itemized: 200 × €45 + 8,000 × €1.40 ≈ €20.2k ≈ **US$20–22k** — a 3–4.5× gap inside two adjacent sections. Fix per Q11(d).

2. **[Internal contradiction]** §3.5 claims the free-tools gap TandaTani fills includes *"chain of custody"*, and §2.3 warns *"one launderer can contaminate — legally and reputationally — an entire container.27"* — yet no MVP feature performs custody; Feature 5 is *"pick verified passports into a batch"*. Fix per Q3(d).

3. **[Contradicts the chosen tech]** §5.6 mitigation *"Key rotation + re-issuance"* vs. §6.2/Feature 3 *"did:key (Ed25519)"* — did:key has no rotation; the key is the identifier. Fix per Q4(d).

4. **[Checkably overstated]** *"two orders of magnitude below today's €800-per-day consultants11"* (§1). €45 vs €800 is **17.8× — 1.25 orders of magnitude**. It only reaches ~100× against the €4–5k SME first-year figure in the same source. Fix: either say *"a twentieth of one consultant day"* or re-anchor: *"two orders of magnitude below a first-year SME compliance bill (≈€4–5k11)."*

5. **[Two numbers, same fact, four lines apart]** *"99.3% of Indonesian coffee is grown by smallholders on 0.5–2 ha plots1,14"* (stat box) vs. *"1.63 million farming households work 98.1% of the coffee area.1"* (§2.2 text), with cite 28 adding *"98% smallholder area"*. Probably production-share vs area-share — but unlabeled, it reads as sloppiness. Fix: label one *"of production14"* and the other *"of area1"*, or use 98.1% everywhere.

6. **[Likely factual error, locally checkable]** *"an EU Geographical Indication since 2010"* (§5.1, re Gayo). 2010 is the **Indonesian** GI registration for Gayo arabica; EU protection came years later (PGI route/CEPA GI lists). An Indonesian coffee-sector judge may know this cold. Fix: *"an Indonesian Geographical Indication since 2010, with EU-side GI protection following"* — or drop the year.

7. **[Overbroad absolute]** *"No incumbent offers this; their records live in the paying client's silo.30"* (§3.1) — your own §3.5 table lists Fairfood Trace, open-source and Hedera-anchored; one counterexample kills an absolute. Fix: *"No commercial incumbent offers this…"* or *"None of the enterprise incumbents…"*.

8. **[Cite stretched across commodity and geography]** *"documented +US$50/tonne premium12"* (§1, §5.3, §5.5) — cite 12 documents **Vietnamese robusta**; the beachhead is **Gayo arabica**. Also §5.5's *"capturing the +US$50/t compliance premium12 at the farm gate rather than the trader's margin"* — nothing in the design ensures farm-gate capture; that's aspiration stated as mechanism. Fix: *"documented for Vietnamese robusta12 — the nearest liquid benchmark"*, and soften §5.5 to *"creating the conditions for the premium to reach the farm gate."*

9. **[Source meaning shifted]** *"Only 46.8% of Indonesia's 28.2 M farmers use any digital technology;26"* — the BPS/ANTARA source (46.84%) covers use of *"modern machinery and digital technology"* (alsintan modern **dan** teknologi digital); "any digital technology" is not what the census measured. Fix: *"use modern agricultural machinery or digital technology (BPS Census 2023)26."*

10. **[Internal 10× inconsistency, trivial but circleable]** *"≈ $0.001 per thousand plots9"* (§1, §6.3 → $0.000001/plot) vs. *"$0.00001 anchoring"* per plot (§5.3). Both negligible, but they disagree by 10× and cite 9 (a gas tracker) supports the gas price, not the computed per-plot claim. Fix: compute once, use everywhere, and mark cite 9 as "gas price; per-plot figure is our calculation."

11. **[Self-undermining headroom math]** *"Free-tier LLM limits (Gemini: 250 requests/day31) exceed demo load ≈50×"* (§6.4) implies a **5-call demo day** — inconsistent with a *"seeded Gayo demo dataset"*, live judge QR scans, and the Tanya Tani copilot in the same document. Fix: state real expected load (e.g., "~60 calls against a 250/day cap, with Groq wired behind the same interface").

12. **[Stale by its own timeline]** *"covers just 0.03% of coffee farmers;5"* — cite 5 is a **Sept 2024** op-ed; the proposal's own cite 24 (Aug 2026) says Ditjenbun is now accelerating via third parties. Two-year-old coverage data presented as current. Fix: *"as of the latest published Ministry figures (Sept 2024)5"* — the number remains devastating with the date attached, and the date protects you.

13. **[Cite composition problem]** *"up to US$7 billion of exports2"* — your own reference [2] itemizes *"CPO-to-EU ≈US$3.5B/yr, rubber ≈US$1B, furniture ≈US$0.6B"* — which (i) sums to ≈$5.1B and (ii) includes **furniture**, not a TandaTani commodity, and not cocoa or coffee. "Up to" plus attribution saves you technically; a judge reading the footnote still scores it as inflation. Fix: *"up to US$7 B (CMEA headline; dominated by palm oil)2"*.

14. **[Absolute that your own text contradicts]** *"Nothing hardcoded, nothing mocked."* (§4) vs. *"a cached verification fixture exists…"* (§4, same section). You reconcile it with labeling, but never hand a judge an absolute sentence and its exception on the same page. Fix: *"Nothing presented as live that isn't — our only cache is labeled CACHED on screen."*

15. **[True but misleading in context]** *"smartphone GPS is accurate to ≤ 4.9 m in open sky36"* (Feature 1) — your flagship anecdote is parak **shade-canopy** agroforest (*"like a tidied forest"*), where consumer GPS degrades to 10–30 m; on 0.5 ha plots that's the difference between your plot and the neighbor's forest. Fix: Feature 1, append: *"Under canopy, the app surfaces the reported GPS accuracy radius, averages multi-fix captures, and flags low-confidence points for officer confirmation against Esri imagery."*

16. **[USP claim outrunning the mechanism]** *"The passport is a signed credential held for the farmer — not locked in our database. If … TandaTani itself disappears, the proof stays valid and verifiable."* (§3.1). "Held **for**" concedes custody: as architected, bundle and VC live in Supabase; validity survives your death but **availability doesn't** unless the farmer actually holds a copy. Fix: *"delivered to the farmer's device and exportable as a printed QR card holding the full credential; we retain only a backup copy"* — and make the printed-QR export real in Feature 3.

17. **[Housekeeping that reads as carelessness]** The submitted text contains literal template placeholders: *"‹institution — fill before export›"*, *"‹member 2 name›"*, *"‹member 3 name›"* etc. Fill or cut before any judge sees it.

18. **[Prep, not error]** *"Exporters click once for an EU-ready due-diligence dossier (TRACES GeoJSON)10"* — under EUDR the DDS is filed in TRACES by the **EU operator** (importer), not the Indonesian exporter. The phrasing is defensible ("EU-ready"), but rehearse the answer: importers push the data duty upstream contractually; the exporter who hands a complete dossier wins the contract. Optionally add *"(filed by their EU counterparty)"* after "dossier".

---

## 3. The 3 Questions to Plant and Answer Pre-emptively

These are the ones that end the pitch if a judge asks first and the team improvises. Plant each as a one-line Q&A (a boxed "Pertanyaan yang jujur / An honest question" sidebar works with the proposal's existing voice).

**Plant 1 — "The passport proves the plot. What proves the bag?"**
Devastating because §2.3 raises laundering and §3.5 currently over-claims custody — the trap is self-built. Planted answer: *"Nothing proves a bean's biography — not for us, not for anyone without isotope testing; EUDR itself binds operators by liability, not physics. What we guarantee: every plot claim is exclusive, every dossier is volume-capped by its plots' harvest estimates, and every attestation is signed, dated, and anchored — so laundering stops being invisible and starts being arithmetic. Physical custody (weigh-slips, lot transfers) is season two, and we say so."* (Requires the Q3 edits so the claim matches the build.)

**Plant 2 — "EUDR demands legality, not just forest cover. Most of these farmers have no land title — what goes in your 'legality documents' slot?"**
Devastating because satellite evidence covers only half the regulation, §3.1 lists *"legality documents"* without ever saying what they are, and the very statistic the proposal leads with (0.03% e-STDB) exists *because* formal tenure is rare. An agrarian-policy judge will see the hole instantly. Planted answer: *"We capture what exists — SKT/village letters, SPPT tax receipts, STDB applications — and the passport carries an explicit legality-status field rather than a pretense: 'documented', 'in process', or 'gap-flagged'. The gap itself is the state's to close, and Ditjenbun's third-party e-STDB program24 is the closing mechanism — every gap-flagged passport is a pre-filled e-STDB application, which is exactly why the Ministry wants this data. We make legality legible; we never fabricate it."*

**Plant 3 — "If TandaTani is dead in three years, what exactly does the farmer still hold, and how does anyone verify it?"**
Devastating because survivability is the load-bearing USP (*"if TandaTani itself disappears, the proof stays valid and verifiable"*) and, as currently architected, the credential and evidence bundle live in the company's Supabase — the claim collapses under one follow-up. Planted answer: *"Three artifacts outlive us: the credential itself on the farmer's device and on a printable QR card that embeds the full signed VC; the cooperative's public key, published in the credential and mirrorable by anyone; and the Merkle root on Polygon, which no one can take down. The verifier page is open-source and static — any party can host it, and verification needs no server of ours: signature check plus Merkle proof against a public chain. Our death would be inconvenient; it would not orphan a single passport."* (Requires the Q16-fix: device-local VC + printed QR export must actually be in Feature 3.)

---

## Priority edit list (if you fix only five things)

1. **§5.2 SOM row** — make the ARR reproducible from your own prices (Q11). A judge with a phone calculator must get your number.
2. **§3.5 table + Feature 5** — delete the custody over-claim; add the volume-plausibility gate (Q3).
3. **§5.6 key row** — resolve the did:key/rotation contradiction; add "theft," status list, did:web path (Q4).
4. **§6.3** — add the PDP/GDPR + consent + crypto-shredding bullet (Q6).
5. **Team table** — fill every ‹placeholder›; add the week-one validation sentence only if true (Q7). Exec summary: fix *"two orders of magnitude"* (scan #4).
