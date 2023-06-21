# 激活函数
import numpy as np


# 1.阶跃函数
def step_function(x):
    y = x > 0
    return y.astype(int)


def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
