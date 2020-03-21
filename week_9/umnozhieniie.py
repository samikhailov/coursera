from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
        if (len(self.matrix) != len(other.matrix) or
                len(self.matrix[0]) != len(other.matrix[0])):
            raise MatrixError(self, other)
        result = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[0])):
                tmp.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(tmp)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                tmp = []
                for j in range(len(self.matrix[0])):
                    tmp.append(self.matrix[i][j] * other)
                result.append(tmp)
        elif isinstance(other, Matrix):
            # ru.wikipedia.org/wiki/Умножение_матриц - Определение
            if len(self.matrix[0]) != len(other.matrix):
                raise MatrixError(self, other)
            m = len(self.matrix[0])
            l = len(self.matrix)
            n = len(other.matrix[0])
            result = [[None for j in range(n)] for i in range(l)]
            for i in range(l):
                for j in range(n):
                    sum = 0
                    for r in range(m):
                        sum += self.matrix[i][r] * other.matrix[r][j]
                    result[i][j] = sum
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        result = [[None for j in self.matrix] for i in self.matrix[0]]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[j][i] = self.matrix[i][j]
        self.matrix = result
        return Matrix(self.matrix)

    @staticmethod
    def transposed(instance):
        result = [[None for j in instance.matrix] for i in instance.matrix[0]]
        for i in range(len(instance.matrix)):
            for j in range(len(instance.matrix[0])):
                result[j][i] = instance.matrix[i][j]
        return Matrix(result)


exec(stdin.read())
