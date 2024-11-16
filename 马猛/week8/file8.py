import cv2

size = 8
img = cv2.imread('lenna.png')

# 均值哈希
img = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sum = 0
hash_avg = ''
for i in range(size):
    for j in range(size):
        sum = sum + gray_img[i, j]
jun = sum / size / size
for i in range(size):
    for j in range(size):
        if gray_img[i, j] > jun:
            hash_avg = hash_avg + '1'
        else:
            hash_avg = hash_avg + '0'
print(hash_avg)

#差值哈希
img = cv2.resize(img, (size+1, size), interpolation=cv2.INTER_CUBIC)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hash_diff = ''
for i in range(size):
    for j in range(size):
        if gray_img[i, j] > gray_img[i, j + 1]:
            hash_diff = hash_diff + '1'
        else:
            hash_diff = hash_diff + '0'
print(hash_diff)
