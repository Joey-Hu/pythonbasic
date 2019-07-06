#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Campaign contributions_1.py
# @time: 2019/7/5 11:52
# @Document：https://www.python.org/doc/
# @desc:

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
# pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
# 设置显示宽度，不让他换行
pd.set_option('display.width', 1000)


contb_vs = pd.read_csv('./data/contb.csv')
contb_vs_dt = pd.read_csv('./data/contb_vs_dt.csv')
# 以时间作为索引
contb_vs_dt['contb_receipt_dt'] = pd.to_datetime(contb_vs_dt['contb_receipt_dt'])
contb_vs_time = contb_vs_dt.set_index('contb_receipt_dt')
print(contb_vs_time.head())
print(contb_vs_time.dtypes)

# 重采样和频率转换
# 行索引是时间，就能进行resample
vs_m = contb_vs_time.groupby('cand_nm').resample('M')['contb_receipt_amt'].sum().unstack(level=0)
# vs_m.plot(kind='bar')   #条形图
# vs_m.plot(kind='line')   #线形图
# vs_m.plot(kind='area')   #面积图
#
# plt.show()


# 各州支持率
# 依据州和候选人进行分组
support_st = contb_vs.groupby(['cand_nm','contbr_st'])['contb_receipt_amt'].sum().unstack(level=0)
print(support_st)
'''
cand_nm      Obama, Barack  Romney, Mitt
contbr_st                               
AA                56405.00        135.00
AB                 2048.00           NaN
AE                42973.75       5680.00
AK               281840.15      86204.24
AL               543123.48     527303.51
AP                37130.50       1655.00
AR               359247.28     105556.00
AS                 2955.00           NaN
AZ              1506476.98    1888436.23
CA             23824984.24   11237636.60
CO              2132429.49    1506714.12
CT              2068291.26    3499475.45
DC              4373538.80    1025137.50
DE               336669.14      82712.00
FF                     NaN      99030.00
FL              7318178.58    8338458.81
FM                  600.00           NaN
GA              2786399.49    1995725.59
GU                11581.50       3850.00
HI               795212.64     111763.00
IA               584829.10     208537.49
ID               197538.06     787158.44
IL             16443895.84    3628571.53
IN               883691.81     542086.23
KS               448038.57     326633.87
KY               714954.32     666902.59
LA               548013.54     991236.60
MA              6649015.25    4710542.30
MD              4832663.93    1633690.40
ME              1167760.12     117151.84
...                    ...           ...
NE               251311.97     178600.50
NH               616994.85     424839.11
NJ              3203257.93    3333320.20
NM               906162.36     168011.36
NOT PROVIDE        1800.00           NaN
NV               710693.67     630049.49
NY             14652118.51   10184212.63
OH              1822728.83    1901560.66
OK               594342.52     839483.96
ON                 1955.00           NaN
OR              1222942.39     526237.73
PA              3713426.98    1941519.43
PR               216019.00      29125.00
QU                  500.00           NaN
RI               457352.22     187892.92
SC               630732.94     402742.86
SD                86530.76     166558.00
TN              1119315.02    1516918.04
TX              6570832.45    6221989.68
UK                     NaN       2500.00
UT               519851.37    3717300.48
VA              4259977.19    3465765.85
VI                80712.00       3500.00
VT               986510.59      55229.44
WA              4250933.16    1341521.56
WI              1130155.46     270316.32
WV               169154.47     126725.12
WY               194046.74     252595.84
XX                     NaN     400250.00
ZZ                 5963.00           NaN

[68 rows x 2 columns]
'''

support_st.fillna(0,inplace=True)
print(support_st)

# plt.figure(figsize=(23,9))
# ax = plt.subplot(1,1,1)
# support_st.plot(kind='bar')
# plt.show()

support_st_rate = support_st.div(support_st.sum(axis=1),axis=0)
print(support_st_rate)
'''
cand_nm      Obama, Barack  Romney, Mitt
contbr_st                               
AA                0.997612      0.002388
AB                1.000000      0.000000
AE                0.883257      0.116743
AK                0.765778      0.234222
AL                0.507390      0.492610
AP                0.957329      0.042671
AR                0.772902      0.227098
AS                1.000000      0.000000
AZ                0.443745      0.556255
CA                0.679498      0.320502
CO                0.585970      0.414030
CT                0.371476      0.628524
DC                0.810113      0.189887
DE                0.802776      0.197224
FF                0.000000      1.000000
FL                0.467417      0.532583
FM                1.000000      0.000000
GA                0.582670      0.417330
GU                0.750510      0.249490
HI                0.876774      0.123226
IA                0.737149      0.262851
ID                0.200608      0.799392
IL                0.819226      0.180774
IN                0.619796      0.380204
KS                0.578359      0.421641
KY                0.517387      0.482613
LA                0.356026      0.643974
MA                0.585323      0.414677
MD                0.747355      0.252645
ME                0.908825      0.091175
...                    ...           ...
NE                0.584565      0.415435
NH                0.592220      0.407780
NJ                0.490051      0.509949
NM                0.843590      0.156410
NOT PROVIDE       1.000000      0.000000
NV                0.530074      0.469926
NY                0.589947      0.410053
OH                0.489417      0.510583
OK                0.414515      0.585485
ON                1.000000      0.000000
OR                0.699152      0.300848
PA                0.656669      0.343331
PR                0.881192      0.118808
QU                1.000000      0.000000
RI                0.708804      0.291196
SC                0.610303      0.389697
SD                0.341899      0.658101
TN                0.424589      0.575411
TX                0.513634      0.486366
UK                0.000000      1.000000
UT                0.122689      0.877311
VA                0.551400      0.448600
VI                0.958438      0.041562
VT                0.946983      0.053017
WA                0.760119      0.239881
WI                0.806982      0.193018
WV                0.571700      0.428300
WY                0.434456      0.565544
XX                0.000000      1.000000
ZZ                1.000000      0.000000

[68 rows x 2 columns]
'''

support_st_rate.drop(labels=['AA','AB','AE','NOT PROVIDE'],inplace=True)

# basemap工具包

from mpl_toolkits.basemap import Basemap

'''
llcrnrlon: 所需地图域的左下角经度
llcrnrlat: 所需地图域的左下角纬度
urcrnrlon: 所需地图域的右上角经度
urcrnrlat：所需地图域的右上角纬度
'''
map = Basemap(llcrnrlon=-122,
              llcrnrlat=23.4,
              urcrnrlon=-64,
              urcrnrlat=45.44,
              projection='lcc',
              lat_1=30,
              lat_2=35,
              lon_0=-100)

# map.drawcoastlines(linewidth=1.5)
# map.drawcountries(linewidth=1.5)
# map.drawstates()
#
# plt.show()

# 地图着色

print(support_st_rate)

cmap = plt.cm.Blue

for i in range(10):
    plt.plot(np.arange(10)+i,c = cmap((i+1)/10))
plt.show()









