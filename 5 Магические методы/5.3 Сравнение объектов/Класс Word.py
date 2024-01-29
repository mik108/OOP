# Будем называть словом любую последовательность из одной или более латинских букв.
#
# Реализуйте класс Word, описывающий слово. При создании экземпляра класс должен принимать один аргумент:
#
# word — слово
# Экземпляр класса Word должен иметь следующее формальное строковое представление:
#
# Word('<слово в исходном виде>')
# И следующее неформальное строковое представление:
#
# <слово, в котором первая буква заглавная, а все остальные строчные>
# Также экземпляры класса Word должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два слова считаются равными, если их длины совпадают. Слово считается больше другого слова, если его длина больше.
#
# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Никаких ограничений касательно реализации класса Word нет, она может быть произвольной.

from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.word}')"

    def __str__(self):
        return f'{self.word[0].upper()}{self.word[1:]}'

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented



print(Word('bee') == Word('hey'))
print(Word('bee') < Word('geek'))
print(Word('bee') > Word('geek'))
print(Word('bee') <= Word('geek'))
print(Word('bee') >= Word('gee'))

words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))