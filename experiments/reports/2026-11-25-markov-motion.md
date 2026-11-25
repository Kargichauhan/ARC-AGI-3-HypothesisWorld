# Markov motion mixture — 2026-11-25

Decision: **reject implementation; merge the research record**. Synthetic temporal
prediction improved, but official public completion regressed. Candidate removed.

## Hypothesis and frozen protocol

An equal-prior Bayesian mixture of IID and first-order categorical motion models
can learn alternating/persistent effects without hard resets, while retaining
stationary calibration. Unlike November17 frequencies and November22–24 change
tests, it models dependence on the previous observed motion.

Base/main:24a5f4173ecb2fadf88360b38c0a77bad8175b65. Inspected fresh main, remote
research/daily refs, history, plan, automation history and relevant recent reports.
Connected GitHub open-PR search found none. Isolated clone preserved original
tracked files; no unmerged implementation incorporated.

Before implementation: each temporal/reversal family must reduce excess Brier
>=50% (Bayes floor .16 for stochastic Markov streams, zero otherwise); each stationary
control may worsen <=.01. Then require >=1 extra public level, no per-game summed
regression, <=2x runtime. No retuning.

## Mechanism

Only agent/hypotheses.py changed production. Keep128 known scalar motions per exact
ActionKey,512FIFO keys; unknown motion does not advance history. Compute IID and
first-order Dirichlet(1/2) row evidence on the same transitions, conditional on the
first observation. Mix next-motion distributions with equal model priors. Multiply
existing explicit-motion weights by this forecast and rescale to preserve their
group mass; unspecified-motion weights remain unchanged. Rule generation/rejection
unchanged. This auxiliary Bayesian mixture is not a calibrated posterior over full
outcome rules: reweighting uses observations already seen by original belief updates.
Alphabet includes history and active predictions. No-op gaps and cross-episode
history remain limitations; no latent-state identification claim.

## Synthetic results

Seed20261125+s;200 seeds per512-step control/Markov family,40 per reversal at64/2048
followed by64 outcomes. Score steps128–511 or final32 post-reversal.806,400 paired
records/1,612,800 arm forecasts. Supplied single-object outcomes, not game solves;
deterministic seed replicates are identical. Pre-update forecasts normalize positive
weight over explicit-motion rules (.5 if absent).

| Family | Baseline Brier | Candidate Brier |
|---|---:|---:|
| Alternating | .250000 | .000061 |
| Flip probability .8 | .250000 | .160934 |
| Stay probability .8 | .250000 | .162960 |
| Constant | .000000 | .000000 |
| IID .1 | .250000 | .090931 |
| IID .5 | .250000 | .252294 |
| IID .9 | .250000 | .089166 |
| Early reversal | .250000 | .000125 |
| Late reversal | .250000 | .000125 |

All synthetic gates pass. Independent audit verifies every RNG input, loss and
summary, plus6,040 sampled forecasts reconstructed using sequential predictive
likelihood products instead of the implementation's gamma-function evidence.

## Official public results

Official environments downloaded then evaluated OFFLINE: arc-agi0.9.10,
arcengine0.9.3, framework revision recorded in evidence. F,seeds0/1/2,100 actions,
30 runs/3,000 actions; arm order alternates by seed. Baseline engine uses shared
ActionKey class to preserve equality across modules.

| Game/version | Baseline levels by seed | Candidate levels by seed |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/0 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Total2→1: fails improvement and no-regression gates. Agent-loop time6.812→6.681s
(.981x); no statistically established speed claim. Audit verifies all3,000 frame
step counts and final levels against summary. This small public cohort supports
rejection under the fixed gate, not a universal performance conclusion. No held-out
RHAE claim or competition submission.

## Validation and disposition

Candidate19tests (four new), formatting/lint and10-module notebook source/compile
checks pass. New tests cover alternation, mass preservation, isolation, unknown
motion and storage bounds. Candidate/tests removed; final baseline15tests and same
checks pass. Production matches main; archived patch passes application check.
Only this report and RESEARCH_PLAN.md committed.

Ignored evidence: experiments/results/2026-11-25-markov-motion/ contains protocol,
baseline/candidate/tests/patch, synthetic/public runners and raw records, audits,
dependency/framework/game hashes, validation and manifest. Mirrored to original
workspace with hash verification. Reproduce from base: apply candidate.patch,
copy candidate-tests.py to tests/test_markov_motion.py; run benchmark.py and audit.py
with PYTHONPATH=.; public.py requires recorded framework and cached official games.

Recommendation: merge negative record, reject policy change. Future work should
isolate how conditional motion calibration affects entropy-based action ranking
before testing another retention estimator.
