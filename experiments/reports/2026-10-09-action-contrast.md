# Action-contrast exploration — 2026-10-09

Decision: **reject the implementation; merge this research record**. The candidate
passed supplied-evidence synthetic gates but never activated during public decisions.
Completion remained 2 → 2. Archived and removed the candidate, tests and runner.

## Hypothesis and preregistration

Hypothesis: comparing action-dependent outcome distributions distinguishes
controllable effects from shared visual noise, improving full-agent exploration
beyond baseline and October 6 raw scene-change curiosity. These observational
contrasts do not establish causality under hidden-state confounding.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected clean checkout, fetched
origin/upstream, main plan/history, remote daily/research branches, prior memory and
recent reports. GitHub public API returned no open PRs. No unmerged mechanisms,
parameter retuning, game-source design access or competition submission.

Candidate reads the existing bounded transition deque. At the exact current
fingerprint, currently legal distinct ActionKeys each need three observations;
at least two must qualify. Exclude RESET/undo. Compare each next-fingerprint
distribution with the equally weighted mixture of the other eligible actions using
total variation distance, then multiply by its non-self-transition frequency. Add
`1.4 × contrast × action_novelty × (1 − predicted_failure_risk)` to C/E/F selection.
Unsupported contexts receive zero; duplicate click candidates do not multiply
comparison weight. Hypotheses, world model, planner, identities, proposals, adapter
and RNG remain unchanged. Comparison arms: exact baseline and October 6 raw effect.

All retention gates fixed before measurement:

- 100 paired four-action synthetic graphs, 24 sampled demonstrations per action:
  distinct-effect accuracy >=90%, >=40 percentage points above baseline and >=20
  above raw effect. Shared-noise mean contrast <=0.25; balanced identical outcome
  distributions numerically zero; unsupported contexts zero.
- Known progress and hazard controls: baseline >=95/100 correct, candidate loss
  <=5 percentage points. Distinct useless effect is an adversarial diagnostic only.
- Five cached official public games, F, seeds 0/1/2, 100 actions: >=1 extra level
  over both comparison arms, no per-game summed loss versus baseline, warm runtime
  <=2x. Rotate three-arm execution order by seed.
- Format/lint/unit tests and notebook generation/source equality/compilation pass.

## Synthetic evidence

One action samples uniformly from four distinct targets; three actions share four
noise targets. Each receives 24 independently sampled observations, reused across
arms. Label/target RNG `20261009 + seed`; policy seeds 0–99. All agents receive the
same transition/model/hypothesis evidence. Supplied visual outcome signatures are
identical except progress/failure controls; contrast uses exact destination identity.

| Fixture | Baseline correct | Raw effect correct | Contrast correct |
|---|---:|---:|---:|
| Distinct effect | 24/100 | 24/100 | 100/100 |
| Known immediate progress | 100/100 | 100/100 | 100/100 |
| Known progress plus distinct hazardous action | 100/100 | 100/100 | 100/100 |
| Distinct useless effect, unobserved designated goal | 28/100 | 28/100 | 0/100 |

Shared-noise mean contrast **0.166389** passes <=0.25. Finite samples yield positive
contrast without a real action difference. Arbitrary designated-label choices are
24/24/30 in that symmetric control, not goal-solving evidence. Balanced identical
distributions give zero within floating-point tolerance. The initial equality test
failed at `8.33e-17`; changed only the assertion to absolute `1e-15` tolerance.
No policy or threshold changed after measurement.

Synthetic retention gates pass. The useless-effect diagnostic shows that
identifiability alone cannot certify usefulness: the candidate always selects the
distinct distractor when no reward evidence identifies the designated alternative.
These are supplied transition graphs with synthetic outcome summaries, not online
solves, causal identification, independent ARC tasks or 1,500 independent trials.
The hazard control also supplies positive evidence for the safe action.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3. Primary cohort:
**45 runs / 4,500 actions**. Entries list seeds 0/1/2.

| Game/version | Baseline levels | Raw effect levels | Contrast levels |
|---|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/0 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 | 0/0/0 |

Totals **2 / 1 / 2** fail completion. Exact repeats **687 / 437 / 687**;
same-fingerprint/no-positive-progress transitions **595 / 353 / 595**. All 15
contrast action/outcome trajectories equal baseline. All 15 baseline trajectories
and selected scores reproduce October 8; all 15 raw-effect trajectories and selected
scores reproduce October 6 (score tolerance `1e-12`).

**Zero eligible contrast decisions in every arm and game.** An independent audit
rebuilt action counts before every recorded selection and verified the legal
candidate support threshold. Final baseline/contrast records contain 38 source
states with multiple observed actions and six with two actions observed three times.
That retrospective support was never available at a subsequent eligible decision.
Raw effect has 50 multi-action sources and no supported pairs even at run end.
Repeated actions alone do not supply comparator evidence; ft09 repeats all fall
under one coarse ActionKey.

Initial elapsed totals baseline/raw/contrast: **36.061 / 12.766 / 15.239 seconds**;
first baseline subprocess took 27.420 s. Warm replay: **19.417 / 13.381 / 50.615 s**
(contrast/baseline **2.607x**, also fails the runtime gate). The warm contrast seed-2
subprocess alone took 40.722 s versus 4.064 s initially; warm baseline seed 1 took
10.936 s versus 4.765 s initially. Timing includes subprocess startup, file I/O and
equal shadow auditing, and is unstable; do not infer an isolated algorithm slowdown
or speedup. Completion and activation evidence already determine rejection.

All 45 public traces and all 1,500 synthetic records exactly replay. Additional
4,500 public actions are deterministic replay, not independent observations.
No held-out access, official RHAE result or submission is claimed.

## Validation and disposition

Candidate **32 tests passed** (17 added cases): evidence support, common noise,
equal action weighting, self-transition scaling, source/legality isolation,
coordinate duplication, RESET/undo exclusion, bounded eviction, ablation/RNG
contracts and failure suppression. Format/lint and all **10** notebook module
source/compile checks passed. Final test source hashes are archived separately;
the initial manifest predates the numerical-tolerance correction.

Archived patch/source/tests/runner, then restored production. Final **15 tests**,
format/lint and all **10** notebook checks pass; production matches main. Forward
and reverse patch applicability checked. Only this report and the plan are committed.

Reject passive same-state outcome contrast under these budgets. Before another
contrast estimator, establish that affordable matched action experiments create
comparison data at states the policy actually revisits. Any active acquisition
proposal needs its own action-cost, hidden-state and useless-distractor controls.

Ignored local evidence: `experiments/results/2026-10-09-action-contrast/` contains
protocol, source/dependency/game manifests, raw/warm traces, audits, validation and
`candidate.patch`. Raw evidence is not pushed. Patch SHA256:
`e8f7aca31f80c6dab0c8a9264995735d97f3584c11424c335bcc10ab2df3b957`.
Reproduce by applying the patch to the base and running
`experiments/run_action_contrast.py --output experiments/results/action-contrast-replay`
with recorded dependencies, cached games, copied protocol and writable
`MPLCONFIGDIR`/`XDG_CACHE_HOME`. Broader ablations were conditional on F passing.
