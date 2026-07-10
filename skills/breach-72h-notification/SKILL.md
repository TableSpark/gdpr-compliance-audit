---
name: breach-72h-notification
description: Work a personal-data breach through the GDPR Article 33-34 decision — whether to notify the supervisory authority within 72 hours, whether to also tell affected individuals, and what to record — and return a structured, article-cited response plan with a clear notification decision, the deadline, a risk assessment, and the register entry. Use this whenever someone has (or suspects) a breach — lost/stolen device, misdirected email, ransomware, exposed database, insider access — and needs to know if and when they must report it and to whom, even when they don't say "breach notification" (e.g. "a laptop with a customer spreadsheet was stolen, do we have to report it?", "we emailed the wrong customer list to a supplier"). This runs the breach-response procedure; for a whole-org readiness review use gdpr-compliance-audit. GDPR/EU only.
---

# Personal-data breach response (Art. 33-34)

Take one described (or suspected) breach and drive it to the notification decision: authority,
individuals, or record-only — defensible and article-cited, not legal-advice prose.

## Before anything: scope + is-it-a-breach gate

GDPR applies only where EU/EEA data subjects are involved. If out of scope, say so and stop.

Confirm it is a **personal-data breach** (Art. 4(12): breach of security leading to accidental/
unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data —
covers confidentiality, integrity, and availability breaches). Then emit exactly one **decision**:

`Notify SA` | `Notify SA + individuals` | `No notification (record only)` | `Insufficient info`

- `Notify SA` — likely to result in a risk to individuals' rights (Art. 33), not high risk.
- `Notify SA + individuals` — **high** risk to individuals (Art. 34).
- `No notification (record only)` — unlikely to result in a risk (e.g. strong encryption of the
  lost data with keys intact) — but the Art. 33(5) register entry is still mandatory.
- `Insufficient info` — a pivotal fact is unknown (encryption status is the classic one); say what
  to establish, and note the 72h clock is already running.

## Procedure

Work through `references/workflows.md` (Detect & contain → Establish facts → Risk assessment →
SA-notification decision → Individual-notification decision → Record). Pull the risk factors and
timing rules from `references/standards.md` — cite from it, not from memory.

`scripts/process.py` computes the 72-hour deadline from the awareness timestamp and maps the
risk level to the decision value so the clock and the threshold aren't guessed.

## Inputs the procedure expects

All optional; degrade gracefully. What happened and when it was discovered (awareness starts the
clock), data categories and volume, number of individuals, whether the data was encrypted/
pseudonymised and whether keys are safe, whether the data is recoverable, who the recipients are,
and any mitigations already taken. When a pivotal fact is missing (especially encryption), decision
is `Insufficient info` and you name what to confirm — never assume "encrypted, so fine".

## Non-negotiable behaviors

- **Cite the specific article for every step** (Art. 33 SA notification + 72h, Art. 34 individual
  communication + high risk, Art. 33(5) register, Art. 4(12) definition).
- **The 72h clock runs from awareness, not from the incident** — state this explicitly, and that a
  late notification must explain the delay (Art. 33(1)).
- **Encryption status is usually the pivotal fact** — treat it as decision-changing and insist it
  be confirmed rather than assumed.
- **Never invent fine amounts or named enforcement cases.** Art. 83 tiers only.
- **Record every breach even when not notifiable** (Art. 33(5)) — record-only is still an action.
- **Identify the competent/lead supervisory authority** question where cross-border (Art. 56).
- **Stay in scope** — GDPR only; other regimes get a one-line flag.

## Output — use this exact structure

### Notification decision
One `decision` value from the taxonomy + the risk finding and pivotal facts that drove it, each
article-tagged.

### Deadline
The 72-hour due timestamp (from the script), the awareness time it runs from, and the late-notice
explanation duty if already past.

### Risk assessment
Data categories, volume, individuals affected, encryption/recoverability, and the resulting risk
level (none / risk / high risk) with one line of reasoning per factor.

### Authority notification (Art. 33)
What to file, to which SA (raise the lead-SA question if cross-border), and the minimum Art. 33(3)
content; phased notification allowed if facts are still emerging.

### Individual notification (Art. 34)
Whether high risk triggers it, what the communication must say (Art. 34(2)), and any Art. 34(3)
exemption (e.g. encryption, or a public communication instead) — each tagged `Compliant | Partial |
Non-compliant | N/A`.

### Breach register entry (Art. 33(5))
The facts, effects, and remedial action to log regardless of the decision.

### Process maturity by area (0–4)
Score detection, containment, risk-assessment, and notification readiness on 0–4. Omit what you
couldn't assess.

### What could not be assessed
Each missing pivotal fact, why it matters, and what would resolve the decision.
