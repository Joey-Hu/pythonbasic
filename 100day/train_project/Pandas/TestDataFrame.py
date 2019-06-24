#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: TestDataFrame.py
# @time: 2019/6/23 15:57
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import xlrd


# DataFrame的创建
# 最常用的方法是传递一个字典来创建，DataFrame以字典的键作为每一列的名称，以字典的值(一个数组)作为每一列。
# 此外，DataFrame会自动加上每一行的索引（和Series一样）。
# 同Series一样，若传入的列与字典的键不匹配，则相应的值为nan

# df = DataFrame(data={'Python':np.random.randint(0,150,size=5),
#                      'Math':np.random.randint(0,150,size=5),
#                      'En':np.random.randint(0,150,size=5)},index=list('abcde'))
df = DataFrame(data={'Python':[116, 64, 116, 138, 117],
                     'Math':[63, 65, 129, 103, 68],
                     'En':[56, 108, 28, 140, 69]},index=['huhao','zhangsan','lisi','wanger','zhangwei'])
print(df)
'''
           En  Math  Python
huhao      56    63     116
zhangsan  108    65      64
lisi       28   129     116
wanger    140   103     138
zhangwei   69    68     117

***为什么列名会逆序呢？？？
'''

df2 = DataFrame(data=np.random.randint(0,150,size=(10,4)),index = list('abcdefghij'),columns=['Python','Math','En','CLP'])
print(df2)

# 将数据保存成.txt,.xlsx
# df2.to_csv('./data.txt')
# df2.to_excel('./data.xlsx')

# 读取.txt数据
df3 = pd.read_csv('./data.txt')
print(df3)      # 出现Unnamed列
'''
  Unnamed: 0  Python  Math   En  CLP
0          a     118   102  132   72
1          b      61    11   48   87
2          c     109    88   92   38
3          d      83    12  133  122
4          e     144    38   97  104
5          f      85    69    1   41
6          g      39   134   69   51
7          h     112   100   59  104
8          i     105    90    4   71
9          j     130    90  134   41
'''
df4 = df3.rename(mapper={'Unnamed: 0':'index'},axis=1);
df5 = df4.set_index(keys='index')
print(df5)
'''
       Python  Math   En  CLP
index                        
a         118   102  132   72
b          61    11   48   87
c         109    88   92   38
d          83    12  133  122
e         144    38   97  104
f          85    69    1   41
g          39   134   69   51
h         112   100   59  104
i         105    90    4   71
j         130    90  134   41
'''

# 读取.xslx数据
df6 = pd.read_excel('./data.xlsx')
print(df6)


# dataFrame的属性

print(df.values)    # 返回二维列表
print(df.columns)   # Index(['En', 'Math', 'Python'], dtype='object')
print(df.index)     # Index(['huhao', 'zhangsan', 'lisi', 'wanger', 'zhangwei'], dtype='object')
print(df.shape)     # (5, 3)
print(df.dtypes)
'''
En        int64
Math      int64
Python    int64
dtype: object

'''


# 对列进行索引
#     - 通过类似字典的方式, eg: df[['Python','Math']]
#     - 通过属性的方式,eg: df.Pthon
# 可以将DataFrame的队列获取为一个Series, 返回的Series拥有原DataFrame相同的索引，且name属性也已经设置好了，就是相应的列名

print(df2.Python)
print(type(df2.Python))     # <class 'pandas.core.series.Series'>
print()
print(df2[['Math','En']])
'''
   Math   En
a    36  126
b   147   57
c   139  145
d    94  132
e   124   31
f    29  121
g    87  124
h    71   45
i   140   82
j   147   28
'''

# 对行进行索引
# 1. 通过df.loc[]
print(df2.loc[['a','c']])
'''
   Python  Math  En  CLP
a      76   103  78   59
c      24   105  30  113

'''
# 2. 通过df.iloc[]
print(df2.iloc[[2,3]])
'''
   Python  Math   En  CLP
c      11    59  110  117
d      56    15  140   12
'''

