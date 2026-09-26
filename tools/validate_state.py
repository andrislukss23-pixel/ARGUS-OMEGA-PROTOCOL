#!/usr/bin/env python3
"""Validate ARGUS repository status invariants using only the Python standard library."""

from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = json.loads((ROOT / "argus_working_state.json").read_text(encoding="utf-8"))
errors: list[str] = []

def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)

canonical = STATE["canonical"]
post = STATE["post_canonical"]

require(canonical["version"] == "v0.35", "canonical version must remain v0.35")
require(canonical["ledger_through"] == "T1422", "canonical ledger must remain frozen through T1422")
require(canonical["status"] == "PROVISIONAL", "canonical status must remain PROVISIONAL")
require(post["latest_recovered_working_boundary"] == "T1430-X62", "working boundary must be T1430-X62")
require(post["defence_patch"] == "OMEGA-HARD R61", "latest recovered defence patch must be OMEGA-HARD R61")
require(post["disposition"] == "PROVISIONAL LIMITED_SURVIVOR", "R61 disposition mismatch")
require(post["t1431"].startswith("RESERVED"), "T1431 must remain reserved")
require(STATE["external_validation"] == "NOT ESTABLISHED", "external validation must not be silently promoted")
require(STATE["reality_veto"] == "ABSOLUTE", "reality veto must remain ABSOLUTE")

for rel in ("README.md", "README_ARGUS_OMEGA.md", "STATUS.md"):
    text = (ROOT / rel).read_text(encoding="utf-8")
    require("v0.35" in text, f"{rel}: missing v0.35 canonical marker")
    require("T1422" in text, f"{rel}: missing T1422 canonical boundary")
    require("T1430-X62" in text, f"{rel}: missing T1430-X62 working boundary")
    require("T1431" in text and "RESERVED" in text, f"{rel}: T1431 reservation not explicit")

gaps = (ROOT / "docs" / "PROVENANCE_GAPS.md").read_text(encoding="utf-8")
require("DO NOT INVENT DETAILS" in gaps, "provenance-gap anti-invention control missing")

if errors:
    for error in errors:
        print(f"FAIL: {error}")
    raise SystemExit(1)

print("ARGUS repository-state invariants: PASS")
print("canonical=v0.35/T1422")
print("post_canonical=T1430-X62/R61 PROVISIONAL LIMITED_SURVIVOR")
print("T1431=RESERVED")
