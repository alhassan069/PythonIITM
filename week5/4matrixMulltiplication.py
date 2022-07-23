a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

b = [[1, 2, 1], [3, 1, 7], [6, 2, 3]]

# initialize c to zero
# I need to consider two matrices a and b
# i need to find dot procuct of two lists
# i need to pick ith row and jth column in a matrix


def initialize_mat(dim):
    c = []
    for i in range(dim):
        d = []
        for j in range(dim):
            d.append(0)
        c.append(d)
    return c


def dot_product(l1, l2):
    ans = 0
    dim = len(l1)
    for i in range(dim):
        ans = ans + (l1[i] * l2[i])
    return ans


def row(M, i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l


def column(M, i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[k][i])
    return l


def matrix_multiply(A, B):
    dim = len(A)
    C = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            # C[i][j] = ith row of A * jth row of B
            C[i][j] = dot_product(row(A, i), column(B, j))
    return C


x = [1, 2, 3]
y = [7, 1, 2]

# print(matrix_multiply(a, b))

import numpy

Aa = numpy.mat(a)
Bb = numpy.mat(b)

C = Aa * Bb

print(C)
