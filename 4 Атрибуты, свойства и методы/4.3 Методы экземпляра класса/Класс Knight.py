#Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

# horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
# color — цвет коня (black или white)
# Экземпляр класса Knight должен иметь три атрибута:
#
# horizontal — координата коня на шахматной доске по горизонтальной оси
# vertical — координата коня на шахматной доске по вертикальной оси
# color — цвет коня
# Класс Knight должен иметь четыре метода экземпляра:
#
# get_char() — метод, возвращающий символ N
# can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
# move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
# draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *


class Knight:
    BORD_SIZE = 8

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, horiz, vertic):
        return abs(ord(horiz) - ord(self.horizontal)) * abs(vertic - self.vertical) == 2

    def move_to(self, horiz, vertic):
        if self.can_move(horiz, vertic):
            self.horizontal, self.vertical = horiz, vertic

    def v_to_board_coord(v):
        return v + 1

    def h_to_board_coord(h):
        return chr(ord('a') + h)

    def draw_board(self):
        for v in range(Knight.BORD_SIZE - 1, 0 - 1, -1):
            row_arr = ['.'] * Knight.BORD_SIZE
            for h in range(Knight.BORD_SIZE):
                horiz = Knight.h_to_board_coord(h)
                vertic = Knight.v_to_board_coord(v)
                if self.horizontal == horiz and self.vertical == vertic:
                    row_arr[h] = self.get_char()
                elif self.can_move(horiz, vertic):
                    row_arr[h] = '*'
            print(''.join(row_arr))


knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)

knight = Knight('c', 3, 'white')

knight.draw_board()