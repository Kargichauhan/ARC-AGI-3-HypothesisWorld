# Conditional motion mass — 2026-11-19

Decision: **do not retain candidate; retain this synthetic research record**. Public
completion gate remains untested because cached game/framework reads stalled.
This is an inconclusive efficacy result, not a demonstrated completion regression.

## Hypothesis and protocol

Preserving explicit-motion group mass while recalibrating conditional directions
should avoid promoting wildcard rules and improve completion. This isolates a
normalization confound in November 18's rejected stationary/single-switch mixture;
it is not November 2's already rejected compatibility-disagreement replacement.
The original entropy, belief updates, planner and action proposals remain unchanged.

Inspected automation memory, fetched remote main/daily/research refs, main history
and plan, November 2/17 reports and November 18's local unpublished report/evidence.
Connected GitHub open-PR search returned none. Main remains
`24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Original checkout eventually reported
clean; work was isolated in a temporary clone and original tracked files untouched.
November 18's unpublished branch is only a local reference, not a fetched remote.

Protocol saved before implementation: 200 paired seeds/family, 64 observations,
reversal stale-mass reduction >=50%; each stationary/Bernoulli(.1/.5/.9) Brier
increase <=.01. Conditional public gate: five cached games, F, seeds 0/1/2,
100 actions, >=1 extra level, no per-game summed regression, runtime <=2x.
All gates and validation required for retention. No tuning after measurement.

## Implementation

Reuse the previous fixed 64-observation, 512-key stationary/single-switch Dirichlet
model. Multiply explicit-motion hypothesis weights by conditional probabilities,
then rescale those weights to their original total before global normalization.
Thus every wildcard weight and total explicit-motion mass are preserved. Within-group
odds still change; this does not guarantee invariant entropy or action rankings.
Five new tests cover exact mixture arithmetic, symmetry, reversal, storage/isolation,
and the new group-mass and wildcard invariants.

## Evidence

128,000 prequential records, five families, 200 paired seeds, 64 steps, two arms.
Intentionally reuse fixture RNG 20261118 + seed to isolate normalization from stream
changes. Outcomes are supplied, not online game solves. Reversal: 16 right then
48 left observations; score steps 56–63. Controls score steps 32–63.

| Metric | Baseline | Candidate |
|---|---:|---:|
| Reversal stale positive conditional mass | .500000 | .022568 |
| Stationary Brier | .000000 | .000000 |
| Bernoulli(.1) Brier | .249201 | .097694 |
| Bernoulli(.5) Brier | .250000 | .257737 |
| Bernoulli(.9) Brier | .248081 | .094732 |

Synthetic gates pass: 95.49% stale reduction, largest control increase .007737.
Independent trace checks verify all paired inputs, forecasts, losses, summaries,
normalization, group mass and wildcard weights. Conditional forecasts match the
November 18 estimator to 1e-12, as expected algebraically. This is a normalization
ablation, not independent confirmation of that estimator's calibration. Synthetic
raw replay is byte-identical. No speed improvement is claimed.

Public evaluation could not start: cached game/framework file reads in the original
workspace stalled, including a targeted copy after stopping a recursive copy.
No complete public cohort, held-out benchmark or official RHAE result exists for this
candidate. Remote benchmark access was not tested. Therefore the completion retention
gate is unestablished and the candidate is removed rather than promoted.

## Verification and disposition

Candidate: 20 tests pass, format/lint pass, ten packaged notebook modules match source
and compile. Final restored baseline: 15 tests, format/lint and ten notebook module
checks pass. Only this report and the research-plan note are committed. Archived
candidate source, five tests, both runners and patch remain under ignored
`experiments/results/2026-11-19-motion-mass/`, together with protocol, raw/replay,
audit, dependency list and validation logs. Raw artifacts are local, not pushed.
Patch SHA256: `b3e44a2a97111d912da167d1953dd8aeee4c4d29ba80a92fbf4fe8a1b0f8b633`.

Reproduce from the recorded main: apply candidate.patch, restore baseline.py at the
ignored evidence path, and run `PYTHONPATH=. python experiments/run_motion_mass.py`.
The public runner requires the official cached games/framework and recorded packages.
Recommend retaining the research record only; defer any production adoption until
this exact frozen candidate meets its public completion gate. Do not retune its
window or mixture priors on these same synthetic controls.
