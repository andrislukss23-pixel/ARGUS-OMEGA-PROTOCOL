# ARGUS Ω — Repository Status

**Repository status date:** 27 September 2026

## Canonical release

- **Canonical version:** ARGUS Ω v0.35 / Omega-Hepta-Prime
- **Canonical ledger boundary:** through T1422
- **Canonical status:** PROVISIONAL
- **Validation domain:** INTERNAL-SYNTHETIC / METHOD-LEVEL ONLY
- **External scientific validation:** NOT ESTABLISHED
- **Physical-world validation:** NOT ESTABLISHED
- **Field/deployment validation:** NOT ESTABLISHED
- **Reality Gate:** CLOSED / WOUNDED
- **Reality veto:** ABSOLUTE
- **High-consequence operational authority:** NONE

The canonical v0.35/T1422 record remains frozen. Post-canonical work does not silently rewrite or promote the canonical release.

## Post-canonical working line

- **T1423:** preserved separately as a post-canonical internal experiment.
- **Recovered working-line boundary:** **T1430-X62**.
- **Latest recovered defence state:** **OMEGA-HARD R61**.
- **Disposition:** **PROVISIONAL LIMITED_SURVIVOR**.
- **T1431:** **RESERVED** for materially independent external clean-room validation.

A PASS in this line means the intended synthetic attack, wound, repair, or regression behavior was reproduced inside the represented test grammar. It does **not** mean external truth, safety, deployment fitness, or physical validation.

## T1430-X55 → X62 recovered attack sequence

| Test | Defence attacked | Recovered attack class | Disposition |
|---|---|---|---|
| T1430-X55 | R53 | Runtime-effective policy diverges from documented/formal policy | R53 WOUNDED |
| T1430-X56 | R54 | Bidirectional ledger/runtime divergence | R54 WOUNDED |
| T1430-X57 | R55 | Authority cycles, self-validation, and scope inflation | R55 WOUNDED |
| T1430-X58 | R56 | Cleanup leaves residual tokens, queues, caches, or irreversible external effects | R56 WOUNDED |
| T1430-X59 | R57 | Cleanup is non-quiescent; effects can continue across the cleanup boundary | R57 WOUNDED |
| T1430-X60 | R58 | Secrets, plugins, config, and supply-chain state can change effective policy | R58 WOUNDED |
| T1430-X61 | R59 | Clock/log ordering is not a reliable causal history by itself | R59 WOUNDED |
| T1430-X62 | R60 | Partitions can yield individually valid but semantically incompatible histories | R60 WOUNDED |

The repaired working state after X62 is **R61 / PROVISIONAL LIMITED_SURVIVOR**.

## R61 hardening contract

1. **Effective-state equivalence:** declared policy, ledger state, executable policy, and runtime effect must be compared rather than assumed equivalent.
2. **Bidirectional reconciliation:** ledger→runtime and runtime→ledger drift must both be detectable.
3. **No self-authorizing cycles:** authority or validation chains that depend on themselves do not gain independence credit.
4. **Residual-effect accounting:** revocation or cleanup must inventory queued authority, cached state, external effects, and irreversible actions.
5. **Quiescence boundary:** a cleanup/revocation claim is not licensed until in-flight and deferred paths are accounted for.
6. **Dynamic-dependency invalidation:** plugin, config, secret, package, runtime, or supply-chain changes invalidate stale trust assumptions.
7. **Causal-order humility:** log timestamps alone do not establish causality when clocks, buffering, replay, or partitions are unreliable.
8. **Fork-preserving conflict handling:** incompatible valid histories may not be silently collapsed by last-writer-wins; preservation itself carries storage, governance, and liveness costs.
9. **External-effect boundary:** internal rollback does not imply rollback of messages, disclosures, deletions, third-party mutations, or physical effects.
10. **MODEL_GAP remains live:** when the represented state graph cannot discriminate the real mechanism, ARGUS preserves MODEL_GAP rather than forcing a winner.

## Earlier hardening landmark — T1430-X16 / R15

T1430-X16 expanded the trusted-computing-base boundary beyond a small named kernel. Permanent controls include effective-TCB closure, checker common-mode accounting, build/bootstrap provenance, total-domain/exception semantics, represented-mediation boundaries, human-meaning binding, exception-path coverage, self-attestation limits, and resistance to agentic trust laundering.

## Provenance-protected continuation

Recovered high-value but incompletely mapped findings are preserved without invented identifiers: confused deputy, irreversible external effects, external-world divergence, shadow state, revocation cascades, evidence garbage collection, economic/resource denial, third-party semantic drift, display/execution mismatch, object-identity reuse, nondeterministic replay, and cryptographic-verification cost.

## Current epistemic boundary

> **POST-CANONICAL / INTERNAL-SYNTHETIC / METHOD-LEVEL research only.**

This is **not** a v0.36 release, external replication, physical validation, deployment/safety certification, proof of complete attack grammar, or elimination of unknown unknowns.

## T1431 reservation

T1431 remains reserved for a materially independent external validation event.

## Legacy root `patch ` file

The root file named `patch ` is a historical unapplied diff snapshot from the earlier X16/R15 working state. It is retained as provenance evidence but is superseded operationally by the applied repository state described here.

## Constitutional boundary

**Reality outranks the model. Survival is not proof. Internal synthetic success does not grant external authority.**
