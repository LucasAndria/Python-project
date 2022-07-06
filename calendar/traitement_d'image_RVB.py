from PIL import Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = Image.open('image/yoda.jpeg')
data = img.getdata()

r = [(d[0], 0, 0) for d in data]
g = [(0, d[1], 0) for d in data]
b = [(0, 0, d[2]) for d in data]

img.putdata(r)
img.save('image/r.png')

img.putdata(g)
img.save('image/g.png')
img.putdata(b)
img.save('image/b.png')