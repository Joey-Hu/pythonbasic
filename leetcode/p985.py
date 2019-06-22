#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: test.py
#@time: 2019/2/16 20:01
#@Ducument：https://www.python.org/doc/
#@desc:

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

Sum = 0
for x in A:
    if x % 2 == 0:
        Sum += x
ans = []
'''
1.先将A[]中的偶数求和
2.循环：
    当A[k]是偶数时，sum-A[k]，A[k]加上x，重新计算偶数和并append到ans[]中
    当A[k]是奇数时，A[k]加上x，重新计算偶数和并append到ans[]中
3.输出ans[]
'''
for x, k in queries:
    if A[k] % 2 == 0:
        Sum -= A[k]
    A[k] += x
    if A[k] % 2 == 0:
        Sum += A[k]
    ans.append(Sum)

print(ans)