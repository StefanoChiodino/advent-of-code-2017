import unittest

from src.day2 import day2


class TestDay2(unittest.TestCase):

    def test_example_1(self):
        input = [[5, 1, 9, 5],
                 [7, 5, 3],
                 [2, 4, 6, 8]]
        self.assertEqual(18, day2(input))
