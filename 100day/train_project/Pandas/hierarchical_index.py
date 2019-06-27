#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Multilayer _ndex.py
# @time: 2019/6/27 9:15
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 创建多层行索引
# 1. 隐式构造
#     最常见的方法值个DataFrame构造函数的index的参数传递两个或多个数组
#         - Series也可以创建多层索引

s1 = Series(data=[68, 140, 22, 128, 139, 143],
            index=pd.MultiIndex.from_product([['A', 'B', 'C'], ['期中', '期末']]))      # 结构清晰，最简单，推荐使用
print(s1)

# 2. 显式创建
#     - 使用array
s2 = Series(data=[68, 140, 22, 128, 139, 143],
            index=pd.MultiIndex.from_arrays([['A', 'A', 'B', 'B', 'C', 'C'], ['期中', '期末', '期中', '期末', '期中', '期末']]))
print(s2)

print("*************")
#     - 使用tuple
s3 = Series(data=[68, 140, 22, 128, 139, 143],
            index=pd.MultiIndex.from_tuples([('A', '期中'), ('A', '期末'), ('B', '期中'), ('B', '期末'), ('C', '期中'),
                                            ('C', '期末')]))
print(s3)



#           - dataframe创建多层索引(主要用到两层，三层索引与两层索引类似)
# nd1 = np.random.randint(0,150,size=(10,3))
# nd2 = nd1.tolist()
# print(nd2)
df = DataFrame(data = [[68, 148, 76], [137, 144, 48], [19, 74, 47], [4, 10, 115], [33, 142, 60], [126, 76, 110], [9, 144, 36], [84, 138, 9], [36, 113, 139], [114, 84, 140]],
               index = pd.MultiIndex.from_product([list('ABCDE'),['期中','期末']]),
               columns=['Python','Math','En'])
print(df)
'''
      Python  Math   En
A 期中      68   148   76
  期末     137   144   48
B 期中      19    74   47
  期末       4    10  115
C 期中      33   142   60
  期末     126    76  110
D 期中       9   144   36
  期末      84   138    9
E 期中      36   113  139
  期末     114    84  140
'''

# 对列进行多层索引

# nd1 = np.random.randint(0,150,size=(5,6))
# nd2 = nd1.tolist()
# print(nd2)

df2 = DataFrame(data=[[114, 42, 107, 9, 44, 29], [25, 66, 105, 131, 68, 30], [36, 99, 92, 38, 40, 85], [136, 89, 106, 125, 56, 50], [93, 15, 137, 56, 93, 28]],
                index=list('abcde'),
               columns=pd.MultiIndex.from_product([['Python','Math','En'],['期中','期末']]))
print(df2)

print('**********')
# 多层索引DataFrame的索引与切片与之前类似
print(df)
print('**********')
print(df['Python'])
print('**********')
print(df.loc[['A','期中'],'Python'])
'''
A  期中     68
   期末    137
Name: Python, dtype: int64
'''
print('**********')
print(df.loc[['A','D']])
'''
      Python  Math  En
A 期中      68   148  76
  期末     137   144  48
D 期中       9   144  36
  期末      84   138   9
'''
print('*********')
print(df.loc['A','期末']['Python'])
'''
137
'''

# 聚合运算
# 求平均值（按列）
print('*********')
print(df.mean())
'''
Python     63.0
Math      107.3
En         78.0
dtype: float64
'''
# 求平均值(按index)  level有分组的意思
print('*********')
print(df.mean(axis=0,level = 0))
'''
   Python   Math     En
A   102.5  146.0   62.0
B    11.5   42.0   81.0
C    79.5  109.0   85.0
D    46.5  141.0   22.5
E    75.0   98.5  139.5
'''
print('*********')
print(df.mean(axis=0,level=1))
'''
    Python   Math    En
期中    33.0  124.2  71.6
期末    93.0   90.4  84.4
'''


# 索引的堆
# stack()
# unstack()
print('*********')
print(df)
'''
      Python  Math   En
A 期中      68   148   76
  期末     137   144   48
B 期中      19    74   47
  期末       4    10  115
C 期中      33   142   60
  期末     126    76  110
D 期中       9   144   36
  期末      84   138    9
E 期中      36   113  139
  期末     114    84  140

'''
# unstack: 行变列
# stack: 列变行
print('*********')
print(df.unstack(level=-1))
'''
  Python      Math        En     
      期中   期末   期中   期末   期中   期末
A     68  137  148  144   76   48
B     19    4   74   10   47  115
C     33  126  142   76   60  110
D      9   84  144  138   36    9
E     36  114  113   84  139  140
'''

print('*********')
print(df.unstack(level=0))
'''
   Python                   Math                     En                   
        A   B    C   D    E    A   B    C    D    E   A    B    C   D    E
期中     68  19   33   9   36  148  74  142  144  113  76   47   60  36  139
期末    137   4  126  84  114  144  10   76  138   84  48  115  110   9  140
'''