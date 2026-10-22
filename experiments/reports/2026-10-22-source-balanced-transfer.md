# Source-balanced fallback transfer — 2026-10-22

Decision: **reject the implementation; merge the research record**. Equal weighting
of source states improves a designed visitation-shift test, but worsens public
fallback prediction error and changes no selected action or completed level.
Candidate code, tests and runner were archived and removed; production matches main.

## Hypothesis and fixed criteria

Hypothesis: repeated visits overrepresent particular source states in cross-state
action-effect predictions. Giving each observed source one distributional vote
improves predictions in unseen contexts and full-agent completion.

Preregistered before implementation and measurement; all retention gates required:

- 200 synthetic visitation-shift trials: at least 25% lower three-channel Brier loss.
- Balanced-source control: both arms exactly match the oracle means. IID stochastic
  control: candidate loss increase at most 0.02, across 200 paired trials each.
- Five cached public games, full agent F, seeds 0/1/2, 100 actions each: at least one
  additional completed level, no per-game summed loss, warm runtime at most 2x.
- Passing unit tests, formatting/lint, notebook source/compilation checks, independent
  formula audit and deterministic replay. A–E public sweep conditional on other gates.

No policy, fixture or threshold was tuned after results. A matched-occupancy diagnostic
was preregistered separately to expose the candidate's target-distribution assumption.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected the clean original
checkout, fresh remote main/daily/research branches, plans, report introductions,
recent full reports, history and automation memory. No open PRs. Used an isolated
temporary clone for faster I/O. No game implementation informed design; no prior
rejected mechanism was incorporated.

Only production file `agent/world_model.py` changed. For unseen fingerprint/ActionKey
pairs, normalize each observed source's outcome-signature counts, then average the
source distributions equally. Derive progress, failure risk, visible-change probability
and half-modal-outcome confidence using the existing formulas. Local predictions,
planner edges, identities, hypotheses, proposals, scoring coefficients and RNG remain
unchanged. This changes the fallback distribution's weighting, unlike earlier
shape/contact conditioning and evidence-confidence experiments.

## Synthetic evidence

600 trials: 200 seeds per family, RNG `20261022 + seed`. Each uses ten distinct
24x24 source frames containing a 2x2 sprite, with randomized colour and action label.
Two source contexts produce progress, two failure, six no-op. Positive/fatal outcomes
translate the sprite one cell; actual perception supplies training differences.
One randomly chosen progress/fatal source receives 80 observations, the other sources
four each. Evaluation uses 100 distinct unseen frames, with 20 progress, 20 failure
and 60 no-op labels. Loss averages progress, failure and visible-change squared errors.
These are supplied distribution tests, not full-agent discovery tasks or ARC games.

| Mean Brier loss | Baseline | Candidate |
|---|---:|---:|
| Skewed visits, uniform-source evaluation | 0.335474 | 0.186667 |
| Balanced visits, uniform-source control | 0.186667 | 0.186667 |
| IID outcomes, skewed visits control | 0.188661 | 0.191416 |
| Matched-occupancy diagnostic | 0.142687 | 0.291494 |

Primary loss falls **44.36%**, passing. Balanced training uses eight observations per
source; both predict the exact oracle means (0.2 progress, 0.2 failure, 0.4 change).
IID outcomes have probabilities 0.2/0.2/0.6 independently of source, with 100 independent
held-out labels. Its **0.002756** loss increase passes the 0.02 gate; paired-seed
10,000-resample bootstrap 95% interval [0.002025, 0.003506].

The diagnostic evaluates the primary deterministic model under probabilities
proportional to training occupancy, and favors baseline strongly. Uniform weighting
is an assumption about future contexts, not a generally unbiased correction.

## Public evidence

Official cached OFFLINE engine: `arc-agi==0.9.9`, `arcengine==0.9.3`. Ten cached game
source/metadata hashes and 30 harness Python hashes match October 21; harness
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Fresh transitive dependencies are recorded.
Primary cohort: **30 runs / 3,000 actions**, alternating arm order by seed.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 2** fails retention. All 15 paired action sequences are identical;
both arms have 595 same-frame/nonpositive-progress transitions and 746 consecutive
exact repeated choices. Across 31,491 candidate queries per arm, 1,443 predictions
differ; 734 failure-risk estimates differ, but no progress estimate differs. Thus the
mechanism activates without changing decisions. Change probability is unused by the
selector; fallback confidence cannot enable planning without a destination state.

Same-history shadow evaluation on 661 executed, nonempty fallback predictions gives
Brier **0.024393 → 0.027121** (+11.18%). Across all 1,488 observed transitions per arm,
loss is 0.035701 → 0.036913. Both arms visit identical trajectories, so their shadow
results duplicate the same evidence. These are on-policy observed outcomes, not
counterfactual or held-out calibration estimates.

Warm replay subprocess totals **22.638 / 20.974 seconds** (0.927x), including equal
shadow tracing, serialization and startup; the audit overlapped part of replay.
Initial totals 32.702 / 21.336 seconds are startup-confounded. No isolated speed claim,
held-out evaluation, official RHAE result or competition submission.

## Verification and disposition

Candidate: **25 tests passed**, including ten new cases; formatting/lint and **ten
notebook source/compilation checks** pass. An independent row-based estimator verifies
all recorded candidate forecasts, local invariance, raw pixel differences, legal
choices and 600 synthetic records. All 15 baseline trajectories, scores and observations
exactly match October 21. All 600 synthetic records and 30 public runs replay exactly;
the additional 3,000 replay actions are repeated evidence.

Archived patch, changed source, tests and runner. Reverse/forward patch checks pass.
After removal, production matches main; **15 tests**, format/lint and ten notebook
checks pass. Only this report and the plan note are committed. Raw evidence is ignored
and hash-mirrored into the original workspace under
`experiments/results/2026-10-22-source-balanced-transfer/`; it is not pushed.
Patch SHA-256: `afbfe47f6b1fab3a27c8c69dc0211c90c88eaf9f0d7d79eded01e07fbc209bad`.

To reproduce, apply that patch to the base and restore its frozen baseline/protocol
at the evidence path. With recorded dependencies and cached engine, run
`python experiments/run_source_balanced_transfer.py --output <ignored-path>` using
writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. The evidence directory also
contains the independent audit and packaging verifier.

Recommend merging the negative record and rejecting unconditional source balancing.
Future transfer work needs evidence about which observed contexts resemble the next
unseen state, and a decision-relevant prediction target. Do not infer improvement
from synthetic uniform-context performance alone.
