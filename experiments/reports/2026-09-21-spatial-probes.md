# Spatially balanced coordinate probes — 2026-09-21

Decision: **reject the candidate; retain the research record**. Spatial coverage
improved on the designed synthetic task, but public completion regressed from two
levels to zero. Candidate implementation, six tests, and runner were archived
locally and removed; production code matches the base revision.

## Hypothesis and protocol

Initial observation: `ft09` exposes 64 detected non-background components, but
raster-order truncation places all 24 baseline coordinate proposals at y=4..14.
Hypothesis: spatially balanced sampling within existing priority tiers prevents
local clutter from excluding actionable regions, improving target coverage and
public completion. This tests proposal coverage separately from earlier action
identity and planner-novelty experiments; neither mechanism was incorporated.

The protocol was saved before implementation or outcome measurement. All gates
were required, with no post-result parameter or threshold changes:

1. At least 1.5× target-centroid coverage on 400 crowded synthetic layouts; no
   decrease greater than five percentage points on a balanced-layout control.
2. At least one additional completed public level, with no per-game sum decrease,
   on five cached games, full agent F, seeds 0/1/2, and 100 actions per game.
3. Total audited public subprocess time at most twice baseline.
4. Passing unit tests, formatting/lint, notebook generation, source equality,
   and embedded Python compilation.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65` (`origin/main`). The checkout
was clean. Fetched origin, inspected remote research/daily branches, main's plan,
git history and September 15/17/18/19/20 reports; GitHub returned no open PRs.
No game implementation source was read to design the mechanism.

## Implementation and method

Only `agent/exploration.py` changed in production. Deduplicate coordinates into
their best priority tier. Choose the first point nearest the frame center, then
maximize minimum squared distance to previously selected points, always exhausting
higher-priority candidates first. Break ties by y then x; retain the 24-point cap.
The underlying proposal pool, action identities, selector weights, hypotheses,
world model and planner remain the baseline implementation. Selection order changes,
so seeded random tie-breaking can also assign different draws to coordinates.

Synthetic frames are 64×64 with 48 isolated 2×2 objects of random colors 1..9
on zero background. Candidate object locations use separated five-pixel grids.
Crowded layouts have 20 objects in each upper quadrant and four in each lower
quadrant; controls have 12 per quadrant. Each target is sampled uniformly by
quadrant, then by object within that quadrant. Seeds are 20260921..20261320.
Coverage means the target centroid is present in the 24 proposals. This measures
proposal inclusion, not sequential discovery, completion, or an unbiased ARC task
sample; its spatial target prior deliberately tests the proposed mechanism.

Public evaluation used the installed official engine in OFFLINE mode and the
existing framework lifecycle. Identical seed injection and transition/selection
auditing were applied to both arms, alternating arm order by seed. The baseline
proposal function was loaded from the fixed base revision. Every baseline action,
coordinate, score, transition and final level exactly reproduced September 20's
15 recorded trajectories. Versions: arc-agi 0.9.9 and arcengine 0.9.3.

A separate secondary diagnostic reset each click-capable game before each of its
24 initial proposals per arm: **192 one-click trials**, with equality of the
initial fingerprint asserted after every reset. Visible response is an altered
final frame, not proof of useful progress or unchanged hidden state.

## Results

| Synthetic target coverage | Baseline | Spatial probes |
|---|---:|---:|
| Crowded, 400 layouts | 141 (35.25%) | 253 (63.25%) |
| Balanced control, 400 layouts | 175 (43.75%) | 195 (48.75%) |

Crowded coverage increased **1.794×**, and the control improved five percentage
points. Both synthetic gates passed.

Public evaluation: **30 runs, 3,000 actions**. Level columns list seeds 0/1/2;
repeat and no-op counts sum all three seeds. Repeats use the same raw fingerprint,
action key and exact coordinates; no-ops are same-fingerprint transitions without
positive progress, which cannot exclude hidden-state changes.

| Game/version | Baseline levels | Spatial levels | Repeats, base → spatial | No-ops, base → spatial |
|---|---|---|---:|---:|
| `ls20-9607627b` | 0 / 0 / 0 | 0 / 0 / 0 | 58 → 58 | 67 → 67 |
| `vc33-5430563c` | 1 / 0 / 1 | 0 / 0 / 0 | 98 → 94 | 0 → 0 |
| `ft09-0d8bbf25` | 0 / 0 / 0 | 0 / 0 / 0 | 291 → 292 | 300 → 300 |
| `cn04-2fe56bfb` | 0 / 0 / 0 | 0 / 0 / 0 | 129 → 66 | 128 → 58 |
| `su15-1944f8ab` | 0 / 0 / 0 | 0 / 0 / 0 | 111 → 63 | 100 → 70 |

Completion fell **2 → 0**, failing both the gain and per-game non-regression gates.
Repeats fell **687 → 573** and no-ops **595 → 495**; these secondary metrics do not
justify retention. Audited subprocess wall time was **9.297 s → 9.758 s (1.050×)**,
passing the runtime gate. Short startup-inclusive timings are not stable latency
estimates. A–E were conditional on F passing and were not run after rejection.

| Initial reset-and-click diagnostic | Baseline responses / 24 | Spatial responses / 24 |
|---|---:|---:|
| `vc33` | 24 | 24 |
| `ft09` | 0 | 1 |
| `cn04` | 17 | 17 |
| `su15` | 22 | 22 |

None of these one-click trials completed a level. Spatial proposals expand `ft09`'s
initial y extent to 4..63. Its effective probe, `(38, 54)`, was never chosen by the
full agent in any seed. Each seed instead selected only two or three distinct
coordinates, all at y≤20, despite 100 actions and access to the effective proposal.
This establishes a gap between proposal availability and actual selection; it does
not identify a sufficient fix or explain every completion regression.

Candidate: **21 tests passed**, formatting/lint passed, and all **10** notebook
modules matched source and compiled. Six added tests covered max-min geometry,
priority preservation, global distance updates, duplicate/clipped coordinates,
clutter coverage, and empty/uniform observations. After removal: **15 baseline
tests passed**, with the same formatting/lint and 10-module packaging validation.

## Interpretation and follow-up

Reject this standalone proposal rule. The audit supports the existence of a
raster cutoff, but removing that cutoff did not improve the acting policy. Before
adding more proposal geometry, measure whether untested candidate actions receive
adequate selection probability after repeated observed no-ops. A future retry
should isolate proposal coverage and selection behavior in a preregistered
factorial comparison; it must also account for changed random tie assignment.
No game-specific coordinate or color should be encoded from this diagnostic.

These are short cached public-game pilot results, not held-out benchmark results
or official Relative Human Action Efficiency measurements. No competition
submission was made. Three policy seeds do not establish general inferiority of
spatial sampling, but the stated evidence does not justify retaining this change.

## Local evidence and reproduction

Ignored evidence: `experiments/results/2026-09-21-spatial-probes/`, including the
preregistered protocol, synthetic target/proposal records, initial-effect trials,
six public logs/traces, summary, audit, source/game/dependency manifest, candidate
and final validation logs, packaging verifier, and removed `candidate.patch`.
Raw evidence is local and is not included in the pushed branch.

Patch SHA-256:
`8796dca36a49ac00d3c59a57941ff252eb7193e8d1832cecd98215235c919137`.

To reproduce locally, apply the patch to the base revision, copy the protocol into
a fresh ignored directory, and run `.venv/bin/python experiments/run_spatial_probes.py
--output experiments/results/spatial-probes-reproduction`. Use the recorded cached
game versions and dependencies. The cross-day audit additionally needs September
20's baseline traces. Only this report and the plan update are retained.
