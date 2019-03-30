import unittest

import numpy as np

from fractals.graphics import Graphics


@unittest.skip("Cannot test until Turtle3D is finished.")
class Test2DStraightSimple(unittest.TestCase):
    def setUp(self):
        self.start = np.array([0, 0, 0])
        self.radius = 0.2
        self.unit = 1
        self.angle = 45

    def test_single_command(self):
        g = Graphics(
            unit=self.unit, angle=self.angle, radius=self.radius, material=None, proportion=None
        )
        expected = {
            "from": self.start,
            "to": np.array([0, 0, self.unit]),
            "radius": self.radius,
            "material": None,
        }

        cylinders = g.draw("F")
        self.assertEqual(len(cylinders), 1)
        self.assertDictEqual(cylinders[0], expected)

        cylinders = g.draw("G")
        self.assertEqual(len(cylinders), 1)
        self.assertDictEqual(cylinders[0], expected)

    def test_unit(self):
        g = Graphics(
            unit=2 * self.unit, angle=self.angle, radius=self.radius, material=None, proportion=None
        )
        expected = {
            "from": self.start,
            "to": np.array([0, 0, 2 * self.unit]),
            "radius": self.radius,
            "material": None,
        }

        cylinders = g.draw("F")
        self.assertEqual(len(cylinders), 1)
        self.assertDictEqual(cylinders[0], expected)

    def test_init_args(self):
        # Constant and proportional radii are mutually exclusive.
        self.assertRaises(ValueError, Graphics, self.unit, self.angle, radius=1, proportion=1)
        g = Graphics(unit=self.unit, angle=self.angle)
        # Default radius.
        self.assertEqual(g.radius, 0.2)
        # Store angle in radians for math purposes.
        self.assertEqual(g.angle, np.radians(self.angle))

    def test_successive_forwards(self):
        g = Graphics(unit=self.unit, angle=self.angle, radius=self.radius)
        expected = {
            "from": self.start,
            "to": np.array([0, 0, 2 * self.unit]),
            "radius": self.radius,
            "material": None,
        }

        cylinders = g.draw("FF")
        # Successive 'forward's should join together.
        self.assertEqual(len(cylinders), 1)
        self.assertDictEqual(cylinders[0], expected)

        cylinders = g.draw("GG")
        # Successive 'forward's should join together.
        self.assertEqual(len(cylinders), 1)
        self.assertDictEqual(cylinders[0], expected)

        cylinders = g.draw("GFGF")
        # Successive 'forward's should join together.
        self.assertEqual(len(cylinders), 1)
        expected["to"] = np.array([0, 0, 4 * self.unit])
        self.assertDictEqual(cylinders[0], expected)

    def test_proportional_radius(self):
        # Make radius 10% of the length.
        p = 0.1
        g = Graphics(unit=self.unit, angle=self.angle, proportion=p)
        expected = {
            "from": self.start,
            # "to": np.array([0, 0, self.unit]),
            "radius": self.radius,
            "material": None,
        }
        for l in range(1, 10):
            expected["to"] = np.array([0, 0, l * self.unit])
            expected["radius"] = p * l
            cylinders = g.draw("F" * l)
            self.assertEqual(len(cylinders), 1)
            self.assertEqual(cylinders[0], expected)


@unittest.skip("One thing at a time...")
class Test2DSimpleForks(unittest.TestCase):
    def setUp(self):
        self.start = np.array([0, 0, 0])
        self.radius = 0.2
        self.unit = 2
        self.angle = 90

    def test_simple_right_elbow(self):
        g = Graphics(unit=self.unit, angle=self.angle)
        expected = [
            {
                "from": self.start,
                "to": np.array([0, 0, self.unit]),
                "radius": self.radius,
                "material": None,
            },
            {
                "from": np.array([0, 0, self.unit]),
                "to": np.array([0, self.unit, self.unit]),
                "radius": self.radius,
                "material": None,
            },
        ]
        cylinders = g.draw("F+F")
        self.assertEqual(len(cylinders), 2)

        for actual, expect in zip(cylinders, expected):
            self.assertDictEqual(actual, expect)

    def test_simple_left_elbow(self):
        g = Graphics(unit=self.unit, angle=self.angle)
        expected = [
            {
                "from": self.start,
                "to": np.array([0, 0, self.unit]),
                "radius": self.radius,
                "material": None,
            },
            {
                "from": np.array([0, 0, self.unit]),
                "to": np.array([0, -self.unit, self.unit]),
                "radius": self.radius,
                "material": None,
            },
        ]
        cylinders = g.draw("F-F")
        self.assertEqual(len(cylinders), 2)

        for actual, expect in zip(cylinders, expected):
            self.assertDictEqual(actual, expect)
