# Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.
#
# Реализуйте функцию is_integer(), которая принимает один аргумент:
#
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_integer(), но не код, вызывающий ее.

def is_integer(x):
    if x[0] == '-':
        x = x[1:]
    return x.isdigit()


print(is_integer('199'))
print(is_integer('-43'))
print(is_integer('5f'))
print(is_integer('5.0'))
print(is_integer('1.1'))
