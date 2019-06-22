#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video0211_1.py
#@time: 2019/2/11 21:29
#@Ducument：https://www.python.org/doc/
#@desc:


# while循环

# count = 0
# while (count<10):
#     print("This index is:", count)
#     # count + 1     错误，没有将加一后的值赋值给count，无限循环
#     count += 1


# 计算1+2+3+...+100

# num = 1
# sum = 0
# while num<=100:
#     sum += num
#     num = num +1
# print("sum =",sum)



# 判断一个数是不是质数

# num = int(input())
# index = 2
#
# if num == 2:
#     print("it's not a prime")
#
# while index < num:
#     if num % index == 0:
#         print("it's not a prime")
#         break
#     index = index + 1
#
# if index == num:
#     print("it's a prime")



# 将字符串里的数字加起来求和

# str = input()
# index = 0
# sum = 0
#
# while index < len(str):
# # if str[index] >= "0" and str[index] <= "9" and index < len(str):
#     if str[index] >= "0" and str[index] <= "9":
#         sum += int(str[index])
#     index += 1
#
# print(sum)



#比较字符串大小
# 逐个字符比较
# str1 = input()
# str2 = input()
# index = 0
#
# min = min(len(str1),len(str2))
# while index < min:
#     if str1[index] > str2[index]:
#         print("str1 > str2")
#         break
#
#     if str1[index] < str2[index]:
#         print("str1 < str2")
#         break
#
#     else:
#         index += 1
## 接着判断字符长度。。。

#直接比较

str1 = input()
str2 = input()

if str1 >= str2:
    print("str1 > str2")
# .......


# 空值: none, python里的一个特殊值







