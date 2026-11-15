# Evidence-based reconsideration — 2026-11-15

Decision: **reject the candidate; merge the negative research record**. Three matching
observations as an alternative to the rejection cooldown produced no changed forecasts.
The intended bottleneck was absent: exact rules were never rejected in these streams.
Candidate implementation and five tests were archived and removed; production matches main.

## Hypothesis and fixed gates

Fresh corroboration of a previously rejected rule should accelerate recovery when a
rule returns without degrading stationary stochastic predictions. Unlike October 13's
empirical forgetting and October 21's conjunctive falsification, this changes only the
hypothesis regeneration gate, retaining the original similarity and rejection criteria.

Before implementation and measurement, the protocol required >=20% lower three-event
Brier loss during the first six observations after each synthetic rule switch, with
positive baseline loss. Each stationary control must increase loss by <=.01 and both
arms must have loss <=.20. Require tests, format/lint, notebook source/compile checks
and deterministic replay. Conditional public gate: five games, F, seeds 0/1/2,
100 actions, an extra level, no per-game regression, <=2x warm runtime. A–E conditional
on F passing. No thresholds, fixtures or policy were retuned after measurement.

## Mechanism and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Read automation history,
fetched origin main/daily/research refs, inspected main plan/history and relevant
conjunctive-falsification, predictive-credibility and recent correspondence reports.
Connected GitHub search found no open PRs. Local clone/worktree attempts stalled on
cloud-file reads; a fresh shallow clone of the verified fork isolated all research.
Original tracked files were untouched. No unmerged implementation was incorporated.

Only `agent/hypotheses.py` changed: maintain the latest observed OutcomePattern and
consecutive count per exact ActionKey, capped at three and 512 keys with FIFO eviction.
Allow normal exact-pattern generation if either the existing 12-step cooldown elapsed
or the streak reaches three. Different actions have separate observation streams.
Generation beliefs, similarity, rejection, population cap and the whole policy stay fixed.
This regenerates a rule; it does not revive its old identity or erase rejection history.

## Synthetic evidence

200 paired seeds per family, 96 supplied observations each: 153,600 arm-step records.
The returning-rule fixture alternates twelve noops and twelve progress effects, with
random initial polarity. Stationary controls use Bernoulli progress probabilities
.1/.5/.9. Progress effects change one pixel and increment progress; noops do neither.
These are injected StateDiff streams, not game episodes. Deterministic streams have
only two polarity variants, not 200 independent tasks. All three predicted channels
(change, positive progress, GAME_OVER) are scored before updating; unspecified fields
use .5. Scoring windows exclude the first block for returns and first 24 control steps.

| Family | Baseline Brier | Candidate Brier | Scored observations/arm |
|---|---:|---:|---:|
| Returning rule | .2151561903 | .2151561903 | 8,400 |
| Stationary .1 | .0781299186 | .0781299186 | 14,400 |
| Stationary .5 | .1706995559 | .1706995559 | 14,400 |
| Stationary .9 | .0782616925 | .0782616925 | 14,400 |

Primary improvement **0%**, failing the 20% gate; controls pass. Every paired forecast,
generation count and post-update exact-rule presence matches, including warmup.
Independent recomputation checked all losses, aggregates and 76,800 paired records;
rerunning the benchmark produced byte-identical raw JSON.

Post-result activation diagnostic found **zero cooldown-blocked exact generations,
zero early-release opportunities and zero exact-rule rejection entries** in every
family. Opposite full no-op/progress patterns agree on terminal, appeared and disappeared:
weighted similarity is 4.5/9.5, above the .38 contradiction threshold. Belief decays
without accumulating contradictions, so rejection and cooldown never become relevant.
Unit fixtures with explicitly registered rejection verify that the new gate works,
but they do not demonstrate useful naturally occurring opportunities.

This is a negative bottleneck test, not proof against evidence-based reconsideration
in other environments. The fixed twelve-step block length also limits sensitivity to
short cooldowns; even a functioning gate need not improve this fixture. Do not retain
inactive machinery or redesign the fixture post hoc to manufacture a positive result.
Future work should first establish naturally rejected, decision-relevant exact rules
and then measure recovery; coupling a different rejection rule requires a new factorial.

Public testing was skipped after the synthetic failure, as preregistered. Official
benchmark access was not tested. No public completion, held-out RHAE or speed claim.

## Validation and artifacts

Candidate: **20 tests pass** (five new tests cover three-observation release, interrupted
streaks, action separation, original cooldown and FIFO/capped streak). Final baseline:
**15 tests pass**. Both pass formatting/lint and ten notebook module source-equality
and compile checks. Patch forward/reverse applicability verified. No candidate code
or tests remain in the final branch; only this report and RESEARCH_PLAN.md are tracked.

Ignored evidence: `experiments/results/2026-11-15-evidence-reconsideration/`: fixed
protocol, frozen baseline/candidate, candidate patch/tests, benchmark, raw JSON,
summary, independent audit/replay, diagnostic, dependency freeze and validation logs.
To reproduce at the base: apply candidate.patch, restore candidate_tests.py into tests,
then run benchmark.py, audit.py and diagnose.py with PYTHONPATH=. using the recorded
Python 3.12 environment. Raw evidence is local and is not pushed.
