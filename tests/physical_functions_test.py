import unittest
import scipy.constants as const
import sys

from code.physical_functions import gravpot
from code.physical_functions import gravforce

sys.path.append('/home/benjamin/Documents/computer_science/gravity-sim')


class TestGravpot(unittest.TestCase):
    def test_gravpot_success(self):
        actual = gravpot(0, 1, 1, 1)
        expected = -const.G
        self.assertEqual(actual, expected)

    def test_gravpot_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            gravpot(0, 0, 1, 1)
        self.assertEqual(
            str(exception_context.exception),
            "Division by 0 Error"
        )


class TestGravforce(unittest.TestCase):
    def test_gravforce_success(self):
        actual = gravforce(0, 1, 1, 1)
        expected = const.G
        self.assertEqual(actual, expected)

    def test_gravforce_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            gravpot(0, 0, 1, 1)
        self.assertEqual(
            str(exception_context.exception),
            "Division by 0 Error"
        )
