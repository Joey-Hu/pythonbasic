# @author: huhao
# @file: USDA_foodDB.py
# @time: 2019/7/11 8:38
# @Document：https://www.python.org/doc/
# @desc:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

import re
import json


#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
# pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
# 设置显示宽度，不让他换行
pd.set_option('display.width', 1000)

db = json.load(open('foods-2011-10-03.json'))
# print(db[:1])
# print(len(db))      # 6636
# print(type(db))     # <class 'list'>
# print(type(db[0]))      # <class 'dict'>
# print(db[0].keys())     # dict_keys(['tags', 'nutrients', 'portions', 'id', 'manufacturer', 'group', 'description'])
# print(db[0]['nutrients'][0])        # {'group': 'Composition', 'description': 'Protein', 'value': 25.18, 'units': 'g'}
# print(len(db[0]['nutrients']))        # 162

# nutrients

info_keys = ['description', 'group', 'id', 'manufacturer', 'tags']
info = DataFrame(db, columns=info_keys)
print(info.head())
'''
                         description                   group    id manufacturer tags
0                     Cheese, caraway  Dairy and Egg Products  1008                []
1                     Cheese, cheddar  Dairy and Egg Products  1009                []
2                        Cheese, edam  Dairy and Egg Products  1018                []
3                        Cheese, feta  Dairy and Egg Products  1019                []
4  Cheese, mozzarella, part skim milk  Dairy and Egg Products  1028                []
'''

# 删除tags列
info.drop(labels='tags', axis=1, inplace=True)
print(info.head())
'''
                        description                   group    id manufacturer
0                     Cheese, caraway  Dairy and Egg Products  1008             
1                     Cheese, cheddar  Dairy and Egg Products  1009             
2                        Cheese, edam  Dairy and Egg Products  1018             
3                        Cheese, feta  Dairy and Egg Products  1019             
4  Cheese, mozzarella, part skim milk  Dairy and Egg Products  1028  
'''

print(pd.value_counts(info.group))
# print(pd.value_counts(nutrients.group))
'''
Vegetables and Vegetable Products    812
Beef Products                        618
Baked Products                       496
Breakfast Cereals                    403
Fast Foods                           365
Legumes and Legume Products          365
Lamb, Veal, and Game Products        345
Sweets                               341
Pork Products                        328
Fruits and Fruit Juices              328
Beverages                            278
Soups, Sauces, and Gravies           275
Finfish and Shellfish Products       255
Baby Foods                           209
Cereal Grains and Pasta              183
Ethnic Foods                         165
Snacks                               162
Nut and Seed Products                128
Poultry Products                     116
Sausages and Luncheon Meats          111
Dairy and Egg Products               107
Fats and Oils                         97
Meals, Entrees, and Sidedishes        57
Restaurant Foods                      51
Spices and Herbs                      41
Name: group, dtype: int64
'''

Nutrients = []

#取特定key为nutrients id 生成一个list
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    Nutrients.append(fnuts)

