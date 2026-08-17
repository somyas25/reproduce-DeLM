"""
solver.py (src/agents)

The real Solver agent. Unlike benchmark/solver.py (the stub),
this version calls the LLM to generate a completion.

This is a baseline version:
  - No shared-lessons input yet.
  - No planning step yet.
  - One solver thread, called once per problem.

Stage 2 will add an optional `shared_notes` argument, once
shared_lessons.py is built.
"""

from src.agents.llm_client import call_llm


def solve(problem: dict) -> str:
    """
    Generate a code completion for one HumanEval problem.

    Args:
        problem: One problem dict with a "prompt" field
                  (the function signature + docstring).

    Returns:
        A string containing the generated function body.
    """
    instruction = (
        "Complete the following Python function. "
        "Return only the function body code, with correct indentation. "
        "Do not include the function signature again. "
        "Do not include any explanation or markdown formatting.\n\n"
        f"{problem['prompt']}"
    )

    raw_output = call_llm(instruction)
    return _clean_completion(raw_output)


def _clean_completion(raw_output: str) -> str:
    """
    Strip markdown code fences from the model's output, if present.
    Models often wrap code in ```python ... ``` even when told not to.
    """
    text = raw_output.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = lines[1:]  # drop the opening ``` line
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]  # drop the closing ``` line
        text = "\n".join(lines)
    return text