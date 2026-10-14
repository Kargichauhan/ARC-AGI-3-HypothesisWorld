# Ordered-pair sequence coverage — 2026-10-14

Decision: **reject the implementation; merge the research record**. Systematic pair
coverage solved the designed repeat and switch tasks, but missed two synthetic
retention gates and added no public levels. Candidate code, tests and runner were
archived and removed. Production matches main.

## Hypothesis and fixed gates

Hypothesis: systematically covering ordered action pairs after an unchanged outcome
reveals hidden repeat- and switch-dependent effects, improving completion at acceptable
action cost. Unlike September 27's three identical attempts, this controller tests
both repeated and distinct action pairs. It does not infer a latent-state model.

Preregistered before implementation or measurement; all gates required:

- Hidden AA and AB fixtures, 100 paired seeds each, 40-action cap: at least 95 solves
  per fixture, at least 20 percentage points of pooled solve improvement, and at
  least 20% lower pooled mean capped actions.
- One-hit control: baseline at least 95 solves, candidate loss at most five points,
  and mean actions at most 1.5x baseline. Visible AB and hidden AAA/ABA are diagnostics.
- Five cached public games, full agent F, seeds 0/1/2, 100 actions: at least one extra
  total level, no per-game summed loss, warm runtime at most 2x baseline.
- Passing unit tests, formatting/lint and notebook source equality/compilation.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean workspace, remote
main/daily heads, open PRs (none), research plan, history, prior memory and recent
reports, including temporal probes, epistemic disagreement, frontier routing,
continuation utility, joint planning, relational transfer and change-point forgetting.
Remote main and daily heads matched the verified temporary checkout. No game source
was inspected to design the policy; no unmerged mechanism or parameter retuning.

Cloud-backed reads stalled and an initial fetch hit disk exhaustion. Reused the
verified temporary checkout and dependencies. Removed only 49,157,526 bytes of
regenerable bytecode from that experiment environment, disabled bytecode generation,
and compressed new raw records. Prior evidence and unrelated user files were preserved.

## Mechanism

F-only adapter controller. After an action leaves an identical fingerprint, no
StateDiff change or progress, and NOT_FINISHED, freeze the four highest-ranked distinct
exact candidates, excluding RESET and undo. If fewer exist, use those. Execute a
linearized order-two de Bruijn cycle, requiring m*m+1 actions to cover every ordered
pair in an alphabet of size m. Exact click coordinates distinguish interventions.
Ordinary ranking and its RNG draws continue on every decision.

Release on visible change, nonzero progress, terminal outcome, changed source, missing
proposed candidate, or reset. Remember attempted source fingerprints in a 512-entry
FIFO; do not repeat a schedule while its source remains remembered. Reset clears that
memory. Hypotheses, world model, planner, pooled action keys, proposals and weights
are unchanged. The top-four restriction can exclude useful actions; pair coverage
cannot guarantee arbitrary longer sequences or persistence through visible changes.

## Synthetic evidence

Four action labels are permuted using `20261014 + seed`; policy seeds are 0–99.
The goal is a specified suffix of action history: AA, AB, A, AAA or ABA. Incorrect
inputs drop the unmatched prefix; overlapping prefixes are retained. Hidden tasks
show one unchanged frame until success. Visible AB changes the fingerprint and
supplies a changed-cell observation for its prefix. Each arm runs the complete
selector and online memory/model/hypothesis updates. These are six designed structures
with label permutations, not 1,200 independent ARC tasks. Visible-prefix observations
are injected structured states, not a pixel-rendered game.

| Fixture | Baseline / candidate solves | Baseline / candidate mean capped actions |
|---|---:|---:|
| AA, primary | 64 / 100 | 21.38 / 10.72 |
| AB, primary | 100 / 100 | 12.21 / 10.27 |
| A, immediate control | 100 / 100 | 3.08 / 4.67 |
| AAA | 0 / 29 | 40.00 / 29.27 |
| ABA | 30 / 37 | 34.24 / 30.88 |
| Visible AB | 40 / 41 | 29.56 / 27.53 |

