#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: is_prime.py
#@time: 2019/5/9 16:43
#@Ducument：https://www.python.org/doc/
#@desc:

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)