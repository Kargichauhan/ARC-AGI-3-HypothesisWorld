# State-conditioned falsification — 2026-10-08

Decision: **reject the implementation; merge this research record**. Context-local
hypotheses solved the supplied contextual decision diagnostic, but public completion
remained two levels. Implementation, tests and runner were archived locally and
removed before commit. Production files match main.

## Hypothesis and protocol

Hypothesis: an action's contradictory effects in distinct visible states should not
falsify each other's rules. Separating their evidence improves contextual decisions
and full-agent public completion.

Retain the globally updated hypothesis engine. For queries with at least three
observations of an exact fingerprint/ActionKey pair, replay the last 32 observations
into an unchanged local engine. Keep at most 64 context pairs, FIFO; invalidate query
caches on updates. Lower-count/unseen contexts use global predictions exactly. D uses
local predicted progress/risk; E/F use local disagreement. Prediction logs follow the
same query path; top-hypothesis/update logs remain global. Memory survives reset as
before. World model, planner, action keys, proposals, coefficients, RNG and observation
contract are unchanged. This tests scoped support/contradiction, distinct from
September 26's empirical uncertainty weighting and October 4's semantic-conflict score.
It neither generalizes preconditions to new frames nor resolves hidden-state aliasing.

All retention gates were recorded before measurement:

- D contextual diagnostic: >=90% correct and >=40 percentage points above baseline
  on 200 decisions, 100 paired seeds.
- Stationary control: baseline >=95% correct, candidate loss <=5 percentage points.
  Exact global-score fallback for unseen/low-count contexts.
- F public pilot: >=1 additional completed level, no per-game summed completion loss,
  warm audited runtime <=2x baseline.
- Unit tests, format/lint, notebook generation/source equality/compilation pass.

Base/main `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Fetched origin and inspected
main, remote research/daily branches, history, plans, recent reports and October 4's
uncommitted negative evidence. No open PRs. No unmerged mechanism, game-source design
access or post-result tuning.

## Synthetic evidence

Two visible contexts require opposite actions. Each receives both-action demonstrations
for 12 alternating rounds: correct action gives progress 1/WIN, other gives progress
0/GAME_OVER. Labels/context order are shuffled with `20261008 + seed`; policy seeds
0–99. The stationary control uses the same good action in both states. The hidden
control maps both contexts onto one fingerprint.

| Correct D decisions / 200 | Baseline | Contextual |
|---|---:|---:|
| Opposite visible preconditions | 100 | 200 |
| Stationary useful action | 200 | 200 |
| Aliased hidden preconditions | 100 | 100 |

The primary gain is 50 percentage points; synthetic gates pass. These are trained
decisions, not online solves. The 1,200 arm/context/fixture/seed records are not
independent ARC tasks. No calibration or hidden-state competence claim.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3, F, seeds 0/1/2,
100 actions per game. Baseline first for seeds 0/2, candidate first for seed 1.
Primary cohort: **30 runs / 3,000 actions**.

| Game/version | Baseline levels, seeds 0/1/2 | Contextual levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion **2 → 2** fails retention. Repeated exact actions **687 → 685**;
same-fingerprint/no-positive-progress outcomes **595 → 600**. Twelve of fifteen
paired action/transition trajectories are identical; only `ls20` changes.

Candidate-history diagnostics, summed over three seeds:

| Game | Decisions with eligible local bank | Any changed information score | Changed shadow top choice |
|---|---:|---:|---:|
| ls20 | 38 | 38 | 14 |
| vc33 | 0 | 0 | 0 |
| ft09 | 291 | 0 | 0 |
| cn04 | 18 | 18 | 0 |
| su15 | 97 | 0 | 0 |

Shadow comparisons substitute only global/local information into the same ranking,
without RNG draws. These are history-conditioned comparisons, not causal performance
estimates. On baseline histories, shadow choices differ 26 times, all in `ls20`.
F already obtains reward/risk from the empirical world model, so the synthetic D gain
does not directly change its reward estimates. Exact-context eligibility is absent in
the only game with completed levels; repeated no-op games retain the same disagreement.
All 300 candidate `ft09` actions remain no-ops.

Initial times **28.763s → 9.805s** were startup-confounded: baseline seed 0 alone took
22.237s. Warm replay: **9.853s → 9.775s (0.992x)**. Both arms include startup, context
recording and identical global/local shadow auditing; this is not isolated production
speed evidence. All 30 public traces and 1,200 synthetic records reproduce exactly.
The additional 3,000 public actions are replay, not independent evidence. All 15
baseline trajectories exactly reproduce October 7's warm baseline, including scores,
actions and transitions. No held-out or official Relative Human Action Efficiency
result; no competition submission.

## Validation, decision and reproduction

Candidate: **31 tests passed** (16 added cases), format/lint passed, all **10** notebook
modules match source and compile. Tests cover cross-context contradiction isolation,
unchanged global updates, low-count fallback, coordinate-key separation, bounded
storage/eviction, cached-window replay, A–C isolation, all-ablation unseen score parity,
and source-context terminal attribution. After removal: **15 baseline tests** and the
same format/lint/packaging checks passed. Production agent/tests/scripts/notebook
configuration match main. Import-order lint was fixed before measurement. An adapter
test was added after the initial manifest; final source hashes are recorded separately.
Dependencies were rebuilt from the previous pinned freeze in a temporary environment
because the previous temporary environment was missing.

Reject this exact-state bank. Do not retain it based only on the D diagnostic. Future
precondition work needs reusable contexts where useful and harmful outcomes coexist
and affect F's ranking; establish that coverage before adding generalization. Any
representation combination needs false-alias controls and a preregistered completion
gate. Broader public ablations were conditional on F passing and were not run.

Ignored evidence: `experiments/results/2026-10-08-contextual-falsification/`, including
protocol, source/game/dependency manifests, raw synthetic/public traces, warm replay,
audit, validation, source snapshot and removed `candidate.patch`. Raw evidence is local
and is not pushed. Patch forward/reverse applicability checked. SHA-256:
`27cfcf3aae9caa447a12fabbed2df6a82bc9b151e28afdc0589a3b2b1b21bfda`.

For local reproduction, apply the archived patch to the base with recorded dependencies
and cached games. Copy the protocol into the output directory, then run
`experiments/run_contextual_falsification.py --output experiments/results/contextual-reproduction`
with writable `MPLCONFIGDIR` and `XDG_CACHE_HOME`. Only this report and the research-plan
addition remain on the branch.
