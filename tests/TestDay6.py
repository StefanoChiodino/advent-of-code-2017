import unittest

from src.day6 import day6


class TestDay6(unittest.TestCase):
    def test_example(self):
        input = [0, 2, 7, 0]
        self.assertEqual(5, day6(input))