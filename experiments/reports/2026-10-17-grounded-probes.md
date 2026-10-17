# Grounded object probes — 2026-10-17

Decision: **reject the implementation; merge the research record**. Grounding primary
probes on object pixels did not improve full-selector synthetic or public completion.
Candidate code, eight new test cases and runner were archived and removed. Production
matches main.

## Hypothesis and fixed gates

Hypothesis: prioritizing actual object support over empty geometric centroids improves
causal intervention targeting and completion without losing useful cavity probes.
Unlike prior spatial sampling and shape-transfer experiments, this changes where an
individual object's primary intervention lands, without changing coverage allocation,
learned action identity or outcome models.

Preregistered before implementation or measurement; all retention gates required:

- Ring/U/C/L surface tasks, 100 paired seeds each, F selector, 24-action cap:
  candidate at least 95% solves on each, pooled solve gain at least 20 percentage
  points, pooled mean capped actions at least 20% lower.
- Solid-object and ring-cavity controls, 100 paired seeds each: baseline at least
  95% solves, candidate loss at most five points and action cost at most 1.5x baseline.
  An incompetent baseline fails control assurance rather than waiving the gate.
- Five cached official public games, F seeds 0/1/2, 100 actions: at least one extra
  total level, no per-game summed loss and warm subprocess runtime at most 2x baseline.
- Unit tests, formatting/lint and notebook embedded-source equality/compilation pass.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected original checkout status,
fresh remote main, all daily/research branches, research plans, reports and git history;
GitHub reported no open PRs. Latest daily branch was October 16. Used a fresh temporary
fork clone because original cloud-backed reads were slow. No unmerged mechanisms,
game-source design inspection, subagents or post-result threshold tuning.

## Smallest mechanism

When an object's rounded centroid is outside its member cells, choose the member
nearest its true centroid by squared Euclidean distance, breaking ties by y then x.
Give that point priority zero; retain the original centroid at priority one. Supported
centroids remain unchanged. Existing corners, boundary/change/coverage proposals,
sorting, deduplication, cap, model, hypotheses, planner, scoring and RNG are unchanged.

This guarantees an object's primary proposal lies on its pixels before global sorting
and truncation. It does not guarantee that the point survives truncation, is selected,
or is interactive. Retained cavities may also be truncated. Changing list order can
reassign random tie-breaking draws to coordinates, so downstream changes cannot all
be attributed to geometric grounding alone.

## Synthetic evidence

Six designed 7x7 shapes on 32x32 pixel grids, translated by offsets sampled from
2..22 and recoloured 1..9 using `20261017 + seed`. Surface tasks accept any member
pixel; the cavity control accepts the ring's center. Nonwinning actions leave the
frame unchanged. Every arm uses production perception, proposal generation, full F
selection and online memory/model/hypothesis updates. These are translated/recoloured
instances of six structures, not 1,200 independent ARC tasks.

| Fixture | Baseline / candidate solves, out of 100 | Mean capped actions |
|---|---:|---:|
| Ring surface | 17 / 17 | 20.09 / 20.09 |
| U surface | 17 / 16 | 20.09 / 20.32 |
| C surface | 17 / 16 | 20.09 / 20.32 |
| L surface | 12 / 11 | 21.24 / 21.47 |
| Solid control | 18 / 18 | 19.86 / 19.86 |
| Cavity control | 10 / 15 | 22.03 / 20.78 |

Primary solves decline **63/400 to 60/400**, or **15.75% to 15.00%**; mean capped
actions rise **20.3775 to 20.55**, about **0.85%**. Every primary solve is on the first
action. None of the initial misses recovers within the remaining budget. Consecutive
identical selections total 4,334 / 4,339 across primary trajectories.

All synthetic improvement gates fail. Both baseline controls are far below the
preregistered 95% competence requirement; the apparent absence of control harm does
not establish safety. No fixtures or thresholds were changed after measurement.

The proposal priority is used for inclusion and ordering, not as a selector feature.
Initial selection still scores and randomly tie-breaks the entire candidate set;
a supported first proposal therefore does not imply a supported first selection.
The subsequent failures are consistent with the earlier documented no-op planning
problem, but this pilot does not isolate or repair that mechanism.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9 / arcengine 0.9.3; framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Alternating arm order by seed.
Primary cohort: **30 runs / 3,000 actions**. Entries are seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Completion remains **2 to 2**, failing retention. Shadow comparison finds different
proposal lists at **591 decisions per arm**, all in cn04/su15. Ten paired runs have
identical selected-action sequences; five differ, with no additional levels. Across
observations there are 3,682 empty object centroids per arm, including repeated
objects; this is not a count of independent targeting errors or selected bad clicks.

Same-fingerprint/nonpositive-progress transitions rise **595 to 599**; consecutive
identical exact action-coordinate selections rise **746 to 809** (source identity
ignored). Availability improvements alone do not satisfy the research objective.

Initial subprocess totals **31.945 / 16.472 seconds** are startup-confounded (first
baseline worker 21.242 seconds). Warm replay totals **14.792 / 14.707 seconds**,
**0.994x**, pass the runtime ceiling. Equal shadow proposal generation and tracing are
included; no isolated speed claim. No held-out benchmark access, official RHAE claim
or competition submission.

## Validation and disposition

Candidate: **23 tests passed**, including eight new cases covering hollow/concave
support, deterministic ties, supported centroids, actual target colour, deduplication,
change proposals and caps. Formatting/lint passed; **10 notebook modules** matched
source and compiled. Runner import/format/closure-binding lint issues were fixed
before measurement; policy and gates were unchanged.

Independent audit checks all **24,624 synthetic steps**, support/target/solve claims,
and **2,976 public non-reset decisions** for legality, fingerprint and proposal
consistency. All 15 baseline transitions, selected scores and candidate sets exactly
match October 16. Replay reproduces all 1,200 synthetic records and all 30 public
runs exactly; its additional 3,000 public actions are repeated evidence, not new trials.

Archived patch/source/tests/runner, then removed the candidate. Final baseline passes
**15 tests**, formatting/lint and **10 notebook source/compile checks**. Patch forward
and reverse applicability passed; production agent/tests/scripts match main.

Reject standalone grounding. A future intervention-grounding experiment should test
whether the selector can use grounded proposals, with competent online controls and
a preregistered factorial separating geometry, selection and random tie assignment.
Do not accumulate this change based on geometric validity alone.

Ignored evidence: `experiments/results/2026-10-17-grounded-probes/` contains protocol,
compressed trajectories, replay, audits, source/dependency/harness manifests,
validation, frozen baseline and candidate patch. Raw evidence is preserved locally,
not pushed. Patch SHA-256:
`eff4e0d8b12a6f99cb893fb14c554d88e65e4a2a0c01efe4f35f483b589459fd`.
Reproduce by applying the patch to the base, restoring the frozen baseline/protocol
at the recorded ignored path, recorded dependencies and cached games, then running
`python experiments/run_grounded_probes.py --output <ignored-output-path>` with writable
MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. Only report and research-plan note remain.
