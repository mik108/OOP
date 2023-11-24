# Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка стоит перед символом дефиса.
#
# Реализуйте функцию is_decimal(), которая принимает один аргумент:
#
# string — строка, содержащая произвольный набор символов
# Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_decimal(), но не код, вызывающий ее.

def is_decimal(string):
    try:
        string is not float(string)
        return True
    except ValueError:
        return False

print(is_decimal('100'))
print(is_decimal('199.1'))
print(is_decimal('-0.2'))
print(is_decimal('-.95'))
print(is_decimal('.10'))
print(is_decimal('.-95'))
