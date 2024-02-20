# Реализуйте класс NonNegativeObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
#
# Примечание 1. Числами будем считать экземпляры классов int и float.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Никаких ограничений касательно реализации класса NonNegativeObject нет, она может быть произвольной.

class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)):
                object.__setattr__(self, key, abs(value))
            else:
                object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return self.kwargs

point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)

point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)