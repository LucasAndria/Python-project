import cv2

imgr = cv2.imread('image/r-eg.jpg', 1)
imgv = cv2.imread('image/v-eg.jpg', 1)
imgb = cv2.imread('image/b-eg.jpg', 1)

b1 = cv2.split(imgr)
r2, v2, b2 = cv2.split(imgv)
r3, v3, b3 = cv2.split(imgb)

image = cv2.merge(b1)

cv2.imshow("lazdj", image)