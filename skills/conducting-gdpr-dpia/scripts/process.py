#!/usr/bin/env python3
"""DPIA risk scorer (Art. 35(7)(c)/(d)) — stdlib only.

Scores likelihood x severity into a risk level and flags when residual risk
forces Art. 36 prior consultation. Feed it a JSON risk register on stdin, or
run with --demo.

Usage:
    echo '{"risks":[...]}' | python3 process.py
    python3 process.py --demo

Input schema (per risk):
    {"id": "R1", "harm_type": "material",
     "likelihood": "Likely", "severity": "Significant",
     "residual_likelihood": "Possible", "residual_severity": "Limited"}
residual_* are optional; if present, a residual level is computed too.
"""
import json
import sys

LIKELIHOOD = {"remote": 1, "possible": 2, "likely": 3, "almost certain": 4}
SEVERITY = {"negligible": 1, "limited": 2, "significant": 3, "maximum": 4}
# product (1..16) -> level band
LEVELS = ["Low", "Medium", "High", "Very High"]


def _norm(d, value, field):
    key = str(value).strip().lower()
    if key not in d:
        raise ValueError(f"{field!r} must be one of {sorted(d)}, got {value!r}")
    return d[key]


def score(likelihood, severity):
    p = _norm(LIKELIHOOD, likelihood, "likelihood") * _norm(SEVERITY, severity, "severity")
    if p <= 2:
        return "Low"
    if p <= 6:
        return "Medium"
    if p <= 9:
        return "High"
    return "Very High"


def assess(register):
    out = []
    prior_consultation = False
    for r in register.get("risks", []):
        rec = {
            "id": r.get("id", "?"),
            "harm_type": r.get("harm_type", "unspecified"),
            "inherent_level": score(r["likelihood"], r["severity"]),
        }
        if "residual_likelihood" in r and "residual_severity" in r:
            rec["residual_level"] = score(r["residual_likelihood"], r["residual_severity"])
            if rec["residual_level"] in ("High", "Very High"):
                prior_consultation = True
        out.append(rec)
    return {
        "risks": out,
        "prior_consultation_required": prior_consultation,
        "decision_hint": "Prior consultation required" if prior_consultation else None,
    }


DEMO = {
    "risks": [
        {"id": "R1", "harm_type": "material", "likelihood": "Likely",
         "severity": "Significant", "residual_likelihood": "Possible",
         "residual_severity": "Limited"},
        {"id": "R2", "harm_type": "non-material", "likelihood": "Almost certain",
         "severity": "Maximum", "residual_likelihood": "Likely",
         "residual_severity": "Significant"},
    ]
}


def main():
    if "--demo" in sys.argv:
        data = DEMO
    else:
        raw = sys.stdin.read().strip()
        data = json.loads(raw) if raw else DEMO
    print(json.dumps(assess(data), indent=2))


if __name__ == "__main__":
    main()
