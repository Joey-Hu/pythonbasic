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
# pd.set_option('display.max_rows', None)
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

# 数据转换：利用字典映射进行转换：党派分析
# 通过搜索引擎等途径，获取到每个总统候选人的所属党派，建立字典parties，候选人的名字作为键，所属党派作为对应的值
# print(contb['cand_nm'].unique())
# print(contb.cand_nm.unique())
parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt': 'Republican',
           'Huntsman, Jon': 'Republican',
           'Johnson, Gary Earl': 'Republican',
           'McCotter, Thaddeus G': 'Republican',
           'Obama, Barack': 'Democrat',
           'Paul, Ron': 'Republican',
           'Pawlenty, Timothy': 'Republican',
           'Perry, Rick': 'Republican',
           "Roemer, Charles E. 'Buddy' III": 'Republican',
           'Romney, Mitt': 'Republican',
           'Santorum, Rick': 'Republican',}

# 将候选人所属党派也加入到DataFrame中，使用map映射    100万数据，给其增加一列耗时125ms
contb['party'] = contb['cand_nm'].map(parties)

# 党派支持率
print(contb['party'].value_counts())
'''
Democrat      593747
Republican    407985
Name: party, dtype: int64
'''

# 根据政党对捐献金额总和进行统计
print(contb.groupby('party')['contb_receipt_amt'].sum())
'''
party
Democrat      1.335028e+08
Republican    1.652496e+08
Name: contb_receipt_amt, dtype: float64
'''

# 按照职业汇总对赞助总金额进行排序
# print(contb.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False))
print(contb.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[50:100])
'''
contbr_occupation
RETIRED                                   48176397.00
ATTORNEY                                  18470473.30
HOMEMAKER                                 17484807.65
INFORMATION REQUESTED PER BEST EFFORTS    15859514.55
INFORMATION REQUESTED                      8742357.59
PHYSICIAN                                  7224044.40
PRESIDENT                                  6347843.59
EXECUTIVE                                  5273717.90
CONSULTANT                                 4932627.98
NOT PROVIDE                                4224760.39
CEO                                        3570942.20
LAWYER                                     3537982.19
OWNER                                      3278488.16
INVESTOR                                   3204481.92
ENGINEER                                   2730527.43
PROFESSOR                                  2458033.81
C.E.O.                                     2433218.11
SELF-EMPLOYED                              2259150.94
MANAGER                                    2167571.47
REAL ESTATE                                2110499.34
SALES                                      1814901.82
NOT EMPLOYED                               1752927.93
BUSINESS OWNER                             1736511.73
TEACHER                                    1709754.05
CHAIRMAN                                   1691595.37
STUDENT                                    1679435.28
FINANCE                                    1664021.31
BANKER                                     1462903.13
WRITER                                     1303267.29
PARTNER                                    1177656.55
VICE PRESIDENT                             1177600.41
INVESTMENTS                                1120947.94
MANAGING DIRECTOR                           969128.57
INVESTMENT BANKER                           961297.90
ARTIST                                      959387.57
DIRECTOR                                    855121.89
SOFTWARE ENGINEER                           836558.02
ACCOUNTANT                                  828374.46
FARMER                                      747042.89
DENTIST                                     741347.59
FINANCIAL ADVISOR                           660786.63
ARCHITECT                                   656140.41
PRESIDENT & C.E.O.                          642686.28
CPA                                         606266.64
INVESTMENT MANAGER                          601899.60
INVESTMENT MANAGEMENT                       583189.02
REAL ESTATE DEVELOPER                       578934.25
PRINCIPAL                                   569543.44
REQUESTED                                   567872.46
PRIVATE EQUITY                              555939.00
Name: contb_receipt_amt, dtype: float64

'''

# 合并一些职业信息: 因为不少职业是相同的，只是表达方式不一样
occupation = {'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDE',
              'INFORMATION REQUESTED':'NOT PROVIDE',
              'C.E.O':'CEO',
              'C.E.O.':'CEO',
              'LAWYER':'ATTORNEY',
              'SELF':'SELF-EMPLOYED',
              'SELF EMPLOYED':'SELF-EMPLOYED'}

