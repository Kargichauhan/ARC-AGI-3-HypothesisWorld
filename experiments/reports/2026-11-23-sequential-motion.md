# Lifetime-budget motion detection — 2026-11-23

Decision: **reject implementation; merge the negative research record**. Lifetime
alpha spending suppresses false resets but renders a fixed-window detector blind to
late reversals. Candidate code and five tests were archived and removed.

## Hypothesis and fixed protocol

A summable lifetime false-alarm budget should allow motion-rule replacement without
stationary false resets or loss of early/late adaptation. This addresses November 22's
18% fair-coin false-reset rate. The joint candidate changes the budget and doubles
the window to restore power; this is not an ablation separating those two effects.

Protocol written before implementation: detect >=95% of early AND late reversals
within 32 new outcomes; halve final 32 post-switch Brier loss in each; <=1% of streams
reset and <=.01 Brier increase in EACH stationary control; validation passes.
Conditional public gate: five cached games, F, seeds 0/1/2, 100 actions, >=1 extra level,
no per-game regression, <=2x runtime. No retuning after measurement.

Base/main: 24a5f4173ecb2fadf88360b38c0a77bad8175b65. Inspected memory, current main
plan/history, fresh remote daily/research refs, recent reports including November 15/17
and local November 21/22 evidence. Connected GitHub open-PR search returned none.
Isolated clone preserves original tracked checkout. No game-source design information
used; no earlier unpublished branch pushed.

## Candidate

Only agent/hypotheses.py changes production. Store 32 known scalar motions per exact
ActionKey, 512 FIFO keys. Compare adjacent 16 windows with two-sided Fisher exact test;
abstain unless exactly two categories. Every full-window test spends
alpha_n=.01/[n(n+1)] from one engine-wide counter, never replenished by reset/eviction.
On rejection invalidate exact-key explicit-motion rules, clear motion cooldowns/window,
then perform ordinary update. Unknown motion does not advance the detector.

The schedule sums to .01. A union-bound interpretation requires valid p-values for
the tested sequence; synthetic controls use fixed sampling and independent stationary
outcomes. No general guarantee is established under adaptive action selection, latent
state changes or multiple engine lifetimes. Observed reset rates are not confidence
bounds on a true 1% error rate.

## Synthetic evidence

998,400 paired arm-step records. 40 replicates per deterministic reversal, 200 seeds per
control. Switches at zero-based steps 64/2048, ending 64 new outcomes later; controls
last 512 outcomes. RNG 20261123+seed. Deterministic replicates are identical, not independent
tasks. Shared random streams across stochastic families/arms are intentional. Injected
single-object StateDiff streams isolate retention; these are not game solves.
Pre-update forecasts normalize explicit-motion weights, defaulting to .5 when absent.
Score final 32 post-switch outcomes and control steps 32–511.

| Family | Baseline Brier | Candidate Brier | Streams reset |
|---|---:|---:|---:|
| Early reversal | .250000000 | .000000000 | 40/40 |
| Late reversal | .250000000 | .250000000 | 0/40 |
| Stationary deterministic | .000000000 | .000000000 | 0/200 |
| Bernoulli .1 | .249883672 | .249883672 | 0/200 |
| Bernoulli .5 | .250000000 | .250010202 | 1/200 |
| Bernoulli .9 | .249763308 | .249763308 | 0/200 |

Early resets occur at step 76, the 13th new outcome. The fair-coin false reset is at
step 34. Late detection/loss gates fail. Minimum attainable two-sided p-value is
2/choose(32,16)=3.32734e-9. At the perfectly separated late window, test 2033,
alpha=2.41831e-9: even maximal evidence cannot trigger. The spending schedule eventually
makes every fixed-size test powerless. The analytic limit supports the measured failure.

Public evaluation skipped after synthetic failure, as preregistered. Official access
was not tested and is not claimed unavailable. No public completion, speed, held-out
RHAE or competition-submission result is reported.

## Validation and disposition

Candidate: 20 tests pass: exact probability, reset scope/cooldowns, unknown motion,
bounded storage, and budget persistence across reset/eviction. Format/lint and ten
notebook source-equality/compilation checks pass. Independent factorial-based audit
checks every trigger, RNG input, paired outcome, loss and summary across 998,400 rows.
Python 3.12 replay is byte-identical to the first Python 3.14 run; no speed claim.
After removal: 15 baseline tests, format/lint and ten notebook checks pass. Production
matches main; candidate patch passes forward/reverse applicability checks.

Only this report and RESEARCH_PLAN.md are committed. Recommend merging the record
and rejecting this fixed-window spending mechanism. Future work needs sensitivity
throughout the evaluation horizon, not merely a summable false-alarm allocation.

Ignored evidence: experiments/results/2026-11-23-sequential-motion/ contains protocol,
baseline/candidate/tests/patch, runner, raw rows, summary, audit, validation and SHA256
manifest, mirrored to original workspace. Raw evidence is local, not pushed. Reproduce
on base by applying candidate.patch and running `PYTHONPATH=. python3.12
experiments/results/2026-11-23-sequential-motion/benchmark.py`, then audit.py.
