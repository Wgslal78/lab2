import numpy as np
import timeit
def matrix():
    arr=np.array([[-1,42,63],[-4,5,6],[7,8,9]])
    result = np.linalg.inv(arr)
    print(result)
time_result=timeit.timeit(matrix,number=1)
print(time_result)
matrix=[[-1,42,63],[-4,5,6],[7,8,9]]
print(matrix)

#без numpy
def det(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += matrix[0][c] * dop(matrix, 0, c)
    return det

def dop(matrix, row, col):
    submatrix = [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]
    return (-1) ** (row + col) * det(submatrix)
print(det(matrix))