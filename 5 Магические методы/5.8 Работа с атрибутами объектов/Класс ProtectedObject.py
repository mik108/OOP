# Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_). Например, _password, __email и __dict__.
#
# Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов.
# Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.
#
# Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров, а также удалять эти атрибуты.
# При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут, должно возбуждаться исключение AttributeError с текстом:
#
# Доступ к защищенному атрибуту невозможен
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.

class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item[0]  == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item[0] == '_':
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, item)

user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)