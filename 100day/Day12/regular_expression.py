# @author: huhao
# @file: regular_expression.py
# @time: 2019/7/19 8:08
# @Document：https://www.python.org/doc/
# @desc:

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    user_name = input("请输入用户名：")
    qq_num = input("输入qq号：")

    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', user_name)
    if not m1:
        print("请输入有效用户名！")
    m2 = re.match(r'^[1-9]\d{4,11}$', qq_num)
    if not m2:
        print("请输入有效qq号！")
    if m1 and m2:
        print("你的信息是有效的！")


if __name__ == '__main__':
    main()
