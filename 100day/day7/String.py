#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: String.py
# @time: 2019/6/6 15:24
# @Ducument：https://www.python.org/doc/
# @desc:

def main():
    str = "huhao is a good guy!"
    # 通过len函数计算字符串的长度
    print(len(str))  # 20
    # 获得字符串首字母大写的拷贝
    print(str.capitalize())  # Huhao is a good guy!
    # 获得字符串变大写后的拷贝
    print(str.upper())  # HUHAO IS A GOOD GUY!
    # 从字符串中查找子串所在位置
    print(str.find('ao'))  # 3
    print(str.find('fuck'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str.index('ao'))
    # print(str.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str.startswith('hu'))  # True
    # 检查字符串是否以指定的字符串结尾
    print(str.endswith('y!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str.center(50, '*'))  # ***************huhao is a good guy!***************
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str.rjust(50, '$'))  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$huhao is a good guy!
    str2 = "abc123456"
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])      # c12
    print(str2[2:])      # c123456
    print(str2[2::2])    # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())


if __name__ == '__main__':  # name两端是双下划线
    main()
