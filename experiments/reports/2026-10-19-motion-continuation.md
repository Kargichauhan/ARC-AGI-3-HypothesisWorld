# Motion-grounded continuation — 2026-10-19

Decision: **reject the implementation; merge the research record**. Consistent
translations support continuation on a demonstrated corridor, but the rule never
activates in the public cohort and continues into a synthetic failure. Candidate
code, tests and runner were archived and removed. Production matches main.

## Hypothesis and fixed criteria

Hypothesis: two consecutive coherent object translations under the same action
provide useful evidence for a short continuation option, improving efficiency and
completion. Unlike September 27's no-op persistence and October 14's blind sequence
coverage, the rule requires visible motion. No rejected mechanism was combined.

The protocol was written before implementation or measurement. All gates required:

- Demonstrated corridor, 100 paired seeds, 24-action cap: at least 95 candidate
  solves and 20% lower mean capped actions. Two initial correct movements are
  forced demonstrations, charged to the action budget in both arms.
- Immediate discovery and known-turn controls: baseline at least 95 solves each;
  candidate solve loss at most five percentage points and cost at most 1.25x.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra total
  level, no per-game summed regression, warm subprocess time at most 2x.
- Passing tests, formatting/lint, notebook generation/source equality/compilation,
  independent trajectory audit and deterministic replay.

Unseeded corridor, unknown turn and harmful motion were preregistered diagnostics.
No policy, threshold or fixture was retuned after results. A–E public runs were
conditional on passing all F gates and were not run.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected the clean original
checkout, fresh remote main/daily/research branches, research plans, report
introductions and recent full reports, history and open PRs (none). Used an isolated
temporary clone because original cloud-backed reads were slow. No game implementation
was inspected to design the experiment.

F-only adapter controller; ordinary ranking and RNG draws still occur. A qualifying
observation has exactly one nonzero object translation of unchanged shape/colour,
no appearance/disappearance/transformation/new contact, zero progress and NOT_FINISHED.
Frame dimensions/background must match; all changed pixels must belong to the object's
old or new cells. RESET and undo are excluded.

Two consecutive observations must agree on exact action, colour, shape and movement
vector, with continuous source/destination and matched object identity. Repeat the
same proposed action while count is 2–5: at most four extra movements per unbroken
run. The counter saturates at six to prevent immediate rearming. Release on other
evidence, lost proposal, reset, predicted risk on the repeated action or any predicted
positive-progress option. Store one motion signature and counter. Models, hypotheses,
planner, proposals and weights are unchanged. Consistent motion does not establish
causal attribution or usefulness.

## Synthetic evidence

Six pixel-rendered structures with 100 paired label/colour permutations each.
Environment RNG `20261019 + seed`; selector RNG `seed`, seeds 0–99. Four keyboard
actions are offered. In the corridor one action moves a single pixel toward a goal
at its sixth movement; others do nothing. The immediate task succeeds on one action.
Turn tasks require a different action after the first two movements. Harmful motion
ends in failure if the original action is repeated a third time.

The known-turn control supplies four additional model/hypothesis observations at the
turn state: one success and three no-ops. These demonstrations are separate from the
two charged movement actions and online budget. It tests preservation of known
progress, not autonomous turn inference. Other turn fixtures receive only the two
initial movement demonstrations. Failed episodes receive capped cost 24, including
early deaths. These are designed structures with permutations, not 1,200 independent
ARC tasks.

| Fixture | Baseline solves / 100 | Candidate solves / 100 | Baseline / candidate capped actions |
|---|---:|---:|---:|
| Demonstrated corridor, primary | 0 | 100 | 24.00 / 6.00 |
| Immediate discovery, control | 100 | 100 | 3.11 / 3.11 |
| Known turn, control | 100 | 100 | 3.00 / 3.00 |
| Unseeded corridor, diagnostic | 0 | 25 | 24.00 / 20.50 |
| Unknown turn, diagnostic | 100 | 100 | 4.86 / 8.47 |
| Harmful motion, diagnostic | 100 | 0 | 4.86 / 24.00 |

