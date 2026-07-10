# DPIA — step-by-step procedure with timelines

Indicative timeline for a moderately complex operation; compress for a single feature. Steps 1 and
the risk register always run.

## Step 1 — Scoping (≈ Week 1)
- Run the threshold check (Art. 35(3) + WP248) to confirm/settle the obligation decision.
- Define the boundary: which systems, data flows, and org units are in scope.
- Name the DPIA team: processing owner, DPO, security rep, legal; consider a data-subject rep (Art. 35(9)).
- Gather existing docs: architecture, data-flow map, privacy notice, consent records, DPAs.

## Step 2 — Systematic description (≈ Week 2) — Art. 35(7)(a)
- Map the data lifecycle collection → deletion.
- List every data element + its lawful basis (Art. 6; Art. 9(2) condition if special category).
- List recipients and sub-processors; document international transfers + safeguards (Chapter V).
- Record the technology stack (flag new tech, automated decision-making).

## Step 3 — Necessity & proportionality (≈ Week 3) — Art. 35(7)(b)
- Per data element: why is it necessary for the stated purpose?
- Are there less-invasive alternatives (aggregation, anonymisation)?
- Data minimisation, purpose limitation, storage limitation each rated + article-tagged.
- Confirm data-subject rights (Art. 15–22) can actually be exercised.

## Step 4 — Risk identification & assessment (≈ Week 3–4) — Art. 35(7)(c)
- Threat-model the data-flow map (internal actors, external attackers, processors, failures).
- Score each risk with `scripts/process.py` (likelihood × severity → level).
- Record in the risk register with unique IDs and **inherent** levels.

## Step 5 — Mitigation & residual risk (≈ Week 4–5) — Art. 35(7)(d)
- For each High/Very High risk, define technical + organisational measures.
- Re-score to a **residual** level (this recalculation is mandatory, not optional).
- If any residual stays High/Very High → escalate to Art. 36 prior consultation.

## Step 6 — DPO advice & sign-off (≈ Week 5–6) — Art. 35(2)
- DPO reviews independently; record the advice and whether it was followed (and why not).
- Processing-owner + senior-management approval.
- Enter in the central DPIA register with a scheduled review date.

## Step 7 — Ongoing review
- Re-open on material change: new data categories, new recipients, tech change, incident, law change.
- Periodic review at least annually; version every revision.
