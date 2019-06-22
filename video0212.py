#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video0212.py
#@time: 2019/2/12 13:29
#@Ducument：https://www.python.org/doc/
#@desc:

# 列表
# 格式: 列表名[列表项1，列表项2，列表项3，...列表项n]

# 创建空列表
# list1 = []
# print(list1)

# 创建带有元素的列表
list2 = [1, 2, "huhao ", [1,"h"], True]     #列表中的元素可以是不同类型的
# print(list2)
list3 = [18,19,21,28,26]



# 列表元素访问
# print(list2[2])

# 列表元素替换
# list2[1] = "good"
# print(list2)



# 求list3中元素的平均值
# avg = 0
# index = 0
# while index < 5:
#     avg = avg + list3[index]
#     index = index + 1
#
# print("average= ",avg/5)





# 列表切片
# print(list3[1:4])

# 二维列表
list4 = [[1,2,3],[4,5,6],[7,8,9]]
# print(list4)
# print(list4[1])
# print(list4[1][1])


# 列表追加
# append 在列表的末尾追加一个元素
# list5 = [1,2,3,4]
# list5.append(5)
# list5.append([6,7,8])
# print(list5)


# extend 在末尾一次性追加另一个列表的多个元素
# list = [1,2,3,4]
# list.extend([6,7,8])
# print(list)



# list.insert(index,object) 在下标处插入对象(元素，列表)，不覆盖原数据，原数据向后顺延
# list.pop(index)  删除下标为index的元素，index默认为-1，并返回删除时数据
# list.remove(object)  删除列表中的某个元素第一个匹配的结果
# list.clear()  清除列表中的所有元素
# list.index(object,start,stop)  从列表中找出某值的第一个匹配元素的下标
# len(list)  返回list的元素个数
# max(list)  获取列表中的最大值
# min(list)  获取列表中的最小值
# list.count(object)  获取元素在列表中出现的次数     ##删除重复出现的元素，先获取出现的次数，再重复执行list.remove(object)
# list.reverse()  倒序输出
# list.sort()  升序排序



# 找出第二大的值

# list = []
#
# num = 0
#
# while num < 10:
#     val = int(input())
#     list.append(val)
#     num += 1
#
# print(list)
#
# max = max(list)
# all = list.count(max)
#
# num = 0
# while num < all:
#     list.remove(max)
#     num += 1
#
# list.sort()
# print(list[-1])


# for 语句
# 格式:
# for 变量名 in 集合：
#         语句

# for i in [1,2,3,4,5]:
#     print(num)


# range() 列表生成器
# 生成数列
"""
    range(stop) -> range object
    range(start, stop[, step]) -> range object

    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
 """

# for i in range(1,10,2):
#     print(i)

# 同时遍历下标和元素
"""
enumerate(iterable[, start]) -> iterator for index, value of iterable

Return an enumerate object.  iterable must be another object that supports
iteration.  The enumerate object yields pairs containing a count (from
start, which defaults to zero) and a value yielded by the iterable argument.
enumerate is useful for obtaining an indexed list:
    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
# for index, val in enumerate([4,5,6,7,8]):
#     print(index,val)

# sum = 0
#
# for num in range(1,101):
#     sum += num
# print(sum)



# break   跳出while, for循环，只能跳出离他最近的一层循环
# continue 跳过当前循环的剩余语句，然后继续执行下一次循环



"""
Turtle 是一个简单的绘图工具

提供一个小海龟，可以将它理解为一个机器人，只能听懂有限的命令

绘制窗口的原点（0，0）在正中间，默认海龟的方向是向右


运动命令
forward(d)      向前移动d距离
backward(d)      向后移动d距离
right(d)        向右转动d度
goto(x,y)       移动到坐标为（x,y）的位置
speed(speed)    笔画绘制的速度

笔画控制命令
up()        笔画抬起，在移动时不会绘图
down()        笔画落下，在移动时不会绘图

"""

import turtle

turtle.forward(100)


turtle.done()



























