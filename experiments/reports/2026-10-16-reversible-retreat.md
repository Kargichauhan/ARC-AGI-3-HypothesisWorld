# Reversible retreat — 2026-10-16

Decision: **reject the implementation; merge the research record**. Undo returned
from synthetic dead ends, but the unchanged selector immediately entered the same
branch again. Delayed-effect action cost increased 80%, and public completion did
not improve. Candidate implementation, tests and runner were archived and removed;
production matches main.

## Hypothesis and fixed gates

Hypothesis: after all currently proposed actions produce two exact-state no-ops,
a single undo toward an observed predecessor escapes exhausted branches and improves
completion at affordable cost. This tests active reversal, unlike previous probe
deferral, fixed repetitions, ordered-pair coverage and graph frontier routing.

Preregistered before implementation and measurement; all gates required:

- Dead-end hub, 100 paired seeds, 60-action cap: candidate at least 95 solves,
  at least 30 percentage points of solve improvement, at least 20% lower mean capped actions.
- Immediate and delayed-effect controls, 100 paired seeds each: baseline at least
  95 solves, candidate loss at most five points, mean capped actions at most 1.5x baseline.
- Five cached official public games, F seeds 0/1/2, 100 actions: at least one extra
  total level, no per-game summed loss, warm runtime at most 2x baseline.
- Unit tests, formatting/lint and notebook source equality/compilation pass.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected the clean original
checkout, current remote main, all remote daily/research branch plans, recent reports,
git history and open PRs (none). Latest completed remote experiment was October 14;
no October 15 branch was present. Main remains unchanged. Git metadata in the original
workspace was read-only in the execution sandbox, so used a fresh temporary fork clone.
No prior unmerged mechanism was included, no game source was read to design the policy,
and no thresholds were adjusted after results.

## Mechanism

F-only adapter postselection. Preserve ordinary ranking and RNG draws. Record a
predecessor when an action other than reset/undo changes the fingerprint without
progress or terminal outcome. Track no-op streaks by exact fingerprint and full
candidate identity, including click coordinates. A no-op requires the same fingerprint,
no StateDiff change, zero progress and NOT_FINISHED.

If every offered non-undo candidate has two no-ops, undo is offered with no predicted
failure risk, no candidate predicts positive progress, and a predecessor is known,
choose undo once per remembered state. Observe whether the resulting fingerprint
actually equals that predecessor; the inverse is not assumed. Keep at most 512 FIFO
states and 128 exact actions per state. Progress, terminal outcomes and reset clear
controller evidence; observed effects clear that action's no-op streak. No routing,
branch suppression, changed state identity, hypothesis update or planner utility.

This intentionally small mechanism tests whether return alone is sufficient. It does
not prove a state is a dead end: hidden progress can produce repeated visible no-ops.
Fingerprint equality also cannot establish equality of hidden game state.

## Synthetic evidence

Five designed structures, each with 100 paired action-label permutations using
`20261016 + seed`, policy seeds 0–99. Each arm runs the complete F selector and online
memory/model/hypothesis updates. Distinct small pixel grids pass through the existing
perception and diff functions. The primary hub offers four actions: one goal, three
dead ends. A dead end offers four inert actions and undo to the hub. Immediate control
has four actions and one goal. Delayed control has one action: enter a branch, then
repeat four times; undo returns to the hub and clears the hidden count. Diagnostics
remove undo or make it lead to another dead end. These are label permutations of five
structures, not 1,000 independent tasks.

| Fixture | Baseline / candidate solves | Mean capped actions | Candidate undo attempts / verified returns |
|---|---:|---:|---:|
| Dead-end hub, primary | 24 / 24 | 45.84 / 45.84 | 76 / 76 |
| Immediate control | 100 / 100 | 3.40 / 3.40 | 0 / 0 |
| Delayed control | 100 / 100 | 5.00 / 9.00 | 100 / 100 |
| No undo available | 24 / 24 | 45.84 / 45.84 | 0 / 0 |
| Misleading undo | 24 / 24 | 45.84 / 45.84 | 76 / 0 |

