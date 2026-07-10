# GDPR Compliance Audit Methodology — Phases 0–8

Work these phases **in order**; each phase's checks yield discrete, evidenced findings
(Compliant / Partial / Non-compliant / N/A) tied to specific articles. Skip a phase only when
the user's question genuinely doesn't touch it (e.g., a pure transfer question may need only
Phases 0, 1, 7, 8) — but always run Phase 0 (scoping) and Phase 8 (findings), because
an audit without a scope gate or a structured output is not defensible.

For the requirement detail behind any check, read `articles.md`. For the volatile items
(DPF status, Digital Omnibus, AI Act), read `current-landscape.md` and treat it as possibly stale.

---

## Phase 0 — Scoping & preparation

- Confirm GDPR applicability first (Part 0 of `articles.md`): material scope (Art. 2), territorial scope (Art. 3), role classification (Art. 4). **If no EU/EEA data subjects are involved, GDPR likely does not apply — say so and do not force an audit.** If applicability is unclear, ask whether EU users/customers exist before proceeding.
- Define the audit boundary: which entities, systems, products, processing activities, and geographies are in scope.
- Inventory the evidence actually provided: ROPA, privacy notices, DPAs with vendors, DPIAs, breach register, consent records, retention schedule, security policies, training records, data-subject-request log. **What is missing constrains what you can conclude** — record missing items now; they feed "What could not be assessed."
- Identify the lead supervisory authority (for cross-border processing, the "one-stop-shop" main establishment).
- Non-EU controller in scope via Art. 3(2)? Check for an Art. 27 EU representative — a high-yield, easily verified finding.

## Phase 1 — Data mapping & inventory *(feeds everything else)*

- Verify a ROPA exists and is current (Art. 30). If it doesn't, that's finding #1 and the audit largely reconstructs one from what the user describes.
- For each processing activity, capture: purpose, lawful basis, data categories (flag special categories), data subjects (flag children/vulnerable), source, recipients, sub-processors, international transfers + mechanism, retention period, and security measures.
- Build/validate data-flow understanding, especially every point where data crosses the EEA border.

## Phase 2 — Lawfulness assessment (Art. 5–10)

- Each activity has a documented, valid lawful basis recorded *before* processing. Every activity needs one — an activity with no identifiable basis is unlawful regardless of how benign it looks, which is why this check is per-activity, not per-organization.
- Consent (where used) meets Art. 7: freely given, specific, informed, unambiguous, withdrawable, with evidence retained. Check consent UIs for **dark patterns** — asymmetric accept/reject, pre-ticks, bundling.
- Legitimate interests are backed by a documented **LIA**.
- Special-category / criminal data have a valid Art. 9/10 condition **on top of** the Art. 6 basis.
- Purpose limitation and minimisation hold in practice (no scope creep, no "collect everything").

## Phase 3 — Transparency review (Art. 12–14) *(2026 enforcement priority — weight heavily)*

- Privacy notices exist at every collection point and cover the full Art. 13/14 content set (see Pillar D in `articles.md` for the required items).
- Lawful basis stated *per purpose*; legitimate interests articulated.
- International transfers disclosed with the specific mechanism and, ideally, named third countries.
- Retention stated as a period or clear criteria — "as long as needed" fails both transparency (Art. 13(2)(a)) and storage limitation (Art. 5(1)(e)).
- The right to lodge a complaint with a supervisory authority is mentioned (a frequently-missing Art. 13(2)(d) item).
- Language is genuinely plain and accessible; layered/just-in-time notices used where helpful.
- Automated decision-making disclosed with meaningful information about the logic.

## Phase 4 — Data-subject rights (Art. 12, 15–22)

- A documented, tested procedure exists for each right, with identity verification and the **one-month** SLA (extendable by two months for complexity, with the individual told within the first month).
- Requests are logged; sample past requests to confirm they were handled correctly and on time.
- Erasure/rectification propagate to backups and to processors, and recipients are notified (Art. 19).
- Portability delivers a machine-readable export where applicable.
- Direct-marketing objections are honoured absolutely; opt-outs are frictionless.
- Art. 22 safeguards (human review, contestability) exist for any solely-automated significant decisions.
- *Test, don't just read the policy* — where possible, trace an actual request end to end.

## Phase 5 — Accountability & governance (Art. 24–39)

- DPO appointed where required; independent, resourced, reachable, published.
- Data protection by design/by default evidenced in the SDLC and in default settings (Art. 25).
- DPIAs completed for high-risk processing (Art. 35); residual-risk sign-off; prior consultation (Art. 36) where needed. New-technology processing of personal data — including wiring an LLM or other AI into a flow — is a classic DPIA trigger.
- Policies, roles, and responsibilities documented; staff training current.
- Board-level oversight / management engagement demonstrable.

## Phase 6 — Security & breach readiness (Art. 32–34)

- Technical/organizational measures proportionate to risk: encryption, access control, pseudonymization, logging, resilience, backup/restore, regular testing.
- Documented incident-response plan mapped to the **72-hour** clock (Art. 33); an internal breach register exists regardless of reportability.
- Communication to affected individuals (Art. 34) when the breach likely poses *high risk* to them — this is a separate decision from notifying the authority.
- Evidence the process works: past incidents logged and assessed; tabletop exercises.

## Phase 7 — Vendors & transfers (Art. 28, 44–49)

- Every processor is under a compliant DPA with all Art. 28(3) clauses; sub-processors authorized and flowed down. An unmapped sub-processor chain is itself an Art. 28 due-diligence gap.
- Vendor due-diligence / security assessments on file.
- Each cross-border transfer has a valid Chapter V mechanism; SCC-based transfers have a **TIA** (post-*Schrems II*) and supplementary measures where needed. SCCs signed years ago without a TIA are a common Partial finding.
- **DPF reliance is stress-tested**: verify the vendor's certification on the official DPF list before relying on it, and check for an SCC fallback if the adequacy decision falls (see `current-landscape.md`).
- Intra-EEA hosting (e.g., an EU cloud region) is not a restricted transfer by itself — but check for non-EEA remote access.

## Phase 8 — Findings, risk-rating & remediation

- Emit each finding in the exact per-finding record defined in SKILL.md (domain, article(s), status, evidence, risk, remediation).
- Rate each finding by **likelihood × impact on individuals' rights** (mirrors how regulators weigh penalties and aligns to a DPIA-style risk model).
- Prioritize: legal-basis gaps, unlawful transfers, transparency failures, and non-functional rights processes are high-severity because they hit the higher fine tier and current enforcement themes.
- Produce a remediation plan with owner-ready next steps; recommend re-testing. Treat compliance as continuous, not a point-in-time certificate.

## The maturity lens (for the "Maturity by domain" output section)

Rather than binary pass/fail, rate each audited domain on:

**0 Absent → 1 Ad hoc → 2 Documented → 3 Operational → 4 Measured/continuous**

Regulators explicitly reward organizations that treat privacy as a living operational practice with monitoring and metrics, over those with static paperwork — so "a policy exists" (2) is not the same as "the process runs and is tested" (3–4). Score only domains you actually assessed; leave the rest out rather than guessing.
