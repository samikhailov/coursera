from sys import stdin
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

    def __add__(self, other):
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


exec(stdin.read())
