#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: homework.py
# @time: 2019/6/17 8:52
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np

# 根据第三列对一个5*5的矩阵进行排序

list = [[26,29,30,87,49],
 [34,37,31,8,38],
 [83,37,98,2,89],
 [89,81,57,11,16],
 [22,33,41,55,81]]
nd1 = np.array(list)
print(nd1)
index = nd1[:,2].argsort()      # 返回第三列排序索引
nd2 = nd1[index]
print(nd2)


# 给定一个4维矩阵，求得最后两维的和
nd3 = np.random.randint(0,10,size=(3,4,5,6))
print(nd3.sum(axis=-1).sum(axis=-1))
# nd3.sum(axis=(-1,-2))


# 给定数组[1,2,3,4,5],在这个数组的每个元素之间插入3个0得到新数组

nd4 = np.arange(1,6)

nd5 = np.zeros(17,dtype=np.int8)
nd5[::4]=nd4
print(nd5)      # 巧妙


# 正则化

nd6 = np.array(list[0:4])
print(nd6)
v_min = nd6.min(axis=0)
v_max = nd6.max(axis=0)
print((nd6-v_min)/(v_max-v_min))