# T1430-X16 — Effective-TCB / Reference-Monitor / Execution-Chain Extreme Proofing

**Classification:** POST-CANONICAL / INTERNAL-SYNTHETIC / METHOD-LEVEL
**Canonical v0.35/T1422 promoted:** No
**External validation claimed:** No
**T1431 consumed:** No

## Recovered wounds

1. **Effective-TCB closure failure** — a named kernel can remain correct while another component still violates the protected invariant.
2. **Checker common-mode failure** — multiple validators do not earn independence credit when they share specification, code/model ancestry, data, infrastructure, calibration, governance, or build chains.
3. **Build/bootstrap provenance gap** — correct source does not imply a correct executable.
4. **Total-domain / exception-semantics gap** — rules defined only on the happy path are not total invariants.
5. **Reference-monitor completeness overclaim** — complete mediation can only be claimed relative to the represented and observable action graph.
6. **Human-meaning / machine-policy mismatch** — a checker can perfectly enforce the wrong formalization.
7. **Exception-path authority escape** — emergency, maintenance, migration, admin, recovery, or override paths can bypass normal policy.
8. **Self-attestation failure** — a component cannot independently establish its own trustworthiness by reporting that it is trustworthy.
9. **Agentic trust laundering** — dependent agents can repeatedly relabel authority or provenance until weak evidence appears strong.

## R15 repair principle

> Any component whose arbitrary compromise can violate a protected invariant belongs to the effective TCB, regardless of label.

Later internal work progressed beyond this state; see repository `STATUS.md`.
