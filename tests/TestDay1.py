import unittest

from src.day1 import day1


class TestDay1(unittest.TestCase):

    def test_day1_example_1(self):
        self.assertEqual(3, day1("1122"))

    def test_day1_example_2(self):
        self.assertEqual(4, day1("1111"))

    def test_day1_example_3(self):
        self.assertEqual(0, day1("1234"))

    def test_day1_example_4(self):
        self.assertEqual(9, day1("91212129"))
