# Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Gun должен иметь три метода экземпляра:
#
# shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
# shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
# shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля

class Gun:
    total = 0
    count = 0
    def shoot(self):
        if self.total == 0:
            self.total += 1
            print('pif')
        elif self.total == 1:
            self.total -= 1
            print('paf')
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0
        self.total = 0
        return self.count

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())


gun = Gun()

gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
gun.shoot()