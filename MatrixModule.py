import copy
from ComplexModule import Complex

class Matrix:
    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.columns = len(array[0])
        for i in range(self.rows):
            for j in range(self.columns):
                if not isinstance(self.array[i][j], Complex):
                    self.array[i][j] = Complex(self.array[i][j], 0)

    def __add__(self, other):
        if self.columns != other.columns or self.rows != other.rows:
            print('Addition not allowed for matrices of these sizes')
            return None

        new_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                new_row.append(self.array[i][j] + other.array[i][j])
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __sub__(self, other):
        return self + (other * -1)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            new_matrix = []
            for i in range(self.rows):
                new_row = []
                for j in range(self.columns):
                    new_row.append(self.array[i][j] * other)
                new_matrix.append(new_row)
            return Matrix(new_matrix)

        if self.columns != other.rows:
            print('Multiplication not allowed for matrices of these sizes')
            print(self.rows, self.columns, other.rows, other.columns)
            return None

        new_matrix = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.columns):
                entry_sum = Complex(0, 0)
                for k in range(other.rows):
                    entry_sum += self.array[i][k] * other.array[k][j]
                new_row.append(entry_sum)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __truediv__(self, other):
        if not isinstance(other, Matrix):
            return self * (1 / other)

    def __pow__(self, power):
        if not self.rows == self.columns:
            print('Exponentiation not allowed for matrices of these sizes')
        temp_matrix = Matrix(self.array)
        if power == 0:
            temp_matrix = temp_matrix * 0
            for i in range(temp_matrix.rows):
                temp_matrix.array[i][i] = 1
            return temp_matrix
        for i in range(power - 1):
            self = self * temp_matrix
        return self

    def identity(self):
        identity = Matrix(self.array) * Complex(0, 0)
        for i in range(identity.rows):
            identity.array[i][i] = Complex(1, 0)
        return identity

    def det(self):
        if not self.rows == self.columns:
            print('Determinant not allowed for non-square matrices')
            return None
        if self.rows == 2:
            return self.array[0][0] * self.array[1][1] - self.array[0][1] * self.array[1][0]
        total = 0
        for i in range(self.columns):
            new_array = []
            for j in range(1, self.rows):
                new_array.append(self.array[j][:i] + self.array[j][i+1:])
            new_matrix = Matrix(new_array)
            total += (-1)**i * new_matrix.det()
        return total

    def rref(self):
        new_array = copy.deepcopy(self.array)
        new_matrix = (Matrix(new_array))
        for i in range(self.rows):
            if new_matrix.array[i][i] != 0:
                scalar = new_matrix.array[i][i]
                for j in range(self.columns):
                    new_matrix.array[i][j] /= scalar
            for j in range(i + 1, self.rows):
                scalar = new_matrix.array[j][i]
                for k in range(self.columns):
                    new_matrix.array[j][k] -= scalar * new_matrix.array[i][k]

        for i in range(self.rows - 1):
            for j in range(i + 1, self.rows):
                scalar = new_matrix.array[self.rows - j - 1][self.rows - i - 1]
                for k in range(0, self.columns):
                    new_matrix.array[self.rows - j - 1][k] -= scalar * new_matrix.array[self.rows - i - 1][k]

        return new_matrix

    def inverse(self):
        if self.det() == 0 or self.det() is None:
            print('Inverse cannot be found for matrix with det = 0 or None')
            return None
        new_array = copy.deepcopy(self.array)
        for i in range(self.rows):
            for j in range(self.rows):
                if i == j:
                    new_array[i].append(1)
                else:
                    new_array[i].append(0)
        new_matrix = Matrix(new_array).rref()
        for i in range(self.rows):
            new_matrix.array[i] = new_matrix.array[i][self.rows:]
        new_matrix.columns = len(new_matrix.array[0])
        return new_matrix

    def __repr__(self):
        for i in self.array:
            for j in i:
                if j.b == 0:
                    print(format(j.a, '^5.4f'), end = ' ')
                else:
                    if j.a == 0:
                        print(str(format(j.b, '3.2f')) + 'i', end = ' ')
                    else:
                        print(str(format(j.a, '3.2f')) + ' + ' + str(format(j.b, '3.2f')) + 'i', end = ' ')
            print()
        return ''