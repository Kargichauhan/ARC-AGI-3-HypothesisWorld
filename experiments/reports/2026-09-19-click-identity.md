# Exact click identity pilot — 2026-09-19

Decision: **reject the implementation; retain this research record**. Separating
local coordinate interventions from pooled semantic evidence did not improve public
completion and made the synthetic discovery task slower. Candidate implementation,
runner, and tests were archived locally and removed before the final commit.

## Hypothesis and preregistered gates

Distinct clicks with the same target colour and coarse screen region currently
share one `ActionKey`. Hypothesis: preserving exact coordinates in local action
memory prevents false transition reuse and redundant probes, improving discovery
and completion while preserving pooled evidence for transfer.

Before implementation, the ignored `protocol.md` required all of:

1. On 100 synthetic seeds with nine same-colour/same-region candidate positions and
   an 18-action budget, reduce mean capped goal-discovery actions by at least 20%
   and solve at least 95/100 trials.
2. On five cached public games, seeds 0/1/2, full agent F and 100 actions per game,
   complete at least one additional level with no per-game summed regression.
3. Total public subprocess wall time no greater than twice baseline.
4. Passing unit tests, formatting, lint, and notebook source/compilation checks.

No post-result tuning or changed thresholds. A–E were conditional on F passing;
that gate failed, so they were not run.

## Method

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65` (`origin/main`). Inspected the
clean checkout, fetched origin, queried open PRs (none), reviewed all remote research
branches, main history, the research plan, and September 15, 17, and 18 reports.
No unmerged representation or prediction mechanism was incorporated.

The candidate added optional coordinates to `ActionKey` and used them for local
novelty, exact world-model transitions, and planner edges. Global novelty counts,
action-outcome fallback, and hypothesis learning still used the original action
ID/colour/region key. Candidate positions, selector weights, and keyboard actions
were unchanged. Six tests checked distinct candidate identities, local novelty,
separate exact outcomes and planning, pooled cross-state predictions, shared
hypotheses, and non-coordinate compatibility.

Synthetic trials used nine background coordinates in one coarse region on a 12×12
grid, with a uniformly sampled rewarding position per seed. A successful click
caused both visible grid change and progress; other clicks were no-ops. This avoids
the progress-only scene-change contract mismatch identified on September 18. Both
arms used the full selector and identical seed/tie-breaking rules. Unsolved trials
were assigned the 18-action cap. This is a deliberately narrow aliasing fixture.

Public trials used the installed official engine in OFFLINE mode and the existing
framework lifecycle. Seed injection was confined to the runner and identical in
both arms. Arm order alternated by seed. The baseline stripped exact coordinates
before learning and selection, reproducing main's coarse-key behavior. Two shadow
models forecast before learning from the same actual transition; both arms paid
this auditing overhead. Repeated clicks mean the same exact coordinate action at
the same raw state fingerprint earlier in that run, including across resets.

## Results

| Synthetic metric | Baseline | Exact identity |
|---|---:|---:|
| Solved trials | 92/100 | 100/100 |
| Mean capped discovery actions | 7.60 | 10.27 |

Despite solving eight more trials, mean actions **increased 35.13%**. The required
20% reduction failed.

All public runs consumed 100 actions: **30 runs, 3,000 actions** total. Seed results
are listed in order 0/1/2; repeat counts are summed across seeds.

| Public game/version | Baseline levels | Candidate levels | Baseline repeat clicks | Candidate repeat clicks |
|---|---|---|---:|---:|
| `ls20-9607627b` | 0 / 0 / 0 | 0 / 0 / 0 | 0 | 0 |
| `vc33-5430563c` | 1 / 0 / 1 | 1 / 0 / 1 | 98 | 114 |
| `ft09-0d8bbf25` | 0 / 0 / 0 | 0 / 0 / 0 | 291 | 291 |
| `cn04-2fe56bfb` | 0 / 0 / 0 | 0 / 0 / 0 | 21 | 34 |
| `su15-1944f8ab` | 0 / 0 / 0 | 0 / 0 / 0 | 111 | 224 |

Total levels remained **2 → 2**, failing the improvement gate. Exact repeated clicks
increased **521 → 663**; both arms made 989 coordinate actions. Total audited wall
time was **33.216 s → 29.322 s (0.883×)**. Timing includes startup and shadow
instrumentation and is not a stable production latency claim.

Diagnostic shadow forecasts on 1,488 baseline-policy transitions had mean loss
**0.0357015 → 0.0351309** (1.60% reduction). Loss averages scene-change Brier error,
failure Brier error, and squared nonnegative progress-count error. In 68 transitions,
the coarse model had an exact-state prediction although that particular coordinate
had no local observation. This measures unsupported local reuse, not proof that
its predicted outcome was wrong. Better identity did not produce better control.

## Explanation and decision

A diagnostic replay of synthetic seed 0 exposes an interaction with the planner.
After one no-op click, its exact self-transition receives a planning value of
**0.6175**; unseen sibling clicks receive zero. The sibling's novelty advantage
contributes only **0.1625** after weighting, and both have the same hypothesis
information term. The tested no-op therefore wins again. The coarse baseline gives
all siblings the same planning value, leaving tie-breaking to explore them. This
calculation explains the early repeat sequence, not every public-game outcome.

Reject exact click identity as a standalone change. The next bounded investigation
should preregister a planner rule for unproductive self-transitions, then evaluate
its interaction with intervention identity. Do not retain this feature based solely
on cleaner semantics, increased synthetic solve rate, or shadow calibration.

These are cached public-game pilot results, not held-out benchmark results or an
official Relative Human Action Efficiency claim. Only three agent seeds and short
budgets were tested; nothing was submitted to the competition gateway.

Candidate validation: **21 tests passed**, formatting/lint passed, notebook generated,
and all **10** embedded Python modules matched source and compiled. A runner lint
fix bound per-game audit closures explicitly; replaying both seed-0 arms reproduced
all recorded game decisions and forecasts exactly. Final restored production code:
**15 tests passed**, formatting/lint and the same packaging checks passed.

## Local evidence and reproduction

Raw evidence is gitignored under `experiments/results/2026-09-19-click-identity/`:
preregistered protocol, all synthetic selections, six public logs and JSON traces,
public and shadow summaries, planner diagnostic, source/game/dependency manifest,
validation logs, deterministic replay records, and `candidate.patch` including the
removed implementation, tests, and runner. The archive is not shipped on the branch.

Candidate patch SHA-256:
`4c0b0d3bb878b147dcf0066ab16650de32dd6be0696fc9af87ecdeb33207e8b3`.

For local reproduction, apply the archived patch to the base revision and run
`.venv/bin/python experiments/run_click_identity.py --output
experiments/results/click-identity-reproduction`. Cached game versions and dependencies
are recorded in the manifest. The report and research-plan update are the only
tracked changes retained.
