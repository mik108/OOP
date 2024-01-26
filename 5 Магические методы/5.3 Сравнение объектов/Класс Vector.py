# Реализуйте класс Vector, описывающий вектор на плоскости.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented


    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"


a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)


v = Vector(x='11', y='12')
print(repr(v))