from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Built-in the string representation of the object for inspection
    def __repr__(self): 
        return 'Vector(x=%r, y=%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3, 4)
print(abs(v1))
print(abs(v1 *3))

v2 = Vector(2, 1)

print(v1+v2)
