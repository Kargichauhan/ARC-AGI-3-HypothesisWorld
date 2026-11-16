# Persistent-clause falsification — 2026-11-16

Decision: **reject the mechanism; merge the negative research record**. Three
consecutive clause contradictions eliminate stale reversal predictions but worsen
fair-coin motion prediction. Candidate source, four tests and runner were archived
and removed. Production matches main.

## Hypothesis and protocol

Hypothesis: sustained contradictions distinguish obsolete rules from isolated noise,
improving adaptation without harming stochastic predictions. Unlike October 21's
immediate conjunctive falsification, require three successive mismatches; unlike
November 15's cooldown bypass, change actual rejection.

Before implementation, gates required >=50% reduction in final-eight-step stale
motion mass after reversal, stationary Brier increase <=.01, and Brier increase
<=.02 in EACH Bernoulli(.1/.5/.9) control. All validation must pass. Conditional
public gate: five cached games, F, seeds 0/1/2, 100 actions; at least one extra level,
no per-game summed loss, <=2x warm runtime. No gates or parameters were retuned.

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected memory, freshly
cloned main/daily/research refs, Git history, plan and relevant prior reports.
Connected GitHub search found no open PRs. Original cloud-backed checkout reports
broken refs; left untouched and used an isolated clone. No unmerged mechanisms or
game-source design information incorporated.

## Mechanism

Only production change: `agent/hypotheses.py`. Each applicable rule counts successive
observations with at least one known predicted clause differing from a known actual
clause. Fully compatible comparable observations reset the streak; observations
without comparable clauses leave it unchanged. At three mismatches, reject the rule,
record the contradiction step and existing cooldown, and skip its usual update.
Otherwise preserve original similarity updates, generation and pruning. Original
updates can still reject unknown-motion rules; this experiment does not repair that.
No policy, action proposal or world-model change.

## Synthetic evidence

200 seeds per family, 64 outcomes each, two arms: **128,000 step records**, 64,000
paired observations. RNG `20261116 + seed` selects colour/action and stochastic
outcomes. Supplied StateDiff motion is +x or -x with other fields unchanged.
Reversal is 16 +x then 48 -x; stationary always +x. Controls draw independent signs.
Forecasts precede updates and renormalize explicit motion-rule weights, defaulting
to .5 when absent. These weights are not calibrated posteriors.

| Metric | Baseline | Candidate |
|---|---:|---:|
| Reversal stale +x mass, steps 56–63 | .500000 | .000000 |
| Stationary Brier, steps 32–63 | .000000 | .000000 |
| Bernoulli(.1) Brier, steps 32–63 | .249201 | .117934 |
| Bernoulli(.5) Brier, steps 32–63 | .250000 | .398711 |
| Bernoulli(.9) Brier, steps 32–63 | .248081 | .113123 |

Reversal and stationary gates pass. Fair-coin loss increases **.148711**, failing
the .02 allowance despite improvements on biased controls. Runs of contradictions
occur naturally in noise; persistence alone does not establish a rule change.
Deterministic families repeat equivalent streams with varied action/colour, not
200 independent tasks. This is supplied-outcome testing, not online solving or
perception evaluation. No completion, held-out, RHAE or speed claim.

Public testing was skipped at the failed synthetic gate. Official access was not
tested this run; absence of a public result does not establish unavailable access.

## Validation and disposition

Candidate: **18 passed, 1 failed**, with all four new tests passing. Existing
`test_information_gain_can_select_disagreement_over_exhausted_action` fails entropy
ordering (.985412 unseen versus .997958 familiar); selected action still passes.
The existing test was not weakened. One initial new test incorrectly expected
unknown-motion rules to survive the unchanged original updater; corrected to
require baseline rejection with zero new streak. No mechanism change followed.

Candidate format/lint and ten notebook module source-equality/compile checks pass.
Independent audit verifies all raw forecasts from saved prediction weights, losses,
RNG inputs, paired observation equality and summaries. Second execution reproduces
raw records and summaries byte-for-byte; this is repeated evidence. After removal:
**15 baseline tests pass**, format/lint pass, ten packaged modules match source and
compile. Agent/tests/scripts/notebook configuration match main. Archived patch
checks apply forward to baseline and reverse to candidate.

Ignored evidence: `experiments/results/2026-11-16-persistent-clauses/`, mirrored with
SHA256 verification to the original workspace. Includes protocol, baseline,
candidate/patch/tests, runner, raw forecasts/outcomes, summary, audit, replay hashes,
dependencies, validation and recovery bundle. Raw evidence is local, not pushed.
Reproduce from base by applying `candidate.patch`, restoring `baseline.py` at the
ignored path, then `PYTHONPATH=. python experiments/run_persistent_clauses.py`.

Recommend merging this report and rejecting the implementation. Future work should
distinguish stochastic alternatives from deterministic claims using predictive
evidence, rather than increasing a fixed streak or relaxing control gates.
