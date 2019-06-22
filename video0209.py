#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: tets3.py
#@time: 2019/2/10 0:12
#@desc: comment,print,input



# 打印输出一条字符串
print("Hello world!")

# 打印多条字符串，逗号分隔，遇到逗号输出空格
print("Hello world!","My name is huhao.")

# 输出数字
print(18)
print(10 + 8)
print("10+8 =", 10 + 8)

#input() 从外部获取变量的值
#等待输入(阻塞)

age = input("please input your age: ")
print("age =", age)

# 加法
# 输出错误结果：例如num1 = 3,num2 = 4,则输出34
num1 = input("please input a number: ")
num2 = input("please input a number: ")

print("num1 + num2 = ", num1 + num2)
#正确算法
num1 = int(input("please input a number: "))
num2 = int(input("please input a number: "))

print("num1 + num2 = ", num1 + num2)

