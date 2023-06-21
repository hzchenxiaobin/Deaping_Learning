import numpy as np

# 一维数组
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# 多维数组
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)
B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)
print(A * 10)

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print(A * B)

# 访问元素
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])
print(X[0][1])

for row in X:
    print(row)

# 将X转换为一维数组
X = X.flatten()
print(X)
print(X[np.array([0, 2, 4])])

print(X > 15)
print(X[X>15])