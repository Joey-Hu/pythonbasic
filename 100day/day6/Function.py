#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: Function.py
# @time: 2019/6/6 7:32
# @Ducument：https://www.python.org/doc/
# @desc:

# 函数的参数

from random import randint


def Roll_dice(n=2):  # 默认值 n=2
    """

    :param n: 色子个数
    :return: n颗色子总点数
    """

    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


# print(Roll_dice())  # 不定义参数，取默认值
# print(Roll_dice(3))  # 调取函数时传入参数，则使用该参数
# print(add())  # 不定义参数，取默认值
# print(add(1))  # 结果=1
# print(add(1,2)) # 结果=3

# 传递参数时可以不按照设定的顺序进行传递
print(add(b=10, a=20, c=30))
