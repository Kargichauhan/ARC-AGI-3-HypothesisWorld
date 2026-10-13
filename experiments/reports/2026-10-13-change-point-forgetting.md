# Change-point forgetting — 2026-10-13

Decision: **reject the implementation; merge the research record**. Forgetting old
local evidence improved a designed regime-switch prediction task, but never
activated on the public games; completion stayed 2 → 2. Candidate, tests and runner
were archived and removed. Production matches main.

## Hypothesis and fixed gates

Hypothesis: a persistent contradiction at an otherwise stable state/action marks a
changed rule; forgetting obsolete local observations improves post-switch prediction
and public completion. This tests temporal replacement of empirical evidence, unlike
the prior action-history fallback, state-conditioned hypotheses and confidence prior.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean checkout, fetched
origin/upstream, main plan/history, remote research/daily branches, recent reports
and automation memory. GitHub's public API returned no open PRs. No unmerged
mechanisms, game-source design inspection, parameter retuning or submission.
Cloud-backed file reads stalled; implementation and evaluation used a fresh temporary
clone of the verified fork. Cached public games were copied without inspecting their
source for design. Official harness revision `4743e7d0aaae0ded0d98a89a7e282e63564cd58b`.

All gates fixed in the ignored protocol before measurement:

- 100 paired synthetic seeds, 120 observations per stream, deterministic rules
  switching every 30 observations: at least 30% lower mean Brier loss across the
  first ten predictions after each switch, averaged over progress/failure/change.
- Stationary Bernoulli p=.5/.75/.9: each mean Brier increase at most .01, excluding
  six initial predictions. Two- and five-observation regimes are diagnostics only.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra completed
  level, no per-game summed loss, warm total subprocess runtime at most 2x baseline.
- Unit tests, formatting/lint and notebook generation/source/compile checks pass.
  Broader A–E runs conditional on F passing. Remove candidate if any gate fails.

## Mechanism

Retain nine joint observations per exact source fingerprint/ActionKey, at most 512
FIFO detector contexts. The signature includes target fingerprint, complete outcome
signature and `diff.changed`. If the oldest six signatures agree, the newest three
agree, and the two groups differ, rebuild that local source/action's transition,
progress, failure and change counts from the newest three. Clear the detector after
a switch. Detector eviction does not erase the learned model. Global fallback
statistics keep all observations. The planner, hypotheses, action proposals,
identities, selector weights and random draws remain unchanged.

This is a fixed persistence detector, not Bayesian change-point inference. Repeated
outcomes can reflect hidden state, stochasticity or pooled click coordinates rather
than a changed rule; the detector cannot distinguish those explanations. It also
needs six fresh stable observations after clearing before detecting another switch.

## Synthetic evidence

Each stream supplies the same observations to both models and measures predictions
before updates. Binary outcomes couple positive progress/visual change with absence
of failure; opposite outcomes supply failure and no change. These are injected
outcomes, not engine episodes or online solves. Source/action labels and initial
polarity use seeds `20261013 + i`; stationary outcomes use the same seeded stream.
Deterministic fixtures have only two polarity patterns, not 100 independent tasks.

| Fixture | Baseline Brier | Candidate Brier | Candidate detections |
|---|---:|---:|---:|
| 30-observation switches, first ten after switch | .464689 | .281543 | 300 |
| Stationary p=.50 | .256019 | .260103 | 41 |
| Stationary p=.75 | .194546 | .200017 | 32 |
| Stationary p=.90 | .095463 | .097345 | 9 |
| Two-observation switches | .258420 | .258420 | 0 |
| Five-observation switches | .263395 | .263395 | 0 |

Primary loss falls **39.41%**, passing the 30% gate. Stationary increases
**.004084/.005471/.001882** pass the .01 tolerances, but false detections harm
calibration. Rapid deterministic switches never satisfy the six-stable-observation
requirement. The primary score contains 3,000 forecasts per arm; other rows contain
11,400 each. Raw data retain all 144,000 arm/stream/step records, including warmup.
Forecasts within each fitted stream are dependent.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3, exact versions below.
Primary cohort: **30 runs / 3,000 actions**, alternating arm order by seed. Entries
list completed levels for seeds 0/1/2.

| Game/version | Baseline | Candidate |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Totals **2 → 2** fail the completion gate. **Zero switches and zero decisions with
changed predictions** in either arm's paired model audit. All 15 paired selected
scores/actions and transition traces match exactly. Both have 595 same-fingerprint,
non-positive-progress transitions and 746 consecutive identical selected action/
coordinate pairs; this repetition count ignores source identity and differs from
prior reports' repeat metric. All 15 baseline traces and selected scores exactly
match October 10's preserved baseline evidence, despite updated transitive packages.

An independent prefix-only audit rebuilt local/global predictions and checked all
**1,488 forecasts per arm**. It found **376 nine-observation windows per arm**;
every window had six identical older observations and no contradictory recent
observation at all. Thus the persistence condition was not narrowly missed by one
sample in those windows. Resets account for the difference between action and
recorded-transition totals. Evidence supports inactivity under this budget, not
absence of nonstationarity in ARC environments generally.

Initial elapsed totals **21.626 → 9.461 s** were startup-confounded (first baseline
process 15.168 s). Warm replay **10.942 → 9.565 s**, ratio **.874x**, passes the
runtime gate. Both arms maintain both models for equal shadow auditing; timings
include startup and I/O and do not establish production speedup.

All 30 public runs and all 144,000 synthetic records exactly replay. The additional
3,000 public actions are deterministic replay, not independent evidence. Dependencies,
source/game hashes and traces are preserved. No held-out evaluation, official RHAE
measurement or competition submission occurred.

## Validation and disposition

Candidate: **22 tests passed**, including seven new tests for persistence, same-frame
progress/failure changes, local-edge replacement, preserved global evidence, context
isolation, detector eviction and repeated switches. Formatting/lint and **10 notebook
module source/compile checks** passed. Archived candidate source/tests/runner/patch,
then removed them. Final baseline: **15 tests**, formatting/lint and the same **10**
notebook checks passed. Patch forward/reverse applicability checked.

Reject this detector for deployment. Before another forgetting mechanism, establish
persistent outcome changes at revisited, precisely identified interventions and
measure their policy relevance. Artificial switches establish adaptation ability;
they do not justify retaining inactive production machinery or relaxing completion.

Ignored evidence: `experiments/results/2026-10-13-change-point-forgetting/`, including
protocol, raw synthetic/public/replay records, audits, source/dependency manifests,
validation, frozen baseline and candidate patch. Raw evidence is not pushed.
Patch SHA256: `43932287b2be2ae385d9173693a029f4e22d82826d7bb8cb30b16216ba1b7c69`.
To reproduce, apply the patch to the base, retain the frozen model/protocol in that
ignored directory, restore recorded dependencies/cached games/harness and run
`python experiments/run_change_point.py --output <ignored-directory>` with writable
plotting/cache paths. Only this report and the research-plan note are committed.
