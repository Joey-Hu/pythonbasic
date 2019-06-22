#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: circle.py
#@time: 2019/5/5 12:03
#@Ducument：https://www.python.org/doc/
#@desc: 输入半径，求圆的周长和面积

import math

radius = float(input("输入圆的半径："))

perimeter = 2 * math.pi * radius
area  = math.pi * radius * radius

print("周长：%.2f" % perimeter)
print("面积：%.2f" % area)