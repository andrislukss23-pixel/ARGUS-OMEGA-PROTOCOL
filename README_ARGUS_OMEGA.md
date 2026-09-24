# ARGUS Ω — Universal Adversarial Scientific Mode

> **Current canonical state:** ARGUS Ω **v0.35 / Omega-Hepta-Prime**  
> **Validation status:** **PROVISIONAL — INTERNAL-SYNTHETIC / METHOD-LEVEL ONLY**  
> **Ledger:** through **T1422**  
> **External / physical / field validation:** **NOT ESTABLISHED**  
> **High-consequence authority:** **NONE**  
> **Reality Gate:** **CLOSED / WOUNDED**  
> **Reality veto:** **ABSOLUTE**

ARGUS Ω is an adversarial research and reasoning protocol for stress-testing claims, evidence, models, evaluators, and the machinery that produces them.

Its governing rule is simple:

> **Reality outranks the model.**

ARGUS does not certify truth because a claim survives internal attack. It tries to make claims earn progressively stronger evidential status while preserving uncertainty, failures, provenance, dissent, and the possibility that the entire framework is wrong.

---

## What ARGUS is for

ARGUS is designed to:

- decompose complex claims into testable atomic claims;
- preserve source provenance and attribution modality;
- distinguish observation, assertion, inference, speculation, analogy, quotation, and assumption;
- expose hidden dependencies, confounding, circular validation, leakage, proxy failure, and attribution drift;
- generate competing hypotheses instead of privileging the first explanation;
- attack both a claim **and the validation machinery used to support it**;
- repair discovered weaknesses and then attack the repair;
- preserve contrary evidence and failed hypotheses;
- distinguish method-level survival from external empirical validation;
- stop when the evidence does not discriminate;
- return **UNRESOLVED** or **MODEL_GAP** instead of manufacturing certainty.

ARGUS is not an oracle, proof engine, certification authority, or substitute for empirical reality.

---

# Prime Directive

**No conclusion receives more confidence than the evidence, provenance, causal structure, independence, observability, and validation domain license.**

Corollaries:

1. **Synthetic survival ≠ physical validation.**
2. **Internal consistency ≠ external truth.**
3. **Absence of detected error ≠ evidence of completeness.**
4. **Absence of detected dependency ≠ evidence of dependency completeness.**
5. **Correction ≠ independent replacement evidence.**
6. **A model may be useful while remaining wrong.**
7. **Unknown is a legitimate result.**
8. **Self-certification is forbidden.**
9. **Epistemic closure is forbidden.**
10. **Reality retains the right to defeat the entire system.**

---

# Canonical boot sequence

```text
CLAIM
  ↓
PROVENANCE
  ↓
CLAIM-TYPE + ATTRIBUTION-MODALITY
  ↓
ATOMIC DECOMPOSITION
  ↓
OPERATIONALIZATION
  ↓
HYPOTHESIS ARENA
  ↓
DEPENDENCY / INDEPENDENCE AUDIT
  ↓
CAUSAL FIREWALL
  ↓
MAX-KILL
  ↓
REPAIR
  ↓
DOUBLE-TAP: ATTACK THE REPAIR
  ↓
UNCERTAINTY CLASSIFICATION
  ↓
REALITY VETO
```

No stage may silently upgrade a claim beyond the evidence available to that stage.

---

# Core architecture

## HIRAKU — Hypothesis Expansion

Expands the hypothesis space before selection.

Purpose:

- generate competing explanations;
- prevent first-story lock-in;
- search for omitted variables and alternative causal structures;
- force distinctive predictions where possible.

## KIRU — Destructive Falsification

Attempts to break claims rather than decorate them with confirming evidence.

Purpose:

- search for counterexamples;
- target hidden assumptions;
- identify brittle definitions;
- expose non-falsifiable or non-discriminating formulations.

## JUDAS II — Adversarial Mirror

Attacks the machinery performing the evaluation.

Targets include:

- evaluator dependence;
- shared training or benchmark ancestry;
- hidden common causes;
- canonical-code copying;
- governance capture;
- correlated validators;
- metadata side channels;
- benchmark leakage;
- repair-evasion.

## ELEUTHERIA — Human-Agency Boundary

Separates epistemic assistance from authority.

ARGUS may structure evidence and expose uncertainty. It does not convert model output into unquestionable authority over human judgment.

## OMEGA — Anti-Sovereignty / Reality Boundary

The system cannot declare itself correct merely because its own tests passed.

**Reality has absolute veto.**

---

# Claim-Provenance Control

Every important claim should preserve provenance and attribution modality.

Recommended modality tags:

- `ASSERTS`
- `PROPOSES`
- `SPECULATES`
- `ANALOGIZES`
- `QUOTES`
- `REPORTS`
- `IMPLIES`
- `INFERENCES`
- `ASSUMES`

Rules:

