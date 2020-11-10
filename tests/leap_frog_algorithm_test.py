import unittest
import numpy as np
import sys
sys.path.append('/home/benjamin/Documents/computer_science/gravity-sim')

from Code.leap_frog_algorithm import update_all_positions
from Code.planet_system_creation import Massiveobject

class TestUpdateAllPositions(unittest.TestCase):
    obj1 = Massiveobject("obj1", 1, 2, 3, 10)
    obj2 = Massiveobject("obj2", 2, 3, 4, 30)
    def test_update_all_positions(self):
        self.assertEqual(self.obj1.x, 2)
        self.assertEqual(self.obj2.x, 3)
        update_all_positions(0.5, [self.obj1, self.obj2])
        self.assertEqual(self.obj1.x, 2.75)
        self.assertEqual(self.obj2.x, 4)