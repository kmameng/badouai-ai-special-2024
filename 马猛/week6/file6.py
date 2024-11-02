# 1.实现透视变化

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# import cv2
# import numpy as np
#
# img = cv2.imread('photo1.jpg')
# imgCopy = img.copy()
# src = np.float32([[207, 151], [517, 285], [17, 601], [343, 731]])
# dst = np.float32([[0, 0], [337, 0], [0, 488], [300, 500]])
# trans = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(imgCopy, trans, (300, 500))
# cv2.imshow("src", img)
# cv2.imshow("result", result)
# cv2.waitKey(0)

# 2.实现kmeans

X = [[0.0888, 0.5885],
     [0.1399, 0.8291],
     [0.0747, 0.4974],
     [0.0983, 0.5772],
     [0.1276, 0.5703],
     [0.1671, 0.5835],
     [0.1306, 0.5276],
     [0.1061, 0.5523],
     [0.2446, 0.4007],
     [0.1670, 0.4770],
     [0.2485, 0.4313],
     [0.1227, 0.4909],
     [0.1240, 0.5668],
     [0.1461, 0.5113],
     [0.2315, 0.3788],
     [0.0494, 0.5590],
     [0.1107, 0.4799],
     [0.1121, 0.5735],
     [0.1007, 0.6318],
     [0.2567, 0.4326],
     [0.1956, 0.4280]]

km = KMeans(n_clusters=3)
y_predict = km.fit_predict(X)
print(km)
print("y_predict:", y_predict)
x2 = [n[0] for n in X]
print(x2)
y2 = [n[1] for n in X]
print(y2)
plt.scatter(x2, y2, c=y_predict, marker='x')
plt.title("km")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["A", "B", "C"])
plt.show()
