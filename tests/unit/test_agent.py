"""Legacy Modernization Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_monolith():
    """Test Analyze monolithic codebase for coupling, cohesion, and boundaries."""
    tools = AgentTools()
    result = await tools.analyze_monolith(project_root="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_bounded_contexts():
    """Test Identify DDD bounded contexts and aggregate roots."""
    tools = AgentTools()
    result = await tools.identify_bounded_contexts(codebase_analysis="test", domain_events="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_extraction_plan():
    """Test Plan microservice extraction using strangler fig pattern."""
    tools = AgentTools()
    result = await tools.generate_extraction_plan(bounded_context="test", dependencies="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_anti_corruption_layer():
    """Test Generate ACL between legacy and new service."""
    tools = AgentTools()
    result = await tools.generate_anti_corruption_layer(legacy_api="test", new_api="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.legacy_modernization_agent_agent import LegacyModernizationAgentAgent
    agent = LegacyModernizationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
