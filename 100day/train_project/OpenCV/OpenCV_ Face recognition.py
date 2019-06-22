#!/usr/bin/env python
# encoding: utf-8

# @author: huhao
# @Software : PyCharm
# @file: OpenCV_ Face recognition.py
# @time: 2019/6/11 8:58
# @Ducument：https://www.python.org/doc/
# @desc:

import numpy as np
import cv2

# 图片中只有一张人脸
# sj = cv2.imread('./img/SteveJobs1.jpg')

# 图片中有多张人脸
# sj = cv2.imread('./img/SteveJobs5.jpg')

# sj = cv2.imread('./img/SteveJobs6.jpg')
'''
识别出错，调整detector.detectMultiScale()里的参数
'''

# 物理学家大会
sj_raw = cv2.imread('./img/physics.jpg')
print(np.shape(sj_raw))

# resize图片尺寸
sj = cv2.resize(sj_raw,dsize=(1080, 640))


# 人脸数据，级联分类器，给定人脸特征数据，返回可以识别人脸的对象
detector = cv2.CascadeClassifier('./feature_data/haarcascade_frontalface_default.xml')

# 识别图片的人脸区域
# 当一张图片人脸较多，可能不能够识别出来大部分的人脸，这时可以通过resize图片的尺寸（主要放大），修改scaleFactor，minNeighbors参数
face_zone = detector.detectMultiScale(sj, scaleFactor=1.1, minNeighbors=6, minSize=(25, 25), maxSize=(150, 150))
print(face_zone)
'''
[x, y, w, h]: 左上角横坐标，左上角纵坐标，宽度，高度
[[135  59 272 272]]
'''

# 在图片中绘制人脸区域
for x, y, w, h in face_zone:
    cv2.rectangle(sj, pt1=(x, y), pt2=(x + w, y + h), color=[0, 255, 0], thickness=2)    # color: BGR
cv2.imshow('sj', sj)
cv2.waitKey(0)
cv2.destroyAllWindows()

