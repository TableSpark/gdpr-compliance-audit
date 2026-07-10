# DPIA — filled example (AI support-ticket triage)

*Illustrative output for a fictional scenario: an EU retailer wiring a third-party LLM into
customer support, where tickets sometimes contain health complaints. Article citations are real;
the risk numbers are worked, not authoritative.*

## DPIA obligation decision
**Required.** Triggers: Art. 35(3)(b) potential large-scale special-category (health) data;
WP248 criteria met — #4 sensitive data, #8 innovative tech (LLM), #1 evaluation (draft scoring).
Two+ criteria ⇒ DPIA mandatory.

## Systematic description — Art. 35(7)(a)
Nature: collection, use, disclosure to processor, storage of support tickets. Scope: all inbound
tickets, EU customers, continuous. Context: controller–customer, data volunteered in tickets.
Purpose: faster support replies. Lawful basis: Art. 6(1)(f) legitimate interest (to test); no
Art. 9(2) condition identified for the health data — **gap**.

## Necessity & proportionality — Art. 35(7)(b)
- Data minimisation — **Partial** (Art. 5(1)(c)): full ticket sent to LLM incl. health detail; redaction not in place.
- Purpose limitation — **Partial** (Art. 5(1)(b)): vendor reuse for model training not excluded by contract.
- Storage limitation — **N/A** (Art. 5(1)(e)): retention at vendor unknown.
- Rights facilitation — **Partial** (Art. 15–22): no process to surface LLM-processed data on access.

## Risk register — Art. 35(7)(c)
| Risk ID | Harm type | Likelihood | Severity | Inherent level |
|---------|-----------|------------|----------|----------------|
| R1 | material (special-category exposure to vendor) | Likely | Significant | High |
| R2 | non-material (distress from health data misuse) | Possible | Significant | Medium |

## Mitigations & residual risk — Art. 35(7)(d)
| Risk | Measure (technical + org) | Residual level |
|------|---------------------------|----------------|
| R1 | PII/health redaction before send (T) + Art. 28 DPA banning training reuse (O) | Medium |
| R2 | Transparency notice + opt-out of AI drafting (O) | Low |

No residual High/Very High ⇒ **no Art. 36 prior consultation** on these facts.

## Process maturity by area (0–4)
Screening 3 · Risk methodology 2 · DPO involvement 2 · Review cadence 1.

## DPO sign-off checklist
☐ Art. 35(2) DPO advice recorded ☐ Art. 35(9) data-subject views considered (n/a justified)
☐ Review date set (12 mo) ☐ DPIA register entry created.

## What could not be assessed
Vendor retention period (need the DPA); whether an Art. 9(2) condition exists (need lawful-basis
analysis); vendor sub-processor list (need Art. 28 disclosures).
