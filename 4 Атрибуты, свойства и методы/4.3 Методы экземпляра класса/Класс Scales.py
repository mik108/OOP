# Реализуйте класс Scales, описывающий весы с двумя чашами. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Scales должен иметь три метода экземпляра:
#
# add_right() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на правую чашу весов этот груз
# add_left() — метод, принимающий в качестве аргумента массу груза в килограммах и добавляющий на левую чашу весов этот груз
# get_result() — метод, возвращающий строку Весы в равновесии, если массы грузов на чашах совпадают, Правая чаша тяжелее — если правая чаша тяжелее, Левая чаша тяжелее — если левая чаша тяжелее
# Примечание 1. Пустые весы всегда находятся в равновесии.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class Scales:
    total_right = 0
    total_left = 0
    def add_right(self, n):
        self.n = n
        self.total_right += n

    def add_left(self, m):
        self.m = m
        self.total_left += m

    def get_result(self):
        if self.total_right == self.total_left:
            return f"Весы в равновесии"
        elif self.total_right > self.total_left:
            return f'Правая чаша тяжелее'
        elif self.total_right < self.total_left:
            return f'Левая чаша тяжелее'

scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

scales = Scales()

scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())