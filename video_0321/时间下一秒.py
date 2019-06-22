#!/usr/bin/env python
# encoding: utf-8

#@author: huhao
#@Software : PyCharm
#@file: video_0321.py
#@time: 2019/3/21 9:19
#@Ducument：https://www.python.org/doc/
#@desc:


'''

练习：输出时间下一秒

'''
timestr = input()   #格式12:23:23

# 分割时间，取出时，分，秒

time_split = timestr.split(":")

'''
print(time_split)

output:
C:\Python35-32\python.exe "D:/Desktop/python/python basics/video_0321.py"
12:23:23
['12', '23', '23']

Process finished with exit code 0

'''

# 切割
h = int(time_split[0])
m = int(time_split[1])
s = int(time_split[2])

# 秒加一
s += 1


if  s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0

print("%.2d:%.2d:%.2d" %(h,m,s))