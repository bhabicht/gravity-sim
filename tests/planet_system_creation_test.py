import unittest
import sys

from Code.planet_system_creation import Massiveobject

sys.path.append('/home/benjamin/Documents/computer_science/gravity-sim')


class TestMassiveobject(unittest.TestCase):
    testobject = Massiveobject("testmass", 1, 2, 3, 4.1)

    def test_massiveobject_values(self):
        self.assertEqual("testmass", self.testobject.name)
        self.assertEqual(1, self.testobject.mass)
        self.assertEqual(2, self.testobject.x)
        self.assertEqual(3, self.testobject.v)
        self.assertEqual(4.1, self.testobject.F)
