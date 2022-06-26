# Dot product of a matrix or 2d array/list

# matrix addition by first principles
import numpy

dim = 3

r1 = [1, 2, 3]
r2 = [4, 5, 6]
r3 = [7, 8, 9]

s1 = [1, 2, 1]
s2 = [6, 2, 3]
s3 = [4, 2, 1]

A = []

A.append(r1)
A.append(r2)
A.append(r3)

B = []

B.append(s1)
B.append(s2)
B.append(s3)

# C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# #  C[i][j] is the dot product of ith row of A
# #  and  the jth column of B

# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             C[i][j] = C[i][j] + A[i][k] * B[k][j]

# print(C)
X = numpy.mat(A)
Y = numpy.mat(B)
