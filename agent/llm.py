import json
from google import genai
from agent.config import GOOGLE_API_KEY
import re

client = genai.Client(api_key=GOOGLE_API_KEY)

SYSTEM_PROMPT = """
You are an AI software engineer working inside a Git repository.

Rules:
- You MUST return valid JSON only
- Do NOT include markdown or explanations
- Modify existing files when possible
- Add tests for all new functionality
- Tests must use pytest
- Return FULL file contents, not diffs
- Paths must be relative to repo root

Return format EXACTLY:

{
  "summary": "...",
  "files": [
    {
      "path": "...",
      "content": "..."
    }
  ]
}
"""

def generate_code(repo_context: str, user_request: str) -> dict:
    prompt = f"""
REPOSITORY CONTEXT:
{repo_context}

USER REQUEST:
{user_request}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
            SYSTEM_PROMPT,
            prompt
        ],
    )

    text = response.text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Gemini returned invalid JSON:\n{text}"
        ) from e

def extract_json(text: str) -> dict:
    # Remove ```json ... ``` or ``` ... ```
    cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)
    return json.loads(cleaned)

# --- HARDCODED RESPONSE FOR TESTING PURPOSES --- #

# def generate_code(repo_context, user_request):
#     return {
#         "summary": "Add dummy constant",
#         "files": [
#             {
#                 "path": "src/mathlib/physics.py",
#                 "action": "modify",
#                 "content": """
# def orbital_velocity(mu, r):
#     return (mu / r) ** 0.5

# DUMMY_CONSTANT = 42
# """.strip()
#             },
#             {
#                 "path": "tests/test_physics.py",
#                 "action": "modify",
#                 "content": """
# from mathlib.physics import orbital_velocity, DUMMY_CONSTANT

# def test_dummy_constant():
#     assert DUMMY_CONSTANT == 42
# """.strip()
#             }
#         ]
#     }

