# Learned continuation utility — 2026-09-23

Decision: **reject the candidate; retain the research record**. Backing up learned
future progress and failure corrected designed two-step decisions, but did not
improve public completion. The candidate implementation, tests and runner were
archived locally and removed before committing.

## Hypothesis and gates

The existing planner rewards immediate progress but evaluates future edges only
for novelty. Hypothesis: adding their observed progress and failure utility enables
known goal routes and avoids downstream hazards, improving public completion.

Before implementation, the ignored protocol required all of:

1. At least 95/100 correct decisions on each of two designed graph fixtures (known
   goal versus novel dead end; safe route versus novel known failure), with at least
   a 50-percentage-point combined gain over baseline.
2. An aligned-novelty delayed-goal control with baseline at least 95/100, losing no
   more than five percentage points; exact planner parity on 100 neutral graphs.
3. At least one additional completed public level with no per-game summed loss:
   five cached games, full agent F, seeds 0/1/2, 100 actions per game. Audited total
   subprocess time at most twice baseline.
4. Passing unit tests, format/lint, notebook generation and embedded-source checks.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Started from a clean checkout,
fetched origin, inspected main, remote research/daily branches, history, plans and
September 15/17/18/19/20/21/22 reports. No open PRs. No unmerged mechanisms were
incorporated, no game source was read to design the experiment, and no thresholds
or parameters were tuned after results. A–E were conditional on F passing.

## Minimal implementation and measurement

For each future edge, add `2 * mean_positive_progress - 2.2 * failure_frequency`
inside its existing confidence multiplier. Retain discount 0.55 and horizon 2.
The adapter passes the configured risk coefficient; the model exposes local
outcome means without cross-state fallback. Root scoring, representations,
proposals, hypotheses, confidence gating, novelty and random tie assignment stay
unchanged. This preserves the baseline's max-over-edges optimism, pooled actions,
repeat novelty and terminal bootstrapping; it is not a full Bellman rewrite.

Synthetic trials train both arms from the same four graph edges, then use the
full selector to choose between two root actions with equal immediate outcomes.
Root/intermediate state visits are 100; goal/safe outcome visits are 100 and the
novel distractor's are 1. The aligned control reverses outcome visit counts.
Each fixture uses 100 randomized action/observation label permutations, RNG
`20260923 + seed`, policy seeds 0–99. These are mechanistic decision diagnostics,
not 100 independent task structures or online solve-rate estimates. The delayed
control is fully observed and does not establish hidden-state competence.

Neutral controls randomize 60 transitions over six states and four actions,
including stochastic outcomes and cycles, with horizons 1–4. All have zero
progress/failure. Of 2,400 action values, 638 are nonzero; all 100 graphs exercise
at least one nonzero value, so equality is not a vacuous all-zero comparison.

Public runs use the installed official OFFLINE engine and framework lifecycle,
arc-agi 0.9.9 / arcengine 0.9.3. Arm order alternates by seed. Both arms audit
baseline and candidate planners on the same observed histories without extra RNG
draws, recording reachable utility edges and shadow choice changes.

## Results

| Diagnostic, 100 permutations each | Baseline correct | Candidate correct |
|---|---:|---:|
| Goal versus novel dead end | 0 | 100 |
| Safe route versus known failure | 0 | 100 |
| Aligned-novelty delayed-goal control | 100 | 100 |

All 100 neutral graphs match exactly. Synthetic gates pass.

Primary public cohort: **30 game runs, 3,000 actions**. Entries list seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion remains **2 → 2**, failing the retention gate. Repeated exact actions
fall **687 → 686**; same-frame/no-positive-progress transitions remain **595 → 595**.
No selected-state lookahead in either arm reaches an observed positive-progress
edge. Exactly one decision per arm reaches a known failure: the last selection
in `vc33`, seed 1. The candidate reduces that route's planning value by 1.21,
changes the chosen coordinate, and still ends with zero completed levels. The
other 14 candidate trajectories match baseline exactly.

All 15 baseline trajectories exactly reproduce September 22, including scores,
actions and transitions. Initial audited times were 349.428 s baseline and
39.786 s candidate; the first baseline subprocess spent 322.710 s including
cloud-placeholder dependency loading and plotting-cache initialization. These
numbers cannot support an efficiency comparison.

A separately labeled repeat used a temporary local environment with the same
recorded engine/NumPy versions and writable caches. All 30 game traces, synthetic
decisions and neutral results reproduced exactly. Audited times were **9.569 s →
9.861 s (1.031×)**, passing the runtime gate. This adds 3,000 replayed actions;
the repeated deterministic trajectories are not additional independent evidence.
A runner import-format issue and relative-output-path error were fixed before
this repeat; the latter occurred before evaluation. Production code was unchanged.

Candidate validation: **24 tests passed**, including nine new cases for discounted
progress/failure, local means/no fallback, root confidence, horizon boundaries,
continuation choice, configurable risk, cycles and stochastic confidence. Format,
lint and all **10** notebook module source/compilation checks passed. After candidate
removal, **15 baseline tests** and the same format/lint/packaging checks passed.
The archived patch applies cleanly to the restored base.

## Interpretation and reproduction

Reject the mechanism in this configuration. The graph fixtures show that future
utility can guide known routes, but the public agent almost never reaches states
where that information is available. This pilot supports auditing reward-bearing
transition reuse and lookahead reachability before adding more planner utility
terms. It does not establish that delayed reward propagation is generally ineffective.
Do not combine it with an unmerged state abstraction without a separate factorial
protocol and false-aliasing controls.

These are short cached public-game pilots, not held-out evaluation or official
Relative Human Action Efficiency measurements. No competition submission or PR
merge was made. The small game set, short horizon/budget, label-permutation
fixtures and retained model limitations constrain interpretation.

Ignored local evidence: `experiments/results/2026-09-23-continuation-utility/` holds
the protocol, synthetic decisions, neutral audit, public logs/traces, source/game
hashes, dependency manifests, startup diagnostics, recovery cohort, reproduction
audits, validation logs and removed `candidate.patch`. Raw evidence is not pushed.

Patch SHA-256:
`0059e7affdb512475e4e2375e74aa19cc0c171fe2cf248c17e0f26e8eac0c1b6`.

To reproduce locally, apply the archived patch to the base revision, copy the
protocol into a fresh ignored output directory, and run Python with the recorded
dependencies: `experiments/run_continuation_utility.py --output
experiments/results/continuation-utility-reproduction`. Provide the cached game
versions and writable plotting/cache directories. The cross-day audit separately
requires September 22 baseline traces. Only this report and the plan are retained.
