#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video0210.py
#@time: 2019/2/10 13:19
#@Ducument：https://www.python.org/doc/
#@desc:


# 导入math库

import math
import random



# 数字类型转换
print(int(1.1))
print(float(3))
print(int(float("12.3")))

num1 = 3
num2 = 4
(num1>num2)

# round(number[, ndigits])
# Return number rounded to ndigits precision after the decimal point.
# If ndigits is omitted or is None, it returns the nearest integer to its input.
print(round(4.23243,2))
print(round(4.23243))

#随机数
# 1
print(random.choice([1,2,3,4,"huhao"]))
print(random.choice(range(5)))  #range(5) == [0,1,2,3,4]
print(random.choice("huhao"))   #"huhao" = ["h","u""h","a","o"]

#产生一个1~100的随机数
print(random.choice(range(101)))    #会产生0的随机数，不合题意
print(random.choice(range(100))+1)

#randrange([start],stop,[step])
#stop 不包含在内
print(random.randrange(1,100,2))

#random.random()
#return the next random floating point number in the range [0.0,1.0)
print(random.random())

#random。shuffle(list)
#shuffle the sequence in place
list = [1,2,3,4,5]
random.shuffle(list)
print(list)

#random.uniform(a,b)
#return a random floating point number N, N = a+(b-a)*random()
print(random.uniform(1,10))

