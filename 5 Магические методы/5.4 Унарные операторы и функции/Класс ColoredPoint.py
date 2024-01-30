# Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости.

class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(map(lambda x: 255 -x, self.color)))

point = ColoredPoint(2, -3)

print(+point)
print(-point)
print(~point)

point1 = ColoredPoint(2, -3)
point2 = ColoredPoint(10, 20, (34, 45, 67))

print(point1.color)
print(point2.color)

point1 = ColoredPoint(1, 2, (100, 150, 200))
point2 = ~point1

print(repr(point1))
print(repr(point2))