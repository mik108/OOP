# Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Formatter должен иметь один статический метод:
#
# format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.
#
# Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые элементы коллекций.
#
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть произвольной.

from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def int_format(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def float_format(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def tuple_format(data):
        print(f'Элементы кортежа: ', end ='')
        print(*data, sep=', ')

    @format.register(list)
    @staticmethod
    def list_format(data):
        print(f'Элементы списка: ', end ='')
        print(*data, sep=', ')

    @format.register(dict)
    @staticmethod
    def dict_format(data):
        print(f'Пары словаря: ', end ='')
        print(*data.items(), sep=', ')

Formatter.format(1337)
Formatter.format(20.77)
Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})


