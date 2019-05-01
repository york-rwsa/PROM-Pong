import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setxy(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __div__(self, divisor):
        return Vector(self.x / divisor, self.y / divisor)

    def __mul__(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)

    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def unit_vector(self):
        return self / self.mag()

    @staticmethod
    def createUnitVector(angle):
        return Vector(math.cos(angle), math.sin(angle))
