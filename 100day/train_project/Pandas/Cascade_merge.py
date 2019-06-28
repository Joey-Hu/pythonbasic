#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Cascade_merge.py
# @time: 2019/6/28 21:51
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


'''
    数据的拼接分两种：
        - 级联：pd.concat, pd.append
        - 合并：pd.merge, pd.join
'''

# 回顾Numpy的级联

nd1 = np.random.randint(0, 10, size=(3, 3))
nd2 = np.random.randint(0, 10, size=(3, 3))

nd3 = np.concatenate((nd1, nd2), axis = 1)  # 水平级联
nd4 = np.concatenate((nd1, nd2))    # 垂直级联  default axis is 0

print('nd1 = ',nd1)
print('nd2 = ',nd2)
print('nd3 = ',nd3)
print('nd4 = ',nd4)


# Pandas的数据级联和Numpy类似
# 数据可能分布在不同的文件中，需要合并到一起
# print(np.random.randint(0, 150, size=(5, 3)).tolist())
df1 = DataFrame(data = [[49, 92, 78], [73, 82, 68], [117, 64, 90], [130, 123, 33], [13, 118, 96]],
                columns=['Python', 'Math', 'En'],
                index=list('ABCDE'))

df2 = DataFrame(data = [[56, 108, 133], [15, 45, 121], [45, 97, 113], [23, 119, 8], [19, 126, 112]],
                columns=['Python', 'Math', 'En'],
                index=list('HIJKL'))
print(df1)
print(df2)

df3 = pd.concat((df1,df2), axis=1)  # 水平连接
'''
   Python   Math    En  Python   Math     En
A    49.0   92.0  78.0     NaN    NaN    NaN
B    73.0   82.0  68.0     NaN    NaN    NaN
C   117.0   64.0  90.0     NaN    NaN    NaN
D   130.0  123.0  33.0     NaN    NaN    NaN
E    13.0  118.0  96.0     NaN    NaN    NaN
H     NaN    NaN   NaN    56.0  108.0  133.0
I     NaN    NaN   NaN    15.0   45.0  121.0
J     NaN    NaN   NaN    45.0   97.0  113.0
K     NaN    NaN   NaN    23.0  119.0    8.0
L     NaN    NaN   NaN    19.0  126.0  112.0

'''
df4 = pd.concat((df1,df2))  # 垂直连接  大多数情况都是两个表属性相同，使用该种方式级联
'''
   Python  Math   En
A      49    92   78
B      73    82   68
C     117    64   90
D     130   123   33
E      13   118   96
H      56   108  133
I      15    45  121
J      45    97  113
K      23   119    8
L      19   126  112
'''
print(df3)
print(df4)

# 属性合并

df6 = DataFrame(data = [[56, 108, 133], [15, 45, 121], [45, 97, 113], [23, 119, 8], [19, 126, 112]],
                columns=['Python', 'Chinese', 'En'],
                index=list('PQRST'))
df7 = pd.concat((df1,df6), axis=1)      # 默认join属性为outer, outer: 在合并时，合并所有属性，添加空数据；inner：在合并时，只合并相同属性的数据
print(df7)
# 填充空值
print(df7.fillna(0))
'''
   Python   Math    En  Chinese  Python   En
A    49.0   92.0  78.0      0.0      0.0    0.0
B    73.0   82.0  68.0      0.0      0.0    0.0
C   117.0   64.0  90.0      0.0      0.0    0.0
D   130.0  123.0  33.0      0.0      0.0    0.0
E    13.0  118.0  96.0      0.0      0.0    0.0
P     0.0    0.0   0.0     56.0    108.0  133.0
Q     0.0    0.0   0.0     15.0     45.0  121.0
R     0.0    0.0   0.0     45.0     97.0  113.0
S     0.0    0.0   0.0     23.0    119.0    8.0
T     0.0    0.0   0.0     19.0    126.0  112.0
'''
print('**************')
df8 = pd.concat((df1,df6), join='inner')
print(df8)
'''
   Python   En
A      49   78
B      73   68
C     117   90
D     130   33
E      13   96
P      56  133
Q      15  121
R      45  113
S      23    8
T      19  112
'''



# pd.append()

print(df1.append(df2))
'''
   Python  Math   En
A      49    92   78
B      73    82   68
C     117    64   90
D     130   123   33
E      13   118   96
H      56   108  133
I      15    45  121
J      45    97  113
K      23   119    8
L      19   126  112
'''