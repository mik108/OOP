# Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, koef):
        return QuadraticPolynomial(*koef)

    @classmethod
    def from_str(cls, s):
        return QuadraticPolynomial(*map(float, s.split()))

polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)