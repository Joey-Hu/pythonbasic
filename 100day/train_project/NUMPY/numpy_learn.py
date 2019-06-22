#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: numpy_learn.py
# @time: 2019/6/7 10:07
# @Ducument：https://www.python.org/doc/
# @desc:

import requests as rq  # 网络请求包
import numpy as np  #

'''
# 产生10个随机数

list = np.random.randint(0, 101, 10)
for value in list:
    print(value, end=" ")
'''


def sum2(x):  # x是一个列表
    total = 0
    for i in x:
        total += i
    return total


x = np.arange(1, 101, 1)    # np.arange([start,] stop[, step,], dtype=None)
print(x)
print(sum2(x))
