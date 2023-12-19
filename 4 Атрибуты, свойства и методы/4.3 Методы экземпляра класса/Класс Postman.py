# Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Экземпляр класса Postman должен иметь один атрибут:
#
# delivery_data — изначально пустой список адресов, по которым следует доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:
#
# add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:
# (<улица>, <дом>, <квартира>)
# get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
# get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
# Примечание 1. Дома и квартиры в списках, возвращаемых методами get_houses_for_street() и get_flats_for_house(), должны располагаться в том порядке, в котором они были добавлены.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class Postman:
    def __init__(self):
        self.delivery_data = list()

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        l = []
        for i in self.delivery_data:
            if i[0] == street:
                if i[1] not in l:
                    l.append(i[1])
        return l

    def get_flats_for_house(self, street, house):
        l1 = []
        for i in self.delivery_data:
            if i[0] == street and i[1] == house:
                if i[2] not in l1:
                    l1.append(i[2])
        return l1

postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
