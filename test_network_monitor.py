#!/usr/bin/env python3
"""
Test script for Network Monitoring Tool
Validates that all functions work correctly
"""

import sys
import unittest
from network_monitor import NetworkMonitor


class TestNetworkMonitor(unittest.TestCase):
    """Test cases for NetworkMonitor class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.monitor = NetworkMonitor()
    
    def test_initialization(self):
        """Test that NetworkMonitor initializes properly"""
        self.assertIsNotNone(self.monitor)
        self.assertIsNotNone(self.monitor.os_type)
        self.assertIsInstance(self.monitor.results, dict)
        print("✓ Initialization test passed")
    
    def test_check_internet_connection(self):
        """Test internet connection check"""
        result = self.monitor.check_internet_connection()
        self.assertIsInstance(result, bool)
        print(f"✓ Internet connection test passed: {result}")
    
    def test_grade_signal(self):
        """Test WiFi signal grading system"""
        # Test excellent signal
        grade = self.monitor.grade_signal(85)
        self.assertIn("Xuất sắc", grade)
        
        # Test good signal
        grade = self.monitor.grade_signal(65)
        self.assertIn("Tốt", grade)
        
        # Test average signal
        grade = self.monitor.grade_signal(45)
        self.assertIn("Trung bình", grade)
        
        # Test weak signal
        grade = self.monitor.grade_signal(25)
        self.assertIn("Yếu", grade)
        
        # Test very weak signal
        grade = self.monitor.grade_signal(10)
        self.assertIn("Rất yếu", grade)
        
        print("✓ Signal grading test passed")
    
    def test_grade_network_speed(self):
        """Test network speed grading system"""
        # Test excellent speed
        grade = self.monitor.grade_network_speed(15, 60)
        self.assertIn("/100", grade)
        self.assertTrue(any(letter in grade for letter in ["A", "B", "C", "D", "F"]))
        
        # Test with no data
        grade = self.monitor.grade_network_speed(None, None)
        self.assertIn("/100", grade)
        
        print("✓ Network speed grading test passed")
    
    def test_check_network_config(self):
        """Test network configuration check"""
        config = self.monitor.check_network_config()
        
        if config:
            self.assertIn('hostname', config)
            self.assertIn('ip_address', config)
            self.assertIn('internet_connected', config)
            print("✓ Network config test passed")
        else:
            print("⚠ Network config test skipped (may require permissions)")
    
    def test_check_wifi_signal(self):
        """Test WiFi signal check"""
        wifi = self.monitor.check_wifi_signal()
        
        # WiFi may not be available in test environment
        self.assertIsInstance(wifi, dict)
        print("✓ WiFi signal test passed (checked return type)")
    
    def test_test_network_speed(self):
        """Test network speed testing"""
        speed = self.monitor.test_network_speed()
        
        self.assertIsInstance(speed, dict)
        self.assertIn('speed_grade', speed)
        print("✓ Network speed test passed")
    
    def test_check_firewall(self):
        """Test firewall status check"""
        firewall = self.monitor.check_firewall()
        
        self.assertIsInstance(firewall, dict)
        print("✓ Firewall check test passed")
    
    def test_generate_report(self):
        """Test report generation"""
        # Run some checks first
        self.monitor.check_network_config()
        
        # Generate report (should not raise exception)
        try:
            self.monitor.generate_report()
            print("✓ Report generation test passed")
        except Exception as e:
            self.fail(f"Report generation failed: {e}")
    
    def test_run_all_checks(self):
        """Test running all checks at once"""
        results = self.monitor.run_all_checks()
        
        self.assertIsInstance(results, dict)
        print("✓ Run all checks test passed")


def run_manual_tests():
    """Run manual tests that show actual output"""
    print("\n" + "="*60)
    print("MANUAL FUNCTIONALITY TESTS")
    print("="*60)
    
    monitor = NetworkMonitor()
    
    print("\n1. Testing signal grading:")
    for strength in [95, 75, 55, 35, 15]:
        grade = monitor.grade_signal(strength)
        print(f"   Signal {strength}% → {grade}")
    
    print("\n2. Testing speed grading:")
    test_cases = [
        (10, 80, "Fast connection, low latency"),
        (100, 15, "Slow connection, high latency"),
        (50, 25, "Medium connection"),
        (None, None, "No data available"),
    ]
    for latency, speed, desc in test_cases:
        grade = monitor.grade_network_speed(latency, speed)
        print(f"   {desc}: {grade}")
    
    print("\n3. Testing OS detection:")
    print(f"   Detected OS: {monitor.os_type}")
    
    print("\n" + "="*60)
    print("✓ All manual tests completed")
    print("="*60)


if __name__ == '__main__':
    print("="*60)
    print("NETWORK MONITOR TEST SUITE")
    print("="*60)
    
    # Run unit tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNetworkMonitor)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Run manual tests
    if result.wasSuccessful():
        run_manual_tests()
        print("\n✓ ALL TESTS PASSED!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed")
        sys.exit(1)
