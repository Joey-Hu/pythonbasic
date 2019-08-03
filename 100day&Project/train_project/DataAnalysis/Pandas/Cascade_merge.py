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


# pd.merge()
# 与concat的区别在于merge需要依据某一共同的行或列来进行合并

# 一对一合并

df9 = DataFrame({'id':[1, 10, 1024], 'name':['Joey', 'Po', 'Philip'], 'sex':['male', 'female', 'male']})
df10 = DataFrame({'id':[1, 11, 1025], 'age':[20, 21, 22], 'salary':[10000, 20000, 30000]})

print(df9.merge(df10))
'''
   id  name   sex  age  salary
0   1  Joey  male   20   10000
'''

# 一对多合并
# 多对多合并 同理


# key的规范化
print('***********************')
df11 = DataFrame({'id':[1, 10, 1024], 'name':['Joey', 'Po', 'Philip'], 'sex':['male', 'female', 'male']})
df12 = DataFrame({'id':[1, 11, 1025], 'name':['Joe', 'Po', 'Philip'], 'age':[20, 30, 40]})
print(pd.merge(df11, df12))     # 没有输出结果，因为尽管两表id=1一样，但是name不一样
print(pd.merge(df11, df12, on='name'))
'''
   id_x    name     sex  age  id_y
0    10      Po  female   30    11
1  1024  Philip    male   40  1025
'''

# 内合并与外合并
# how属性：inner, outer, left, right

# 列冲突
print(df11)
print(df12)
'''
     id    name     sex
0     1    Joey    male
1    10      Po  female
2  1024  Philip    male
   age    id    name
0   20     1     Joe
1   30    11      Po
2   40  1025  Philip
'''
# 当列有冲突时，即有多个列名称相同时，需要使用on=来指定哪一个列作为key,配合suffix指定冲突列名
print(pd.merge(df11,df12,on='id',suffixes=['_A','_B']))
'''
   id name_A   sex  age name_B
0   1   Joey  male   20    Joe
'''