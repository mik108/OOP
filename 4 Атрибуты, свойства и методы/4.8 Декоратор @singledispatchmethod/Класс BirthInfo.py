# Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:
#
# birth_date — дата рождения, представленная в одном из следующих вариантов:
# экземпляр класса date
# строка с датой в ISO формате
# список или кортеж из трех целых чисел: года, месяца и дня
# Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:
#
# Аргумент переданного типа не поддерживается
# Экземпляр класса BirthInfo должен иметь один атрибут:
#
# birth_date — дата рождения в виде экземпляра класса date
# Класс BirthInfo должен иметь одно свойство:
#
# age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день

import re
from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _(self, birth_date):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', birth_date):
            raise TypeError('Аргумент переданного типа не поддерживается')
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, birth_date):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age

birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)