f = lambda x : occupation.get(x,x)
contb['contbr_occupation'] = contb['contbr_occupation'].map(f)
print('#################################################')
print(contb.groupby('contbr_occupation')['contb_receipt_amt'].sum().sort_values(ascending=False)[:50])


# 按照雇主汇总对赞助总金额进行排序
print(contb.groupby('contbr_employer')['contb_receipt_amt'].sum().sort_values(ascending=False)[:50])
'''
contbr_employer
RETIRED                                   41374333.67
SELF-EMPLOYED                             28745318.28
INFORMATION REQUESTED PER BEST EFFORTS    16629440.70
HOMEMAKER                                 14738524.86
INFORMATION REQUESTED                      8997347.66
NOT EMPLOYED                               8636809.43
NOT PROVIDE                                5655209.40
SELF                                       5243486.83
NONE                                       3809332.99
SELF EMPLOYED                              3495090.11
STUDENT                                     957971.85
REQUESTED                                   894009.54
MORGAN STANLEY                              386129.40
UNEMPLOYED                                  377088.31
INFORMATION REQUESTED (BEST EFFORTS)        340503.63
CREDIT SUISSE                               300740.90
VOLUNTEER                                   294118.02
MICROSOFT                                   286304.32
GOLDMAN SACH & CO.                          233250.00
US ARMY                                     230796.52
GOLDMAN SACHS                               205338.57
BANK OF AMERICA                             197408.93
IBM                                         197129.19
SIDLEY AUSTIN LLP                           191733.70
BARCLAYS CAPITAL                            188560.20
WELLS FARGO                                 166585.93
CITIGROUP                                   166091.20
MERRILL LYNCH                               163069.44
DLA PIPER                                   158735.00
GOOGLE                                      155917.58
REFUSED                                     152116.07
MICROSOFT CORPORATION                       151719.60
HARVARD UNIVERSITY                          148870.14
KIRKLAND & ELLIS LLP                        147762.00
H.I.G. CAPITAL                              147000.00
JONES DAY                                   142084.30
AT&T                                        136291.14
KAISER PERMANENTE                           134193.06
J.P. MORGAN                                 133448.00
STANFORD UNIVERSITY                         130760.63
US GOVERNMENT                               123458.38
AETNA                                       118614.84
VERIZON                                     118491.18
COLUMBIA UNIVERSITY                         117830.61
BAIN & COMPANY                              110925.00
KIRKLAND & ELLIS L.L.P.                     104736.00
E.M.C. CORPORATION                          104450.00
BAIN CAPITAL                                103720.00
CITI                                        103620.93
FIDELITY INVESTMENTS                        103486.05
Name: contb_receipt_amt, dtype: float64
'''

# 合并公司
employer = {'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDE',
           'INFORMATION REQUESTED':'NOT PROVIDE',
           'SELF':'SELF-EMPLOYED',
           'SELF EMPLOYED':'SELF-EMPLOYED',
           'NONE':'NOT PROVIDE'}
f = lambda x : employer.get(x,x)
contb['contbr_employer'] = contb['contbr_employer'].map(f)
print(contb.groupby('contbr_employer')['contb_receipt_amt'].sum().sort_values(ascending=False)[:50])


# 数据筛选
# 捐赠金额大于0
cond = contb['contb_receipt_amt'] > 0
contb_ = contb[cond]
print(contb.shape)
print(contb_.shape)
'''
Name: contb_receipt_amt, dtype: float64
(1001732, 8)
(991476, 8)
'''

# 查看各候选人获得的赞助总金额
cand_nm_amt = contb_.groupby('cand_nm')['contb_receipt_amt'].sum().sort_values(ascending=False)
print(cand_nm_amt)
'''
cand_nm
Obama, Barack                     1.358776e+08
Romney, Mitt                      8.833591e+07
Paul, Ron                         2.100962e+07
Perry, Rick                       2.030675e+07
Gingrich, Newt                    1.283277e+07
Santorum, Rick                    1.104316e+07
Cain, Herman                      7.101082e+06
Pawlenty, Timothy                 6.004819e+06
Huntsman, Jon                     3.330373e+06
Bachmann, Michelle                2.711189e+06
Johnson, Gary Earl                5.669616e+05
Roemer, Charles E. 'Buddy' III    3.730099e+05
McCotter, Thaddeus G              3.903000e+04
Name: contb_receipt_amt, dtype: float64
'''

