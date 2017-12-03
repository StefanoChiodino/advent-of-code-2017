import unittest

from src.day1 import day1a, day1b


class TestDay1(unittest.TestCase):
    def test_day1a_example_1(self):
        self.assertEqual(3, day1a("1122"))

    def test_day1a_example_2(self):
        self.assertEqual(4, day1a("1111"))

    def test_day1a_example_3(self):
        self.assertEqual(0, day1a("1234"))

    def test_day1a_example_4(self):
        self.assertEqual(9, day1a("91212129"))

    def test_day1b_example_1(self):
        self.assertEqual(6, day1b("1212"))

    def test_day1b_example_2(self):
        self.assertEqual(0, day1b("1221"))

    def test_day1b_example_3(self):
        self.assertEqual(4, day1b("123425"))

    def test_day1b_example_4(self):
        self.assertEqual(12, day1b("123123"))

    def test_day1b_example_5(self):
        self.assertEqual(4, day1b("12131415"))
