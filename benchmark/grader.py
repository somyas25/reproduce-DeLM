"""
grader.py

Grades one completion against its HumanEval test cases.
Uses human_eval's own check_correctness function.
"""

from human_eval.execution import check_correctness


def grade_completion(problem: dict, completion: str, timeout: float = 5.0) -> dict:
    """
    Run one completion against its test cases.

    Args:
        problem: One problem dict from load_problems().
        completion: The generated function body, as a string.
        timeout: Max seconds allowed for the test run.

    Returns:
        A dict with keys: task_id, passed (bool), result (str message).
    """
    result = check_correctness(problem, completion, timeout)
    return {
        "task_id": problem["task_id"],
        "passed": result["passed"],
        "result": result["result"],
    }