# cand_nm_amt.plot(kind = 'bar')  # 柱状图
# cand_nm_amt.plot(kind = 'barh')     # 水平柱状图
# cand_nm_amt.plot(kind = 'pie')      # 饼图
# plt.show()


# 选区候选人为Obama, Romney的子集数据
# 方式一：
cond1 = contb_['cand_nm'] == 'Obama, Barack'
cond2 = contb_['cand_nm'] == 'Romney, Mitt'
cond = cond1 | cond2
contb_vs = contb_[cond]
print(contb_vs[:100])

'''
# 方式二：
print('######################################################')
contb_vs2 = contb_.query("cand_nm =='Obama, Barack' or cand_nm =='Romney, Mitt'")
print(contb_vs2[:100])

#方式三：
print('######################################################')
cond = contb_['cand_nm'].isin(['Obama, Barack','Romney, Mitt'])
contb_vs3 = contb_[cond]
'''


# 面元化数据
# 利用cut函数根据出资额大小将数据离散化到多个面元中
print(contb_.contb_receipt_amt.unique().size)       # 7326
print(contb_.contb_receipt_amt.max())       # 2014490.51
print(contb_.contb_receipt_amt.min())       # 0.01
bins = [0,1,10,100,1000,10000,100000,1000000,5000000]
labels = pd.cut(contb_['contb_receipt_amt'],bins)
print(labels[:10])
'''
0    (100, 1000]
1      (10, 100]
2    (100, 1000]
3    (100, 1000]
4    (100, 1000]
5    (100, 1000]
6    (100, 1000]
7    (100, 1000]
8    (100, 1000]
9    (100, 1000]
Name: contb_receipt_amt, dtype: category
Categories (8, interval[int64]): [(0, 1] < (1, 10] < (10, 100] < (100, 1000] < (1000, 10000] < (10000, 100000] < (100000, 1000000] < (1000000, 5000000]]

'''
print(contb_['contb_receipt_amt'][:10])
'''
对比上面
0    250.0
1     50.0
2    250.0
3    250.0
4    300.0
5    500.0
6    250.0
7    250.0
8    250.0
9    250.0
Name: contb_receipt_amt, dtype: float64

'''


# 数据聚合与分组运算
# 透视表（pivot_table）分析党派和职业
# 按照党派、职业对赞助金额进行汇总，类似Excel的透视表操作，聚合函数为sum

