# Реализуйте класс Calculator, экземпляры которого позволяют выполнять различные арифметические операции с двумя числами. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Экземпляр класса Calculator должен являться вызываемым объектом и принимать три аргумента:
#
# a — число
# b — число
# operation — один из символов +, -, * и /

class Calculator:

    def __call__(self, a, b, operation):
        if operation == '*':
            return a * b
        elif operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '/' and b != 0:
            return a / b
        else:
            raise ValueError('Деление на ноль невозможно')

calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))

calculator = Calculator()

try:
    print(calculator(10, 0, '/'))
except ValueError as e:
    print(e)
