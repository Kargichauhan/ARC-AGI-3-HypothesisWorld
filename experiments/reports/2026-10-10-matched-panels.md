# Active matched action panels — 2026-10-10

Decision: **reject the mechanism; retain the research record**. Paired evidence
arrived faster on a synthetic hub but did not increase acquisition success,
increased immediate-goal cost, and added no public levels. Implementation removed.

## Hypothesis and fixed gates

Hypothesis: budgeting comparisons at naturally revisited states supplies useful
matched action evidence that passive exploration misses, improving completion at
acceptable action cost. October 9's passive contrast estimator had no eligible public
decisions. This experiment changes acquisition alone, without adding that estimator.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean checkout,
fetched origin/upstream, current main plan/history, remote daily/research branches,
recent reports and open PRs (none). Reviewed September 22's deferral and September
27's temporal commitment to avoid duplication. No game source informed the policy;
no parameter or gate changed after measurement.

All preregistered retention gates required:

- Recurrent hub, 100 paired seeds, 20 actions: at least 90% obtain three observations
  each for two actions, at least 30 percentage points more than baseline, and at least
  20% lower mean capped acquisition cost.
- Four online controls, 100 paired seeds each, 40 actions: at most five percentage
  points fewer solves per control and mean capped cost at most 1.25x baseline.
  Immediate-goal baseline must solve at least 95%; report other baseline competence.
- Five cached public games, F, seeds 0/1/2, 100 actions each: at least one extra level,
  no per-game summed completion loss, warm runtime at most 2x baseline.
- Tests, formatting/lint and notebook source/compile checks pass. Broader A–E
  evaluation conditional on F passing; not run after rejection.

## Smallest implementation

F-only selection postprocessing admits a panel after two retained outgoing records
from an exact fingerprint. Reference is the highest-ranked zero-predicted-risk key;
challenger is the least-sampled other eligible key, breaking ties by original rank.
Select the less-sampled member until both have three observations. At most 64 panels,
no eviction/reopening. Pause for predicted progress or unavailable members; abandon
on observed panel progress/failure. Exclude RESET/undo; add no return-navigation or
reset actions. Panel state persists across reset, like the existing learned evidence.
Counts use the 512-record memory; evaluated 100-action runs never exhaust it.

Original scores, RNG draws, proposals, hypotheses, model and planner are unchanged.
Clicks retain coarse colour/region ActionKeys: these are action-class comparisons,
not controlled exact-coordinate interventions. Zero estimated risk does not certify
safety; equal frames need not imply equal hidden state.

## Synthetic evidence

Policy seeds 0–99; fixture seed `20261010 + seed` permutes four labels. The hub moves
to distinct spokes; a forced return costs one action. Controls: a one-hit goal,
three consecutive hidden target hits, a hidden ABA sequence, and a visible three-stage
corridor with varying productive actions and inexhaustible unique distractor frames.
Both policies learn online. Means include capped unsuccessful runs.

| Fixture (100 trials) | Baseline successes | Panels successes | Baseline actions | Panels actions |
|---|---:|---:|---:|---:|
| Hub acquisition | 100 | 100 | 19.00 | 15.00 |
| Immediate goal | 100 | 100 | 3.45 | 4.83 |
| Hidden three-hit | 0 | 20 | 40.00 | 34.20 |
| Hidden ABA | 34 | 43 | 32.25 | 29.57 |
| Distractor corridor | 100 | 100 | 7.18 | 7.18 |

Hub cost falls **21.05%**, but coverage gain is **zero**. Immediate cost rises
**40%**, exceeding the 25% allowance. Both failures independently reject the candidate.
Hidden-control competence is limited, especially the zero-solve delayed baseline.
These are five designed fixtures and permutations, not 500 independent ARC tasks.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3, rotating arm order.
**30 runs / 3,000 actions**. Level entries list seeds 0/1/2.

| Game/version | Baseline | Panels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Levels **2 → 2** fail the completion gate. Repeated exact actions **687 → 531**;
equal-fingerprint/no-positive-progress outcomes **595 → 501**. Panels override
ranking **101** times and admit **100** panels. Eligible comparisons increase from
zero to **282** decisions, all in `ft09`, whose 300 candidate transitions are no-ops.
Seven panels have sufficient final counts, but only three are observed complete at
a subsequent decision. The other four never supply an eligible later comparison.
Final sample counts must not be confused with usable online evidence.

The policy collects evidence where recurrence is easy, without showing that it helps
progress. No held-out access, official Relative Human Action Efficiency result, or
competition submission is claimed.

## Verification and disposition

Candidate: **30 tests pass**, including 15 added cases for balancing, stopping,
legality, progress/failure, capacity, coarse-coordinate identity, score/RNG preservation
and unchanged non-F behavior. Format/lint and all **10** notebook source/compile
checks pass. A test helper default argument was corrected for lint; policy unchanged.

Initial subprocess totals were 38.953 s baseline / 11.286 s panels, confounded by
31.763 s in the first baseline process. Warm isolated-clone replay totals were
**10.533 / 10.319 s (0.980x)**, including startup and equal auditing. No production
speedup claim follows. All 1,000 synthetic records and 25 accessible initial public
traces replay exactly. The original baseline seed-2 trace (five games) remained
cloud-inaccessible; its aggregate summary matches replay but exact trace equality
was not verified. Independent prefix-count auditing verifies support on all 30
replay runs. The additional 3,000 actions are replay, not independent evidence.

The first replay attempt stopped before games ran: macOS evicted repository, Git
and game files into cloud placeholders and reads timed out. Disk free space was
about 365 MiB. Recovered measured policy, runner, protocol and all five game-source
hashes match the initial manifest. Reconstructed the same official harness commit
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b` in an isolated temporary clone to
complete replay and the report-only commit. No unrelated files were removed.

Archived and removed candidate source, runner and tests. Final baseline: **15 tests**,
format/lint and **10** notebook source/compile checks pass; production files match
origin/main. Original checkout's candidate edits were also removed. Patch forward
and reverse applicability checked; SHA-256:
`c3af53f2fdf3b91a11bc86ef4b8ed7d9fc08e8265889869def625694dabe4d99`.

Ignored evidence is under `experiments/results/2026-10-10-matched-panels/`: protocol,
traces, summaries, manifests, audit scripts, validation and candidate patch. A recovery
copy lives at `/private/tmp/hypothesisworld-20261010-recovery/` under the same relative
path; original baseline seed-2 evidence remains in the original cloud-backed folder.
Raw evidence is not pushed. Apply the patch to the base, copy the protocol into a new
ignored output folder, and run `experiments/run_matched_panels.py --output <folder>`
with recorded dependencies, cached games and writable plotting/cache directories.
Only this report and RESEARCH_PLAN.md are retained.

Reject this acquisition-only schedule. Require useful consequences and affordable
return opportunities before another paired-comparison mechanism. Repeated no-ops
can meet a sample-count target without helping solve a game.
