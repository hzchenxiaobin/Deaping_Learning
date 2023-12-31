import numpy as np


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # 生成和x形状相同的数组

    for idx in range(x.size):
        tmp_val = x[idx]
        # 计算 f(x+h)
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # 计算 f(x+h)
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return grad


# def function_2(x):
#     return np.sum(x**2)


# print(numercial_gradient(function_2, np.array([3.4, 4.0])))
# print(numercial_gradient(function_2, np.array([0.0, 2.0])))
# print(numercial_gradient(function_2, np.array([3.0, 0.0])))
