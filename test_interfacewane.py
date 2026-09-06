# test_interfacewane.py
"""
Tests for InterfaceWane module.
"""

import unittest
from interfacewane import InterfaceWane

class TestInterfaceWane(unittest.TestCase):
    """Test cases for InterfaceWane class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InterfaceWane()
        self.assertIsInstance(instance, InterfaceWane)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InterfaceWane()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
