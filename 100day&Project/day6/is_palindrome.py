#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: is_palindrome.py
#@time: 2019/6/6 15:10
#@Ducument：https://www.python.org/doc/
#@desc:

def is_palindrome(num):
    temp = num
    converse = 0
    while temp > 0:
        converse = converse * 10 + temp % 10
        temp = temp // 10
    return converse == num


is_palindrome(12321)