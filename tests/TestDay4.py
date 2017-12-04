import unittest

from src.Day4 import Day4


class TestDay4(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(1, len(Day4.get_valid_passphrases(["aa bb cc dd ee"])))

    def test_example_2(self):
        self.assertEqual(0, len(Day4.get_valid_passphrases(["aa bb cc dd aa"])))

    def test_example_3(self):
        self.assertEqual(1, len(Day4.get_valid_passphrases(["aa bb cc dd aaa"])))
