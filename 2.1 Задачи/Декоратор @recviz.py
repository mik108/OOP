# Реализуйте декоратор @recviz, который полностью визуализирует выполнение декорируемой функции, в том числе и рекурсивной. Декоратор должен отображать все рекурсивные вызовы и возвращаемые значения, полученные при этих вызовах, причем рекурсивные вызовы, выполняемые в глубину, должны отделяться друг от друга четырьмя пробелами.
#
# Очередной вызов декорируемой функции при визуализации должен включать в себя знак ->, имя декорируемой функции и аргументы, переданные при этом вызове. Возвращаемое значение при визуализации должно включать в себя знак <- и непосредственно само возвращаемое значение.
#
# Примечание 1. Рекурсивный вызов и возвращаемое значение, полученное при этом вызове, должны находиться на одном уровне отступов.
#
# Примечание 2. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @recviz, но не код, вызывающий его.﻿

import inspect
from functools import wraps

def recviz(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        a = list(map(repr, args))
        b = [f'{k}={v!r}' for k, v in kwargs.items()]
        params = ', '.join(a + b)
        c = '    ' * (len(inspect.getouterframes(inspect.currentframe())) // 2 - 1)
        print(c + f'-> {x.__name__}({params})')
        res = x(*args, **kwargs)
        print(c + f'<- {repr(res)}')
        return res
    return wrapper

@recviz
def add(a, b):
    return a + b

add(1, b=2)

@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)