ret = contb_.pivot_table('contb_receipt_amt', index='contbr_occupation', columns='party',aggfunc='sum', fill_value=0)
print(ret)
'''
party                                  Democrat  Republican
contbr_occupation                                          
   MIXED-MEDIA ARTIST / STORYTELLER       100.0        0.00
 AREA VICE PRESIDENT                      250.0        0.00
 RESEARCH ASSOCIATE                       100.0        0.00
 TEACHER                                  500.0        0.00
 THERAPIST                               3900.0        0.00
'MIS MANAGER                                0.0      177.60
(PART-TIME) SALES CONSULTANT & WRITER       0.0      285.00
(RETIRED)                                   0.0      250.00
-                                        5000.0     2114.80
--                                          0.0       75.00
.NET PROGRAMMER                           481.0        0.00
0                                           0.0       20.00
07/13/1972                                 98.0        0.00
100% DISABLED ARMY VET                      0.0      350.00
100% DISABLED VETERAN                       0.0     2080.78
100% DISABLED VIET NAM COMBAT VETER         0.0      100.00
100% DISABLED VIETNAM VETERAN               0.0      236.25
11B                                         0.0      300.00
12K ADVOCATE                              150.0        0.00
13B CANNON CREWMEMBER                       0.0       71.80
13D                                       721.0        0.00
15J                                         0.0      150.00
15U - CHINOOK MECHANIC                      0.0      200.00
1SG RETIRED                               210.0        0.00
1ST ASSISTANT DIRECTOR 2ND UNIT            35.0        0.00
1ST ASSISTANT SOUND EDITOR                  0.0      292.80
1ST GRADE TEACHER                         435.0        0.00
1ST LIEUTENANT (MILITARY OFFICER)           0.0      500.00
1ST LIEUTENANT (RET)                        0.0      449.50
1ST LT                                      0.0      500.00
...                                         ...         ...
YOUTH CORRECTIONS SUPERVISOR               50.0        0.00
YOUTH COUNSELOR                             0.0     1133.05
YOUTH COUNTRY CHAIR                         0.0      250.00
YOUTH DEVELOPMENT                         650.0        0.00
YOUTH DIRECTOR                            550.0      546.32
YOUTH MINISTER                            725.0      780.24
YOUTH MINISTRY                              0.0      250.00
YOUTH OUTREACH DIRECTOR                     0.0     1000.00
YOUTH PASTOR                                0.0      335.00
YOUTH PROGRAMS DIRECTOR                   205.0        0.00
YOUTH SERVICE AIDE                          0.0       88.60
YOUTH SERVICE COORDINATOR                 425.0        0.00
YOUTH SERVICES LIBRARIAN                  290.0        0.00
YOUTH SERVICES MANAGER                    300.0        0.00
YOUTH SPECIALIST                          652.0        0.00
YOUTH SPORTS DIRECTOR                     110.0        0.00
YOUTH VOTE DIRECTOR                       165.0        0.00
YOUTH WORKER                                0.0     1011.74
ZEN BUDDHIST PRIEST                       400.0        0.00
ZEN TEACHER                               100.0        0.00
ZEPPOS AND ASSOCIATES                    1000.0        0.00
ZIMMERMANS DAIRY                            0.0       83.71
ZMS                                         0.0       70.12
ZOMBIE SLAYER                               0.0      125.00
ZONE MANAGER                              135.0        0.00
ZOOKEEPER                                  35.0        0.00
ZOOLOGIST                                 400.0        0.00
ZOOLOGY EDUCATION                          25.0        0.00
NONE                                     0.0      250.00
~                                           0.0       75.00

[45061 rows x 2 columns]
'''

# 将每个职业所捐赠的献金加和并排序，得出哪个职业捐的献金最多

print(ret.sum(axis=1).sort_values(ascending=False))
'''
contbr_occupation
RETIRED                                   4.886631e+07
NOT PROVIDE                               3.469680e+07
ATTORNEY                                  2.217088e+07
HOMEMAKER                                 1.788315e+07
PHYSICIAN                                 7.329445e+06
PRESIDENT                                 6.599434e+06
CEO                                       6.309716e+06
EXECUTIVE                                 5.494011e+06
CONSULTANT                                5.004638e+06
OWNER                                     3.409854e+06
INVESTOR                                  3.315902e+06
SELF-EMPLOYED                             2.987019e+06
ENGINEER                                  2.769899e+06
PROFESSOR                                 2.461774e+06
MANAGER                                   2.207416e+06
REAL ESTATE                               2.154804e+06
SALES                                     1.848352e+06
CHAIRMAN                                  1.792640e+06
BUSINESS OWNER                            1.773322e+06
NOT EMPLOYED                              1.754008e+06
TEACHER                                   1.714954e+06
STUDENT                                   1.701383e+06
FINANCE                                   1.698546e+06
BANKER                                    1.483553e+06
WRITER                                    1.312117e+06
PARTNER                                   1.237937e+06
VICE PRESIDENT                            1.205809e+06
INVESTMENTS                               1.179148e+06
INVESTMENT BANKER                         9.993329e+05
MANAGING DIRECTOR                         9.963786e+05
                                              ...     
TEMP PARALEGAL                            5.000000e+00
PROFESSIONAL PROMOTER                     5.000000e+00
EDUCATION ADMIN                           5.000000e+00
PROFESSIONAL AUTHOR                       5.000000e+00
RANCHER, ENVIRONMENTALIST                 5.000000e+00
HOMEMAKER/TEACHER                         5.000000e+00
ALTERATIONS                               5.000000e+00
FINANCIAL INSTITUTION - CEO               5.000000e+00
ENVIRONMENTAL INVESTIGATOR                5.000000e+00
SR. PROJECT MGR. & PROCESS ANALYST        5.000000e+00
EDITOR IN CHIEF AND EXEC. VICE PRESIDE    5.000000e+00
CONTRACT REP                              5.000000e+00
SYSTEMS ANALYST/FREELANCE WRITER          5.000000e+00
PRODUCE/DSD CLERK                         5.000000e+00
RESEARCHER / WRITER/ ETC                  5.000000e+00
ADMINISTRATIVE MANAGEMENT                 4.120000e+00
MEDIA & FINANCIAL SERVICE                 4.000000e+00
REMODELER & SEMI RETIRED                  3.000000e+00
IFC CONTRACTING SOLUTIONS                 3.000000e+00
AFFORDABLE REAL ESTATE DEVELOPER          3.000000e+00
INDEPENDENT PROFESSIONAL                  3.000000e+00
SR MGR                                    3.000000e+00
3RD GENERATION FAMILY BUSINESS OWNER      3.000000e+00
ADMINISTRATION/INSTRUCTOR                 3.000000e+00
LEAD UI/UX DEVELOPER                      3.000000e+00
SPRINKLER FITTER FIRE PROTECTION SPECI    3.000000e+00
LAN/WAN ANALYST                           3.000000e+00
POLICY/ LAWYER                            3.000000e+00
VICE PRESIDENT, REAL ESTATE               1.000000e+00
FREELANCE VOICE-OVER                      1.000000e+00
Length: 45061, dtype: float64
'''

