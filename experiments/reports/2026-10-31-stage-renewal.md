# Progress-boundary model renewal — 2026-10-31

Decision: **reject the implementation; merge this negative research record**.
Renewal adapts faster after a synthetic rule switch but discards useful knowledge
when rules persist. It destroys delayed-action control performance and adds no
public completions. Candidate code, tests and runner were archived under ignored
results and removed before committing; production matches main.

## Hypothesis and preregistered criteria

Hypothesis: an observed level-completion event identifies a useful causal-context
boundary. Renewing learned action-effect rules then prevents negative transfer
into changed levels and improves completion. This differs from October 13's
contradiction-driven forgetting within a state/action and October 8's visible-state
hypothesis conditioning: the boundary is an external progress signal, with no
contradiction detector or learned threshold.

Four arms: baseline, hypothesis renewal, empirical-model renewal, joint renewal.
Before implementation or measurement, the saved protocol required all of:

- Switched-rule synthetic fixture, 200 paired seeds, 32-action cap: joint solves
  at least 95% and reduces mean capped actions at least 20% against baseline.
- Unchanged-rule and competing-action four-hit controls: baseline solves at
  least 95% in each; joint loses at most five percentage points and costs at most
  1.25x baseline. A missing-boundary fixture is diagnostic.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one additional
  joint level, no per-game summed regression, warm subprocess time at most 2x
  baseline. Components are attribution controls, not post-result alternatives.
- Passing unit tests, format/lint, notebook embedded-source equality/compilation,
  independent trace audit and deterministic replay. A–E expansion conditional
  on all F gates passing.

No criteria, fixtures or policy parameters changed after measurement.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation
memory, freshly cloned main, remote daily/research branches, history, research
plans, prior report introductions and relevant full reports. Connected GitHub
search found no open PRs. The original cloud-backed checkout had read timeouts
and five reported modified paths; its tracked files were left untouched. An
isolated temporary fork clone was used. No game implementation informed design.

After recording a successful transition, renew only when `levels_completed`
increased and state is `NOT_FINISHED`, and only for F. Recreate the hypothesis
engine and/or empirical model; update adapter, selector and planner references.
Preserve the hypothesis ID counter so logs do not reuse IDs. Retain novelty and
episodic memory, previous diff, perception, proposals, weights, RNG and planner
settings. Do not renew on reset alone, nonpositive progress, WIN or GAME_OVER.
No old model bank, new dependency, or other rejected mechanism is included.

## Synthetic results

Each seed permutes four keyboard labels with seed `20261031 + seed`. Supplied
prior-level history contains eight no-op observations per action, followed by
one successful action[0] with visible scene change and progress. This is the
first renewal event. The next stage rewards action[1] for switched rules,
action[0] for unchanged rules, or four consecutive action[0] presses for the
competing-action delay control. A diagnostic uses switched rules but zero
boundary progress. Every arm receives identical supplied history and then
learns online. Policy seeds are 0–199. Cells show solves out of 200 / mean
capped actions, measured only after the supplied boundary.

| Fixture | Baseline | Hypotheses | Model | Joint |
|---|---:|---:|---:|---:|
| Switched rule | 200 / 6.98 | 200 / 4.995 | 200 / 6.98 | 200 / 3.58 |
| Unchanged rule | 200 / 1 | 200 / 1 | 200 / 1 | 200 / 6 |
| Unchanged, four consecutive hits | 200 / 4 | 0 / 32 | 200 / 4 | 0 / 32 |
| Switched, no boundary signal | 200 / 7.99 | 200 / 7.99 | 200 / 7.99 | 200 / 7.99 |

Joint adaptation improves **48.71%**, passing the primary gate. Both preservation
controls fail: immediate cost rises sixfold, while delayed solves fall from
100% to zero despite a fully competent baseline with competing actions. Hypothesis
renewal alone causes the delayed failure; model renewal alone matches baseline
in these fixtures. The missing-boundary trajectories match exactly across arms.
A level boundary does not establish that the action-effect rules changed.

These are four designed supplied-history families and label permutations, not
independent ARC tasks or evidence of initial-level acquisition. Equal no-op
training and the retained novelty counters affect the ranking after renewal.

## Public results

Official cached OFFLINE engine: arc-agi 0.9.9, arcengine 0.9.3; framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. All ten cached game/metadata and
thirty harness Python hashes match October 30. Arm order rotates by seed.
Primary cohort: **60 runs / 6,000 actions**. Entries list seeds 0/1/2.

| Game/version | Baseline | Hypotheses | Model | Joint |
|---|---|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| Metric | Baseline | Hypotheses | Model | Joint |
|---|---:|---:|---:|---:|
| Completed levels | 2 | 2 | 2 | 2 |
| Renewal events | 0 | 2 | 2 | 2 |
| Equal-frame/nonpositive-progress outcomes | 595 | 595 | 595 | 595 |
| Consecutive identical selected actions | 746 | 720 | 746 | 720 |

Each renewal arm triggers twice, after vc33 seeds 0 and 2 complete their first
level, with 13 and 20 observations in the departing model respectively. Hypothesis
and joint renewal each change 165 selected-action positions across those two runs;
the other thirteen runs retain baseline choices. Model-only renewal preserves
all fifteen selected-action sequences. None adds another level.

Warm replay totals are 21.946 s baseline, 20.727 s hypotheses, 20.263 s model and
20.528 s joint (**0.935x** baseline). Initial totals were
20.623/20.002/19.769/20.028 s. Equal instrumentation and subprocess startup are
included; the timing is a budget check, not evidence of a production speedup.

## Verification and disposition

Candidate: **31 tests pass**, including sixteen new cases for component isolation,
non-boundaries, other ablations, unchanged policy/RNG/memory, unique hypothesis IDs,
positive level jumps and the adapter's record-before-renewal/rebinding lifecycle.
Formatting/lint and **10** notebook source/compilation checks pass. Independent
row-prefix reconstruction audits 3,200 synthetic records, 132,699 observations and
108,396 forecasts; public checks cover 60 runs, 5,952 decisions/observations and
125,964 forecasts. It verifies boundary eligibility, model-history separation,
hypothesis clearing, legal selection, raw pixel differences, supplied task outcomes
and source hashes. All fifteen baseline traces reproduce October 30 exactly,
including scores, selected actions and observations.

All 3,200 synthetic records and 60 public runs replay exactly by uncompressed
trace hashes. The additional 6,000 public actions are repeated evidence, not
independent trials. No candidate source changed between runs. After archiving
and removal, **15 baseline tests**, formatting/lint and **10** notebook module
checks pass; production matches main. Both forward and reverse patch application
checks pass.

Reject renewal based only on level completion. Any future attempt needs evidence
that specific rules became incompatible while preserving transferable rules and
competent repeated-action behavior. Do not retain this reset rule on adaptation
speed or reduced repetition alone. No held-out access, official RHAE score or
competition submission is claimed; these are repeatedly used public development
games with short budgets.

Ignored evidence: `experiments/results/2026-10-31-stage-renewal/` contains the
preregistered protocol, raw traces, source/dependency/cache manifests, audit,
replay, validation, archived candidate source and removed patch. Raw evidence is
not pushed. Patch SHA-256:
`6d50d6f847718de0eaa7b1eb25693cb01579635f9e8dbc2fda78a2de1578c316`.
Forward/reverse patch checks pass. To reproduce, apply the patch to the base,
copy the protocol to its expected ignored directory, and run `.venv/bin/python
experiments/run_stage_renewal.py --output <fresh-directory>` with the recorded
dependencies/cached games and writable plotting/cache directories. Only this
report and the research-plan entry are committed.
