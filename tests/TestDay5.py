import unittest

from src.Day5 import day5a, day5b


class TestDay5(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(5, day5a([0, 3, 0, 1, -3]))

    def test_example_1(self):
        self.assertEqual(10, day5b([0, 3, 0, 1, -3]))
