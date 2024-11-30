import numpy as np

# 标准化
x = [-10, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
     11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 15, 15, 30]
l1 = []
cs = []
for i in x:
    c = x.count(i)
    cs.append(c)
[(float(i) - np.mean(x)) / (max(x) - min(x)) for i in x]
x_mean = np.mean(x)
s2 = sum([(i - np.mean(x)) * (i - np.mean(x)) for i in x]) / len(x)
x2 = [(i - x_mean) / s2 for i in x]