# print(Nutrients[:1])
'''
[                            description        group    units     value    id
0                               Protein  Composition        g    25.180  1008
1                     Total lipid (fat)  Composition        g    29.200  1008
2           Carbohydrate, by difference  Composition        g     3.060  1008
3                                   Ash        Other        g     3.280  1008
4                                Energy       Energy     kcal   376.000  1008
5                                 Water  Composition        g    39.280  1008
6                                Energy       Energy       kJ  1573.000  1008
7                  Fiber, total dietary  Composition        g     0.000  1008
8                           Calcium, Ca     Elements       mg   673.000  1008
9                              Iron, Fe     Elements       mg     0.640  1008
10                        Magnesium, Mg     Elements       mg    22.000  1008
11                        Phosphorus, P     Elements       mg   490.000  1008
12                         Potassium, K     Elements       mg    93.000  1008
13                           Sodium, Na     Elements       mg   690.000  1008
14                             Zinc, Zn     Elements       mg     2.940  1008
15                           Copper, Cu     Elements       mg     0.024  1008
16                        Manganese, Mn     Elements       mg     0.021  1008
17                         Selenium, Se     Elements      mcg    14.500  1008
18                        Vitamin A, IU     Vitamins       IU  1054.000  1008
19                              Retinol     Vitamins      mcg   262.000  1008
20                       Vitamin A, RAE     Vitamins  mcg_RAE   271.000  1008
21       Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1008
22                              Thiamin     Vitamins       mg     0.031  1008
23                           Riboflavin     Vitamins       mg     0.450  1008
24                               Niacin     Vitamins       mg     0.180  1008
25                     Pantothenic acid     Vitamins       mg     0.190  1008
26                          Vitamin B-6     Vitamins       mg     0.074  1008
27                        Folate, total     Vitamins      mcg    18.000  1008
28                         Vitamin B-12     Vitamins      mcg     0.270  1008
29                           Folic acid     Vitamins      mcg     0.000  1008
..                                  ...          ...      ...       ...   ...
132                              Niacin     Vitamins       mg     0.180  1008
133                    Pantothenic acid     Vitamins       mg     0.190  1008
134                         Vitamin B-6     Vitamins       mg     0.074  1008
135                       Folate, total     Vitamins      mcg    18.000  1008
136                        Vitamin B-12     Vitamins      mcg     0.270  1008
137                          Folic acid     Vitamins      mcg     0.000  1008
138                        Folate, food     Vitamins      mcg    18.000  1008
139                         Folate, DFE     Vitamins  mcg_DFE    18.000  1008
140                          Tryptophan  Amino Acids        g     0.324  1008
141                           Threonine  Amino Acids        g     0.896  1008
142                          Isoleucine  Amino Acids        g     1.563  1008
143                             Leucine  Amino Acids        g     2.412  1008
144                              Lysine  Amino Acids        g     2.095  1008
145                          Methionine  Amino Acids        g     0.659  1008
146                             Cystine  Amino Acids        g     0.126  1008
147                       Phenylalanine  Amino Acids        g     1.326  1008
148                            Tyrosine  Amino Acids        g     1.216  1008
149                              Valine  Amino Acids        g     1.682  1008
150                            Arginine  Amino Acids        g     0.952  1008
151                           Histidine  Amino Acids        g     0.884  1008
152                             Alanine  Amino Acids        g     0.711  1008
153                       Aspartic acid  Amino Acids        g     1.618  1008
154                       Glutamic acid  Amino Acids        g     6.160  1008
155                             Glycine  Amino Acids        g     0.439  1008
156                             Proline  Amino Acids        g     2.838  1008
157                              Serine  Amino Acids        g     1.472  1008
158                         Cholesterol        Other       mg    93.000  1008
159        Fatty acids, total saturated        Other        g    18.584  1008
160  Fatty acids, total monounsaturated        Other        g     8.275  1008
161  Fatty acids, total polyunsaturated        Other        g     0.830  1008

[162 rows x 5 columns]]
'''

