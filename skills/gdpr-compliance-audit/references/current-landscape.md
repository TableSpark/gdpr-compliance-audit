# Current Landscape — Volatile Developments (verify, don't assert)

> **Staleness warning — read this first.** This file was written in **July 2026** and describes
> the parts of EU data-protection law that were actively moving at that time. Unlike
> `articles.md` (stable since 2018), everything here decays. When a finding depends on an item
> below, **flag the uncertainty and recommend the user verify the live status** (official DPF
> list, EDPB/Commission announcements, the EUR-Lex text) rather than asserting it as settled
> fact. Confidently stating outdated law is worse than flagging uncertainty.

---

## Enforcement posture

- **Enforcement now tests real-world effectiveness, not documentation.** A policy that exists but isn't actionable, a consent banner that's harder to reject than accept, or a DPA lacking real terms are all treated as failures. Audit for *operating* controls, not just their existence on paper.
- **Transparency is the 2026 coordinated-enforcement focus.** The EDPB launched its fifth Coordinated Enforcement Framework action on Articles 12–14 in March 2026; DPAs across the EU are actively probing privacy notices and consent flows. Weight this area heavily.

## EU–US Data Privacy Framework (DPF) — under fresh legal pressure

The DPF remains formally in force, but its foundations have weakened:

- On **29 June 2026 the US Supreme Court decided *Trump v. Slaughter* (6–3)**, overruling *Humphrey's Executor* (1935) and ending "for-cause" removal protection for FTC commissioners — so the FTC, one of the enforcement pillars the EU's adequacy decision relies on, is no longer structurally independent of the President.
- *Schrems III* is separately progressing, and Section 702 FISA reauthorization is unsettled.
- The removal ruling doesn't automatically void the DPF, but it hands the framework's challengers a concrete argument and makes an EU re-examination of adequacy more likely.

**Audit stance:** don't rely on the DPF alone. Flag DPF-only transfers as a resilience risk; recommend SCCs + a TIA as a fallback; recommend verifying the vendor's current self-certification on the official DPF list. Always caveat that the DPF's status should be re-checked as of the date of the audit.

## The "Digital Omnibus" reform — in flight, nothing final

The Commission proposed (Nov 2025) the most significant GDPR amendments since 2018 — touching cookie consent, SME burden, breach rules, and AI. The EDPB/EDPS issued a critical Joint Opinion (10 Feb 2026), notably resisting attempts to narrow the definition of "personal data" — and a leaked Council compromise text has already dropped that redefinition, showing how unstable the package is. Adoption is not expected before late 2026, entry into force ~2027–2028. **Do not apply any relaxed rule from this package** — audit against the law in force, and mention the reform only as an outlook item.

## AI Act × GDPR convergence

- High-risk AI provisions of the EU AI Act apply from **2 August 2026**.
- Penalty tiers: the headline **€35M / 7%** ceiling is for *prohibited* AI practices (AI Act Art. 5); breaches of the high-risk obligations are capped at **€15M / 3%** — separate from, and stackable on top of, any GDPR fine.
- The EDPB has signalled that **LLMs rarely meet GDPR anonymization standards**, so deploying third-party AI on personal data generally requires a **DPIA and a documented lawful basis**. Joint EDPB–Commission guidance on the interplay is rolling out through 2026.
- If the audited system uses AI on personal data, treat AI Act interplay as an additional audit dimension (and check deadlines current at audit time).

## Adjacent regimes — "stacked liability"

A single mishandled data flow can simultaneously implicate GDPR, the EU Data Act (in force Sept 2025), NIS2, and DORA (for financial entities). A thorough audit at least flags where these overlap; a full assessment of those regimes is out of this skill's scope.

## UK divergence

The UK's Data Use and Access Act 2025 (in force Feb 2026) creates a UK-specific regime that no longer perfectly mirrors EU GDPR (notably around automated decision-making and research). Organizations operating in both must not assume one policy satisfies both. Flag this whenever the audited organization handles both UK and EU data; a UK-DUAA audit itself is out of scope.
