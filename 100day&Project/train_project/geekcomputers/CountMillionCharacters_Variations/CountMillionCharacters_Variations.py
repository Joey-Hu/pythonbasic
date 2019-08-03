#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: CountMillionCharacters_Variations.py
# @time: 2019/6/27 18:48
# @Ducument：https://www.python.org/doc/
# @desc: 统计一个文件中各个英文字符的数量
# 识别txt文件，不能识别docx文件


try:
    input = input
except NameError:
    pass


def count_chas(filename):
    count = {}

    with open(filename,encoding='UTF-8') as info:    # inputFile Replaced with filename
        readfile = info.read()
        for character in readfile.upper():  # 为什么要大写？？  把大写去掉之后也可以，能区分大小写字符
            count[character] = count.get(character, 0) + 1

        return count


def main():
    is_exist = True
    # Try to open file if exist else raise exception and try again

    while(is_exist):
        try:
            inputFile = input("File Name / (0)exit : ").strip()     # Return a copy of the string S with leading and trailing whitespace removed.
            if inputFile == 0:
                break
            print(count_chas(inputFile))
        except FileNotFoundError:
            print('File not found...Try again!')

if __name__ == '__main__':
    main()