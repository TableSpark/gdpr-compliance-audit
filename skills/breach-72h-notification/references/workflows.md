# Breach response — step-by-step procedure

The **72-hour clock runs from awareness** (Art. 33(1)), not from when the breach happened. Timestamp
awareness first; everything downstream is measured from it.

## Step 1 — Detect & contain (Hour 0)
- Record the awareness timestamp — this starts the 72h clock.
- Contain: revoke access, isolate systems, remote-wipe the device if possible, rotate credentials.
- Confirm it meets the Art. 4(12) definition (confidentiality, integrity, OR availability breach).

## Step 2 — Establish the pivotal facts
- Data categories, sensitivity, volume, number of individuals.
- **Encryption / pseudonymisation status and key safety** — the usually-decisive fact.
- Recoverability (is this an availability breach that's already resolved?).
- Recipients / who now has the data.
- If a pivotal fact can't be established yet → decision `Insufficient info`, but keep the clock running.

## Step 3 — Risk assessment (EDPB Guidelines 9/2022)
- Weigh the risk factors → none / a risk / high risk.
- `scripts/process.py` maps the risk level to the decision value.

## Step 4 — SA-notification decision (Art. 33)
- A risk (or higher) ⇒ notify the SA within 72h of awareness; if late, include the delay reasons.
- Cross-border processing ⇒ identify the lead SA (Art. 56).
- File the Art. 33(3) minimum content; use phased notification (Art. 33(4)) if facts are still emerging.

## Step 5 — Individual-notification decision (Art. 34)
- **High** risk ⇒ communicate to affected individuals without undue delay, in plain language (Art. 34(2)).
- Check Art. 34(3) exemptions: encryption/unintelligibility; measures that removed the high risk;
  disproportionate effort → public communication instead.

## Step 6 — Record (Art. 33(5))
- Log the facts, effects, and remedial action in the breach register **regardless** of the decision —
  including non-notifiable breaches. This is what a regulator inspects later.
