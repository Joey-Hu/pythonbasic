# @author: huhao
# @file: is_prime_file.py
# @time: 2019/7/18 14:54
# @Document：https://www.python.org/doc/
# @desc:如何将1-9999直接的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）。

import math


def is_prime(num):
    assert num > 0  # 检查条件，不符合就终止程序
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    fs_list = ['a.txt', 'b.txt', 'c.txt']
    try:
        a = open("./is_prime/a.txt", 'w', encoding='utf-8')
        b = open("./is_prime/b.txt", 'w', encoding='utf-8')
        c = open("./is_prime/c.txt", 'w', encoding='utf-8')

        for i in range(1, 10000):
            if is_prime(i):
                if i < 100:
                    a.write(str(i) + "\n")
                elif i < 999:
                   b.write(str(i) + "\n")
                else:
                    c.write(str(i) + "\n")
        a.close()
        b.close()
        c.close()

    except IOError as ex:
        print(ex)
        print("写文件时发生错误")
    print("DONE!!!")

if __name__ == '__main__':
    main()