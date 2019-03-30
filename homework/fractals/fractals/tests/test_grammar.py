import unittest

from fractals.grammar import Grammar


class GrammarTest(unittest.TestCase):
    def setUp(self):
        self.koch_axiom = "F-F-F-F"
        self.koch = {"F": "F-F+F+FF-F-F+F"}
        self.koch_alternate_axiom = "F+F+F+F"
        self.koch_a = {"F": "F+F+F-FFF-F"}
        self.koch_b = {"F": "FF+F+F+F+FF"}
        self.tree_axiom = "F"
        self.tree = {"F": "G[-F]G[+F]F", "G": "GG"}

    def test_passthrough_unknowns(self):
        g = Grammar(productions={"a": "b", "b": "c", "c": "a"})

        # 'd' is alphabetic, and not a known symbol.
        self.assertRaises(ValueError, g.apply, "abcd")
        # nonalphabetic symbols are passed through with no changes.
        self.assertEqual(g.apply("[]+-<>"), "[]+-<>")
        self.assertEqual(g.apply("a[]+-<>"), "b[]+-<>")
        # known alphabetic symbols get transformed.
        self.assertEqual(g.apply("abc"), "bca")

    def test_simple_iapply(self):
        g = Grammar(productions={"a": "c", "b": "ac", "c": "b"})
        axiom = "a"

        expecteds = [
            "c",
            "b",
            "ac",
            "cb",
            "bac",
            "accb",
            "cbbac",
            "bacaccb",
            "accbcbbac",
            "cbbacbacaccb",
            "bacaccbaccbcbbac",
        ]

        for actual, expected in zip(g.iapply(axiom=axiom), expecteds):
            self.assertEqual(actual, expected)

    def test_simple_apply(self):
        g = Grammar(productions={"a": "c", "b": "ac", "c": "b"})
        axiom = "a"

        expecteds = [
            "c",
            "b",
            "ac",
            "cb",
            "bac",
            "accb",
            "cbbac",
            "bacaccb",
            "accbcbbac",
            "cbbacbacaccb",
            "bacaccbaccbcbbac",
        ]

        for expected in expecteds:
            axiom = g.apply(axiom)
            self.assertEqual(axiom, expected)

    def test_bracketed(self):
        g = Grammar(productions=self.tree)

        expecteds = ["G[-F]G[+F]F", "GG[-G[-F]G[+F]F]GG[+G[-F]G[+F]F]G[-F]G[+F]F"]

        for actual, expected in zip(g.iapply(axiom=self.tree_axiom), expecteds):
            self.assertEqual(actual, expected)

    def test_large(self):
        g = Grammar(productions={"a": "aa", "b": "bb"})
        axiom = "a" * 2 + "b" * 2

        for power, result in zip(range(2, 16), g.iapply(axiom)):
            expected = "a" * (2 ** power) + "b" * (2 ** power)
            self.assertEqual(result, expected)
