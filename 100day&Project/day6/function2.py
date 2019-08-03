#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: function2.py
# @time: 2019/6/6 8:18
# @Ducument：https://www.python.org/doc/
# @desc:

# 当不确定函数参数个数时
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for value in args:
        total += value
    return total


print(add())  # result=0
print(add(1))   # result=1
print(add(1,2,3))   # result=6
print(add(1,3,5,7,9))   # result=25

