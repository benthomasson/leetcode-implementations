#!/usr/bin/env python3
"""Run all LeetCode solution tests and produce a report."""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
PYTHON = str(ROOT / ".venv" / "bin" / "python")


def find_problems():
    problems = []
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and (d / "solution.py").exists():
            problems.append(d)
    return problems


def run_test(problem_dir):
    test_file = problem_dir / "test_solution.py"
    if not test_file.exists():
        return {"status": "skipped", "reason": "no test file"}

    try:
        result = subprocess.run(
            [PYTHON, "-m", "pytest", str(test_file), "-x", "-q", "--tb=short", "--no-header"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(problem_dir),
        )
        passed = result.returncode == 0
        output = (result.stdout + result.stderr).strip()
        return {
            "status": "passed" if passed else "failed",
            "returncode": result.returncode,
            "output": output,
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "reason": "exceeded 30s"}
    except Exception as e:
        return {"status": "error", "reason": str(e)}


def main():
    problems = find_problems()
    print(f"Found {len(problems)} problems\n")

    results = {"passed": [], "failed": [], "skipped": [], "timeout": [], "error": []}
    start = time.time()

    for i, problem_dir in enumerate(problems, 1):
        name = problem_dir.name
        result = run_test(problem_dir)
        status = result["status"]
        results[status].append((name, result))

        marker = {"passed": ".", "failed": "F", "skipped": "S", "timeout": "T", "error": "E"}[status]
        print(marker, end="", flush=True)
        if i % 80 == 0:
            print()

    elapsed = time.time() - start
    print(f"\n\n{'=' * 60}")
    print(f"RESULTS  ({elapsed:.1f}s)")
    print(f"{'=' * 60}")
    print(f"  Passed:  {len(results['passed'])}")
    print(f"  Failed:  {len(results['failed'])}")
    print(f"  Skipped: {len(results['skipped'])}")
    print(f"  Timeout: {len(results['timeout'])}")
    print(f"  Error:   {len(results['error'])}")
    print(f"  Total:   {len(problems)}")

    if results["failed"]:
        print(f"\n{'=' * 60}")
        print("FAILURES")
        print(f"{'=' * 60}")
        for name, result in results["failed"]:
            print(f"\n--- {name} ---")
            print(result["output"])

    if results["timeout"]:
        print(f"\n{'=' * 60}")
        print("TIMEOUTS")
        print(f"{'=' * 60}")
        for name, _ in results["timeout"]:
            print(f"  {name}")

    if results["error"]:
        print(f"\n{'=' * 60}")
        print("ERRORS")
        print(f"{'=' * 60}")
        for name, result in results["error"]:
            print(f"  {name}: {result['reason']}")

    report = {
        "total": len(problems),
        "passed": len(results["passed"]),
        "failed": len(results["failed"]),
        "skipped": len(results["skipped"]),
        "timeout": len(results["timeout"]),
        "error": len(results["error"]),
        "elapsed_seconds": round(elapsed, 1),
        "failures": [
            {"problem": name, "output": r["output"]} for name, r in results["failed"]
        ],
        "timeouts": [name for name, _ in results["timeout"]],
        "errors": [
            {"problem": name, "reason": r["reason"]} for name, r in results["error"]
        ],
    }
    report_path = ROOT / "test_report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nJSON report written to {report_path}")

    return 1 if results["failed"] or results["error"] else 0


if __name__ == "__main__":
    sys.exit(main())
