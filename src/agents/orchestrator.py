"""
orchestrator.py

Runs N independent solver threads on one problem.
This is the baseline: no data sharing between threads.

Each thread calls src/agents/solver.py separately.
Results are collected and returned together, so
benchmark code can compute avg@1 and pass@N.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from src.agents.solver import solve


def run_threads(problem: dict, n_threads: int = 4) -> list:
    """
    Run n_threads independent solver attempts on one problem.

    Args:
        problem: One HumanEval problem dict.
        n_threads: How many parallel solver threads to run.

    Returns:
        A list of completion strings, one per thread.
    """
    completions = []

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        futures = [executor.submit(solve, problem) for _ in range(n_threads)]
        for future in as_completed(futures):
            completions.append(future.result())

    return completions