import numpy as np


class Graphics:
    """Interprets Lindenmayer graphics command strings to generate 3D cylinders.

    TODO: Add graphics command string specification and examples.
    """

    @staticmethod
    def __check_args(radius, proportion):
        if radius is not None and proportion is not None:
            raise ValueError("`radius` and `proportion` are mutually exclusive.")

    def __init__(self, unit, angle, material=None, radius=None, proportion=None):
        """Initialize a Graphics object to draw command strings for fractals.

        If neither a radius or a proportionality constant is given, default to a constant radius
        of 0.2.

        :param unit: The length of each 'forward' command.
        :param angle: The angle of each 'rotate' and 'bend' command. In degrees.
        :param material: The Blender material to make each cylinder object with, defaults to None.
        :param radius: The radius of each cylinder. Mutually exclusive with `proportion`.
        :param proportion: Make each cylinder's radius proportional to its length. Mutually
        exclusive with `radius`.
        """
        self.__check_args(radius, proportion)

        self.unit = unit
        self.angle = np.radians(angle)
        self.material = material
        self.radius = radius if radius is not None else 0.2
        self.proportion = proportion

    def draw(self, commands):
        """Generate the 3D cylinders from the given graphics commands.

        :param commands: A string of successive graphics commands.
        :return: A list of cylinder dictionaries.
        """
        return [{}]
