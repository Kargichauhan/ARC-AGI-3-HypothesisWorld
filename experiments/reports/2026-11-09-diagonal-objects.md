# Diagonal object connectivity — 2026-11-09

Decision: **reject the mechanism; merge the negative research record**. Eight-connected
segmentation repairs diagonal sprites but merges independent corner-touching objects,
corrupting motion evidence. Removed candidate source and five tests before commit.

## Hypothesis and method

Hypothesis: same-colour diagonal connectivity reduces sprite fragmentation and improves
object-level motion without unacceptable false mergers. Only the component neighbourhood
changed from four to eight; matching, background inference, learning and policy stayed fixed.
This differs from October 20's assignment optimizer and October 23's background inference.

Base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected current remote main,
daily/research refs, main history/plan, prior report introductions and relevant reports,
and automation memory. Connected GitHub search returned no open PRs. Used an isolated
clone because the original checkout had slow reads and broken refs; left it untouched.

Before implementation, the ignored protocol fixed 200 paired seeds per family,
RNG `20261109 + seed`, 32x32 grids, random colour/origin/slope/length. Primary scenes
contain a 3–7-cell diagonal sprite moving one cell right. Controls contain two 2x2
objects touching at a corner, two separated objects, or one horizontal line. In the
two-object scenes only the second object moves right. Ground truth is the generated
object partition. Partition accuracy is the fraction of true objects recovered exactly,
pooled over before/after; motion accuracy requires exactly the true displacement list.

Retention required at least 25% lower primary partition error, at least 95% primary
motion accuracy, baseline control competence of at least 95%, and candidate control
losses no greater than five percentage points. All gates required; no retuning.
Public F testing and subsequent A–E expansion were conditional on synthetic success.

## Results

800 paired fixtures, 1,600 arm records; identical accuracy on a second execution:

| Family | Partition accuracy, baseline → candidate | Motion accuracy, baseline → candidate |
|---|---:|---:|
| Diagonal sprite | 0% → 100% | 0% → 100% |
| Independent corner contact | 100% → 50% | 100% → 0% |
| Separated objects | 100% → 100% | 100% → 100% |
| Horizontal sprite | 100% → 100% | 100% → 100% |

The corner control fails decisively: before movement both objects become one; after
separation there are two, so matching produces no correct motion event. This is a
representation ambiguity, not a parameter-search failure. Random seeds vary rendering;
they do not supply 200 independent semantic task families. These tests do not establish
ARC solve rates or how frequent either topology is in public games.

No official/public benchmark was run: the preregistered synthetic stopping gate failed.
Access was not tested, and no unavailability, completion or RHAE claim is made. Per-record
perception/differencing timings are retained, but sub-millisecond interleaved measurements
are not a reliable speed benchmark. No full-agent improvement claim.

## Verification and artifacts

Candidate: 20 tests pass, formatting/lint pass, notebook generated with all 10 embedded
modules source-equal and compilable. Final baseline: 15 tests pass, same format/lint and
notebook checks. Independent set-overlap audit checks oracle recovery and pixel-support
conservation across 1,600 records. Raw rows, protocol, runner, dependency versions,
source snapshots, candidate patch/tests, audit and validation logs are preserved in the
ignored `experiments/results/2026-11-09-diagonal-objects/` directory. The archived patch
covers production changes; the separate candidate test snapshot preserves new tests.

Production matches main. Only this report and the research-plan entry are committed.
A useful follow-up must infer connectivity from temporal evidence or retain competing
partitions; replacing one universal neighbourhood with another is insufficient.
