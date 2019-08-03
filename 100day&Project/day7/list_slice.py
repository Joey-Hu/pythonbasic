#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: list_slice.py
# @time: 2019/6/6 17:07
# @Ducument：https://www.python.org/doc/
# @desc:

def main():
    fruits = ["grape", "apple", "strawberry", "waxberry"]
    fruits += ["pitaya", "pear", "mango"]
    # 循环遍历
    for fruit in fruits:
        print(fruit.title(), end=" ")  # 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruit3 = fruits     # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == "__main__":
    main()
