# Palette-invariant effect transfer — 2026-10-29

Decision: **reject the mechanism; merge the negative research record**. Agreement
under two palettes does not establish colour irrelevance. The candidate solves a
constructed recolouring test but fails its colour-semantic control and changes no
public decision or completed level. Candidate source, tests and runner were removed.

## Hypothesis and fixed gates

Hypothesis: action effects that agree across two distinct palettes transfer to a
bijective recolouring of the same geometry, improving predictions and completion.
This differs from prior shape/contact transfer, which retained exact colour identity.

Before implementation and measurement, the ignored protocol required all of:

- 200 recolouring fixtures: at least 25% lower three-channel prediction squared
  error; full-selector choice accuracy at least 90%, with at least 20 percentage
  points of improvement.
- Colour-semantic and IID controls, 200 seeds each: mean squared-error increase
  at most .02 in each family.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra total
  level, no per-game summed regression, warm runtime at most twice baseline.
- Passing unit tests, formatting/lint, notebook source equality/compilation,
  independent forecast audit and exact replay. A–E expansion conditional on success.

No threshold, fixture or policy parameter was retuned after measurement.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean original
checkout, automation memory, freshly cloned remote main/daily/research branches,
plans, recent reports and history. Connected GitHub search returned no open PRs.
Latest remote daily work was October 24; memory also documented the unpublished
October 26 experiment. Used an isolated checkout because original Git reads stalled.
No game implementation informed the design; no unmerged mechanism was included.

Only production file `agent/world_model.py` changed. Canonicalize full grids using
first-occurrence colour labels while preserving dimensions and every pixel relation.
For unseen local ACTION1–5 pairs, transfer effects only if a 512-transition FIFO
contains two distinct source fingerprints for the same canonical grid/action and
all corresponding progress/failure/change vectors agree. Any counterexample disables
transfer. A 128-entry cache stores canonical grids. Exact local evidence overrides
transfer; other actions, confidence, targets, graph edges and decision policy remain
unchanged. No transferred destination or planner edge is invented.

During verification, dimensions were added to the canonical-cache lookup key, fixing
an implementation inconsistency with the prespecified dimension-preserving rule.
The initial run and complete corrected rerun have identical synthetic and public
records. The archived final implementation and replay manifest are authoritative.
Lint-only import/default-argument fixes also preceded final validation.

## Synthetic evidence

600 paired fixtures, RNG `20261029 + seed`. Each 16x16 frame contains one horizontal
or vertical two-cell object. Location and the two keyboard action labels vary by
seed. Two foreground colours supply training; six disjoint colours supply evaluation.
One action gives progress and translates the object one pixel; the other is a no-op.
Actual perception computes differences from rendered grids. Both arms share training,
held-out outcomes, full-selector components and random seeds. There are 24 held-out
action forecasts and 12 decisions per fixture, without held-out model updates.

| Family | Baseline error | Candidate error | Choice accuracy, baseline → candidate |
|---|---:|---:|---:|
| Palette-invariant rule | .166667 | 0 | 50% → 100% |
| Colour-semantic reversal | .166667 | .666667 | 50% → 0% |
| IID progress | .172091 | .172091 | Not a meaningful choice metric |

The primary error reduction is 100%, but control error increases by .5, failing
the .02 gate. In that deliberately adversarial control, the two training colours
agree while the held-out colours reverse the rewarding action. These observations
cannot distinguish a palette-invariant rule from a colour-dependent one. The IID
control uses eight observations per training source/action and fresh random binary
outcomes; no transferred forecast changes there.

These are constructed distribution tests, not independent ARC tasks or evidence
of general discovery. Colour-semantic reversal intentionally imposes distribution
shift; it measures failure of the proposed license for transfer, not its prevalence.
No confidence interval across these palette permutations establishes ARC generality.

## Public evidence

Official cached OFFLINE engine: `arc-agi==0.9.9`, `arcengine==0.9.3`. All ten cached
game/metadata and 30 harness Python hashes match the preserved October 26 manifest.
Primary cohort: 30 runs / 3,000 actions. Arm order alternates by seed.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 2** fails retention. All 15 paired decisions and observations are
identical. Each arm has 1,488 decisions/observations, 595 no-ops and 746 consecutive
exact repeated choices. There are zero changed forecasts among 31,491 shadow queries
per arm. Thus these games provide no demonstrated decision benefit from the mechanism.

Warm totals: **19.611 / 19.468 seconds** (.993x), including equal shadow tracing,
serialization and process startup. Initial totals 32.003 / 19.863 seconds were
startup-confounded. Timing is not an isolated speed claim. The corrected complete
rerun reproduces all 600 synthetic records and 30 public runs exactly; its additional
3,000 actions are repeated evidence. No held-out evaluation, official RHAE result
or competition submission was performed.

## Verification and disposition

Candidate: **25 tests passed**, including ten new tests. Final restored baseline:
**15 tests passed**. Both pass formatting/lint and generation plus source-equality/
compilation checks for all ten packaged notebook modules. Forward/reverse archived
patch checks pass. Production matches main; only this report and a plan note remain.

Raw protocol, complete training/forecast and public traces, dependency/source hashes,
independent row-based forecast audit, replay, validation logs and removed candidate
are preserved under ignored `experiments/results/2026-10-29-palette-transfer/` and
mirrored into the original workspace. The audit reconstructs base forecasts and
candidate eligibility/effects from raw prefix rows, checks raw pixel differences,
legal choices and recorded scores, and verifies exact replay equality.

Candidate patch SHA-256:
`1b65f352d7a183e197abd8600ea48a80e37ba5760c999cee6b494c97e716b622`.
To reproduce, apply that patch to the base, restore the recorded evidence helpers and
cached engine, and run `python experiments/run_palette_transfer.py --output <ignored-path>`.
Use writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. The archived `audit.py`
and `verify_packaging.py` check forecasts and notebook contents.

Recommend merging the research record and rejecting this transfer rule. Future work
must establish when colour is irrelevant through discriminating observations; two
agreeing palettes and geometric equality alone are insufficient.
