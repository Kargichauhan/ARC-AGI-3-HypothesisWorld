# Evidence-sensitive transition confidence — 2026-09-24

Decision: **reject the candidate; retain this research record**. Reserving confidence
for unseen outcomes improved synthetic exploration, but public completion stayed at
two levels and public predictive calibration worsened. Candidate code, tests and
runner were archived locally and removed before committing.

## Hypothesis and preregistration

Hypothesis: a conservative unseen-outcome prior prevents sparsely observed transitions
from monopolizing planning, improving prediction, exploration and public completion.
Baseline modal-target confidence is `count / total`, including confidence 1 after one
observation. The candidate used `count / (total + 2)` for local predictions and known
planner edges. Five deterministic observations now pass the existing 0.68 gate.

This reserves mass for unseen outcomes; it is not a calibrated posterior over a known
outcome vocabulary. Progress, risk, change estimates, global fallback, state/action
identities, hypotheses, proposals, planner rewards and RNG remain unchanged. This
is distinct from the prior state-alias penalty and path-exclusive novelty pilots.

All preregistered retention gates were required:

- At least 20% lower modal-target Brier loss after one training observation on two
  stochastic generators (target probabilities 0.5 and 0.75), each with 200 seeds and
  100 held-out outcomes per seed.
- At least 95/100 online four-action discovery solves and 15% lower mean capped
  actions; one random successful action, three no-ops, 20-action limit. A learned
  route control and an immediate-progress control require baseline accuracy at
  least 95/100 and candidate loss at most five percentage points.
- At least one extra public level without any per-game summed regression, and no
  more than 2x audited runtime: five cached games, F, seeds 0/1/2, 100 actions each.
- Passing unit tests, formatting/lint, notebook generation and embedded-source checks.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Origin was fetched; main was
unchanged and no PRs were open. Inspected research/daily branches, history, plans and
prior experiment evidence. No unmerged mechanism was included and no game source was
read to design the candidate. Parameters and gates were not tuned after results.

## Results

| Synthetic diagnostic | Baseline | Candidate |
|---|---:|---:|
| Mean held-out Brier loss | 0.425250 | 0.302694 |
| Discovery solves / 100 | 100 | 100 |
| Mean discovery actions | 3.06 | 2.39 |
| Learned route choices correct / 100 | 100 | 100 |
| Immediate-progress choices correct / 100 | 100 | 100 |

Prediction loss fell **28.82%**; discovery actions fell **21.90%**. Paired action
savings were 0.67, bootstrap 95% interval [0.50, 0.85]; 43 better, 57 ties, zero
worse. RNG was `20260924 + seed`, policy RNG `seed`. Both arms used identical
training observations, targets and label permutations. Calibration has 40,000
held-out outcomes but only 400 training draws; outcomes within a fixture share a
fitted prediction. These are designed mechanisms, not independent ARC tasks.

The learned-route control demonstrates both actions 20 times and favors the
less-visited destination (visits 1 versus 100). The immediate-progress control uses
one demonstration per action and equal destination visits. These controls test
retained demonstrated choices, not hidden-state or delayed-effect competence.

Public primary cohort: **30 runs, 3,000 actions**, installed official OFFLINE engine,
arc-agi 0.9.9 / arcengine 0.9.3. Entries list levels for seeds 0/1/2.

| Game/version | Baseline | Candidate |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Completion **2 → 2** fails the gate. Repeated exact actions fell **687 → 306**;
same-frame/no-positive-progress transitions fell **595 → 475**. Decisions with
nonzero planning values fell **766 → 237**; all 237 candidate planning activations
were in `ft09`, where every observed transition still had no visible change.
Repeated deterministic no-ops eventually overcome the confidence prior.

Shadow models forecast before learning from the same baseline-policy transitions:

| Game | Local forecasts | Baseline Brier loss | Candidate Brier loss |
|---|---:|---:|---:|
| `ls20` | 58 | 0.000000 | 0.170773 |
| `vc33` | 114 | 0.000000 | 0.444444 |
| `ft09` | 297 | 0.000000 | 0.015559 |
| `cn04` | 140 | 0.671429 | 0.247421 |
| `su15` | 146 | 0.102740 | 0.103115 |
| **Pooled** | **755** | **0.144371** | **0.152167** |

Public loss worsened **5.40%**. For the 274 forecasts with exactly one prior sample,
loss worsened **0.295620 → 0.345904**. All 114 `vc33` forecasts were single-sample
predictions and correct. The blanket prior underestimates their reliability, while
helping unreliable pooled predictions in `cn04`. This audit was diagnostic, not an
additional retention gate, and excludes fallback forecasts with no predicted target.

All 15 baseline trajectories exactly reproduce September 23 recovery, including
scores, choices and transitions. Initial times were 30.154 s baseline / 9.682 s
candidate; baseline seed 0 alone took 24.279 s, so these are startup-confounded.
A warm repeat reproduced all 30 traces and every synthetic record exactly:
**9.411 s → 9.170 s (0.974x)**. This adds 3,000 replay actions, not independent
completion evidence. Times include subprocess startup and equal shadow auditing.

Candidate validation: **21 tests passed** (six new cases and one updated confidence
expectation), format/lint passed, and all **10** notebook modules matched source
and compiled. After removal, **15 baseline tests**, format/lint and the same
packaging checks passed. Production source, tests and scripts match main.

## Decision and reproduction

Merge the research record; reject this uniform confidence prior. Predictability and
exploration value should be measured separately: reliable no-ops remain unproductive,
and sparse transitions are not uniformly unreliable. Before another confidence
penalty, audit reliability conditional on action pooling and observation context on
separate trajectories. Do not retain this rule on repetition reduction alone.

These short cached public-game pilots provide no held-out benchmark or official
Relative Human Action Efficiency claim. A–E parity checks were conditional on F
passing, so no broader sweep was run. No submission or PR merge was made.

Ignored local evidence under `experiments/results/2026-09-24-evidence-confidence/`
contains the protocol, synthetic records, public logs/traces, source/game/dependency
manifest, pre-update calibration and cross-day audits, warm repeat, validation and
removed `candidate.patch`. Raw evidence is not pushed. Patch SHA-256:
`07e4d8202e1569cbe99738a6ce23c709bbb4d28f4c8c771a6360f8effbe2447d`.

Apply that patch to the base revision and run
`experiments/run_evidence_confidence.py --output experiments/results/confidence-reproduction`
with the recorded dependencies, cached games and writable plotting/cache directories.
Copy the protocol to the output directory to include its hash in the manifest.
Patch forward/reverse applicability was checked. Only this report and the plan remain.
