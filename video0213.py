#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video0213.py
#@time: 2019/2/13 22:37
#@Ducument：https://www.python.org/doc/
#@desc:


# 元组 类似列表；外形上一个圆括号，一个方括号

# 创建元组
# tuple = (123,"abc",True,4.56,["inner","list"],("inner","tuple"),)
# print(tuple)


# 元组元素访问    方括号作为切片操作符
# print(tuple[1:4])
# print(tuple[4][0])

# 修改元组
# tuple[0] = 456    元组元素一旦初始化就不可变
# tuple[4][0] = 123   不会报错，因为改动是元组里的列表元素
# print(tuple)


# 删除元组    del tuple

# 判断元素是否在元组里
# print(123 in tuple)


# 元组的方法
# len()   返回元组里元素的个数
# max()   返回元组的元素最大值
# min()   返回元组的元素最小值
# 将列表转换为元组
# list = [1,2,3]
# tuple1 = tuple(list)
# print(tuple1)


tuple = (123,"abc",True,4.56,["inner","list"],("inner","tuple"),)
# list1 = list[tuple]
# print(list1)


# 元组的遍历
# for i in range(len(tuple)):
#     print(tuple[i])



















