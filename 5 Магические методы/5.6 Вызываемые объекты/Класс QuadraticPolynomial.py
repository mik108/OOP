# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# a — коэффициент  a квадратного трехчлена
# b — коэффициент  b квадратного трехчлена
# c — коэффициент  c квадратного трехчлена
# Экземпляр класса QuadraticPolynomial должен являться вызываемым объектом и принимать один аргумент:
#
# x — число

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c

func = QuadraticPolynomial(1, 2, 1)

print(func(1))
print(func(2))

func = QuadraticPolynomial(1, 3, 4)

print(func(1))
print(func(2))