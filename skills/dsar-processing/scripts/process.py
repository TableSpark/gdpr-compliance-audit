#!/usr/bin/env python3
"""DSAR deadline calculator (Art. 12(3)) — stdlib only.

Computes the one-month response deadline from the receipt date, plus the
two-month extension deadline and the date by which the extension notice must
be sent (within the first month).

Usage:
    echo '{"received": "2026-07-10", "extension": false}' | python3 process.py
    python3 process.py --demo

"One month" is calculated by calendar month per EDPB guidance: same day next
month, clamped to month end (e.g. 31 Jan -> 28/29 Feb).
"""
import calendar
import json
import sys
from datetime import date


def add_months(d, months):
    m = d.month - 1 + months
    year = d.year + m // 12
    month = m % 12 + 1
    last = calendar.monthrange(year, month)[1]
    return date(year, month, min(d.day, last))


def compute(received_iso, extension=False):
    received = date.fromisoformat(received_iso)
    base_due = add_months(received, 1)
    result = {
        "received": received.isoformat(),
        "base_deadline": base_due.isoformat(),
        "extension_taken": bool(extension),
    }
    if extension:
        result["extended_deadline"] = add_months(received, 3).isoformat()
        # notice must go out within the first month
        result["extension_notice_by"] = base_due.isoformat()
    return result


DEMO = {"received": "2026-07-10", "extension": True}


def main():
    if "--demo" in sys.argv:
        data = DEMO
    else:
        raw = sys.stdin.read().strip()
        data = json.loads(raw) if raw else DEMO
    print(json.dumps(compute(data["received"], data.get("extension", False)), indent=2))


if __name__ == "__main__":
    main()
