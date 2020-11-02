import unittest
from justgrav import gravpot
import scipy.constants as const

class PotentialEnergyTestCase(unittest.TestCase):

    def test_grav(self):
        result = gravpot(0, 1, 1, 1)
        self.assertEqual(result, -const.G)