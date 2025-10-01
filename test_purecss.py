# test_purecss.py
"""
Tests for PureCss module.
"""

import unittest
from purecss import PureCss

class TestPureCss(unittest.TestCase):
    """Test cases for PureCss class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PureCss()
        self.assertIsInstance(instance, PureCss)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PureCss()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
