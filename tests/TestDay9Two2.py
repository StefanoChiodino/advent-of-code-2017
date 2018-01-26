import unittest

from src import Day9Two


class TestDay9Two(unittest.TestCase):
    def test_example_(self):
        self.assertEqual(0, Day9Two.solve("<>"))

    def test_example_(self):
        self.assertEqual(17, Day9Two.solve("<random characters>"))

    def test_example_(self):
        self.assertEqual(3, Day9Two.solve("<<<<>"))

    def test_example_(self):
        self.assertEqual(2, Day9Two.solve("<{!>}>"))

    def test_example_(self):
        self.assertEqual(0, Day9Two.solve("<!!>"))

    def test_example_(self):
        self.assertEqual(0, Day9Two.solve("<!!!>>"))

    def test_example_(self):
        self.assertEqual(10, Day9Two.solve("<{o\"i!a,<{i<a>"))
