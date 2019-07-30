# @author: huhao
# @file: mat.py
# @time: 2019/7/13 9:52
# @Document：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

# 线形图
# print(np.random.randint(1,10,size=10).tolist())
s = Series(data=[9, 9, 9, 9, 4, 5, 7, 4, 4, 5])

'''

'''
# fig = plt.figure(figsize=(12,7))
# plt.subplot(221)
# s.plot(kind = "line")
# plt.subplot(222)
# s.plot(kind = "bar")
# plt.subplot(223)
# s.plot(kind = "barh")
# plt.subplot(224)
# s.plot(kind = "hist",bins = 10, range=[0,10])   # 直方图
# plt.show()
#
# fig = plt.figure(figsize=(12,7))
# plt.subplot(221)
# s.plot(kind = "box")        # 看出数据的分布（最大值，最小值，中位数），绿线表示中位数
# plt.subplot(222)
# s.plot(kind = "density")
# plt.subplot(223)
# s.plot(kind = "area")
# plt.subplot(224)
# s.plot(kind = "pie")
#
# plt.show()

# df = np.random.randint(0,150,size=(10,2)).tolist()
# print(df)
df = DataFrame(data=[[75, 16], [90, 142], [63, 89], [3, 117], [96, 56], [126, 28], [52, 32], [122, 36], [62, 78], [29, 18]],columns=["Python","Math"], index=list("ABCDEFGHJK"))
print(df)
df["En"] = df["Python"].map(lambda x: x+np.random.randint(-10,10,size=1)[0])
print(df)

# fig = plt.figure(figsize=(12,7))
# plt.subplot(221)
df.plot(kind = "line")
plt.show()