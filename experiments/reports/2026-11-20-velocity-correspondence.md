# Velocity-guided correspondence — 2026-11-20

Decision: **reject the candidate; merge the negative research record**. A previous
observed displacement resolves crossings, but the same prior asserts crossings when
identical sprites bounce. The control gate fails. Candidate code and five tests were
archived under ignored results and removed before commit.

## Hypothesis and fixed criteria

Hypothesis: constant-velocity continuation supplies enough temporal evidence to
resolve repeated-object crossings without unacceptable identity errors in controls.
Unlike November 11/14's two-frame correspondence priors, this uses an additional
observed transition. For each current object, use the previous motion ending at its
object ID to predict its next centroid. Preassign an edge only when colour, shape
and predicted centroid agree, and both endpoints have exactly one continuation edge.
Use unchanged greedy matching for the remaining objects. The adapter supplies its
existing previous diff, suppresses history on progress, and retains reset clearing.
No oracle velocities, game source, parameter fitting or policy-score changes.

Protocol was written before implementation and measurement. Require >=95% crossing
identity accuracy and >=20% relative baseline error reduction. Each bounce, stationary
and translation control may lose at most five percentage points. Both arms must
recover >=95% of first-transition identities. Conditional on passing, run five public
games with F, seeds 0/1/2 and 100 actions, requiring an additional completed level,
no per-game regression and <=2x runtime. All gates are necessary; none were relaxed.

## Synthetic evidence

200 paired seeds per family, RNG `20261120 + seed`, three 48x48 frames. Two identical
singleton sprites start at offsets 0 and 8g, then 3g and 5g; g is uniform 1–2.
Crossing ends at 6g and 2g by identity; bounce ends at 2g and 6g. Origins are sampled
8–16 on each axis, colour 1–9, quarter turn 0–3. Stationary repeats the initial
positions; translation shifts both by g on each step. Identity ground truth comes
from the generator. Previous velocities come from the first actual parsed diff.

| Correct final identities / 400 per arm | Baseline | Candidate |
|---|---:|---:|
| Crossing | 0 | 400 |
| Bounce | 400 | 0 |
| Stationary | 400 | 400 |
| Translation | 400 | 400 |

Both arms recover all 400 first-transition identities in every family. Thus failure
is not due to a bad initial velocity estimate. Primary gates pass, but bounce accuracy
falls 100 percentage points, exceeding the five-point limit. Across 800 paired
fixtures there are 1,600 arm records. These are four designed geometries with nuisance
variation, not 800 independent ARC tasks or an estimate of collision frequency.

Crossing and bounce render the same **three** frames, despite opposite final identity
assignments. Both arms necessarily return identical outputs across these families.
Additional temporal context alone therefore does not establish continuation through
a possible collision. This extends earlier two-frame ambiguity evidence: use competing
crossing/bounce explanations or collision/intervention evidence before committing a
single identity. It does not reject velocity as a proposal or establish that the
baseline is generally better at tracking.

Public evaluation was skipped because the preregistered synthetic gate failed.
Official access was not tested; no access-unavailability, public completion, held-out,
RHAE or runtime improvement claim is made. No competition submission.

## Verification and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation memory,
fresh origin main/daily/research refs, git history, main research plan, recent research
records and relevant correspondence/segmentation reports. Connected GitHub search
returned no open PRs. Worked in an isolated clone; original tracked checkout preserved.

Candidate: **20 tests pass** (five new); restored baseline: **15 tests pass**. Both
pass formatting/lint and notebook generation, source equality and compilation of all
**10 embedded modules**. Ruff 0.17.5 executable was used after discovering the reused
Python environment does not expose it as an importable module. Independent audit
checks all 1,600 rows, coordinate bounds, bijections, oracle identity scoring, inferred
warm velocities, paired inputs, summaries and 400 equivalent-observation arm pairs.
Raw evidence replays byte-for-byte. Patch forward/reverse checks pass; final production
agent/tests/scripts match main exactly.

Ignored evidence: `experiments/results/2026-11-20-velocity-correspondence/` contains
protocol, baseline/candidate source, five candidate tests, patch, runner, raw identity
traces, summary, independent audit, validation, refs/history and dependency versions.
Evidence is mirrored with SHA-256 verification to the original repository's ignored
results path. It is local, not pushed. To reproduce from main, apply `candidate.patch`,
copy `candidate-tests.py` to `tests/test_velocity.py`, restore this evidence directory,
then run `PYTHONPATH=. python` on its `benchmark.py` and `audit.py`. Build the notebook
before running `check_notebook.py`.

Only this report and the research-plan entry are committed. Recommend merging the
research record and rejecting unconditional velocity preassignment.
