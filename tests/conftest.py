"""Test configuration for Legacy Modernization Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "legacy-modernization-agent", "category": "Software Engineering"}
