# @author: huhao
# @file: regular_expression2.py
# @time: 2019/7/19 14:39
# @Document：https://www.python.org/doc/
# @desc:

'''
从一段文字中提取出国内手机号码
电信号段：133/153/180/181/189/177
联通号段：130/131/132/155/185/186/145/176
移动号段：134/135/136/137/138/139/150/151/151/157/158/159/182/184/187/188/147/178

'''

import re

def main():

    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    # re.compile()      编译正则表达式返回正则表达式对象
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''

    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print("###################")

    # 通过迭代器取出匹配对象并返回匹配的内容
    for temp in re.finditer(pattern,sentence):
        print(temp.group())     # 正则表达式中，group（）用来提出分组截获的字符串，（）用来分组
    print("###################")

    # 通过search函数指定搜索位置并获得匹配的内容
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())

if __name__ == '__main__':
    main()
