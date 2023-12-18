# Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробельными символами.
#
# Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Экземпляр класса TextHandler должен иметь три метода:
#
# add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
# get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
# get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
# Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться в том порядке, в котором они были добавлены в набор.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


class TextHandler:
    l = []
    def add_words(self, s):
        self.s = s
        for i in s.split():
            self.l.append(i)

    def get_shortest_words(self):
        a = []
        if len(self.l) > 0:
            shortest = min(self.l, key=len)
        for word in self.l:
            if len(word) <= len(shortest):
                shortest = word
                a.append(shortest)
        return a


    def get_longest_words(self):
        b = []
        if len(self.l) > 0:
            longest = max(self.l, key=len)
        for word in self.l:
            if len(word) >= len(longest):
                longest = word
                b.append(longest)
        return b

texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())