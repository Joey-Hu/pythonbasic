#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: gcd_lcm.py
# @time: 2019/6/6 14:49
# @Ducument：https://www.python.org/doc/
# @desc:

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
    # for factor in range(1, x, 1):     ******错误示范******
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
