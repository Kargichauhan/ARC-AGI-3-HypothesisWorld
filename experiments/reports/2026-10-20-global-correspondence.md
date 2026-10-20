# Global object correspondence — 2026-10-20

Decision: **reject the implementation; merge the research record**. Global assignment
reduces designed synthetic identity errors but changes no public correspondence,
outcome or decision. Public completion stays at two levels. Candidate implementation,
tests and runner were archived locally and removed before the final commit.

## Hypothesis and fixed criteria

Hypothesis: maximizing total object similarity across consecutive frames avoids greedy
identity theft, improving motion evidence and full-agent completion. This changes
perceptual correspondence alone, unlike October 19's motion continuation policy.
No rejected controller or other unmerged mechanism was included.

Before implementation and measurement, all retention gates were recorded:

- Primary synthetic: 200 paired layouts, eight identical moving objects each;
  at least 20% fewer incorrect source-object correspondences, with nonzero baseline
  errors. An unmatched surviving object counts as an error.
- Stationary and distinct-colour controls, 200 layouts each: both arms must achieve
  at least 95% correspondence accuracy; candidate loss at most one percentage point.
  Removal/replacement is a separately reported diagnostic.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra total
  completed level without per-game summed regression; warm subprocess runtime at
  most twice baseline. A–E runs conditional on passing the F and synthetic gates.
- Passing unit tests, formatting/lint, notebook generation/source equality/compile,
  trace audit and deterministic replay.

No gate or parameter was tuned after measurement. Before measurement, an explicit
protocol clarification added a fixed (+1,+1) rendering origin to prevent a -4 shift
from leaving the frame. All sampled layouts and both arms share this translation.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected the clean original
checkout, fresh remote main/daily/research branches, plans, all report introductions,
recent full reports, Git history and open pull requests (none). Used an isolated
temporary clone because original cloud-backed Git reads had been slow. No game
implementation was inspected for experiment design.

Replace greedy edge selection with dependency-free maximum-weight bipartite assignment.
Keep the exact original overlap, shape, colour, distance and size score, and the
strict score >0.25 admissibility threshold. Add zero-weight dummy columns so every
old object may remain unmatched. A shortest-augmenting-path solver uses deterministic
ascending-index tie breaks. Return chosen matches in the original descending-score
order. Extraction, fingerprints, differencing semantics, proposals, hypotheses,
world model, planner, selector and RNG remain unchanged. Worst-case cost on dense
frames was not established by this pilot.

The runner loads frozen main perception for baseline and changes only the matcher.
All 15 baseline public runs reproduce October 19's transitions, scores and proposals.

## Synthetic evidence

Four designed scene families, 200 seeds each, with RNG `20261020 + seed`.
Each 40x40 frame contains eight non-touching 2x2 sprites, uniformly rejection-sampled
at x/y in [3,26], then translated by (+1,+1). Common displacement is sampled from
(4,0), (-4,0), (0,4), (0,-4). Primary sprites share a sampled colour 1–9. The
stationary control has zero displacement; the distinct control uses colours 1–8.
The occlusion diagnostic removes a random sprite and introduces a differently
coloured sprite at a free location. Generated identity is the scoring ground truth.
Extraction is checked against all eight intended objects in every frame.

| Fixture | Baseline errors / 1,600 | Candidate errors / 1,600 |
|---|---:|---:|
| Coherent translation, primary | 743 | 263 |
| Stationary, control | 0 | 0 |
| Distinct colours, control | 137 | 0 |
| Removal/replacement, diagnostic | 732 | 377 |

Primary errors fall **64.60%**, passing the improvement gate. Paired error savings
average 2.40 per layout; 10,000 seed resamples give a 95% bootstrap interval
[2.185, 2.620]. Better/tie/worse layouts: **167 / 33 / 0**. This interval describes
variation within the designed generator, not unseen ARC task uncertainty.

Both stationary arms and the candidate distinct-colour arm reach 100% accuracy.
However, baseline distinct-colour accuracy is **91.44%**, failing the preregistered
baseline-competence requirement. Do not treat that control as proof that baseline
already solves easy identity cases. Preserved pair scoring can favor cross-colour
spatial overlap over the true translated object. Even global optimization leaves
263 primary errors: maximizing this score does not establish physical identity.
These are 800 designed frame pairs, not 800 independent ARC tasks or online solves.

