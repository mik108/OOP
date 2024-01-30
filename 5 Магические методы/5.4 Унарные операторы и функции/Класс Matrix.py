# Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# rows — количество строк в матрице
# cols — количество столбцов в матрице
# value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
# Экземпляр класса Matrix должен иметь два атрибута:
#
# rows — количество строк в матрице
# cols — количество столбцов в матрице

class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value for i in range(cols)] for j in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value


    def __repr__(self):
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'

    def __str__(self):
        m = []
        for row_ in self.matrix:
            m.append(" ".join(map(str, row_)))
        return '\n'.join(m)

    def __pos__(self):
        new_mx = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_mx.set_value(i, j, self.get_value(i, j))
        return new_mx

    def __neg__(self):
        new_mx = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_mx.set_value(i, j, -self.get_value(i, j))
        return new_mx

    def __invert__(self):
        new_mx = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                new_mx.set_value(j, i, self.get_value(i, j))
        return new_mx

    def __round__(self, n=None):
        new_mx = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_mx.set_value(i, j, self.get_value(i, j), n)
        return new_mx

print(Matrix(2, 3))

matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)

matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)

