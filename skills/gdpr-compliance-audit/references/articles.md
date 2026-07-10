# GDPR Article Reference — Scope, Principles, Bases, Rights, Obligations

Use this file when you need the requirement detail behind an audit phase. Every finding you
emit must cite the specific article(s) from this file (or the quick-map at the bottom); if you
cannot tie a verdict to an article here, treat that as a signal to re-check the verdict.

Contents: Part 0 scope · Pillar A principles · Pillar B lawful basis · Pillar C rights ·
Pillar D transparency · Pillar E accountability · Pillar F security & breach · Pillar G
processors · Pillar H transfers · Article quick-map · Fine tiers.

---

## Part 0 — Scope: does GDPR even apply?

Before auditing *how* an organization complies, establish *whether* it must. Two tests, plus the actor question.

**Material scope (Art. 2).** GDPR governs processing of *personal data* wholly or partly by automated means, or manual processing of data that forms (or is intended to form) part of a filing system. "Personal data" (Art. 4(1)) is any information relating to an identified or identifiable natural person — directly or indirectly, including online identifiers, location data, and pseudonymized data (which is still personal data; only truly anonymized data falls outside scope). Excluded: purely personal/household activity, and law-enforcement processing (governed instead by the Law Enforcement Directive 2016/680).

**Territorial scope (Art. 3).** GDPR applies if either:
- The processing happens in the context of an EU/EEA establishment's activities (regardless of where the processing physically occurs), **or**
- The organization is outside the EU but (a) offers goods or services to people in the EU, or (b) monitors the behaviour of people in the EU.

This extraterritorial reach is real and enforced — non-EU companies have been fined under it. A US-only SaaS with EU users is in scope. Conversely, a company with **no EU/EEA data subjects at all is normally out of scope** — do not force a GDPR audit onto a purely non-EU scenario; say so and stop.

**EU representative (Art. 27).** An organization caught by Art. 3(2) *because* it is outside the EU but targets or monitors people in the EU must, in most cases, designate in writing a representative established in an EU member state where affected individuals are. The representative is the local contact point for supervisory authorities and data subjects. This obligation is frequently overlooked by exactly the non-EU companies most likely to trip the territorial-scope test, so it is a high-yield, easily-verified check: an in-scope non-EU controller with no named EU representative (and no Art. 27 exemption) is non-compliant on its face.

**Actor roles (Art. 4).** Correctly classifying each party is foundational, because obligations differ:
- **Controller** — determines the purposes and means of processing. Bears primary accountability.
- **Processor** — processes on the controller's behalf and instructions (e.g., a cloud host, a payroll vendor).
- **Joint controllers (Art. 26)** — two+ parties jointly determine purposes/means; must have an arrangement defining respective responsibilities.
- **Sub-processor** — a processor engaged by a processor.

*Audit implication:* a system can be non-compliant simply because roles were never mapped, so no one knows who owes what.

---

## Pillar A — Principles relating to processing (Art. 5)

These seven principles are the spine of the whole Regulation. Every downstream obligation is an operationalization of one of them, and infringing them attracts the **higher fine tier**. Principle 7 (accountability) is distinct: it requires being *able to demonstrate* compliance with the other six — this is what makes documentation legally load-bearing, not optional.

1. **Lawfulness, fairness, transparency** — processing needs a valid legal basis, must not be deceptive or unduly detrimental, and must be explained clearly to the individual.
2. **Purpose limitation** — data collected for specified, explicit, legitimate purposes; not further processed in ways incompatible with those purposes.
3. **Data minimisation** — adequate, relevant, and limited to what's necessary. Collecting "just in case" is a violation.
4. **Accuracy** — kept accurate and up to date; inaccurate data erased or rectified without delay.
5. **Storage limitation** — kept in identifiable form no longer than necessary. Requires defined retention periods and deletion mechanisms.
6. **Integrity and confidentiality (security)** — protected against unauthorized/unlawful processing, loss, destruction, or damage, via appropriate technical and organizational measures.
7. **Accountability** — the controller is responsible for, *and must be able to demonstrate*, compliance with 1–6.

## Pillar B — Lawful basis for processing (Art. 6, 9, 8, 10)

No processing is lawful without a basis. **Art. 6** provides six, and the controller must identify the specific one *before* processing and record it:

| Basis | Typical use | Watch-outs |
|---|---|---|
| Consent | Marketing, cookies, optional features | Must be freely given, specific, informed, unambiguous, and as easy to withdraw as to give (Art. 7). Pre-ticked boxes, bundling, and "consent walls" are invalid. |
| Contract | Fulfilling a service the person signed up for | Only covers what's *necessary* for the contract, not everything adjacent. |
| Legal obligation | Tax records, statutory reporting | Must point to an actual EU/member-state law. |
| Vital interests | Life-or-death (medical emergency) | Narrow; rarely the right basis outside emergencies. |
| Public task | Government / official authority functions | Sector-specific. |
| Legitimate interests | Fraud prevention, network security, some analytics | Requires a documented **Legitimate Interests Assessment (LIA)** balancing the interest against the individual's rights. Cannot be used by public authorities for their tasks. Under sustained regulatory scrutiny for ad-tech. |