Nutrients = pd.concat(Nutrients, ignore_index=True)     #将list中的成员整合到一个DataFrame
# print(Nutrients.head(163))
'''
                            description        group    units     value    id
0                               Protein  Composition        g    25.180  1008
1                     Total lipid (fat)  Composition        g    29.200  1008
2           Carbohydrate, by difference  Composition        g     3.060  1008
3                                   Ash        Other        g     3.280  1008
4                                Energy       Energy     kcal   376.000  1008
5                                 Water  Composition        g    39.280  1008
6                                Energy       Energy       kJ  1573.000  1008
7                  Fiber, total dietary  Composition        g     0.000  1008
8                           Calcium, Ca     Elements       mg   673.000  1008
9                              Iron, Fe     Elements       mg     0.640  1008
10                        Magnesium, Mg     Elements       mg    22.000  1008
11                        Phosphorus, P     Elements       mg   490.000  1008
12                         Potassium, K     Elements       mg    93.000  1008
13                           Sodium, Na     Elements       mg   690.000  1008
14                             Zinc, Zn     Elements       mg     2.940  1008
15                           Copper, Cu     Elements       mg     0.024  1008
16                        Manganese, Mn     Elements       mg     0.021  1008
17                         Selenium, Se     Elements      mcg    14.500  1008
18                        Vitamin A, IU     Vitamins       IU  1054.000  1008
19                              Retinol     Vitamins      mcg   262.000  1008
20                       Vitamin A, RAE     Vitamins  mcg_RAE   271.000  1008
21       Vitamin C, total ascorbic acid     Vitamins       mg     0.000  1008
22                              Thiamin     Vitamins       mg     0.031  1008
23                           Riboflavin     Vitamins       mg     0.450  1008
24                               Niacin     Vitamins       mg     0.180  1008
25                     Pantothenic acid     Vitamins       mg     0.190  1008
26                          Vitamin B-6     Vitamins       mg     0.074  1008
27                        Folate, total     Vitamins      mcg    18.000  1008
28                         Vitamin B-12     Vitamins      mcg     0.270  1008
29                           Folic acid     Vitamins      mcg     0.000  1008
..                                  ...          ...      ...       ...   ...
133                    Pantothenic acid     Vitamins       mg     0.190  1008
134                         Vitamin B-6     Vitamins       mg     0.074  1008
135                       Folate, total     Vitamins      mcg    18.000  1008
136                        Vitamin B-12     Vitamins      mcg     0.270  1008
137                          Folic acid     Vitamins      mcg     0.000  1008
138                        Folate, food     Vitamins      mcg    18.000  1008
139                         Folate, DFE     Vitamins  mcg_DFE    18.000  1008
140                          Tryptophan  Amino Acids        g     0.324  1008
141                           Threonine  Amino Acids        g     0.896  1008
142                          Isoleucine  Amino Acids        g     1.563  1008
143                             Leucine  Amino Acids        g     2.412  1008
144                              Lysine  Amino Acids        g     2.095  1008
145                          Methionine  Amino Acids        g     0.659  1008
146                             Cystine  Amino Acids        g     0.126  1008
147                       Phenylalanine  Amino Acids        g     1.326  1008
148                            Tyrosine  Amino Acids        g     1.216  1008
149                              Valine  Amino Acids        g     1.682  1008
150                            Arginine  Amino Acids        g     0.952  1008
151                           Histidine  Amino Acids        g     0.884  1008
152                             Alanine  Amino Acids        g     0.711  1008
153                       Aspartic acid  Amino Acids        g     1.618  1008
154                       Glutamic acid  Amino Acids        g     6.160  1008
155                             Glycine  Amino Acids        g     0.439  1008
156                             Proline  Amino Acids        g     2.838  1008
157                              Serine  Amino Acids        g     1.472  1008
158                         Cholesterol        Other       mg    93.000  1008
159        Fatty acids, total saturated        Other        g    18.584  1008
160  Fatty acids, total monounsaturated        Other        g     8.275  1008
161  Fatty acids, total polyunsaturated        Other        g     0.830  1008
162                             Protein  Composition        g    24.900  1009

[163 rows x 5 columns]
'''
# print(len(Nutrients))       # 389355

# print(Nutrients.duplicated().sum())   #统计重复项，默认是根据第一列nutrients 统计   14179
# print(Nutrients.duplicated('group').sum())   #统计重复项，根据group列统计   389348

Nutrients_with_no_duplicates = Nutrients.drop_duplicates()      # 丢弃重复项
# print(len(Nutrients_with_no_duplicates))        # 375176

# 两个DataFrame 都有"group"、"description"列名重命名
col_maping = {'description':'food', 'group':'fgroup'}
info = info.rename(columns=col_maping, copy=False)
col_maping = {'description':'nutrients', 'group':'nutgroup'}
Nutrients = Nutrients.rename(columns=col_maping, copy=False)

#合并2个DataFrame 根据id关联 outer外连接
ndata = pd.merge(Nutrients,info,how='outer',on='id')
print(ndata['fgroup'].unique())
'''
['Dairy and Egg Products' 'Spices and Herbs' 'Baby Foods' 'Fats and Oils'
 'Poultry Products' 'Soups, Sauces, and Gravies'
 'Sausages and Luncheon Meats' 'Breakfast Cereals'
 'Fruits and Fruit Juices' 'Pork Products'
 'Vegetables and Vegetable Products' 'Nut and Seed Products'
 'Beef Products' 'Beverages' 'Finfish and Shellfish Products'
 'Legumes and Legume Products' 'Lamb, Veal, and Game Products'
 'Baked Products' 'Snacks' 'Sweets' 'Cereal Grains and Pasta' 'Fast Foods'
 'Meals, Entrees, and Sidedishes' 'Ethnic Foods' 'Restaurant Foods']
'''
print(ndata.head())

'''
                     nutrients     nutgroup units   value    id             food                  fgroup manufacturer
0                      Protein  Composition     g   25.18  1008  Cheese, caraway  Dairy and Egg Products             
1            Total lipid (fat)  Composition     g   29.20  1008  Cheese, caraway  Dairy and Egg Products             
2  Carbohydrate, by difference  Composition     g    3.06  1008  Cheese, caraway  Dairy and Egg Products             
3                          Ash        Other     g    3.28  1008  Cheese, caraway  Dairy and Egg Products             
4                       Energy       Energy  kcal  376.00  1008  Cheese, caraway  Dairy and Egg Products  
'''

