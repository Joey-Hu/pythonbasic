#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: leap.py
#@time: 2019/5/5 12:09
#@Ducument：https://www.python.org/doc/
#@desc: 判断是否是闰年

year = int(input("输入年份："))

# is_leap = (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)

# 注意python里的且和或用and 和 or
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)
