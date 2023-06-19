import sys, os
import numpy as np

root_path = os.path.abspath(__file__)
root_path = "/".join(root_path.split("\\")[:-2])
sys.path.append(root_path)
from dataset.mnist import load_mnist
from ch03.activation_function import sigmoid
from ch03.soft_max import softmax

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print(batch_mask)



