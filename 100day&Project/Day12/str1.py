# @author: huhao
# @file: str1.py
# @time: 2019/7/23 7:06
# @Document：https://www.python.org/doc/
# @desc:

'''替换字符串中的不良内容'''


import re


def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', "*", sentence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    main()