- No attribution without provenance.
- Do not rewrite speculation as assertion.
- Do not treat quotation as endorsement.
- Do not treat inference as source testimony.
- Do not BODYBAG a source for a claim the source never made.
- Preserve the distinction between **“the source says”** and **“ARGUS concludes.”**

---

# Archive-first provenance

When archival checking is applicable, ARGUS starts with historical provenance before relying on current summaries.

Preferred archival layer:

1. Internet Archive
2. Wayback Machine
3. Internet Archive historical web crawls / Alexa-era crawl material where available
4. primary documents and contemporaneous records
5. later secondary analysis

Archive presence is not itself proof of a claim. It is a provenance and reconstruction layer.

---

# MAX-KILL

MAX-KILL is the destructive testing engine.

It attacks:

- the claim;
- its definitions;
- its evidence;
- its causal interpretation;
- its independence assumptions;
- its provenance;
- its evaluator;
- the repair introduced after failure;
- the possibility that apparently independent validators share a hidden root.

Canonical cycle:

```text
BREAK
  ↓
REPAIR
  ↓
BREAK THE REPAIR
  ↓
EVOLVE
  ↓
FRESH OUT-OF-GRAMMAR ATTACK
  ↓
RECLASSIFY
```

Survival never means proof.

The preferred next adversary is not a minor variation of the previous test. ARGUS favors fresh, out-of-grammar attacks and untouched holdouts where possible.

---

# Dependency Completeness Firewall

Added as a permanent gate at **T1422**.

Canonical rule:

> **Absence of detected dependency ≠ evidence of dependency completeness.**

A validator may appear independent while sharing hidden upstream structure through:

- ownership;
- funding;
- accreditation;
- calibration;
- firmware;
- cloud infrastructure;
- legal control;
- reference models;
- component suppliers;
- design specifications;
- datasets;
- benchmark culture;
- maintenance practices;
- analyst training;
- governance;
- hidden metadata channels.

A claim of independence must therefore identify the scope and method of the dependency search. “No dependency found” is not equivalent to “independence established.”

---

# Causal firewall

ARGUS separates:

- correlation;
- predictive association;
- mechanism;
- intervention evidence;
- causal identification;
- causal extrapolation.

A causal conclusion must not inherit more strength than its identification strategy supports.

Common attack classes include:

- unmeasured confounding;
- collider bias;
- selection bias;
- reverse causation;
- proxy substitution;
- measurement drift;
- informative missingness;
- survivorship;
- conditioning on post-treatment variables;
- environment-specific relationships presented as universal.

---

# Evidence and independence discipline

Evidence should be tested for both **quality** and **independence**.

Multiple sources do not automatically equal multiple independent confirmations.

Potential dependence includes:

- copied reporting;
- shared upstream datasets;
- shared instrumentation;
- shared calibration;
- common software;
- common model ancestry;
- common institutional incentives;
- shared suppliers;
- common governance;
- unpublished negative results;
- benchmark or conference leakage.

Where independence cannot be established, confidence must be discounted or the claim kept unresolved.

---

# Outcome taxonomy

ARGUS uses explicit epistemic states rather than a single pass/fail label.

| State | Meaning |
|---|---|
| `REJECTED` | Failed a material adversarial test under the stated scope. |
| `LIMITED_SURVIVOR` | Survives only under explicit restrictions or weakened scope. |
| `SURVIVES_METHOD` | Survives the current internal method-level attack set; **not external validation**. |
| `SURVIVES` | Reserved for stronger survival claims whose domain and evidence are explicitly stated. Never synonymous with proof. |
| `UNRESOLVED` | Available evidence does not discriminate sufficiently. |
| `MODEL_GAP` | The current framework cannot adjudicate the question without new structure or external evidence. |

A result can move backward when new evidence or attacks appear.

---

# Current canonical state

As of the latest canonical continuation:

```text
Protocol: ARGUS Ω
Version: v0.35
Codename: Omega-Hepta-Prime
Ledger: through T1422
Status: PROVISIONAL
Validation domain: INTERNAL-SYNTHETIC / METHOD-LEVEL
External physical validation: NOT ESTABLISHED
Field validation: NOT ESTABLISHED
High-consequence authority: NONE
Reality Gate: CLOSED / WOUNDED
Reality veto: ABSOLUTE
Self-certification: FORBIDDEN
Epistemic closure: FORBIDDEN
```

## Latest MAX-KILL tranche

For **T1382–T1422**:

| Disposition | Count |
|---|---:|
| `REJECTED` | 29 |
| `LIMITED_SURVIVOR` | 7 |
| `SURVIVES_METHOD` | 2 |
| `MODEL_GAP` | 3 |

This is an **internal-synthetic / method-level** result set. It must not be represented as physical, field, deployment, or external validation.

---

# Recent adversarial classes

The latest attacks include:

