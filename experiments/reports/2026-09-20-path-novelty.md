# Path-exclusive planner novelty pilot — 2026-09-20

Decision: **reject the implementation; retain the research record**. Paying novelty
only once per state along a simulated path reduced repetitive actions, but failed
both the synthetic improvement threshold and the public completion threshold.
Candidate code, runner, and tests were archived locally and removed.

## Hypothesis and preregistered gates

The baseline planner can reward an observed no-op for reaching its current state,
then reward the same state again through its continuation or leaf bootstrap.
Hypothesis: excluding repeated destinations from simulated exploration credit
improves goal discovery and public completion while preserving immediate progress.

The protocol was saved before implementation. All retention gates were required:

1. On 100 paired synthetic seeds with four keyboard actions and a 12-action cap,
   solve at least 95 trials and reduce mean capped discovery actions by at least 20%.
2. On five cached public games, full agent F, seeds 0/1/2 and 100 actions per game,
   complete at least one additional level with no per-game summed regression.
3. Total public subprocess wall time no greater than twice baseline.
4. Passing unit tests, formatting/lint, notebook generation, and embedded source
   equality and compilation checks.

No post-result tuning or relaxed thresholds. A–E were conditional on F passing all
gates; they were not run after the rejection criteria were met.

## Implementation and method

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65` (`origin/main`). Inspected the
clean checkout, fetched origin, queried open PRs (none), reviewed remote daily and
research branches, history, the research plan, and September 15/17/18/19 reports.
No unmerged mechanism was incorporated. September 19's rejected exact-click pilot
motivated this independent test of the planner's repetition incentive.

Only `agent/planner.py` changed in production. A rollout starts with the current
state in an immutable visited set. A fresh destination receives its state novelty
once; a repeated destination terminates novelty expansion with zero credit. Known
continuations retain the 0.55 discount and empirical edge confidence. Leaves have
no additional bootstrap, so the depth-two search pays at most two destinations.
Immediate expected progress remains rewarded even for an identical observation.
Future progress is still omitted, as in the baseline. State/action identities,
confidence thresholds, models, action candidates, and selector weights are unchanged.

The synthetic fixture has one uniformly drawn rewarding action and three no-ops.
The rewarding action visibly changes the grid and adds progress. The full selector
starts without training; target RNG seeds are `20260920 + seed`, and policy seeds
are 0–99. Both arms use the same target and tie-breaking seed. This is a narrow
discovery fixture, not a representative ARC distribution. It avoids the progress-only
change-contract mismatch identified on September 18.

Public runs used the installed official engine in OFFLINE mode and the existing
framework lifecycle. The runner supplied identical agent-seed handling and auditing
to both arms; arm order alternated by seed. The baseline planner was loaded directly
from the fixed base revision. All 15 baseline game trajectories reproduced the
September 19 baseline's raw-state/action/coordinate decisions and final levels
exactly. The candidate did not include September 19's coordinate identity changes.

## Results

| Synthetic metric | Baseline | Path-exclusive novelty |
|---|---:|---:|
| Solved trials | 100/100 | 100/100 |
| Mean discovery actions | 3.22 | 2.61 |
| Repeated actions before discovery | 79 | 0 |

Mean discovery actions decreased **18.94%**, missing the required 20%. Candidate
trials were faster on 38 seeds, tied on 62, and slower on none. Paired mean savings
were 0.61 actions; a descriptive 10,000-resample paired percentile bootstrap gave
a 95% interval of [0.44, 0.79] actions (RNG seed 20260920). This uncertainty estimate
does not replace the preregistered point-estimate gate.

Public evaluation consumed **30 runs and 3,000 actions**, exactly 100 per run. Level
results list seeds 0/1/2; repeat and self-transition counts are summed across seeds.
Repeated actions mean the same raw-state fingerprint, action key, and exact
coordinates previously selected in that run, including across resets. A no-op below
means a same-fingerprint transition without positive progress; it does not establish
that hidden game state was unchanged.

| Game/version | Baseline levels | Candidate levels | Repeat actions, base → candidate | No-ops, base → candidate |
|---|---|---|---:|---:|
| `ls20-9607627b` | 0 / 0 / 0 | 0 / 0 / 0 | 58 → 32 | 67 → 66 |
| `vc33-5430563c` | 1 / 0 / 1 | 1 / 0 / 1 | 98 → 98 | 0 → 0 |
| `ft09-0d8bbf25` | 0 / 0 / 0 | 0 / 0 / 0 | 291 → 257 | 300 → 300 |
| `cn04-2fe56bfb` | 0 / 0 / 0 | 0 / 0 / 0 | 129 → 24 | 128 → 96 |
| `su15-1944f8ab` | 0 / 0 / 0 | 0 / 0 / 0 | 111 → 20 | 100 → 17 |

Total completion remained **2 → 2**, failing the additional-level gate. Repeated
actions fell **687 → 431** (37.26%), and no-ops fell **595 → 479** (19.50%). These
secondary improvements did not produce the required task progress. Total audited
subprocess wall time was **40.273 s → 39.636 s (0.984×)**. Timing includes startup
and logging; it is not a stable production latency estimate.

Candidate validation: **23 tests passed**, formatting/lint passed, and all **10**
notebook modules matched source and compiled. Eight additional tests covered no-op
credit, progress on unchanged observations, leaf credit, long cycles, depth/discount,
independent paths sharing destinations, confidence gating, and confidence scaling.
Final restored production code: **15 tests passed**, formatting/lint and the same
10-module packaging checks passed.

## Interpretation and next step

The candidate removes a real incentive for repetitive exploration, but this pilot
does not justify retaining it. Even after suppressing loop credit, every `ft09`
transition remained an observed no-op. Reducing repeated selections alone is an
insufficient objective when the available probes fail to expose useful effects.

Before another planner feature, inspect whether proposed coordinate probes can
produce visible effects in the persistent-no-op cases. If revisiting exact action
identity, preregister a factorial comparison of identity and path novelty so their
interaction can be separated from either standalone mechanism. Do not assume their
combination succeeds from these results. Hidden-state changes, delayed effects,
short action budgets, and three public seeds limit the rejection's scope.

These are cached public-game pilot results, not held-out benchmark results or an
official Relative Human Action Efficiency claim. No competition submission was made.

## Local evidence and reproduction

Raw evidence is gitignored under `experiments/results/2026-09-20-path-novelty/`:
preregistered protocol, all synthetic rankings, six public traces and sanitized
logs, aggregated results and audit, source/game/dependency manifest, source hash
verification, candidate/final validation, and the removed `candidate.patch`.
The patch includes the planner, eight tests, and runner. The local archive is not
shipped on this branch; only this report and the research-plan update are retained.

Candidate patch SHA-256:
`e46e312745d91803cf701da83fdf6848d678290fcc7a610a73feb1e69164f038`.

For local reproduction, apply the archived patch to the base revision, copy the
protocol into a fresh ignored output directory, and run `.venv/bin/python
experiments/run_path_novelty.py --output experiments/results/path-novelty-reproduction`.
Use the recorded cached game versions and dependencies. The separate audit script
also requires the September 19 baseline traces for its cross-run reproduction check.
