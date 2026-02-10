from dotenv import load_dotenv
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

STRATO_REPO_URL = os.getenv("STRATO_REPO_URL")
WORKDIR = os.getenv("WORKDIR", "/tmp/strato_workdir")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# When LLM quota is reached, use a mock LLM that returns a fixed response for testing purposes
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "true").lower() == "true"

