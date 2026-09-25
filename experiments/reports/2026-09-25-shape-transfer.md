# Object-shape effect transfer — 2026-09-25

Decision: **reject the candidate; merge this research record**. Shape-conditioned
pooling improved designed synthetic predictions, but public completion and every
selected action remained unchanged. The implementation, eight new test cases and
runner were archived locally and removed before committing.

## Hypothesis and gates

Hypothesis: conditioning click effects on object colour and shape transfers useful
knowledge across visual states better than pooling by coarse click region, improving
public completion. Candidate context: ACTION6, colour, exact translation-normalized
shape and border contact. A context is admissible only when exactly one matching
object intersects the action's 3×3 region. Require at least three observations from
at least two source fingerprints; store at most two source witnesses per context.
Exact state/action evidence takes priority. Transferred effects predict no destination
state and create no planner edges. All other agent mechanisms remain unchanged.

All preregistered retention gates were required:

- At least 25% lower held-out squared effect error on shape-dependent synthetic
  data, and at most 0.01 absolute loss increase on a shape-independent control.
- At least one additional public level, with no per-game summed regression:
  five cached games, full variant F, seeds 0/1/2, 100 actions per game.
- Audited runtime at most twice baseline; unit tests, formatting/lint and notebook
  generation/source equality/compilation passing.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Fetched origin; main remained
unchanged and no PRs were open. Reviewed remote research/daily branches, history,
main/current research plans and recent reports. No unmerged mechanism was included,
no game source was read to design the candidate, and no parameters or gates were
retuned after results. A–E evaluation was conditional on F passing.

## Evidence

Each synthetic generator used 100 paired seeds, 40 training examples and 200 fresh
held-out examples per seed. Two four-cell shapes (square and horizontal line) move
among nine regions; colour and which shape is beneficial vary by seed. A nuisance
marker makes each fingerprint distinct. Progress probabilities are 0.9/0.1 by shape,
or 0.5 for both shapes in the control. Progress coincides with visible pixel change;
failure is complementary. Loss averages progress, failure and visible-change squared
errors. These channels are coupled, not three independent measurements. Both arms
see identical training data and no held-out updates. All held-out contexts qualify.

| Generator | Baseline loss | Candidate loss | Reduction |
|---|---:|---:|---:|
| Shape-dependent | 0.330523 | 0.096095 | 70.93% |
| Shape-independent control | 0.326602 | 0.262338 | 19.68% |

Both synthetic gates pass. Cross-region pooling also increases effective sample size,
so the gain does not isolate semantic shape recognition from variance reduction.
The 40,000 held-out observations share 200 fitted pairs of models; these designed
fixtures are not independent ARC tasks or evidence of general causal identification.
Unit controls cover ambiguity, border mismatch, insufficient evidence, exact-local
precedence, prediction purity, source-witness bounds and absence of fabricated edges.

Public primary cohort: **30 runs / 3,000 actions**, installed official OFFLINE engine,
arc-agi 0.9.9 and arcengine 0.9.3. Arm order alternates by seed.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion **2 → 2** fails the gate. Repeated exact actions remain **687 → 687**;
same-frame/no-positive-progress transitions remain **595 → 595**. All 15 candidate
trajectories exactly match baseline, including scores and transitions. All 15 baseline
trajectories reproduce September 24's warm cohort.

Pre-update shadow forecasts on the same baseline-policy fallback transitions:

| Game | Fallback forecasts | Unambiguous context | Supported transfer |
|---|---:|---:|---:|
| ls20 | 242 | 0 | 0 |
| vc33 | 183 | 106 | 91 |
| ft09 | 3 | 0 | 0 |
| cn04 | 157 | 34 | 14 |
| su15 | 148 | 1 | 0 |
| **Total** | **733** | **141** | **105** |

Pooled fallback effect loss is identical: **0.03018254 → 0.03018254**. On selected
fallback actions, only confidence changes (91 forecasts); progress, failure and
visible-change estimates never change. Across all candidate proposals there are
725 supported-transfer instances and 502 differing prediction instances, including
repeated coordinates sharing a key. These are not independent contexts. The agent
never selects differently. Supported fallback has no destination, so its confidence
cannot activate the planner; root selection uses progress and failure estimates.

Initial total times, 33.779 s baseline / 13.359 s candidate, are startup-confounded:
the first baseline subprocess alone took 26.210 s. A warm replay yields **11.560 s →
13.133 s (1.136×)**, including equal shadow auditing and subprocess startup. All
30 game trajectories and all 40,000 synthetic records reproduce exactly. This adds
3,000 replay actions, not independent completion evidence. An initial diagnostic
counter compared prediction dataclasses from different modules and incorrectly
reported every pair unequal. The warm runner compares field dictionaries instead;
all other trace fields match exactly. The original runner/hash and invalid counter
are preserved and labeled; neither policy nor gates used that counter.

Candidate validation: **23 tests passed**, formatting/lint and **10** notebook
module equality/compilation checks passed. After removal: **15 baseline tests**
and the same formatting/lint/packaging checks passed. Agent, tests, scripts and
notebook configuration match main.

## Decision and reproduction

Reject this shape-transfer fallback. Better predictions on a designed distribution
are insufficient when public transfer changes no useful decision signal. Before
another fallback context, measure how often reward/failure evidence exists and can
reach an unobserved action on separate trajectories. Translation-invariant shape
alone also cannot establish equal semantics across different scene relationships.
This short cached public-game pilot makes no held-out or official Relative Human
Action Efficiency claim. No competition submission or PR merge was made.

Ignored local evidence: `experiments/results/2026-09-25-shape-transfer/` contains
preregistration, training/held-out records, public logs/traces, source/game/dependency
manifests, calibration and reproduction audits, warm replay, validation and removed
`candidate.patch`. Raw evidence is not pushed. Patch SHA-256:
`8f718f7ace36e8ff35ff5f08cbdd7b4a53f5881dee6e488f6e10ddd36486001f`.

Apply the patch to the base revision and run `experiments/run_shape_transfer.py
--output experiments/results/shape-reproduction` with recorded dependencies and
cached game versions. Set writable `MPLCONFIGDIR`/`XDG_CACHE_HOME` and
`MPLBACKEND=agg`; copy the protocol to the output directory to record its hash.
Patch forward/reverse applicability was checked. Only this report and plan remain.
