# Boundary-consensus background inference — 2026-10-23

Decision: **reject the implementation; merge the research record**. Edge consensus
recovers large synthetic foreground objects but mistakes decorative frames for
background. It changes no public-game interpretation, proposal or completed level.
Candidate source, tests and runner were archived locally and removed before commit.

## Hypothesis and fixed criteria

Hypothesis: agreement across independent frame edges identifies background when a
large foreground object dominates pixel counts, improving perception and completion
without confusing foreground borders with background. This tests segmentation,
not the earlier object-matching optimizer or stable-state identity abstraction.

All gates fixed before implementation and measurement:

- 200 large-object scenes: candidate background accuracy at least 95%, foreground
  support intersection-over-union (IoU) at least .95 and mean IoU gain at least .25.
- Sparse-object, decorative-frame and edge-touching controls, 200 seeds each:
  baseline accuracy at least 95%; candidate accuracy/IoU loss at most .05 each.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra total
  level, no per-game summed regression, warm subprocess runtime at most 2x baseline.
- Passing unit tests, formatting/lint, notebook source/compilation checks, independent
  pixel/trace audit and deterministic replay. A–E extension conditional on all gates.

No policy, fixture or threshold was tuned after results. No game source informed design.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Reviewed memory, clean original
checkout, fresh remote main/daily/research branches, plans, experiment reports and
history. Connected GitHub search found no open PRs. An isolated clone avoided slow
cloud-backed Git reads; no unrelated changes or unmerged mechanisms were included.

Only `agent/perception.py:infer_background` changed. On frames at least 3x3, accept
a colour with a strict majority on at least three of four edges and a strict majority
of unique perimeter cells. Otherwise retain the existing area-mode rule and its
border/colour tie breaks. Extraction, matching, hypotheses and selection remain as
before. A changed background would also affect the existing state fingerprint.
The same colour can dominate multiple edges; these are geometric checks, not
statistically independent evidence about semantic role.

## Synthetic evidence

800 scenes: 200 paired seeds per family, RNG `20261023 + seed`, dimensions sampled
independently from 28–40 and three distinct colours sampled from 0–9. Large rectangles
are inset two pixels. Controls contain a 3x3 object: interior, interior plus a
one-pixel decorative border, or touching one randomly chosen edge. The renderer
supplies semantic background and exact foreground support, including the decorative
frame. These labels encode the task definition; colour alone cannot establish role.

| Family | Background accuracy, baseline → candidate | Mean foreground IoU |
|---|---:|---:|
| Large interior object | 0% → 100% | 0 → 1 |
| Sparse interior object | 100% → 100% | 1 → 1 |
| Decorative frame | 100% → 0% | 1 → 0.007857 |
| One-edge-touching object | 100% → 100% | 1 → 1 |

Primary recovery passes, but the decorative-frame control fails decisively. The
candidate discards the frame and treats the interior background as foreground.
The randomized scenes share four designed geometries; they are not 800 independent
ARC tasks, and no full-agent discovery advantage follows from segmentation accuracy.

## Public evidence

Official cached OFFLINE engine: `arc-agi==0.9.9`, `arcengine==0.9.3`; harness revision
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. All ten cached game/metadata hashes and
30 harness Python hashes match October 22. The initial launch stopped before gameplay
because yesterday's temporary cache was incomplete. Restored the original cache;
eight unused harness main/test files were restored from the pinned official clone
after the first successful cohort launched. Failure logs and provenance are retained.

Primary cohort: **30 runs / 3,000 actions**, alternating arm order by seed.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion **2 → 2** fails retention. Across 1,488 decisions per arm, same-frame
shadow comparisons show **zero changed backgrounds, object sets or proposals**.
All paired actions, scores, observations and transitions are identical; each arm
has 595 same-frame/nonpositive-progress transitions and 746 consecutive exact repeats.
The mechanism never changes a decision in this cohort. Public frames have no semantic
background annotations, so agreement is not evidence that either parser is correct.

Warm replay totals: **36.726 / 35.640 seconds** (candidate/baseline **0.970x**).
Initial totals were 41.796 / 42.308 seconds.
Timings include identical shadow parsing, trace serialization and subprocess startup;
they are not isolated inference speed measurements. No held-out evaluation, official
RHAE result or competition submission. A–E sweep was unnecessary after failed gates.

## Verification and disposition

Candidate: **29 tests passed**, including 14 new cases; formatting/lint and **ten
notebook embedded-source equality/compilation checks** pass. The independent audit
recomputes edge votes, area/perimeter counts, connected-component supports, synthetic
IoU, fingerprints, raw changed pixels, legal proposals and score ordering. It covers
all 800 scenes, 2,976 public decisions and 2,976 observations. All 15 baseline runs exactly
match October 22 on scores, actions, observations and transitions.

All 800 synthetic records and 30 public runs replay exactly. The extra 3,000
replay actions are repeated evidence, not additional independent trials.

Archived the patch, changed source, tests and runner under the ignored
`experiments/results/2026-10-23-boundary-background/` path, hash-mirrored into the
original workspace. Raw evidence is local and not pushed. Patch SHA-256:
`c10bd7e6a471d67c2da4a17f651f08ad44590e720498177e8b4f32e95eba328d`.
Forward/reverse patch checks pass. After candidate removal, production matches main;
**15 tests**, format/lint and ten notebook checks pass. Only this report and the
research-plan note are committed.

To reproduce: apply the archived patch to the base, restore its frozen baseline
and protocol at the evidence path, install recorded dependencies and cached engine,
and run `python experiments/run_boundary_background.py --output <ignored-path>` with
writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. The audit and packaging
verifier are also archived.

Recommend merging the negative record and rejecting unconditional edge consensus.
Future background inference needs evidence that distinguishes semantic background
from a foreground frame, and public decision-relevant ambiguities. Do not replace
area dominance with another fixed geometric prior based on large-object recovery alone.
