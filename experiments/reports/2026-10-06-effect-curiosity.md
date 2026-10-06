# Effect-based exploration — 2026-10-06

Decision: **reject the implementation; merge the research record**. Exposing
predicted scene change to selection improved designed sequence tasks, but public
completion regressed from two levels to one. Candidate code, tests and runner were
archived locally and removed before committing.

## Hypothesis and fixed gates

Hypothesis: predicted observable effects guide exploration toward sparse-reward
sequences better than disagreement and novelty alone, improving completion.
Add `1.4 * (2*p_change - 1) * action_novelty * (1-p_failure)` to C/E/F scores,
excluding RESET and undo. Unseen predictions (`p_change=.5`) are neutral; the
existing novelty discounts repeated actions. Log the signed contribution.
Models, local/global prediction precedence, hypotheses, reward/risk weights,
planner, proposals, identities and RNG are unchanged. This is effect seeking,
not causal identification or an empowerment estimator. No prior rejected feature
was incorporated and no parameters or gates were tuned after measurement.

All gates were preregistered:

- Untrained four-action corridors, lengths 3/6, 100 paired permutations each,
  40-action cap: at least 95 candidate solves per length and at least 20% lower
  pooled capped action cost.
- Matched irrelevant-flicker controls: solve loss at most five percentage points
  per length and pooled cost at most 1.25x baseline.
- Demonstrated immediate-goal/visible-distractor/fatal-action control: baseline
  at least 95/100 correct first choices, candidate loss at most five points.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one extra level,
  no per-game summed loss, and warm runtime at most 2x baseline.
- Passing tests, format/lint, notebook source equality and compilation.

Three-consecutive-hit hidden goals were diagnostic only. Broader A–E public runs
were conditional on F passing. Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`.
Fetched origin; main unchanged and no open PRs. Reviewed remote research/daily
branches, main plan, history, recent reports and October 4 local negative evidence.
Branch starts directly from main; no game source was read to design the policy.

## Synthetic evidence

One action advances a marker, the others are no-ops. Flicker replaces one no-op
with a task-irrelevant colour-bit toggle. Action labels are shuffled by
`20261006 + seed`, policy seeds 0–99. Both arms learn online through the same
`diff_states`/memory/model/hypothesis pipeline, including terminal observations.
The known-goal control demonstrates all four actions once at the current state;
it includes one goal, a visible distractor and a fatal action. Baseline uses the
same candidate implementation with effect coefficient zero.

| Fixture | Solves, baseline → candidate | Mean actions, baseline → candidate |
|---|---:|---:|
| Corridor, length 3 | 100 → 100 | 12.37 → 4.87 |
| Corridor, length 6 | 100 → 100 | 34.53 → 7.87 |
| Flicker, length 3 | 100 → 100 | 12.14 → 7.24 |
| Flicker, length 6 | 100 → 100 | 30.46 → 10.24 |
| Known goal/hazard, one choice | 100 → 100 | 1.00 → 1.00 |
| Hidden three-hit goal | 0 → 21 | 40.00 → 33.00 |

Corridor pooled cost falls **72.84%**; flicker cost falls **58.97%**. All synthetic
retention gates pass. Every corridor/flicker pair improves. Paired mean savings
bootstrap 95% intervals: corridor-3 [6.97,8.03], corridor-6 [26.45,26.87],
flicker-3 [4.32,5.50], flicker-6 [19.57,20.87]. Ten thousand seeded resamples.

These six fixture/length combinations with label permutations are not 1,200
independent tasks. A single productive action works at every corridor position;
visible effects correlate strongly with eventual progress. The flicker has only
two states and does not test endlessly novel visual distractions. Hidden-goal
competence remains poor; its 21 solves support no general latent-state claim.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9 / arcengine 0.9.3. Primary cohort:
30 runs / 3,000 actions, alternating arm order by seed. Entries are seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/0 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Completion **2→1** fails both public completion gates. Repeated exact actions
fall **687→437**, and same-frame/no-positive-progress outcomes fall **595→353**.
Removing the effect term from the current candidate ranking changes its top choice
at 866 decisions; this conditional diagnostic is not an estimate of causal gain.
Unlike yesterday's policy-disconnected predictions, this intervention changes
behavior substantially and still harms completion.

In vc33, all three paired trajectories first diverge at selection index 1.
For seed 2, one prior visible effect gives a pooled colour/region action a **1.05**
bonus despite zero predicted progress, moving its score to **2.7691** above an
untested action's **1.8017**. The candidate finishes with zero levels versus one
for baseline. This identifies the first policy divergence, not a proof that this
single action alone caused the final loss. All 300 candidate ft09 outcomes remain
no-ops. Reduced repetition or increased visible change is insufficient evidence
of goal-directed improvement.

All 15 baseline traces exactly reproduce October 5's warm baseline, including
scores, selected actions and transitions. Initial timing **33.912→9.429 s** is
startup-confounded: first baseline subprocess alone took 27.737 s. Warm replay:
**9.476→9.451 s (0.997x)**, including startup and equal tracing. All 30 public
traces and all 1,200 synthetic records reproduce exactly. Replay adds 3,000
actions, not independent completion evidence. No held-out benchmark, official
Relative Human Action Efficiency result, competition submission or merge claimed.

## Validation and disposition

Candidate: **28 tests passed** (13 added cases), format/lint and **10** notebook
module source/compilation checks passed. Tests cover unknown-score/RNG parity,
effect/no-op signs and accounting, novelty decay, hazard suppression, reset/undo,
all six ablations, and exact-local precedence. Initial runner import and test
helper lint fixes preceded measurements. After candidate removal: **15 baseline
tests**, format/lint and the same 10-module packaging checks passed. Production
agent, tests and scripts match main.

Reject the fixed effect bonus. Merge this negative record. Future effect-based
exploration should first distinguish reusable task affordances from incidental
change, including changing useful actions across states and inexhaustible visual
distractors. Do not combine this bonus with yesterday's relational fallback or
relax completion gates on the strength of the synthetic corridor result.

Ignored evidence: `experiments/results/2026-10-06-effect-curiosity/` contains the
protocol, synthetic/public traces, warm replay, manifests, dependencies, audits,
validation, candidate source and `candidate.patch`. Raw evidence is not pushed.
Patch SHA-256: `ccf43f2e0e451477d690c8675b63a7bc7bc7ce3d6e15d64bc9005758a3257434`.
Forward and reverse patch applicability passed. Reproduce by applying the patch
to the base, copying the protocol into an ignored output directory and running
`experiments/run_effect_curiosity.py --output experiments/results/effect-reproduction`
with recorded dependencies/cached games and writable MPLCONFIGDIR/XDG_CACHE_HOME.
Only this report and the research-plan note remain on the branch.
