import unittest

from src.day2 import day2a, day2b


class TestDay2(unittest.TestCase):

    def test_example_1(self):
        input = [[5, 1, 9, 5],
                 [7, 5, 3],
                 [2, 4, 6, 8]]
        self.assertEqual(18, day2a(input))

    def test_example_2(self):
        input = [[5, 9, 2, 8],
                 [9, 4, 7, 3],
                 [3, 8, 6, 5]]
        self.assertEqual(9, day2b(input))
