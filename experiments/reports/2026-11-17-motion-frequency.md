# Rolling motion frequency — 2026-11-17

Decision: **reject implementation; merge this negative research record**.
Candidate code, four tests and runner were archived and removed; production matches main.

## Hypothesis and fixed gates

Probabilistic motion frequencies should downweight obsolete alternatives without
the noise sensitivity of hard contradiction streaks. Unlike November 16 hard rejection,
November 1 cumulative credibility, and October 13 transition replacement, this changes
hypothesis mixture weights using a bounded motion-frequency window.

Before implementation: require >=50% stale positive-motion mass reduction over reversal
steps 56–63; <=.01 absolute Brier increase in EACH stationary and Bernoulli(.1/.5/.9)
control over steps 32–63; all validation passing. Conditional public gate: five cached
games, F, seeds 0/1/2, 100 actions, >=1 extra level, no per-game summed regression,
<=2x runtime. No parameters, gates or fixtures retuned after measurement.

Base/main: 24a5f4173ecb2fadf88360b38c0a77bad8175b65. Inspected memory, current main
plan/history, fresh remote daily/research refs and relevant reports. GitHub open PR
search returned none. Isolated clone /private/tmp/hw-research-20261117 preserved the
original checkout. No unmerged implementation or game-source design information used.

## Mechanism

Only production change: agent/hypotheses.py. Store last 16 known motions per exact
ActionKey, bounded to 512 FIFO keys. Unknown motion neither appends nor ages history.
Multiply each explicit-motion hypothesis's floored effective belief by
(1 + motion count)/(window length + category count). Categories union history and
active predicted motions. Unspecified-motion weights stay neutral; normalize.

Original updates, rejection, generation, pruning, world model and policy remain.
This empirical reweighting is not a Bayesian posterior: observations also inform
original beliefs. Lowering specified-motion weights relative to unspecified rules
can alter entropy; full-outcome calibration is not established.

## Synthetic evidence

200 paired seeds/family, 64 supplied outcomes, two arms: 128,000 step records.
RNG 20261117 + seed varies action/colour and stochastic signs. Reversal is 16 positive-x
then 48 negative-x motions; stationary always positive. Pre-update forecasts renormalize
positive mass over explicit-motion rules, default .5 if absent. Deterministic streams
vary labels, not task logic. These are supplied-outcome diagnostics, not online solves.

| Metric | Baseline | Candidate |
|---|---:|---:|
| Reversal final-eight stale positive mass | .500000 | .055556 |
| Stationary Brier | .000000 | .000000 |
| Bernoulli(.1) Brier | .249201 | .098387 |
| Bernoulli(.5) Brier | .250000 | .262048 |
| Bernoulli(.9) Brier | .248081 | .095809 |

Stale mass falls 88.89%; fair-coin loss increases .012048, exceeding .01 allowance.
Recent frequencies add sampling variance even without hard rejection. Reject this
fixed window; do not retune against the same controls or promote aggregate gains.

Public tests skipped at failed synthetic gate. Official access was not tested;
this is not evidence of unavailable access. No completion, held-out, RHAE or speed claim.

## Verification and disposition

Candidate 19 tests pass (four new): frequency odds/normalization, window adaptation,
retained alternatives, action isolation, unknown motion and bounded storage.
Formatting/lint pass; ten notebook modules equal source and compile.
Independent audit verifies all 128,000 rows' RNG inputs, pairing, forecasts, losses
and summaries; reconstructs 64,000 candidate weight vectors from baseline weights
and preceding observations. Raw records and summaries replay byte-for-byte.
After removal: 15 tests, formatting/lint and ten notebook source/compile checks pass.
Production matches main; patch passes forward/reverse applicability checks.

Ignored evidence: experiments/results/2026-11-17-motion-frequency/ contains protocol,
baseline/candidate/tests/runner/patch, raw records, summary, audit, replay hashes,
dependencies, validation and remote refs. Mirrored with SHA256 verification into
the original workspace; raw evidence is local, not pushed.
Reproduce from base: apply candidate.patch, restore baseline.py at the evidence path,
then PYTHONPATH=. python experiments/run_motion_frequency.py.

Commit only this report and RESEARCH_PLAN.md. Recommend merging research record and
rejecting implementation. Future work should compare stationary and switching
probabilistic models explicitly instead of treating a fixed recent window as evidence
of a changed rule.