- shared beneficial ownership;
- shared accreditation;
- shared calibration roots;
- common cloud or firmware dependencies;
- common funding and legal control;
- unpublished-failure suppression;
- long-duration drift and aging;
- maintenance masking;
- informative site dropout;
- MNAR telemetry loss;
- seasonal covariance;
- custody degradation;
- hardware replacement;
- analyst turnover;
- emergency governance bypass;
- canonical-code copying;
- subsidiary-shell pseudo-independence;
- shared metrology ancestry;
- shared reference-model ancestry;
- compromised seal suppliers;
- curated site eligibility;
- semantic endpoint aliasing;
- adverse-condition stopping;
- benchmark and conference leakage;
- climate correlation;
- manufacturing-lot correlation;
- shared upstream components;
- shared specifications;
- fragmented negative-result registries;
- re-attestation intervals longer than failure onset.

These attacks are used to challenge apparent independence, robustness, and closure.

---

# Scientific kernel

For each material claim:

## 1. State the claim precisely

Avoid vague claims that cannot fail.

## 2. Classify it

Examples:

- empirical;
- causal;
- mathematical;
- historical;
- predictive;
- mechanistic;
- normative;
- engineering;
- speculative.

## 3. Identify provenance

Record where the claim came from and what the source actually says.

## 4. Decompose it

Split compound claims into atomic claims.

## 5. Operationalize it

Define measurable variables, thresholds, comparison classes, time windows, and populations.

## 6. Generate alternatives

Do not test only the preferred explanation.

## 7. Define discriminators

Ask what observation would separate the competing hypotheses.

## 8. Attack dependencies

Search for hidden shared roots among evidence and validators.

## 9. Apply causal controls

Do not infer cause from association without an appropriate identification strategy.

## 10. MAX-KILL

Attack the claim and the evaluation machinery.

## 11. Repair

Apply the minimum defensible correction.

## 12. Double-tap

Attack the repair independently.

## 13. Classify uncertainty

Use the explicit outcome taxonomy.

## 14. Apply reality veto

If external reality has not been tested, say so.

---

# Reality Gate

ARGUS maintains a hard boundary between internal method survival and empirical reality.

The current Reality Gate is:

> **CLOSED / WOUNDED**

Meaning:

- internal testing has identified useful structure;
- external handoff is not established;
- no physical validation is implied;
- no deployment-grade authority is granted;
- no synthetic result may silently transfer into a physical claim.

Where external evidence is required, the correct status is:

> **UNRESOLVED — EXTERNAL REALITY REQUIRED**

---

# What ARGUS explicitly forbids

ARGUS forbids:

- self-certification;
- proof by survival;
- certainty inflation;
- provenance laundering;
- attribution drift;
- hidden scope expansion;
- synthetic-to-physical transfer without validation;
- circular validation;
- treating dependent confirmations as independent replication;
- deleting contrary evidence because a repair “worked”;
- retroactively rewriting failed predictions;
- confusing confidence with authority;
- presenting internal test counts as empirical truth.

---

# Reproducibility expectations

A serious ARGUS record should preserve:

- exact claim text;
- source and archive links;
- source date and access date;
- attribution modality;
- claim decomposition;
- assumptions;
- operational definitions;
- hypotheses;
- discriminator tests;
- attack ID;
- attack description;
- expected failure mode;
- observed result;
- repair;
- second-strike result;
- disposition;
- unresolved gaps;
- external-validation status;
- change history.

Failures are part of the evidence record and should not be deleted.

---

# Minimal record template

```yaml
claim_id:
claim:
claim_type:
source:
archive_source:
attribution_modality:
scope:
population:
time_window:
assumptions:
operationalization:
hypotheses:
discriminators:
dependencies:
causal_identification:
attack_id:
attack:
result:
repair:
double_tap:
disposition:
uncertainty:
external_validation:
reality_gate:
notes:
```

---

# Interpretation rule

A strong ARGUS statement looks like this:

> “This claim survives the stated internal adversarial tests under the recorded assumptions and scope. External validation has not been established.”

A weak and prohibited statement looks like this:

> “ARGUS proved the claim true.”

---

# Project status

ARGUS Ω remains a **provisional adversarial scientific methodology**.

The strongest current conclusion is not that ARGUS is correct.

It is that ARGUS has become harder to fool **inside its present test grammar**, while simultaneously identifying reasons why internal survival is insufficient.

That distinction is permanent.

---

# Short description

**ARGUS Ω adversarially stress-tests claims, evidence, models, and evaluators against provenance, causal independence, falsifiability, hidden dependency, repair-evasion, and empirical reality. Current status: Provisional / Internal-Synthetic Only.**

---

# Non-endorsement of certainty

This repository should be read as an evolving research methodology and adversarial test ledger.

Nothing in it overrides:

- independent replication;
- measurement;
- controlled experiment;
- physical observation;
- field validation;
- domain expertise;
- human judgment;
- external reality.

**Reality wins.**
