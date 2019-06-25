#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Pandas_missingValue.py
# @time: 2019/6/23 15:38
# @Ducument：https://www.python.org/doc/
# @desc:


# 处理丢失数据
# 有两种丢失数据:
#     - None
#     - np.nan(NaN)

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Python中None和np.nan的区别

# 数据类型
print(type(None))       # <class 'NoneType'>
print(type(np.nan))     # <class 'float'>

'''
None vs NaN要点总结
在pandas中， 如果其他的数据都是数值类型， pandas会把None自动替换成NaN, 甚至能将s[s.isnull()]= None,和s.replace(NaN, None)操作的效果无效化。 这时需要用where函数才能进行替换。
None能够直接被导入数据库作为空值处理， 包含NaN的数据导入时会报错。
numpy和pandas的很多函数能处理NaN，但是如果遇到None就会报错。
None和NaN都不能被pandas的groupby函数处理，包含None或者NaN的组都会被忽略。
等值性比较的总结:（True表示被判定为相等）

 	            None对None	NaN对NaN	    None对NaN
单值  	        True	    False	    False
tuple(整体)	    True	    True	    False
np.array(逐个)	True	    False	    False
Series(逐个)  	False	    False	    False
assert_equals	True	    True	    False
Series.equals	True	    True	    True
merge	        True	    True	    True

由于等值性比较方面，None和NaN在各场景下表现不太一致，相对来说None表现的更稳定。

为了不给自己惹不必要的麻烦和额外的记忆负担。 实践中，建议遵循以下三个原则即可

    在用pandas和numpy处理数据阶段将None,NaN统一处理成NaN,以便支持更多的函数。
    如果要判断Series,numpy.array整体的等值性，用专门的Series.equals,numpy.array函数去处理，不要自己用==判断 *
    如果要将数据导入数据库，将NaN替换成None
'''
# 自己造数据的过程
# df1 = DataFrame(data=np.random.randint(0,150,size=(150,3)),columns=['Python', 'Math','En'])
# print(df1)
# 保存成excel
# df1.to_excel('./grades.xlsx')
df2 = pd.read_excel('./grades.xlsx')
print(df2)
df3 = df2.rename(mapper={'Unnamed: 0':'index'},axis=1)
df = df3.set_index(keys='index')
print()
print(df)
'''
       Python  Math   En
index                   
0          56    68   95
1         119    71    0
2          17    26   62
3          99    66    5
4          96   100   86
5          88   100   79
6          63    46   28
7         143    34  149
8         119    68  137
9          74    87    6
10        136   118    1
11         54    86   38
12          1    82   65
13          8    12   22
14         42    28    1
15        121    68    9
16        146    14    9
17         34    43   14
18        113    80   59
19        143   135   28
20         35    73    4
21         58   132  128
22        119    18  144
23        143    63  109
24         32    91  116
25         23   109  139
26         98    88   36
27         23     2  110
28          8    30   77
29         12    83   30
...       ...   ...  ...
120        52     6   32
121        22   149   77
122        16     9   69
123        64    40   23
124        78    52  113
125        39    45    8
126       116     3  146
127        49    42    1
128       149    82  132
129        55    13   10
130       146    41    9
131       149    33   39
132       132   113    0
133       104     7   23
134        86    96   36
135        45    95  102
136       133   142   13
137        93    12  137
138        63    41  135
139         8    34   89
140       111    37   58
141       118    94  123
142        51   125   48
143        17   136  144
144       105    93  114
145       148   102   79
146        88   106  116
147         8    72   64
148        27   147   58
149       132    98   78

[150 rows x 3 columns]
'''

# # 赋予空数据
# index_random = np.random.randint(0,150,size=15)
# np.savetxt('./index_random.txt',index_random)
# column_random = np.random.randint(0,3,size=15)
# np.savetxt('./column_random.txt',column_random)

nd_index = np.loadtxt('index_random.txt')
print(nd_index)
# print(type(nd_index))

nd_column = np.loadtxt('column_random.txt')
print(nd_column)

list_index = nd_index.tolist()
list_column = nd_column.tolist()
for index,column in list_index,list_column:
    df.iloc[index,column] = None
print(df.describe())