ret['total'] = ret['Democrat'] + ret['Republican']

print(ret.sort_values(by= 'total', ascending=False))
'''
party                                      Democrat    Republican         total
contbr_occupation                                                              
RETIRED                                 25305316.38  2.356099e+07  4.886631e+07
NOT PROVIDE                             13725187.32  2.097161e+07  3.469680e+07
ATTORNEY                                14302461.84  7.868419e+06  2.217088e+07
HOMEMAKER                                4248875.80  1.363428e+07  1.788315e+07
PHYSICIAN                                3735124.94  3.594320e+06  7.329445e+06
PRESIDENT                                1878509.95  4.720924e+06  6.599434e+06
CEO                                      2075974.79  4.233742e+06  6.309716e+06
EXECUTIVE                                1355161.05  4.138850e+06  5.494011e+06
CONSULTANT                               2459912.71  2.544725e+06  5.004638e+06
OWNER                                    1001567.36  2.408287e+06  3.409854e+06
INVESTOR                                  884133.00  2.431769e+06  3.315902e+06
SELF-EMPLOYED                             741746.40  2.245273e+06  2.987019e+06
ENGINEER                                  951525.55  1.818374e+06  2.769899e+06
PROFESSOR                                2165071.08  2.967027e+05  2.461774e+06
MANAGER                                   762883.22  1.444532e+06  2.207416e+06
REAL ESTATE                               528902.09  1.625902e+06  2.154804e+06
SALES                                     392886.91  1.455465e+06  1.848352e+06
CHAIRMAN                                  496547.00  1.296093e+06  1.792640e+06
BUSINESS OWNER                            449979.30  1.323342e+06  1.773322e+06
NOT EMPLOYED                             1709188.20  4.481973e+04  1.754008e+06
TEACHER                                  1250969.15  4.639849e+05  1.714954e+06
STUDENT                                   628099.75  1.073284e+06  1.701383e+06
FINANCE                                   296031.40  1.402515e+06  1.698546e+06
BANKER                                    224084.40  1.259469e+06  1.483553e+06
WRITER                                   1084188.88  2.279284e+05  1.312117e+06
PARTNER                                   395759.50  8.421771e+05  1.237937e+06
VICE PRESIDENT                            325647.15  8.801623e+05  1.205809e+06
INVESTMENTS                               160480.00  1.018668e+06  1.179148e+06
INVESTMENT BANKER                         164011.70  8.353212e+05  9.993329e+05
MANAGING DIRECTOR                         329688.25  6.666903e+05  9.963786e+05
...                                             ...           ...           ...
EDUCATION ADMIN                                0.00  5.000000e+00  5.000000e+00
ENGINEER/RISK EXPERT                           0.00  5.000000e+00  5.000000e+00
SCOTT GREENBAUM                                0.00  5.000000e+00  5.000000e+00
TWC                                            0.00  5.000000e+00  5.000000e+00
LAND PROFESSIONAL                              5.00  0.000000e+00  5.000000e+00
MPRF                                           0.00  5.000000e+00  5.000000e+00
PUBLIX                                         0.00  5.000000e+00  5.000000e+00
BUSINESS COMPLIANCE                            0.00  5.000000e+00  5.000000e+00
AUDILOLOGIST                                   5.00  0.000000e+00  5.000000e+00
TECHNICAL WRITER FOR IT                        0.00  5.000000e+00  5.000000e+00
HOMEMAKER/TEACHER                              5.00  0.000000e+00  5.000000e+00
PUBLIC SCHOOL GUEST TEACHER                    0.00  5.000000e+00  5.000000e+00
ACTOR-WRITER-DIRECTOR                          5.00  0.000000e+00  5.000000e+00
BUSINESS ADVISOR, TEACHER                      5.00  0.000000e+00  5.000000e+00
HEB GROCERY                                    0.00  5.000000e+00  5.000000e+00
ADMINISTRATIVE MANAGEMENT                      0.00  4.120000e+00  4.120000e+00
MEDIA & FINANCIAL SERVICE                      0.00  4.000000e+00  4.000000e+00
REMODELER & SEMI RETIRED                       0.00  3.000000e+00  3.000000e+00
SR MGR                                         3.00  0.000000e+00  3.000000e+00
LEAD UI/UX DEVELOPER                           3.00  0.000000e+00  3.000000e+00
SPRINKLER FITTER FIRE PROTECTION SPECI         3.00  0.000000e+00  3.000000e+00
3RD GENERATION FAMILY BUSINESS OWNER           0.00  3.000000e+00  3.000000e+00
INDEPENDENT PROFESSIONAL                       0.00  3.000000e+00  3.000000e+00
LAN/WAN ANALYST                                3.00  0.000000e+00  3.000000e+00
IFC CONTRACTING SOLUTIONS                      0.00  3.000000e+00  3.000000e+00
POLICY/ LAWYER                                 3.00  0.000000e+00  3.000000e+00
AFFORDABLE REAL ESTATE DEVELOPER               0.00  3.000000e+00  3.000000e+00
ADMINISTRATION/INSTRUCTOR                      3.00  0.000000e+00  3.000000e+00
VICE PRESIDENT, REAL ESTATE                    0.00  1.000000e+00  1.000000e+00
FREELANCE VOICE-OVER                           0.00  1.000000e+00  1.000000e+00

[45061 rows x 3 columns]
'''
# 过滤掉赞助金额小于200w的数据
cond = ret['total'] < 2000000
index = ret[cond].index
ret_big = ret.drop(labels=index)

