import matplotlib.pyplot as plt
from matplotlib.image import imread
import os

img_path=os.path.join(os.getcwd(), "Deep Learning from Scratch\dataset\lena.png")
img = imread(img_path)
plt.imshow(img)
plt.show()