# Breach response — filled example (stolen laptop, encryption unknown)

*Illustrative output. A fictional EU online retailer with customers in Germany and France: a sales
rep's laptop was stolen overnight with a spreadsheet of names, emails, and order history; encryption
status not yet confirmed. Article citations are real; the decision turns on a fact still to establish.*

## Notification decision
**Insufficient info** — the pivotal fact (was the laptop's disk encrypted, keys uncompromised?) is
unknown, and it flips the outcome between `No notification (record only)` and `Notify SA (+ individuals)`.
Establish it immediately; the 72h clock (Art. 33(1)) is already running from awareness.

## Deadline
Awareness ~ this morning → **SA notification due within 72 hours** of that timestamp (Art. 33(1)).
If confirmation of encryption pushes past 72h, any notification must explain the delay.

## Risk assessment
- Data: names, emails, order history — identifiable, moderate sensitivity, whole customer list (volume high).
- Encryption/recoverability: **unknown** — decisive. If strongly encrypted with safe keys → likely
  no risk (data unintelligible). If not → likely a risk, possibly high given the volume.
- Individuals: DE + FE customers (cross-border → lead-SA question).

## Authority notification (Art. 33)
If encryption is absent/unknown and risk ≥ "a risk": file with the SA within 72h, Art. 33(3)
minimum content, phased if facts still emerging. Cross-border ⇒ identify the lead SA (Art. 56) —
one-stop-shop rather than filing in every affected country. — Partial pending the encryption fact.

## Individual notification (Art. 34)
Only if **high** risk. If the disk was encrypted and keys safe, Art. 34(3)(a) likely exempts
telling individuals. If not encrypted and risk is high, communicate in plain language (Art. 34(2)):
what happened, likely consequences, what you're doing, how to protect themselves. — N/A until risk confirmed.

## Breach register entry (Art. 33(5))
Log now regardless of outcome: date/time of theft and of awareness, data involved, ~number of
individuals, containment (remote wipe attempt, credential reset), and the pending encryption check.

## Process maturity by area (0–4)
Detection 2 · Containment 2 · Risk assessment 1 · Notification readiness 1.

## What could not be assessed
Encryption status of the device (the decision hinges on it); exact number of customers on the
spreadsheet; whether remote wipe succeeded — all needed to finalise the decision.
