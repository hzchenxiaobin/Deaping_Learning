import numpy as np

A = np.array([1, 2, 3, 4])
print(A)

# 数组的维度
print(np.ndim(A))

# 数组的形状
print(A.shape)

# 二维数组
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)

print(np.ndim(B))

print(B.shape)

# 矩阵乘
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])
print(np.dot(A, B))