# 对元素索引
# 先行后列df.loc[][]
# 先列后行df[][]
# df.loc['index','column']
print(df5)
print(df5['Python']['b'])
print(df5.loc['b']['Python'])
print(df5.loc['b','Python'])        # 此方法必须先行后列


# # 切片
# 对行进行切片
print()
print(df2['a':'f'])
'''
   Python  Math   En  CLP
a      74   134  129   64
b      50   142   64  143
c     113    52   11  135
d      30    68   62  107
e      80    56  109   72
f      31    88  106  144
'''
print(df2.loc['a':'c'])
print(df2.iloc[0:3])

# 对列进行切片,和前面列索引类似
print(df2.iloc[:,0:2])
'''
   Python  Math
a     147    58
b     113   116
c     121    16
d       5    24
e      67    11
f     108   135
g     105     4
h      54    51
i     126   121
j      91     1
'''

# DataFrame的运算
print(df5+10)
'''
       Python  Math   En  CLP
index                        
a         128   112  142   82
b          71    21   58   97
c         119    98  102   48
d          93    22  143  132
e         154    48  107  114
f          95    79   11   51
g          49   144   79   61
h         122   110   69  114
i         115   100   14   81
j         140   100  144   51
'''

print(df5.pow(2))
'''
j         140   100  144   51
       Python   Math     En    CLP
index                             
a       13924  10404  17424   5184
b        3721    121   2304   7569
c       11881   7744   8464   1444
d        6889    144  17689  14884
e       20736   1444   9409  10816
f        7225   4761      1   1681
g        1521  17956   4761   2601
h       12544  10000   3481  10816
i       11025   8100     16   5041
j       16900   8100  17956   1681
'''
print(df5.divide(3).round(2))       # 保留两位小数
'''
       Python   Math     En    CLP
index                             
a       39.33  34.00  44.00  24.00
b       20.33   3.67  16.00  29.00
c       36.33  29.33  30.67  12.67
d       27.67   4.00  44.33  40.67
e       48.00  12.67  32.33  34.67
f       28.33  23.00   0.33  13.67
g       13.00  44.67  23.00  17.00
h       37.33  33.33  19.67  34.67
i       35.00  30.00   1.33  23.67
j       43.33  30.00  44.67  13.67
'''
print(df5.cov())
print(df5.corr())
'''
          Python      Math        En       CLP
Python  1.000000 -0.014083  0.345338  0.100817
Math   -0.014083  1.000000 -0.078859 -0.580825
En      0.345338 -0.078859  1.000000  0.202063
CLP     0.100817 -0.580825  0.202063  1.000000
'''
# 输出df的基本信息
print(df5.info())
'''
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
Python    10 non-null int64
Math      10 non-null int64
En        10 non-null int64
CLP       10 non-null int64
dtypes: int64(4)
memory usage: 552.0+ bytes
None
'''
df5.iloc[3,3] = None
print(df5)
'''
        Python  Math   En    CLP
index                          
a         118   102  132   72.0
b          61    11   48   87.0
c         109    88   92   38.0
d          83    12  133    NaN
e         144    38   97  104.0
f          85    69    1   41.0
g          39   134   69   51.0
h         112   100   59  104.0
i         105    90    4   71.0
j         130    90  134   41.0
'''
print(df5.info())
'''
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
Python    10 non-null int64
Math      10 non-null int64
En        10 non-null int64
CLP       9 non-null float64
dtypes: float64(1), int64(3)
memory usage: 552.0+ bytes
None
'''
print(df5.describe())
'''
50%: 中位数，25%: 0%-中位数之间的中位数， 75%：中位数到100%之间的中位数
           Python        Math          En         CLP
count   10.000000   10.000000   10.000000    9.000000
mean    98.600000   73.400000   76.900000   67.666667
std     31.878938   40.686334   49.854121   26.514147
min     39.000000   11.000000    1.000000   38.000000
25%     83.500000   45.750000   50.750000   41.000000
50%    107.000000   89.000000   80.500000   71.000000
75%    116.500000   97.500000  123.250000   87.000000
max    144.000000  134.000000  134.000000  104.000000
'''

