#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: list_sort.py
#@time: 2019/6/6 17:33
#@Ducument：https://www.python.org/doc/
#@desc:

def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # list2 = list1.sort()
    # list.sort()给列表对象发出排序消息直接在列表对象上进行排序，而列表又不能整体赋值，详见list_slice.py
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list2 = sorted(list1)
    print("list2 = ", list2)
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print("list3 = ", list3)
    print("list4 = ", list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort()
    print(list1)




if __name__ == "__main__":
    main()