#根据营养分类得到锌的中位值
result = ndata.groupby(['nutrients','fgroup'])['value'].quantile(0.5)
print(result['Zinc, Zn'])
'''
fgroup
Baby Foods                           0.590
Baked Products                       0.660
Beef Products                        5.390
Beverages                            0.040
Breakfast Cereals                    2.885
Cereal Grains and Pasta              1.090
Dairy and Egg Products               1.330
Ethnic Foods                         1.045
Fast Foods                           1.250
Fats and Oils                        0.020
Finfish and Shellfish Products       0.670
Fruits and Fruit Juices              0.100
Lamb, Veal, and Game Products        3.940
Legumes and Legume Products          1.140
Meals, Entrees, and Sidedishes       0.630
Nut and Seed Products                3.290
Pork Products                        2.320
Poultry Products                     2.500
Restaurant Foods                     0.800
Sausages and Luncheon Meats          2.130
Snacks                               1.470
Soups, Sauces, and Gravies           0.200
Spices and Herbs                     2.750
Sweets                               0.360
Vegetables and Vegetable Products    0.330
Name: value, dtype: float64
'''
result['Zinc, Zn'].sort_values().plot(kind='barh')
plt.show()


#营养成分最为丰富的食物
by_nutrients = ndata.groupby(['nutgroup','nutrients'])
get_max = lambda x: x.xs(x.value.idxmax())
get_min = lambda x: x.xs(x.value.idxmin())
max_food = by_nutrients.apply(get_max)[['value', 'food']]

print(max_food.food.str[:10])
'''
Amino Acids  Alanine                           Gelatins, 
             Arginine                          Seeds, ses
             Aspartic acid                     Soy protei
             Cystine                           Seeds, cot
             Glutamic acid                     Soy protei
             Glycine                           Gelatins, 
             Histidine                         Whale, bel
             Hydroxyproline                    KENTUCKY F
             Isoleucine                        Soy protei
             Leucine                           Soy protei
             Lysine                            Seal, bear
             Methionine                        Fish, cod,
             Phenylalanine                     Soy protei
             Proline                           Gelatins, 
             Serine                            Soy protei
             Threonine                         Soy protei
             Tryptophan                        Sea lion, 
             Tyrosine                          Soy protei
             Valine                            Soy protei
Composition  Adjusted Protein                  Baking cho
             Carbohydrate, by difference       Sweeteners
             Fiber, total dietary              Corn bran,
             Protein                           Soy protei
             Sugars, total                     Sugars, gr
             Total lipid (fat)                 Oil, wheat
             Water                             Water, bot
Elements     Calcium, Ca                       Leavening 
             Copper, Cu                        Veal, vari
             Fluoride, F                       Tea, insta
             Iron, Fe                          Salad dres
                                                  ...    
Vitamins     Cryptoxanthin, beta               Spices, pa
             Dihydrophylloquinone              Margarine,
             Folate, DFE                       Cereals re
             Folate, food                      Leavening 
             Folate, total                     Leavening 
             Folic acid                        Cereals re
             Lutein + zeaxanthin                Kale, raw
             Lycopene                          Tomato pow
             Menaquinone-4                     Chicken, b
             Niacin                            Yeast extr
             Pantothenic acid                  Cereals re
             Retinol                           Fish oil, 
             Riboflavin                        Yeast extr
             Thiamin                           MORNINGSTA
             Tocopherol, beta                  Yellow pon
             Tocopherol, delta                 Oil, cooki
             Tocopherol, gamma                 Oil, cooki
             Vitamin A, IU                     Fish oil, 
             Vitamin A, RAE                    Fish oil, 
             Vitamin B-12                      Mollusks, 
             Vitamin B-12, added               Cereals re
             Vitamin B-6                       Cereals re
             Vitamin C, total ascorbic acid    Orange-fla
             Vitamin D                         Fish oil, 
             Vitamin D (D2 + D3)               Fish oil, 
             Vitamin D2 (ergocalciferol)       Mushrooms,
             Vitamin D3 (cholecalciferol)      Fish, hali
             Vitamin E (alpha-tocopherol)      Oil, wheat
             Vitamin E, added                  Cereals re
             Vitamin K (phylloquinone)         Spices, sa
Name: food, Length: 94, dtype: object
'''



