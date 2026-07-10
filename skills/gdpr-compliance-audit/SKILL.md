---
name: gdpr-compliance-audit
description: Audit an organization, system, product, or policy for GDPR compliance and return structured, article-cited findings with a risk rating and remediation plan. Use this whenever someone asks whether their data handling, privacy notice, vendor/transfer setup, cookie consent, breach process, data-subject request handling, or AI feature meets EU data protection law — even when they don't say "GDPR" (e.g. "can we send EU user data to our US analytics vendor?", "a user asked us to delete their data — what must we do?", "we had a breach, do we have to report it?", "review our privacy policy"). Covers GDPR/EU data protection only, not CCPA/PIPL/other regimes.
---

# GDPR Compliance Audit

Produce a defensible, article-cited GDPR audit of whatever the user gives you — a pasted
privacy notice, a vendor stack, a described data flow, an AI feature, a breach scenario, or a
whole organization. The output is a set of evidenced findings, not legal advice prose.

## Before anything: the scope gate

GDPR applies only where EU/EEA data subjects are involved (or an EU establishment processes
the data). If the request is about a different regime (CCPA, PIPL, UK-only DUAA questions) or a
purely non-EU scenario, **do not force a GDPR audit** — say GDPR likely doesn't apply, offer to
proceed only if EU users exist, and stop. A confident GDPR verdict on an out-of-scope scenario
is a wrong answer, not a helpful one.

## Audit procedure

Work through the phases in `references/audit-phases.md` in order (0 Scoping → 8 Findings),
skipping only phases the question genuinely doesn't touch (Phase 0 and Phase 8 always run).
Read `references/articles.md` when you need the requirement detail for a phase — cite articles
from it rather than from memory.
Treat `references/current-landscape.md` as possibly out of date: for anything it covers (DPF
status, Digital Omnibus, AI Act timing), verify rather than assert, and tell the user to check
the live status.

## Inputs the procedure expects

All optional; the audit degrades gracefully: organization/context description, privacy notice
text, vendor/sub-processor list, ROPA, DPA status, breach process, whether any AI system
processes personal data, and — critically — whether EU/EEA data subjects are involved. When
something is missing, assess what the evidence supports and name what's needed for the rest;
**never upgrade silence to Compliant**.

## Non-negotiable behaviors

These exist because a compliance tool that gets them wrong is dangerous, not just unhelpful:

- **Cite the specific article for every finding.** Use the quick-map in `references/articles.md` to tag findings; an un-sourced verdict is unusable in front of a regulator.
- **Never invent fine amounts, named enforcement cases, or EDPB decisions.** You may cite the Art. 83 fine *tiers*; you may not predict a fine or name a case as settled fact unless the user supplied it. Hallucinated case law is this skill's worst failure mode.
- **Verify, don't assert, volatile law.** Anything from `current-landscape.md` gets an uncertainty flag and a "verify current status" recommendation.
- **Assess only what the evidence supports.** Missing ROPA, unseen DPAs, unknown vendor certifications → `Partial`/`N/A` findings that name what's needed, plus an entry in "What could not be assessed".
- **Stay in scope.** GDPR/EU data protection only; adjacent regimes get at most a one-line flag.

## Output — use this exact structure

### Executive summary
Two to five sentences: overall posture, the highest-risk gaps, and whether anything blocked assessment.

### Findings (one record each)
- **Domain:** e.g. Transparency, Lawful basis, Transfers
- **Article(s):** e.g. Art. 13, Art. 44–49
- **Status:** Compliant | Partial | Non-compliant | N/A
- **Evidence:** what in the input supports this (or "insufficient evidence — need X")
- **Risk:** likelihood × impact on data subjects (High / Medium / Low, with one line of reasoning)
- **Remediation:** owner-ready next step

### Maturity by domain (0–4)
Score each assessed domain on the scale in `references/audit-phases.md` (0 Absent → 4 Measured/continuous). Omit domains you couldn't assess.

### What could not be assessed
Name each item, why it matters, and what evidence would unlock it.
