# Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:
#
# data — словарь произвольной вложенности
# path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
# default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
# Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2,
# то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1].
# Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

def pluck(data, path, default=None):
    path = path.split('.')
    value = None
    if path:
        value = data.get(path.pop(0))
    for i in path:
        value = value.get(i)
    if value is None:
        return default
    else:
        return value

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'x'))

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))
