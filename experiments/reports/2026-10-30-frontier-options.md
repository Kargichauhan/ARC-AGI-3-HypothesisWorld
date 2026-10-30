# Frontier options factorial — 2026-10-30

Decision: **reject the implementation; merge this negative research record**.
Committing to an untested probe after navigation solves supplied-map corridors
that neither component solves alone. Public completion remains two levels in all
four arms, and the joint policy never starts a route. Candidate code, tests and
runner were archived under ignored results and removed before committing.

## Hypothesis and fixed criteria

Hypothesis: carrying an exact untested intervention through a reliable observed
route, then executing it on arrival, improves completion beyond navigation or
local probing alone. October 3's routing experiment reached synthetic frontiers
but left their useful probes unexecuted. This is a new factorial of a committed
navigation controller and local probe selection; it does not reuse that pilot's
planner reward or silently incorporate its rejected implementation.

Before implementation and measurement, the protocol required all of:

- Supplied-map corridors of two/four/six edges, 100 paired seeds each, 32-action
  cap: joint solves at least 95% at every length, improves pooled solve rate by
  at least 20 percentage points and reduces capped actions at least 20% against
  baseline **and each component**.
- Known immediate goal and single-action four-hit controls, 100 seeds each:
  baseline solves at least 95%, joint loses at most five points and costs at
  most 1.25x baseline. A 20% route-slip fixture is diagnostic.
- Five cached public games, F, seeds 0/1/2, 100 actions: joint adds at least one
  level against baseline **and each component**, with no per-game summed loss
  against baseline and warm runtime at most twice baseline.
- Unit tests, formatting/lint, notebook source equality/compilation, independent
  event-prefix audit and exact replay pass. A–E expansion conditional on F success.

No gate, fixture or policy parameter changed after results.

## Mechanism and provenance

Main/base: `24a5f4173ecb2fadf88360b38c0a77bad8175b65`. Inspected automation memory,
fresh remote main/daily/research branches, research plans, history, prior report
introductions and relevant full reports. Connected GitHub search found no open
PRs. Latest published daily branch was October 29; memory also recorded October
26's unpublished experiment. Original checkout reads timed out and status listed
four modified files alongside read errors. Left it untouched and used an isolated
fork checkout. No game implementation informed the design.

Four arms: baseline, routing only, probing only, joint. Ordinary selector scores
and RNG draws are preserved; an F-only postprocessor may move one action first.
The world model, hypotheses, proposals and pooled learning identities are unchanged.
Separate controller records retain exact click coordinates, preventing navigation
from substituting a sibling coordinate sharing a pooled learning key.

Keep 512 exact transition records and 512 FIFO observed candidate sets. A route
edge needs at least two samples, modal destination frequency at least .9, observed
source legality, and no retained terminal or negative-progress outcome. Search
simple paths breadth-first, at most six edges and 512 expansions. Exclude reset
and undo. When no candidate predicts positive progress, probing chooses the
highest-ranked untested exact current candidate with zero predicted failure risk.
Otherwise routing searches for a remote observed state with an untested candidate;
remote probe ties use cached proposal order. Joint carries that probe at the end
of the route; routing-only stops on arrival. Each step rechecks actual state and
current eligibility; mismatch, lost legality, positive progress opportunity, reset
or terminal outcome cancels commitment. Empirical zero risk is not a safety guarantee.

## Synthetic evidence

Four demonstrations of every state/action except the final forward goal probe,
plus 20 visit observations per state, supply the map. Forward/backward/two-no-op
labels are permuted with seed `20261030 + seed`; policy seeds are 0–99. Every arm
gets identical training and learns online afterward. Each table cell reports
solves out of 100 / mean capped actions.

| Fixture | Baseline | Route | Probe | Joint |
|---|---:|---:|---:|---:|
| Two-edge corridor | 0 / 32 | 0 / 32 | 0 / 32 | 100 / 3 |
| Four-edge corridor | 0 / 32 | 0 / 32 | 0 / 32 | 100 / 5 |
| Six-edge corridor | 0 / 32 | 0 / 32 | 0 / 32 | 100 / 7 |
| Known immediate goal | 100 / 1 | 100 / 1 | 100 / 1 | 100 / 1 |
| Single-action four-hit | 100 / 4 | 100 / 4 | 100 / 4 | 100 / 4 |
| Four-edge, 20% route slips | 0 / 32 | 52 / 28.58 | 0 / 32 | 89 / 17.73 |

