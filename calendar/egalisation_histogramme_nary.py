import cv2

def hisEqulColor(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    cv2.merge(channels, ycrcb)
    cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
    return img


fr = 'image/r.png'
fv = 'image/g.png'
fb = 'image/b.png'

imgr = cv2.imread(fr)
imgv = cv2.imread(fv)
imgb = cv2.imread(fb)

img2r = hisEqulColor(imgr)
img2v = hisEqulColor(imgv)
img2b = hisEqulColor(imgb)

cv2.imwrite('image/r-eg.jpg', img2r)
cv2.imwrite('image/v-eg.jpg', img2v)
cv2.imwrite('image/b-eg.jpg', img2b)

cv2.waitKey(0)
cv2.destroyAllWindows()
