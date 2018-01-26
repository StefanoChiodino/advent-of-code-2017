import unittest

from src.Day9One import Day9One


class TestDay9One(unittest.TestCase):
    def test_sanitise_string(self):
        self.assertEqual("{}", Day9One().sanitise_stream("{<abc123>}"))
        self.assertEqual("{}", Day9One().sanitise_stream("{<!abc123>}"))
        self.assertEqual("{}", Day9One().sanitise_stream("{<ab!>c123>}"))
        self.assertEqual("{}", Day9One().sanitise_stream("{<!!abc123>}"))
        self.assertEqual("{}", Day9One().sanitise_stream("{}"))
        self.assertEqual("{{}{}}", Day9One().sanitise_stream("{{<{!}!>{>},{<fadfas!!!>fdasf>}}"))
        self.assertEqual("", Day9One().sanitise_stream(""))

    def test_example_1(self):
        stream = "{}"
        self.assertEqual(1, Day9One().day9(stream))

    def test_example_2(self):
        stream = "{{{}}}"
        self.assertEqual(6, Day9One().day9(stream))

    def test_example_3(self):
        stream = "{{},{}}"
        self.assertEqual(5, Day9One().day9(stream))

    def test_example_4(self):
        stream = "{{{},{},{{}}}}"
        self.assertEqual(16, Day9One().day9(stream))

    def test_example_5(self):
        stream = "{<a>,<a>,<a>,<a>}"
        self.assertEqual(1, Day9One().day9(stream))

    def test_example_6(self):
        stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
        self.assertEqual(9, Day9One().day9(stream))

    def test_example_7(self):
        stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
        self.assertEqual(9, Day9One().day9(stream))

    def test_example_6(self):
        stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
        self.assertEqual(3, Day9One().day9(stream))
