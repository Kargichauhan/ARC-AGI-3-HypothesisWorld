# Compatibility-aware disagreement — 2026-11-02

Decision: **reject the mechanism; merge this negative research record**. Explicit
contradiction scoring fixes supplied-rule diagnostic choices but reduces public
completion from two levels to one. Candidate code, 13 test cases and runner were
archived under ignored results and removed. Production matches main.

## Hypothesis and fixed gates

Hypothesis: compatible descriptions should not count as competing predictions;
scoring actual contradictions improves falsifying intervention choice and completion.
This directly compares partial predictions without inventing unspecified outcomes or
likelihoods, unlike September 17's rejected posterior-rollout estimator. It leaves
belief learning intact, unlike October 21's strict falsification and November 1's
predictive credibility weighting. It tests a new estimator for a previously observed
problem, not a new discovery that compatible labels can inflate entropy.

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation memory,
current fetched main/daily/research branches, research plans, report introductions,
relevant full reports and history. Connected GitHub search found no open PRs.
Original checkout was clean after slow status completion; used an isolated temporary
clone and left original tracked files untouched. No unmerged code or game-source
knowledge informed design. No subagents, threshold retuning or competition submission.

Protocol saved before implementation and measurement; all retention gates required:

- Three supplied-rule synthetic families, 200 paired seeds each: at least 95%
  diagnostic choices per family and at least 50 percentage points pooled improvement.
- Known-reward and known-hazard controls, 200 seeds each: baseline competence at
  least 95%, candidate loss at most five percentage points. Equal contradictory
  binary predictions score one; compatible/disjoint predictions score zero.
- Five cached public games, full F, seeds 0/1/2, 100 actions per run: at least one
  additional total level, no per-game summed regression, warm runtime at most 2x.
- Unit tests, formatting/lint, notebook source equality/compilation, independent
  trace audit and deterministic replay pass. A–E expansion conditional on all gates.

## Mechanism

Only `agent/hypotheses.py` changes production behavior. Let `Cij` be one when two
predictions disagree on at least one field specified by both, otherwise zero.
Use `min(1, 4 * sum(i<j, wi * wj * Cij))` instead of normalized label entropy.
None is a wildcard. Seven fields participate: changed, progress, terminal, motion,
appeared, disappeared, affected colour. Cross-field logical implications are not
inferred. Weights, updates, rejection, model, planner, proposals and RNG stay intact.

Four sets a balanced contradictory binary pair to one; multiway conflict can saturate.
This is a heuristic contradiction score, not information gain or a posterior.
Splitting a prediction's mass into identical copies preserves it, but adding a
compatible refinement can change normalized mass. The replacement also changes score
scale on already-incompatible sets: .8/.2 binary weights give .64 versus baseline
entropy .721928. This pilot does not isolate compatibility handling from that scaling.

## Synthetic evidence

Full F selector with default coefficients, varied action IDs/order/field values,
fixture RNG `20261102 + seed`, policy RNG `seed`. Diagnostic actions have two
opposed rules with weights .8/.2; distractors have four equally weighted compatible
nested descriptions. Controls supply eight observations per action to the unchanged
model, hypotheses and memory. No parameters were tuned after measurement.

| Family | Baseline correct / 200 | Candidate correct / 200 |
|---|---:|---:|
| Motion diagnostic | 0 | 200 |
| Appearance diagnostic | 0 | 200 |
| Progress diagnostic | 0 | 200 |
| Known-reward control | 200 | 200 |
| Known-hazard control | 200 | 200 |

Primary improvement is **100 percentage points**; controls preserve perfect choices.
All synthetic gates pass. These 2,000 arm/seed records are supplied-rule decisions,
not online task solves or independent ARC tasks. They establish the designed ranking
property, not whether useful conflicting hypotheses are acquired naturally.

## Public evidence

Official cached OFFLINE engine, `arc-agi==0.9.9`, `arcengine==0.9.3`. Reused the prior
local runtime/cache; recorded hashes of all game Python/metadata files and harness
Python files without reading game implementations for design. Alternated arm order
by seed. Primary cohort: **30 runs, 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 0 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 1** fails both completion gates. All 15 paired action sequences
change. Same-frame/nonpositive-progress transitions increase **595 → 664**.
Consecutive identical submitted action/data pairs decrease **744 → 495**; resets
remain in the sequence. These repeat counts are not the prior reports' selected-probe
metric, and no cross-day trace-equivalence claim is made.

Within baseline histories, replacing only information changes the top choice at
757/1,488 decisions; reversing the change on candidate histories changes 537/1,491.
These are conditional score comparisons, not off-policy completion estimates.
All 31,491 baseline and 31,566 candidate forecast rows change information value.
**No public forecast has zero conflict with positive label entropy**: the pure
compatible-only synthetic distractor is not encountered. Scores saturate in 2,327
baseline-history and 820 candidate-history forecasts. The lost vc33 seed first
changes its submitted action at index three; this does not identify a unique cause
of eventual failure. Scale changes and mixed compatible/incompatible populations
remain plausible confounds, not proven explanations.

Warm replay subprocess totals: **11.068 → 11.166 seconds (1.009x)**, including equal
shadow calculations, tracing and startup. Initial totals **22.843 → 11.426 seconds**
are startup-confounded. No isolated performance claim. No held-out benchmark access
or official Relative Human Action Efficiency result is claimed.

## Verification and disposition

Candidate: **28 tests pass** (13 new cases), formatting/lint pass, **10 notebook
modules** exactly match source and compile. Tests cover every field, wildcards,
disjoint clauses, duplicate mass splitting, boundedness/order, action/rejection
scope and unchanged evidence. Runner lint/closure bindings were fixed before any
measurements; policy source did not change between initial and replay cohorts.

Independent audit verifies **67,057 forecast rows**, all 2,000 synthetic records,
3,000 public actions and 2,979 public observations. It independently recomputes
ordered-pair conflict and grouped entropy, selector arithmetic, action legality,
selected coordinates, raw-pixel/state differences and final levels. It rebuilds
public hypothesis updates from observed prefixes and compares normalized prediction
weights, ignoring arbitrary hypothesis IDs. Source hashes match the measured manifest.
All seven compressed trace files replay exactly by decompressed SHA-256; six public
summaries and source manifests also match. Replay's additional 3,000 actions are
repeated evidence, not independent trials.

Archived patch/source/tests/runner and removed all candidate changes. Final baseline:
**15 tests pass**, formatting/lint and all **10 notebook checks pass**. Production
agent/tests/scripts/notebook configuration match main. Patch forward/reverse checks
pass. Only this report and the research-plan note are committed.

Reject the score replacement. Future disagreement research should first establish
naturally acquired, decision-relevant compatible alternatives and separate semantic
compatibility from score scaling; this pilot does not justify accumulating another
information heuristic on synthetic ranking alone.

Ignored evidence: `experiments/results/2026-11-02-compatible-disagreement/` contains
protocol, baseline method, compressed traces/replay, audit/analysis, source/dependency
manifests, validation and removed `candidate.patch`. Raw evidence is local, not pushed.
Patch SHA-256:
`3b8e285f644b5801d36fb3e17769f59d88351327209b0b930b20667dc699ff20`.
Reproduce by applying that patch to the base, restoring the archived baseline method
and protocol at the recorded ignored path, then running
`python experiments/run_compatible_disagreement.py --output <ignored-output-path>`
with the recorded cached games/framework/runtime. No network evaluation is required.
