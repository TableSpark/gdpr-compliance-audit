---
name: conducting-gdpr-dpia
description: Run a GDPR Data Protection Impact Assessment (DPIA) under Article 35 for a specific processing operation and return a structured, article-cited assessment with an obligation decision, a risk register, mitigations, residual risk, and a DPO sign-off checklist. Use this whenever someone needs to decide whether a DPIA is required or wants to actually carry one out for a new system, feature, vendor, AI tool, monitoring scheme, or large-scale/special-category processing — even when they don't say "DPIA" (e.g. "do we need an impact assessment before launching this facial-recognition login?", "is this new analytics pipeline high-risk enough that we have to assess it?"). This runs the DPIA procedure; for a whole-org GDPR review use gdpr-compliance-audit instead. GDPR/EU only.
---

# Conducting a GDPR DPIA (Article 35)

Take one described **processing operation** and run it through the Article 35 / EDPB
WP248rev.01 methodology, ending in a defensible, article-cited DPIA — not legal-advice prose.
The core deliverables are an **obligation decision**, a **risk register**, **mitigations with
residual risk**, and a **DPO sign-off checklist**.

## Before anything: scope + obligation gate

GDPR applies only where EU/EEA data subjects are involved (or an EU establishment processes the
data). If it's out of scope, say so and stop — don't run a DPIA on a non-EU scenario.

Then decide the **DPIA obligation** using the trigger logic in `references/standards.md`
(Art. 35(3) automatic triggers + the WP248 nine criteria — two or more presumes a DPIA). Emit
exactly one **decision** value:

`Required` | `Not required` | `Recommended` | `Prior consultation required`

Use `Prior consultation required` only when residual risk stays high after mitigation (Art. 36).
Use `Recommended` for borderline single-criterion cases where a DPIA is good practice but not
strictly mandated. Never invent certainty the facts don't support — if the trigger facts are
missing, say what you need and lean to `Recommended`.

## Procedure

Work through `references/workflows.md` (Steps 1–7: Scoping → Systematic description → Necessity &
proportionality → Risk identification → Mitigation → DPO advice → Ongoing review). Skip a step
only if the operation genuinely doesn't touch it; Step 1 (scoping) and the risk register always
run. Pull requirement detail and citations from `references/standards.md` — cite from it, not
from memory.

`scripts/process.py` scores the risk matrix (likelihood × severity → Low/Medium/High/Very High)
and flags when residual risk forces Art. 36 prior consultation. Call it rather than eyeballing.

## Inputs the procedure expects

All optional; degrade gracefully. Processing purpose and lawful basis, data categories (flag any
Art. 9 special category or Art. 10 criminal data), data subjects (flag vulnerable groups incl.
children/employees), scale and duration, recipients/sub-processors, international transfers, the
technology involved (flag new/innovative tech and automated decision-making), and existing
safeguards. When something is missing, assess what the evidence supports and name the gap — never
upgrade silence to "low risk".

## Non-negotiable behaviors

- **Cite the specific article/guidance for every finding** (Art. 35(7) elements, the WP248
  criteria). An un-sourced risk verdict is unusable.
- **Never invent fine amounts or named enforcement cases.** Cite Art. 83 tiers only.
- **Compute residual risk explicitly** — identifying a mitigation without re-scoring the risk is
  the most common DPIA deficiency. If residual stays High/Very High → `Prior consultation required`.
- **Treat volatile law as possibly stale** (supervisory-authority DPIA lists change) — flag and
  say verify current national list.
- **Stay in scope** — GDPR only; other regimes get a one-line flag at most.

## Output — use this exact structure

### DPIA obligation decision
One `decision` value from the taxonomy above + the triggers/criteria that drove it, each with its
Art. 35(3) letter or WP248 criterion number.

### Systematic description (Art. 35(7)(a))
Nature, scope, context, purpose + lawful basis (Art. 6, and Art. 9(2) condition if special data).

### Necessity & proportionality (Art. 35(7)(b))
Data minimisation, purpose limitation, storage limitation, rights facilitation — each `Compliant |
Partial | Non-compliant | N/A` with an article tag.

### Risk register (Art. 35(7)(c))
One record per risk: `Risk ID` · `Harm type` (physical/material/non-material) · `Article(s)`
(the provision or right at stake — e.g. Art. 22 for automated denial, Art. 5(1)(d) for
inaccuracy, Art. 9 for special-category exposure) · `Likelihood` (Remote/Possible/Likely/Almost
certain) · `Severity` (Negligible/Limited/Significant/Maximum) · `Inherent risk level` (from the
script). A risk row without an article tag is an unsourced verdict — the same rule as every
other finding.

### Mitigations & residual risk (Art. 35(7)(d))
Per risk: technical + organisational measure, expected reduction, `Residual risk level`. Escalate
any remaining High/Very High to prior consultation.

### Process maturity by area (0–4)
Score the DPIA-relevant areas (screening, risk methodology, DPO involvement, review cadence) on
the 0 Absent → 4 Measured/continuous scale. Omit areas you couldn't assess.

### DPO sign-off checklist
Art. 35(2) DPO advice recorded, Art. 35(9) data-subject views considered, review date set,
register entry made.

### What could not be assessed
Each missing item, why it matters, and the evidence that would unlock it.
