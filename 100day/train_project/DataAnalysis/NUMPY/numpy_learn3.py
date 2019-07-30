#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: numpy_learn3.py
# @time: 2019/6/9 7:32
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1 求和np.sum：
nd1 = np.random.randint(0, 100, size=(5, 4))
print(nd1)
print(np.sum(nd1))

# 2 最大最小值np.max/np.min
# 3 求平均值  np.mean()
# 4 类乘 np.prod()
print(np.prod(nd1[2]))
# 5 标准差 np.std()
# 6 方差 np.var()
# 7 求最大值的索引 np.argmax()
# 8 求最小值的索引 np.argmin()
# 9 求满足条件的值的索引 np.argwhere()
print(np.argmax(nd1))
print(np.argmin(nd1))
index = np.argwhere((nd1 > 50) & (nd1 < 70))  # 输出值大于50的索引
print(index)
for x, y in index:
    print(nd1[x, y])

# 9 平坦化 np.ravel() 把多维数组平坦化成一维数组
nd2 = np.ravel(nd1)
print(nd2)

# 10 中位数 median()
# print(nd2.median()) #  'numpy.ndarray' object has no attribute 'median'    median不是一个对象方法，模块方法
print(np.median(nd2))

# 11 按百分比排列 np.percentile()

# 12 数组中有任意一个元素为true或非0，则返回True     np.any()
# Test whether any array element along a given axis evaluates to True.
#
# Returns single boolean unless `axis` is not ``None``

# 13 数组中有所有元素为true或非0，则返回True     np.all()
