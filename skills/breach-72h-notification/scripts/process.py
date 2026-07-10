#!/usr/bin/env python3
"""Breach 72-hour clock + notification decision mapper (Art. 33-34) — stdlib only.

Computes the 72h SA-notification deadline from the awareness timestamp and maps
a risk level (+ encryption knowledge) to the Art. 33/34 decision value.

Usage:
    echo '{"aware_at": "2026-07-10T09:00:00", "risk": "high", "encryption_known": true}' | python3 process.py
    python3 process.py --demo

risk ∈ none | risk | high
encryption_known: if false and risk not clearly 'none', decision -> Insufficient info
"""
import json
import sys
from datetime import datetime, timedelta

DECISIONS = {
    "none": "No notification (record only)",
    "risk": "Notify SA",
    "high": "Notify SA + individuals",
}


def decide(aware_at_iso, risk, encryption_known=True, now_iso=None):
    aware = datetime.fromisoformat(aware_at_iso)
    deadline = aware + timedelta(hours=72)
    risk = str(risk).strip().lower()
    if risk not in DECISIONS:
        raise ValueError(f"risk must be one of {sorted(DECISIONS)}, got {risk!r}")

    if not encryption_known and risk != "none":
        decision = "Insufficient info"
    else:
        decision = DECISIONS[risk]

    now = datetime.fromisoformat(now_iso) if now_iso else None
    result = {
        "aware_at": aware.isoformat(),
        "sa_deadline_72h": deadline.isoformat(),
        "risk_level": risk,
        "encryption_status_known": bool(encryption_known),
        "decision": decision,
        "notify_sa": decision in ("Notify SA", "Notify SA + individuals"),
        "notify_individuals": decision == "Notify SA + individuals",
        "record_required": True,  # Art. 33(5) always
    }
    if now is not None:
        result["already_past_deadline"] = now > deadline
        if now > deadline:
            result["note"] = "Past 72h — notification must explain the delay (Art. 33(1))."
    return result


DEMO = {"aware_at": "2026-07-10T09:00:00", "risk": "high", "encryption_known": True}


def main():
    if "--demo" in sys.argv:
        data = DEMO
    else:
        raw = sys.stdin.read().strip()
        data = json.loads(raw) if raw else DEMO
    print(json.dumps(
        decide(data["aware_at"], data["risk"],
               data.get("encryption_known", True), data.get("now")),
        indent=2))


if __name__ == "__main__":
    main()
