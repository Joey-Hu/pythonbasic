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

# 查看state属性的缺值数据
cond = pop_abbr['state'].isnull()
a = pop_abbr['state/region'][cond]
print(a)

# 去重
print(a.unique())       # ['PR' 'USA'] 可以看出缺失州名的数据的简写是'PR', 'USA'
print('*************')
# USA -- United States
# PR -- Puerto Rico

cond = pop_abbr['state/region'] == 'PR'
pop_abbr['state'][cond] = 'Puerto Rico'

cond = pop_abbr['state/region'] == 'USA'
pop_abbr['state'][cond] = 'United States'

print(pop_abbr.isnull().any())
'''
state/region    False
ages            False
year            False
population       True
state           False       # 已被填充完毕
dtype: bool
'''

# 查询population属性的缺失数据
cond = pop_abbr['population'].isnull()
print(pop_abbr[cond])
'''
     state/region     ages  year  population        state
2448           PR  under18  1990         NaN  Puerto Rico
2449           PR    total  1990         NaN  Puerto Rico
2450           PR    total  1991         NaN  Puerto Rico
2451           PR  under18  1991         NaN  Puerto Rico
2452           PR    total  1993         NaN  Puerto Rico
2453           PR  under18  1993         NaN  Puerto Rico
2454           PR  under18  1992         NaN  Puerto Rico
2455           PR    total  1992         NaN  Puerto Rico
2456           PR  under18  1994         NaN  Puerto Rico
2457           PR    total  1994         NaN  Puerto Rico
2458           PR    total  1995         NaN  Puerto Rico
2459           PR  under18  1995         NaN  Puerto Rico
2460           PR  under18  1996         NaN  Puerto Rico
2461           PR    total  1996         NaN  Puerto Rico
2462           PR  under18  1998         NaN  Puerto Rico
2463           PR    total  1998         NaN  Puerto Rico
2464           PR    total  1997         NaN  Puerto Rico
2465           PR  under18  1997         NaN  Puerto Rico
2466           PR    total  1999         NaN  Puerto Rico
2467           PR  under18  1999         NaN  Puerto Rico
'''

# 删除PR的空值数据
pop_abbr.dropna(inplace=True)
print(pop_abbr.isnull().any())
'''
state/region    False
ages            False
year            False
population      False   空值数据已被删除
state           False
dtype: bool

'''


# 合并area
print(pop_abbr.head())
print(area.head())  # state属性一一对应

pop_abbr = pd.merge(pop_abbr,area,how='outer')
print(pop_abbr.head(),pop_abbr.shape)

