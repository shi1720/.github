# TandaTani — Pitch Scripts (read verbatim)

Two scripts: a 90-second video (optional for Devpost / Public Favorite voting) and the
4½-minute live pitch for Phase 2. Written for Shivam's voice — plain words, short sentences,
no jargon until it's earned. **Bold** = hit the word. `/` = short pause.

---

## A. The 90-second video

*(Open on: a cup of coffee. Or just you, holding one.)*

> This coffee started on a farm smaller than a football field, / somewhere in the highlands of
> Sumatra.
>
> On **December 30th, 2026**, the European Union starts refusing every bean that can't prove —
> with GPS coordinates — that its farm didn't touch a single tree after 2020.
>
> Here's the problem. / Indonesian coffee is **ninety-nine percent** grown by smallholders. And
> the government registration that records a farm's location? / It covers **zero point zero
> three percent** of coffee farmers.
>
> The farmers who never cut a tree / are about to be treated as if they had. / Up to **seven
> billion dollars** of exports are on the line.
>
> So we built **TandaTani**. / In Bahasa, *tanda* is a mark. *Tani* is a farmer. / Together —
> it sounds like *tanda tangan*. / **A signature.**
>
> A cooperative officer maps a farmer's plot in **minutes**, on a cheap Android phone, fully
> **offline**. / Our AI checks the plot against satellite forest data — the same official
> sources the EU trusts — and explains the verdict in plain Bahasa.
>
> Then the cooperative signs a **Plot Passport**: a credential the farmer **owns**. Not us. Not
> a corporation. / The proof is sealed on a public blockchain for a tenth of a cent, / and any
> buyer in Hamburg can scan a QR code and verify it — without trusting anyone. Including us.
>
> Farmers pay **nothing**. / Exporters pay about forty-five euros per shipment — instead of
> eight hundred a day for consultants.
>
> **TandaTani.** / The farmer's signature, / verified from space, / sealed on-chain. /
> Let's keep the people who grow our mornings / **in** the market.

*(~230 words ≈ 90 seconds at a calm pace.)*

---

## B. The Phase 2 live pitch (4½ minutes of the 10-minute slot)

Structure: 2 min setup allowance is separate; speak 4½ min; leave ~3½ min for Q&A.
Division for a Mix/International hybrid stage: onsite member does §1–2 (story + demo driving),
remote member does §3 (architecture), Shivam closes §4–5 (business + ask).

### 1. The wall *(45 s)*

> Judges — before this pitch ends, the EU will have imported about forty tonnes of Indonesian
> coffee. In **eighty days** — December 30th — every one of those bags needs plot-level GPS proof
> that it grew on land untouched since 2020. Ninety-nine percent of our coffee comes from
> smallholders. Their registration coverage is zero point zero three percent. That's not a
> compliance gap. That's a wall — between one point six million families and a seven-billion-
> dollar market.

### 2. The demo *(2 min — LIVE, on the public URL; phone on screen)*

> This is Ladang, our farmer app. Airplane mode — watch — **no signal**. I map Pak Karim's plot:
> one tap. Photo. Done. Now signal returns — it syncs.
>
> The AI engine just asked FAO's Whisp and Global Forest Watch one question: was this forest
> after 2020? Here's the verdict — in Bahasa — with the satellite evidence attached. And here's
> a plot I drew over a deforestation alert on purpose: **rejected**. The system can say no —
> that's what makes its yes worth money.
>
> The cooperative reviews, taps *Terbitkan* — and signs a **Plot Passport**, a W3C Verifiable
> Credential the farmer owns. Its hash just went into a Merkle batch anchored on Polygon —
> there's the transaction.
>
> Now the exporter: select passports, one click — an EU-ready TRACES dossier. And this QR —
> please, scan it with your own phones right now. Your browser is re-computing the hash and
> checking the chain. You are not trusting me. **That's the point.**

### 3. Why this architecture *(45 s)*

