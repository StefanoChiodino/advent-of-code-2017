import unittest

from src.day1 import day1


class TestDay1(unittest.TestCase):

    def test_day1_example1(self):
        self.assertEqual(day1("1122"), 3)

    def test_day1_example2(self):
        self.assertEqual(day1("1111"), 4)

    def test_day1_example3(self):
        self.assertEqual(day1("1234"), 0)

    def test_day1_example4(self):
        self.assertEqual(day1("91212129"), 9)
