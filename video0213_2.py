#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video2013_2.py
#@time: 2019/2/13 23:55
#@Ducument：https://www.python.org/doc/
#@desc:



# 字典
# map type 映射类型
# 使用键值对(key-value)存储数据，具有极快的查找速度
# 字典是无序的
# key的特性：
# 1. 字典的key必须唯一
# 2. key必须是不可变对象，字符串、整数等都是不可变的，都可以作为key，list是可变的，不能作为key


# 元素访问  字典名[key]
# print(dict1["tom"])
# Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
# print(dict1.get("huhao"))

# 添加元素
# dict1["huhao"] = 330
# print(dict1)


# 修改元素
# 因为一个key只能对应一个value,所以对一个key重新赋值就是修改元素
# dict1["tom"] = 100
# print(dict1)


# 删除元素
# print(dict1.pop("tom"))
# print(dict1)


# 遍历

# for key in dict1:
#     print(key,dict1[key])
#
# for value in dict1.values():
#     print(value)
#
# for key,value in dict1.items():
#     print(key,value)

# dictionary和list比较
# 1.查找和插入的速度极快，不会随着key-value的增加而变慢
# 2.需要占用大量的内存，内存浪费多

'''
# 练习：统计一段文本中单词出现的频率
# 改进：1. 读取文本文件  2. 有一些单词有连词符，明明下文China出现了两次（China,China）,但结果显示只出现了一次
# str = "A delegation of nearly 50 people from the US state of Iowa started their 10-day visit to China on Sunday and a groundbreaking for a China-US Friendship Demonstration Farm, believed to be the first of its kind, is set for Saturday."
str = input("please input a string:")
dict2 = {}

SplitedStr = str.split(" ")     # 以空格切割字符串
# print(SplitedStr)

for value in SplitedStr:
    if value not in dict2.keys():
        dict2[value] = 1
    else:
        dict2[value] += 1

for k,v in dict2.items():
    print(k + ":",v)
'''


'''
dict1 = {"tom": 60, "lilei": 70, "hanmeimei": 100, "Joey": 90}

print(dict1["huhao"])   #不存在该值，报错
ret = print(dict1.get("huhao"))   #不报错，返回None
if ret == None:
    op1;
else:
    op2

'''



'''
统计某个单词在字符串中出现的次数

w = input()

str = "A delegation of nearly 50 people from the US state of Iowa started their 10-day visit to China on Sunday and a groundbreaking for a China-US Friendship Demonstration Farm, believed to be the first of its kind, is set for Saturday"

print(str.count(w))

'''

w = input()

str = "A delegation of nearly 50 people from the US state of Iowa started their 10-day visit to China on Sunday and a groundbreaking for a China-US Friendship Demonstration Farm, believed to be the first of its kind, is set for Saturday"





























