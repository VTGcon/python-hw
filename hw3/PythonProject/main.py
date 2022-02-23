import numpy as np


class Matrix:

    def __init__(self, lst):
        self.n = len(lst)
        self.m = len(lst[0])
        new_numbers = []
        for i in range(self.n):
            new_numbers.append([])
            for j in range(self.m):
                new_numbers[i].append(lst[i][j])
        self.numbers = new_numbers

    def __add__(self, other):
        new_numbers = []
        if self.n != other.n:
            raise ValueError
        if self.m != other.m:
            raise ValueError
        for i in range(self.n):
            new_numbers.append([])
            for j in range(self.m):
                new_numbers[i].append(self.numbers[i][j] + other.numbers[i][j])
        return Matrix(new_numbers)

    def __mul__(self, other):
        new_numbers = []
        if self.n != other.n:
            raise ValueError
        if self.m != other.m:
            raise ValueError
        for i in range(self.n):
            new_numbers.append([])
            for j in range(self.m):
                new_numbers[i].append(self.numbers[i][j] * other.numbers[i][j])
        return Matrix(new_numbers)

    def __matmul__(self, other):
        new_numbers = []
        if self.m != other.n:
            raise ValueError
        for i in range(self.n):
            new_numbers.append([])
            for j in range(other.m):
                new_number = 0
                for k in range(self.m):
                    new_number += self.numbers[i][k] * other.numbers[k][j]
                new_numbers[i].append(new_number)
        return Matrix(new_numbers)

    def __str__(self):
        ans = "["
        for i in range(self.n - 1):
            ans += '['
            for j in range(self.m - 1):
                ans += str(self.numbers[i][j]) + ','
            ans += str(self.numbers[i][self.m - 1]) + '],\n'
        ans += '['
        for j in range(self.m - 1):
            ans += str(self.numbers[self.n - 1][j]) + ','
        ans += str(self.numbers[self.n - 1][self.m - 1]) + ']]'
        return ans


class Writer:
    def __str__(self):
        return '%s' % self._matrix


class GetSetClass:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = np.asarray(matrix)


class NPMatrix(np.lib.mixins.NDArrayOperatorsMixin, Writer, GetSetClass):
    def __init__(self, matrix):
        self._matrix = np.asarray(matrix)

    def __array_func__(self, func, method, *inputs, **kwargs):
        inputs = list(x.matrix if isinstance(x, NPMatrix) else x for x in inputs)
        result = getattr(func, method)(*inputs, **kwargs)
        return type(self)(result)

