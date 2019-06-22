#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: chicken.py
# @time: 2019/5/9 16:55
# @Ducument：https://www.python.org/doc/
# @desc:
'''

"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

穷取法
'''

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if x * 5 + y * 3 + z // 3 == 100:
            print("x = %d, y = %d, z = %d" %(x, y, z))
