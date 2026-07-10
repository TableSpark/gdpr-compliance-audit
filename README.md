`npx skills add TableSpark/gdpr-compliance-audit`

**English** | [简体中文](README.zh-CN.md)

# gdpr-compliance-audit

An agent skill that audits an organization, system, product, or policy for **GDPR compliance**
and returns structured, article-cited findings with a risk rating, a 0–4 maturity score per
domain, and an owner-ready remediation plan.

Give it a pasted privacy notice, a vendor stack, a described data flow, an AI feature, a breach
scenario, or a whole organization. It works through a phased audit methodology (scoping →
data mapping → lawfulness → transparency → rights → governance → security/breach →
vendors/transfers → findings) and tags every finding with the specific GDPR article.

## Install

```bash
# cross-agent install from this repo (Claude Code, Codex, Cursor, 60+ agents)
npx skills add TableSpark/gdpr-compliance-audit

# target Claude Code specifically, installed globally
npx skills add TableSpark/gdpr-compliance-audit -a claude-code -g
```

## Scope and limitations

- **GDPR / EU data protection only.** It deliberately refuses to force a GDPR audit onto
  CCPA-only, PIPL, or other-regime questions — it will say GDPR doesn't apply and stop.
- **Not legal advice.** Output is a structured gap analysis to bring to your DPO or counsel.
- It only assesses what the evidence you provide supports; missing evidence becomes
  "what could not be assessed", never silent compliance.
- It will not estimate fine amounts or cite enforcement cases — by design.

## ⚠️ Current as of July 2026

This skill encodes law that changes. The bundled `references/current-landscape.md` describes
the state of the volatile items in **July 2026** — before relying on any of these, verify the
live status:

- **EU–US Data Privacy Framework (DPF)** — under active legal pressure; check the official DPF
  list and any adequacy re-examination.
- **The Digital Omnibus reform** — GDPR amendments in flight, nothing final.
- **AI Act deadlines** — high-risk obligations phasing in from August 2026.

The skill itself is instructed to flag these as "verify, don't assert", but a stale copy of
this repo cannot flag what it doesn't know. Re-check the volatile items on any audit that
touches transfers or AI.

## Layout

```
skills/gdpr-compliance-audit/
├── SKILL.md                    # trigger description + audit procedure + output schema
├── references/
│   ├── articles.md             # scope, principles, lawful bases, rights, obligations, article quick-map
│   ├── audit-phases.md         # the Phase 0–8 audit methodology + maturity scale
│   └── current-landscape.md    # the volatile stuff (DPF, Digital Omnibus, AI Act) — decays!
├── scripts/
└── evals/evals.json            # test prompts + assertions used to develop the skill
```

The `skills/<name>/` layout leaves room for sibling regime modules later (CCPA, PIPL, UK DUAA).

## License

MIT — see [LICENSE](LICENSE).
