# Conjunctive falsification — 2026-10-21

Decision: **reject the implementation; merge the research record**. Strict clause
contradictions remove stale synthetic rules, but worsen stochastic predictions,
fail an existing exploration test and reduce public completion from two levels to
zero. Candidate implementation, tests and runner were archived and removed.

## Hypothesis and fixed gates

Hypothesis: falsifying any known contradicted clause prevents matching fields from
masking a false prediction, improving hypothesis quality and full-agent completion.
The baseline's weighted similarity can strengthen a wrong-motion rule when its
other fields match. This changes hypothesis evidence updates, unlike prior
empirical change-point forgetting or information-score changes.

Before implementation and measurement, the ignored protocol required all of:

- 200 paired reversal fixtures: at least 50% lower late contradictory belief mass,
  nonzero baseline error, and at most 5% initial wrong-rule survival after four
  counterexamples.
- Stationary controls: both arms' contradictory mass at most 0.10; candidate loss
  at most 0.01. Stochastic controls: held-out binary motion Brier increase at most
  0.02 over baseline.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one additional
  completed level, no per-game summed loss, warm subprocess time at most 2x.
- Passing unit tests, format/lint, notebook source/compilation checks, trace audit
  and deterministic replay. A–E sweep conditional on passing all other gates.

No policy, threshold or fixture was tuned after results. Continued benchmarking
after a unit-test failure to measure consequences; did not weaken that test or
add a compensating policy.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean original
checkout, fetched remote branches, plans, daily reports, history and open PRs
(none). Used an isolated clone because original cloud-backed reads were slow.
No game implementation informed design; no unmerged mechanism was incorporated.

Only production file `agent/hypotheses.py` changed. Specified prediction fields are
conjunctive clauses; unspecified predictions are wildcards. Unknown observed
motion/affected colour is uninformative. Any comparable mismatch gives evidence
zero; all comparable clauses matching gives one; no comparable clauses skips
evidence mutation. Existing increments, contradiction decay, rejection thresholds,
population cap and reconsideration cooldown remain. Generation uses the revised
evidence score. Models, planning, proposals, selector and RNG are unchanged.

## Synthetic evidence

600 designed trials: 200 seeds per fixture, RNG `20261021 + seed`. Each transition
renders one 2x2 sprite on a 12x12 frame; colour, location, cardinal displacement and
action ID vary. Perception supplies the actual outcome. Reversal starts with the
opposite motion then observes 12 true motions; stationary uses 13 true motions.
Contradictory belief is normalized weight of rules with a known mismatched clause,
measured before updates 10–13.

| Measurement | Baseline | Candidate |
|---|---:|---:|
| Reversal late contradictory mass | 0.348245 | 0 |
| Initial wrong rule active after four counterexamples | 200/200 | 0/200 |
| Stationary late contradictory mass | 0.067462 | 0 |
| Stochastic held-out motion Brier | 0.250101 | 0.295081 |

Primary and stationary gates pass. Stochastic data has 13 independent equiprobable
signed motions and 16 independent held-out outcomes, without test-time updates.
Forecasts renormalize explicit motion-rule weights, defaulting to 0.5 when absent;
these weights are not calibrated posteriors. Brier worsens **0.044980**, exceeding
the 0.02 gate. Paired-seed bootstrap, 10,000 resamples: 95% interval
[0.031397, 0.059812]. This describes this generator, not unseen ARC tasks.
Candidate has no active explicit motion rule after training in 159/200 trials
(baseline zero); retaining a specific rule in other trials can overcommit to a
random mode. Low contradictory mass alone does not establish useful prediction.

## Public evidence

Official cached OFFLINE engine, `arc-agi==0.9.9`, `arcengine==0.9.3`; harness source
matches `4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Ten cached game source/metadata
hashes and 30 harness Python hashes match October 20. Arm order alternates by seed.
Primary cohort: **30 runs, 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 0 / 0 / 0 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 0** fails retention. Eleven of 15 paired action sequences differ.
Same-frame/nonpositive-progress transitions fall 595 → 415, while consecutive exact
choices repeat 746 → 871. Coverage proxies do not imply completion gains.

Audit finds **938 baseline updates** supporting rules despite known contradicted
clauses; candidate has zero. Mismatched clause counts are appearance 397,
disappearance 270, scene change 268, motion 21 and terminal 10; counts overlap
within updates. The issue occurs in public trajectories, but strict rejection is
not a successful remedy. It treats stochastic/context-dependent outcomes as
counterexamples to unconditional deterministic rules.

Warm replay totals **13.968 / 13.214 seconds**, candidate/baseline **0.946x**,
including equal tracing, serialization and startup. Initial totals 24.268 / 13.143
seconds are startup-confounded. No isolated speed claim. No held-out evaluation,
official RHAE result or competition submission.

## Verification and disposition

Candidate: **28 tests passed, one failed** (14 new cases all pass). Existing test
`test_information_gain_can_select_disagreement_over_exhausted_action` fails its
entropy-ordering assertion: familiar-action label entropy 0.997958 exceeds unseen
0.985412, although novelty still makes the selected action pass. Strict evidence
makes compatible broad/specific rules similarly weighted; their label entropy
can remain high. This is a validation failure, not an adjusted acceptance criterion.
Formatting/lint and ten notebook module equality/compilation checks pass.

Audit verifies 600 synthetic records, 54,514 applicable synthetic-rule updates,
2,977 public decisions/observations and 10,386 applicable public-rule updates,
raw pixel differences, action legality, belief changes and source hashes. All 15
baselines exactly reproduce October 20. All 600 synthetic records and 30 public
runs replay exactly; the additional 3,000 actions are repeated evidence.

Archived complete patch, changed source, tests and runner. Forward/reverse patch
checks pass. Restored production matches main; final **15 tests**, formatting/lint
and **ten notebook module checks** pass. Only this report and the plan note remain.
Ignored evidence is mirrored with hashes to the original workspace under
`experiments/results/2026-10-21-conjunctive-falsification/`.
Patch SHA-256: `e6621da79e2ed5768b89d115fab519ada96d8d29c3216a77ce1fd609e964c505`.

Reproduce by applying the archived patch to the base, restoring the protocol and
frozen baseline at that ignored path, and using recorded dependencies/cached engine
to run `python experiments/run_conjunctive_falsification.py --output <ignored-path>`.
Use writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. Raw evidence is local,
not included in the pushed commit.

Recommend merging this negative record and rejecting the mechanism. Distinguish
probabilistic/contextual predictions from deterministic claims, and measure
semantic disagreement between compatible rules before retrying. Do not infer
improvement from zero contradictory belief alone.
