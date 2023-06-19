import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

import numpy as np
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
v = mean_squared_error(np.array(y), np.array(t))
print(v)

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
v = mean_squared_error(np.array(y), np.array(t))
print(v)
