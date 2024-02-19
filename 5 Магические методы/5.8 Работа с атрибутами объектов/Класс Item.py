# Требовалось реализовать класс Item, описывающий предмет. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
#
# name — название предмета
# price — цена предмета в рублях
# quantity — количество предметов
# Предполагалось, что при обращении к атрибуту name экземпляра класса Item будет возвращаться его название с заглавной буквы, а при обращении к атрибуту total — произведение цены предмета на его количество.
#
# Программист торопился и решил задачу неправильно. Дополните приведенный ниже код и реализуйте правильный класс Item.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса Item нет, она может быть произвольной.

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, item):
        if item == 'name':
            return object.__getattribute__(self, item).title()
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item == 'total':
            return self.price * self.quantity

fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)

