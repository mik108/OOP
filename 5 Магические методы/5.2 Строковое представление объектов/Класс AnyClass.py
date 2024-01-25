# Реализуйте класс AnyClass. При создании экземпляра класс должен принимать произвольное количество именованных аргументов и устанавливать их в качестве атрибутов создаваемому экземпляру.
#
# Экземпляр класса AnyClass должен иметь следующее формальное строковое представление:
#
# AnyClass(<имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...)
# И следующее неформальное строковое представление:
#
# AnyClass: <имя 1-го атрибута>=<значение 1-го атрибута>, <имя 2-го атрибута>=<значение 2-го атрибута>, ...
# Примечание 1. Обратите внимание, что значения атрибутов, которые принадлежат типу str, должны быть обрамлены апострофами.
#
# Примечание 2. Никаких ограничений касательно реализации класса AnyClass нет, она может быть произвольной.

class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.atr = ", ".join([f'{i[0]}={repr(i[1])}' for i in kwargs.items()])

    def __str__(self):
        return f"{self.__class__.__name__}: {self.atr}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.atr})"

any = AnyClass()

print(str(any))
print(repr(any))

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))


