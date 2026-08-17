"""
llm_client.py

One shared function for calling the LLM API.
All agents call this function, instead of each agent
writing its own API code.

Reads the API key from the .env file (via python-dotenv).
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

_client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def call_llm(prompt: str, model: str = "claude-sonnet-4-6", max_tokens: int = 1000) -> str:
    """
    Send one prompt to the LLM and return the text response.

    Args:
        prompt: The full text prompt to send.
        model: Which model to call.
        max_tokens: Max tokens in the response.

    Returns:
        The model's text response, as a plain string.
    """
    response = _client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    # Combine all text blocks in the response into one string.
    text_parts = [block.text for block in response.content if block.type == "text"]
    return "".join(text_parts)