Primary cost falls 75%; both declared positive controls pass. Autonomous corridor
discovery remains poor. Unknown-turn cost rises 74.28%; all 100 harmful candidate
episodes die, versus 100 baseline solves. Shared movement evidence is insufficient
to choose whether to persist. This is a substantive rejection reason apart from the
failed public completion gate; it was not used to tune the mechanism.

## Public evidence

Official cached OFFLINE engine: `arc-agi==0.9.9`, `arcengine==0.9.3`; framework
source matches pinned revision `4743e7d0aaae0ded0d98a89a7e282e63564cd58b`.
All ten game source/metadata hashes and 30 harness Python hashes match October 18.
Alternate arm order by seed. Primary cohort: **30 runs / 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate levels |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion remains **2 to 2**, failing retention. Zero qualifying observations,
established motion runs or overrides occur in either arm. Per arm, 1,208 of 1,488
observed transitions have no detected motion; the remaining 280 have multiple
motions. **None has exactly one motion.** Multiple-motion counts by game are
134 / 26 / 0 / 20 / 100 in table order. The first eligibility condition excludes the
entire cohort; later guards cannot explain inactivity.

All 15 paired runs have identical trajectories, scores and observations. Same-frame,
nonpositive-progress transitions remain 595; consecutive exact action-coordinate
repeats remain 746, ignoring source identity. Initial subprocess totals:
34.313 / 34.015 seconds. Warm replay: 35.723 / 35.961 seconds, **1.007x**.
These include full observation serialization, equal shadow controllers and startup;
audit I/O overlapped part of replay. They pass the bounded runtime check but are
not isolated production performance measurements. No held-out benchmark access,
official RHAE evaluation or competition submission.

## Verification and disposition

Candidate: **39 tests passed**, including 24 new cases for evidence continuity,
bounded continuation, action/direction/colour/source changes, contacts, progress,
terminal outcomes, irrelevant pixel changes, legal proposals, risk, reset/undo,
exact clicks and A–F adapter isolation. Formatting/lint passed; **11** notebook
modules matched source and compiled. Runner import sorting was fixed before runs.
Six adapter tests were added after the initial run; policy/runner/protocol hashes
stayed unchanged.

Independent audit checks **10,791 synthetic steps** and all **2,976 public decisions
and observations**, raw-grid fingerprints/diffs, continuity, guards, legality and
fixture solve/failure claims. All 15 baselines reproduce October 18's transitions,
scores and proposals after removing its serialized ActionKey `coordinates: null`
field; every removed field was asserted null. This schema-only normalization was
added after the initial comparison correctly flagged a mismatch. All 1,200 synthetic
records and 30 public runs replay exactly. Replay's extra 3,000 public actions are
repeated evidence, not independent trials.

Archived patch/source/tests/runner, then removed the candidate. Forward/reverse patch
checks pass. Restored baseline passes **15 tests**, formatting/lint and **10 notebook
source/compile checks**; production agent/tests/scripts match main. Only this report
and the research-plan note are committed.

Ignored evidence: `experiments/results/2026-10-19-motion-continuation/`, including
protocol, source/dependency/game/harness manifests, sanitized logs, compressed traces,
replay, independent audit, eligibility diagnostics and candidate source. Patch SHA-256:
`1788092ed50e68deb00a29849bd955c652424b47ea4e00749b36b41deae0050e`.
Reproduce by applying the archived patch to the base, restoring the protocol at that
ignored path, using recorded dependencies/cached games/harness, and running
`python experiments/run_motion_continuation.py --output <ignored-output-directory>`
with writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. Evidence is preserved
locally and mirrored with hash verification to the original workspace. Raw files are
not included in the pushed commit.

Recommend merging the negative research record and rejecting the mechanism. Before
another motion option, establish affordable evidence attributing object movement to
an intervention amid multiple moving components, and distinguishing useful from
harmful continuation. Relaxing the single-motion gate alone would not resolve the
demonstrated failure and requires a separate experiment.
