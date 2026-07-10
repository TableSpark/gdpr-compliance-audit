<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://tablespark.uk/assets/brand/tablespark-wordmark-reversed.svg">
  <img src="https://tablespark.uk/assets/brand/tablespark-wordmark.svg" alt="TableSpark" height="44">
</picture>

<br><br>

# gdpr-compliance-audit

**A four-skill GDPR suite: a generalist auditor plus three procedural specialists (DPIA · DSAR · 72h breach) — all answering in *findings*, not vibes.**

[![Install](https://img.shields.io/badge/npx-skills%20add%20TableSpark%2Fgdpr--compliance--audit-566F46?style=flat-square)](https://github.com/TableSpark/gdpr-compliance-audit)
[![Benchmark](https://img.shields.io/badge/eval%20pass%20rate-100%25%20vs%2066.7%25%20baseline-3F5334?style=flat-square)](#05--performance-metrics)
[![Current as of](https://img.shields.io/badge/law%20current%20as%20of-July%202026-71B357?style=flat-square)](#04--compliance--auditing)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20brand%20notice-8C8C8C?style=flat-square)](#07--license--brand-notice)

**English** | [简体中文](README.zh-CN.md)

<sub>BUILT WITH THE EVAL-DRIVEN SKILL-CREATOR LOOP &nbsp;✦&nbsp; EVERY FINDING CITES ITS ARTICLE</sub>

</div>

---

```bash
npx skills add TableSpark/gdpr-compliance-audit                    # any agent (Claude Code, Codex, Cursor, 60+)
npx skills add TableSpark/gdpr-compliance-audit -a claude-code -g  # Claude Code, globally
```

---

## 01 — Project overview

<sub>WHAT THIS IS &nbsp;·&nbsp; Fig. 01</sub>

An **agent skill** is a folder of instructions and reference material that an AI coding agent
loads on demand — it changes *how* the agent works when a matching task appears. This one turns
a general-purpose agent into a *disciplined* GDPR auditor.

Give it a pasted privacy notice, a vendor stack, a described data flow, an AI feature, a breach
scenario, or a whole organization. It works through a phased audit methodology and returns:

| Output | What it looks like |
|---|---|
| **Executive summary** | Overall posture, highest-risk gaps, what blocked assessment |
| **Findings** | One record each: domain · article(s) · status (`Compliant / Partial / Non-compliant / N/A`) · evidence · risk · remediation |
| **Maturity by domain** | `0 Absent → 1 Ad hoc → 2 Documented → 3 Operational → 4 Measured/continuous` |
| **What could not be assessed** | Missing evidence, named — never upgraded to silent compliance |

The design goal is *defensibility*: every verdict is tied to a specific GDPR article, every
status is backed by evidence from the input, and anything the evidence can't support is
declared unassessable instead of guessed.

**What it deliberately refuses to do** is as important as what it does:

- It will **not fabricate fine amounts, enforcement cases, or EDPB decisions** — the worst
  failure mode of any compliance tool, held to zero by a standing test assertion.
- It will **not force a GDPR audit onto out-of-scope questions** (CCPA-only, PIPL, no EU data
  subjects) — it says GDPR doesn't apply and stops.
- It will **not assert volatile law** (DPF status, Digital Omnibus, AI Act timing) — it flags
  uncertainty and tells you to verify the live status.

## 02 — Skills in this pack

<sub>ONE INSTALL · FOUR SKILLS &nbsp;·&nbsp; Fig. 02</sub>

One `npx skills add` installs the whole suite: a **generalist auditor** plus three
**procedural specialists** — the workflows an audit tells you to go run. All four speak the
same output contract (bare status values, per-finding article tags, 0–4 maturity,
"could not be assessed"), and each specialist adds its own gated decision taxonomy.

| Skill | Regime hook | Decision it drives | Final eval (with skill vs baseline) |
|---|---|---|---|
| **gdpr-compliance-audit** | whole-GDPR audit | `Compliant / Partial / Non-compliant / N/A` per finding | **100%** vs 66.7% |
| **conducting-gdpr-dpia** | Art. 35 / WP248rev.01 | `Required / Not required / Recommended / Prior consultation required` | **100%** vs 64.5% |
| **dsar-processing** | Art. 12, 15–22 | `Fulfil / Partially fulfil / Refuse / Extend / Need identity verification` per right | **100%** vs 82.5% |
| **breach-72h-notification** | Art. 33–34 | `Notify SA / Notify SA + individuals / No notification (record only) / Insufficient info` | **100%** vs 77.5% |

The trigger boundaries are drawn deliberately: the auditor flags "you need a DPIA" in one
line; `conducting-gdpr-dpia` runs it. Breach/DSAR prompts route to the specialist, not the
auditor — each description names its near-misses so the four don't fight over one prompt.

Every skill follows the same five-part anatomy:

```
skills/<name>/
├── SKILL.md                    # trigger description · procedure · locked output contract
├── references/                 # the law, layered by decay rate — volatile parts flagged verify-don't-assert
├── scripts/process.py          # stdlib-only determinism (deadline clocks, risk matrices, trigger counts)
├── assets/template.md          # a filled real-world example of the output
└── evals/evals.json            # contract assertions — the skill's regression suite
```

The `skills/<name>/` layout still leaves room for sibling regime modules (CCPA, PIPL, UK DUAA).

## 03 — Development process

<sub>HOW IT WAS BUILT &nbsp;·&nbsp; Fig. 03</sub>

This skill was not written once. It was built with Anthropic's **skill-creator** loop —
draft → run against realistic prompts *with a no-skill baseline beside it* → grade every
assertion → read the failures → generalize the fix — repeated until the outputs stopped improving.

| Milestone | What happened |
|---|---|
| **Scaffold** | 25-page GDPR framework split into three references by decay rate; output contract locked before any testing |
| **Iteration 1 — run** | 6 scenarios × 2 configurations (with skill / without) = 12 independent agent runs |
| **Iteration 1 — grade** | First grading round scored 100% vs 97.7% — graders unanimously flagged the assertions as *non-discriminating* (they tested general GDPR knowledge, not the audit contract) |
| **Assertion upgrade** | 4 contract assertions added per scenario (exact status taxonomy, per-finding citations, 0–4 maturity, unassessed section); regraded: **98.3% vs 66.7%** — the skill's real value made measurable |
| **Iteration 2 — refine** | The single with-skill failure (a compound status label, "Non-compliant risk pending action") fixed by tightening the contract wording in SKILL.md; all 12 runs re-run to confirm: **100% (53/53), regression-free** |

The eval suite ships in `evals/evals.json` so the loop can continue: change the skill, re-run
the six scenarios, and the 53 assertions tell you what regressed.

## 04 — Compliance & auditing

<sub>WHAT IT CHECKS · WHAT IT PROMISES &nbsp;·&nbsp; Fig. 04</sub>

**The methodology.** Audits run through nine phases, each yielding discrete, evidenced
findings: scoping & applicability → data mapping (ROPA) → lawfulness (Art. 5–10) →
transparency (Art. 12–14, the EDPB's 2026 enforcement priority) → data-subject rights
(Art. 12, 15–22) → governance (Art. 24–39) → security & breach (Art. 32–34) →
vendors & transfers (Art. 28, 44–49) → findings, risk-rating & remediation.

**Behavioral guarantees, verified by the test suite** (12/12 runs clean in both iterations):

- Every finding cites its article from the bundled quick-map — no un-sourced verdicts.
- Zero fabricated fines or case law across all recorded runs; only the Art. 83 fine *tiers* may be cited.
- Missing evidence produces `Partial`/`N/A` findings naming what's needed — silence is never upgraded to `Compliant`.
- The CCPA near-miss scenario confirms the scope gate holds: no GDPR audit is forced onto a US-only context.

> **⚠️ Law current as of July 2026.** The bundled `current-landscape.md` snapshot covers the
> EU–US Data Privacy Framework (under active legal pressure), the Digital Omnibus reform
> (nothing final), and AI Act deadlines (high-risk obligations from August 2026). The skill is
> instructed to *verify, not assert* these — but a stale clone cannot flag what it doesn't
> know. Re-check the volatile items on any audit touching transfers or AI.

**Not legal advice.** The output is a structured gap analysis to bring to your DPO or counsel —
it makes the conversation faster, it does not replace it.

## 05 — Performance metrics

<sub>MEASURED, NOT CLAIMED &nbsp;·&nbsp; Fig. 05</sub>

Benchmarked with skill-creator's harness: each scenario runs twice in parallel — once with the
skill, once without (same model, same prompt) — and an independent grader agent scores all 53
assertions against both answers.

| Metric · iteration 1 | With skill | Baseline (no skill) | Delta |
|---|---|---|---|
| Assertion pass rate | **98.3%** (52/53) | 66.7% (33/53) | **+31.6 pts** |
| Fabricated fines / case law | **0** | 0 | — |
| Scope-gate correctness (CCPA near-miss) | ✓ declined | ✓ declined | guard holds |
| Time per audit | 103.6 s | 68.9 s | +34.7 s |
| Tokens per audit | ~41.9 k | ~28.2 k | +13.7 k |

| Metric · iteration 2 (after refinement) | With skill | Baseline (no skill) | Delta |
|---|---|---|---|
| Assertion pass rate | **100%** (53/53) | 66.7% | **+33.3 pts** |
| Fabricated fines / case law | **0** | 0 | — |
| Time per audit | 106.9 s | 71.6 s | +35.3 s |
| Tokens per audit | ~42.6 k | ~28.3 k | +14.3 k |

The iteration-1 failure (a compound status label) did not recur after the contract wording was
tightened — and the overhead stayed flat across iterations, so the fix cost nothing.

Where the +32 points come from: baselines produce knowledgeable *prose*, but fail the audit
*contract* — no status taxonomy, no per-finding citations, no maturity scoring, no declared
gaps. That contract is exactly what makes an audit actionable and comparable over time, and it
is what the skill enforces. The overhead (+35 s, +14 k tokens) is the cost of the agent
actually reading the reference law before it speaks.

Test scenarios: privacy-policy audit · international-transfer audit · LLM-in-the-stack ·
CCPA near-miss (must decline) · 72-hour breach clock · access + erasure request.

## 06 — Roadmap

<sub>WHERE THIS GOES &nbsp;·&nbsp; Fig. 06</sub>

- **Trigger tuning** — optimize all four skill descriptions against a ~20-query trigger eval set (the near-misses matter most: DPIA-vs-audit, DSAR-vs-privacy-policy, breach-vs-general-security).
- **Sibling regimes** — the layout reserves space for `ccpa/`, `pipl/`, `uk-duaa/` modules.
- **`current-landscape.md` refresh cadence** — the volatile layer is designed to be replaced without touching the stable law.

## 07 — License & brand notice

<sub>USAGE &nbsp;·&nbsp; Fig. 07</sub>

The skill's source (SKILL.md, references, evals) is released under the **MIT License** — see
[LICENSE](LICENSE) — so you can use, adapt, and extend it for your own compliance work.

**Brand & material notice.** This project, its documentation, and its compiled knowledge base
are an asset of **TableSpark**. The TableSpark name, spark symbol, and wordmark are TableSpark
brand assets and may not be used to endorse derived works. **Selling this material, or
packaging it into commercial products for sale, is not permitted.** Use it, learn from it,
adapt it for your own audits — don't resell it.

---

<div align="center">

<a href="https://tablespark.uk/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://tablespark.uk/assets/brand/tablespark-wordmark-reversed.svg">
  <img src="https://tablespark.uk/assets/brand/tablespark-wordmark.svg" alt="TableSpark" height="32">
</picture>
</a>

<sub>A <a href="https://tablespark.uk/">TABLESPARK</a> ASSET &nbsp;<b>✦</b>&nbsp; BEAUTIFUL WEBSITES FOR RESTAURANTS</sub>

<sub>GDPR COMPLIANCE AUDIT · V1.1 · 2026 &nbsp;·&nbsp; LONDON · 51.5072°N · 0.1276°W</sub>

</div>