Pooled primary solves improve **82% to 100%**, only **18 points**, below the required
20. Mean capped actions fall **16.795 to 10.495**, a **37.51%** reduction. Immediate
control cost rises **51.62%**, narrowly exceeding the fixed 1.5x ceiling. Reject both
failed gates without loosening them. Poor visible and longer-sequence performance
limits the scope of the positive pair-coverage demonstration.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9 / arcengine 0.9.3; framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Alternate arm order by seed.
Primary cohort: **30 runs / 3,000 actions**. Entries show seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Completion remains **2 to 2**, failing retention. The controller activates 104 times,
executes 235 scheduled actions and overrides the top-ranked action 75 times. Only
three schedules complete full pair coverage: one per ft09 seed. All 300 ft09 actions
still yield no-op outcomes. No schedule activates in vc33.

Same-frame/no-positive-progress transitions fall **595 to 490**. Consecutive identical
action-coordinate pairs fall **746 to 592**; this metric ignores source identity and
is not the older 687-repeat metric. Most no-op reduction is in su15 seed 2 (100 to 15)
and cn04 seed 1 (55 to 25), with no level completion. Exploration effects alone do
not meet the stated objective.

Independent audits verify every synthetic suffix/solve claim, all 2,974 non-reset
public decisions against offered candidates, no-op prerequisites for activations,
and all 16 ordered pairs exactly once in each completed four-action schedule.
All 15 baseline trajectories and selected scores match October 13 exactly.
Replay reproduces all 30 public trajectories and all 1,200 synthetic records exactly;
its additional 3,000 public actions are not independent evidence.

Initial subprocess totals **24.025 to 12.258 seconds** are startup-confounded (first
baseline: 15.785 seconds). Warm totals **11.870 to 12.143 seconds**, **1.023x**, pass
the runtime ceiling. Times include startup and equal tracing, not isolated policy
speed. No held-out access, official RHAE measurement or competition submission.

## Validation and disposition

Candidate: **30 tests passed** (15 new cases), formatting/lint and all **11 notebook
modules** matched source and compiled. Unit cases cover exact pair coverage for
alphabets one through four, no-op gating, frozen ranking, exhaustion, effect/progress/
terminal cancellation, source changes, coordinate identity, lost legality, excluded
actions, bounds, reset and disabled selection parity. A runner import-format issue
was fixed before measurement; an audit-script indentation error was fixed before its
final checks. Neither changed the measured policy or thresholds.

Archived candidate sources, tests, runner and patch; restored baseline passes
**15 tests**, formatting/lint and **10 notebook source/compile checks**. Forward and
reverse patch applicability passed. Production agent, tests and scripts match main.
Broader public ablations were conditional on F passing and were not run.

Reject this unconditional pair schedule. It guarantees local pair coverage but spends
extra actions on easy tasks and does not ensure that its frozen alphabet contains
useful interventions. Future sequence work should first demonstrate affordable
selection of relevant interventions and evidence that distinguishes repeat-required
from switch-required contexts; do not accumulate this controller based on fewer no-ops.

Ignored local evidence: `experiments/results/2026-10-14-sequence-cover/` contains the
protocol, compressed raw traces, manifests, dependencies, audits, replay, validation,
candidate sources and `candidate.patch`. Raw evidence is not pushed. Patch SHA-256:
`84f6104485259d48e4af9b5775753d9aff5a181969e94b0833eab3f5949ee071`.

Reproduce by applying the patch to the base and running
`experiments/run_sequence_cover.py --output experiments/results/sequence-reproduction`
with recorded dependencies, cached games, writable MPLCONFIGDIR/XDG_CACHE_HOME and
MPLBACKEND=agg. Copy the protocol to its original ignored path for manifest hashing.
Only this report and the research-plan note remain in the final commit.
