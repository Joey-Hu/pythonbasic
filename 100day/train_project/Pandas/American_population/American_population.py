#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: American_population.py
# @time: 2019/6/29 14:38
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 读取csv文件
area = pd.read_csv('./state-areas.csv')
'''
                   state  area (sq. mi)
0                Alabama          52423
1                 Alaska         656425
2                Arizona         114006
3               Arkansas          53182
4             California         163707
5               Colorado         104100
6            Connecticut           5544
7               Delaware           1954
8                Florida          65758
9                Georgia          59441
10                Hawaii          10932
11                 Idaho          83574
12              Illinois          57918
13               Indiana          36420
14                  Iowa          56276
15                Kansas          82282
16              Kentucky          40411
17             Louisiana          51843
18                 Maine          35387
19              Maryland          12407
20         Massachusetts          10555
21              Michigan          96810
22             Minnesota          86943
23           Mississippi          48434
24              Missouri          69709
25               Montana         147046
26              Nebraska          77358
27                Nevada         110567
28         New Hampshire           9351
29            New Jersey           8722
30            New Mexico         121593
31              New York          54475
32        North Carolina          53821
33          North Dakota          70704
34                  Ohio          44828
35              Oklahoma          69903
36                Oregon          98386
37          Pennsylvania          46058
38          Rhode Island           1545
39        South Carolina          32007
40          South Dakota          77121
41             Tennessee          42146
42                 Texas         268601
43                  Utah          84904
44               Vermont           9615
45              Virginia          42769
46            Washington          71303
47         West Virginia          24231
48             Wisconsin          65503
49               Wyoming          97818
50  District of Columbia             68
51           Puerto Rico           3515

'''
abbr = pd.read_csv('./state-abbrevs.csv')
'''
                   state abbreviation
0                Alabama           AL
1                 Alaska           AK
2                Arizona           AZ
3               Arkansas           AR
4             California           CA
5               Colorado           CO
6            Connecticut           CT
7               Delaware           DE
8   District of Columbia           DC
9                Florida           FL
10               Georgia           GA
11                Hawaii           HI
12                 Idaho           ID
13              Illinois           IL
14               Indiana           IN
15                  Iowa           IA
16                Kansas           KS
17              Kentucky           KY
18             Louisiana           LA
19                 Maine           ME
20               Montana           MT
21              Nebraska           NE
22                Nevada           NV
23         New Hampshire           NH
24            New Jersey           NJ
25            New Mexico           NM
26              New York           NY
27        North Carolina           NC
28          North Dakota           ND
29                  Ohio           OH
30              Oklahoma           OK
31                Oregon           OR
32              Maryland           MD
33         Massachusetts           MA
34              Michigan           MI
35             Minnesota           MN
36           Mississippi           MS
37              Missouri           MO
38          Pennsylvania           PA
39          Rhode Island           RI
40        South Carolina           SC
41          South Dakota           SD
42             Tennessee           TN
43                 Texas           TX
44                  Utah           UT
45               Vermont           VT
46              Virginia           VA
47            Washington           WA
48         West Virginia           WV
49             Wisconsin           WI
50               Wyoming           WY

'''
pop = pd.read_csv('./state-population.csv')
'''
     state/region     ages  year   population
0              AL  under18  2012    1117489.0
1              AL    total  2012    4817528.0
2              AL  under18  2010    1130966.0
3              AL    total  2010    4785570.0
4              AL  under18  2011    1125763.0
5              AL    total  2011    4801627.0
6              AL    total  2009    4757938.0
7              AL  under18  2009    1134192.0
8              AL  under18  2013    1111481.0
9              AL    total  2013    4833722.0
10             AL    total  2007    4672840.0
11             AL  under18  2007    1132296.0
12             AL    total  2008    4718206.0
13             AL  under18  2008    1134927.0
14             AL    total  2005    4569805.0
15             AL  under18  2005    1117229.0
16             AL    total  2006    4628981.0
17             AL  under18  2006    1126798.0
18             AL    total  2004    4530729.0
19             AL  under18  2004    1113662.0
20             AL    total  2003    4503491.0
21             AL  under18  2003    1113083.0
22             AL    total  2001    4467634.0
23             AL  under18  2001    1120409.0
24             AL    total  2002    4480089.0
25             AL  under18  2002    1116590.0
26             AL  under18  1999    1121287.0
27             AL    total  1999    4430141.0
28             AL    total  2000    4452173.0
29             AL  under18  2000    1122273.0
...           ...      ...   ...          ...
2514          USA  under18  1999   71946051.0
2515          USA    total  2000  282162411.0
2516          USA  under18  2000   72376189.0
2517          USA    total  1999  279040181.0
2518          USA    total  2001  284968955.0
2519          USA  under18  2001   72671175.0
2520          USA    total  2002  287625193.0
2521          USA  under18  2002   72936457.0
2522          USA    total  2003  290107933.0
2523          USA  under18  2003   73100758.0
2524          USA    total  2004  292805298.0
2525          USA  under18  2004   73297735.0
2526          USA    total  2005  295516599.0
2527          USA  under18  2005   73523669.0
2528          USA    total  2006  298379912.0
2529          USA  under18  2006   73757714.0
2530          USA    total  2007  301231207.0
2531          USA  under18  2007   74019405.0
2532          USA    total  2008  304093966.0
2533          USA  under18  2008   74104602.0
2534          USA  under18  2013   73585872.0
2535          USA    total  2013  316128839.0
2536          USA    total  2009  306771529.0
2537          USA  under18  2009   74134167.0
2538          USA  under18  2010   74119556.0
2539          USA    total  2010  309326295.0
2540          USA  under18  2011   73902222.0
2541          USA    total  2011  311582564.0
2542          USA  under18  2012   73708179.0
2543          USA    total  2012  313873685.0
'''

