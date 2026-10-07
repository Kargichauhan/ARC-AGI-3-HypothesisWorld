# Joint-outcome planning — 2026-10-07

Decision: **reject the implementation; merge the research record**. Averaging
complete outcomes fixes supplied stochastic route decisions, but public completion
remains two levels. Candidate, tests, controls and runner were archived and removed
before committing. Production matches main.

## Hypothesis and fixed gates

Hypothesis: averaging observed outcomes within an action before choosing between
actions, while stopping continuation at terminal outcomes, improves stochastic
route selection and public completion beyond the prior reward-only planner.

Four-arm factorial: **baseline** (exact main), **utility** (September 23 future
progress/failure), **outcomes** (joint averaging and terminal masking, without
future utility), and **joint** (both). No state abstraction or other rejected policy
was incorporated. This tests an extension of the earlier utility pilot rather than
attributing its gains to averaging. Preregistered before measurement:

- Three supplied-model route fixtures, 100 label permutations each: joint at least
  95 correct per fixture; pooled gains at least 50 percentage points over baseline
  and 25 over utility alone.
- Two positive controls: baseline at least 95/100, joint loss at most five points.
  Exact neutral deterministic-graph parity; passing tests and packaging.
- Five cached public games, F, seeds 0/1/2, 100 actions: joint at least one additional
  level over **both** baseline and utility, no per-game summed loss versus baseline,
  and warm total subprocess runtime at most 2x baseline.
- Remove candidate if any retention gate fails. Broader A–E public runs conditional
  on F passing. No parameters or gates tuned after results.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Clean checkout; fetched origin,
reviewed main, remote daily/research branches, plan, history, recent reports and
prior memory. No open PRs. No game source inspected to design the mechanism.

## Mechanism

Group the existing bounded 512 transition records by source fingerprint and action,
retaining joint target/progress/terminal observations. Future action value is mean
`2*positive_progress - 2.2*failure + nonterminal*(target_novelty + .55*V(target))`;
maximize action means. WIN/GAME_OVER receive no novelty or continuation. Root value
averages its outcomes under the existing modal-confidence gate .68 and outer
confidence multiplier; retain immediate progress and leave root risk to the selector.
Preserve horizon two, nonterminal repeated novelty/leaf credit, identities, hypotheses,
proposals, selector weights, legal-action handling and RNG. The adapter supplies
its configured risk coefficient.

The bounded graph can forget data retained by the baseline model; all measured
graphs fit 512 records, avoiding that confound here. The retained root confidence
gate can still exclude multimodal transitions. This is an empirical finite-horizon
backup experiment, not a calibrated stochastic control guarantee.

## Synthetic evidence

Graphs supply memory/model evidence to the full selector, with equal cold hypothesis
priors and equal root action counts. Action labels use seeds `20261007+i`, marker
positions `7102026+i`, and policy seeds 0–99. Hand-calculated expected values check
every joint score. These are five designed structures, not 2,000 independent ARC
tasks or online solve trials.

| Correct choices / 100 | Baseline | Utility | Outcomes | Joint |
|---|---:|---:|---:|---:|
| Reward spread across multiple targets | 0 | 0 | 47 | 100 |
| Same target, mixed fatal/live outcomes | 0 | 100 | 100 | 100 |
| Minority root branch reaches known reward | 0 | 0 | 0 | 100 |
| Aligned deterministic goal control | 100 | 100 | 0 | 100 |
| Immediate known goal control | 100 | 100 | 100 | 100 |

The first fixture contrasts certain progress split across two destinations with
75% progress concentrated at one destination; max-edge confidence underweights the
better mean. The second mixes three failures and one live outcome at one fingerprint.
The third gives a root action an 80% dead branch and 20% known reward continuation.
Joint passes all synthetic gates: primary gains are 100 points over baseline and
66.67 over utility. Outcomes alone loses the aligned control because terminal
masking removes novelty without supplying future reward; do not retain it alone.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9 / arcengine 0.9.3. Primary cohort:
**60 runs / 6,000 actions**, four arms in cyclic order by seed. All four arms have
identical per-game completion; entries are seeds 0/1/2.

| Game/version | Levels in every arm |
|---|---|
| ls20-9607627b | 0/0/0 |
| vc33-5430563c | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 |
| su15-1944f8ab | 0/0/0 |

Both completion-improvement gates fail. Repeated exact actions are
**687/686/687/686** for baseline/utility/outcomes/joint; no-op counts are **595**
in every arm. Joint changes only two public action choices from baseline:

- vc33 seed 1, selection index 98: utility and joint avoid the same learned future
  failure, reproducing the prior reward-only effect.
- cn04 seed 1, index 82: outcomes and joint raise ACTION5's planning value from
  .308750 to .379792 and select it over ACTION4; completion stays zero.

After the actual root confidence gate, each arm has 32 decisions with reachable
stochastic future actions, one with a future terminal failure, and zero with future
positive reward. No eligible root action is stochastic or terminal. Averaging can
change novelty values, but these trajectories offer no downstream reward to exploit.
Broader ungated trace counts report 56 stochastic decisions; these are not eligible
planner counts. All 300 joint ft09 outcomes remain no-ops.

All 15 baseline traces exactly match October 6's warm baseline, including scores,
actions and outcomes. Replay reproduces all 60 public traces and all 2,000 synthetic
records exactly. Its extra 6,000 actions are not independent evidence.

Initial subprocess totals: **42.639/28.004/10.148/9.848 s**. Warm totals:
**22.361/11.288/11.571/10.600 s** (joint/baseline .474x), including equal shadow audits
and process startup. Timing remains startup-confounded: baseline seed 0 takes
36.252 s initially and 15.808 s on replay, versus about 3.3 s for later baseline
processes. The observed ratio is below the gate but supports no speedup claim or
isolated production-runtime estimate. Completion decides rejection regardless.
No held-out evaluation, official RHAE measurement or competition submission occurred.

## Validation and disposition

Candidate: **26 tests passed**, including 11 new cases for joint averaging,
terminal/live targets, absorbing roots, expectation weighting, confidence, expiry,
configured risk, maximizing actions, the factorial control and 100 deterministic
neutral graphs over horizons 1–4. Format/lint and **10** notebook module source/
compilation checks passed. After removal: **15 baseline tests** and the same checks
passed. Patch forward/reverse checks passed; agent, tests, scripts and notebook
settings match main.

Reject the implementation. Establish that reachable learned rewards recur under
the agent's observation/action identities before extending backups of reward-free
graphs. Any representation-plus-planner retry needs a separate factorial and
false-alias controls; supplied-model gains do not justify relaxed completion gates.

Ignored evidence: `experiments/results/2026-10-07-joint-outcome-planning/` contains
protocol, traces, manifests, dependencies, audits, validation, candidate sources and
`candidate.patch`. Raw evidence is not pushed. Patch SHA-256:
`49f4f9e84b2b84bcf878a0b3154a49a80029219a3058ab06f91fa18fe75853d6`.
Reproduce by applying the patch to the base, copying the protocol to an ignored
output directory and running `experiments/run_joint_planning.py --output <directory>`
with recorded dependencies/cached games and writable plotting/cache directories.
Only this report and the research-plan note remain on the branch.
