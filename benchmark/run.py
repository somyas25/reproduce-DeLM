"""
run.py

Entry point for a single grading pass.
Loads a small set of problems, runs the stub solver,
grades each result, and prints a summary.

This is the minimal version. It does not yet include:
  - parallel solver threads
  - the Shared Lessons store
  - avg@1 / pass@N across multiple runs

Add those in the next stage, once this baseline runs clean.
"""

from benchmark.loader import load_problems
from benchmark.solver import solve
from benchmark.grader import grade_completion


def main():
    # grade only 5 problems for a fast first run.
    problems = load_problems(limit=5)

    results = []
    for task_id, problem in problems.items():
        completion = solve(problem)
        graded = grade_completion(problem, completion)
        results.append(graded)
        print(f"{graded['task_id']}: {'PASSED' if graded['passed'] else 'FAILED'}")

    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)
    print(f"\n{passed_count}/{total_count} problems passed.")


if __name__ == "__main__":
    main()