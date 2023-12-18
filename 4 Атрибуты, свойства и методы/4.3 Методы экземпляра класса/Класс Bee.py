# Реализуйте класс Bee, описывающий пчелку, которая перемещается по координатной плоскости в четырех направлениях: вверх, вниз, влево и вправо. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n

bee = Bee()

print(bee.x, bee.y)

bee = Bee()

bee.move_up(1)
bee.move_right(1)
bee.move_down(1)
bee.move_left(1)

print(bee.x, bee.y)

bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)