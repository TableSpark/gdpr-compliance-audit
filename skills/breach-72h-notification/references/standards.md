# Breach notification — standards, thresholds, and timing

> **Verify before relying:** SA filing mechanics differ by country; EDPB Guidelines 9/2022 on
> breach notification are the primary reference. Do not present any fine or case as settled fact
> unless the user supplied it.

## Definitions & duties

| Item | Reference | Rule |
|------|-----------|------|
| Personal-data breach | Art. 4(12) | Breach of security → accidental/unlawful destruction, loss, alteration, unauthorised disclosure of / access to personal data |
| SA notification | Art. 33(1) | Without undue delay and where feasible within **72 hours** of becoming aware, unless unlikely to result in a risk |
| Late notification | Art. 33(1) | If later than 72h, must be accompanied by reasons for the delay |
| Minimum content | Art. 33(3) | Nature, categories & approx numbers, DPO contact, likely consequences, measures taken/proposed |
| Phased notification | Art. 33(4) | Info may be provided in phases where not all available at once |
| Processor duty | Art. 33(2) | Processor notifies the controller without undue delay |
| Register | Art. 33(5) | Document **all** breaches (facts, effects, remedial action) — even non-notifiable ones |
| Individual communication | Art. 34(1) | Required when the breach is likely to result in a **high risk** to individuals |
| Communication content | Art. 34(2) | Plain language: nature, DPO contact, likely consequences, measures |
| Exemptions | Art. 34(3) | Not required if (a) data was encrypted/unintelligible; (b) subsequent measures remove the high risk; (c) it would involve disproportionate effort → public communication instead |
| Lead authority | Art. 56 | For cross-border processing, notify the lead SA (one-stop-shop) |

## The three thresholds → decision (mirrors scripts/process.py)

| Risk to individuals | SA (Art. 33) | Individuals (Art. 34) | Decision value |
|---------------------|--------------|-----------------------|----------------|
| Unlikely to result in a risk | No | No | `No notification (record only)` |
| A risk | Yes (72h) | No | `Notify SA` |
| High risk | Yes (72h) | Yes | `Notify SA + individuals` |
| Pivotal fact unknown | — | — | `Insufficient info` |

## Risk factors (EDPB Guidelines 9/2022)

Type of breach (confidentiality/integrity/availability); nature, sensitivity & volume of data;
ease of identifying individuals; severity of consequences; special characteristics of individuals
(children, vulnerable) or of the controller; number of affected individuals.

## Encryption is usually pivotal

If the data was strongly encrypted and the keys were not compromised, the data is likely
"unintelligible" → often `No notification (record only)` and an Art. 34(3)(a) exemption from
telling individuals. If encryption status is **unknown**, decision is `Insufficient info` — do not
default to "safe". This is the most consequential single fact in most device-loss breaches.
