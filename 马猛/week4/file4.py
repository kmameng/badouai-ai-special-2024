import cv2
import random
import cv2 as cv
from skimage import util
import numpy as np


# # 1.1 高斯噪声
# img = cv2.imread('lenna.png', 0)
# percent = 0.6
# noise_sum = int(img.shape[0] * img.shape[1] * percent)
# for i in range(noise_sum):
#     random_x = random.randint(0, img.shape[0] - 1)
#     random_y = random.randint(0, img.shape[1] - 1)
#     dot = img[random_x, random_y]
#     dot = dot + random.gauss(2, 3)  # means=2, sigma=3
#     if dot < 0:
#         dot = 0
#     elif dot > 255:
#         dot = 255
#     img[random_x, random_y] = dot
#
# cv2.imshow('gaosimg', img)
# cv2.waitKey(0)

# # 1.2 椒盐噪声
# img = cv2.imread('lenna.png', 0)
# noise = int(img.shape[0] * img.shape[1] * 0.8)
# for i in range(noise):
#     randX = random.randint(0, img.shape[0] - 1)
#     randY = random.randint(0, img.shape[1] - 1)
#     if random.random() < 0.5:
#         img[randX, randY] = 0
#     else:
#         img[randX, randY] = 255
# cv2.imshow('jiaoYan', img)
# cv2.waitKey(0)

# # 2.噪声接口调用
# img = cv.imread("lenna.png")
# jkZs = util.random_noise(img, mode='s&p')  # gaussian：高斯噪声 s&p：椒盐噪声
# cv.imshow("jk", jkZs)
# cv.waitKey(0)

# 3.实现pca
X = np.array([[10, 15, 29],
              [15, 46, 13],
              [23, 21, 30],
              [11, 9, 35],
              [42, 45, 11],
              [9, 48, 5],
              [11, 21, 14],
              [8, 5, 15],
              [11, 12, 21],
              [21, 20, 25]])
K = np.shape(X)[1] - 1

# 中心化
mean = np.array([np.mean(a) for a in X.T])
centrX = X - mean
print(centrX)

# 矩阵X的协方差矩阵C
all = np.shape(centrX)[0]
C = np.dot(centrX.T, centrX) / (all - 1)
print(C)

# 求X的降维转换矩阵U
fa, fb = np.linalg.eig(C)
topK = np.argsort(-1 * fa)
zUt = [fb[:, topK[i]] for i in range(K)]
U = np.transpose(zUt)
print(U)

# 按照Z=XU求降维矩阵Z
Z = np.dot(X, U)
print(Z)
