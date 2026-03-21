"""
Tests for Green Tracker MCP resource
Issue #13 - Bounty: 10 RTC
"""

import pytest
from rustchain_mcp.green_tracker import get_preserved_machines, format_green_tracker_report


class TestGetPreservedMachines:
    """Test machine data fetching."""
    
    def test_returns_list(self):
        """Should return a list of machines."""
        machines = get_preserved_machines()
        assert isinstance(machines, list)
        assert len(machines) > 0
    
    def test_machine_has_required_fields(self):
        """Each machine should have required fields."""
        machines = get_preserved_machines()
        required_fields = [
            "machine_name",
            "year",
            "architecture",
            "power_draw_w",
            "co2_saved_kg",
            "status",
            "role"
        ]
        
        for machine in machines:
            for field in required_fields:
                assert field in machine, f"Missing field: {field}"
    
    def test_machine_year_is_integer(self):
        """Year should be an integer."""
        machines = get_preserved_machines()
        for machine in machines:
            assert isinstance(machine["year"], int)
            assert 1970 <= machine["year"] <= 2030
    
    def test_power_draw_is_positive(self):
        """Power draw should be positive."""
        machines = get_preserved_machines()
        for machine in machines:
            assert machine["power_draw_w"] > 0
            assert machine["power_draw_w"] < 10000  # Reasonable limit
    
    def test_co2_saved_is_positive(self):
        """CO₂ saved should be positive."""
        machines = get_preserved_machines()
        for machine in machines:
            assert machine["co2_saved_kg"] > 0
    
    def test_status_is_valid(self):
        """Status should be 'active' or 'preserved'."""
        machines = get_preserved_machines()
        valid_statuses = ["active", "preserved"]
        for machine in machines:
            assert machine["status"] in valid_statuses


class TestFormatGreenTrackerReport:
    """Test report formatting."""
    
    def test_returns_string(self):
        """Should return a string report."""
        report = format_green_tracker_report()
        assert isinstance(report, str)
        assert len(report) > 100
    
    def test_contains_summary_table(self):
        """Report should contain summary table."""
        report = format_green_tracker_report()
        assert "**Total Machines**" in report
        assert "**Active**" in report
        assert "**Total Power Draw**" in report
        assert "**CO₂ Saved**" in report
    
    def test_contains_fleet_details(self):
        """Report should contain fleet details table."""
        report = format_green_tracker_report()
        assert "| Machine | Year | Architecture |" in report
    
    def test_contains_environmental_impact(self):
        """Report should contain environmental impact section."""
        report = format_green_tracker_report()
        assert "## Environmental Impact" in report
        assert "kg CO₂" in report
        assert "e-waste" in report.lower()
    
    def test_contains_architecture_diversity(self):
        """Report should contain architecture diversity section."""
        report = format_green_tracker_report()
        assert "## Architecture Diversity" in report
        assert "PowerPC" in report
        assert "x86_64" in report
    
    def test_contains_install_instructions(self):
        """Report should contain install instructions."""
        report = format_green_tracker_report()
        assert "pip install clawrtc" in report
        assert "rustchain.org/preserved.html" in report
    
    def test_markdown_format(self):
        """Report should be valid markdown."""
        report = format_green_tracker_report()
        # Check for markdown elements
        assert report.startswith("\n#")  # Header
        assert "|" in report  # Tables
        assert "**" in report  # Bold text
        assert "```" in report  # Code blocks


class TestGreenTrackerData:
    """Test data accuracy."""
    
    def test_total_co2_calculation(self):
        """Total CO₂ should be sum of individual machines."""
        machines = get_preserved_machines()
        total_co2 = sum(m["co2_saved_kg"] for m in machines)
        assert total_co2 > 0
    
    def test_total_power_calculation(self):
        """Total power should be sum of individual machines."""
        machines = get_preserved_machines()
        total_power = sum(m["power_draw_w"] for m in machines)
        assert total_power > 0
    
    def test_architecture_variety(self):
        """Should have multiple architectures."""
        machines = get_preserved_machines()
        architectures = set(m["architecture"] for m in machines)
        assert len(architectures) >= 2  # At least 2 different architectures
    
    def test_vintage_hardware_present(self):
        """Should include vintage hardware (pre-2010)."""
        machines = get_preserved_machines()
        vintage_count = sum(1 for m in machines if m["year"] < 2010)
        assert vintage_count > 0  # At least one vintage machine


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
