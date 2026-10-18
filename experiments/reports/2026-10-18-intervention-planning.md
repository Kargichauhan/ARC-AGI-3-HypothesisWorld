# Intervention-consistent planning factorial — 2026-10-18

Decision: **reject the implementation; merge the research record**. Exact click
identity and path-exclusive novelty interact strongly on immediate synthetic
discovery, but do not improve public completion. Candidate code, tests and runner
were archived under ignored results and removed before commit.

## Hypothesis and fixed criteria

Hypothesis: exact local intervention identity becomes useful when the planner
stops rewarding observed self-loops. Together these changes should improve discovery
and completion beyond either alone. September 19 rejected identity alone and
September 20 rejected path-exclusive novelty alone; their interaction remained
untested. This is a new factorial test of those frozen mechanisms, not a new claim
about either component. No spatial-proposal or probe-deferral change was included.

All gates were recorded before implementation and measurement:

- Nine-click discovery, 100 paired seeds, 18-action cap: joint solves at least
  95/100; mean capped actions at least 20% below baseline and 10% below each component.
- Three positive controls, 100 seeds each: four-key immediate discovery,
  single-click immediate, and single-click four-hit. Each baseline must solve at
  least 95/100; joint loses at most five percentage points and costs at most 1.25x.
- Five cached official public games, F, seeds 0/1/2, 100 actions each: joint adds
  at least one level over baseline **and each component**, without per-game summed
  regression against baseline. Warm runtime at most twice baseline.
- Unit tests, formatting/lint, notebook generation, source equality and compilation.

The nine-click four-hit fixture was a preregistered diagnostic. No threshold,
parameter, policy or fixture was retuned after results. A–E runs were conditional
on passing F; they were unnecessary after the failed completion gate.

