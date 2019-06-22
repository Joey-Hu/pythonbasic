#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: lili.py
# @time: 2019/5/9 16:48
# @Ducument：https://www.python.org/doc/
# @desc: 水仙花数

for num in range(100, 1000):
    a = num % 10
    b = (num // 10) % 10        # 取整除
    c = num // 100
    if num == a * a * a + b * b * b + c * c * c:
        print("%d是水仙花数" %(num))
