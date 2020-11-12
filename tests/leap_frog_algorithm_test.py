import unittest
import numpy as np
import sys
sys.path.append('/home/benjamin/Documents/computer_science/gravity-sim')

import scipy.constants as const

from Code.leap_frog_algorithm import update_all_positions, calculate_all_forces
from Code.planet_system_creation import Massiveobject

class TestUpdateAllPositions(unittest.TestCase):
    obj1 = Massiveobject("obj1", 1, 0, 3, 10)
    obj2 = Massiveobject("obj2", 2, 1, 4, 30)
    obj3 = Massiveobject("obj3", 3, 2, 4, 30)
    def test_update_all_positions(self):
        self.assertEqual(self.obj1.x, 0)
        self.assertEqual(self.obj2.x, 1)
        self.assertEqual(self.obj3.x, 2)
        update_all_positions(0.5, [self.obj1, self.obj2, self.obj3])
        self.assertEqual(self.obj1.x, 0.75)
        self.assertEqual(self.obj2.x, 2)
        self.assertEqual(self.obj3.x, 3)

class TestCalculateAllForces(unittest.TestCase):
    obj1 = Massiveobject("obj1", 1, np.array([0,0,0]), np.array([3,0,0]), np.array([10,0,0]))
    obj2 = Massiveobject("obj2", 2, np.array([1,0,0]), np.array([4,0,0]), np.array([30,0,0]))
    obj3 = Massiveobject("obj3", 3, np.array([2,0,0]), np.array([4,0,0]), np.array([30,0,0]))
    def test_calculate_all_forces(self):
        calculate_all_forces([self.obj1, self.obj2, self.obj3])
        self.assertTrue(np.array_equal(self.obj1.F, np.array([11/4*const.G,0,0])))
        self.assertTrue(np.array_equal(self.obj2.F, np.array([4*const.G,0,0])))
        self.assertTrue(np.array_equal(self.obj3.F, np.array([-27/4*const.G,0,0])))