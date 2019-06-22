#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video0211.py
#@time: 2019/2/11 17:14
#@Ducument：https://www.python.org/doc/
#@desc: 水仙花数，位运算，字符串运算


#水仙花数

# num = int(input("请输入一个数: "))
#
# gewei = num % 10
# shiwei = (num//10) % 10
# baiwei = num // 100
#
# if gewei ** 3 + shiwei ** 3 + baiwei ** 3 ==num:
#     print(num,"是水仙花数！")
# else:
#     print(num,"不是水仙花数！")

# << 左移运算符
# a<<b a向左移动b位

# print(2<<2)
#
# # >> 右移运算符
# # a>>b a向右移b位
#
# print(8>>2)


# 字符串运算
# 字符串连接

# str1 = "huhao is a "
# str2 = "nice guy!"
# str3 = str1 + str2
# print(str1)
# print(str2)
# print(str3)


# 访问字符串中的某一个字符
# 通过索引下标访问，索引从0开始

# str1 = "huhao is a nice guy!"
# print(str1[3])

# 截取字符串的一部分
# str[start,end] start是目标字符的下标，end是目标字符的后一位的下标
# str1 = "huhao is a nice guy!"
# str2 = str1[5:15]
# print(str2)


# 判断一段字符是否在字符串里
# in, not in

# str = "huhao is a nice guy!"
# print("huhao" in str)
# print("huhao" not in str)



# eval(str,)
# 将字符串当作表达式并返回其计算值

# print(eval("123"))
# print(eval("12+3"))


#len()计算字符串长度
# print(len("huhao is a nice guy!"))



# center(width,[fillchar]) 居中显示
# ljust(width,[fillchar]) 左对齐
# rjust(width,[fillchar]) 右对齐

# str = "huhao is a nice guy!"
# print(str.center(50,"#"))
# print(str.ljust(50,"*"))
# print(str.rjust(50,"*"))


# str.count(substring [,start [end]])
# return the number of non-overlapping occurrences of substring in the range [start,end]

# str = "huhao is a nice guy and a good student!"
# print(str.count("a",5,len(str)))




# str.find(substring [,start [end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

str = "huhao is a nice guy and a good student!"
# print(str.find("guy",5,len(str)))
# print(str.find("no this word",5,len(str)))


# str.spilt(mark = ""，maxsplit)
# 以mark作为分隔符截取字符串，max指代的是截取段的数量
# print(str.split(" "))


# 编码
# encode(encoding="utf-8", errors= "strict")


# isalpha() 如果字符串中至少有一个字符且所有字符都是字母，则返回True,否则返回False
# isalnum() 如果字符串中至少有一个字符且所有字符都是字母或数字，则返回True,否则返回False
# isupper() 如果字符串中至少有一个英文字符且所有字符都是大写英文字母，则返回True,否则返回False
# islower() 如果字符串中至少有一个英文字符且所有字符都是小写英文字母，则返回True,否则返回False
# isdigit() 如果字符串中只包含数字，则返回True, 否则返回False
# isspace() 如果字符串中只包含空格，则返回True, 否则返回False






