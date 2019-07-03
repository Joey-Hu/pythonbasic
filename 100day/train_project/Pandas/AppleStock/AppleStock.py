#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: AppleStock.py
# @time: 2019/7/3 16:22
# @Document：https://www.python.org/doc/
# @desc:


import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 数据获取
# 从雅虎财经上下载apple公司一年的股票数据，文件类型为csv格式 AAPL.csv

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
# 设置显示宽度，不让他换行
pd.set_option('display.width', 1000)

# 读取数据
apple_stock = pd.read_csv('./AAPL.csv')
print(apple_stock.shape)
print(apple_stock.head())

# 检查数据类型
print(apple_stock.dtypes)
'''
Date          object    # string类型
Open         float64
High         float64
Low          float64
Close        float64
Adj Close    float64
Volume       float64
dtype: object

'''

# 将data这一列数据转换为时间类型数据
apple_stock['Date'] = pd.to_datetime(apple_stock['Date'])
print(apple_stock.dtypes)
'''
Date         datetime64[ns]
Open                float64
High                float64
Low                 float64
Close               float64
Adj Close           float64
Volume              float64
dtype: object
'''

# 将Date设置为索引
apple_stock.set_index('Date',inplace = True)
print(apple_stock.head())
'''
                Open      High       Low     Close  Adj Close       Volume
Date                                                                      
1980-12-12  0.513393  0.515625  0.513393  0.513393   0.410525  117258400.0
1980-12-15  0.488839  0.488839  0.486607  0.486607   0.389106   43971200.0
1980-12-16  0.453125  0.453125  0.450893  0.450893   0.360548   26432000.0
1980-12-17  0.462054  0.464286  0.462054  0.462054   0.369472   21610400.0
1980-12-18  0.475446  0.477679  0.475446  0.475446   0.380182   18362400.0
'''

# 重采样：根据时间进行划分，划分成天D，划分成月M，划分成年Y    resample()


# 绘制图形，字段Adj Close：已调整收盘价格
apple_stock['Adj Close'].plot()
plt.show()