# Реализуйте класс FoodInfo, описывающий пищевую ценность продуктов. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# Экземпляр класса FoodInfo должен иметь три атрибута:
#
# proteins — количество белков в граммах
# fats — количество жиров в граммах
# carbohydrates — количество углеводов в граммах
# И следующее формальное строковое представление:
#
# FoodInfo(<количество белков>, <количество жиров>, <количество углеводов>)
# Также экземпляры класса FoodInfo должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса FoodInfo с суммарным количеством белков, жиров и углеводов исходных экземпляров.
#
# Наконец, экземпляр класса FoodInfo должен поддерживать операции умножения, деления и деления нацело на число n с помощью операторов *, / и // соответственно:
#
# результатом умножения должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого умножены на n
# результатом деления должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены на n
# результатом деления нацело должен являться новый экземпляр класса FoodInfo, количество белков, жиров и углеводов которого поделены нацело на n

class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'{self.__class__.__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) in [int, float]:
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        else:
            return NotImplemented

    def __floordiv__(self, other):
        if type(other) in [int, float]:
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        else:
            return NotImplemented


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)

food1 = FoodInfo(10, 20, 30)

try:
    food2 = (5, 10, 15) + food1
except TypeError:
    print('Некорректный тип данных')