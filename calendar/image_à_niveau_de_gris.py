import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])

img = mpimg.imread('Image/yoda(low).png')

gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.axis('off')
plt.savefig('Image/niveau-de-gris.jpg', dpi = 167, bbox_inches='tight', pad_inches=0)
plt.show()

##import numpy as np
##import cv2 as cv
##from matplotlib import pyplot as plt
##
##img = cv.imread('couleur.jpg', cv.IMREAD_GRAYSCALE)
##
##plt.hist(img.ravel(), 256, [0, 256]); plt.show()
##

