import math


class Point(object):
    """A Cartesian point (x, y) - all values are floats unless otherwise stated."""

    def __init__(self, x=0.0, y=0.0):
        """Initialise a point with x and y coordinates."""
        self.x = x
        self.y = y

    def distance(self, other):
        """Get the distance between self and another Point."""
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def sum(self, other):
        """Get the vector sum of self and another Point, return a Point instance."""
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        """Print a Point as a coordinate pair."""
        return "({:.2f}, {:.2f})".format(self.x, self.y)


x = float(input("Enter x value: "))
y = float(input("Enter y value: "))
p1 = Point(x, y)
print(p1)