Reject primary coverage, improvement and action-cost gates. All 76 successful primary
retreats were followed immediately by re-entry into the same dead end. Return alone
does not change the selector's valuation of the known ingress. The delayed control
has a competent baseline; candidate cost is **1.8x**, failing the 1.5x ceiling despite
preserving solves. No parameter retuning or branch-avoidance addition after measurement.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3; framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Alternate arm order by seed.
Primary cohort: **30 runs / 3,000 actions**. Entries are seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Completion remains **2 to 2**, failing retention. Candidate made **zero undo probes
and zero overrides**. Among 1,488 candidate non-reset decisions, undo was offered 294
times, a predecessor was known 1,063 times, and both held 186 times. Zero decisions
had two no-ops for every offered non-undo proposal. The all-proposal exhaustion
criterion never became available under the unchanged selector and proposal generator.

All 15 paired trajectories and selected scores were identical. Each arm had 595
same-fingerprint/nonpositive-progress transitions and 746 consecutive identical exact
action-coordinate pairs (source identity ignored). All 15 baseline runs' transitions,
selected scores and proposed candidates match the October 14 baseline exactly.

Initial subprocess totals **25.067 / 11.724 seconds** were startup-confounded (first
baseline worker: 17.103 seconds). Warm replay totals **9.506 / 9.933 seconds**, **1.045x**,
pass the runtime ceiling. Times include startup and equal controller observation/
tracing work in both arms; they are not isolated policy timings. Replay reproduces all
1,000 synthetic records and all 30 public runs exactly; its extra 3,000 public actions
are repeated evidence, not additional independent trials. No held-out access, official
RHAE measurement or competition submission; these public local results do not establish
performance on the hidden benchmark.

## Validation and disposition

Candidate: **30 tests passed**, including 15 new cases covering exhaustion prerequisites,
exact-coordinate identity, once-only attempts, false inverse verification, predicted
risk/progress guards, evidence bounds, effects, resets and adapter observation/ablation
integration. Formatting/lint passed; all **11 notebook modules** matched source and
compiled. An initial test incorrectly expected an unvisited undo destination to have
a context; corrected the test to expect absence. Adapter coverage was added afterward.
Neither change modified the measured policy. Both initial and validated source manifests
are preserved; the replay uses the final test sources and the same policy and runner.

Independent audit reconstructs all 29,584 synthetic transitions and checks environment
rules, legality and solve claims. It reconstructs public evidence prefixes and checks
all 2,976 non-reset decisions, full paired equality and exact replay. Candidate patch
passes forward/reverse application checks. Removed candidate; final baseline passes
**15 tests**, formatting/lint and **10 notebook source/compile checks**. Production
agent/tests/scripts match main. Broader ablations were conditional on F passing.

Reject this all-proposal exhaustion trigger and standalone retreat. A future experiment
must demonstrate affordable evidence for branch exhaustion, useful selection after
return, and protection for delayed progress. Any retreat plus branch-avoidance design
needs a separate preregistered factorial, including hidden-state and misleading-undo
controls. Do not infer that the public games lack reversible opportunities: this
controller never tested one.

Ignored evidence: `experiments/results/2026-10-16-reversible-retreat/` contains protocol,
compressed trajectories, manifests, dependencies, audits, validation, replay,
`candidate-source/` and `candidate.patch`. Raw evidence is preserved locally, not pushed.
Patch SHA-256: `93b2a1e3a4b65334a315224250da79e14afc75692d8715e8513e19d8b431fbd1`.
Reproduce by applying the patch to the base and running `experiments/run_retreat.py
--output experiments/results/retreat-reproduction` with the recorded dependencies,
cached games and writable MPLCONFIGDIR/XDG_CACHE_HOME, MPLBACKEND=agg. Copy the protocol
to its original ignored path for manifest hashing. Only this report and the research-plan
note remain in the final commit.
