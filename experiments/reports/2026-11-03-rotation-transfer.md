# Rotation-equivariant effect transfer — 2026-11-03

Decision: **reject the mechanism; merge this negative research record**. Agreement
at two orientations does not establish rotation invariance. The candidate passes
the designed equivariant diagnostic, damages both orientation-sensitive controls,
and never activates publicly. Candidate code/tests/runner were archived and removed.

## Hypothesis and fixed gates

Hypothesis: corroborated rotated scene/action pairs license effect transfer to
unseen orientations, improving full-agent decisions and public completion without
harming orientation-sensitive rules. Unlike October 29's palette transfer, this
transforms scene geometry and action identity together while retaining colours.

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Reviewed automation memory,
freshly cloned main/daily/research branches, plans, recent reports and history.
Connected GitHub search found no open PRs. Original checkout was clean after slow
cloud reads; tracked files were left untouched. No unmerged mechanism, game-source
design knowledge, subagents, parameter retuning or competition submission.

Protocol saved before implementation/measurement; every retention gate required:

- Equivariant synthetic family: 200 seeds, two held-out orientations per seed;
  at least 25% lower three-channel squared prediction loss, at least 95% correct
  full-F choices, and at least 20 percentage points of improvement.
- Fixed-direction and two-angle-agreement controls: baseline at least 95% correct;
  candidate loses at most five percentage points and adds at most .02 mean loss.
- Five cached public games, F, seeds 0/1/2, 100 submitted actions: at least one
  additional total level, no per-game summed regression, warm runtime at most 2x.
- Tests, format/lint, notebook source equality/compilation, independent trace audit
  and exact replay pass. A–E expansion conditional on F success.

## Mechanism

Only `agent/world_model.py` changes production behavior. Canonicalize the complete
pixel grid and bare ACTION1–4 under four clockwise rotations, using the assumed
action cycle `1,4,2,3`. This geometric interpretation is an experimental assumption,
**not a universal game contract**. Rectangular grids rotate normally; dimensions
and colours are preserved. A 128-entry cache stores canonicalizations.

Keep a FIFO of 512 eligible transitions. At an unseen local state/action pair,
transfer only if the canonical orbit has at least two distinct source fingerprints,
at least two canonicalizing rotation counts, and unanimous retained effects:
positive progress magnitude, GAME_OVER, and `StateDiff.changed`. Exact local evidence
wins. Preserve fallback target/confidence, learned edges, hypotheses, proposals,
weights and random draws. Clicks, undo, reset, ACTION5 and contextual directional
keys cannot transfer. This is corroborated equivariance, not learned action semantics.

## Synthetic evidence

Each seed supplies eight training transitions: all four directional actions on two
orientations of an asymmetric 5×7 scene. Query the other two orientations without
updates. Fixture RNG `20261103 + seed`, policy RNG `seed`; colours and designated
useful action vary. Full-F defaults apply; only the empirical model receives supplied
demonstrations. Every outcome changes pixels; useful actions give progress and
alternatives GAME_OVER. These are trained decisions, not online solves or independent
ARC tasks. The hypotheses and memory are untrained, isolating model transfer.

The equivariant family rotates the useful action with the scene. Fixed-direction
keeps one useful raw action. Two-angle agreement shares equivariant training evidence,
but at held-out orientations the two demonstrated useful raw action IDs remain useful
and the other two harmful. No controls or gates changed after results.

| Family | Baseline correct / 400 | Candidate | Baseline loss | Candidate loss |
|---|---:|---:|---:|---:|
| Equivariant | 0 | 400 | .250000 | .000000 |
| Fixed direction | 400 | 98 | .000000 | .166667 |
| Two-angle agreement | 400 | 0 | .083333 | .500000 |

Primary gates pass. Both competent controls fail: accuracy loses **75.5** and **100
percentage points**. In fixed-direction, unanimous negative observations in a rotated
orbit can override the useful raw action's pooled positive evidence at a new frame.
Even partial orbit agreement can therefore cause harmful negative transfer.

## Public evidence

Official cached OFFLINE engine, `arc-agi==0.9.9`, `arcengine==0.9.3`; source/dependency
hashes recorded. Cached games/harness copied without game-source design inspection.
Alternating arm order by seed; both arms retain rotation records and perform identical
shadow tracing. Primary cohort: **30 runs / 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 2** fails retention. All 15 paired traces are identical, including
actions, outcomes and shadow forecasts. **Zero eligible transfers and zero changed
predictions across 62,982 forecasts**. Same-grid/nonpositive-progress observations:
595 per arm. Whole-frame rotational recurrence is absent under these eligibility
conditions; this does not establish that rotations never matter.

Replay subprocess time **14.767 → 15.549 seconds (1.053x)**. Initial time
25.984 → 14.278 seconds was dominated by baseline's first import. Replay includes
startup, equal tracing/shadow calculations and a briefly concurrent independent audit;
timings are not isolated production-speed evidence. Replay adds 3,000 repeated actions,
not independent trials. No held-out benchmark or official RHAE claim.

Initial dependency installation failed with ENOSPC; original cloud-backed imports
timed out. Removed only this run's incomplete disposable environment. Space later
recovered, a fresh isolated installation succeeded, and the complete public cohort
and replay ran. No cached-pilot access limitation remains; held-out access was absent.

## Verification and disposition

Candidate: **27 tests pass** (12 new cases), format/lint pass, all **10 notebook
modules** match source and compile. Tests cover rectangular rotation/action alignment,
corroboration, repeated single-source evidence, local precedence, contradictions,
unsupported actions, FIFO expiry and separate progress/failure channels.

An independent coordinate-index reference audits **1,200 synthetic records, 2,400
decisions and 9,600 forecasts**, including training/oracle construction and selector
arithmetic. A separate public audit rebuilds empirical counts and rotation eligibility
from prefixes and checks **62,982 forecasts, 3,000 actions and 2,976 observations**,
raw pixel changes, legality, coordinates and levels. All seven compressed traces
reproduce exactly by decompressed SHA-256; seven summaries match. Runner formatting
and closure bindings changed after the first synthetic run; policy did not change,
and the final runner reproduces it exactly.

Archived and removed candidate source/tests/runner. Final baseline: **15 tests pass**,
format/lint and all **10 notebook checks pass**. Production agent/tests/scripts/notebook
configuration match main. Forward/reverse patch checks pass. Only this report and
the research-plan note remain on the branch.

Reject two-orientation unanimous transfer. Future symmetry work needs evidence that
transformations preserve action semantics and useful naturally occurring query coverage,
with asymmetric controls retained. Designed equivariance does not justify another rule.

Ignored local evidence: `experiments/results/2026-11-03-rotation-transfer/` contains
protocol, source/dependency manifests, traces/replay, audits, validation, candidate
snapshot and removed patch. Raw evidence is not pushed. Patch SHA-256:
`a0edede5610e1c212203589d0b6d1429c20b2f92d9504498c6f6eb6630f74560`.
Apply the patch to the base and restore recorded dependencies/cached games/harness.
Run `python experiments/run_rotation_transfer.py --synthetic --output <ignored-path>`;
omit `--synthetic` for the public cohort. Use writable plotting/cache directories.
Audit scripts are archived alongside the evidence.
