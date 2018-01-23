import unittest

from src.Day9 import Day9


class TestDay9(unittest.TestCase):
    def test_sanitise_string(self):
        self.assertEqual("{}", Day9().sanitise_stream("{<abc123>}"))
        self.assertEqual("{}", Day9().sanitise_stream("{<!abc123>}"))
        self.assertEqual("{}", Day9().sanitise_stream("{<ab!>c123>}"))
        self.assertEqual("{}", Day9().sanitise_stream("{<!!abc123>}"))
        self.assertEqual("{}", Day9().sanitise_stream("{}"))
        self.assertEqual("{{}{}}", Day9().sanitise_stream("{{<{!}!>{>},{<fadfas!!!>fdasf>}}"))
        self.assertEqual("", Day9().sanitise_stream(""))

    def test_example_1(self):
        stream = "{}"
        self.assertEqual(1, Day9().day9(stream))

    def test_example_2(self):
        stream = "{{{}}}"
        self.assertEqual(6, Day9().day9(stream))

    def test_example_3(self):
        stream = "{{},{}}"
        self.assertEqual(5, Day9().day9(stream))

    def test_example_4(self):
        stream = "{{{},{},{{}}}}"
        self.assertEqual(16, Day9().day9(stream))

    def test_example_5(self):
        stream = "{<a>,<a>,<a>,<a>}"
        self.assertEqual(1, Day9().day9(stream))

    def test_example_6(self):
        stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
        self.assertEqual(9, Day9().day9(stream))

    def test_example_7(self):
        stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
        self.assertEqual(9, Day9().day9(stream))

    def test_example_6(self):
        stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
        self.assertEqual(3, Day9().day9(stream))