# 寻找空数据
print(pop_abbr.isnull().any())      # 返回area (sq. mi)     True，说明area属性列存在空值
cond = pop_abbr['area (sq. mi)'].isnull()
print(pop_abbr[cond])
'''
     state/region     ages  year   population          state  area (sq. mi)
2476          USA  under18  1990   64218512.0  United States            NaN
2477          USA    total  1990  249622814.0  United States            NaN
2478          USA    total  1991  252980942.0  United States            NaN
2479          USA  under18  1991   65313018.0  United States            NaN
2480          USA  under18  1992   66509177.0  United States            NaN
2481          USA    total  1992  256514231.0  United States            NaN
2482          USA    total  1993  259918595.0  United States            NaN
2483          USA  under18  1993   67594938.0  United States            NaN
2484          USA  under18  1994   68640936.0  United States            NaN
2485          USA    total  1994  263125826.0  United States            NaN
2486          USA  under18  1995   69473140.0  United States            NaN
2487          USA  under18  1996   70233512.0  United States            NaN
2488          USA    total  1995  266278403.0  United States            NaN
2489          USA    total  1996  269394291.0  United States            NaN
2490          USA    total  1997  272646932.0  United States            NaN
2491          USA  under18  1997   70920738.0  United States            NaN
2492          USA  under18  1998   71431406.0  United States            NaN
2493          USA    total  1998  275854116.0  United States            NaN
2494          USA  under18  1999   71946051.0  United States            NaN
2495          USA    total  2000  282162411.0  United States            NaN
2496          USA  under18  2000   72376189.0  United States            NaN
2497          USA    total  1999  279040181.0  United States            NaN
2498          USA    total  2001  284968955.0  United States            NaN
2499          USA  under18  2001   72671175.0  United States            NaN
2500          USA    total  2002  287625193.0  United States            NaN
2501          USA  under18  2002   72936457.0  United States            NaN
2502          USA    total  2003  290107933.0  United States            NaN
2503          USA  under18  2003   73100758.0  United States            NaN
2504          USA    total  2004  292805298.0  United States            NaN
2505          USA  under18  2004   73297735.0  United States            NaN
2506          USA    total  2005  295516599.0  United States            NaN
2507          USA  under18  2005   73523669.0  United States            NaN
2508          USA    total  2006  298379912.0  United States            NaN
2509          USA  under18  2006   73757714.0  United States            NaN
2510          USA    total  2007  301231207.0  United States            NaN
2511          USA  under18  2007   74019405.0  United States            NaN
2512          USA    total  2008  304093966.0  United States            NaN
2513          USA  under18  2008   74104602.0  United States            NaN
2514          USA  under18  2013   73585872.0  United States            NaN
2515          USA    total  2013  316128839.0  United States            NaN
2516          USA    total  2009  306771529.0  United States            NaN
2517          USA  under18  2009   74134167.0  United States            NaN
2518          USA  under18  2010   74119556.0  United States            NaN
2519          USA    total  2010  309326295.0  United States            NaN
2520          USA  under18  2011   73902222.0  United States            NaN
2521          USA    total  2011  311582564.0  United States            NaN
2522          USA  under18  2012   73708179.0  United States            NaN
2523          USA    total  2012  313873685.0  United States            NaN

发现是USA的面积为空值，面积为各州面积和
'''

area_USA = area['area (sq. mi)'].sum()
print(area_USA)

# 填充空值
pop_abbr.fillna(area_USA, inplace=True)

print(pop_abbr[pop_abbr['state/region'] == 'USA'])
'''

     state/region     ages  year   population          state  area (sq. mi)
2476          USA  under18  1990   64218512.0  United States      3790399.0
2477          USA    total  1990  249622814.0  United States      3790399.0
2478          USA    total  1991  252980942.0  United States      3790399.0
2479          USA  under18  1991   65313018.0  United States      3790399.0
2480          USA  under18  1992   66509177.0  United States      3790399.0
2481          USA    total  1992  256514231.0  United States      3790399.0
2482          USA    total  1993  259918595.0  United States      3790399.0
2483          USA  under18  1993   67594938.0  United States      3790399.0
2484          USA  under18  1994   68640936.0  United States      3790399.0
2485          USA    total  1994  263125826.0  United States      3790399.0
2486          USA  under18  1995   69473140.0  United States      3790399.0
2487          USA  under18  1996   70233512.0  United States      3790399.0
2488          USA    total  1995  266278403.0  United States      3790399.0
2489          USA    total  1996  269394291.0  United States      3790399.0
2490          USA    total  1997  272646932.0  United States      3790399.0
2491          USA  under18  1997   70920738.0  United States      3790399.0
2492          USA  under18  1998   71431406.0  United States      3790399.0
2493          USA    total  1998  275854116.0  United States      3790399.0
2494          USA  under18  1999   71946051.0  United States      3790399.0
2495          USA    total  2000  282162411.0  United States      3790399.0
2496          USA  under18  2000   72376189.0  United States      3790399.0
2497          USA    total  1999  279040181.0  United States      3790399.0
2498          USA    total  2001  284968955.0  United States      3790399.0
2499          USA  under18  2001   72671175.0  United States      3790399.0
2500          USA    total  2002  287625193.0  United States      3790399.0
2501          USA  under18  2002   72936457.0  United States      3790399.0
2502          USA    total  2003  290107933.0  United States      3790399.0
2503          USA  under18  2003   73100758.0  United States      3790399.0
2504          USA    total  2004  292805298.0  United States      3790399.0
2505          USA  under18  2004   73297735.0  United States      3790399.0
2506          USA    total  2005  295516599.0  United States      3790399.0
2507          USA  under18  2005   73523669.0  United States      3790399.0
2508          USA    total  2006  298379912.0  United States      3790399.0
2509          USA  under18  2006   73757714.0  United States      3790399.0
2510          USA    total  2007  301231207.0  United States      3790399.0
2511          USA  under18  2007   74019405.0  United States      3790399.0
2512          USA    total  2008  304093966.0  United States      3790399.0
2513          USA  under18  2008   74104602.0  United States      3790399.0
2514          USA  under18  2013   73585872.0  United States      3790399.0
2515          USA    total  2013  316128839.0  United States      3790399.0
2516          USA    total  2009  306771529.0  United States      3790399.0
2517          USA  under18  2009   74134167.0  United States      3790399.0
2518          USA  under18  2010   74119556.0  United States      3790399.0
2519          USA    total  2010  309326295.0  United States      3790399.0
2520          USA  under18  2011   73902222.0  United States      3790399.0
2521          USA    total  2011  311582564.0  United States      3790399.0
2522          USA  under18  2012   73708179.0  United States      3790399.0
2523          USA    total  2012  313873685.0  United States      3790399.0
'''

