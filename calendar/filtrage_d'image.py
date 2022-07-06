import random
import math
import numpy
from matplotlib.pyplot import *

from PIL import Image
img = Image.open("Image/niveau-de-gris.jpg")
(red, green, blue) = img.split()
array = numpy.array(red)
figure(figsize=(4, 4))

array = numpy.array(red)
s = array.shape
sigma = 10
for j in range(s[0]):
    for i in range(s[1]):
        v = int(math.floor(array[j][i]+random.gauss(0, sigma)))
        if v > 255:
            v = 255
        if v < 0:
            v = 0
        array[j][i] = v
figure(figsize=(4, 4))
Image.fromarray(array).save("Image/bruit-gaussin-img.jpg")

array = numpy.array(red)
s = array.shape
N = 5000

for k in range(N):
    i = random.randint(0, s[1]-1)
    j = random.randint(0, s[0]-1)
    array[j][i] = int(array[j][i]/2)
figure(figsize=(4, 4))
imshow(array, cmap=cm.gray)
Image.fromarray(array).save("Image/bruit-impulsif-img.jpg")
