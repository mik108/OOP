# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Gun должен иметь один метод экземпляра:
#
# shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее

class Gun:
    total = 0
    def shoot(self):
        if self.total == 0:
            self.total += 1
            print('pif')
        elif self.total == 1:
            self.total -= 1
            print('paf')


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
