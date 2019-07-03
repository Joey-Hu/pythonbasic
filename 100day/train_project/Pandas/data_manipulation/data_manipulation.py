#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: data_manipulation.py
# @time: 2019/7/3 15:53
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# print(np.random.randint(0,150,size=(6,3)).tolist())
df = DataFrame(data=[[7, 131, 105], [48, 68, 65], [42, 51, 3], [16, 113, 143], [28, 107, 85], [39, 14, 4]],
               columns=['Python', 'Math', 'En'],
               index=pd.MultiIndex.from_product([['张三', '李四', '王五'], ['期中', '期末']]))

print(df)

# 切片
print(df.loc['张三':'李四'])

# 删除重复元素

df2 = DataFrame({'color':['red', 'green', 'blue', 'red'], 'price':[10,15,20,10]})
print(df2)
'''
   color  price
0    red     10
1  green     15
2   blue     20
3    red     10
'''

print(df2.duplicated())     # duplicated()函数检测重复的行，返回对象为布尔类型的Series对象，每个元素对应一行，如果该行不是第一次出现，则返回True

# 使用drop_duplicates()函数删除重复行
print(df2.drop_duplicates())
'''
   color  price
0    red     10
1  green     15
2   blue     20
'''
