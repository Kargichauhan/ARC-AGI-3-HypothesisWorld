# Correspondence abstention — 2026-11-10

Decision: **reject the candidate; merge the negative research record**. A fixed
match-confidence margin suppresses symmetric identity assertions but discards all
correct correspondences in a coherent-motion control. Existing event semantics turn
abstentions into births and deaths, rather than representing unknown identity.
Candidate implementation and five tests were archived and removed before commit.

## Hypothesis and fixed criteria

Hypothesis: admitting an object match only when its similarity score exceeds every
competing admissible edge sharing either endpoint by at least 0.5 protects the causal
motion evidence consumed by outcome hypotheses without losing reliable matches.
Only this filter was added before the existing greedy assignment; original scoring,
edge threshold (>0.25), extraction, event semantics and downstream policy stayed fixed.
Unlike October 20's total-score assignment optimizer, this tests selective abstention.
It does not incorporate November 9's rejected segmentation change.

Before implementation or measurement, recorded these gates:

- At least 90% fewer asserted matches on symmetric ambiguous scenes, with nonzero
  baseline assertions. These scenes have no identifiable ground-truth pairing;
  the metric measures unsupported assertions, not demonstrated identity errors.
- Stationary, coherent translation and distinct-colour controls: both arms at least
  95% correct identity recovery, candidate loss at most five percentage points.
  Unmatched surviving objects count as errors. Moving controls also require at least
  95% candidate motion recovery.
- Conditional on synthetic success: five cached public games, ablation F, seeds
  0/1/2, 100 actions; at least one extra total level, no per-game summed regression,
  warm runtime at most twice baseline. A–E expansion conditional on passing F.
- Passing unit tests, formatting/lint, notebook source/compile checks and raw audit.

## Synthetic benchmark

200 paired seeds per family, RNG `20261110 + seed`, 48x48 grids. Each scene contains
two single-pixel sprites with a sampled origin (x/y 8–16), colour (1–9), and quarter
turn about the frame centre. Source offsets are (-2,0), (2,0). Ambiguous destinations
are (0,-2), (0,2); stationary destinations are unchanged; coherent destinations are
translated (0,10). Distinct-colour controls use that same motion with different colours.
The generator checks that perception recovers exactly two components in each frame.
These are four designed geometries with nuisance variation, not 800 independent tasks.

| Measurement (400 object slots per arm/family) | Baseline | Candidate |
|---|---:|---:|
| Ambiguous asserted matches | 400 | 0 |
| Stationary correct identities | 400 | 400 |
| Coherent-motion correct identities | 400 | 0 |
| Distinct-colour correct identities | 400 | 400 |
| Coherent-motion recovered motions | 400 | 0 |
| Distinct-colour recovered motions | 400 | 400 |

Primary suppression passes (100%); coherent-motion retention fails (100% to 0%).
For coherent motion, true edges score 2.7 and alternatives approximately 2.6384:
a physically correct common translation has a small pairwise margin. The fixed
threshold cannot distinguish this case from uncertainty. No threshold retuning was
performed. Each rejected family also produces **400 births and 400 deaths** under
existing differencing semantics, despite all objects persisting. Thus simply filtering
matches cannot safely encode epistemic uncertainty for downstream hypotheses.

The synthetic failure stopped conditional public evaluation. Official access was not
tested this run; no unavailability, public completion, runtime improvement, held-out
performance or RHAE claim is made. No competition submission.

## Verification and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected memory, clean original
checkout, freshly fetched main/daily/research refs, main plan/history, prior report
introductions and relevant full reports. Connected GitHub search found no open PRs.
Used an isolated temporary clone, preserving the original checkout and prior evidence.
No game-source inspection, unmerged mechanism or subagent work.

Candidate: **20 tests pass** (15 baseline plus five new tests for ambiguous identity,
unique motion, stationary matching, empty matching and births). Final restored baseline:
**15 tests pass**. Both pass formatting/lint and generation, source equality and
compilation of all **10 notebook modules**. An independent singleton-score/pixel/identity
and event-count audit checks all **1,600 arm-specific records**. Deterministic rerun
reproduces raw JSON byte-for-byte; this is repeated evidence, not additional samples.
Production agent/tests/scripts match main.

Ignored evidence: `experiments/results/2026-11-10-correspondence-abstention/`, containing
protocol, frozen baseline/candidate, patch, five tests, runner, raw grids and matches,
summary, audit, dependency list, validation logs, inspected prior reports and manifest.
To reproduce from the base, apply `candidate.patch`, copy `candidate_tests.py` to
`tests/test_abstention.py`, and run the archived `benchmark.py` and `verify.py` from the
repository root with that evidence directory restored. Run pytest and the archived
`package_check.py` after `scripts/build_notebook.py`.

Recommend merging only this report and the plan entry. A future uncertainty mechanism
needs an explicit unknown-correspondence state rather than birth/death substitution,
and evidence for motion coherence before trying another universal pairwise threshold.
