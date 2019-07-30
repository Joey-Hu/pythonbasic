# @author: huhao
# @file: quantitative_analysis.py
# @time: 2019/7/22 7:33
# @Document：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt


data = pd.read_excel('../data/catering_fish_congee.xls')
print(data)

# 提取特定时间段的数据
# data["日期"] = pd.to_datetime(data["日期"])
# print(data.head())
# data2 = data[(data["日期"] >= pd.to_datetime("20140401")) & (data["日期"] <= pd.to_datetime("20140630"))]
# print(data2)

