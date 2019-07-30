# @author: huhao
# @file: str3.py
# @time: 2019/7/24 7:30
# @Document：https://www.python.org/doc/
# @desc:

'''实现字符串倒置'''


from io import StringIO


def reverse_str1(str):
    return str[::-1]

def reverse_str2(str):
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]


def main():
    str = "Notepad++ is a tool."
    # print(reverse_str1(str))
    # print(str)
    print(reverse_str2(str))
    print(str)


if __name__ == '__main__':
    main()