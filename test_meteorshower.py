# test_meteorshower.py
"""
Tests for MeteorShower module.
"""

import unittest
from meteorshower import MeteorShower

class TestMeteorShower(unittest.TestCase):
    """Test cases for MeteorShower class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MeteorShower()
        self.assertIsInstance(instance, MeteorShower)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MeteorShower()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
