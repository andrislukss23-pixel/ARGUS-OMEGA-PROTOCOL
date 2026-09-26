# Unmapped Internal-Synthetic Continuation — 27 September 2026

**Status:** PRESERVED WITHOUT LEDGER-ID PROMOTION

Useful findings were recovered from conversation history, but the T1430-X / OMEGA-HARD identifier mapping is incomplete or conflicting. ARGUS provenance rules prohibit inventing identifiers merely to make the history look continuous.

## Recovered failure classes and repair directions

- **Confused deputy:** bind authorization to initiator, deputy, purpose, audience, scope, and effect; reauthorize at execution.
- **Irreversible side effects:** internal rollback cannot undo sent messages, secret disclosure, external deletion, physical actuation, or third-party mutation.
- **External-world divergence:** restored internal state does not imply restored external reality.
- **Shadow-state blindness:** caches, queues, replicas, delegated credentials, retry buffers, and third-party state may survive nominal cleanup.
- **Revocation cascades:** propagate authority epochs and re-check deferred work at execution.
- **Evidence garbage collection:** preserve retention tombstones and record non-silent evidence loss.
- **Economic/resource denial:** account for verifier/attacker cost asymmetry and degraded verification modes.
- **Third-party semantic drift:** use semantic canaries, runtime identity, version/effect binding, and stale-assumption invalidation.
- **Display/execution mismatch:** bind displayed/approved object to the executed effect.
- **Object-identity reuse:** use immutable generations/epochs rather than stable names alone.
- **Nondeterministic replay:** record replay envelopes and explicitly mark uncaptured external state.
- **Cryptographic-verification cost:** bound verification work and preserve the distinction between authenticated provenance and substantive truth.

These remain recovered internal findings, not canonical ledger entries.