## Public evidence

Official cached OFFLINE engine: `arc-agi==0.9.9`, `arcengine==0.9.3`; harness source
matches pinned revision `4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. All ten cached
game source/metadata hashes and 30 harness Python hashes match October 19. Arm
order alternates by seed. Primary cohort: **30 runs / 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Candidate levels |
|---|---|---|
| ls20-9607627b | 0 / 0 / 0 | 0 / 0 / 0 |
| vc33-5430563c | 1 / 0 / 1 | 1 / 0 / 1 |
| ft09-0d8bbf25 | 0 / 0 / 0 | 0 / 0 / 0 |
| cn04-2fe56bfb | 0 / 0 / 0 | 0 / 0 / 0 |
| su15-1944f8ab | 0 / 0 / 0 | 0 / 0 / 0 |

Completion remains **2 to 2**, failing retention. Independently recomputing both
matchers on all **2,976 observed frame pairs** finds zero different assignments,
zero different outcome signatures and zero higher assignment objectives. Thus
all 15 paired traces, scores, observations and transitions are identical.
Per arm, 595 same-frame/nonpositive-progress transitions and 746 consecutive exact
choices repeat. Detected object motions by game are 274 / 52 / 0 / 56 / 200;
these count objects, not transitions. Yesterday's multiple-motion observations
therefore cannot be attributed to greedy assignment suboptimality in this cohort.
This does not establish that the shared scoring or segmentation is correct.

Initial subprocess totals: **13.181 / 13.884 seconds** (baseline/candidate).
Warm replay: **13.185 / 13.535 seconds**, **1.027x**, passing the runtime gate.
Public runs include equal tracing/serialization and startup; shadow matching is
computed separately during the audit, outside timed gameplay. Matcher-only sampled
times are also retained. No held-out benchmark access, official RHAE evaluation or
competition submission.

## Verification and disposition

Candidate: **26 tests passed** (15 baseline and 11 new), including a separately
implemented exhaustive assignment oracle over 320 random small matrices, optional
unmatched/rectangular cases, deterministic ties, unique-optimum permutations, unchanged
frames and birth/death events. Formatting/lint pass; **10 notebook modules** match
source and compile. Runner lint was repaired before the measurement manifest.

The audit checks **800 synthetic scenes / 12,800 arm-specific correspondence slots**,
2,976 public decisions and observations, raw-grid differences, assignment legality,
partition completeness, original pair scores, objective dominance, outcome signatures,
legal selected proposals, source integrity and prior baseline reproduction.
All 800 synthetic records and 30 public runs replay exactly with the same source
manifest. Replay adds 3,000 repeated public actions, not independent trials.

Archived the complete candidate patch/source/tests/runner, then removed the candidate.
Forward/reverse patch checks pass. Final baseline: **15 tests**, formatting/lint and
**10 notebook source/compile checks** pass; production agent/tests/scripts match main.
Only this report and the research-plan note are committed.

Ignored evidence: `experiments/results/2026-10-20-global-correspondence/`, including
protocol, frozen baseline, dependency/source/game/harness manifest, raw compressed
traces, sanitized logs, replay, independent audit, paired summaries and candidate.
Patch SHA-256: `fef4e9ad0544e4761fcef54c283a3bb2045c058ec57f37d4ce25755c09ada9cc`.
Reproduce by applying that patch to the base, restoring the archived protocol and
baseline perception at the ignored evidence path, using the recorded dependencies
and cached games/harness, then running
`python experiments/run_global_correspondence.py --output <ignored-output-directory>`.
Use writable MPLCONFIGDIR/XDG_CACHE_HOME and MPLBACKEND=agg. Raw evidence is mirrored
with hash verification to the original workspace; it is not in the pushed commit.

Recommend merging the negative research record and rejecting the implementation.
Before another correspondence change, establish public, decision-relevant matching
errors or a different correspondence objective with ground-truth controls. Merely
optimizing the existing score more thoroughly does not address this cohort's failure.
