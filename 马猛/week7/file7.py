# 层次聚类

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from matplotlib import pyplot as plt

X = [[1, 2], [3, 2], [4, 4], [1, 2], [1, 3]]
L = linkage(X, 'ward')
fcluster(L, 4, 'distance')
plt.figure(figsize=(5, 4))
dendrogram(L)
print(L)
plt.show()
