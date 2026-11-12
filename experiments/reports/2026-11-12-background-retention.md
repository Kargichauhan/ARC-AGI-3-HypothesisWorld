# Enclosed background retention — 2026-11-12

Decision: **reject the candidate; merge the negative research record**. Enclosure
recovers background-coloured objects but also asserts objects in every closed-hole
control. Candidate source and ten parameterized test cases were archived and removed.

## Hypothesis and fixed gates

Hypothesis: retaining border-disconnected components of the inferred background
colour recovers camouflaged objects without unacceptable false foreground assertions.
Only extraction changes: flood every four-connected colour component, discard a
background component only if it touches a frame edge. Background inference, matching,
state fingerprints, hypotheses and policy remain unchanged. Unlike October 23's
boundary-consensus experiment, this preserves the selected background colour and
changes which of its components become objects.

Before implementation or measurement, fixed 200 paired seeds in each of four
families. Require >=95% primary object recovery; each control must retain >=95%
exact segmentation with <=5 percentage-point loss relative to baseline. Conditional
on synthetic success, require >=1 extra completed public level, no per-game regression
and <=2x runtime. Validation includes unit tests, format/lint and notebook packaging.
No mechanism, fixture or threshold was retuned after measurement.

## Synthetic benchmark

RNG `20261112 + seed`; width/height independently uniform 24–40, two distinct colours
sampled from 0–9, square side 5–9 at a random interior location with two-cell margin.
Camouflage scenes contain a one-cell-thick foreground ring and a distinct semantic
object filling its background-coloured interior. Hole controls use identical pixels
but label only the ring as an object. Open-cavity controls remove one top-edge ring
pixel; ordinary controls fill the entire square with foreground colour. Ground truth
is the generator's exact cell partition, not the parser's output.

| Exact scene partitions / 200 per arm | Baseline | Candidate |
|---|---:|---:|
| Camouflaged interior object | 0 | 200 |
| Closed hole | 200 | 0 |
| Open cavity | 200 | 200 |
| Ordinary solid object | 200 | 200 |

Primary target recovery improves 0/200 to 200/200. Closed-hole false objects increase
0 to 200, decisively failing control retention. All 1,600 arm records retain the
correct inferred background. These are four designed geometries with nuisance
variation, not 800 independent tasks or estimates of ARC scene frequencies.

An enclosed background-coloured region can represent either a separate object or
empty space. The identical camouflage/hole inputs establish that single-frame
connectivity cannot identify the semantic role under both definitions. This pilot
rejects unconditional promotion, not every use of enclosed regions as hypotheses or
probe targets. It does not establish any full-agent action-efficiency benefit.

The synthetic stopping gate failed, so the conditional public cohort was not run.
Official access was not tested; no access-unavailability, public completion, held-out,
RHAE or speed-improvement claim is made. No competition submission.

## Verification and provenance

Base/main: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Reviewed automation memory,
fresh origin main/daily/research branches, main plan/history, recent reports and the
prior boundary-background report. Connected GitHub search returned no open PRs.
Used an isolated clone, leaving the clean original checkout and prior work untouched.
No unmerged implementation or game implementation source was used.

Candidate: **25 tests pass**; restored baseline: **15 tests pass**. Both pass
formatting/lint, notebook generation, and source equality/compilation of all **10
embedded modules**. An independent exterior-reachability/set audit checks all **1,600
records**, pixel supports, partitions, false/missed objects and paired ambiguity.
A second execution reproduces raw JSON byte-for-byte; replay is not extra evidence.
Final production agent/tests/scripts match main exactly. Patch forward/reverse checks pass.

Ignored evidence: `experiments/results/2026-11-12-background-retention/` contains
protocol, frozen sources, candidate patch/tests, benchmark, raw grids/partitions,
summary, audit/replay records, dependencies, validation logs and SHA-256 manifest.
Patch SHA-256: `18d5b5fdbf3858182e784b609259151eadec79940ffe632a18d22187011529e8`.
Evidence is mirrored into the original checkout's ignored results path. It is local,
not pushed. To reproduce from the base, apply `candidate.patch`, copy
`candidate_tests.py` to `tests/test_background_retention.py`, restore the evidence
folder at the same relative path, and run its `benchmark.py` and `verify.py` from the
repository root. Build the notebook before running `package_check.py`.

Recommend merging only this report and the research-plan entry. Future work should
retain alternative object/hole interpretations and seek temporal or intervention
evidence before committing either interpretation to causal outcome learning.
