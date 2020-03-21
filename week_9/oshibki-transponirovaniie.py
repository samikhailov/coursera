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
        result = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[0])):
                tmp.append(self.matrix[i][j] * other)
            result.append(tmp)
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
