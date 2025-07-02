#!/usr/bin/env python3
"""
Unit tests for the sample application
"""

import unittest
import sys
import os

# Add the src directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import (
    get_current_time, 
    validate_input, 
    format_message, 
    calculate_statistics, 
    process_data, 
    log_event
)
from config import APP_NAME, VERSION, FEATURES


class TestUtils(unittest.TestCase):
    """Test cases for utility functions"""
    
    def test_validate_input_valid(self):
        """Test validate_input with valid inputs"""
        valid_inputs = [
            "John Doe",
            "Alice",
            "Bob-Smith", 
            "Mary_Jane",
            "Dr. Johnson"
        ]
        
        for input_str in valid_inputs:
            with self.subTest(input_str=input_str):
                self.assertTrue(validate_input(input_str))
    
    def test_validate_input_invalid(self):
        """Test validate_input with invalid inputs"""
        invalid_inputs = [
            "",
            None,
            123,
            "John@Doe",
            "Alice#Smith",
            "Bob$Jones"
        ]
        
        for input_str in invalid_inputs:
            with self.subTest(input_str=input_str):
                self.assertFalse(validate_input(input_str))
    
    def test_get_current_time(self):
        """Test get_current_time returns proper format"""
        timestamp = get_current_time()
        self.assertIsInstance(timestamp, str)
        self.assertIn("UTC", timestamp)
        # Check format: YYYY-MM-DD HH:MM:SS UTC
        parts = timestamp.split()
        self.assertEqual(len(parts), 3)
        self.assertEqual(parts[2], "UTC")
    
    def test_format_message(self):
        """Test format_message function"""
        message = "Test message"
        formatted = format_message(message)
        
        self.assertIn("System:", formatted)
        self.assertIn(message, formatted)
        self.assertIn("UTC", formatted)
        
        # Test with custom author
        custom_formatted = format_message(message, "Travis")
        self.assertIn("Travis:", custom_formatted)
        self.assertIn(message, custom_formatted)
    
    def test_calculate_statistics(self):
        """Test calculate_statistics function"""
        numbers = [1, 2, 3, 4, 5]
        stats = calculate_statistics(numbers)
        
        expected_stats = {
            'count': 5,
            'sum': 15,
            'average': 3.0,
            'min': 1,
            'max': 5
        }
        
        self.assertEqual(stats, expected_stats)
    
    def test_calculate_statistics_empty(self):
        """Test calculate_statistics with empty list"""
        stats = calculate_statistics([])
        self.assertEqual(stats, {})
    
    def test_process_data_string(self):
        """Test process_data with string input"""
        input_str = "hello world"
        result = process_data(input_str)
        self.assertEqual(result, "HELLO WORLD")
    
    def test_process_data_list(self):
        """Test process_data with list input"""
        input_list = ["hello", "world", 123]
        result = process_data(input_list)
        expected = ["HELLO", "WORLD", 123]
        self.assertEqual(result, expected)
    
    def test_process_data_other(self):
        """Test process_data with other input types"""
        inputs = [123, None, {"key": "value"}]
        for input_data in inputs:
            with self.subTest(input_data=input_data):
                result = process_data(input_data)
                self.assertEqual(result, input_data)
    
    def test_log_event(self):
        """Test log_event function"""
        event_type = "test"
        message = "Test message"
        log_entry = log_event(event_type, message)
        
        self.assertIn("TEST:", log_entry)
        self.assertIn(message, log_entry)
        self.assertIn("UTC", log_entry)


class TestConfig(unittest.TestCase):
    """Test cases for configuration values"""
    
    def test_app_constants(self):
        """Test application constants"""
        self.assertEqual(APP_NAME, "GitHub Webhook Test Application")
        self.assertEqual(VERSION, "1.0.0")
    
    def test_features_config(self):
        """Test features configuration"""
        self.assertIsInstance(FEATURES, dict)
        self.assertIn("user_authentication", FEATURES)
        self.assertIn("data_validation", FEATURES)
        
        # Test that features are boolean values
        for feature, enabled in FEATURES.items():
            with self.subTest(feature=feature):
                self.assertIsInstance(enabled, bool)


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_workflow_simulation(self):
        """Simulate a typical workflow"""
        # Validate user input
        user_name = "Travis"
        self.assertTrue(validate_input(user_name))
        
        # Format a message
        message = format_message("User logged in", user_name)
        self.assertIn("Travis:", message)
        
        # Process some data
        data = ["feature", "development"]
        processed = process_data(data)
        self.assertEqual(processed, ["FEATURE", "DEVELOPMENT"])
        
        # Calculate statistics
        test_numbers = [10, 20, 30, 40, 50]
        stats = calculate_statistics(test_numbers)
        self.assertEqual(stats['average'], 30.0)
        
        # Log the completion
        log_entry = log_event("workflow", "Integration test completed")
        self.assertIn("WORKFLOW:", log_entry)


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2)