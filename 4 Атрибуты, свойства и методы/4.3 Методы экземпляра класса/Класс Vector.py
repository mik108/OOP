# Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        abs = (self.x ** 2 + self.y ** 2) ** 0.5
        return abs

vector = Vector()

print(vector.x, vector.y)
print(vector.abs())

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())