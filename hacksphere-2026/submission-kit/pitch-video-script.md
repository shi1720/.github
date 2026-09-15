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

### Q&A crib — the five answers to know cold

1. **"Why blockchain, not a database?"** — Three reasons: EUDR's 5-year record duty must survive
   any startup's death; an importer 10,000 km away must verify without trusting the vendor; and
   farmer credentials must stay valid if the farmer — or we — leave. A private database delivers
   none of the three.
2. **"How do you know the coffee in the bag came from that plot?"** — The passport certifies the
   plot and its capacity; harvest events are logged against it and anomaly-checked (volumes vs.
   plot capacity, PostGIS overlaps). Full physical chain-of-custody is roadmap — we say so; DDS
   liability stays with the exporter, and we make their evidence honest.
3. **"What if Whisp is down during your demo?"** — Two independent evidence tracks (Whisp + GFW);
   either alone yields a verdict. If the venue Wi-Fi dies, the offline-first design *is* the
   contingency.
4. **"Koltiva has 1.9M farmers. Why you?"** — Koltiva sells enterprise silos; the farmer is a
   data row. We sell per-shipment and the farmer keeps the credential. A structural wedge, not a
   feature war — copying it breaks their pricing.
5. **"EUDR delays again?"** — The same passport serves Fairtrade's Jan-2027 geodata mandate,
   e-STDB registration, ISPO, and buyer programs. The wall has many bricks; we sell the door.