# 查询语句  df.query()
# 2010年的全民（total）人口数据

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',1000)


pop_2010 = pop_abbr.query("year == 2010 and ages == 'total'")
print('************')
# 对查询结果处理，以state为列作为新的行索引
pop_2010.set_index('state/region',inplace = True)
print(pop_2010)

# 计算人口密度
pop_2010_density = pop_2010['population']/pop_2010['area (sq. mi)']
print(pop_2010_density)

# 将人口密度转为DataFrame格式
print(type(pop_2010_density))   # <class 'pandas.core.series.Series'>
pop_2010_density1 = DataFrame(pop_2010_density, columns=['pop_density (/sq. mi)'])
pop_2010_density1 = pop_2010_density1['pop_density (/sq. mi)'].round(2)
print('************')
print(pop_2010_density1)
'''
state/region
AL       91.29
AK        1.09
AZ       56.21
AR       54.95
CA      228.05
CO       48.49
CT      645.60
DE      460.45
DC     8898.90
FL      286.60
GA      163.41
HI      124.75
ID       18.79
IL      221.69
IN      178.20
IA       54.20
KS       34.75
KY      107.59
LA       87.68
ME       37.51
MD      466.45
MA      621.82
MI      102.02
MN       61.08
MS       61.32
MO       86.02
MT        6.74
NE       23.65
NV       24.45
NH      140.80
NJ     1009.25
NM       16.98
NY      356.09
NC      177.62
ND        9.54
OH      257.55
OK       53.78
OR       39.00
PA      275.97
RI      681.34
SC      144.85
SD       10.58
TN      150.83
TX       93.99
UT       32.68
VT       65.09
VA      187.62
WA       94.56
WV       76.52
WI       86.85
WY        5.77
PR     1058.67
USA      81.61
Name: pop_density (/sq. mi), dtype: float64
'''

# 合并
pop_abbr_area_density2010 = pd.merge(pop_2010, pop_2010_density1, left_index=True, right_index = True)
print(pop_abbr_area_density2010)

# 排序，找出人口密度最高的五个州
print(pop_abbr_area_density2010.sort_values(by = 'pop_density (/sq. mi)', ascending=False).head())
'''
              pop_density (/sq. mi)  
state/region                         
DC                          8898.90  
PR                          1058.67  
NJ                          1009.25  
RI                           681.34  
CT                           645.60 
'''

# 写出数据
pop_abbr_area_density2010.to_csv('./pop_abbr_area_density2010.csv')
pop_abbr_area_density2010.to_excel('./pop_abbr_area_density2010.xlsx')