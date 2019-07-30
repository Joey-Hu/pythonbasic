#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: mySQL.py
# @time: 2019/7/3 15:29
# @Ducument：https://www.python.org/doc/
# @desc:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import pymysql

# 连接mySQL本地数据库
# pymysql.connection(host, port, user, password, database, charset)
con = pymysql.Connection(host = '127.0.0.1', port = 3306, user = 'root', password = 'hh123456', database = 'employees', charset = 'utf8')

# 定义查询语句
sql = 'select * from departments'

# python 读取sql文件
df = pd.read_sql(sql, con)
print(df)
'''
  dept_no           dept_name
0    d009    Customer Service
1    d005         Development
2    d002             Finance
3    d003     Human Resources
4    d001           Marketing
5    d004          Production
6    d006  Quality Management
7    d008            Research
8    d007               Sales
'''

# 操作mySQL数据库    目前省略

# 保存
# df.to_sql()









