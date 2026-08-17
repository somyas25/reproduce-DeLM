"""
solver.py

This is a stub solver. It does not call an LLM yet.
Replace solve() with a real LLM call in a later step.

For now, it returns the problem's own canonical_solution,
so you can confirm the grading pipeline works end to end
before you plug in a real model.
"""


def solve(problem: dict) -> str:
    """
    Given one HumanEval problem, return a code completion.

    Args:
        problem: One problem dict from load_problems().
                 Has keys: task_id, prompt, canonical_solution, test, entry_point.

    Returns:
        A string containing the function body completion.
    """
    # TODO: replace this line with a real LLM call.
    # Example shape for later:
    #   completion = call_llm(problem["prompt"])
    #   return completion
    return problem["canonical_solution"]