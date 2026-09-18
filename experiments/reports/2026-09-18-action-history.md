# Action-history fallback pilot — 2026-09-18

Decision: **reject this implementation**. Conditioning unseen-state action outcomes
on the preceding action did not improve public-game completion, and its prediction
improvement was below the preregistered threshold. Candidate code and tests were
removed; production behavior matches the base revision.

## Hypothesis and protocol

Hypothesis: the preceding action identifies latent preconditions that a state-only
model misses, improving cross-state prediction and action efficiency. Keep exact
state/action predictions unchanged and condition only fallback outcome counts on
`(previous action ID, current ActionKey)`. Shrink each context toward the global
action distribution using eight pseudo-observations. Reset history at RESET,
WIN and GAME_OVER. Do not change planning or experiment-selection weights.

Before implementation, the ignored `protocol.md` recorded these retention gates:

1. At least 25% combined squared-error reduction on held-out history-dependent
   synthetic transitions; at most 5% regression on an independent control.
2. At least 5% combined prediction-error reduction on baseline-policy public
   fallback transitions, with no per-game regression greater than 5%.
3. At least one additional completed public-game level, no decrease in summed
   levels for any game, and total wall time no more than twice baseline.

All gates were required. Parameters and thresholds were not retuned after results.

## Implementation and evaluation

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65` (`origin/main`). Origin was fetched;
there were no open PRs. The stable-state branch and September 17 negative EIG
report were inspected. Neither unmerged experiment was incorporated. This resumes
the September 18 scheduled run, which had stopped at a usage limit during research.

The candidate added optional history-conditioned fallback in `agent/world_model.py`,
reset integration in `agent/my_agent.py`, and seed/history environment flags in
`agent/config.py`. Both benchmark arms used the same seed handling. Seven additional
test cases covered shrinkage, exact-state precedence, unseen histories, reset and
terminal boundaries, temporal alignment, prediction purity, and configuration.

Synthetic evaluation used 20 seeds for each of two generators, with 200 training
and 200 held-out transitions per seed. Actions were sampled from IDs 1 and 2.
Progress probability was 0.9 after action 1 and 0.1 after action 2 in the dependent
generator, and 0.5 regardless of history in the control. Evaluation used fresh state
keys and the observed preceding action without updating fitted counts. There were
8,000 held-out transitions total. Effects were represented as progress-only diffs.

Public evaluation used the installed official engine in OFFLINE mode and its usual
framework lifecycle, with five cached games, agent seeds 0/1/2, full ablation F,
and 100 actions per game. Arm order alternated across seeds. Each arm maintained
two shadow models that predicted before learning from the same transition and
received identical episode resets. Only baseline-policy fallback records were used
for the calibration gate. Shadow auditing was included in both runtime measurements.

The primary prediction loss averaged scene-change Brier loss, failure Brier loss,
and squared error of nonnegative progress count. Exact-state predictions were
excluded from the public calibration gate because the candidate does not change them.

## Results

| Held-out synthetic generator | Baseline error | History error | Relative change |
|---|---:|---:|---:|
| History-dependent | 0.249844 | 0.196436 | −21.38% |
| Independent control | 0.249070 | 0.250082 | +0.41% |

The dependent synthetic reduction missed the 25% gate. An audit found a limitation:
`StateDiff.changed` includes progress, while the existing fallback outcome signature
uses only `bool(changed_cells)`. Progress-only synthetic events therefore produced
an unavoidable change-channel error in both arms. This makes the aggregate synthetic
test an imperfect measure of history learning. It was not repaired or used to lower
the gate after observing results; the independent public gates also failed.

Public pre-update calibration on **733 fallback transitions**:

| Game/version | Transitions | Baseline error | History error |
|---|---:|---:|---:|
| `ls20-9607627b` | 242 | 0.012371 | 0.011059 |
| `vc33-5430563c` | 183 | 0.013206 | 0.013206 |
| `ft09-0d8bbf25` | 3 | 0.083333 | 0.083333 |
| `cn04-2fe56bfb` | 157 | 0.088652 | 0.090415 |
| `su15-1944f8ab` | 148 | 0.017196 | 0.017196 |

Transition-weighted mean error: **0.0301825 → 0.0301270**, a **0.18% reduction**,
below the required 5%. Largest per-game regression was 1.99% on `cn04`.
The very small `ft09` sample provides little calibration evidence.

Across **30 game runs and 3,000 actions**, both arms completed **two levels**:
`vc33` completed **1 / 0 / 1** levels for seeds 0/1/2 in both arms; the other four
games completed zero in every run. Every game run consumed its 100-action budget.
There was no required completion gain. Baseline wall time was **9.999 s**, history
**9.712 s** (0.971×); these short audited runs are not a stable latency estimate.

Candidate validation: **22 tests passed**, formatting/lint passed, notebook generated,
and all 10 embedded Python modules matched source and compiled. After removal:
**15 baseline tests passed**, formatting/lint and the same packaging checks passed.

## Decision and follow-up

Retain the research record; reject the candidate. This result does not rule out
history-dependent models generally. It provides no evidence to retain this particular
previous-action fallback on the tested budget and public games. Only F was tested;
no broader ablation sweep was needed after the retention gates failed.

Before another history-model experiment, make the prediction/observation definition
of scene change consistent and validate the synthetic fixture against that contract.
Then test richer history only if calibration on separate trajectories supports it.
These are cached public-game pilot results, not held-out benchmark or official
Relative Human Action Efficiency claims.

Raw evidence is gitignored under `experiments/results/2026-09-18-action-history/`:
preregistered protocol, synthetic records, public summaries, six run logs and JSON
files containing every shadow forecast, calibration summary, validation logs, game
hashes/dependency versions in `manifest.json`, and the removed candidate and runner
in `candidate.patch`. The local archive can reproduce the experiment by applying
its patch to the base revision and running `experiments/run_action_history.py` with
the repository virtual environment. The archive is not included in this branch.

Archived candidate patch SHA-256: `a8e5c89774e22e384774ac38673003fff216b94ba6aa12015afcc839a16faa6d`.
