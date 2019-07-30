#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: OpenCV1.py
# @time: 2019/6/11 7:50
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np

import cv2  # openCV是C++写的语言，python调用CV2中的方法

sj1 = cv2.imread('./img/SteveJobs1.jpg')    # cv2读取图片的路径中不能包含中文，否则return none
print(sj1)

print(sj1.shape)
'''
(375, 600, 3)
'''


# 1. 显示图片
cv2.imshow('sj', sj1)
# 等待键盘的输入任意字符关闭窗口，单位毫秒，如果是0，无限等待
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2. 颜色转化
# BGR cv2读取图片，颜色通道是BGR
# PIL 读取图片，颜色通道是RGB
sj1_gray = cv2.cvtColor(sj1, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('sj_gray', sj1_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 3. 保存图片
cv2.imwrite('./img/SteveJobs1_gray.jpg',sj1_gray)


# 4. 图片尺寸
sj1_2size = cv2.resize(sj1, dsize=(185, 300))
cv2.imshow('sj1_2size', sj1_2size)
# 当且仅当键盘输入“q”时，退出
while True:
    if ord('q') == cv2.waitKey(0):  # """ ord(c): Return the Unicode code point for a one-character string. """
        break
cv2.destroyAllWindows()






