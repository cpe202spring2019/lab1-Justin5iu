import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc4 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc == loc4)
        self.assertFalse(loc == loc2)

    def test_init(self):
        loc = Location("SF", 37.8, -122.4)
        self.assertEqual(loc.name, "SF")
        self.assertEqual(loc.lat, 37.8)
        self.assertEqual(loc.lon, -122.4)

if __name__ == "__main__":
        unittest.main()
