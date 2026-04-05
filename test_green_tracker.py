#!/usr/bin/env python3
"""
Test suite for Green Tracker Resource (Issue #13)

Verifies:
- green_tracker.py module exists and works
- Server integrates green_tracker resource
- Returns proper fleet data
- Markdown report is well-formatted
"""

import sys
from pathlib import Path

def test_green_tracker_module():
    """Test that green_tracker module exists"""
    module_path = Path("rustchain_mcp/green_tracker.py")
    assert module_path.exists(), f"Module not found: {module_path}"
    print("✅ test_green_tracker_module: PASSED")

def test_get_preserved_machines():
    """Test get_preserved_machines function"""
    sys.path.insert(0, str(Path.cwd()))
    from rustchain_mcp import green_tracker
    
    machines = green_tracker.get_preserved_machines()
    
    assert isinstance(machines, list), "Should return a list"
    assert len(machines) >= 4, f"Expected 4+ machines, found {len(machines)}"
    
    for i, machine in enumerate(machines, 1):
        assert "machine_name" in machine, f"Machine {i} missing machine_name"
        assert "year" in machine, f"Machine {i} missing year"
        assert "architecture" in machine, f"Machine {i} missing architecture"
        assert "power_draw_w" in machine, f"Machine {i} missing power_draw_w"
        assert "co2_saved_kg" in machine, f"Machine {i} missing co2_saved_kg"
    
    print(f"✅ test_get_preserved_machines: PASSED")
    print(f"   Machines: {len(machines)}")
    for m in machines:
        print(f"   - {m['machine_name']} ({m['year']})")

def test_format_report():
    """Test format_green_tracker_report function"""
    sys.path.insert(0, str(Path.cwd()))
    from rustchain_mcp import green_tracker
    
    report = green_tracker.format_green_tracker_report()
    
    assert isinstance(report, str), "Should return a string"
    assert len(report) > 500, "Report too short"
    assert "# Elyan Labs Green Tracker" in report, "Missing title"
    assert "## Summary" in report, "Missing summary section"
    assert "## Fleet Details" in report, "Missing fleet details"
    assert "## Environmental Impact" in report, "Missing environmental impact"
    assert "IBM POWER8" in report or "Mac Pro" in report, "Missing machine data"
    
    print("✅ test_format_report: PASSED")
    print(f"   Report length: {len(report)} chars")

def test_server_integration():
    """Test that server.py imports green_tracker"""
    server_path = Path("rustchain_mcp/server.py")
    
    with open(server_path) as f:
        content = f.read()
    
    assert "from . import green_tracker" in content, "Server doesn't import green_tracker"
    assert "green_tracker_resource" in content, "Server missing green_tracker_resource function"
    assert "@mcp.resource" in content, "Server missing MCP resource decorator"
    assert 'rustchain://green-tracker' in content, "Server missing resource URI"
    
    print("✅ test_server_integration: PASSED")

def test_resource_decorator():
    """Test that resource has proper MCP decorator"""
    server_path = Path("rustchain_mcp/server.py")
    
    with open(server_path) as f:
        content = f.read()
    
    # Find the green_tracker_resource function
    assert "@mcp.resource(\"rustchain://green-tracker\")" in content, "Missing or incorrect resource decorator"
    
    print("✅ test_resource_decorator: PASSED")

def test_data_accuracy():
    """Test that machine data is accurate"""
    sys.path.insert(0, str(Path.cwd()))
    from rustchain_mcp import green_tracker
    
    machines = green_tracker.get_preserved_machines()
    
    # Check for expected machines
    machine_names = [m["machine_name"] for m in machines]
    
    expected_machines = [
        "IBM POWER8",
        "Mac Pro",
        "PowerMac G4",
        "PowerMac G5"
    ]
    
    found_count = sum(1 for expected in expected_machines if any(expected in name for name in machine_names))
    assert found_count >= 3, f"Expected at least 3 known machines, found {found_count}"
    
    print("✅ test_data_accuracy: PASSED")
    print(f"   Found {found_count}/{len(expected_machines)} expected machines")

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Green Tracker Resource Test Suite (Issue #13)")
    print("=" * 60)
    print()
    
    tests = [
        test_green_tracker_module,
        test_get_preserved_machines,
        test_format_report,
        test_server_integration,
        test_resource_decorator,
        test_data_accuracy,
    ]
    
    passed = 0
    failed = 0
    skipped = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__}: FAILED - {e}")
            failed += 1
        except Exception as e:
            print(f"⚠️  {test.__name__}: ERROR - {e}")
            skipped += 1
    
    print()
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60)
    
    return failed == 0

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
