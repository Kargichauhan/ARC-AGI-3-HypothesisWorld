# Reachable action frontiers — 2026-10-03

Decision: **reject the implementation; merge this research record**. Routing reaches
synthetic states containing untested actions, but the selector does not execute the
useful probe. Neither synthetic solves nor public completion improve. Archived and
removed the candidate, its ten tests, frozen baseline and runner before committing.

## Hypothesis and fixed gates

Hypothesis: navigating known transitions to observed states with untested actions
improves exploration and completion over short-horizon state novelty. Unlike the
September 20 path-novelty and September 23 continuation-utility pilots, the objective
is a reachable experiment opportunity, with search beyond the existing two-step horizon.

Preregistered before implementation and measurement:

- Four-edge pre-explored corridor/branch fixture, 100 paired seeds, 32-action cap:
  at least 95 candidate solves and at least 20% lower mean capped action cost.
- Immediate-goal control: baseline at least 95 solves, candidate loss at most five
  percentage points, action cost at most 1.1x. Lengths two and six are diagnostics.
- Five cached official public games, F seeds 0/1/2, 100 actions: at least one extra
  level without per-game summed regression; warm runtime at most 2x baseline.
- Passing unit controls, formatting/lint and notebook source/compilation checks.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. The restored checkout was clean;
fetched origin and inspected main, remote daily/research branches, history, plans
and prior reports/evidence. GitHub connector returned no open PRs. No unmerged
mechanisms or game implementation details were used to design the candidate.

## Mechanism and experiment

Only the F planner changes. Store the latest observed candidate keys for at most
512 fingerprints, evicting states FIFO. A frontier has an observed non-reset/non-undo
key with zero local tests. Construct edges from the existing 512-transition memory,
require empirical destination frequency at least 0.68, and exclude source/action
pairs with a retained terminal or negative-progress observation. Edges also require
an observed legal key at their source. No RESET or undo navigation.

Search simple paths of at most six edges and 512 expansions per root action. Exclude
the root as a frontier. Replace old novelty continuation with twice the best path
probability product, discounted by 0.8 per extra edge. Preserve the original immediate
`2 * confidence * expected_progress` term and all selector weights, hypotheses,
proposals, action identities and RNG draws. No retuning after results.

The synthetic fixture supplies frozen exploration data: four observations for every
state/action except the final goal probe, registered candidate sets at every state,
and 20 extra visit observations per corridor state. Forward traverses the corridor,
backward retreats (or visits a root-side branch), and two other actions are no-ops;
the branch returns to the root. The final forward probe completes the task. Labels
are permuted with seed `20261003 + seed`; selection uses seeds 0–99. Each arm receives
identical data and updates the complete selector online. The immediate control
includes known terminal progress. These are designed topology/label diagnostics,
not independent ARC tasks or a demonstration of learning a map from scratch.

## Results and diagnosis

| Fixture | Baseline solves | Candidate solves | Baseline mean actions | Candidate mean actions |
|---|---:|---:|---:|---:|
| Immediate known goal | 100/100 | 100/100 | 1.00 | 1.00 |
| Two-edge corridor | 0/100 | 0/100 | 32.00 | 32.00 |
| Four-edge corridor, primary | 0/100 | 0/100 | 32.00 | 32.00 |
| Six-edge corridor | 0/100 | 0/100 | 32.00 | 32.00 |

Candidate reaches the frontier in **100/100** trials at each corridor length,
using exactly two/four/six actions; baseline never reaches it within budget. But
arrival is not completion. In primary seed zero, at the frontier the unseen goal
probe scores **1.122**, while trained no-ops score **1.469** through persistent
hypothesis disagreement. Root exclusion prevents fictitious self-loop navigation
credit, but leaves probe execution to that selector. The synthetic gate fails;
no coefficient or frontier rule was revised to fit this observation.

Official cached OFFLINE engine: arc-agi 0.9.9, arcengine 0.9.3, framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. Primary cohort: **30 runs / 3,000 actions**,
alternating arm order by seed. Each entry lists seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion **2 → 2** fails the public gate. Repeated exact actions **687 → 432**;
same-fingerprint/no-positive-progress outcomes **595 → 478**. Candidate assigns
positive frontier continuation on 209 decisions: vc33 114, cn04 34, su15 61;
none in ls20 or ft09. Thus changed behavior in those latter games reflects removal
of old novelty continuation, not successful routing. No frontier-only causal benefit
can be isolated without a separate ablation. All 300 candidate ft09 outcomes are no-ops.
The raw `frontier_active` field means any exploration planning above immediate progress;
for baseline it measures the old novelty term, not a frontier mechanism.

Initial times **34.940 s → 9.901 s** are startup-confounded: first baseline subprocess
alone took 28.611 s. Warm replay totals **10.310 s → 10.706 s (1.038x)** pass the
runtime gate, including equal auditing and process startup. All 30 public trajectories
and 800 synthetic records reproduce exactly. The extra 3,000 public actions are
replay, not independent evidence. All 15 baseline trajectories exactly reproduce
September 27's warm actions, scores and transition records.

## Validation, limitations and disposition

Candidate **25 tests passed**, including ten new tests for discounted reachability,
exhausted graphs, root loops, terminal/low-confidence edges, immediate progress,
observed legality, undo exclusion, bounded state storage/search and duplicate keys.
Formatting/lint and all **10 notebook module source/compile checks** passed.
After removal, **15 baseline tests** and the same format/lint and packaging checks
passed; production agent, tests, scripts and notebook settings match main.
A–E parity was conditional on F retention and was not run after rejection.

The cloud-backed old virtual environment stalled. A temporary environment restored
the same benchmark engine versions; full dependencies and hashes are archived.
No held-out evaluation, official RHAE measurement or competition submission occurred.
Observed legal sets can become stale, pooled click keys can hide untried coordinates,
and exact fingerprints limit transfer. Bounds and confidence thresholds are fixed
pilot choices, not calibrated guarantees of safe or reliable navigation.

Reject standalone frontier routing. Before another routing experiment, test whether
a policy can execute the intended untested probe once it arrives; the existing
persistent-disagreement bonus defeats that step even on a fully supplied map.
Any routing/probe-selection combination needs an independently preregistered factorial
with competent controls, not retention based on frontier arrivals or fewer repeats.

Ignored local evidence: `experiments/results/2026-10-03-frontier-routing/` holds the
protocol, raw traces, manifests, dependency versions, replay/parity audit, validation
and removed `candidate.patch`. Raw evidence is not pushed. Patch SHA-256:
`034bc93984dd04e9013544266bb3c10a88f2008e51ac12866a673031154de1be`.
Forward and reverse application checks passed. To reproduce, apply the patch to the
base, copy the protocol into a fresh ignored output directory, and run
`experiments/run_frontier.py --output experiments/results/frontier-reproduction`
with recorded dependencies/cached games and writable plotting/cache directories.
