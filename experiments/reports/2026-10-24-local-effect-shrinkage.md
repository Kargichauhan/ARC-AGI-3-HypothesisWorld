# Local effect shrinkage — 2026-10-24

Decision: **reject the implementation; merge the research record**. Shrinking sparse
local effects toward other states improves synthetic and public aggregate prediction
loss, but the public gain is confined to visible-change prediction. Completion stays
at two levels. Candidate source, tests and runner were archived and removed.

## Hypothesis and fixed gates

Hypothesis: two virtual observations drawn from other sources of the same action
reduce noisy local progress/risk/change estimates and improve full-agent completion.
This changes effects at already-observed local state/action pairs, unlike October 22's
unseen-state fallback weighting or September 24's target-confidence penalty.

All retention gates were recorded before implementation and measurement:

- Sparse IID prediction, 200 paired seeds: at least 20% lower mean three-channel
  held-out Brier loss after one local observation and 64 other-source observations.
- Homogeneous deterministic control, 200 seeds: both arms predict the exact oracle.
- Supported heterogeneous control, 200 seeds: after 32 local observations opposing
  the other-source rule, baseline predicts exactly and candidate loss is at most .01.
- Five cached public games, full agent F, seeds 0/1/2, 100 actions: at least one extra
  total level without per-game summed regression; warm subprocess time at most 2x.
- Passing tests, formatting/lint, notebook source/compilation checks, independent
  formula/frame audit and deterministic replay. A–E sweep conditional on all gates.

Sparse heterogeneity was a separately reported diagnostic. No policy, fixture or
threshold was retuned after results. No game implementation informed the design.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation memory,
clean original checkout, fresh remote main/daily/research branches, plans, recent
reports and history; connected GitHub search found no open PRs. Used an isolated
clone for faster I/O, preserving the original checkout and excluding unmerged work.

Only production file `agent/world_model.py` changed. For a local sample count n,
local effect sum s, and other-source empirical mean m, predict `(s + 2*m)/(n + 2)`.
Exclude every observation of the queried source from m; if no other evidence exists,
retain `s/n`. Three additional action counters make the effect calculation constant
time. Same exact ActionKey is required. The prior is weighted by observation counts,
not equally by source. Its two-observation strength is fixed, not learned.

Fallback predictions, next-state targets, confidence, graph edges, hypotheses,
proposals, selector weights and RNG are unchanged. Local change uses `diff.changed`,
as before; the pre-existing fallback uses changed pixels. This experiment does not
repair that contract discrepancy. Progress is a nonnegative mean, not generally a
Bernoulli probability; this pilot's measured outcomes are binary.

## Synthetic evidence

800 records: 200 seeds per family, RNG `20261024 + seed`. Nine distinct 24x24 frames
contain a 2x2 sprite; source zero is queried and eight other sources contribute eight
observations each. IID categories are no-op/progress/fatal with probabilities .6/.2/.2;
100 independent held-out labels follow training. Controls use deterministic categories.
Both arms receive identical training and held-out labels.

| Family | Baseline Brier | Candidate Brier |
|---|---:|---:|
| Sparse IID | 0.385867 | 0.208082 |
| Homogeneous deterministic | 0 | 0 |
| Heterogeneous, 32 local observations | 0 | 0.002307 |
| Heterogeneous, one local observation (diagnostic) | 0 | 0.296296 |

Primary loss falls **46.07%**; the paired-seed 10,000-resample bootstrap 95% interval
for candidate-minus-baseline loss is [-0.194590, -0.161671]. Both control gates pass.
Sparse deterministic heterogeneity strongly favors baseline: transfer can overwrite
correct local evidence when states differ. The supported control establishes eventual
local dominance, not safety of early transfer. These are supplied-distribution tests,
not full-agent discovery or independent ARC tasks.

## Public evidence

Official cached OFFLINE engine, `arc-agi==0.9.9`, `arcengine==0.9.3`; harness revision
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. All ten cached game/metadata and 30 harness
Python hashes match October 23. Dependency and source manifests are archived.
Primary cohort: **30 runs / 3,000 actions**, alternating arm order by seed.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 2** fails retention. Fourteen of 15 paired action sequences are
identical; only cn04 seed 2 changes. No-ops remain 595 per arm; consecutive exact
repeated choices fall 746 → 745. No progress prediction changes among 31,491 queries
per arm. On baseline trajectories, 549 predictions change: 333 risk and 222 change
estimates, with overlap. Targets and confidence remain identical on shared histories.

Pre-update shadow evaluation of 755 executed local predictions on baseline trajectories:

| Channel | Baseline squared error | Candidate squared error |
|---|---:|---:|
| Progress | 0 | 0 |
| Failure | 0 | 0.000687 |
| Visible change | 0.123179 | 0.079621 |
| Mean across channels | 0.041060 | 0.026769 |

Aggregate local loss improves **34.80%**, entirely through change prediction, which
the selector does not use. Risk prediction worsens slightly. On the candidate's own
753 local observations, mean shadow loss is 0.040283 → 0.026150. These are on-policy
observed outcomes, not counterfactual or held-out calibration claims.

Warm replay totals **19.864 / 19.574 seconds** (0.985x). Timing includes equal shadow
tracing, serialization and startup; the independent audit overlapped part of replay.
Initial totals 30.836 / 19.555 seconds were startup-confounded (baseline seed 0 took
17.955 seconds). No isolated speed claim, hidden-game evaluation, official RHAE result
or competition submission. A–E expansion was unnecessary after rejection.

## Verification and disposition

Candidate: **25 tests passed**, including ten new cases; formatting/lint and **ten
notebook embedded-source equality/compilation checks** pass. Before measurement, one
new test expectation was corrected: a fatal outcome without pixels or progress does
not satisfy the existing `diff.changed` contract. No production change followed results.

Independent row-based estimation verifies every recorded prediction, local exclusion,
fallback/target/confidence invariance, 800 synthetic records, and all 2,976 public
decisions plus 2,976 observations. Raw-grid diffs, legal proposals, selected top scores
and source hashes were checked. All 15 baseline trajectories, scores, observations and
transitions exactly match October 23. All 800 synthetic records and 30 public runs
replay exactly; the additional 3,000 actions are repeated evidence.

Archived implementation, tests, runner and patch under ignored
`experiments/results/2026-10-24-local-effect-shrinkage/`, hash-mirrored to the original
workspace. Raw evidence is local and not pushed. Patch SHA-256:
`b8b035c73403a2b7954010ff7f30643a94c5693440b7b7c7605061c96775a42b`.
Forward/reverse patch checks pass. After removal, production matches main; **15 tests**,
format/lint and ten notebook checks pass. Only this report and the plan note remain.

Reproduce by applying the archived patch to the base and restoring its frozen baseline
and protocol at the evidence path. With recorded dependencies/cached engine, run
`python experiments/run_local_shrinkage.py --output <ignored-path>` with writable
MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. Audit and packaging/replay verifiers
are archived alongside the runner.

Recommend merging the negative record and rejecting fixed cross-source shrinkage.
Future transfer needs evidence of local/source compatibility and improvement in a
quantity the decision policy uses. Lower aggregate error alone is insufficient.
