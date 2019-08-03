#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: LIST.py
# @time: 2019/6/6 15:49
# @Ducument：https://www.python.org/doc/
# @desc:

def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ["hello"] * 5
    print(list2)
    # 计算列表长度
    print(len(list1))
    # 下标(索引)运算
    print(list1[0])
    print(list1[4])
    # print(list1[5])     # list index out of range
    print(list1[-1])
    print(list1[-2])
    # 修改元素
    list1[2] = 300
    print(list1)
    # 添加元素  append、insert、+=
    list1.append(200)       # 末尾插入[1, 3, 300, 7, 100, 200]
    list1.insert(1, 400)        # 按索引插入[1, 3, 300, 7, 100, 200]
    list1 +=[1000, 2000]        # 末尾插入[1, 400, 3, 300, 7, 100, 200, 1000, 2000]
    print(list1)
    # 删除元素  remove、clear
    list1.remove(300)     # 删除值是3的元素
    print(list1)
    del list1[0]        # 删除下标为0的元素
    print(list1)
    list1.clear()       # 清空列表
    print(list1)




if __name__ == "__main__":
    main()
