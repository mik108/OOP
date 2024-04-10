# Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
# x — координата точки по оси x
# y — координата точки по оси y
# color — цвет точки
# Класс ColoredPoint должен иметь три свойства:
#
# x — свойство, доступное только для чтения, возвращающее координату точки по оси x
# y — свойство, доступное только для чтения, возвращающее координату точки по оси y
# color — свойство, доступное только для чтения, возвращающее цвет точки
# Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
#
# ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
# Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения с помощью операторов == и !=.
# Две цветные точки считаются равными, если их цвета и координаты по обеим осям совпадают.
#
# Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение,
# вычисленное с помощью функции hash() на основе кортежа, первым элементом которого является координата точки по оси x, вторым — координата точки по оси y, третьим — цвет точки.

class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __eq__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return self._x == other._x and self._y == other._y and self._color == other._color

    def __ne__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self._x, self._y, self._color))

    def __repr__(self):
        return f"ColoredPoint({self._x!r}, {self._y!r}, {self._color!r})"