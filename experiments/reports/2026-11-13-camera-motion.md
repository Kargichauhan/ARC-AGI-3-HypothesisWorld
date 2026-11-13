# Common-motion camera suppression — 2026-11-13

Decision: **reject the mechanism; merge the negative research record**. Common motion
suppression removes camera-induced labels but erases every genuine motion in a moving
swarm control. Candidate implementation and seven test cases were archived and removed.

## Hypothesis and fixed gates

Hypothesis: a common nonzero displacement supported by at least three objects and 75%
of all matched objects identifies camera scrolling sufficiently reliably to exclude
it from causal object-motion outcomes. Count unchanged-shape motions from the existing
matcher, remove the dominant displacement when the threshold holds, then construct
contacts. Preserve changed pixels, identities, transformations, progress, terminal,
background, and downstream policy. This tests motion interpretation, unlike November
11's group correspondence, which changed identities. Suppression also removes affected
colours and contacts derived from those motions; this is not a new camera state model.

Before implementation and measurement, required >=95% reduction in camera false motion;
each control >=95% exact motion accuracy with <=5 percentage-point baseline loss.
Conditional public gate: five games, F seeds 0/1/2, 100 actions, >=1 extra level,
no per-game regression and <=2x warm runtime, then A–E. Stop on synthetic failure.
Require tests, format/lint, notebook generation/source equality/compile, raw audit/replay.
No threshold or fixture was retuned after measurement.

## Synthetic benchmark

200 paired seeds in each of four families; RNG `20261113 + seed`. On 48x48 zero grids,
four singleton sprites with distinct sampled colours 1–9 occupy a square with side ten.
Origin coordinates are independently sampled from 8–15. Translation is 1–3 cells in a
sampled cardinal direction. Camera and swarm families translate all four sprites;
single-motion controls translate only the first; stationary controls translate none.
The camera oracle labels world objects stationary, whereas swarm motion is genuine.
These are four designed cases with nuisance variation, not 800 independent tasks or
an estimate of how often scrolling occurs in ARC games.

| Exact motion sets / 200 per arm | Baseline | Candidate |
|---|---:|---:|
| Camera translation | 0 | 200 |
| Genuine moving swarm | 200 | 0 |
| Single moving object | 200 | 200 |
| Stationary | 200 | 200 |

Camera false motion labels fall 800 to zero; genuine swarm motion recovery also falls
800 to zero. Both arms retain correct single-object motions (200) and no-motion controls.
No births or deaths occur. The control gate fails decisively. Camera and swarm pairs
have identical pixels: common displacement alone cannot distinguish these semantics.
This is a feasibility counterexample, not evidence that camera compensation is generally
harmful. A useful successor must retain competing camera/world-motion interpretations
or acquire anchored temporal/intervention evidence rather than erase motion labels.

The conditional public cohort was not run after synthetic rejection. Official access
was not tested; no claim of unavailability, public completion, held-out performance,
RHAE or speed improvement is made. No competition submission.

## Verification and provenance

Base/main `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Reviewed run memory, fresh origin
main/daily/research refs, main history/plan, prior report introductions and recent full
reports. Connected GitHub search found no open PRs. Used an isolated clone; original
clean tracked checkout and unrelated work were left untouched. No unmerged mechanism,
subagents or game-source design inspection.

Candidate: **22 tests pass**, including seven new threshold/invariant cases. Restored
baseline: **15 tests pass**. Both pass formatting/lint and generation, source equality
and compilation of all **10 notebook modules**. A separate pixel-derived audit verifies
all **1,600 arm records**, motion labels, equal paired inputs, camera/swarm observational
identity and event counts. A second run reproduces raw JSON byte-for-byte; it adds no
samples. Patch forward/reverse checks pass; final agent/tests/scripts match main.

Ignored local evidence: `experiments/results/2026-11-13-camera-motion/` contains protocol,
frozen baseline/candidate, patch, candidate tests, runner, raw grids and motion records,
summary, independent audit, replay hash, dependency list and validation logs. Evidence
is mirrored into the original checkout with a SHA-256 manifest and complete-history
bundle. Raw evidence is not pushed. To reproduce from the base, apply `candidate.patch`,
copy `candidate_tests.py` to `tests/test_camera_motion.py`, restore the evidence directory
at its relative path and run `PYTHONPATH=. python` with `benchmark.py`, then `verify.py`.
Build the notebook before running `package_check.py`.

Recommend merging only this report and research-plan entry; reject the suppression rule.
