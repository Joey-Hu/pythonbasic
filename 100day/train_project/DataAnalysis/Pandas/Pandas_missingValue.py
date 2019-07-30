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
df4 = df3.set_index(keys='index')
print()
print(df4)
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

#
# nd_index = np.loadtxt('index_random.txt')
# print(nd_index)
# # print(type(nd_index))
#
# nd_column = np.loadtxt('column_random.txt')
# print(nd_column)
#
# list_index = nd_index.tolist()
# list_column = nd_column.tolist()
#
# for i in range(15):
#     df[list_index[i],list_column[i]] = None
# print(df.info())
# print(df)

for i in range(15):
    index = np.random.randint(0,150,size=1)[0]
    column = np.random.randint(0,3,size=1)[0]
    df4.iloc[index,column] = None
print(df4.info())

# df4.to_excel('./grades.xlsx')
df5 = pd.read_excel('./grades.xlsx')
print(df5)
df6 = df5.rename(mapper={'Unnamed: 0':'index'},axis=1)
df = df6.set_index(keys='index')
print(df.info())

print('***********')
# 返回空值数据的索引
cond = df.isnull().any(axis=1)
print(df[cond])
'''
       Python   Math     En
index                      
23      143.0   63.0    NaN
27       23.0    NaN  110.0
36        7.0    NaN   72.0
42        NaN  101.0    1.0
44       42.0   40.0    NaN
47        NaN  121.0   16.0
53      118.0    NaN   86.0
55       12.0    NaN  125.0
59       59.0    NaN   68.0
65       25.0    NaN   83.0
87      112.0    NaN   75.0
88        NaN   76.0   18.0
92       88.0    NaN   34.0
103     143.0   14.0    NaN
149     132.0    NaN   78.0
'''
print('***********')
# 非空数据
cond = df.notnull().all(axis= 1)
print(df[cond])
# 或者直接用dropna()
print('***********')
print(df.dropna())  # 过滤函数 Remove missing values.
# 对应填充函数 df.fillna() 使用中位数，平均值，众数填充    向前填充，向后南充


# 删除DataFrame数据
# 删除列数据
print('***********')
print(df.drop(labels=['En'],axis=1))        # df.drop()默认删除行
'''
       Python   Math
index               
0        56.0   68.0
1       119.0   71.0
2        17.0   26.0
3        99.0   66.0
4        96.0  100.0
5        88.0  100.0
6        63.0   46.0
7       143.0   34.0
8       119.0   68.0
9        74.0   87.0
10      136.0  118.0
11       54.0   86.0
12        1.0   82.0
13        8.0   12.0
14       42.0   28.0
15      121.0   68.0
16      146.0   14.0
17       34.0   43.0
18      113.0   80.0
19      143.0  135.0
20       35.0   73.0
21       58.0  132.0
22      119.0   18.0
23      143.0   63.0
24       32.0   91.0
25       23.0  109.0
26       98.0   88.0
27       23.0    NaN
28        8.0   30.0
29       12.0   83.0
...       ...    ...
120      52.0    6.0
121      22.0  149.0
122      16.0    9.0
123      64.0   40.0
124      78.0   52.0
125      39.0   45.0
126     116.0    3.0
127      49.0   42.0
128     149.0   82.0
129      55.0   13.0
130     146.0   41.0
131     149.0   33.0
132     132.0  113.0
133     104.0    7.0
134      86.0   96.0
135      45.0   95.0
136     133.0  142.0
137      93.0   12.0
138      63.0   41.0
139       8.0   34.0
140     111.0   37.0
141     118.0   94.0
142      51.0  125.0
143      17.0  136.0
144     105.0   93.0
145     148.0  102.0
146      88.0  106.0
147       8.0   72.0
148      27.0  147.0
149     132.0    NaN

[150 rows x 2 columns]
'''

# 删除行数据(存在空值的元组)

cond = df.isnull().any(axis = 1)

# 删除小于60的元组
# cond = (df<60).any(axis=1)

# 删除平均分小于60的元组
# cond = df.mean(axis = 1)<60

# 条件的合并
# cond1 = df.mean(axis=1)<60
# cond2 = df.mean(axis=1)>100
# cond = cond1|cond2
index = df[cond].index
print(df.drop(labels=index))




