# Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
#
# Экземпляр класса AttrsNumberObject должен иметь один атрибут:
#
# attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        if item == 'attrs_num':
            self.__dict__['attrs_num'] = len(self.__dict__)
        return object.__getattribute__(self, item)

music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
music_group.genre = 'jazz'
print(music_group.attrs_num)

music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
music_group.genre = 'jazz'
print(music_group.attrs_num)