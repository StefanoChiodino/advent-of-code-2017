import unittest

from src.day3 import day3a


class TestDay3(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(0, day3a(1))

    def test_example_2(self):
        self.assertEqual(3, day3a(12))

    def test_example_3(self):
        self.assertEqual(2, day3a(23))

    def test_example_4(self):
        self.assertEqual(31, day3a(1024))
