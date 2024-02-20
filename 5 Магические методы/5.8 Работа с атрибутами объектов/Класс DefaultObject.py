# Реализуйте класс DefaultObject. При создании экземпляра класс должен принимать один именованный аргумент default, имеющий значение по умолчанию None, а после произвольное количество именованных аргументов.

class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)

    def __getattr__(self, item):
        return self.default

god = DefaultObject(name='Ares', mythology='greek')

print(god.name)
print(god.mythology)
print(god.age)
