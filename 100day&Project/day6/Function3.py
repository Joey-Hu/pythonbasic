#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: Function3.py
#@time: 2019/6/6 8:34
#@Ducument：https://www.python.org/doc/
#@desc:

# 函数的覆盖
def foo():
    print("hello, world!")

def foo():
    print("你好，世界！")

foo()