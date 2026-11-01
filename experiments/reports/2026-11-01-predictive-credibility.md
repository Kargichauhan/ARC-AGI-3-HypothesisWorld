# Predictive hypothesis credibility — 2026-11-01

Decision: **reject the mechanism; merge this negative research record**. Weighting
hypotheses by prediction error improves stationary calibration but reduces public
completion from two levels to zero. Candidate source, ten tests and the runner were
archived under ignored results and removed. Production matches main.

## Hypothesis and fixed gates

Hypothesis: measured predictive accuracy supplies better hypothesis weights than
saturating support beliefs alone, improving calibration and information-guided
completion. This changes hypothesis competition, unlike prior empirical-model
shrinkage, hard conjunctive falsification, or posterior information rollouts.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Fetched origin main and all
daily/research branches; inspected plans, reports, history and prior run memory.
Connected GitHub search found no open PRs. Used an isolated checkout because original
cloud-managed reads were slow; original tracked files were untouched. No game source
informed design and no unmerged mechanisms were incorporated.

Protocol saved before implementation/measurement; all retention gates required:

- Five synthetic families, 200 paired seeds each, 128 outcomes, score steps 32–127:
  at least 20% lower pooled three-channel Brier loss on rare progress and no-op.
  Unpredictable and deterministic visible-change controls may lose at most .02
  absolute loss each. A step-64 rule switch is a separate diagnostic.
- Five cached public games, F, seeds 0/1/2, 100 actions: at least one additional
  total level, no per-game summed regression, warm subprocess runtime at most 2x.
- Tests, formatting/lint, notebook source equality/compilation, independent prefix
  audit and deterministic replay pass. A–E expansion conditional on all gates.

No parameters or gates changed after measurement.

## Mechanism

Each active applicable hypothesis accumulates pre-update mean squared error across
visible change, positive progress and GAME_OVER. Specified fields predict zero/one;
unspecified fields predict .5. New hypotheses do not score their generating outcome.
Weight is existing floored effective belief times
`exp(-8 * ((loss_sum + 1)/(observation_count + 4) - .25))`, then normalized.
Four virtual .25-loss observations give neutral initial weights. Original support,
contradiction, rejection and population rules remain intact. Baseline disables only
weighting and collects identical diagnostic evidence.

No new planner, proposal, transfer rule or selector coefficient. In full agent F,
weights affect hypothesis entropy; progress/failure scores still use the empirical
world model. This three-event score is not a posterior over full outcomes. Treating
wildcards as .5 is an assumption.

## Synthetic evidence

2,000 arm/seed records, 256,000 observations. Rare progress is Bernoulli(.1) with
visible change always true. The unpredictable control independently draws cell-change,
progress and failure flags at .5; StateDiff's changed event includes progress.
The switch changes no-op outcomes into deterministic progress at step 64.

| Fixture | Baseline Brier | Weighted Brier |
|---|---:|---:|
| Rare progress | .061031 | .044531 |
| No-op | .023338 | .011568 |
| Primary pooled | .042185 | .028050 |
| Unpredictable control | .276192 | .282266 |
| Visible-change control | .023566 | .011580 |
| Rule switch, entire scoring window | .028209 | .032581 |
| Rule switch, steps 64–127 | .030644 | .042949 |

Primary loss improves **33.51%**; both required controls pass. Rare-progress paired
mean difference bootstrap 95% interval: [-.016723, -.016281]; unpredictable loss
increases .006075, interval [.005614, .006528]. Ten thousand seeded resamples.
Post-switch loss increases **40.15%**, exposing stale credibility. Deterministic
families repeat identical streams across seeds, not 200 independent tasks. These
supplied outcome streams demonstrate calibration, not online game solving.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9 / arcengine 0.9.3. All 10 game/metadata
and 30 harness Python hashes match the preceding local cache. Primary cohort:
30 runs, 3,000 actions. Entries are completed levels for seeds 0/1/2.

| Game/version | Baseline | Weighted |
|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 0/0/0 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 |

Completion **2 → 0** fails both public gates. Same-frame/nonpositive-progress
outcomes fall 595 → 545; consecutive exact action-coordinate repeats rise 746 → 796.
Eleven of fifteen paired choice sequences change. Both previously successful vc33
seeds first diverge at decision index 2 at the same source: weighting selects an
already-tested action class over baseline's untested class. This locates divergence,
not the unique cause of eventual failure.

On baseline's 1,488 executed transitions, evaluating both mixtures on identical
prefixes reduces Brier loss .050705 → .044854 (**11.54%**). Candidate's 1,489-transition
history gives .047320 → .040886. These are within-history shadow comparisons, not
an off-policy completion estimate. Better event forecasts do not establish that
normalized hypothesis-label entropy reliably values experiments.

Warm replay subprocess totals: 12.634 → 11.993 seconds (0.949x); initial totals
12.851 → 13.077. Includes startup/equal tracing, not an isolated speed claim.
Replay reproduces all 2,000 synthetic records and 30 public runs exactly by
uncompressed hashes; repeated actions are not independent evidence. An earlier
replay hit transient ENOSPC before the last seed finished; partial files remain
archived and the full public cohort was rerun. Old cloud trace reads also timed out;
retention does not depend on a prior-day trace comparison. No held-out access,
official RHAE result or competition submission is claimed.

## Verification and disposition

Candidate: **25 tests** (10 new), format/lint and **10** notebook source/compile
checks pass. Tests cover score formula, wildcards, signed progress, prequential
initialization, action scope, disabled parity, rejection and long streams.
Independent audit reconstructs 1,087,296 hypothesis prefixes and 319,007 forecasts
across 256,000 synthetic plus 2,977 public observations; checks weights, information
scores, public pixel changes, selected proposals and seeded outcome streams.
Only runner formatting/context-manager cleanup followed initial measurement;
policy stayed unchanged. Final replay manifest records the archived source.

After removal: **15 baseline tests**, format/lint and the same ten notebook checks
pass; agent/tests/scripts/notebook settings match main. Forward/reverse patch checks
pass. Only this report and the research-plan note are committed.

Reject fixed cumulative credibility weighting. Before revisiting it, establish
useful experiment ranking and adaptation to obsolete credibility. Do not promote
this mechanism on aggregate calibration gains or combine it with rejected renewal.

Ignored evidence: `experiments/results/2026-11-01-predictive-credibility/` contains
protocol, compressed records/replay, audits, manifests, validation, removed source,
runner and `candidate.patch`. Raw evidence is not pushed. Patch SHA256:
`3b0bf25040f2b58da15f2f1fdffb51a03688f4bfde7c32869d591946457e2c8b`.
Reproduce by applying the patch to the base and running
`experiments/run_predictive_credibility.py --output experiments/results/credibility-replay`
with recorded dependencies/cached games and writable MPLCONFIGDIR/XDG_CACHE_HOME.
