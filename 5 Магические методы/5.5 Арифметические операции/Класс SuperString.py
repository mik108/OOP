# Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
#
# string — значение строки
# Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
#
# <значение строки>
# Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.
#
# Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
#
# результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n
# результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
# результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
# результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
# Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.
#
# Примечание 1. Будем гарантировать, что экземпляр класса SuperString всегда делится на ненулевое число.
#
# Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 3. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной.

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) is int:
            return SuperString(self.string * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) is int:
            return SuperString(self.string[:len(self.string) // other])
        else:
            return NotImplemented

    def __lshift__(self,n):
        if isinstance(n,int):
            if n >= len(self.string):
                return SuperString('')
            else:
                n = len(self.string)-n
                return SuperString(self.string[:n])
        else:
            return NotImplemented

    def __rshift__(self, other):
        if type(other) is int:
            return SuperString(self.string[other:])
        return NotImplemented


s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)

s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)