# DSAR — standards, rights, deadlines, and exemptions

> **Verify before relying:** national derogations vary (e.g. some Member States add exemptions).
> Do not present any fine or case as settled fact unless the user supplied it.

## The rights (Chapter III)

| Right | Article | Core obligation |
|-------|---------|-----------------|
| Transparency / modalities | Art. 12 | Respond without undue delay, within one month; free of charge (usually); facilitate rights |
| Access | Art. 15 | Copy of the personal data + supplementary info (purposes, recipients, retention, source, rights) |
| Rectification | Art. 16 | Correct inaccurate / complete incomplete data |
| Erasure ("right to be forgotten") | Art. 17 | Delete where grounds apply; **not absolute** (see 17(3)) |
| Restriction | Art. 18 | Limit processing while accuracy/objection is resolved |
| Notification to recipients | Art. 19 | Tell each recipient of rectification/erasure/restriction unless impossible/disproportionate |
| Portability | Art. 20 | Provide data in a structured, commonly used, machine-readable format (consent/contract + automated only) |
| Objection | Art. 21 | Stop processing based on legitimate interest/direct marketing on objection |
| Automated decisions | Art. 22 | Right not to be subject to solely automated decisions with significant effect |

## Deadlines (Art. 12(3)) — mirrors scripts/process.py

- Base: **one month** from receipt.
- Extension: **+ two months** for complexity or number of requests, **only if** the controller
  informs the data subject of the extension and the reasons **within the first month**.
- Manifestly unfounded/excessive (Art. 12(5)): may charge a reasonable fee or refuse — but the
  burden of demonstrating this is on the controller.

## Identity verification (Art. 12(6))

Where there are reasonable doubts about identity, request additional info to confirm it — but only
what is proportionate. Cannot be used as a blanket delay tactic.

## Erasure exceptions (Art. 17(3)) — narrow, name them

Processing necessary for: (a) freedom of expression/information; (b) a legal obligation or public-
interest task; (c) public-health reasons; (d) archiving/research; (e) establishment/exercise/
defence of legal claims. A retention obligation under other law is the most common real exception.

## Outcome mapping (feeds the SKILL.md taxonomy)

| Situation | Outcome value |
|-----------|---------------|
| Right applies, no exemption | `Fulfil` |
| Right applies but some data withheld under an exemption | `Partially fulfil` (name article) |
| A valid exemption defeats the whole request | `Refuse` (name article) |
| Complex/multiple requests, extension taken | `Extend` (with Art. 12(3) notice) |
| Identity not yet established | `Need identity verification` |
