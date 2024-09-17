import cv2
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(221)
plt.imshow(plt.imread("lenna.png"))

img = cv2.imread("lenna.png")
height, width, k = img.shape[:3]
img_gray = np.zeros([height, width], img.dtype)

for i in range(height):
    for j in range(width):
        rgb = img[i, j]
        img_gray[i, j] = int(rgb[0] * 0.11 + rgb[1] * 0.59 + rgb[2] * 0.3)

# cv2.imshow('ss',img_gray)
# cv2.waitKey(0)

plt.subplot(222)
plt.imshow(img_gray, cmap='gray')

# cv2.imshow('ss',img_gray)
# cv2.waitKey(0)
print(img_gray)

img_gray = rgb2gray(plt.imread("lenna.png"))

print(img_gray)

hang, shu = img_gray.shape
for i in range(hang):
    for j in range(shu):
        if img_gray[i, j] > 0.5:
            img_gray[i, j] = 1
        else:
            img_gray[i, j] = 0
# img_gray = np.where(img_gray > 0.5, 1, 0)
print(img_gray)

plt.subplot(223)
plt.imshow(img_gray, cmap='gray')
plt.show()
