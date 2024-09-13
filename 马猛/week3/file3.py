# 1.1 临近插值
import cv2
import numpy as np
from matplotlib import pyplot as plt

imgResultSize = 666

img = cv2.imread("lenna.png")
height, width, channels = img.shape
print('height=', height)
print('width=', width)
zerosImg = np.zeros((imgResultSize, imgResultSize, channels), np.uint8)
heightRatio = imgResultSize / height
widthRatio = imgResultSize / width

for i in range(imgResultSize):
    for j in range(imgResultSize):
        x = int(i / heightRatio + 0.5)
        y = int(j / widthRatio + 0.5)
        zerosImg[i, j] = img[x, y]

cv2.imshow('ytu', img)
cv2.imshow('jgtu', zerosImg)
cv2.waitKey(0)

# 1.2 双线性插值
img = cv2.imread("lenna.png")
height, width, channels = img.shape
imgResultHeight = 888
imgResultWidth = 888
zerosImg = np.zeros((imgResultHeight, imgResultWidth, channels), np.uint8)
scale_x, scale_y = float(width) / imgResultWidth, float(height) / imgResultHeight

for i in range(channels):
    for x in range(imgResultWidth):
        for y in range(imgResultHeight):
            src_x = (x + 0.5) * scale_x - 0.5
            src_y = (y + 0.5) * scale_y - 0.5

            src_x0 = int(np.floor(src_x))
            src_y0 = int(np.floor(src_y))
            src_x1 = min(src_x0 + 1, width - 1)
            src_y1 = min(src_y0 + 1, height - 1)

            temp = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[src_y0, src_x1, i]
            temp2 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
            zerosImg[y, x, i] = int((src_y1 - src_y) * temp + (src_y - src_y0) * temp2)

cv2.imshow('ytu', img)
cv2.imshow('jgtu', zerosImg)
cv2.waitKey(0)

# 2.证明中心重合+0.5
# (m-1)/2+z=((n-1)/2+z)*m/n
#
# 1/2m-1/2+z=1/2m(n-1)/n+mz/n
# z-mz/n=1/2m(n-1)/n-1/2m+1/2
# z(1-m/n)={1/2m(n-1)-1/2mn+1/2n}/n
# z(1-m/n)=(1/2n-1/2m)/n
# z(n-m)/n=1/2(n-m)/n
# z=1/2


# 3.直方图均衡化

img = cv2.imread("lenna.png", 1)
print('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.equalizeHist(gray)
hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()

cv2.imshow("zft", np.hstack([gray, dst]))
cv2.waitKey(0)