**Special category data (Art. 9)** — racial/ethnic origin, political opinions, religious/philosophical beliefs, trade-union membership, genetic data, biometric data used for identification, health, sex life, sexual orientation. Processing is *prohibited* unless one of the Art. 9(2) exceptions applies (explicit consent, employment/social-security law, vital interests, etc.). This is a **second gate on top of** an Art. 6 basis, not a substitute.

**Criminal offence data (Art. 10)** — extra restrictions; generally needs official authority or specific legal authorization.

**Children (Art. 8)** — for information-society services offered directly to children on a consent basis, consent must be given/authorized by a parent below a member-state age threshold (13–16, varies by country). Requires reasonable age-verification efforts.

## Pillar C — Data subjects' rights (Art. 12–22)

Eight core rights, all subject to the **modalities in Art. 12**: responses generally within **one month** (extendable by two for complexity), free of charge in most cases, in clear and plain language, with identity verification.

1. **Right to be informed (Art. 13–14)** — proactive transparency at collection (see Pillar D).
2. **Right of access (Art. 15)** — confirmation of processing, a copy of the data, and supplementary information (purposes, recipients, retention, source, rights). The most-exercised right and the most-complained-about; a frequent enforcement topic.
3. **Right to rectification (Art. 16)** — correction of inaccurate/incomplete data.
4. **Right to erasure / "right to be forgotten" (Art. 17)** — deletion where data is no longer necessary, consent is withdrawn, processing was unlawful, etc. Not absolute (exceptions: legal obligations, freedom of expression, public-interest archiving).
5. **Right to restriction (Art. 18)** — "pause" processing while accuracy or lawfulness is contested.
6. **Right to data portability (Art. 20)** — receive data provided by the individual in a structured, commonly used, machine-readable format, and transmit it elsewhere. Applies only where basis is consent or contract *and* processing is automated.
7. **Right to object (Art. 21)** — object to processing based on legitimate interests/public task; **absolute** for direct marketing.
8. **Rights re: automated decision-making & profiling (Art. 22)** — not to be subject to solely automated decisions with legal/similarly significant effects, unless necessary for a contract, authorized by law, or based on explicit consent — and even then with safeguards (human intervention, right to contest).

**Downstream notification (Art. 19).** Coupled to rights 3–5: when a controller rectifies, erases, or restricts data, it must communicate that to *each recipient* the data was disclosed to (unless impossible or disproportionate), and tell the individual who those recipients are if asked. This is the mechanism that makes erasure and rectification actually propagate through the supply chain rather than stopping at the controller's own database — audit it alongside Art. 17/16, not as an afterthought.

*Audit implication:* rights are where "paper compliance" and reality most often diverge. A privacy policy can promise all eight while the organization has no actual mechanism, no defined SLA, and no staff trained to recognize a request that arrives by email or phone.

## Pillar D — Transparency & information obligations (Art. 12–14)

**This is the EDPB's coordinated enforcement priority for 2026** — expect it to be the highest-yield area for findings right now.

- **Art. 13** — information to provide when data is collected *directly* from the individual.
- **Art. 14** — information to provide when data is obtained *from another source*.

Required content includes: controller (and DPO) identity and contact; purposes *and the lawful basis for each*; legitimate interests where relied on; recipients or categories of recipients; **international transfers and the safeguard used**; retention period (or the criteria for it); the full list of data-subject rights including withdrawal of consent and the right to lodge a complaint with a supervisory authority; whether provision is a statutory/contractual requirement; and the existence of automated decision-making with meaningful information about the logic.

Recent enforcement raises the bar on specificity: several authorities now expect notices to **name each third country** to which data is transferred, not just say "outside the EU." Notices must be concise, transparent, intelligible, accessible, and in plain language (Art. 12) — dense legalese is itself a compliance failure.

## Pillar E — Accountability & organizational governance

Accountability (Art. 5(2)) is made concrete by a cluster of obligations that together form the organization's privacy governance:

- **Responsibility of the controller (Art. 24)** — implement appropriate technical and organizational measures, proportionate to risk, and be able to demonstrate them.
- **Data protection by design and by default (Art. 25)** — bake safeguards (e.g., pseudonymization, minimisation) into systems from the outset; default settings must be the most privacy-protective (e.g., no opt-in to sharing by default).
- **Records of Processing Activities — ROPA (Art. 30)** — an inventory of processing activities (purposes, categories of data and subjects, recipients, transfers, retention, security measures). Mandatory for organizations with 250+ employees, and effectively mandatory for smaller ones too whenever processing is not occasional, involves special categories, or risks rights. The ROPA is the backbone artifact of any audit.
- **Data Protection Impact Assessment — DPIA (Art. 35)** — required before processing likely to result in *high risk* (large-scale special-category processing, systematic monitoring of public areas, systematic profiling with significant effects, new technologies). Where a DPIA shows unmitigated high residual risk, **prior consultation with the supervisory authority (Art. 36)** is required.
- **Data Protection Officer — DPO (Art. 37–39)** — mandatory when the core activities involve large-scale systematic monitoring or large-scale special-category/criminal data, or for public authorities. Must be independent, adequately resourced, report to the highest management level, and not be penalized or have conflicting duties.
- **Codes of conduct & certification (Art. 40–43)** — voluntary mechanisms to demonstrate compliance.

