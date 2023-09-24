matrix = [[1, 2]]
transpose_matrix = [[matrix[0][0]], [matrix[0][1]]]
for i in transpose_matrix:
    print(i)

# Напишем код через библиотеку numpy


import numpy as np

# исходная матрица
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Транспонирование матрицы
transpose_matrix = np.transpose(matrix)
print("Исходная матрица:")
print(matrix)
print("\nТранспонированная матрица:")
print(transpose_matrix)

import numpy as np

# Определение первой матрицы
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])
# Определение второй матрицы
matrix2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])
# Умножение матриц
result_matrix = np.dot(matrix1, matrix2)
print("Первая матрица:")
print(matrix1)

print("Вторая матрица:")
print(matrix2)

print("Результат умножения:")
print(result_matrix)

# определение ранга матрицы
import numpy as np

# Определение матрицы
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Определение ранга матрицы
rank = np.linalg.matrix_rank(matrix)

# Вывод результата
print("Матрица:")
print(matrix)
print("Ранг матрицы:", rank)