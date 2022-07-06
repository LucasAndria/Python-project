import cv2
import sys
import numpy as np
import pywt
np.set_printoptions(threshold=12)
image = cv2.imread('lucas.jpg')
image = cv2.resize(image, (256, 256))
cv2.imshow('imageorg', image)
[b, g, r] = cv2.split(image)
x = b
coffes = pywt.dwt2(x, 'haar')
ca, (ch, cv, cd) = coffes
print(b)
print('-----------')
print(ch)

# ca2 = np.uint8(ca)
# ch2 = np.uint8(ch)
# cv2 = np.uint8(cv)
# cd2 = np.uint8(cd)
# coffes = ca2, (ch2, cv2, cd2)


origin = pywt.idwt2(coffes, 'haar')
origin = np.uint8(origin)
k = np.zeros_like(b)
blue = cv2.merge([origin, k, k])
cv2.imshow('image', blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
