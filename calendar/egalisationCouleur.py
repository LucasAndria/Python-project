import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import scipy.misc


img = cv2.imread('lucat.jpg')
b, g, r = cv2.split(img)



k = np.zeros_like(b)
b = cv2.merge([b, k, k])
g = cv2.merge([k, g, k])
r = cv2.merge([k, k, r])

hist, bins= np.histogram(b.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0,256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf','histogram'), loc='upper left')

equ = cv2.equalizeHist(img)




cv2.waitKey(0)
cv2.destroyAllWindows()

#blue=cv2.equalizeHist(b)
#green=cv2.equalizeHist(g)
#red=cv2.equalizeHist(r)


# convert image from RGB to HSV
# img_hsv = cv2.cvtColor(b, cv2.COLOR_RGB2HSV)
#
# img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
#
# blue = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
#
# # convert image from RGB to HSV
# img_hsv = cv2.cvtColor(r, cv2.COLOR_RGB2HSV)
#
# img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
#
# red = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
#
# # convert image from RGB to HSV
# img_hsv = cv2.cvtColor(g, cv2.COLOR_RGB2HSV)
#
# img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
#
# green = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)


blue, g, r=cv2.split(b)
b, green, r=cv2.split(g)
b, g, red=cv2.split(r)

imgLast=cv2.merge([blue, green, red])

cv2.imshow("equalized", imgLast)

cv2.waitKey(0)


cv2.destroyAllWindows()
