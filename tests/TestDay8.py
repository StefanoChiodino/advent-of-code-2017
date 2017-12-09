import unittest

from src.day8 import day8


class TestDay8(unittest.TestCase):
    def test_example(self):
        instructions = ["b inc 5 if a > 1",
                        "a inc 1 if b < 5",
                        "c dec -10 if a >= 1",
                        "c inc -20 if c == 10"]
        self.assertEqual(1, day8(instructions))
