#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: String.py
#@time: 2019/5/5 12:19
#@Ducument：https://www.python.org/doc/
#@desc: 字符串常用操作

str = "hello, world!"

print("字符串长度：", len(str))
print("单词首字母大写：", str.title())
print("字符串变大写：", str.upper())
# str1 = str.upper()
print("判断字符串是否大写：", str.isupper())
print("判断字符串是否以hello开头：", str.startswith("hello"))
print("判断字符串是否以hello结尾：", str.endswith("hello"))

str2 = '- \u9a86\u660a'
str3 = str.title() + ' ' + str2.lower()
print(str3)

