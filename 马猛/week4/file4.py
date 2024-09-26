import cv2
import random

# 1.1 高斯噪声
img = cv2.imread('lenna.png', 0)
percent = 0.6
noise_sum = int(img.shape[0] * img.shape[1] * percent)
for i in range(noise_sum):
    random_x = random.randint(0, img.shape[0] - 1)
    random_y = random.randint(0, img.shape[1] - 1)
    dot = img[random_x, random_y]
    dot = dot + random.gauss(2, 3)  # means=2, sigma=3
    if dot < 0:
        dot = 0
    elif dot > 255:
        dot = 255
    img[random_x, random_y] = dot

cv2.imshow('gaosimg', img)
cv2.waitKey(0)
