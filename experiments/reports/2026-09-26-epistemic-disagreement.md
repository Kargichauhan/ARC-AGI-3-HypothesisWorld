# Epistemic disagreement — 2026-09-26

Decision: **reject the candidate; merge this research record**. Scaling hypothesis
entropy by empirical uncertainty improved synthetic discovery, but public completion
stayed at two levels. Candidate implementation, tests and runner were archived locally
and removed before committing.

## Hypothesis and fixed gates

Hypothesis: local uncertainty about outcome probabilities distinguishes learnable
uncertainty from persistent disagreement among hypothesis labels, reducing redundant
experiments and improving completion. Multiply the existing information bonus by mean
normalized Beta(1,1) expected information for three binary observations: visible cell
change, positive progress, and GAME_OVER. Use only matching fingerprint/action records
in the existing 512-transition window; unseen contexts retain weight one.

For posterior counts `a,b`, information is binary entropy at `a/(a+b)` minus expected
posterior binary entropy, computed with harmonic numbers and normalized by
`log(2)-1/2`. Average the three marginal weights. This heuristic is not a joint
posterior or information about the agent's explicit hypotheses. State/action pooling,
model confidence, hypothesis updates, planning, reward, novelty, proposals and RNG
remain unchanged; only E/F information scores change. Unlike September 17's rejected
rollout estimator, this uses empirical binary outcomes without wildcard likelihoods.

Preregistered retention required all of:

- At least 95/100 synthetic discovery solves and 20% lower mean capped actions.
- Known-progress control baseline accuracy at least 95/100, candidate loss at most
  five percentage points; exact score parity in unseen contexts.
- Residual information below 5% after 100 deterministic or balanced outcomes, with
  the analytic formula independently checked by numerical integration.
- At least one extra public level, no per-game summed loss, and runtime at most 2x:
  five cached games, F, seeds 0/1/2, 100 actions each.
- Passing unit tests, formatting/lint, notebook generation and source/compile checks.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Fetched origin; main unchanged,
no open PRs. Reviewed remote daily/research branches, history, plans and recent reports.
No unmerged mechanism or game-source knowledge informed the candidate. No retuning.

## Evidence

Discovery used four randomized action labels, one successful action and three no-ops,
20-action cap, fixture RNG `20260926 + seed`, policy seeds 0–99. The control demonstrated
20 successes for one action and 20 no-ops for each alternative. Progress observations
can occur without cell changes; both arms use the same observation contract.

| Synthetic diagnostic | Baseline | Candidate |
|---|---:|---:|
| Discovery solves / 100 | 100 | 100 |
| Mean discovery actions | 3.61 | 2.67 |
| Known-progress choices correct / 100 | 100 | 100 |

Discovery actions fell **26.04%**; paired savings 0.94, bootstrap 95% interval
[0.74, 1.15], 56 better / 44 ties / zero worse. Unseen-context scores match exactly.
Residual information is 2.53% for balanced and 2.15% for deterministic observations.
These are designed fixtures and label permutations, not independent ARC tasks or
hidden-state competence tests. No calibration or causal-identification claim follows.

Public primary cohort: **30 runs / 3,000 actions**, official cached OFFLINE engine,
arc-agi 0.9.9 / arcengine 0.9.3; alternating arm order. Entries list seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion **2 → 2** fails the gate. Repeated exact actions fell **687 → 450**;
same-frame/no-positive-progress outcomes fell **595 → 490**. On baseline histories,
changing only the information term changes the top choice at 509 decisions; the
reverse comparison on candidate histories changes 118. These conditional shadow
counts are not trajectory improvement estimates.

In `ft09`, unique exact actions rose from 3/3/3 to 24/24/23, yet **all 300 outcomes
remain no-ops**. Mean selected information fell 0.680 → 0.266. Increased use of the
existing proposal set cannot establish that useful interventions are available.
`vc33` has zero shadow choice changes and retains the same completion pattern.

Initial times 30.190 s baseline / 13.843 s candidate were startup-confounded despite
engine import warmup: first baseline subprocess alone took 23.043 s. Warm replay:
**11.203 s → 11.308 s (1.009x)**, including equal shadow auditing and startup.
All 30 traces and synthetic/control records reproduced exactly; the extra 3,000
actions are replay, not independent evidence. All 15 baseline trajectories reproduce
September 25's warm scores, actions and recorded transitions.

Candidate: **25 tests passed** (ten added cases), formatting/lint and all **10**
notebook module source/compilation checks passed. After removal: **15 baseline tests**
and the same checks passed. Production source, tests, scripts and notebook configuration
match main. A–D unit checks confirm only E/F read the weights; broader public ablations
were conditional on F passing and were not run after rejection.

## Decision and reproduction

Reject this standalone uncertainty weighting. Do not retain it on reduced repetition
alone. Future work should audit whether generated interventions can expose useful
state changes and sequences; any combination with changed proposals needs a separate
factorial protocol and a completion gate. This short public pilot provides no held-out
benchmark or official Relative Human Action Efficiency result. No submission or merge.

Ignored evidence under `experiments/results/2026-09-26-epistemic-disagreement/` includes
protocol, raw synthetic/public records, warm replay, source/game/dependency manifests,
reproduction audits, validation and removed `candidate.patch`. Raw evidence is not pushed.
Patch SHA-256: `1723a8ad19316ec58f05490f5e4b4ae89d497cead324e743966b91954dece16c`.

To reproduce, apply the archived patch to the base, then run
`experiments/run_epistemic_disagreement.py --output experiments/results/epistemic-reproduction`
with recorded dependencies and cached games. Use writable `MPLCONFIGDIR`/`XDG_CACHE_HOME`
and copy the protocol into the output directory to record its hash. Patch forward and
reverse applicability were checked. Only this report and the plan remain on the branch.
