# Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен принимать один аргумент:
#
# number — число в римской системе счисления. Например, IV
# Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:
#
# <число в римской системе счисления>
# Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому его значением должно являться целое число в десятичной системе счисления, которому он соответствует.
#
# Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=.
#
# Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью операторов + и - соответственно:
#
# результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
# результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
# Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.

# class RomanNumeral:
#     def __init__(self, number):
#         self.number = number


from functools import total_ordering


@total_ordering
class RomanNumeral:
    ROMANS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
              'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
              'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, number):
        self.roman = number
        self.number = self.to_arabian(number)

    @staticmethod
    def to_arabian(val):
        res = 0
        for roman, arabic in RomanNumeral.ROMANS.items():
            while val.startswith(roman):
                res += arabic
                val = val.replace(roman, '', 1)
        return res

    @staticmethod
    def to_roman(val):
        res = ''
        for roman, arabic in RomanNumeral.ROMANS.items():
            while val >= arabic:
                res += roman
                val -= arabic
        return res

    def __str__(self):
        return self.roman

    def __int__(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.number < other.number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.to_roman(self.number + other.number))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.to_roman(self.number - other.number))
        return NotImplemented

number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)

number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)