import unittest

from src.day7 import day7


class TestDay7(unittest.TestCase):
    # noinspection SpellCheckingInspection
    def test_example(self):
        input = ["pbga (66)",
                 "xhth (57)",
                 "ebii (61)",
                 "havc (66)",
                 "ktlj (57)",
                 "fwft (72) -> ktlj, cntj, xhth",
                 "qoyq (66)",
                 "padx (45) -> pbga, havc, qoyq",
                 "tknk (41) -> ugml, padx, fwft",
                 "jptl (61)",
                 "ugml (68) -> gyxo, ebii, jptl",
                 "gyxo (61)",
                 "cntj (57)"]
        self.assertEqual("tknk", day7(input))