Primary pooled cost falls 32 → 5 actions, **84.38%**, with 300/300 joint solves
versus zero for each comparator. All synthetic retention gates pass. Slip failures
show that supplied deterministic route evidence is not robust to changed dynamics.
The controls have competent baselines but limited breadth: one has known reward,
and the other has no competing action. These are six designed topology/control
families and label permutations, not 600 independent ARC tasks or evidence of
learning useful maps from scratch.

## Public evidence

Official cached OFFLINE engine: arc-agi 0.9.9, arcengine 0.9.3, framework
`4743e7d0aaae0ded0d98a89a7e282e63564cd58b`. All ten game/metadata and thirty
harness Python hashes match October 29. Arm order rotates by seed.
Primary cohort: **60 runs, 6,000 actions**. Entries list seeds 0/1/2.

| Game/version | Baseline | Route | Probe | Joint |
|---|---|---|---|---|
| ls20-9607627b | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| vc33-5430563c | 1/0/1 | 1/0/1 | 1/0/1 | 1/0/1 |
| ft09-0d8bbf25 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| cn04-2fe56bfb | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| su15-1944f8ab | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |

| Metric | Baseline | Route | Probe | Joint |
|---|---:|---:|---:|---:|
| Completed levels | 2 | 2 | 2 | 2 |
| Equal-frame/nonpositive-progress outcomes | 595 | 595 | 456 | 456 |
| Consecutive identical selected actions | 746 | 745 | 346 | 346 |
| Overrides of ordinary ranking | 0 | 7 | 365 | 365 |

Joint and probe have exactly identical decisions and observations in all fifteen
paired runs. Joint uses local probes on 1,258 decisions and baseline fallback on
228; it starts **zero routes**. Route-only starts seven one-edge routes, all in
su15, with no completion benefit. The successful synthetic interaction never
occurs in this public pilot. Local probing changes visits and choices, but cannot
supply the completion evidence needed to retain either mechanism. All fifteen
baseline trajectories exactly reproduce October 29, including scores and outcomes.

Warm replay subprocess totals were 19.143 s baseline, 19.796 s route, 19.549 s
probe and 19.111 s joint (**0.998x** baseline). Initial totals were
19.241/19.126/20.091/19.890 s. Equal instrumentation and process startup are
included; these timings do not establish a production speedup.

## Verification, limitations and disposition

Candidate: **30 tests pass**, including fifteen added cases for route/probe
composition, exact coordinate identity, unsafe/undersupported edges, stale legality,
state mismatch, progress/risk guards, bounds, reset, non-F parity, unchanged scores
and RNG, and terminal adapter observations. Formatting/lint and **11** notebook
module source/compile checks pass. Independent prefix reconstruction verifies all
2,400 synthetic records (43,331 decisions) and all 60 public runs (5,948 decisions
and observations), including route support, commitment, raw pixel changes and
legal execution. All 2,400 synthetic records and 60 public runs replay exactly by uncompressed
trace hashes. The additional 6,000 public actions are repeated evidence, not
independent trials.

Only test additions and a semantics-preserving explicit adjacent-zip argument
followed the first cohort; the candidate policy remained unchanged. The final
replay manifest is authoritative. After archiving/removal, **15 baseline tests**,
formatting/lint and **10** notebook module checks pass; production matches main.
No held-out access, official RHAE result or competition submission is claimed.
These are repeatedly used public development games with short budgets.

Reject the candidate; retain the factorial evidence. Reaching a supplied frontier
and executing its probe is sufficient for the designed corridor, but this policy
does not create that situation online. Before retrying, require evidence of
naturally acquired reusable routes to useful probes, and a control with competing
hidden-delay actions. Do not retain navigation complexity on supplied-map gains
or reduced repetition alone.

Ignored evidence: `experiments/results/2026-10-30-frontier-options/` contains the
protocol, raw traces, source/dependency/cache manifests, independent audit, replay,
validation, archived candidate sources and removed patch. Raw evidence is not
pushed. Patch SHA-256: `68e26ad09a2f6e7fe593c67dfca0790403d77e3788caff713c28ab1ea3c038f3`.
Forward/reverse patch checks passed. To reproduce, apply the patch to the base,
copy the saved protocol into the expected ignored evidence directory, and run
`.venv/bin/python experiments/run_frontier_options.py --output <fresh-directory>`
with recorded dependencies/cached games and writable plotting/cache directories.
Only this report and the research-plan entry are committed.