> Three planes. A Web2 core — Supabase, PostGIS — because speed and cost matter. An AI plane —
> official satellite datasets plus Gemini in Bahasa — because verification must cost cents, not
> eight hundred euros a day. And a Web3 trust plane — verifiable credentials, a public anchor —
> for exactly three honest reasons: records must outlive companies, proof must be checkable by
> strangers, and farmers must be able to **leave** with their data. Everything on-chain is a
> salted hash. Never coordinates. Never names.

### 4. The business *(40 s)*

> Farmers: free, forever — they are the network. Exporters pay about forty-five euros per
> due-diligence dossier — against consultants at eight hundred a day, enterprise platforms at
> ten to fifty thousand a year, and a fifty-dollar-per-tonne premium on compliant beans — one
> compliant container carries about nine hundred fifty dollars of that premium. Our marginal
> cost per verified plot is under one cent. And the incumbents can't copy us — farmer-owned,
> portable credentials would break their own lock-in model. Our wedge is their conflict.

### 5. Close *(20 s)*

> Tanda tangan means signature. For four hundred years, other people signed papers about what
> Indonesian farmers grow. TandaTani hands the pen back. / We're Team Root Access — and this
> passport is ready for its first real harvest. Terima kasih.

---

### Q&A crib — the nine answers to know cold
(Full 12-question adversarial dossier: `judge-reviews/adversarial_qa.md`.)

1. **"Why blockchain, not a database?"** — A signature proves *who* wrote a record; the public
   anchor proves *when* — no issuer can backdate a passport after a deforestation alert lands.
   Add EUDR's 5-year record duty (must survive any startup's death) and strangers verifying
   without trusting the vendor: a private database delivers none of the three.
2. **"The passport proves the plot — what proves the bag?"** — Honestly: nothing fully, and no
   remote system can. What we do: the Studio's volume-plausibility gate blocks any dossier whose
   tonnage exceeds its passports' summed harvest estimates — the launderer's math stops working;
   claims are exclusive (no overlapping plots) and signed, so fraud is attributable. Physical
   custody (bagging events, lot QR) is season-two roadmap, stated as such.
3. **"What if Whisp is down during your demo?"** — Two independent evidence tracks (Whisp + GFW);
   either alone yields a verdict. If venue Wi-Fi dies, offline-first *is* the contingency.
4. **"Koltiva has 1.9M farmers. Why you?"** — Koltiva's own number: only ~1% of smallholders
   meet EUDR requirements — the enterprise model skips the long tail by design. We sell to
   cooperatives and mid-tier exporters at a price below a Koltiva onboarding call, and the
   farmer keeps the credential. Copying that breaks their custody-and-pricing model.
5. **"EUDR delays again?"** — The 2024 delay itself triggered +72% buyer front-loading: buyers,
   not Brussels, now enforce the deadline. And the same passport serves Fairtrade Jan-2027,
   e-STDB, and ISPO. The wall has many bricks; we sell the door.
6. **"Standard risk = only 3% get checked. Is the pain real?"** — 3% is the *ex-post audit*
   rate. A valid DDS reference is a customs precondition for **100% of shipments**, and buyers
   facing 4%-of-turnover fines push the data burden upstream regardless. Exclusion, not
   discounts: mixing contaminates the lot.
7. **"Aren't you just a UI on free Whisp?"** — Whisp answers one question for someone who
   already holds a correct polygon. Everything upstream (offline capture, identity,
   attestation) and downstream (portable credentials, 5-year verifiability, TRACES dossiers)
   is the product. An intern's spreadsheet is redone every season; a passport verifies once and
   is reused — the attested registry compounds.
8. **"Farmer data privacy — GDPR? Indonesia's PDP Law?"** — Consent at enrollment; the
   cooperative is data controller, we are processor (UU 27/2022 + GDPR framing); coordinates
   sit under row-level security and are disclosed only inside the exporter's DDS; the chain
   holds salted hashes, so destroying a salt is a clean erasure path; the public QR shows a
   verdict, never coordinates or names.
9. **"If TandaTani is dead in 3 years, what does the farmer hold?"** — A self-contained signed
   file on their device and a printed QR card; verification needs only the credential, an
   open-source static verifier, and the public chain. Validity *and* availability survive us.
