# DSAR — step-by-step handling procedure

The clock (Art. 12(3)) starts at **receipt**, so log the date first and do not let identity checks
silently consume the month.

## Step 1 — Receipt & logging (Day 0)
- Record the request date (starts the one-month clock) and the channel it came in on.
- A DSAR is valid in any form — email, chat, even verbal — it need not say "GDPR" or "DSAR".
- Identify every right invoked; a single message often mixes access + erasure + objection.

## Step 2 — Identity verification (Art. 12(6), early)
- Establish identity with proportionate checks; don't demand excessive ID.
- Until established, outcome is `Need identity verification` — but keep the clock running.

## Step 3 — Locate the data
- Search all systems, backups, and processors for the requester's personal data.
- Note recipients the data was shared with (needed for Art. 19 later).

## Step 4 — Assess exemptions & grounds
- Access: any third-party data to redact? Any Art. 15(4) rights-of-others limit?
- Erasure: does an Art. 17(3) exception apply (esp. legal-retention obligation)? Name it.
- Objection/restriction/portability: confirm the right's preconditions are met.
- Decide the per-right outcome value.

## Step 5 — Compile the response
- Access: the data copy + the Art. 15(1)(a)-(h) supplementary information.
- Erasure/rectification/restriction: perform it and prepare confirmation.
- Keep the response free of charge unless Art. 12(5) manifestly-excessive applies.

## Step 6 — Deadline & delivery
- Compute the due date with `scripts/process.py`.
- If taking the two-month extension, send the Art. 12(3) notice **within the first month**.
- Deliver securely to the verified data subject.

## Step 7 — Recipient / processor notification (Art. 19)
- For erasure/rectification/restriction, notify each recipient unless impossible/disproportionate;
  inform the data subject about those recipients if they ask.
