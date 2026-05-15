import pytest
from core.config import Settings

@pytest.fixture
def mock_settings():
    """
    Returns a fresh Settings instance for testing.
    """
    return Settings(
        LLM_BACKEND="test-model",
        OPENAI_API_KEY="test-key",
        GEMINI_API_KEY="test-key",
        API_PORT=9999
    )

@pytest.fixture
def api_base_url():
    """
    Returns the base URL for the API in tests.
    """
    return "http://localhost:8000"
