#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: variable.py
#@time: 2019/5/9 15:30
#@Ducument：https://www.python.org/doc/
#@desc: 检查变量类型

a = 10
b = 10.0000
c = 1000000000000000000000000000
d = 1 + 5j
# e = "A"
e = 'A'     # 不管是单引号还是双引号都是string类型
f = "hello, world!"
g = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# 类型转换
h = int(b)
print(type(h))
