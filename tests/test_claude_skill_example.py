"""
Tests for Claude Code skill example
Issue #14 - Bounty: 5 RTC
"""

import pytest
import os
from pathlib import Path


class TestClaudeSkillExample:
    """Test Claude Code skill example file."""
    
    def test_skill_file_exists(self):
        """Skill file should exist."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        assert skill_path.exists(), f"Skill file not found: {skill_path}"
    
    def test_skill_file_not_empty(self):
        """Skill file should not be empty."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert len(content) > 100, "Skill file is too short"
    
    def test_skill_has_setup_section(self):
        """Skill file should have setup instructions."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "## Setup" in content, "Missing setup section"
        assert "pip install" in content, "Missing pip install command"
    
    def test_skill_has_tools_section(self):
        """Skill file should document available tools."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "## Available Tools" in content, "Missing tools section"
        assert "rustchain_health" in content, "Missing rustchain_health tool"
        assert "rustchain_epoch" in content, "Missing rustchain_epoch tool"
        assert "rustchain_miners" in content, "Missing rustchain_miners tool"
        assert "rustchain_create_wallet" in content, "Missing rustchain_create_wallet tool"
        assert "rustchain_balance" in content, "Missing rustchain_balance tool"
        assert "rustchain_stats" in content, "Missing rustchain_stats tool"
    
    def test_skill_has_code_examples(self):
        """Skill file should have code examples."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "```python" in content, "Missing Python code examples"
        assert "rustchain_" in content, "Missing tool usage examples"
    
    def test_skill_has_workflows_section(self):
        """Skill file should have common workflows."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "## Common Workflows" in content or "Workflow" in content, "Missing workflows section"
    
    def test_skill_has_api_reference(self):
        """Skill file should have API reference."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "## API Reference" in content or "rustchain.org" in content, "Missing API reference"
    
    def test_skill_has_wallet_info(self):
        """Skill file should have wallet info for bounty."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "Dlove123" in content, "Missing wallet name"
        assert "RTCb72a1accd46b9ba9f22dbd4b5c6aad5a5831572b" in content, "Missing RTC address"


class TestMCPConfigExample:
    """Test MCP config example."""
    
    def test_config_example_in_skill(self):
        """Skill file should have MCP config example."""
        skill_path = Path(__file__).parent.parent / ".claude" / "skills" / "rustchain.md"
        content = skill_path.read_text()
        assert "mcpServers" in content, "Missing MCP config example"
        assert "rustchain" in content, "Missing rustchain server config"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
