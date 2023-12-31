# 数值微分
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)

def function_1(x):
    return 0.01 * x ** 2 + 0.1 * x

# import numpy as np
# import matplotlib.pylab as plt

# x = np.arange(0.0, 20.0, 0.1)
# y = function_1(x)
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.plot(x, y)
# plt.show()

# print(numerical_diff(function_1, 5))
# print(numerical_diff(function_1, 10))


# import numpy as np
# import matplotlib.pylab as plt

# x = np.arange(-1000, 1000, 0.001).reshape(2, -1)
# print(x)
# y = function_1(x)
# plt.plot(x, y)
# plt.show()



