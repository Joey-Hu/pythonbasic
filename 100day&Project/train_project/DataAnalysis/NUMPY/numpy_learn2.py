#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: numpy_learn2.py
# @time: 2019/6/7 11:15
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np
import pandas as pd
import requests as requests

print(np.__version__)  # numpy版本 1.16.1
print(pd.__version__)  # 0.24.2
print(requests.__version__)  # 2.21.0

# 将python的list类型转换成ndarray类型
# 一维
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(list1))  # <class 'list'>
nd = np.array(list1)
print(type(nd))  # <class 'numpy.ndarray'>

# 二维

list2 = [[1, 3, 5, 7], [2, 4, 6, 8]]
print(list2)  # [[1, 3, 5, 7], [2, 4, 6, 8]]
nd2 = np.array(list2)
print(nd2)
print(type(nd2))  # <class 'numpy.ndarray'>

# ndarray方法 sum，sort，min, max, ...
print(nd.sum())  # 45
