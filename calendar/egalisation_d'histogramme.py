import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import scipy.misc


img = cv2.imread('image/lucas.jpg')
b, g, r = cv2.split(img)

k = np.zeros_like(b)
b = cv2.merge([b, k, k])
g = cv2.merge([k, g, k])
r = cv2.merge([k, k, r])

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(b)

# Randomly generate 500 salt and pepper
rows, cols, dims = img.shape
for i in range(500):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y:] = 255

plt.figure("manda")
plt.imshow(img)

plt.axis('off')
plt.show()