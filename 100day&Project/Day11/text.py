# @author: huhao
# @file: text.py
# @time: 2019/7/17 17:02
# @Document：https://www.python.org/doc/
# @desc:

import time

def main():
    f = None

    '''
    try:
        f = open("致橡树.txt", "r", encoding="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("无法打开指定文件！")
    except LookupError:
        print("指定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")
    finally:
        if f:
            f.close()
    '''

    try:
        # # 一次性读取整个文件
        # with open("致橡树.txt", "r", encoding="utf-8") as f:
        #     print(f.read())
        #
        # # for-in 循环
        # with open("致橡树.txt", "r", encoding="utf-8") as f:
        #     for line in f:
        #         print(line, end="\n")
        #         time.sleep(0.5)

        # 按行读取文件到列表中
        with open("致橡树.txt", "r", encoding="utf-8") as f:
            line = f.readlines()
            print(line)

    except FileNotFoundError:
        print("无法打开指定文件！")
    except LookupError:
        print("指定了未知的编码！")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")

if __name__ == '__main__':
    main()