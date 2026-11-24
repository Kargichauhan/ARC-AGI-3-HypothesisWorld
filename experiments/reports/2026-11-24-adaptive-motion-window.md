# Multi-scale motion detection — 2026-11-24

Decision: **reject implementation; merge the negative research record**. Multiple
windows restore deterministic late-change detection but noisy adaptation is too slow.
Candidate code and six tests were archived and removed before commit.

## Hypothesis and fixed protocol

Hypothesis: multiple temporal scales restore early/late motion-change sensitivity
under lifetime false-alarm spending, including stochastic reversals. This extends
November23's fixed-window power failure; it is a finite scale bank, not learned windows.
Base/main:24a5f4173ecb2fadf88360b38c0a77bad8175b65. Inspected memory, fresh remote
main/daily/research refs, main plan/history, recent reports and local November22 evidence.
Connected GitHub open-PR search found none. Original index reads timed out; isolated
clone preserved the original tracked checkout. No game-source design information used.

Before implementation: require >=95% detection within32 new outcomes and >=50% final32
Brier reduction in EACH deterministic/noisy early/late reversal; stationary controls
must reset <=1% of streams and increase Brier <=.01. Validation must pass. Conditional
public gate: five games, F, seeds0/1/2,100 actions, >=1 extra level, no per-game regression,
<=2x runtime. No parameters or gates retuned after measurement.

Protocol defect: halving raw Brier from .25 targets .125, below the .16 Bayes loss of
Bernoulli(.8), so the noisy loss gate is inappropriate as a population target. Even
post-hoc halving excess loss above .16 (target .205) fails. Rejection independently
follows the valid preregistered latency gate. Future protocols should preregister
excess proper-score improvement for noisy outcomes.

## Mechanism

Only agent/hypotheses.py changes production. Up to128 known scalar motions per exact
ActionKey,512 FIFO keys. Test adjacent equal halves of8,16,32,64, shortest first,
with two-sided Fisher exact probabilities; abstain unless exactly two categories.
Every eligible test, including constant windows, consumes alpha_n=.01/[n(n+1)] from
one global counter surviving reset/eviction. First rejection invalidates exact-key
explicit-motion rules and cooldowns, clears history, then performs normal update.
Unknown motion does not advance it. The schedule sums to .01, but any union-bound
interpretation requires valid p-values; independent fixed-sampling controls do not
prove guarantees under adaptive selection or multiple engine lifetimes. A finite
scale bank eventually exhausts power too, because attainable p-values are bounded.

## Evidence

1,177,600 paired arm-step rows,960 streams.40 seeds per reversal,200 per control.
Switches at offsets64/2048, then64 new outcomes; controls512 steps. Noisy reversals
change Bernoulli probability .2 to .8. RNG20261124+seed, paired outcomes. Deterministic
replicates are identical, not independent tasks. Injected single-object StateDiffs
isolate retention, not game solves. Pre-update forecasts normalize explicit-motion
weights, default .5; score final32 post-switch outcomes or control steps32–511.

| Family | Baseline Brier | Candidate Brier | Detected within32 | Any reset |
|---|---:|---:|---:|---:|
| Early deterministic | .250000000 | .000000000 | 40/40 | 40/40 |
| Late deterministic | .250000000 | .000000000 | 40/40 | 40/40 |
| Early noisy | .250000000 | .245206264 | 22/40 | 40/40 |
| Late noisy | .250000000 | .243505897 | 1/40 | 31/40 |
| Stationary deterministic | .000000000 | .000000000 | — | 0/200 |
| Bernoulli .1 | .249883672 | .249883672 | — | 0/200 |
| Bernoulli .5 | .250000000 | .250000000 | — | 0/200 |
| Bernoulli .9 | .249763308 | .249763308 | — | 0/200 |

Deterministic latencies14/24 observations; noisy detected-event ranges16–64/31–64.
Zero observed false resets is not a confidence bound on a true1% rate. Multiple scales
rescue clean late signals but fail noisy latency; other designs remain untested.
Public evaluation skipped after synthetic failure. Official access untested, not
claimed unavailable. No completion, speed, held-out RHAE or submission claim.

## Validation and disposition

Candidate21tests, format/lint and10 notebook source-equality/compilation checks pass.
An initial eviction test accidentally reused an existing key; fixed its fixture to
use fresh keys. Independent factorial-based audit checks every trigger, paired input,
RNG outcome, loss, latency and summary. Final baseline15tests, format/lint and10-module
packaging checks pass. Production matches main; patch forward/reverse checks pass.
Only this report and RESEARCH_PLAN.md committed. Recommend merging the record only.

Ignored evidence: experiments/results/2026-11-24-adaptive-motion-window/ contains
protocol, baseline/candidate/tests/patch, runner, raw rows, summary, audit, validation
and hash manifest, mirrored to original workspace. Raw data not pushed. Reproduce on
base by applying candidate.patch, running benchmark.py with PYTHONPATH=., then audit.py
(Python3.12, pytest8.4.2). check_notebook.py verifies all10 packaged modules.
