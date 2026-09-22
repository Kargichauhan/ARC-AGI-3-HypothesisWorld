# Temporary probe deferral — 2026-09-22

Decision: **reject both candidates; retain the research record**. Exact-click
coverage and visible responses improved, but neither candidate improved public
completion. Experimental code, nine test cases, and runner were archived locally
and removed. Production code matches main's base revision.

## Hypothesis and preregistration

September 21 exposed a proposal/selection gap: spatial sampling supplied an
initial `ft09` probe with a visible effect, but the agent never selected it.
Hypothesis: temporarily deferring exact clicks after two observed no-ops, while
untested proposals remain, prevents pooled confidence from starving discovery and
improves completion. This changes selection rather than learned action identity,
world-model estimates, planner rewards, or hypothesis weights.

The protocol was saved before implementation and measurement. All gates required:

1. On 100 paired synthetic immediate-effect trials, solve at least 95 and reduce
   mean capped discovery actions by at least 20%.
2. On a delayed-effect control, lose no more than five percentage points of solves.
3. On five cached public games, F, seeds 0/1/2, 100 actions per game, complete at
   least one additional level with no per-game summed regression.
4. Audited subprocess time at most twice baseline; passing tests, format/lint,
   notebook generation, embedded-source equality, and compilation.

A four-arm factorial compared baseline, deferral, September 21's fixed spatial
proposal rule, and their combination. Deferral and combined were independently
eligible against baseline; spatial was a control. Parameters and gates were not
retuned. A–E were conditional on passing F and were not run after rejection.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. The initial checkout was clean.
Fetched origin, inspected main, remote research/daily branches, open PRs (none),
research plans, history, and September 15/17/18/19/20/21 reports. Created this branch
from main; incorporated no unmerged learning or representation mechanisms.

## Smallest implementation and method

The selector stores a bounded 512-record history of exact coordinate outcomes,
separate from pooled `ActionKey` learning. For the current raw fingerprint, a
probe is deferred after two consecutive observed no-ops for that exact probe.
A changed frame, positive progress, or terminal outcome clears its streak.
Deferral applies only while an untested coordinate candidate remains; once all
are tested, the original ranking resumes. RESET clears this history. Keyboard
candidates and random ablation behavior are unchanged.

All candidates retain original scores and RNG draws before a stable partition
moves deferred probes behind the others. Thus deferral alone does not reassign
tie-breaking draws. Spatial arms retain September 21's changed proposal ordering;
comparing deferral within each geometry isolates that ordering from selection.
The adapter records the pending exact coordinates alongside each observed outcome.

Synthetic proposals are 24 fixed blank-frame points, eight in each of three coarse
regions on a 64×64 grid. Policy seeds are 0–99; each rewarding point is uniformly
sampled using seed `20260922 + seed`. The full selector learns after each action.
Reward produces both visible change and progress. Immediate trials allow 48 actions.
The delayed control requires three consecutive clicks at the target, resets that
count after any other click, and allows 72 actions. Fixed proposals isolate
selection, so the geometry arms share these synthetic results. These fixtures
are designed diagnostics, not a representative ARC distribution.

The public runs use the installed official engine in OFFLINE mode and the existing
framework lifecycle: arc-agi 0.9.9, arcengine 0.9.3. Arm order rotates by seed;
seed injection and auditing are identical. No game implementation was read to
design the mechanism. All 30 baseline/spatial control trajectories exactly
reproduced September 21, including scores, selections, transitions, and levels.

## Results

| Synthetic metric, 100 trials each | Baseline | Deferral |
|---|---:|---:|
| Immediate solves | 28 | 100 |
| Immediate mean capped actions | 36.64 | 23.95 |
| Delayed solves | 4 | 0 |
| Delayed mean capped actions | 71.31 | 72.00 |

Immediate mean actions improved **34.63%**. The delayed four-point loss passes the
preset tolerance, but both solve rates are near zero. This control provides weak
assurance and exposes harm on useful repeated actions; it does not establish
hidden-state robustness.

Public evaluation: **60 runs, 6,000 actions**. Level entries list seeds 0/1/2.

| Game/version | Baseline levels | Deferral levels | Spatial levels | Combined levels |
|---|---|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 | 0/0/0 | 0/0/0 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| Aggregate | Baseline | Deferral | Spatial | Combined |
|---|---:|---:|---:|---:|
| Completed levels | 2 | 2 | 0 | 0 |
| Repeated exact actions | 687 | 529 | 573 | 376 |
| Observed no-ops | 595 | 508 | 495 | 462 |
| Audited subprocess seconds | 41.615 | 41.182 | 41.835 | 41.881 |

Repeats use raw fingerprint, action key, and exact coordinates within a run.
Diagnostic no-ops mean equal fingerprints without positive progress; they do not
exclude hidden-state changes. Timings include startup and instrumentation, including
shadow deferral eligibility in controls, and are not stable production latency claims.
Both candidate runtime gates pass. Deferral fails the extra-level gate; combined
also fails per-game non-regression on `vc33`.

On `ft09`, deferral expands selected distinct coordinates from **3/3/3 to 24/24/24**,
but all 300 outcomes remain no-ops. Spatial alone selects **3/2/3** coordinates with
zero visible responses. Combined selects **30/33/32** coordinates and causes
**9/9/9** visible responses; first responses occur at actions **25/31/19**. Neither
factor alone exposes these effects in this pilot. Their interaction resolves the
observed availability/selection gap but produces no level progress. Deferral also
reduces `su15` no-ops from 100 to 13 without completing a level.

Candidate validation: **24 tests passed**; format/lint and all **10** notebook
module equality/compilation checks passed. Nine added cases cover exact identity,
two-no-op threshold, exhaustion, progress/terminal recovery, state isolation,
reset, bounded history, keyboard/random behavior, score/RNG preservation, and
adapter coordinate alignment. After removal, **15 baseline tests** and the same
format/lint and 10-module packaging checks passed.

## Decision, limitations, and reproduction

Reject both candidates. Reduced repetition, broader exploration, and visible
changes are insufficient retention objectives without completion. Future work
should diagnose why newly reached transitions fail to support goal-directed
sequences, and use a delayed-effect control with a competent baseline before
revisiting action suppression. Do not repeat this deferral/spatial combination
based solely on improved probe coverage.

These are short cached public-game pilots, not held-out results or official
Relative Human Action Efficiency measurements. No competition submission was made.
Three seeds and five games limit generalization; no broad inferiority claim follows.

Ignored local evidence: `experiments/results/2026-09-22-probe-deferral/` contains the
protocol, 400 synthetic trajectories, twelve public logs and trace files, summaries,
source/game/dependency hashes, control-reproduction audit, candidate/final validation,
packaging verifier, and removed `candidate.patch`. Raw evidence is not pushed.
The patch includes the self-contained runner and frozen spatial control source.

Patch SHA-256:
`77d866482f204e3ea36f687b1e4cb5a5823ccf0771cab65929b2187ab894119a`.

To reproduce locally, apply that patch to the base revision, copy the protocol to
a fresh ignored output directory, and run `.venv/bin/python
experiments/run_probe_deferral.py --output experiments/results/probe-deferral-reproduction`
with the recorded dependencies and cached games. The cross-day audit additionally
requires September 21's traces. Only this report and the plan update are retained.
