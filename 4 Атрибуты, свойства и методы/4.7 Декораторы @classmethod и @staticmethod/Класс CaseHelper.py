# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
#
# Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
#
# Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс CaseHelper должен иметь четыре статических метода:
#
# is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
# is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
# to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
# to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class CaseHelper:
    @staticmethod
    def is_snake(text):
        return True if text == text.lower() and " " not in text and "__" not in text else False

    @staticmethod
    def is_upper_camel(text):
        return True if text[0] == text[0].upper() and " " not in text and "_" not in text else False

    @staticmethod
    def to_snake(text):
        l = ""
        for i in text:
            if i == i.upper():
                l += " "
                l += i.lower()
            else:
                l += i.lower()
        return "_".join(l.split())

    @staticmethod
    def to_upper_camel(text):
        return "".join(map(str.capitalize, text.split("_")))

print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))