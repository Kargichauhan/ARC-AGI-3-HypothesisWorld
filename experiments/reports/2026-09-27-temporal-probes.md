# Bounded temporal probes — 2026-09-27

Decision: **reject the implementation; merge this research record**. Three-attempt
interventions solved the designed hidden-delay task, but did not add public levels
and harmed an alternating-action control. Archived and removed the controller,
adapter changes, tests and runner before committing.

## Hypothesis and preregistration

Hypothesis: committing briefly to an apparently ineffective action reveals hidden
accumulated effects that single-step selection misses, improving completion.
Unlike September 22's probe deferral, this deliberately persists with an intervention;
unlike September 18's action-history fallback, it changes execution, not prediction.

F-only wrapper: on first selection of a fingerprint/exact-action context, execute
up to three consecutive attempts. Continue only after identical fingerprint, no
observable change or progress, and `NOT_FINISHED`. Release after any other outcome,
lost candidate legality, changed source or reset. Exclude RESET and ACTION7; retain
512 tried contexts FIFO, clear on reset. Coarse action keys still drive the original
learning and scores, but controller identity includes exact click coordinates.
No new proposals, model, hypothesis, planner, score or RNG changes. Ranking remains
visible in logs even when commitment selects a lower-ranked action.

All retention gates were written before implementation or measurement:

- Four-action hidden-delay fixture: at least 95/100 solves, at least 20 percentage
  points more solves, and at least 20% lower mean capped actions.
- Matched one-hit control: baseline at least 95/100 solves, candidate solve loss at
  most five points and mean capped action cost at most 2x baseline.
- Release on visible intermediate effects; report alternating-sequence performance
  as an adversarial diagnostic without a post-hoc numerical gate.
- Five cached official public games, F, seeds 0/1/2, 100 actions: at least one extra
  level, no per-game summed completion loss, warm runtime at most 2x.
- Passing tests, format/lint, notebook generation and embedded-source compilation.

Base `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Fetched origin; main unchanged;
GitHub connector reported no open PRs. Inspected clean checkout, remote daily/research
branches, history, main/current plans and recent evidence. No unmerged mechanisms,
parameter retuning or game-source inspection to design the policy.

## Synthetic evidence

100 paired seeds per fixture, 24-action cap. Fixture RNG `20260927 + seed` permutes
four action labels; policy seeds 0–99. Hidden-delay success requires three consecutive
target hits; other actions reset the streak. Immediate requires one hit. Visible
uses the same three-hit rule but displays the streak. Alternating requires target,
second label, target. Both arms receive identical transition observations.

| Fixture | Baseline solves | Candidate solves | Baseline mean actions | Candidate mean actions |
|---|---:|---:|---:|---:|
| Hidden delay | 0/100 | 100/100 | 24.00 | 8.25 |
| Immediate | 100/100 | 100/100 | 3.61 | 6.25 |
| Visible intermediate | 0/100 | 29/100 | 24.00 | 20.52 |
| Alternating sequence | 22/100 | 8/100 | 21.31 | 23.49 |

Hidden-delay capped actions fell **65.63%**, passing the synthetic gate. Paired
savings 15.75 actions, bootstrap 95% interval [15.15,16.38]; all 100 pairs improve.
Immediate cost increased **73.13%**, within the permissive 2x control gate but a
substantial drawback (68 worse, 32 ties). Alternating solves fell 14 points; mean
cost rose 2.18 actions, bootstrap 95% interval [1.09,3.35]. Visible-effect release
passes unit tests; low visible-fixture competence prevents a broad sequence claim.

These are four designed environments with label permutations, not 400 independent
ARC tasks. The fixed three-attempt budget directly matches the hidden-delay rule;
it does not demonstrate learning unknown delays or identifying latent causal state.

## Public evidence

Official cached OFFLINE engine, arc-agi 0.9.9 / arcengine 0.9.3. Primary cohort:
**30 runs / 3,000 actions**, alternating arm order by seed. Entries list seeds 0/1/2.

| Game/version | Baseline levels | Candidate levels |
|---|---|---|
| `ls20-9607627b` | 0/0/0 | 0/0/0 |
| `vc33-5430563c` | 1/0/1 | 1/0/1 |
| `ft09-0d8bbf25` | 0/0/0 | 0/0/0 |
| `cn04-2fe56bfb` | 0/0/0 | 0/0/0 |
| `su15-1944f8ab` | 0/0/0 | 0/0/0 |

Levels **2 → 2** fail the primary retention gate. Repeated exact actions **687 → 674**;
same-fingerprint/no-positive-progress outcomes **595 → 567**. Commitment overrides
the instantaneous top-ranked choice only **22** times on candidate histories:
13 in ft09, seven in cn04, two in su15. All 300 candidate ft09 outcomes remain no-ops.
This does not establish whether longer or different sequences could help.

All 15 baseline trajectories exactly reproduce September 26's warm scores, selected
actions, levels and transitions. Baseline uses the same wrapper with commitment
disabled; this parity checks the adapter instrumentation against prior main behavior.

Initial elapsed totals 31.110 s baseline / 9.591 s candidate are startup-confounded:
first baseline subprocess took 24.597 s. Warm replay totals **9.955 s → 9.598 s
(0.964x)**, including startup and equal tracing. All 30 public traces and all 800
synthetic records reproduce exactly. Additional 3,000 public actions are deterministic
replay, not independent evidence. No held-out access, official RHAE result or
competition submission is claimed.

## Validation and disposition

Candidate **29 tests passed**, including 14 new cases for burst limits, exact click
identity, legality, visible/progress/terminal cancellation, bounded memory, reset,
disabled parity and actual adapter terminal-observation consumption. Format/lint and
all **11** notebook module source/compile checks passed. An adapter test was added
during the initial benchmark; policy/runner hashes did not change, and the warm
manifest captures final test source. No parameter or gate changed.

After removal: **15 baseline tests**, format/lint and all **10** notebook module
source/compile checks passed. Production agent, tests, scripts and notebook settings
match main. Broader public ablations were conditional on F passing and were not run.

Reject unconditional short-burst commitment. Matching a known delayed fixture is
insufficient when one-step efficiency degrades, alternating sequences regress, and
public completion remains unchanged. Future temporal work should distinguish
repeat-required from switch-required contexts using evidence, and require a competent
alternating control before claiming general sequence improvement.

Ignored evidence: `experiments/results/2026-09-27-temporal-probes/` contains protocol,
raw choices/outcomes, manifests, public/warm traces, audits, validation and
`candidate.patch`. Raw evidence remains local and is not pushed. Patch SHA-256:
`5d43227140826e5388baba189532c3d4431a2fdec15b582a052f28749a9a6eba`.
Forward and reverse applicability were checked.

Reproduce by applying the archived patch to the base, copying the protocol into an
ignored output directory, and running `experiments/run_temporal_probes.py --output
experiments/results/temporal-reproduction` with recorded dependencies/cached games
and writable `MPLCONFIGDIR`/`XDG_CACHE_HOME`. Only this report and the plan remain.
