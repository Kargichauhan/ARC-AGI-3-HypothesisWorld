# Posterior information gain pilot — 2026-09-17

Decision: **reject the implementation**. A controlled diagnostic test passed, but
public-game completion regressed. Production code, configuration, and tests were
restored to the base revision before committing this report.

## Hypothesis and preregistered gate

Hypothesis: posterior expected information gain (EIG) can distinguish incompatible
outcome predictions from compatible broad/specific refinements, improving diagnostic
action selection and public-game completion over entropy of prediction labels.

Before implementation, the protocol was saved under the ignored result directory.
The acceptance criteria were:

- Select the incompatible probe in at least 90/100 synthetic trials and improve
  over label entropy by at least 20 percentage points.
- On five cached public games, with full agent F, seeds 0/1/2 and 100 actions per
  game: no decrease in summed levels for any game and at least one additional
  completed level overall.
- Total run time no greater than twice the entropy baseline.

## Method

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65` (`origin/main`). The origin was
fetched; there were no open PRs or remote daily branches. The stable-state branch
and September 15 pilot were inspected but not incorporated into this experiment.

The candidate replaced only the information term in experiment selection. Each
partial hypothesis defined a product of categorical likelihoods over all seven
`OutcomePattern` fields. Unspecified fields were uniform; specified fields used
5% uniform contamination. Domains contained predicted values plus a residual
category, or both boolean values. Sixteen stratified rollouts per hypothesis
estimated expected posterior KL divergence, normalized by log of the number of
unique prediction patterns. Samples were deterministic; an LRU cache avoided
repeated evaluation. Reward, risk, novelty and planning weights were unchanged.
This was an assumed observation model; the agent's heuristic belief updates were
unchanged and were not calibrated Bayesian posteriors.

The synthetic fixture paired conflicting `changed` predictions (prior sampled
uniformly from 0.2–0.8) with equally weighted compatible broad/specific predictions.
Action order was shuffled, fixture seed 20260917. This deliberately adversarial
fixture tests one ranking failure; it is not a representative task distribution.

The official installed local engine ran in OFFLINE mode to pin cached versions.
The existing `scripts/play_local.py` and framework adapter were reused; the runner
changed only Arcade construction to OFFLINE. Both arms received identical seed
configuration support, since main did not read `HYPOTHESISWORLD_SEED`. Arm order
alternated across seeds. All 30 game runs returned successfully and used 100
actions each (3,000 actions total). Only ablation F was tested; the failed gate
made a broader ablation sweep unnecessary for the rejection decision.

## Results

Synthetic diagnostic choices: entropy **0/100**, EIG **100/100**. Gate passed.

Completed levels, with seed results listed in order 0/1/2:

| Public game/version | Entropy | EIG |
|---|---|---|
| `su15-1944f8ab` | 0 / 0 / 0 | 0 / 0 / 0 |
| `cn04-2fe56bfb` | 0 / 0 / 0 | 0 / 0 / 0 |
| `ft09-0d8bbf25` | 0 / 0 / 0 | 0 / 0 / 0 |
| `vc33-5430563c` | 1 / 0 / 1 | 1 / 0 / 0 |
| `ls20-9607627b` | 0 / 0 / 0 | 0 / 0 / 0 |

Total levels: **2 → 1**. Both completion criteria failed. Total subprocess wall
time was 9.233 s for entropy and 10.279 s for EIG (**1.113×**); runtime gate passed.
Timing includes startup and is a local pilot measurement, not a stable latency claim.

The candidate passed 23 unit tests, including an analytic binary-channel check,
identical predictions, compatible refinements, order invariance, rare priors, and
invalid parameters. Formatting and lint passed. Notebook generation succeeded;
all 11 embedded Python modules matched source and compiled. After candidate
removal, all 15 baseline tests, formatting, lint and notebook packaging passed;
the final notebook contains the original 10 modules.

## Interpretation and evidence

Improved ranking on the designed fixture did not transfer to this public-game
pilot. Uniform wildcard likelihoods, conditional independence, heuristic beliefs,
and a changed scale for the information term remain unvalidated assumptions.
The observed loss does not isolate which assumption caused it. There was no
post-result retuning or expansion of the success criterion.

These are cached public-game results, not held-out benchmark results or an
official Relative Human Action Efficiency claim. The main-branch representation
differs from the unmerged stable-state pilot, so their scores are not directly
comparable. Do not promote this EIG estimator based on synthetic success alone.
A future attempt should first validate observation likelihoods and measure
information-term calibration on separate trajectories.

Raw evidence is local and gitignored at
`experiments/results/2026-09-17-posterior-information/`: preregistered `protocol.md`,
`synthetic.json`, `public.json`, six arm/seed logs, validation logs, game/source
hashes and dependency versions in `manifest.json`, and the removed implementation,
runner and tests in `candidate.patch`. Candidate patch SHA-256:
`ab6a6bb2f670d27bfbc023d4fb97839580c67162c71914892a5675c41820088e`.

For local reproduction, start from the base revision, apply that archived patch,
and run `.venv/bin/python experiments/run_posterior_information.py --output
experiments/results/posterior-reproduction`. The archive is not shipped with the
branch; the tracked report is the durable record of this negative experiment.
