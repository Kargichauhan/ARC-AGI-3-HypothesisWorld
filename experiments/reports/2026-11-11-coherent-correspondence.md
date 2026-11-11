# Coherent group correspondence — 2026-11-11

Decision: **reject the candidate; merge the negative research record**. Complete
translation explains a moving group perfectly, but identical observations can also
come from independent motion. The candidate converts all correct identities into
errors in that control. Implementation and six tests were archived and removed.

## Hypothesis and fixed gates

Hypothesis: a unique complete translation of at least three same-colour, same-shape
components provides reliable identity evidence beyond greedy proximity, improving
the motion outcomes consumed by HypothesisWorld. Preassign these group matches and
use unchanged greedy matching for the remaining components. Groups must have equal
cardinality in both frames and unique destination centroids. No scoring, segmentation,
event semantics or downstream policy changes. This differs from October 20's
maximum-total-score assignment and November 10's pairwise confidence filter.

Recorded before implementation or measurement:

- Coherent motion: candidate identity accuracy >=95%, baseline errors reduced >=20%.
- Stationary and distinct-colour controls: each arm >=95% accuracy, loss <=5 points.
- Independent motion: candidate identity loss <=5 points versus baseline; stationary
  object recovery >=95%.
- Conditional on synthetic success: five public games, F, seeds 0/1/2, 100 actions;
  >=1 extra level, no per-game summed regression, warm runtime <=2x baseline, then A–E.
- Unit tests, formatting/lint, notebook source equality/compilation and evidence audit.

## Benchmark and result

200 paired seeds per family, RNG `20261111 + seed`, 48x48 grids. Three singleton
sprites start at offsets 0,g,2g; g sampled uniformly from 3–6, origin x/y from 8–16,
quarter turn 0–3, colour 1–7. Coherent destinations are g,2g,3g. Independent motion
uses 3g,g,2g: the first sprite moves past the other two, which remain stationary.
Stationary destinations are unchanged; distinct-colour uses coherent motion and
three successive colours. These are four designed geometries with nuisance variation,
not 800 independent tasks. Ground truth comes from generator identities, not matching.

| Correct identities / 600 per arm | Baseline | Candidate |
|---|---:|---:|
| Coherent translation | 0 | 600 |
| Independent motion | 600 | 0 |
| Stationary | 600 | 600 |
| Distinct-colour translation | 0 | 0 |

Primary passes, independent-motion retention fails: stationary identity recovery in
that family falls from 400/400 to 0/400. The distinct-colour control also fails the
absolute competence gate in both arms. Baseline overlap scoring matches stationary
locations across colour changes, treating them as transformations. This is a preexisting
failure, not a candidate regression, and prevents claiming broad baseline competence.
An initial unit test incorrectly expected colour identity to defeat overlap; it was
corrected to assert the actual unchanged fallback before benchmark measurement.
No policy, fixture, parameter or gate was retuned after measurement.

For each seed the coherent and independent families render exactly the same pair of
grids, but require incompatible identity assignments. Both arms therefore make the
same assignments across those families. This establishes a two-frame identifiability
limit: spatial coherence is a prior, not corroborating causal evidence. Six hundred
errors in this constructed control are not an estimate of public-game error frequency.

Synthetic failure stopped conditional public evaluation. Official access was not
tested; no claim of access unavailability, public completion, runtime improvement,
held-out performance or RHAE is made. No competition submission.

## Verification and provenance

Base/main `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation memory,
clean original checkout, fresh origin main/daily/research refs, main plan/history,
all prior report introductions and relevant full correspondence reports. Connected
GitHub search found no open PRs. Used an isolated clone to preserve the original
checkout. No subagents, unmerged mechanisms or game implementation inspection.

Candidate: **21 tests pass** (15 existing plus six new); final baseline: **15 pass**.
Both pass formatting/lint and generation, source equality and compilation of all
**10 notebook modules**. Audit independently checks all **1,600 arm records** for
rendered pixels, identity scoring, one-to-one matches, birth/death counts, motion
deltas, equal paired inputs and identical coherent/independent observations.
A second benchmark execution reproduces raw JSON byte-for-byte. Repeated evidence
is not additional samples. Final agent/tests/scripts match main exactly.

Ignored evidence: `experiments/results/2026-11-11-coherent-correspondence/` contains
protocol, frozen source, patch, six candidate tests, benchmark, raw grids/matches,
summary, independent audit, replay reference, dependency/provenance records and
validation logs. From the base, apply `candidate.patch`, copy `candidate_tests.py`
to `tests/test_coherent_correspondence.py`, then run `PYTHONPATH=. python` with the
archived `benchmark.py` and `verify.py`. Run `scripts/build_notebook.py` before the
archived `package_check.py`. Evidence is also preserved in the original checkout's
ignored results directory with a SHA-256 manifest.

Recommend merging only the research record and plan entry. Future correspondence
work needs additional temporal/intervention evidence or explicit competing identity
hypotheses, retaining the observationally identical independent-motion control.