# 简单看一下数据
print(pop.head())       # tail
'''
  state/region     ages  year  population
0           AL  under18  2012   1117489.0
1           AL    total  2012   4817528.0
2           AL  under18  2010   1130966.0
3           AL    total  2010   4785570.0
4           AL  under18  2011   1125763.0
'''

print(type(pop))    # <class 'pandas.core.frame.DataFrame'>

# 合并pop与abbrevs两个DataFrame，分别依据state/region和abbreviation列来合并，
# pop_abbr = pd.merge(pop, abbr, left_on='state/region',right_on='abbreviation',how='inner')
# print(pop_abbr.shape)       # (2448, 6)数据丢失

# 为保留所有信息，使用外合并，但数据存在空值
pop_abbr = pd.merge(pop, abbr, left_on='state/region',right_on='abbreviation',how='outer')
print(pop_abbr.shape)   # (2544, 6)

# 查看并填补空值
print(pop_abbr.info())
'''
Int64Index: 2544 entries, 0 to 2543
Data columns (total 6 columns):
state/region    2544 non-null object
ages            2544 non-null object
year            2544 non-null int64
population      2524 non-null float64
state           2448 non-null object
abbreviation    2448 non-null object
dtypes: float64(1), int64(1), object(4)
memory usage: 99.4+ KB
None

可以看出，population, state列和abbreviation存在空值
'''
pop_abbr.drop(labels='abbreviation', axis=1, inplace=True)  # inplace属性，直接在原表的基础上删除列
print(pop_abbr.head())
'''
  state/region     ages  year  population    state
0           AL  under18  2012   1117489.0  Alabama
1           AL    total  2012   4817528.0  Alabama
2           AL  under18  2010   1130966.0  Alabama
3           AL    total  2010   4785570.0  Alabama
4           AL  under18  2011   1125763.0  Alabama
'''

#查看存在缺失数据的列
# 存在空值的列返回True
print(pop_abbr.isnull().any())
'''
state/region    False
ages            False
year            False
population       True
state            True
dtype: bool

'''

# 查看空值数据