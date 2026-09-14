"""Run reproducible HypothesisWorld ablations through the official local harness."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", default="ls20,vc33")
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--ablations", default="A,B,C,D,E,F")
    args = parser.parse_args()

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    output_dir = ROOT / "experiments" / "results" / stamp
    output_dir.mkdir(parents=True, exist_ok=False)
    summary: list[dict[str, object]] = []
    for ablation in [item.strip().upper() for item in args.ablations.split(",")]:
        environment = os.environ.copy()
        environment["HYPOTHESISWORLD_ABLATION"] = ablation
        command = [
            str(ROOT / ".venv" / "bin" / "python"),
            str(ROOT / "scripts" / "play_local.py"),
            "--game",
            args.games,
            "--max-steps",
            str(args.steps),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        (output_dir / f"ablation-{ablation}.log").write_text(
            completed.stdout + "\n--- STDERR ---\n" + completed.stderr
        )
        summary.append({"ablation": ablation, "returncode": completed.returncode})
        print(f"{ablation}: returncode={completed.returncode}")
    (output_dir / "summary.json").write_text(
        json.dumps(
            {
                "created_at": stamp,
                "games": args.games,
                "steps": args.steps,
                "python": sys.version,
                "runs": summary,
            },
            indent=2,
        )
        + "\n"
    )
    if any(run["returncode"] != 0 for run in summary):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
