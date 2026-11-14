# Unique-shape correspondence — 2026-11-14

Decision: **reject the mechanism; merge the negative research record**. Prioritizing
unique colour/shape correspondences fixes crossing identities but substitutes motion
for in-place shape transformations. Candidate source and seven tests were archived and
removed before commit. Production matches main.

## Hypothesis and fixed criteria

Hypothesis: an admissible colour/shape match unique in both frames provides reliable
identity evidence, recovering crossing objects without damaging shape-changing objects.
This tests a different objective from October 20's global assignment and November 11's
common-translation matching; neither unmerged mechanism was incorporated.

Before implementation or measurement: primary correspondence accuracy >=95% and >=25%
relative error reduction; every control must have >=95% accuracy in both arms and
candidate loss <=5 percentage points. Require correct extraction, unit tests, format,
lint, notebook source equality/compile, independent audit and deterministic replay.
Only if synthetic gates pass, run five cached public games with ablation F, seeds
0/1/2, 100 actions, requiring an extra completed level, no per-game regression and
<=2x runtime; run A-E only after F passes. No parameter or gate was tuned.

## Mechanism and fixtures

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation history, fetched
origin main/daily/research branches, main research plan/history, prior report introductions,
the full global-correspondence report and recent experiment records. Connected GitHub
open-PR search returned none. An isolated temporary clone preserved the original
checkout and its untracked cache. No game implementation was read for design.

Keep the existing admissible edges and scores. Sort edges first by whether their
colour and translation-normalized exact shape match uniquely in both frames, then
by the original descending score/index tuple. Greedy one-to-one assignment, segmentation,
event semantics and policy remain unchanged. No additional matching threshold.

Four families each use 200 paired seeds (20261114 + seed), 40x40 grids, two same-colour
L triominoes of distinct orientations, random colour 1–9, x/y origin 4–12, site separation
5–9 and horizontal/vertical arrangement. Crossing swaps the physical objects' sites;
morph exchanges shapes in place while preserving physical identities. The other two
controls retain the objects or translate both by (+1,+1). Identity labels come from the
generator; exact extracted cell sets are checked in every arm. These are designed
frame pairs, not online solves or independent ARC tasks.

## Results

Correct object correspondences out of 400 per family and arm:

| Family | Baseline | Candidate |
|---|---:|---:|
| Crossing (primary) | 0 | 400 |
| In-place shape exchange (control) | 400 | 0 |
| Stationary (control) | 400 | 400 |
| Common translation (control) | 400 | 400 |

Primary errors decrease 100%, but the competent shape-changing control loses 100
percentage points, decisively failing retention. Crossing and shape exchange render
identical before/after grids for each seed, with incompatible physical identities.
Candidate motion labels replace the control's transformations. Uniqueness of a visible
signature is therefore insufficient evidence of persistence of that signature.
This is a bounded counterexample to unconditional priority, not an estimate of ARC
prevalence. Future identity hypotheses need temporal/intervention evidence or explicit
competing motion/transformation interpretations; do not repeat unique-shape priority
alone or retune this fixture's score.

Conditional public evaluation was skipped after the synthetic failure. Official access
was not tested in this run; no claim of unavailability, public completion improvement,
held-out performance, official RHAE or speed improvement. No competition submission.

## Verification and disposition

Candidate: 22 tests passed (15 original + seven new), covering crossing, stationary,
translation, transformation ambiguity, empty scenes, inadmissible long-distance edges
and duplicate-shape fallback. Final baseline: 15 tests passed. Both versions pass
format/lint and generation plus source equality/compilation of all 10 notebook modules.
The reused environment lacked its formatter module, so ruff 0.17.5 was installed in an
isolated temporary directory and the checks completed successfully.

Independent raw-record audit checks 1,600 rows for pixel partitions, one-to-one
assignments, correspondence totals, motion/transform events, and 400 arm-specific
crossing/morph pixel-equivalence pairs. A second execution produced byte-identical
raw evidence. Candidate patch forward/reverse checks pass. Only this report and the
research-plan note are committed; source, seven tests and runner are archived locally.

Ignored evidence: `experiments/results/2026-11-14-unique-shape/`, including protocol,
frozen baseline/candidate, candidate tests/patch, benchmark, raw records, summary,
independent audit, replay hash, dependency list and both validation logs. Patch SHA256:
`f4d1a7cdb49a60a4c19543fa400b33fa27a44f8ee0bfc4a6ae4dd2bd7f1ac60d`.

Reproduce in the base checkout: restore the archived evidence directory, apply
`candidate.patch`, copy `candidate_tests.py` to `tests/test_unique_shape.py`, and run
`python experiments/results/2026-11-14-unique-shape/benchmark.py` followed by
`verify.py`. Use the recorded dependencies; run `validate.py candidate` with ruff
available. Raw evidence is ignored and not included in the pushed commit.
