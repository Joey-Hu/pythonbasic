#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: for.py
#@time: 2019/5/9 16:18
#@Ducument：https://www.python.org/doc/
#@desc:


'''
for循环

sum = 0
#for x in range(101):    # 可以产生一个0到100的整数序列
# for x in range(1,100):  # 可以产生一个1到99的整数序列
for x in range(1,100,2):    # 可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量
    sum += x
print(sum)


'''

from random import randint

answer = randint(1,100)
counter = 0;

while True:

    counter += 1
    number = int(input("please enter a number:"))
    if number < answer:
        print("猜小了！")
    elif number > answer:
        print("猜大了！")
    else:
        print("猜对了！")
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