print(ret_big)
'''
party                 Democrat    Republican         total
contbr_occupation                                         
ATTORNEY           14302461.84  7.868419e+06  2.217088e+07
CEO                 2075974.79  4.233742e+06  6.309716e+06
CONSULTANT          2459912.71  2.544725e+06  5.004638e+06
ENGINEER             951525.55  1.818374e+06  2.769899e+06
EXECUTIVE           1355161.05  4.138850e+06  5.494011e+06
HOMEMAKER           4248875.80  1.363428e+07  1.788315e+07
INVESTOR             884133.00  2.431769e+06  3.315902e+06
MANAGER              762883.22  1.444532e+06  2.207416e+06
NOT PROVIDE        13725187.32  2.097161e+07  3.469680e+07
OWNER               1001567.36  2.408287e+06  3.409854e+06
PHYSICIAN           3735124.94  3.594320e+06  7.329445e+06
PRESIDENT           1878509.95  4.720924e+06  6.599434e+06
PROFESSOR           2165071.08  2.967027e+05  2.461774e+06
REAL ESTATE          528902.09  1.625902e+06  2.154804e+06
RETIRED            25305316.38  2.356099e+07  4.886631e+07
SELF-EMPLOYED        741746.40  2.245273e+06  2.987019e+06
'''

ret_big.plot(kind='bar')
plt.show()





