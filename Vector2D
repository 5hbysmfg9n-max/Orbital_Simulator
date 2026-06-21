# vector.py

import math


class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    # string representation (for debugging)
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # addition: v + w
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # subtraction: v - w
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # scalar multiplication: v * k
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    # scalar multiplication: k * v
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # scalar division: v / k
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    # magnitude |v|
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    # normalized vector v / |v|
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return self / mag