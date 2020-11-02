import unittest
import scipy.constants as const
import sys
sys.path.append('/home/benjamin/Documents/computer_science/gravity-sim')

from Code.physical_functions import gravpot

class PotentialEnergyTestCase(unittest.TestCase):

    def test_grav(self):
        result = gravpot(0, 1, 1, 1)
        self.assertEqual(result, -const.G)