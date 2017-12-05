import unittest

from src.Day5 import day5


class TestDay5(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(5, day5([0, 3, 0, 1, -3]))
