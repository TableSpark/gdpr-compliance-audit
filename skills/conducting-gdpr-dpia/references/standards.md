# DPIA — standards, triggers, and citations

> **Verify before relying:** supervisory-authority DPIA lists (Art. 35(4)) change per country.
> Precedents below are illustrative and must be confirmed against a primary source before use in
> a real assessment. Do not present any fine or case as settled fact to a user unless they
> supplied it.

## Legal basis — Article 35 elements

| Element | Reference | Requirement |
|---------|-----------|-------------|
| Obligation | Art. 35(1) | DPIA required where processing is "likely to result in a high risk" |
| DPO involvement | Art. 35(2) | Controller shall seek the DPO's advice |
| Automatic triggers | Art. 35(3)(a)-(c) | Systematic profiling w/ significant effect; large-scale special/criminal data; large-scale systematic monitoring of public areas |
| Minimum content | Art. 35(7)(a)-(d) | Description; necessity & proportionality; risk assessment; measures |
| SA lists | Art. 35(4)-(5) | National lists of operations that (do/don't) require a DPIA |
| Data-subject views | Art. 35(9) | Seek views "where appropriate" |
| Prior consultation | Art. 36 | Consult the SA if residual risk stays high |

## EDPB WP248rev.01 — nine high-risk criteria (two or more ⇒ DPIA presumed)

1. Evaluation or scoring (incl. profiling/prediction)
2. Automated decision-making with legal or similarly significant effect
3. Systematic monitoring
4. Sensitive data or data of a highly personal nature
5. Data processed on a large scale
6. Matching or combining datasets
7. Data concerning vulnerable data subjects (children, employees, patients, …)
8. Innovative use / new technological solutions (AI, biometrics, IoT)
9. Processing that prevents data subjects from exercising a right or using a service

## Obligation decision mapping (feeds the SKILL.md taxonomy)

| Situation | Decision value |
|-----------|----------------|
| Any Art. 35(3) trigger OR ≥2 WP248 criteria | `Required` |
| Exactly one WP248 criterion, no automatic trigger | `Recommended` |
| No triggers/criteria met and low-risk on the facts | `Not required` |
| DPIA done, residual risk still High/Very High | `Prior consultation required` |

## Risk scoring model (mirrors scripts/process.py)

- **Likelihood:** Remote (<10%) · Possible (10–50%) · Likely (50–90%) · Almost certain (>90%)
- **Severity:** Negligible · Limited · Significant · Maximum
- **Level = Likelihood × Severity** → Low / Medium / High / Very High
- Any residual **High/Very High** ⇒ Art. 36 prior consultation.

## Harm types to test (Art. 35(7)(c))

Physical · material (financial loss, identity theft) · non-material (distress, reputational) ·
social (discrimination, chilling effects) · loss of control over personal data.

## Common deficiencies (grade against these)

Generic risk descriptions; missing proportionality analysis; **no residual-risk recalculation**;
DPO advice not documented; static DPIA never reviewed; no Art. 35(9) justification.

## Illustrative precedent — VERIFY before citing to anyone

- Karolinska Institute (Swedish DPA, 2019) — sanction linked to processing without a required DPIA.
- Clearview AI (CNIL, 2022) — biometric processing without DPIA/lawful basis.

*(Placeholders for orientation only — confirm names, dates, and amounts against the DPA's own
decision before repeating. This skill must not assert these as fact unsupplied.)*