## Pillar F — Security & breach management (Art. 32–34)

- **Security of processing (Art. 32)** — appropriate technical and organizational measures given the state of the art and risk: e.g., encryption, pseudonymization, confidentiality/integrity/availability/resilience, restoration after incidents, and a process for regularly testing effectiveness.
- **Breach notification to the authority (Art. 33)** — a personal-data breach must be reported to the supervisory authority **within 72 hours** of becoming aware, unless it's unlikely to risk individuals' rights. Requires an internal breach register regardless of reportability.
- **Breach communication to individuals (Art. 34)** — when the breach is likely to result in *high risk* to individuals, notify them without undue delay.

Breach-notification volumes hit record highs in 2025–2026, so this is an area regulators watch closely.

## Pillar G — Processors & the supply chain (Art. 28)

Controllers may only use processors giving sufficient guarantees, under a binding contract (a **Data Processing Agreement**) that includes the Art. 28(3) mandatory clauses: process only on documented instructions, confidentiality, security, sub-processor authorization, assistance with data-subject rights and breaches, deletion/return at end of contract, and audit rights. Processors have direct obligations too (security, ROPA, breach notification to the controller, transfer rules, DPO where applicable). A missing or deficient DPA is a common and easily-detected finding.

## Pillar H — International data transfers (Art. 44–49)

Transfers of personal data outside the EEA are prohibited unless a Chapter V mechanism ensures protection travels with the data:

- **Adequacy decision (Art. 45)** — the Commission has deemed the destination adequate. Current adequate jurisdictions include the UK, Switzerland, Japan, South Korea, Canada (commercial), New Zealand, Argentina, Israel, Uruguay, and others — plus **the US, but *only* for organizations self-certified under the EU–US Data Privacy Framework (DPF)**. DPF status is volatile — see `current-landscape.md` and verify before relying on it.
- **Appropriate safeguards (Art. 46)** — chiefly **Standard Contractual Clauses (SCCs)** and **Binding Corporate Rules (BCRs)**. Since *Schrems II*, using SCCs also requires a **Transfer Impact Assessment (TIA)** evaluating whether the destination's laws (e.g., surveillance) undermine the contractual protections, plus supplementary measures (often encryption with EU-held keys) where they do.
- **Derogations (Art. 49)** — narrow, situation-specific exceptions (explicit consent, contract necessity, etc.); not for routine or bulk transfers.
- **Foreign-authority access (Art. 48)** — a judgment or decision of a *non-EU* court or authority demanding a transfer is not, by itself, a lawful basis to transfer; it is only enforceable through a mutual legal-assistance treaty or similar international agreement. This is the article behind the whole "can a US government order compel my EU data?" question, and it is why a processor that would quietly hand over EU data on receipt of a foreign subpoena is a transfer risk worth flagging.

Storage in an EU/EEA region (e.g., AWS eu-central-1) is **not** a restricted transfer by itself — but check for remote access from outside the EEA (support, admin), which can constitute a transfer.

*Transfers are the single highest-value enforcement area.* The DPF is currently contested, so a robust audit treats it as fragile and checks for an SCC fallback.

---

## Appendix — Article quick-map (for tagging findings)

Use this table to tag every finding with the right article. Cite from this map; never guess an article number.

| Domain | Key articles |
|---|---|
| Scope & definitions | 2, 3, 4 |
| Principles | 5 |
| Lawful basis | 6, 7, 8, 9, 10 |
| Transparency | 12, 13, 14 |
| Data-subject rights | 15, 16, 17, 18, 19, 20, 21, 22 |
| Controller/processor duties | 24, 25, 26, 27, 28, 29, 30 |
| Security & breach | 32, 33, 34 |
| DPIA & prior consultation | 35, 36 |
| DPO | 37, 38, 39 |
| Certification / codes | 40, 41, 42, 43 |
| International transfers | 44, 45, 46, 47, 48, 49 |
| Complaints & remedies | 77, 78, 79 |
| Liability & fines | 82, 83, 84 |

**Fine tiers (Art. 83):** lower tier up to €10M / 2% of global annual turnover (e.g., ROPA, security, DPO, breach-notification failures); higher tier up to €20M / 4% (principles, lawful basis, data-subject rights, transfers). Whichever is higher applies. Cite the *tier*, never a specific predicted fine amount for the audited organization, and never a named enforcement case unless the user supplied it.