## Design and provenance

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`, current remote main.
Inspected the clean original checkout, fresh remote main/daily/research branches,
all remote research plans, report introductions and recent reports, git history
and open PRs (none). Cloud reads were slow, so work used an isolated temporary
clone of the fork. No game implementation was read to design the experiment.

Four arms: **baseline**, **identity**, **path**, **joint**. Identity retains exact
coordinates in local novelty, transitions and planner edges, while pooling global
novelty, outcome fallback and hypotheses by the original colour/region key. Path
pays state novelty once per rollout, excluding the root and repeated destinations,
with no leaf double payment; immediate progress survives. Each production change
and its original tests were reapplied directly from the archived September patch.
Three new tests exercise combined selection, same-frame progress and local risk.
Proposals, weights, model confidence, horizon and RNG are unchanged.

The runner strips coordinate keys for baseline/path and loads the frozen baseline
planner for baseline/identity. All arms use the ordinary full selector and adapter.
Public baseline trajectories, scores and proposals exactly match October 17 on all
15 runs, independently checking that the factorial baseline reproduces main.

Synthetic discovery offers nine background coordinates in one coarse region of
a 12x12 frame. A uniformly sampled target produces visible change and progress;
others do nothing. Target RNG is `20261018 + seed`; selector RNG is `seed`, 0–99.
Four-key discovery uses the same construction with four keyboard actions. Four-hit
fixtures reset their hidden streak after a different action. These are designed
fixtures and label permutations, not independent ARC tasks. Single-action controls
are intentionally easy and do not establish competent multi-action delayed planning.

Public evaluation uses official `arc-agi==0.9.9`, `arcengine==0.9.3`, OFFLINE cached
games and harness source matching pinned revision
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Exact source/game hashes and dependency
versions are retained. Arm order reverses for seed 1. All 60 runs use 100 actions:
6,000 total. Held-out benchmark access and official RHAE were not evaluated; there
was no competition submission.

## Results

Each cell lists **solves / mean capped actions**, over 100 seeds.

| Synthetic fixture | Baseline | Identity | Path | Joint |
|---|---:|---:|---:|---:|
| Nine-click immediate | 85 / 7.90 | 100 / 9.92 | 85 / 7.90 | 100 / 4.83 |
| Four-key immediate | 100 / 3.12 | 100 / 3.12 | 100 / 2.49 | 100 / 2.49 |
| Single-click immediate | 100 / 1.00 | 100 / 1.00 | 100 / 1.00 | 100 / 1.00 |
| Single-click four-hit | 100 / 4.00 | 100 / 4.00 | 100 / 4.00 | 100 / 4.00 |
| Nine-click four-hit, diagnostic | 0 / 18.00 | 10 / 16.60 | 0 / 18.00 | 0 / 18.00 |

Joint immediate discovery is 38.86% cheaper than baseline/path and 51.31% cheaper
than identity. It visits each click at most once before success. All synthetic
retention gates pass. The paired capped-cost interaction
`joint - identity - path + baseline` is -5.09 actions; a 10,000-resample seed
bootstrap interval is [-5.81, -4.38]. This describes permutation variability on
this fixture, not generalization uncertainty. The four-hit diagnostic shows a
limit: joint loses identity's 10 solves and cannot discover hidden accumulation.

Public completed levels by seed 0/1/2:

| Game/version | Baseline | Identity | Path | Joint |
|---|---|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 |
| Total | **2** | **2** | **2** | **2** |

No public completion improvement: the retention gate fails. No-op transitions
(same fingerprint, no positive progress) are 595 / 595 / 479 / 463; consecutive
identical action-coordinate choices are 746 / 664 / 409 / 411. These repeat counts
ignore source identity and differ from older reports' same-state repeat metric.
All 300 ft09 transitions remain no-ops. Joint reduces cn04 no-ops from 128 to 89
and su15 from 100 to 8, without adding levels.

Initial subprocess totals (baseline / identity / path / joint) were
27.122 / 13.042 / 12.958 / 13.462 seconds; baseline's first process took 18.888
seconds, so this is startup-confounded. Warm replay totals were
10.908 / 10.852 / 10.902 / 10.969 seconds: joint/baseline **1.006x**, passing the
runtime gate. Startup and equal tracing overhead are included; no isolated speed
claim. All 60 public trajectories/scores and 2,000 synthetic records replay exactly,
with an unchanged source manifest. The extra 6,000 public actions are repeated
evidence, not additional independent trials.

## Verification and disposition

Candidate: 32 tests pass (15 baseline, 14 reused component tests, three new joint
tests), formatting/lint pass, notebook generated and all 10 embedded modules match
source and compile. Independent prefix audit checks 5,948 public decisions,
6,463 eligible self-loop planner scores and 13,237 synthetic steps across 2,000
records, including legality, identity, local/global novelty, local progress/risk,
ranked selection, target streaks and solve claims. All 15 baseline runs reproduce
October 17 exactly. The audit implementation is separate from policy selection.

Archived candidate patch SHA256:
`d65b518ec854680262c1ca0d7aac005b7dfdda8f056d7cb96e5e0cf165f8c2e8`.
Forward and reverse patch checks pass. After restoring the five production files
and removing the three experimental test files and runner, production matches
main exactly.
The restored baseline passes all 15 tests, formatting/lint, notebook generation and
all 10 packaged-source equality/compilation checks. Only this report and
`RESEARCH_PLAN.md` are committed.

Raw protocol, dependency/source/game manifests, sanitized logs, compressed traces,
initial/replay summaries, audit, baseline sources and complete candidate patch are
ignored under `experiments/results/2026-10-18-intervention-planning/`, mirrored to
the original workspace with hash verification. Reproduction: apply the archived
patch to the base, use the recorded dependencies and cached games/harness, then run
`python experiments/run_intervention_planning.py --output <ignored-output-dir>`.
The runner also needs the archived baseline planner and protocol at the evidence
path. This local evidence archive is not included in the pushed report commit.

Recommendation: merge the negative research record, reject the mechanism. The
interaction resolves a real immediate-discovery failure on the designed fixture;
it does not establish a useful public-game solver improvement. Future work needs
observable evidence for when to persist versus switch, and proposals that reach
useful interventions, with competent multi-action delay controls. Do not rerun
this fixed combination without a distinct, preregistered causal question.
