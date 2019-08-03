#!/usr/bin/env python
# encoding: utf-8

# /**
#  *                             _ooOoo_
#  *                            o8888888o
#  *                            88" . "88
#  *                            (| -_- |)
#  *                            O\  =  /O
#  *                         ____/`---'\____
#  *                       .'  \\|     |//  `.
#  *                      /  \\|||  :  |||//  \
#  *                     /  _||||| -:- |||||-  \
#  *                     |   | \\\  -  /// |   |
#  *                     | \_|  ''\---/''  |   |
#  *                     \  .-\__  `-`  ___/-. /
#  *                   ___`. .'  /--.--\  `. . __
#  *                ."" '<  `.___\_<|>_/___.'  >'"".
#  *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#  *               \  \ `-.   \_ __\ /__ _/   .-` /  /
#  *          ======`-.____`-.___\_____/___.-`____.-'======
#  *                             `=---='
#  *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  *                     佛祖保佑        永无BUG
#  *            佛曰:
#  *                   写字楼里写字间，写字间里程序员；
#  *                   程序人员写程序，又拿程序换酒钱。
#  *                   酒醒只在网上坐，酒醉还来网下眠；
#  *                   酒醉酒醒日复日，网上网下年复年。
#  *                   但愿老死电脑间，不愿鞠躬老板前；
#  *                   奔驰宝马贵者趣，公交自行程序员。
#  *                   别人笑我忒疯癫，我笑自己命太贱；
#  *                   不见满街漂亮妹，哪个归得程序员？
# */

# @author: huhao
# @Software : PyCharm
# @file: testSeries.py
# @time: 2019/6/23 9:08
# @Ducument：https://www.python.org/doc/
# @desc:

# 导入三剑客

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt

'''
Series是一种类似于一维数组的对象，有以下两部分组成：

    values: 一组数据（ndarray类型）
    index: 相关的数据索引
'''

# Series的创建
# 1.由列表或numpy数组创建
# 默认索引为0-N-1的整数型索引

list1 = [65, 70, 59, 74, 85, 89, 90, 98, 99, 94]
s = Series(data = np.array(list1),index=list('abcdefghij'),name='Python')
print(s)

# 2.由字典创建

s2 = Series({'A':95, 'B':90, 'C':89, 'D':97},name="C++")
print(s2)

# Series的索引和切片-和Numpy类似
# 可以使用中括号取单个索引(此时返回的是元素类型)，或者中括号里一个列表取多个索引(此时返回仍是一个Series类型)，分为显示索引和隐式索引：
# (1) 显示索引：
#     - 使用index中的元素作为索引值
#     - 使用.loc[](推荐)
# 注意，此时是闭区间

print('a\t',s['a'])
print()
print(s2[['A','B','B','C']])
print(s2.loc["A"])      # loc[] 显示索引，里面规则用索引值

# (2) 隐式索引
#     - 使用整数作为索引值
#     - 使用.iloc[] (推荐)

print('s2的第一个数据\t',s2[0])
print('s2的倒数第一个数据\t',s2[-1])
print(s.iloc[0])        # iloc[] 隐式索引，里面索引值用数字

# Series的切片，切片规则与Numpy类似

print(s['a':'f'])
print(s['a':'w'])       # end的值越界索引值，直接切到最后
print(s[::2])       # 间隔2个取值
print(s.loc['a':'f'])
print(s.loc[::-1])
print(s.iloc[::-2])


# Series基本概念
# 可以把Series看作一个定长的有序字典
print(s.shape)
print(s.size)
print(s.index)
# print(s.values)
values = s.values
print(type(values))     # <class 'numpy.ndarray'>


# 可以通过head(), tail()快速查看Series对象的样式
# 当数据量庞大时,通过head(),tail()查看前几个数据和后几个数据,s.head/tail(n), n默认为5
print(s.head())
print(s.tail())


# 当索引没有对应的值时,可能出现缺失数据显示NaN(Not a Number)的情况
s[['d','f']] = np.nan
print(s)
'''
a    65.0
b    70.0
c    59.0
d     NaN
e    85.0
f     NaN
g    90.0
h    98.0
i    99.0
j    94.0
Name: Python, dtype: float64
'''

# 可以使用pd.isnull(), 或自带的isnull(),notnull()函数检测缺失数据
# 先检测空数据,然后把空数据替换成999
cond = s.isnull()
for index in s[cond].index:
    s[index]=999
print(s)
'''
a    False
b    False
c    False
d     True
e    False
f     True
g    False
h    False
i    False
j    False
Name: Python, dtype: bool
'''
print(s.notnull())
'''
a     True
b     True
c     True
d    False
e     True
f    False
g     True
h     True
i     True
j     True
Name: Python, dtype: bool
'''

# 更改数值类型
print(s.dtype)
s.astype(np.uint8)
print(s.dtype)

# 以下运算与Numpy一致
print(s.mean())
print(s.median())
print(s.max())
print(s.min())
print(s.std())
print(s.value_counts())     # 统计每个值出现的频数

# 习题:统计后缀出项的频数,输出频数最多的后缀
list1 = ['safa.mp3','fafsdf.wav','dbvsdhb.mp3','dfnsdfg.als','fsf.ps','sgds.als']
suffix = []
for str in list1:
    suffix.append(str.split('.')[-1])
print(suffix)
s = Series(data=suffix)
print(s.value_counts()[:2])

'''
一行代码搞定
Series([str.split('.')[-1] for str in list1]).value.counts()[:2]
'''



