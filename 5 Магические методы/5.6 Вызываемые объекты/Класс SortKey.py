# Нередко во время сортировки объектов мы используем дополнительную функцию, которая описывает правило сортировки. Например, если нам нужно отсортировать список экземпляров некоторого класса на основе значений определенного атрибута, мы можем реализовать функцию, которая принимает в качестве аргумента этот экземпляр и возвращает значение необходимого атрибута.


class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        return [getattr(obj, i) for i in self.args]


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(max(users, key=SortKey('name')))
print(max(users, key=SortKey('age')))
print(max(users, key=SortKey('name', 'age')))
print(max(users, key=SortKey('age', 'name')))

