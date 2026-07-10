---
name: dsar-processing
description: Process a GDPR data-subject rights request (DSAR) from receipt to a compliant, on-time response — access, erasure, rectification, restriction, portability, or objection under Articles 15-22. Returns a structured, article-cited handling plan with a per-right outcome decision, the response deadline, identity-verification and exemption analysis, and recipient-notification steps. Use this whenever someone gets a request from a user to see, correct, delete, export, or stop processing their data and needs to know what they must do and by when — even when they don't say "DSAR" (e.g. "a customer wants all their data and their account gone", "someone asked us to stop emailing them and delete everything"). This runs the request-handling procedure; for a whole-org rights-readiness review use gdpr-compliance-audit. GDPR/EU only.
---

# Processing a GDPR data-subject request (Art. 12, 15-22)

Take one described **rights request** and produce a defensible, article-cited handling plan: what
must be done, by when, what can be refused, and how to verify the requester — not legal-advice prose.

## Before anything: scope + right identification

GDPR applies only where EU/EEA data subjects are involved. If out of scope, say so and stop.

Identify **which right(s)** the request invokes (one message often mixes several — "see my data
and delete my account" = Art. 15 + Art. 17). For each right, emit exactly one **outcome** value:

`Fulfil` | `Partially fulfil` | `Refuse` | `Extend` | `Need identity verification`

`Refuse` and `Partially fulfil` must always name the exemption/exception relied on and its article.
`Need identity verification` gates everything else — you cannot `Fulfil` until identity is
reasonably established (Art. 12(6)).

The outcome field carries **one bare value, never a chain** ("Need identity verification →
then Fulfil" breaks tracking that keys on the value). Which value depends on what the user is
actually asking:

- **Processing a live request** whose identity is unestablished and whose fulfilment would
  disclose or destroy data → the outcome is `Need identity verification`; the post-verification
  path (fulfil, partial-fulfil with the exemption, …) belongs in the handling narrative.
- **A substantive question about the answer** ("can we refuse?", "must we comply?", "fully or
  partly?") → give the substantive outcome (`Fulfil` / `Partially fulfil` / `Refuse` / `Extend`)
  — that is the decision being asked for — and list identity verification as a handling step.

## Procedure

Work through `references/workflows.md` (Receipt → Identity → Locate data → Assess exemptions →
Compile response → Deadline & delivery → Recipient notification). Pull deadlines and exemption
detail from `references/standards.md` — cite from it, not from memory.

`scripts/process.py` computes the response deadline from the receipt date (one month, Art. 12(3),
with the two-month extension and its notice requirement) so the clock is never guessed.

## Inputs the procedure expects

All optional; degrade gracefully. The request text and date received, which rights are asked for,
whether identity is verified, the data categories held, recipients/processors the data was shared
with, any legal-retention obligations, and whether the request is manifestly unfounded/excessive.
When something is missing, name it and give the conditional path — never assume a refusal ground
that isn't evidenced.

## Non-negotiable behaviors

- **Cite the specific article for every obligation** (Art. 15 access, Art. 17 erasure, Art. 12(3)
  deadline, Art. 19 recipient notification, etc.).
- **State the deadline explicitly** and that the one-month clock runs from receipt, extendable by
  two months for complexity *with* notice inside the first month (Art. 12(3)).
- **Never invent fine amounts or named enforcement cases.** Art. 83 tiers only.
- **Treat rights as not absolute but exemptions as narrow** — erasure has real exceptions
  (Art. 17(3): legal obligation, freedom of expression, legal claims); name them rather than
  refuse vaguely, and don't over-refuse.
- **Require identity verification before disclosure** (Art. 12(6)) — but don't demand excessive ID.
- **Stay in scope** — GDPR only; other regimes get a one-line flag.

## Output — use this exact structure

### Request summary & outcome per right
A row per right invoked: `Right` · `Article` · `Outcome` (from the taxonomy) · one-line reason.

### Deadline
The response due date (from the script), the receipt date it runs from, and whether an extension is
being taken (with the Art. 12(3) notice obligation).

### Identity verification
Whether identity is established; if not, what proportionate verification to request (Art. 12(6)).

### Per-right handling & exemptions
For each right: what to provide/do, and any exemption relied on with its article and why it applies
— each step tagged `Compliant | Partial | Non-compliant | N/A` against the obligation.

### Recipient / processor notification (Art. 19)
Who the data was shared with and the obligation to notify them of erasure/rectification/restriction.

### Process maturity by area (0–4)
Score intake, identity verification, data-location, and deadline-tracking readiness on 0–4. Omit
areas you couldn't assess.

### What could not be assessed
Each missing item, why it matters, and the evidence that would unlock it.
