#Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, args):
        self.a, self.b, self.c = args

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')



polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)
