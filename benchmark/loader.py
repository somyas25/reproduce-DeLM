"""
loader.py

Loads problems from the HumanEval dataset.
"""

from human_eval.data import read_problems


def load_problems(limit: int = None) -> dict:
    """
    Load HumanEval problems.

    Args:
        limit: If set, only return the first N problems.
               Useful for a quick test run.

    Returns:
        A dict of {task_id: problem_dict}.
    """
    problems = read_problems()

    if limit is not None:
        limited_ids = list(problems.keys())[:limit]
        problems = {task_id: problems[task_id] for task_id in limited_ids}

    return problems