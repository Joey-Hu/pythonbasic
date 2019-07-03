#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Campaign contributions.py
# @time: 2019/7/3 17:11
# @Document：https://www.python.org/doc/
# @desc:

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 数据载入
contb1 = pd.read_csv('./data/data_01.csv')
contb2 = pd.read_csv('./data/data_02.csv')
contb3 = pd.read_csv('./data/data_03.csv')

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
# 设置显示宽度，不让他换行
pd.set_option('display.width', 1000)

# 数据合并
print(contb1.columns)
print(contb2.columns)
print(contb3.columns)
'''
Index(['cand_nm', 'contbr_nm', 'contbr_st', 'contbr_employer', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt'], dtype='object')
Index(['cand_nm', 'contbr_nm', 'contbr_st', 'contbr_employer', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt'], dtype='object')
Index(['cand_nm', 'contbr_nm', 'contbr_st', 'contbr_employer', 'contbr_occupation', 'contb_receipt_amt', 'contb_receipt_dt'], dtype='object')

'''
print(contb1.shape)
print(contb2.shape)
print(contb3.shape)
'''
(500000, 7)
(500001, 7)
(1731, 7)
'''

# 可以看出三个表的属性都一样

contb = pd.concat([contb1,contb2,contb3],axis=0)
print(contb.head())
'''
              cand_nm           contbr_nm contbr_st        contbr_employer      contbr_occupation  contb_receipt_amt contb_receipt_dt
0  Bachmann, Michelle     HARVEY, WILLIAM        AL                RETIRED                RETIRED              250.0        20-Jun-11
1  Bachmann, Michelle     HARVEY, WILLIAM        AL                RETIRED                RETIRED               50.0        23-Jun-11
2  Bachmann, Michelle       SMITH, LANIER        AL  INFORMATION REQUESTED  INFORMATION REQUESTED              250.0         5-Jul-11
3  Bachmann, Michelle    BLEVINS, DARONDA        AR                   NONE                RETIRED              250.0         1-Aug-11
4  Bachmann, Michelle  WARDENBURG, HAROLD        AR                   NONE                RETIRED              300.0        20-Jun-11
'''
print(contb.shape)  # 百万级数据
'''
(1001732, 7)
'''

# 查询是否存在空数据
print(contb.info())
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1001732 entries, 0 to 1730
Data columns (total 7 columns):
cand_nm              1001732 non-null object
contbr_nm            1001732 non-null object
contbr_st            1001728 non-null object
contbr_employer      988003 non-null object
contbr_occupation    993302 non-null object
contb_receipt_amt    1001732 non-null float64
contb_receipt_dt     1001732 non-null object
dtypes: float64(1), object(6)
memory usage: 38.2+ MB
None
'''
print('********************')
print(contb.isnull().any())
'''
cand_nm              False
contbr_nm            False
contbr_st             True
contbr_employer       True
contbr_occupation     True
contb_receipt_amt    False
contb_receipt_dt     False
dtype: bool
'''

# 查看数据描述
print(contb.dtypes)
'''
cand_nm               object
contbr_nm             object
contbr_st             object
contbr_employer       object
contbr_occupation     object
contb_receipt_amt    float64
contb_receipt_dt      object
dtype: object
'''
# print(contb.descibe())        # 返回错误信息，AttributeError: 'DataFrame' object has no attribute 'descibe'  describe is a Series method rather than a DataFrame method

print(contb['contb_receipt_amt'].describe())    # 对数据有一个大概的认识
'''
count    1.001732e+06   总共有1001732条记录
mean     2.982358e+02   平均298.2358元
std      3.749665e+03   标准差3749.665,捐献的差距很大，max=$2014491，min = $-3080(负数？？？)
min     -3.080000e+04
25%      3.500000e+01
50%      1.000000e+02
75%      2.500000e+02
max      2.014491e+06
Name: contb_receipt_amt, dtype: float64
'''

# 缺失值处理 填充
cond = contb['contbr_st'].isnull()
print(contb[cond])
contb['contbr_st'].fillna('NOT PROVIDE',inplace=True)
contb['contbr_employer'].fillna('NOT PROVIDE',inplace=True)
contb['contbr_occupation'].fillna('NOT PROVIDE',inplace=True)
print(contb.info())
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1001732 entries, 0 to 1730
Data columns (total 7 columns):
cand_nm              1001732 non-null object
contbr_nm            1001732 non-null object
contbr_st            1001732 non-null object
contbr_employer      1001732 non-null object
contbr_occupation    1001732 non-null object
contb_receipt_amt    1001732 non-null float64
contb_receipt_dt     1001732 non-null object
dtypes: float64(1), object(6)
memory usage: 38.2+ MB
None
'''


